//! Synthesise one example instance from a (bundled) schema, preferring the
//! `example`/`examples` values TOTVS ships and respecting constraints for the
//! placeholders we invent.

use crate::index::schema_ref_name;
use serde_json::{Map, Value};

const MAX_DEPTH: usize = 48;

pub fn example_from_schema(schema: Option<&Value>, bundled: &Value) -> Value {
    example(schema, bundled, 0, &mut Vec::new())
}

fn example(schema: Option<&Value>, bundled: &Value, depth: usize, seen: &mut Vec<String>) -> Value {
    let Some(Value::Object(obj)) = schema else {
        return Value::Null;
    };
    if depth > MAX_DEPTH {
        return Value::Null;
    }
    if let Some(reference) = schema_ref_name(schema) {
        if seen.contains(&reference) {
            return Value::Null;
        }
        seen.push(reference.clone());
        let target = bundled["components"]["schemas"].get(&reference);
        let out = example(target, bundled, depth + 1, seen);
        seen.pop();
        return out;
    }
    if let Some(ex) = obj.get("example") {
        return ex.clone();
    }
    if let Some(Value::Array(exs)) = obj.get("examples") {
        if let Some(first) = exs.first() {
            return first.clone();
        }
    }
    if let Some(all_of) = obj.get("allOf") {
        let mut merged = Map::new();
        if let Value::Array(parts) = all_of {
            for part in parts {
                if let Value::Object(val) = example(Some(part), bundled, depth + 1, seen) {
                    for (k, v) in val {
                        merged.insert(k, v);
                    }
                }
            }
        }
        return Value::Object(merged);
    }
    for key in ["oneOf", "anyOf"] {
        if let Some(Value::Array(options)) = obj.get(key) {
            if let Some(first) = options.first() {
                return example(Some(first), bundled, depth + 1, seen);
            }
        }
    }
    if let Some(Value::Array(values)) = obj.get("enum") {
        if let Some(first) = values.first() {
            return first.clone();
        }
    }
    let type_ = match obj.get("type") {
        Some(Value::Array(items)) => items
            .iter()
            .filter_map(Value::as_str)
            .find(|s| *s != "null"),
        Some(Value::String(s)) => Some(s.as_str()),
        _ => None,
    };
    if type_ == Some("object") || obj.contains_key("properties") {
        let mut out = Map::new();
        if let Some(Value::Object(props)) = obj.get("properties") {
            for (k, v) in props {
                out.insert(k.clone(), example(Some(v), bundled, depth + 1, seen));
            }
        }
        return Value::Object(out);
    }
    match type_ {
        Some("array") => {
            let item = example(obj.get("items"), bundled, depth + 1, seen);
            Value::Array(if item.is_null() {
                Vec::new()
            } else {
                vec![item]
            })
        }
        Some("integer") | Some("number") => {
            let mut value = 1.0_f64;
            if let Some(lo) = obj.get("minimum").and_then(Value::as_f64) {
                if value < lo {
                    value = lo;
                }
            }
            if let Some(hi) = obj.get("maximum").and_then(Value::as_f64) {
                if value > hi {
                    value = hi;
                }
            }
            if type_ == Some("integer") {
                Value::from(value.trunc() as i64)
            } else {
                Value::from(value)
            }
        }
        Some("boolean") => Value::Bool(false),
        Some("string") => {
            let mut text = match obj.get("format").and_then(Value::as_str) {
                Some("date-time") => "2026-01-01T00:00:00Z",
                Some("date") => "2026-01-01",
                Some("uri") => "https://example.invalid/",
                Some("email") => "user@example.invalid",
                _ => "string",
            }
            .to_string();
            if let Some(max) = obj.get("maxLength").and_then(Value::as_i64) {
                if text.chars().count() as i64 > max {
                    text = "x".repeat(max.max(0) as usize);
                }
            }
            if let Some(min) = obj.get("minLength").and_then(Value::as_i64) {
                let len = text.chars().count() as i64;
                if len < min {
                    text.push_str(&"x".repeat((min - len) as usize));
                }
            }
            Value::String(text)
        }
        _ => Value::Null,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn follows_refs_and_all_of_and_constraints() {
        let bundled = serde_json::json!({"components":{"schemas":{
            "Paging":{"type":"object","properties":{"hasNext":{"type":"boolean","example":false}}},
            "Info":{"type":"object","properties":{"code":{"type":"string","maxLength":3},"n":{"type":"integer","minimum":5},
                    "kind":{"type":"string","enum":["A","B"]},"when":{"type":"string","format":"date"}}},
            "Paged":{"allOf":[{"$ref":"#/components/schemas/Paging"},{"type":"object","properties":{"items":{"type":"array","items":{"$ref":"#/components/schemas/Info"}}}}]}
        }}});
        let ex = example_from_schema(
            Some(&serde_json::json!({"$ref":"#/components/schemas/Paged"})),
            &bundled,
        );
        assert_eq!(
            ex,
            serde_json::json!({"hasNext":false,"items":[{"code":"xxx","n":5,"kind":"A","when":"2026-01-01"}]})
        );
    }

    #[test]
    fn cycles_yield_null_and_empty_arrays() {
        let bundled = serde_json::json!({"components":{"schemas":{
            "Node":{"type":"object","properties":{"children":{"type":"array","items":{"$ref":"#/components/schemas/Node"}}}}}}});
        let ex = example_from_schema(
            Some(&serde_json::json!({"$ref":"#/components/schemas/Node"})),
            &bundled,
        );
        assert_eq!(ex, serde_json::json!({"children":[]}));
    }
}
