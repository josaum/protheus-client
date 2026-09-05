//! Decode a TTALK response page into an Arrow `RecordBatch` and validate every
//! row against the response's item schema — reporting, never dropping, what
//! does not fit. No DOM is built: the rows are sliced out of the raw bytes,
//! decoded by `arrow-json`'s tape decoder, and the schema's constraints
//! (required, enum, length, pattern, range, date formats, declared type) are
//! checked on the Arrow columns.
//!
//! The Arrow schema is derived from the JSON Schema (string/enum → Utf8,
//! integer → Int64, number → Float64, boolean → Boolean, object → Struct,
//! array → List). Live Protheus data violates its schema often enough
//! (`"5,2"` in a number field) that a primitive field which cannot be decoded
//! as declared is *demoted* to Utf8 for the rest of the decoder's life, so
//! column types stay stable across pages once settled; rows whose values do
//! not parse as the declared type are then reported as type violations.

use crate::json_scan::{array_is_empty, array_to_record_stream, locate_rows};
use crate::Error;
use arrow_array::cast::AsArray;
use arrow_array::types::{Float64Type, Int64Type};
use arrow_array::{Array, ArrayRef, RecordBatch};
use arrow_json::ReaderBuilder;
use arrow_schema::{DataType, Field, Fields, Schema, SchemaRef};
use regex::Regex;
use serde::Serialize;
use serde_json::{Map, Value};
use std::borrow::Cow;
use std::sync::{Arc, LazyLock, Mutex};

static FIELD_IN_ERROR: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"field '([^']+)'").unwrap());
static DATE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$").unwrap());
static DATE_TIME: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])[Tt ]([01]\d|2[0-3]):[0-5]\d:[0-5]\d(\.\d+)?([Zz]|[+-]([01]\d|2[0-3]):[0-5]\d)$").unwrap()
});
const MAX_DEMOTIONS_PER_PAGE: usize = 32;
/// Rows per flush of the tape decoder; pages larger than this are concatenated.
const BATCH_SIZE: usize = 8192;

#[derive(Debug, Clone, Serialize)]
pub struct Violation {
    pub row: usize,
    pub path: String,
    pub message: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct FieldInfo {
    pub name: String,
    #[serde(rename = "type")]
    pub type_: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct DecodeReport {
    pub rows: usize,
    pub invalid_rows: usize,
    pub violations: Vec<Violation>,
    pub violations_truncated: bool,
    pub demoted_fields: Vec<String>,
    pub has_next: Option<bool>,
    pub fields: Vec<FieldInfo>,
}

#[derive(Debug, Clone, Copy, PartialEq)]
enum Declared {
    String,
    Integer,
    Number,
    Boolean,
    Object,
    Array,
    Any,
}

#[derive(Debug, Clone, Copy, PartialEq)]
enum Format {
    Date,
    DateTime,
}

/// Constraints of one schema node, aligned with the Arrow field derived from it.
#[derive(Debug)]
struct Rules {
    declared: Declared,
    required: bool,
    enum_values: Option<Vec<String>>,
    min_len: Option<usize>,
    max_len: Option<usize>,
    pattern: Option<Regex>,
    minimum: Option<f64>,
    maximum: Option<f64>,
    exclusive_min: bool,
    exclusive_max: bool,
    format: Option<Format>,
    fields: Vec<(String, Rules)>,
    item: Option<Box<Rules>>,
}

/// Follow `$ref`s and merge `allOf` parts into one object schema.
fn resolve_object(bundled: &Value, schema: &Value, depth: usize) -> Map<String, Value> {
    if depth > 16 {
        return Map::new();
    }
    if let Some(reference) = schema.get("$ref").and_then(Value::as_str) {
        let name = reference.rsplit('/').next().unwrap_or("");
        return match bundled["components"]["schemas"].get(name) {
            Some(target) => resolve_object(bundled, target, depth + 1),
            None => Map::new(),
        };
    }
    let mut out = schema.as_object().cloned().unwrap_or_default();
    if let Some(Value::Array(parts)) = out.get("allOf").cloned() {
        let mut props = Map::new();
        let mut required: Vec<Value> = Vec::new();
        for part in parts {
            let resolved = resolve_object(bundled, &part, depth + 1);
            if let Some(Value::Object(p)) = resolved.get("properties") {
                for (k, v) in p {
                    props.insert(k.clone(), v.clone());
                }
            }
            if let Some(Value::Array(r)) = resolved.get("required") {
                required.extend(r.iter().cloned());
            }
            for (k, v) in resolved {
                if !matches!(k.as_str(), "properties" | "allOf" | "required")
                    && !out.contains_key(&k)
                {
                    out.insert(k, v);
                }
            }
        }
        out.remove("allOf");
        out.insert("properties".to_string(), Value::Object(props));
        if !required.is_empty() {
            out.insert("required".to_string(), Value::Array(required));
        }
        out.entry("type").or_insert(Value::String("object".into()));
    }
    out
}

fn declared_type(schema: &Map<String, Value>) -> Declared {
    let name = match schema.get("type") {
        Some(Value::Array(items)) => items
            .iter()
            .filter_map(Value::as_str)
            .find(|s| *s != "null"),
        Some(Value::String(s)) => Some(s.as_str()),
        _ => None,
    };
    if name == Some("object") || schema.contains_key("properties") {
        return Declared::Object;
    }
    match name {
        Some("string") => Declared::String,
        Some("integer") => Declared::Integer,
        Some("number") => Declared::Number,
        Some("boolean") => Declared::Boolean,
        Some("array") => Declared::Array,
        _ => Declared::Any,
    }
}

fn render(v: &Value) -> String {
    match v {
        Value::String(s) => s.clone(),
        other => other.to_string(),
    }
}

/// Build the Arrow type and the rules for one schema node, in lockstep.
fn plan(bundled: &Value, schema: &Value, depth: usize) -> (DataType, Rules) {
    let resolved = resolve_object(bundled, schema, 0);
    let declared = if depth > 16 {
        Declared::Any
    } else {
        declared_type(&resolved)
    };
    let mut rules = Rules {
        declared,
        required: false,
        enum_values: resolved
            .get("enum")
            .and_then(Value::as_array)
            .map(|vals| vals.iter().map(render).collect()),
        min_len: resolved
            .get("minLength")
            .and_then(Value::as_u64)
            .map(|v| v as usize),
        max_len: resolved
            .get("maxLength")
            .and_then(Value::as_u64)
            .map(|v| v as usize),
        pattern: resolved
            .get("pattern")
            .and_then(Value::as_str)
            .and_then(|p| Regex::new(p).ok()),
        minimum: resolved.get("minimum").and_then(Value::as_f64),
        maximum: resolved.get("maximum").and_then(Value::as_f64),
        exclusive_min: resolved
            .get("exclusiveMinimum")
            .and_then(Value::as_bool)
            .unwrap_or(false),
        exclusive_max: resolved
            .get("exclusiveMaximum")
            .and_then(Value::as_bool)
            .unwrap_or(false),
        format: match resolved.get("format").and_then(Value::as_str) {
            Some("date") => Some(Format::Date),
            Some("date-time") => Some(Format::DateTime),
            _ => None,
        },
        fields: Vec::new(),
        item: None,
    };
    if rules.enum_values.is_some() && declared != Declared::Object && declared != Declared::Array {
        rules.declared = Declared::String;
        return (DataType::Utf8, rules);
    }
    match declared {
        Declared::Object => {
            let required: Vec<&str> = resolved
                .get("required")
                .and_then(Value::as_array)
                .map(|r| r.iter().filter_map(Value::as_str).collect())
                .unwrap_or_default();
            let mut fields = Vec::new();
            if let Some(Value::Object(props)) = resolved.get("properties") {
                for (name, sub) in props {
                    let (dt, mut child) = plan(bundled, sub, depth + 1);
                    child.required = required.contains(&name.as_str());
                    fields.push(Field::new(name, dt, true));
                    rules.fields.push((name.clone(), child));
                }
            }
            (DataType::Struct(Fields::from(fields)), rules)
        }
        Declared::Array => {
            let (dt, child) = resolved
                .get("items")
                .map(|s| plan(bundled, s, depth + 1))
                .unwrap_or((
                    DataType::Utf8,
                    Rules {
                        ..leaf(Declared::Any)
                    },
                ));
            rules.item = Some(Box::new(child));
            (
                DataType::List(Arc::new(Field::new("item", dt, true))),
                rules,
            )
        }
        Declared::Integer => (DataType::Int64, rules),
        Declared::Number => (DataType::Float64, rules),
        Declared::Boolean => (DataType::Boolean, rules),
        Declared::String | Declared::Any => (DataType::Utf8, rules),
    }
}

fn leaf(declared: Declared) -> Rules {
    Rules {
        declared,
        required: false,
        enum_values: None,
        min_len: None,
        max_len: None,
        pattern: None,
        minimum: None,
        maximum: None,
        exclusive_min: false,
        exclusive_max: false,
        format: None,
        fields: Vec::new(),
        item: None,
    }
}

/// Demote the primitive leaf at `path` to Utf8; `None` when nothing changed.
fn demote(fields: &Fields, path: &[String]) -> Option<Fields> {
    let (head, rest) = path.split_first()?;
    let mut out: Vec<Field> = Vec::with_capacity(fields.len());
    let mut changed = false;
    for f in fields.iter() {
        if f.name() != head {
            out.push(f.as_ref().clone());
            continue;
        }
        let replaced = match (rest.is_empty(), f.data_type()) {
            (false, DataType::Struct(inner)) => {
                demote(inner, rest).map(|nf| Field::new(f.name(), DataType::Struct(nf), true))
            }
            (false, DataType::List(item)) => match item.data_type() {
                DataType::Struct(inner) => demote(inner, rest).map(|nf| {
                    Field::new(
                        f.name(),
                        DataType::List(Arc::new(Field::new("item", DataType::Struct(nf), true))),
                        true,
                    )
                }),
                _ => None,
            },
            (true, DataType::Int64 | DataType::Float64 | DataType::Boolean) => {
                Some(Field::new(f.name(), DataType::Utf8, true))
            }
            (true, DataType::List(item))
                if matches!(
                    item.data_type(),
                    DataType::Int64 | DataType::Float64 | DataType::Boolean
                ) =>
            {
                Some(Field::new(
                    f.name(),
                    DataType::List(Arc::new(Field::new("item", DataType::Utf8, true))),
                    true,
                ))
            }
            _ => None,
        };
        match replaced {
            Some(nf) => {
                out.push(nf);
                changed = true;
            }
            None => out.push(f.as_ref().clone()),
        }
    }
    changed.then(|| Fields::from(out))
}

fn describe(fields: &Fields) -> Vec<FieldInfo> {
    fields
        .iter()
        .map(|f| FieldInfo {
            name: f.name().clone(),
            type_: format!("{}", f.data_type()),
        })
        .collect()
}

// ------------------------------------------------------------- validation
enum Prefix {
    Shared(String),
    Each(Vec<String>),
}

impl Prefix {
    fn at(&self, i: usize) -> Cow<'_, str> {
        match self {
            Prefix::Shared(s) => Cow::Borrowed(s),
            Prefix::Each(v) => Cow::Borrowed(&v[i]),
        }
    }
}

struct Ctx {
    /// Top-level row for each element of the array being validated (None = skip).
    rows: Vec<Option<usize>>,
    prefix: Prefix,
}

struct Collector<'a> {
    max: usize,
    report: &'a mut DecodeReport,
    invalid: Vec<bool>,
}

impl Collector<'_> {
    fn hit(&mut self, row: usize, path: String, message: String) {
        if !self.invalid[row] {
            self.invalid[row] = true;
            self.report.invalid_rows += 1;
        }
        if self.report.violations.len() < self.max {
            self.report
                .violations
                .push(Violation { row, path, message });
        } else {
            self.report.violations_truncated = true;
        }
    }
}

fn quote(s: &str) -> String {
    Value::String(s.to_string()).to_string()
}

fn check_string(rules: &Rules, s: &str) -> Option<String> {
    match rules.declared {
        Declared::Integer if s.parse::<i64>().is_err() => {
            return Some(format!("{} is not of type \"integer\"", quote(s)))
        }
        Declared::Number if s.parse::<f64>().is_err() => {
            return Some(format!("{} is not of type \"number\"", quote(s)))
        }
        Declared::Boolean if !matches!(s, "true" | "false") => {
            return Some(format!("{} is not of type \"boolean\"", quote(s)))
        }
        Declared::Integer | Declared::Number | Declared::Boolean => return None,
        _ => {}
    }
    if let Some(values) = &rules.enum_values {
        if !values.iter().any(|v| v == s) {
            let listed: Vec<String> = values.iter().map(|v| quote(v)).collect();
            return Some(format!(
                "{} is not one of [{}]",
                quote(s),
                listed.join(", ")
            ));
        }
    }
    let len = s.chars().count();
    if let Some(max) = rules.max_len {
        if len > max {
            return Some(format!("{} is longer than {max} characters", quote(s)));
        }
    }
    if let Some(min) = rules.min_len {
        if len < min {
            return Some(format!("{} is shorter than {min} characters", quote(s)));
        }
    }
    if let Some(re) = &rules.pattern {
        if !re.is_match(s) {
            return Some(format!(
                "{} does not match {}",
                quote(s),
                quote(re.as_str())
            ));
        }
    }
    match rules.format {
        Some(Format::Date) if !DATE.is_match(s) => Some(format!("{} is not a \"date\"", quote(s))),
        Some(Format::DateTime) if !DATE_TIME.is_match(s) => {
            Some(format!("{} is not a \"date-time\"", quote(s)))
        }
        _ => None,
    }
}

fn check_number(rules: &Rules, v: f64, rendered: impl Fn() -> String) -> Option<String> {
    if let Some(min) = rules.minimum {
        if v < min || (rules.exclusive_min && v == min) {
            return Some(format!("{} is less than the minimum of {min}", rendered()));
        }
    }
    if let Some(max) = rules.maximum {
        if v > max || (rules.exclusive_max && v == max) {
            return Some(format!(
                "{} is greater than the maximum of {max}",
                rendered()
            ));
        }
    }
    if let Some(values) = &rules.enum_values {
        let r = rendered();
        if !values.contains(&r) {
            return Some(format!("{r} is not one of [{}]", values.join(", ")));
        }
    }
    None
}

fn validate(rules: &Rules, array: &ArrayRef, ctx: &Ctx, name: &str, out: &mut Collector<'_>) {
    let n = array.len();
    let element_path = |i: usize| -> String { format!("{}/{name}", ctx.prefix.at(i)) };
    for i in 0..n {
        let Some(row) = ctx.rows[i] else { continue };
        if array.is_null(i) {
            if rules.required {
                out.hit(
                    row,
                    ctx.prefix.at(i).into_owned(),
                    format!("{} is a required property", quote(name)),
                );
            }
            continue;
        }
        let message = match array.data_type() {
            DataType::Utf8 => check_string(rules, array.as_string::<i32>().value(i)),
            DataType::Int64 => {
                let v = array.as_primitive::<Int64Type>().value(i);
                check_number(rules, v as f64, || v.to_string())
            }
            DataType::Float64 => {
                let v = array.as_primitive::<Float64Type>().value(i);
                check_number(rules, v, || v.to_string())
            }
            _ => None,
        };
        if let Some(message) = message {
            out.hit(row, element_path(i), message);
        }
    }
    match array.data_type() {
        DataType::Struct(_) => {
            let sa = array.as_struct();
            let rows: Vec<Option<usize>> = (0..n)
                .map(|i| if sa.is_null(i) { None } else { ctx.rows[i] })
                .collect();
            let prefix = match &ctx.prefix {
                Prefix::Shared(p) => Prefix::Shared(format!("{p}/{name}")),
                Prefix::Each(v) => Prefix::Each(v.iter().map(|p| format!("{p}/{name}")).collect()),
            };
            let child_ctx = Ctx { rows, prefix };
            for (idx, (child_name, child_rules)) in rules.fields.iter().enumerate() {
                if let Some(column) = sa.columns().get(idx) {
                    validate(child_rules, column, &child_ctx, child_name, out);
                }
            }
        }
        DataType::List(_) => {
            let Some(item_rules) = &rules.item else {
                return;
            };
            let la = array.as_list::<i32>();
            let offsets = la.offsets();
            let values = la.values();
            let mut rows = vec![None; values.len()];
            let mut paths = vec![String::new(); values.len()];
            for i in 0..n {
                if la.is_null(i) || ctx.rows[i].is_none() {
                    continue;
                }
                let (start, end) = (offsets[i] as usize, offsets[i + 1] as usize);
                let base = format!("{}/{name}", ctx.prefix.at(i));
                for (k, j) in (start..end).enumerate() {
                    rows[j] = ctx.rows[i];
                    paths[j] = format!("{base}/{k}");
                }
            }
            let child_ctx = Ctx {
                rows,
                prefix: Prefix::Each(paths),
            };
            // list items carry their own path; validate() appends `name`, so pass an empty one
            validate_items(item_rules, values, &child_ctx, out);
        }
        _ => {}
    }
}

/// Like [`validate`] for list elements, whose path is already complete.
fn validate_items(rules: &Rules, array: &ArrayRef, ctx: &Ctx, out: &mut Collector<'_>) {
    let n = array.len();
    for i in 0..n {
        let Some(row) = ctx.rows[i] else { continue };
        if array.is_null(i) {
            continue;
        }
        let message = match array.data_type() {
            DataType::Utf8 => check_string(rules, array.as_string::<i32>().value(i)),
            DataType::Int64 => {
                let v = array.as_primitive::<Int64Type>().value(i);
                check_number(rules, v as f64, || v.to_string())
            }
            DataType::Float64 => {
                let v = array.as_primitive::<Float64Type>().value(i);
                check_number(rules, v, || v.to_string())
            }
            _ => None,
        };
        if let Some(message) = message {
            out.hit(row, ctx.prefix.at(i).into_owned(), message);
        }
    }
    if let DataType::Struct(_) = array.data_type() {
        let sa = array.as_struct();
        let rows: Vec<Option<usize>> = (0..n)
            .map(|i| if sa.is_null(i) { None } else { ctx.rows[i] })
            .collect();
        let prefix = match &ctx.prefix {
            Prefix::Shared(p) => Prefix::Shared(p.clone()),
            Prefix::Each(v) => Prefix::Each(v.clone()),
        };
        let child_ctx = Ctx { rows, prefix };
        for (idx, (child_name, child_rules)) in rules.fields.iter().enumerate() {
            if let Some(column) = sa.columns().get(idx) {
                validate(child_rules, column, &child_ctx, child_name, out);
            }
        }
    }
}

// ---------------------------------------------------------------- decoder
pub struct Decoder {
    rules: Rules,
    schema: Mutex<SchemaRef>,
    demoted: Mutex<Vec<String>>,
    items_key: String,
    paged: bool,
    max_violations: usize,
}

impl Decoder {
    /// `schema_name` is the response component (e.g. `PagedCustomerVendors`);
    /// when it has an array property `items_key`, rows are its items and
    /// `hasNext` is reported, otherwise the whole body is one row.
    pub fn new(
        bundled: &Value,
        schema_name: &str,
        items_key: &str,
        max_violations: usize,
    ) -> Result<Self, Error> {
        let response = serde_json::json!({"$ref": format!("#/components/schemas/{schema_name}")});
        let resolved = resolve_object(bundled, &response, 0);
        if resolved.is_empty() {
            return Err(Error::Decode(format!("unknown schema {schema_name}")));
        }
        let items_schema = resolved
            .get("properties")
            .and_then(|p| p.get(items_key))
            .map(|s| resolve_object(bundled, s, 0))
            .filter(|s| declared_type(s) == Declared::Array)
            .and_then(|s| s.get("items").cloned());
        let paged = items_schema.is_some();
        let row_schema = items_schema.unwrap_or(response);
        let (row_type, rules) = plan(bundled, &row_schema, 0);
        let fields = match row_type {
            DataType::Struct(fields) => fields,
            other => Fields::from(vec![Field::new("value", other, true)]),
        };
        Ok(Self {
            rules,
            schema: Mutex::new(Arc::new(Schema::new(fields))),
            demoted: Mutex::new(Vec::new()),
            items_key: items_key.to_string(),
            paged,
            max_violations,
        })
    }

    pub fn schema(&self) -> SchemaRef {
        self.schema.lock().unwrap().clone()
    }

    pub fn decode(&self, body: &[u8]) -> Result<(RecordBatch, DecodeReport), Error> {
        let (stream, has_next) = if self.paged {
            let shape = locate_rows(body, &self.items_key).ok_or_else(|| {
                Error::Decode(format!("page has no array property {:?}", self.items_key))
            })?;
            let stream = if array_is_empty(shape.rows) {
                Vec::new()
            } else {
                array_to_record_stream(shape.rows)
            };
            (stream, shape.has_next)
        } else {
            (body.to_vec(), None)
        };
        let mut report = DecodeReport {
            rows: 0,
            invalid_rows: 0,
            violations: Vec::new(),
            violations_truncated: false,
            demoted_fields: Vec::new(),
            has_next,
            fields: Vec::new(),
        };
        let mut schema = self.schema();
        let batch = loop {
            match Self::to_batch(&schema, &stream) {
                Ok(batch) => break batch,
                Err(message) => {
                    let path: Vec<String> = FIELD_IN_ERROR
                        .captures_iter(&message)
                        .map(|c| c[1].to_string())
                        .collect();
                    let demoted = if report.demoted_fields.len() < MAX_DEMOTIONS_PER_PAGE {
                        demote(schema.fields(), &path)
                    } else {
                        None
                    };
                    let Some(fields) = demoted else {
                        return Err(Error::Decode(format!(
                            "cannot decode page as declared schema: {message}"
                        )));
                    };
                    schema = Arc::new(Schema::new(fields));
                    report.demoted_fields.push(path.join("."));
                }
            }
        };
        if !report.demoted_fields.is_empty() {
            *self.schema.lock().unwrap() = schema.clone();
            self.demoted
                .lock()
                .unwrap()
                .extend(report.demoted_fields.iter().cloned());
        }
        report.rows = batch.num_rows();
        {
            let mut out = Collector {
                max: self.max_violations,
                report: &mut report,
                invalid: vec![false; batch.num_rows()],
            };
            let ctx = Ctx {
                rows: (0..batch.num_rows()).map(Some).collect(),
                prefix: Prefix::Shared(String::new()),
            };
            let root: ArrayRef = Arc::new(arrow_array::StructArray::from(batch.clone()));
            validate_items(&self.rules, &root, &ctx, &mut out);
        }
        report.demoted_fields = self.demoted.lock().unwrap().clone();
        report.fields = describe(schema.fields());
        Ok((batch, report))
    }

    fn to_batch(schema: &SchemaRef, stream: &[u8]) -> Result<RecordBatch, String> {
        let mut decoder = ReaderBuilder::new(schema.clone())
            .with_coerce_primitive(true)
            .with_strict_mode(false)
            .with_batch_size(BATCH_SIZE)
            .build_decoder()
            .map_err(|e| e.to_string())?;
        let mut consumed = 0;
        let mut batches = Vec::new();
        while consumed < stream.len() {
            let read = decoder
                .decode(&stream[consumed..])
                .map_err(|e| e.to_string())?;
            if read == 0 {
                break;
            }
            consumed += read;
            if let Some(batch) = decoder.flush().map_err(|e| e.to_string())? {
                batches.push(batch);
            }
        }
        if let Some(batch) = decoder.flush().map_err(|e| e.to_string())? {
            batches.push(batch);
        }
        match batches.len() {
            0 => Ok(RecordBatch::new_empty(schema.clone())),
            1 => Ok(batches.pop().unwrap()),
            _ => arrow_select::concat::concat_batches(schema, &batches).map_err(|e| e.to_string()),
        }
    }

    /// Decode and serialise as an Arrow IPC stream.
    pub fn decode_ipc(&self, body: &[u8]) -> Result<(Vec<u8>, DecodeReport), Error> {
        let (batch, report) = self.decode(body)?;
        let mut buf = Vec::new();
        {
            let mut writer =
                arrow_ipc::writer::StreamWriter::try_new(&mut buf, batch.schema().as_ref())
                    .map_err(|e| Error::Decode(e.to_string()))?;
            writer
                .write(&batch)
                .map_err(|e| Error::Decode(e.to_string()))?;
            writer.finish().map_err(|e| Error::Decode(e.to_string()))?;
        }
        Ok((buf, report))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn bundled() -> Value {
        serde_json::json!({"components":{"schemas":{
            "Paging":{"type":"object","properties":{"hasNext":{"type":"boolean"}}},
            "Region":{"type":"object","required":["code"],"properties":{
                "code":{"type":"string","maxLength":3},
                "ISSRate":{"type":"number","minimum":0},
                "active":{"type":"boolean"},
                "kind":{"type":"string","enum":["A","B"]},
                "when":{"type":"string","format":"date-time"},
                "address":{"type":"object","required":["city"],"properties":{"city":{"type":"string"},"zip":{"type":"integer"}}},
                "tags":{"type":"array","items":{"type":"string","maxLength":2}},
                "contacts":{"type":"array","items":{"type":"object","properties":{"email":{"type":"string","minLength":3}}}}}},
            "PagedRegions":{"allOf":[{"$ref":"#/components/schemas/Paging"},{"type":"object","properties":{"items":{"type":"array","items":{"$ref":"#/components/schemas/Region"}}}}]}
        }}})
    }

    fn paths(report: &DecodeReport) -> Vec<(usize, String)> {
        report
            .violations
            .iter()
            .map(|v| (v.row, v.path.clone()))
            .collect()
    }

    #[test]
    fn decodes_paged_collection_and_reports_violations() {
        let dec = Decoder::new(&bundled(), "PagedRegions", "items", 100).unwrap();
        let body = br#"{"hasNext":true,"items":[
            {"code":"001","ISSRate":5.2,"active":true,"kind":"A","when":"2026-01-01T00:00:00Z","address":{"city":"SP","zip":1},"tags":["x"],"contacts":[{"email":"a@b"}]},
            {"code":"TOOLONG","ISSRate":-3.0,"kind":"Z","when":"2018-09-23T12:20:34","address":{"zip":2},"tags":["ok","bad"],"contacts":[{"email":"ok!"},{"email":"x"}]},
            {"ISSRate":1.0}]}"#;
        let (batch, report) = dec.decode(body).unwrap();
        assert_eq!(batch.num_rows(), 3);
        assert_eq!(report.rows, 3);
        assert_eq!(report.has_next, Some(true));
        assert_eq!(report.invalid_rows, 2);
        let got = paths(&report);
        for expected in [
            (1, "/code"),
            (1, "/ISSRate"),
            (1, "/kind"),
            (1, "/when"),
            (1, "/address"),
            (1, "/tags/1"),
            (1, "/contacts/1/email"),
            (2, ""),
        ] {
            assert!(
                got.contains(&(expected.0, expected.1.to_string())),
                "missing {expected:?} in {got:?}"
            );
        }
        assert!(report
            .violations
            .iter()
            .any(|v| v.path == "/address" && v.message.contains("required")));
        assert!(report
            .violations
            .iter()
            .any(|v| v.path.is_empty() && v.message == "\"code\" is a required property"));
        assert!(report.demoted_fields.is_empty());
        assert_eq!(
            batch
                .schema()
                .field_with_name("ISSRate")
                .unwrap()
                .data_type(),
            &DataType::Float64
        );
    }

    #[test]
    fn demotes_field_that_cannot_be_decoded_and_keeps_it_demoted() {
        let dec = Decoder::new(&bundled(), "PagedRegions", "items", 100).unwrap();
        let body = br#"{"hasNext":false,"items":[{"code":"001","ISSRate":"5,2","address":{"city":"x","zip":"01000-000"}},{"code":"002","ISSRate":7}]}"#;
        let (batch, report) = dec.decode(body).unwrap();
        assert_eq!(batch.num_rows(), 2);
        assert_eq!(
            report.demoted_fields,
            vec!["ISSRate".to_string(), "address.zip".to_string()]
        );
        assert_eq!(
            batch
                .schema()
                .field_with_name("ISSRate")
                .unwrap()
                .data_type(),
            &DataType::Utf8
        );
        // the demoted column keeps reporting per-row type violations
        assert!(report.violations.iter().any(|v| v.row == 0
            && v.path == "/ISSRate"
            && v.message.contains("not of type \"number\"")));
        assert!(report
            .violations
            .iter()
            .any(|v| v.row == 0 && v.path == "/address/zip" && v.message.contains("integer")));
        assert!(!report.violations.iter().any(|v| v.row == 1));
        // next page, clean data: still Utf8 so column types are stable
        let (batch2, report2) = dec
            .decode(br#"{"hasNext":false,"items":[{"code":"003","ISSRate":5.2}]}"#)
            .unwrap();
        assert_eq!(
            batch2
                .schema()
                .field_with_name("ISSRate")
                .unwrap()
                .data_type(),
            &DataType::Utf8
        );
        assert_eq!(report2.demoted_fields.len(), 2);
        assert_eq!(report2.invalid_rows, 0);
        let (ipc, _) = dec.decode_ipc(body).unwrap();
        assert!(ipc.len() > 100);
    }

    #[test]
    fn empty_pages_and_non_paged_bodies() {
        let dec = Decoder::new(&bundled(), "PagedRegions", "items", 10).unwrap();
        let (batch, report) = dec.decode(br#"{"hasNext":false,"items":[]}"#).unwrap();
        assert_eq!(
            (batch.num_rows(), report.rows, report.has_next),
            (0, 0, Some(false))
        );
        let dec = Decoder::new(&bundled(), "Region", "items", 10).unwrap();
        let (batch, report) = dec.decode(br#"{"code":"001","ISSRate":1.5}"#).unwrap();
        assert_eq!(
            (batch.num_rows(), report.has_next, report.invalid_rows),
            (1, None, 0)
        );
        assert!(Decoder::new(&bundled(), "Nope", "items", 10).is_err());
    }

    #[test]
    fn violations_are_capped_but_counted() {
        let dec = Decoder::new(&bundled(), "PagedRegions", "items", 2).unwrap();
        let (_, report) = dec
            .decode(br#"{"items":[{"code":"LONG1"},{"code":"LONG2"},{"code":"LONG3"}]}"#)
            .unwrap();
        assert_eq!(
            (
                report.invalid_rows,
                report.violations.len(),
                report.violations_truncated
            ),
            (3, 2, true)
        );
    }
}
