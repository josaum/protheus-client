//! `ttalk_fast` — Python bindings for `ttalk-fast-core`.
//!
//! ```python
//! import ttalk_fast
//! summary = ttalk_fast.build_spec_index("/path/to/ttalk-standard-message", "Protheus", "build/")
//! dec = ttalk_fast.Decoder(open("bundle.json").read(), "PagedCustomerVendors", "items")
//! ipc, report = dec.decode(body_bytes)   # Arrow IPC stream + JSON report
//! ```

use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyDict};
use std::path::Path;
use std::time::Duration;
use ttalk_fast_core::arrow::DecodeLimits;

pyo3::create_exception!(ttalk_fast, DecodeError, PyValueError);
pyo3::create_exception!(ttalk_fast, ResourceLimitError, DecodeError);

fn decode_err(error: ttalk_fast_core::Error) -> PyErr {
    let message = error.to_string();
    if matches!(error, ttalk_fast_core::Error::ResourceLimit { .. }) {
        ResourceLimitError::new_err(message)
    } else {
        DecodeError::new_err(message)
    }
}

fn usize_limit(dict: &Bound<'_, PyDict>, name: &str, default: usize) -> PyResult<usize> {
    Ok(dict
        .get_item(name)?
        .map(|value| value.extract::<usize>())
        .transpose()?
        .unwrap_or(default))
}

fn decode_limits(dict: Option<Bound<'_, PyDict>>) -> PyResult<DecodeLimits> {
    let mut limits = DecodeLimits::default();
    let Some(dict) = dict else {
        return Ok(limits);
    };
    const KEYS: &[&str] = &[
        "max_input_bytes",
        "max_rows",
        "max_columns",
        "max_nesting_depth",
        "max_string_length",
        "max_array_length",
        "max_decode_time_ms",
        "max_ipc_bytes",
    ];
    for key in dict.keys().iter() {
        let key = key.extract::<String>()?;
        if !KEYS.contains(&key.as_str()) {
            return Err(PyValueError::new_err(format!(
                "unknown decoder limit {key:?}"
            )));
        }
    }
    limits.max_input_bytes = usize_limit(&dict, "max_input_bytes", limits.max_input_bytes)?;
    limits.max_rows = usize_limit(&dict, "max_rows", limits.max_rows)?;
    limits.max_columns = usize_limit(&dict, "max_columns", limits.max_columns)?;
    limits.max_nesting_depth = usize_limit(&dict, "max_nesting_depth", limits.max_nesting_depth)?;
    limits.max_string_length = usize_limit(&dict, "max_string_length", limits.max_string_length)?;
    limits.max_array_length = usize_limit(&dict, "max_array_length", limits.max_array_length)?;
    limits.max_ipc_bytes = usize_limit(&dict, "max_ipc_bytes", limits.max_ipc_bytes)?;
    if let Some(milliseconds) = dict
        .get_item("max_decode_time_ms")?
        .map(|value| value.extract::<u64>())
        .transpose()?
    {
        limits.max_decode_time = Some(Duration::from_millis(milliseconds));
    }
    Ok(limits)
}

/// Run the spec engine over a TTALK checkout and write `spec-index.json`,
/// `fixtures.json` and `bundles/<api_id>.json` into `out_dir`. Returns the
/// summary as a JSON string.
#[pyfunction]
#[pyo3(signature = (repo, product = "Protheus", out_dir = "ttalk-build"))]
fn build_spec_index(py: Python<'_>, repo: &str, product: &str, out_dir: &str) -> PyResult<String> {
    let (repo, product, out_dir) = (repo.to_string(), product.to_string(), out_dir.to_string());
    let summary = py.detach(move || -> Result<String, String> {
        let build =
            ttalk_fast_core::build(Path::new(&repo), &product).map_err(|e| e.to_string())?;
        ttalk_fast_core::write_build(&build, Path::new(&out_dir)).map_err(|e| e.to_string())?;
        serde_json::to_string(&build.summary).map_err(|e| e.to_string())
    });
    summary.map_err(PyRuntimeError::new_err)
}

/// Decode response pages of one operation into Arrow, validating every row
/// against the bundled schema and reporting violations and field demotions.
#[pyclass(frozen)]
struct Decoder {
    inner: ttalk_fast_core::arrow::Decoder,
}

#[pymethods]
impl Decoder {
    /// `bundle_json`: the bundled OpenAPI document (or just `{"components": {"schemas": …}}`)
    /// as a JSON string; `schema_name`: the response component name.
    #[new]
    #[pyo3(signature = (bundle_json, schema_name, items_key = "items", max_violations = 100, limits = None))]
    fn new(
        bundle_json: &str,
        schema_name: &str,
        items_key: &str,
        max_violations: usize,
        limits: Option<Bound<'_, PyDict>>,
    ) -> PyResult<Self> {
        let bundled: serde_json::Value = serde_json::from_str(bundle_json)
            .map_err(|e| PyValueError::new_err(format!("bundle_json: {e}")))?;
        let limits = decode_limits(limits)?;
        let inner = ttalk_fast_core::arrow::Decoder::with_limits(
            &bundled,
            schema_name,
            items_key,
            max_violations,
            limits,
        )
        .map_err(decode_err)?;
        Ok(Self { inner })
    }

    /// Decode one page. Returns `(arrow_ipc_stream: bytes, report_json: str)`.
    fn decode<'py>(&self, py: Python<'py>, body: &[u8]) -> PyResult<(Bound<'py, PyBytes>, String)> {
        let body = body.to_vec();
        let inner = &self.inner;
        let (ipc, report) = py
            .detach(move || inner.decode_ipc(&body))
            .map_err(decode_err)?;
        let report =
            serde_json::to_string(&report).map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
        Ok((PyBytes::new(py, &ipc), report))
    }

    /// Current Arrow schema (after any demotions) as `[{"name", "type"}]` JSON.
    fn fields(&self) -> String {
        let schema = self.inner.schema();
        let fields: Vec<serde_json::Value> = schema
            .fields()
            .iter()
            .map(|f| serde_json::json!({"name": f.name(), "type": format!("{}", f.data_type())}))
            .collect();
        serde_json::Value::Array(fields).to_string()
    }
}

#[pymodule]
fn ttalk_fast(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(build_spec_index, m)?)?;
    m.add_class::<Decoder>()?;
    m.add("DecodeError", m.py().get_type::<DecodeError>())?;
    m.add(
        "ResourceLimitError",
        m.py().get_type::<ResourceLimitError>(),
    )?;
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}
