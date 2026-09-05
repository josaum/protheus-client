//! Identifier derivation. Every function here mirrors a Python helper in the
//! original generator one-to-one; the committed `index.json` is the oracle.

use regex::Regex;
use std::sync::LazyLock;

static NON_ALNUM: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"[^0-9A-Za-z]+").unwrap());
static LOWER_UPPER: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"([a-z0-9])([A-Z])").unwrap());
static ACRONYM: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"([A-Z]+)([A-Z][a-z])").unwrap());
static UNDERSCORES: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"_+").unwrap());
static SPEC_FILE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^(.*?)_v(\d+)(?:_(\d+))?\.json$").unwrap());

/// Python 3.12 keywords (`keyword.kwlist`).
const PY_KEYWORDS: &[&str] = &[
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
    "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while",
    "with", "yield",
];

pub fn snake(name: &str) -> String {
    let s = NON_ALNUM.replace_all(name, "_");
    let s = LOWER_UPPER.replace_all(&s, "${1}_${2}");
    let s = ACRONYM.replace_all(&s, "${1}_${2}");
    let s = UNDERSCORES.replace_all(&s, "_");
    let mut s = s.trim_matches('_').to_ascii_lowercase();
    if s.is_empty() {
        s = "x".to_string();
    }
    if s.as_bytes()[0].is_ascii_digit() {
        s = format!("n_{s}");
    }
    if PY_KEYWORDS.contains(&s.as_str()) {
        s.push('_');
    }
    s
}

pub fn pascal(name: &str) -> String {
    snake(name).split('_').map(capitalize_first).collect()
}

fn capitalize_first(part: &str) -> String {
    let mut chars = part.chars();
    match chars.next() {
        Some(first) => first.to_uppercase().collect::<String>() + chars.as_str(),
        None => String::new(),
    }
}

/// `CustomerVendor_v1_000.json` -> (`CustomerVendor`, `1`, `1_000`).
pub fn api_stem_and_version(filename: &str) -> Option<(String, String, String)> {
    let caps = SPEC_FILE.captures(filename)?;
    let stem = caps[1].to_string();
    let major = caps[2].to_string();
    let minor = caps.get(3).map(|m| m.as_str()).unwrap_or("0");
    Some((stem, major.clone(), format!("{major}_{minor}")))
}

/// filename -> api_id. Same stem+major twice keeps the full version token.
pub fn assign_api_ids(filenames: &[String]) -> indexmap::IndexMap<String, String> {
    let mut groups: indexmap::IndexMap<String, Vec<String>> = indexmap::IndexMap::new();
    for fname in filenames {
        let (stem, major, _) = api_stem_and_version(fname).expect("spec filename");
        groups
            .entry(format!("{}_v{}", snake(&stem), major))
            .or_default()
            .push(fname.clone());
    }
    let mut ids = indexmap::IndexMap::new();
    for (short, members) in &groups {
        for fname in members {
            let id = if members.len() == 1 {
                short.clone()
            } else {
                let (stem, _, full) = api_stem_and_version(fname).unwrap();
                format!("{}_v{}", snake(&stem), full)
            };
            ids.insert(fname.clone(), id);
        }
    }
    ids
}

/// Facade method name from HTTP method + path template.
pub fn method_name(method: &str, path: &str) -> String {
    let mut words: Vec<String> = Vec::new();
    let mut trailing_param = false;
    for part in path.trim_matches('/').split('/').filter(|p| !p.is_empty()) {
        if let Some(inner) = part.strip_prefix('{') {
            let inner = inner.trim_end_matches('}');
            let prefix = if trailing_param { "and_" } else { "by_" };
            words.push(format!("{prefix}{}", snake(inner)));
            trailing_param = true;
        } else {
            words.push(snake(part));
            trailing_param = false;
        }
    }
    let verb = match method {
        "get" => {
            if trailing_param {
                "get"
            } else {
                "list"
            }
        }
        "post" => "create",
        "put" => "update",
        "patch" => "patch",
        "delete" => "delete",
        other => other,
    };
    let mut out = vec![verb.to_string()];
    out.extend(words);
    out.join("_")
}

/// Mirror datamodel-code-generator's class naming for a component name.
pub fn model_class(component: &str) -> String {
    let name: String = NON_ALNUM
        .split(component)
        .filter(|p| !p.is_empty())
        .map(capitalize_first)
        .collect();
    let name = if name.is_empty() {
        "Model".to_string()
    } else {
        name
    };
    if name.as_bytes()[0].is_ascii_digit() {
        format!("Model{name}")
    } else {
        name
    }
}

/// Python annotation for a parameter schema (`python_type` in the generator).
pub fn python_type(schema: Option<&serde_json::Value>) -> &'static str {
    let Some(schema) = schema.and_then(|s| s.as_object()) else {
        return "str";
    };
    if schema.is_empty() {
        return "str";
    }
    let t = match schema.get("type") {
        Some(serde_json::Value::Array(items)) => items
            .iter()
            .filter_map(|v| v.as_str())
            .find(|s| *s != "null")
            .unwrap_or("string")
            .to_string(),
        Some(serde_json::Value::String(s)) => s.clone(),
        _ => String::new(),
    };
    match t.as_str() {
        "integer" => "int",
        "number" => "float",
        "boolean" => "bool",
        "array" => "list[str]",
        "object" => "dict[str, Any]",
        _ => "str",
    }
}

/// Python's `repr()` of a str: single quotes unless the text has a single
/// quote and no double quote.
pub fn py_repr(text: &str) -> String {
    let quote = if text.contains('\'') && !text.contains('"') {
        '"'
    } else {
        '\''
    };
    let mut out = String::with_capacity(text.len() + 2);
    out.push(quote);
    for ch in text.chars() {
        match ch {
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if c == quote => {
                out.push('\\');
                out.push(c);
            }
            c => out.push(c),
        }
    }
    out.push(quote);
    out
}

/// Python's `str(float)` for the values we meet (no exponent notation).
pub fn py_float(value: f64) -> String {
    if value.fract() == 0.0 && value.abs() < 1e16 {
        format!("{value:.1}")
    } else {
        format!("{value}")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn snake_matches_python() {
        assert_eq!(snake("customerVendorId"), "customer_vendor_id");
        assert_eq!(snake("MRPProduct"), "mrp_product");
        assert_eq!(snake("PriceListHeaderItem"), "price_list_header_item");
        assert_eq!(snake("from"), "from_");
        assert_eq!(snake("Accept-Language"), "accept_language");
        assert_eq!(snake("123abc"), "n_123abc");
        assert_eq!(snake("__"), "x");
    }

    #[test]
    fn method_names() {
        assert_eq!(
            method_name("get", "/customerVendor"),
            "list_customer_vendor"
        );
        assert_eq!(
            method_name("get", "/customerVendor/{entityType}"),
            "get_customer_vendor_by_entity_type"
        );
        assert_eq!(
            method_name(
                "delete",
                "/salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}"
            ),
            "delete_sales_charge_by_internal_id_and_account_receivable_document_internal_id"
        );
        assert_eq!(
            method_name("put", "/ordersPublic/complete/{orderId}"),
            "update_orders_public_complete_by_order_id"
        );
    }

    #[test]
    fn versions_and_ids() {
        assert_eq!(
            api_stem_and_version("JobScheduler_v1_001.json").unwrap(),
            ("JobScheduler".into(), "1".into(), "1_001".into())
        );
        let ids = assign_api_ids(&[
            "JobScheduler_v1_001.json".into(),
            "JobScheduler_v1_100.json".into(),
            "User_v1_000.json".into(),
        ]);
        assert_eq!(ids["JobScheduler_v1_001.json"], "job_scheduler_v1_001");
        assert_eq!(ids["User_v1_000.json"], "user_v1");
        assert_eq!(pascal("job_scheduler_v1_001"), "JobSchedulerV1001");
        assert_eq!(
            model_class("CustomerVendor_2_008_Paging"),
            "CustomerVendor2008Paging"
        );
        assert_eq!(model_class("customerVendorInfo"), "CustomerVendorInfo");
    }

    #[test]
    fn python_formatting() {
        assert_eq!(py_repr("999,999,999.99"), "'999,999,999.99'");
        assert_eq!(py_repr("it's"), "\"it's\"");
        assert_eq!(py_float(0.0), "0.0");
        assert_eq!(py_float(999999999.99), "999999999.99");
        assert_eq!(py_float(50.0), "50.0");
    }
}
