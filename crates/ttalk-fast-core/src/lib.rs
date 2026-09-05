//! `ttalk-fast-core` — the TOTVS TTALK spec engine behind `totvs-protheus`.
//!
//! Given a checkout of `totvs/ttalk-standard-message` and a product name, it
//! bundles each spec into a self-contained OpenAPI document, normalises the
//! corpus' known defects (recording each one), indexes the operations the
//! product can actually call, synthesises example responses, validates those
//! examples against their own schemas, and decodes live pages into Arrow.
//!
//! The Python generator (`tools/build.py`) consumes [`build`]'s output to emit
//! the typed facade and pydantic models; nothing product-specific lives here.

pub mod arrow;
pub mod bundle;
pub mod example;
pub mod index;
pub mod json_scan;
pub mod load;
pub mod naming;
pub mod validate;

use indexmap::IndexMap;
use serde::Serialize;
use serde_json::Value;
use std::path::Path;

#[derive(Debug, thiserror::Error)]
pub enum Error {
    #[error("{0}: {1}")]
    Io(String, std::io::Error),
    #[error("{0}: {1}")]
    Json(String, serde_json::Error),
    #[error("spec: {0}")]
    Spec(String),
    #[error("provenance: {0}")]
    Provenance(String),
    #[error("decode: {0}")]
    Decode(String),
}

#[derive(Debug, Clone, Serialize)]
pub struct Fixture {
    pub status: u16,
    pub body: Value,
}

#[derive(Debug, Clone, Serialize)]
pub struct Summary {
    pub apis: usize,
    pub operations: usize,
    pub apis_without_product_operations: usize,
    pub examples_violating_own_schema: usize,
}

/// Everything derived from the specs for one product.
#[derive(Debug, Clone, Serialize)]
pub struct Build {
    pub provenance: load::Provenance,
    pub product: String,
    pub summary: Summary,
    pub apis: Vec<index::Api>,
    pub fixtures: IndexMap<String, Fixture>,
    /// Bundled OpenAPI documents keyed by api id (input for model codegen and
    /// the runtime decoder).
    #[serde(skip)]
    pub bundles: IndexMap<String, Value>,
}

/// Run the full pipeline over `repo` for `product` (e.g. `"Protheus"`).
pub fn build(repo: &Path, product: &str) -> Result<Build, Error> {
    let repo = repo
        .canonicalize()
        .map_err(|e| Error::Io(repo.display().to_string(), e))?;
    let provenance = load::git_provenance(&repo)?;
    let apis_dir = repo.join("jsonschema").join("apis");
    let mut spec_paths: Vec<std::path::PathBuf> = std::fs::read_dir(&apis_dir)
        .map_err(|e| Error::Io(apis_dir.display().to_string(), e))?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| p.extension().is_some_and(|x| x == "json"))
        .collect();
    spec_paths.sort();

    let mut product_specs = Vec::new();
    for path in spec_paths {
        let raw = load::load_json(&path)?;
        let listed = raw["info"]["x-totvs"]["productInformation"]
            .as_array()
            .map(|items| items.iter().any(|p| p["product"].as_str() == Some(product)))
            .unwrap_or(false);
        if listed {
            product_specs.push(path);
        }
    }
    let filenames: Vec<String> = product_specs
        .iter()
        .map(|p| p.file_name().unwrap().to_string_lossy().to_string())
        .collect();
    let api_ids = naming::assign_api_ids(&filenames);

    let mut apis = Vec::new();
    let mut bundles = IndexMap::new();
    let mut fixtures = IndexMap::new();
    let mut skipped = 0;
    let mut defects = 0;
    for (path, filename) in product_specs.iter().zip(&filenames) {
        let (bundled, quirks) = bundle::Bundler::new(&repo, path)?.bundle()?;
        let Some(mut api) =
            index::index_api(filename, &api_ids[filename], &bundled, product, &quirks)
        else {
            skipped += 1;
            continue;
        };
        for op in &mut api.operations {
            let ok_schema = op
                .responses
                .iter()
                .find(|(s, r)| s.starts_with('2') && r.schema.is_some())
                .map(|(s, r)| (s.clone(), r.schema.clone().unwrap()));
            let Some((status, schema)) = ok_schema else {
                continue;
            };
            let body = example::example_from_schema(
                Some(&serde_json::json!({"$ref": format!("#/components/schemas/{schema}")})),
                &bundled,
            );
            let verdict = match validate::validator_for(&bundled, &schema) {
                Ok(validator) => validate::verdict(&validator, &body),
                Err(message) => index::Verdict {
                    ok: false,
                    error: Some(message),
                },
            };
            if !verdict.ok {
                defects += 1;
            }
            let mut ev = IndexMap::new();
            ev.insert("schema".to_string(), verdict);
            op.example_validation = Some(ev);
            fixtures.insert(
                op.id.clone(),
                Fixture {
                    status: status.parse().unwrap_or(200),
                    body,
                },
            );
        }
        bundles.insert(api.id.clone(), bundled);
        apis.push(api);
    }
    apis.sort_by(|a, b| a.id.cmp(&b.id));
    let summary = Summary {
        apis: apis.len(),
        operations: apis.iter().map(|a| a.operations.len()).sum(),
        apis_without_product_operations: skipped,
        examples_violating_own_schema: defects,
    };
    Ok(Build {
        provenance,
        product: product.to_string(),
        summary,
        apis,
        fixtures,
        bundles,
    })
}

/// Write `spec-index.json`, `fixtures.json` and `bundles/<api_id>.json` into `out_dir`.
pub fn write_build(build: &Build, out_dir: &Path) -> Result<(), Error> {
    let io = |p: &Path, e: std::io::Error| Error::Io(p.display().to_string(), e);
    let bundles_dir = out_dir.join("bundles");
    std::fs::create_dir_all(&bundles_dir).map_err(|e| io(&bundles_dir, e))?;
    let index_path = out_dir.join("spec-index.json");
    std::fs::write(
        &index_path,
        serde_json::to_vec(build).map_err(|e| Error::Json("spec-index".into(), e))?,
    )
    .map_err(|e| io(&index_path, e))?;
    let fixtures_path = out_dir.join("fixtures.json");
    std::fs::write(
        &fixtures_path,
        serde_json::to_vec(&build.fixtures).map_err(|e| Error::Json("fixtures".into(), e))?,
    )
    .map_err(|e| io(&fixtures_path, e))?;
    for (id, bundled) in &build.bundles {
        let path = bundles_dir.join(format!("{id}.json"));
        std::fs::write(
            &path,
            serde_json::to_vec(bundled).map_err(|e| Error::Json(id.clone(), e))?,
        )
        .map_err(|e| io(&path, e))?;
    }
    Ok(())
}
