//! Operation index for one product, derived from a bundled TTALK spec.
//!
//! Selection rule: the API must list the product in
//! `info.x-totvs.productInformation`; an operation is kept unless it carries
//! `available: false` for that product. Operations with no operation-level
//! flag are kept and tagged `availability = "inherited"`.

use crate::naming::{api_stem_and_version, method_name, model_class, pascal, python_type, snake};
use indexmap::IndexMap;
use serde::Serialize;
use serde_json::{Map, Value};

pub const HTTP_METHODS: [&str; 5] = ["get", "post", "put", "patch", "delete"];
pub const STANDARD_QUERY: [(&str, &str); 6] = [
    ("fields", "fields"),
    ("order", "order"),
    ("page", "page"),
    ("pageSize", "page_size"),
    ("filter", "filter"),
    ("expand", "expand"),
];
const CLIENT_MANAGED_HEADERS: [&str; 2] = ["authorization", "accept-language"];

#[derive(Debug, Clone, Serialize, PartialEq)]
pub struct Param {
    pub name: String,
    pub python: String,
    pub required: bool,
    #[serde(rename = "type")]
    pub type_: String,
    pub description: String,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
pub struct RequestBody {
    pub required: bool,
    pub content_type: Option<String>,
    pub schema: Option<String>,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
pub struct ResponseRef {
    pub description: Value,
    pub schema: Option<String>,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
pub struct Verdict {
    pub ok: bool,
    pub error: Option<String>,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
pub struct Operation {
    pub id: String,
    pub name: String,
    pub operation_id: Option<String>,
    pub method: String,
    pub path: String,
    pub summary: String,
    pub description: String,
    pub deprecated: bool,
    pub side_effect: bool,
    pub availability: String,
    pub minimal_version: Value,
    pub note: Option<String>,
    pub path_params: Vec<Param>,
    pub query_params: Vec<Param>,
    pub header_params: Vec<Param>,
    pub standard_params: Vec<String>,
    pub request_body: Option<RequestBody>,
    pub responses: IndexMap<String, ResponseRef>,
    pub request_model: Option<String>,
    pub response_model: Option<String>,
    /// `{"schema": Verdict}` — the JSON-Schema verdict on the synthesised
    /// example; the Python generator adds `"model"` for the pydantic verdict.
    pub example_validation: Option<IndexMap<String, Verdict>>,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
pub struct ProductInfo {
    pub contact: Value,
    pub description: Option<String>,
    pub adapter: Value,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
pub struct Api {
    pub id: String,
    pub class_name: String,
    pub spec_file: String,
    pub title: String,
    pub description: String,
    pub version: Value,
    pub segment: Option<String>,
    pub base_path: String,
    pub product_info: ProductInfo,
    pub spec_quirks: Vec<String>,
    pub operations: Vec<Operation>,
}

fn str_or_empty(v: Option<&Value>) -> String {
    v.and_then(Value::as_str).unwrap_or("").to_string()
}

/// Python `value or None`.
fn py_or_none(v: Option<&Value>) -> Value {
    match v {
        Some(v) if truthy(v) => v.clone(),
        _ => Value::Null,
    }
}

fn product_infos(node: &Value) -> Vec<&Map<String, Value>> {
    node.get("x-totvs")
        .and_then(|x| x.get("productInformation"))
        .and_then(Value::as_array)
        .map(|items| items.iter().filter_map(Value::as_object).collect())
        .unwrap_or_default()
}

/// `Some((availability, info))` when the operation is usable on `product`.
fn op_availability<'a>(
    op: &'a Value,
    product: &str,
) -> Option<(&'static str, Option<&'a Map<String, Value>>)> {
    for info in product_infos(op) {
        if info.get("product").and_then(Value::as_str) == Some(product) {
            if info.get("available") == Some(&Value::Bool(false)) {
                return None;
            }
            return Some(("declared", Some(info)));
        }
    }
    Some(("inherited", None))
}

pub fn schema_ref_name(schema: Option<&Value>) -> Option<String> {
    schema?
        .get("$ref")
        .and_then(Value::as_str)
        .map(|r| r.rsplit('/').next().unwrap_or(r).to_string())
}

/// Resolve a parameter (inline or `#/components/parameters/X`), repairing
/// ones that lack `name`/`in` (assumed query parameters) and recording it.
fn resolve_param(spec: &Value, p: &Value, quirks: &mut Vec<String>) -> Map<String, Value> {
    let mut key: Option<String> = None;
    let mut param = p.as_object().cloned().unwrap_or_default();
    if let Some(reference) = p.get("$ref").and_then(Value::as_str) {
        let k = reference.rsplit('/').next().unwrap_or("").to_string();
        param = spec["components"]["parameters"][&k]
            .as_object()
            .cloned()
            .unwrap_or_default();
        key = Some(k);
    }
    let has_name = param
        .get("name")
        .and_then(Value::as_str)
        .map(|s| !s.is_empty())
        .unwrap_or(false);
    let has_in = param
        .get("in")
        .and_then(Value::as_str)
        .map(|s| !s.is_empty())
        .unwrap_or(false);
    if !has_name || !has_in {
        let name = param
            .get("name")
            .and_then(Value::as_str)
            .filter(|s| !s.is_empty())
            .map(str::to_string)
            .or(key)
            .unwrap_or_else(|| "param".to_string());
        let location = param
            .get("in")
            .and_then(Value::as_str)
            .filter(|s| !s.is_empty())
            .unwrap_or("query")
            .to_string();
        param.insert("name".to_string(), Value::String(name.clone()));
        param.insert("in".to_string(), Value::String(location));
        quirks.push(format!(
            "parameter '{name}' lacks name/in; assumed query parameter"
        ));
    }
    param
}

fn unique_arg_names(op: &mut Operation) {
    let mut reserved: Vec<String> = ["self", "body", "extra_query"]
        .iter()
        .map(|s| s.to_string())
        .collect();
    reserved.extend(STANDARD_QUERY.iter().map(|(_, py)| py.to_string()));
    for (group, suffix) in [
        (&mut op.path_params, "_path"),
        (&mut op.query_params, "_q"),
        (&mut op.header_params, "_h"),
    ] {
        for p in group.iter_mut() {
            let mut name = p.python.clone();
            while reserved.contains(&name) {
                name.push_str(suffix);
            }
            p.python = name.clone();
            reserved.push(name);
        }
    }
}

fn param_entry(p: &Map<String, Value>) -> Param {
    let name = str_or_empty(p.get("name"));
    Param {
        python: snake(&name),
        name,
        required: p.get("required").map(truthy).unwrap_or(false),
        type_: python_type(p.get("schema")).to_string(),
        description: str_or_empty(p.get("description")).trim().to_string(),
    }
}

/// Build the index entry for one bundled spec, or `None` when the product is
/// not listed or has no usable operation.
pub fn index_api(
    filename: &str,
    api_id: &str,
    spec: &Value,
    product: &str,
    bundle_quirks: &[String],
) -> Option<Api> {
    let info = spec.get("info")?;
    let prod = product_infos(info)
        .into_iter()
        .find(|p| p.get("product").and_then(Value::as_str) == Some(product))?;
    let (stem, _, _) = api_stem_and_version(filename)?;

    let server_url = spec["servers"][0]["url"].as_str().unwrap_or("").to_string();
    let base_path = match server_url.split_once("/api/") {
        Some((_, rest)) => format!("/{rest}"),
        None => server_url.clone(),
    };
    let base_path = format!("/api/{}", base_path.trim_start_matches('/'));

    let mut operations = Vec::new();
    let mut seen_methods: Vec<String> = Vec::new();
    let mut quirks: Vec<String> = Vec::new();
    let path_re = regex::Regex::new(r"\{([^}]+)\}").unwrap();

    let paths = spec.get("paths").and_then(Value::as_object)?;
    for (path, item) in paths {
        let path_level: Vec<Map<String, Value>> = item
            .get("parameters")
            .and_then(Value::as_array)
            .map(|ps| {
                ps.iter()
                    .map(|p| resolve_param(spec, p, &mut quirks))
                    .collect()
            })
            .unwrap_or_default();
        for method in HTTP_METHODS {
            let Some(op) = item.get(method).filter(|v| !v.is_null()) else {
                continue;
            };
            if op.as_object().map(|m| m.is_empty()).unwrap_or(true) {
                continue;
            }
            let Some((availability, pinfo)) = op_availability(op, product) else {
                continue;
            };
            let mut params = path_level.clone();
            params.extend(
                op.get("parameters")
                    .and_then(Value::as_array)
                    .map(|ps| {
                        ps.iter()
                            .map(|p| resolve_param(spec, p, &mut quirks))
                            .collect::<Vec<_>>()
                    })
                    .unwrap_or_default(),
            );
            let (mut path_params, mut query_params, mut header_params, mut standard) =
                (Vec::new(), Vec::new(), Vec::new(), Vec::new());
            for p in &params {
                let location = p.get("in").and_then(Value::as_str).unwrap_or("");
                let mut entry = param_entry(p);
                match location {
                    "path" => {
                        entry.required = true;
                        entry.type_ = "str".to_string();
                        path_params.push(entry);
                    }
                    "query" => {
                        if STANDARD_QUERY.iter().any(|(n, _)| *n == entry.name) {
                            standard.push(entry.name.clone());
                        } else {
                            query_params.push(entry);
                        }
                    }
                    "header"
                        if !CLIENT_MANAGED_HEADERS
                            .contains(&entry.name.to_lowercase().as_str()) =>
                    {
                        header_params.push(entry);
                    }
                    _ => {}
                }
            }
            for caps in path_re.captures_iter(path) {
                let tmpl = caps[1].to_string();
                if !path_params.iter().any(|pp| pp.name == tmpl) {
                    quirks.push(format!(
                        "{} {path}: path parameter '{tmpl}' not declared; added",
                        method.to_uppercase()
                    ));
                    path_params.push(Param {
                        python: snake(&tmpl),
                        name: tmpl,
                        required: true,
                        type_: "str".to_string(),
                        description: String::new(),
                    });
                }
            }
            let order: Vec<String> = path_re
                .captures_iter(path)
                .map(|c| c[1].to_string())
                .collect();
            path_params.sort_by_key(|pp| {
                order
                    .iter()
                    .position(|n| *n == pp.name)
                    .unwrap_or(order.len())
            });

            let request_body = op.get("requestBody").filter(|rb| truthy(rb)).map(|rb| {
                let content = rb.get("content").and_then(Value::as_object);
                let ctype = content.and_then(|c| {
                    if c.contains_key("application/json") {
                        Some("application/json".to_string())
                    } else {
                        c.keys().next().cloned()
                    }
                });
                RequestBody {
                    required: rb.get("required").map(truthy).unwrap_or(true),
                    schema: ctype
                        .as_ref()
                        .and_then(|ct| content.and_then(|c| c.get(ct)))
                        .and_then(|c| schema_ref_name(c.get("schema"))),
                    content_type: ctype,
                }
            });

            let mut responses = IndexMap::new();
            if let Some(resps) = op.get("responses").and_then(Value::as_object) {
                for (status, resp) in resps {
                    let json = resp
                        .get("content")
                        .and_then(|c| c.get("application/json"))
                        .filter(|v| !v.is_null());
                    responses.insert(
                        status.clone(),
                        ResponseRef {
                            description: resp
                                .get("description")
                                .cloned()
                                .unwrap_or(Value::String(String::new())),
                            schema: schema_ref_name(json.and_then(|j| j.get("schema"))),
                        },
                    );
                }
            }
            let mut name = method_name(method, path);
            while seen_methods.contains(&name) {
                name.push('_');
            }
            seen_methods.push(name.clone());
            let ok_schema = responses
                .iter()
                .find(|(s, r)| s.starts_with('2') && r.schema.is_some())
                .and_then(|(_, r)| r.schema.clone());
            let summary = str_or_empty(op.get("summary")).trim().to_string();
            let description = str_or_empty(op.get("description")).trim().to_string();
            let mut operation = Operation {
                id: format!("{api_id}.{name}"),
                name,
                operation_id: op
                    .get("operationId")
                    .and_then(Value::as_str)
                    .map(str::to_string),
                method: method.to_uppercase(),
                path: path.clone(),
                summary,
                description,
                deprecated: op.get("deprecated").map(truthy).unwrap_or(false),
                side_effect: method != "get",
                availability: availability.to_string(),
                minimal_version: pinfo
                    .map(|i| py_or_none(i.get("minimalVersion")))
                    .unwrap_or(Value::Null),
                note: pinfo
                    .and_then(|i| i.get("note"))
                    .and_then(Value::as_str)
                    .map(str::trim)
                    .filter(|s| !s.is_empty())
                    .map(str::to_string),
                path_params,
                query_params,
                header_params,
                standard_params: standard,
                request_model: request_body
                    .as_ref()
                    .and_then(|b| b.schema.as_deref())
                    .map(model_class),
                request_body,
                responses,
                response_model: ok_schema.as_deref().map(model_class),
                example_validation: None,
            };
            unique_arg_names(&mut operation);
            operations.push(operation);
        }
    }
    if operations.is_empty() {
        return None;
    }
    let mut spec_quirks: Vec<String> = quirks
        .into_iter()
        .chain(bundle_quirks.iter().cloned())
        .collect();
    spec_quirks.sort();
    spec_quirks.dedup();
    let xt = info.get("x-totvs");
    Some(Api {
        id: api_id.to_string(),
        class_name: pascal(api_id),
        spec_file: filename.to_string(),
        title: info
            .get("title")
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|s| !s.is_empty())
            .unwrap_or(&stem)
            .to_string(),
        description: str_or_empty(info.get("description")).trim().to_string(),
        version: info.get("version").cloned().unwrap_or(Value::Null),
        segment: xt
            .and_then(|x| x.get("messageDocumentation"))
            .and_then(|m| m.get("segment"))
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|s| !s.is_empty())
            .map(str::to_string),
        base_path,
        product_info: ProductInfo {
            contact: py_or_none(prod.get("contact")),
            description: prod
                .get("description")
                .and_then(Value::as_str)
                .map(str::trim)
                .filter(|s| !s.is_empty())
                .map(str::to_string),
            adapter: py_or_none(prod.get("adapter")),
        },
        spec_quirks,
        operations,
    })
}

/// Python truthiness for JSON values.
fn truthy(v: &Value) -> bool {
    match v {
        Value::Null => false,
        Value::Bool(b) => *b,
        Value::Number(n) => n.as_f64().map(|f| f != 0.0).unwrap_or(true),
        Value::String(s) => !s.is_empty(),
        Value::Array(a) => !a.is_empty(),
        Value::Object(o) => !o.is_empty(),
    }
}
