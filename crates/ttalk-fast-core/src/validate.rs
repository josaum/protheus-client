//! JSON-Schema validation against the bundled component schemas.
//!
//! TTALK schemas are draft-04 flavoured (boolean `exclusiveMinimum`, `$ref`
//! with siblings), so validators are built with Draft 4 semantics and format
//! assertions on. A verdict names the first violation; callers decide whether
//! that is fatal — for live ERP data it never is (validate and report).

use crate::index::Verdict;
use jsonschema::{Draft, Validator};
use serde_json::Value;

/// Compile a validator for `#/components/schemas/<name>` inside `bundled`.
pub fn validator_for(bundled: &Value, name: &str) -> Result<Validator, String> {
    validator_for_schema(
        bundled,
        &serde_json::json!({"$ref": format!("#/components/schemas/{name}")}),
    )
}

/// Compile a validator for an arbitrary (sub)schema whose `$ref`s point into
/// `bundled`'s components.
pub fn validator_for_schema(bundled: &Value, schema: &Value) -> Result<Validator, String> {
    let mut root = serde_json::json!({
        "components": {"schemas": bundled["components"]["schemas"]},
    });
    match schema.get("$ref") {
        Some(r) => {
            root["$ref"] = r.clone();
        }
        None => {
            root["allOf"] = serde_json::json!([schema]);
        }
    }
    jsonschema::options()
        .with_draft(Draft::Draft4)
        .should_validate_formats(true)
        .build(&root)
        .map_err(|e| format!("schema_compile: {e}"))
}

/// First violation of `instance` against the validator, as a compact verdict.
pub fn verdict(validator: &Validator, instance: &Value) -> Verdict {
    match validator.iter_errors(instance).next() {
        None => Verdict {
            ok: true,
            error: None,
        },
        Some(err) => Verdict {
            ok: false,
            error: Some(format!("{} at {}", err, err.instance_path())),
        },
    }
}

/// All violations (bounded), as `(instance_path, message)` pairs.
pub fn violations(validator: &Validator, instance: &Value, limit: usize) -> Vec<(String, String)> {
    validator
        .iter_errors(instance)
        .take(limit)
        .map(|e| (e.instance_path().to_string(), e.to_string()))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn draft4_semantics_and_formats() {
        let bundled = serde_json::json!({"components":{"schemas":{
            "Info":{"type":"object","properties":{
                "kind":{"type":"string","enum":["1","2"]},
                "page":{"type":"integer","minimum":1,"exclusiveMinimum":false},
                "when":{"type":"string","format":"date-time"},
                "rate":{"type":"number"}}}}}});
        let v = validator_for(&bundled, "Info").unwrap();
        assert!(
            verdict(
                &v,
                &serde_json::json!({"kind":"1","page":1,"when":"2026-01-01T00:00:00Z","rate":5.2})
            )
            .ok
        );
        let bad = verdict(&v, &serde_json::json!({"kind":"1-Company"}));
        assert!(!bad.ok);
        assert!(bad.error.unwrap().contains("/kind"));
        assert!(!verdict(&v, &serde_json::json!({"rate":"5,2"})).ok);
        assert!(
            !verdict(&v, &serde_json::json!({"when":"2018-09-23T12:20:34"})).ok,
            "date-time requires an offset"
        );
    }
}
