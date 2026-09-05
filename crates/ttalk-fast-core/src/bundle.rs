//! Rewrite one TTALK spec into a self-contained OpenAPI 3 document.
//!
//! External `$ref`s (absolute GitHub URLs and cross-file relative paths) are
//! copied into `components/schemas` / `components/parameters` under stable,
//! readable names. Draft-03 style `required: true` on properties is folded into
//! the parent's `required` list, and numeric constraints written as strings are
//! coerced. Every normalisation is recorded in `quirks`.

use crate::load::load_json;
use crate::naming::{py_float, py_repr};
use crate::Error;
use indexmap::IndexMap;
use regex::Regex;
use serde_json::{Map, Value};
use std::collections::HashMap;
use std::path::{Path, PathBuf};
use std::sync::LazyLock;

pub const RAW_PREFIX: &str =
    "https://raw.githubusercontent.com/totvs/ttalk-standard-message/master/";

static NON_IDENT: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"[^A-Za-z0-9_]").unwrap());
static FILE_VERSION: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"_\d+_\d+$").unwrap());

const NUMERIC_KEYS: [&str; 5] = [
    "maximum",
    "minimum",
    "exclusiveMaximum",
    "exclusiveMinimum",
    "multipleOf",
];
const INT_KEYS: [&str; 6] = [
    "maxLength",
    "minLength",
    "maxItems",
    "minItems",
    "maxProperties",
    "minProperties",
];
const OPAQUE_KEYS: [&str; 5] = ["example", "examples", "default", "enum", "x-totvs"];
const JSON_SCHEMA_TYPES: [&str; 7] = [
    "string", "number", "integer", "boolean", "object", "array", "null",
];

/// TTALK writes database-ish types where JSON Schema types belong.
fn normalised_type(raw: &str) -> Option<&'static str> {
    match raw.trim().to_ascii_lowercase().as_str() {
        "string" | "str" | "char" | "varchar" | "text" | "date" | "datetime" | "date-time"
        | "time" | "uuid" => Some("string"),
        "integer" | "int" | "int32" | "int64" | "long" | "short" => Some("integer"),
        "number" | "double" | "float" | "float32" | "float64" | "decimal" | "numeric" => {
            Some("number")
        }
        "boolean" | "bool" => Some("boolean"),
        "object" => Some("object"),
        "array" | "list" => Some("array"),
        _ => None,
    }
}

pub struct Bundler {
    repo: PathBuf,
    spec_path: PathBuf,
    docs: HashMap<PathBuf, Value>,
    names: HashMap<(PathBuf, String), String>,
    pub quirks: Vec<String>,
    spec: Value,
}

fn file_stem(path: &Path) -> String {
    path.file_stem()
        .and_then(|s| s.to_str())
        .unwrap_or_default()
        .to_string()
}

/// Lexically normalise `..` and `.` segments (Python's `Path.resolve()` for our purposes).
fn normalize(path: PathBuf) -> PathBuf {
    let mut out = PathBuf::new();
    for comp in path.components() {
        match comp {
            std::path::Component::ParentDir => {
                out.pop();
            }
            std::path::Component::CurDir => {}
            other => out.push(other.as_os_str()),
        }
    }
    out
}

impl Bundler {
    pub fn new(repo: &Path, spec_path: &Path) -> Result<Self, Error> {
        let mut spec = load_json(spec_path)?;
        {
            let comps = spec
                .as_object_mut()
                .ok_or_else(|| {
                    Error::Spec(format!("{}: root is not an object", spec_path.display()))
                })?
                .entry("components")
                .or_insert_with(|| Value::Object(Map::new()));
            let comps = comps
                .as_object_mut()
                .ok_or_else(|| Error::Spec("components is not an object".into()))?;
            comps
                .entry("schemas")
                .or_insert_with(|| Value::Object(Map::new()));
            comps
                .entry("parameters")
                .or_insert_with(|| Value::Object(Map::new()));
        }
        let mut docs = HashMap::new();
        docs.insert(spec_path.to_path_buf(), spec.clone());
        Ok(Self {
            repo: repo.to_path_buf(),
            spec_path: spec_path.to_path_buf(),
            docs,
            names: HashMap::new(),
            quirks: Vec::new(),
            spec,
        })
    }

    fn doc(&mut self, path: &Path) -> Result<&Value, Error> {
        if !self.docs.contains_key(path) {
            let value = load_json(path)?;
            self.docs.insert(path.to_path_buf(), value);
        }
        Ok(&self.docs[path])
    }

    fn target_file(&self, current: &Path, reference: &str) -> Result<PathBuf, Error> {
        let target = reference.split('#').next().unwrap_or("");
        if target.is_empty() {
            return Ok(current.to_path_buf());
        }
        if let Some(rest) = target.strip_prefix(RAW_PREFIX) {
            return Ok(self.repo.join(rest));
        }
        if target.starts_with("http") {
            return Err(Error::Spec(format!(
                "unsupported external ref {reference} in {}",
                current.display()
            )));
        }
        Ok(normalize(
            current.parent().unwrap_or(Path::new("")).join(target),
        ))
    }

    fn deref<'a>(doc: &'a Value, fragment: &str) -> Result<&'a Value, Error> {
        let mut node = doc;
        for part in fragment
            .trim_start_matches("#/")
            .trim_start_matches('/')
            .split('/')
        {
            if part.is_empty() {
                continue;
            }
            let key = part.replace("~1", "/").replace("~0", "~");
            node = match node {
                Value::Object(map) => map.get(&key),
                Value::Array(items) => key.parse::<usize>().ok().and_then(|i| items.get(i)),
                _ => None,
            }
            .ok_or_else(|| Error::Spec(format!("unresolvable pointer {fragment}")))?;
        }
        Ok(node)
    }

    fn bucket(&mut self, section: &str) -> &mut Map<String, Value> {
        self.spec["components"][section]
            .as_object_mut()
            .expect("components section")
    }

    fn component_name(&mut self, file: &Path, fragment: &str, section: &str) -> String {
        let key = (file.to_path_buf(), fragment.to_string());
        if let Some(name) = self.names.get(&key) {
            return name.clone();
        }
        let last_raw = fragment
            .trim_end_matches('/')
            .rsplit('/')
            .next()
            .unwrap_or("");
        let last = NON_IDENT.replace_all(last_raw, "_").to_string();
        let stem_full = file_stem(file);
        let stem = FILE_VERSION.replace(&stem_full, "").to_string();
        let candidates = [
            last.clone(),
            format!("{stem}_{last}"),
            format!("{stem_full}_{last}"),
        ];
        let bucket = self.bucket(section);
        for cand in candidates {
            if !bucket.contains_key(&cand) {
                bucket.insert(cand.clone(), Value::Null);
                self.names.insert(key, cand.clone());
                return cand;
            }
        }
        let mut n = 2;
        while bucket.contains_key(&format!("{stem_full}_{last}_{n}")) {
            n += 1;
        }
        let name = format!("{stem_full}_{last}_{n}");
        bucket.insert(name.clone(), Value::Null);
        self.names.insert(key, name.clone());
        name
    }

    fn rewrite(&mut self, node: Value, current: &Path) -> Result<Value, Error> {
        match node {
            Value::Array(items) => Ok(Value::Array(
                items
                    .into_iter()
                    .map(|v| self.rewrite(v, current))
                    .collect::<Result<_, _>>()?,
            )),
            Value::Object(map) => {
                if let Some(Value::String(reference)) = map.get("$ref") {
                    let reference = reference.clone();
                    let file = self.target_file(current, &reference)?;
                    let fragment = reference
                        .split_once('#')
                        .map(|(_, f)| f)
                        .unwrap_or("")
                        .to_string();
                    if file == self.spec_path && fragment.starts_with("/components/") {
                        return Ok(Value::Object(map));
                    }
                    let section = if fragment.starts_with("/parameters/") {
                        "parameters"
                    } else {
                        "schemas"
                    };
                    let key = (file.clone(), fragment.clone());
                    let name = match self.names.get(&key) {
                        Some(name) => name.clone(),
                        None => {
                            let name = self.component_name(&file, &fragment, section);
                            let target = Self::deref(self.doc(&file)?, &fragment)?.clone();
                            let rewritten = self.rewrite(target, &file)?;
                            self.bucket(section).insert(name.clone(), rewritten);
                            name
                        }
                    };
                    let mut out = Map::new();
                    for (k, v) in map {
                        if k != "$ref" {
                            out.insert(k, v);
                        }
                    }
                    out.insert(
                        "$ref".to_string(),
                        Value::String(format!("#/components/{section}/{name}")),
                    );
                    return Ok(Value::Object(out));
                }
                let mut out = Map::new();
                for (k, v) in map {
                    out.insert(k, self.rewrite(v, current)?);
                }
                Ok(Value::Object(out))
            }
            other => Ok(other),
        }
    }

    /// Move draft-03 `required: <bool>` from property schemas to the parent list.
    fn fold_draft3_required(node: &mut Value) {
        match node {
            Value::Array(items) => items.iter_mut().for_each(Self::fold_draft3_required),
            Value::Object(map) => {
                if map.get("properties").map(Value::is_object).unwrap_or(false) {
                    let mut req: Vec<Value> = match map.get("required") {
                        Some(Value::Array(items)) => items.clone(),
                        _ => Vec::new(),
                    };
                    let props = map
                        .get_mut("properties")
                        .and_then(Value::as_object_mut)
                        .unwrap();
                    for (pname, pschema) in props.iter_mut() {
                        if let Value::Object(ps) = pschema {
                            if let Some(Value::Bool(flag)) = ps.get("required").cloned() {
                                ps.shift_remove("required");
                                if flag && !req.iter().any(|r| r.as_str() == Some(pname)) {
                                    req.push(Value::String(pname.clone()));
                                }
                            }
                        }
                    }
                    if !req.is_empty() {
                        map.insert("required".to_string(), Value::Array(req));
                    }
                }
                if map.get("required").map(Value::is_boolean).unwrap_or(false) {
                    map.shift_remove("required");
                }
                for (k, v) in map.iter_mut() {
                    if !OPAQUE_KEYS.contains(&k.as_str()) {
                        Self::fold_draft3_required(v);
                    }
                }
            }
            _ => {}
        }
    }

    /// Coerce numeric constraints written as strings (`"999,999,999.99"`, `"50"`).
    fn sanitize(node: &mut Value, at: &str, quirks: &mut Vec<String>) {
        match node {
            Value::Array(items) => {
                for (i, v) in items.iter_mut().enumerate() {
                    Self::sanitize(v, &format!("{at}[{i}]"), quirks);
                }
            }
            Value::Object(map) => {
                if let Some(Value::String(raw)) = map.get("type") {
                    if !JSON_SCHEMA_TYPES.contains(&raw.as_str()) {
                        let raw = raw.clone();
                        match normalised_type(&raw) {
                            Some(fixed) => {
                                map.insert("type".to_string(), Value::String(fixed.to_string()));
                                quirks.push(format!(
                                    "{at}.type: {} is not a JSON Schema type; read as '{fixed}'",
                                    py_repr(&raw)
                                ));
                            }
                            None => {
                                map.shift_remove("type");
                                quirks.push(format!(
                                    "{at}.type: {} is not a JSON Schema type; dropped",
                                    py_repr(&raw)
                                ));
                            }
                        }
                    }
                }
                for key in NUMERIC_KEYS.iter().chain(INT_KEYS.iter()) {
                    let Some(Value::String(raw)) = map.get(*key) else {
                        continue;
                    };
                    let raw = raw.clone();
                    let cleaned = raw.replace(',', "");
                    match cleaned.trim().parse::<f64>().ok() {
                        Some(num) if NUMERIC_KEYS.contains(key) => {
                            map.insert(key.to_string(), serde_json::json!(num));
                            quirks.push(format!(
                                "{at}.{key}: string constraint {} coerced to {}",
                                py_repr(&raw),
                                py_float(num)
                            ));
                        }
                        Some(num) => {
                            let int = num.trunc() as i64;
                            map.insert(key.to_string(), serde_json::json!(int));
                            quirks.push(format!(
                                "{at}.{key}: string constraint {} coerced to {int}",
                                py_repr(&raw)
                            ));
                        }
                        None => {
                            map.shift_remove(*key);
                            quirks.push(format!(
                                "{at}.{key}: unparsable constraint {} dropped",
                                py_repr(&raw)
                            ));
                        }
                    }
                }
                for (k, v) in map.iter_mut() {
                    if !OPAQUE_KEYS.contains(&k.as_str()) {
                        let next = if at.is_empty() {
                            k.clone()
                        } else {
                            format!("{at}.{k}")
                        };
                        Self::sanitize(v, &next, quirks);
                    }
                }
            }
            _ => {}
        }
    }

    pub fn bundle(mut self) -> Result<(Value, Vec<String>), Error> {
        let own: IndexMap<&str, Vec<String>> = ["parameters", "schemas"]
            .into_iter()
            .map(|section| {
                let names = self.spec["components"][section]
                    .as_object()
                    .unwrap()
                    .keys()
                    .cloned()
                    .collect();
                (section, names)
            })
            .collect();
        let paths = self.spec["paths"].take();
        let spec_path = self.spec_path.clone();
        self.spec["paths"] = self.rewrite(paths, &spec_path)?;
        for (section, names) in own {
            for name in names {
                let value = self.spec["components"][section][&name].take();
                let rewritten = self.rewrite(value, &spec_path)?;
                self.spec["components"][section][&name] = rewritten;
            }
        }
        for section in ["parameters", "schemas"] {
            let unresolved: Vec<String> = self.spec["components"][section]
                .as_object()
                .unwrap()
                .iter()
                .filter(|(_, v)| v.is_null())
                .map(|(k, _)| k.clone())
                .collect();
            if !unresolved.is_empty() {
                return Err(Error::Spec(format!(
                    "{}: unresolved {section} {unresolved:?}",
                    self.spec_path.display()
                )));
            }
        }
        Self::fold_draft3_required(&mut self.spec["components"]["schemas"]);
        if let Some(params) = self.spec["components"]["parameters"].as_object_mut() {
            for param in params.values_mut() {
                if let Some(schema) = param.get_mut("schema") {
                    Self::fold_draft3_required(schema);
                }
            }
        }
        let mut quirks = std::mem::take(&mut self.quirks);
        Self::sanitize(
            &mut self.spec["components"]["schemas"],
            "schemas",
            &mut quirks,
        );
        Self::sanitize(
            &mut self.spec["components"]["parameters"],
            "parameters",
            &mut quirks,
        );
        Ok((self.spec, quirks))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn fold_moves_boolean_required_to_parent_list() {
        let mut v = serde_json::json!({"type":"object","properties":{"a":{"type":"string","required":true},"b":{"type":"string","required":false}}});
        Bundler::fold_draft3_required(&mut v);
        assert_eq!(v["required"], serde_json::json!(["a"]));
        assert!(v["properties"]["a"].get("required").is_none());
        assert!(v["properties"]["b"].get("required").is_none());
    }

    #[test]
    fn fold_leaves_examples_alone() {
        let mut v = serde_json::json!({"type":"object","example":{"required":true}});
        Bundler::fold_draft3_required(&mut v);
        assert_eq!(v["example"]["required"], serde_json::json!(true));
    }

    #[test]
    fn sanitize_normalises_non_json_schema_types() {
        let mut v = serde_json::json!({"Info":{"type":"object","properties":{"when":{"type":"Date"},"n":{"type":"int32"},"x":{"type":"blob"},"type":{"type":"String"}}}});
        let mut quirks = Vec::new();
        Bundler::sanitize(&mut v, "schemas", &mut quirks);
        assert_eq!(v["Info"]["properties"]["when"]["type"], "string");
        assert_eq!(v["Info"]["properties"]["n"]["type"], "integer");
        assert!(v["Info"]["properties"]["x"].get("type").is_none());
        assert_eq!(v["Info"]["properties"]["type"]["type"], "string");
        assert_eq!(
            quirks[0],
            "schemas.Info.properties.when.type: 'Date' is not a JSON Schema type; read as 'string'"
        );
        assert_eq!(
            quirks[2],
            "schemas.Info.properties.x.type: 'blob' is not a JSON Schema type; dropped"
        );
    }

    #[test]
    fn sanitize_coerces_and_reports_like_python() {
        let mut v = serde_json::json!({"Value":{"type":"number","maximum":"999,999,999.99","minimum":"0","maxLength":"50"}});
        let mut quirks = Vec::new();
        Bundler::sanitize(&mut v, "schemas", &mut quirks);
        assert_eq!(v["Value"]["maximum"], serde_json::json!(999999999.99));
        assert_eq!(v["Value"]["minimum"], serde_json::json!(0.0));
        assert_eq!(v["Value"]["maxLength"], serde_json::json!(50));
        assert_eq!(
            quirks,
            vec![
                "schemas.Value.maximum: string constraint '999,999,999.99' coerced to 999999999.99",
                "schemas.Value.minimum: string constraint '0' coerced to 0.0",
                "schemas.Value.maxLength: string constraint '50' coerced to 50",
            ]
        );
    }
}
