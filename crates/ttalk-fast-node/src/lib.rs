//! `ttalk_fast_node` — N-API bindings for `ttalk-fast-core`, mirroring the
//! Python wheel (`ttalk_fast`) so Node consumers (jai-pay and friends) get the
//! same spec engine and the same DOM-free Arrow page decoder.
//!
//! ```js
//! const { buildSpecIndex, Decoder } = require('ttalk-fast-node');
//! const summary = buildSpecIndex('/path/to/ttalk-standard-message', 'Protheus', 'build/');
//! const dec = new Decoder(fs.readFileSync('customer_vendor_v1.json', 'utf8'), 'PagedCustomerVendors');
//! const { ipc, report } = await dec.decodeAsync(bodyBuffer);   // ipc: Arrow IPC stream
//! ```

use napi::bindgen_prelude::*;
use napi_derive::napi;
use serde_json::Value;
use std::path::Path;
use std::sync::Arc;
use std::time::Duration;
use ttalk_fast_core::arrow::DecodeLimits;

#[napi(object)]
pub struct DecoderLimits {
    pub max_input_bytes: Option<u32>,
    pub max_rows: Option<u32>,
    pub max_columns: Option<u32>,
    pub max_nesting_depth: Option<u32>,
    pub max_string_length: Option<u32>,
    pub max_array_length: Option<u32>,
    pub max_decode_time_ms: Option<u32>,
    pub max_ipc_bytes: Option<u32>,
}

impl DecoderLimits {
    fn apply(&self, limits: &mut DecodeLimits) {
        if let Some(value) = self.max_input_bytes {
            limits.max_input_bytes = value as usize;
        }
        if let Some(value) = self.max_rows {
            limits.max_rows = value as usize;
        }
        if let Some(value) = self.max_columns {
            limits.max_columns = value as usize;
        }
        if let Some(value) = self.max_nesting_depth {
            limits.max_nesting_depth = value as usize;
        }
        if let Some(value) = self.max_string_length {
            limits.max_string_length = value as usize;
        }
        if let Some(value) = self.max_array_length {
            limits.max_array_length = value as usize;
        }
        if let Some(value) = self.max_decode_time_ms {
            limits.max_decode_time = Some(Duration::from_millis(value as u64));
        }
        if let Some(value) = self.max_ipc_bytes {
            limits.max_ipc_bytes = value as usize;
        }
    }
}

fn err(e: impl ToString) -> Error {
    Error::from_reason(e.to_string())
}

/// Crate / binding version string.
#[napi]
pub fn version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}

/// Run the spec engine over a TTALK checkout and write `spec-index.json`,
/// `fixtures.json` and `bundles/<api_id>.json` into `outDir`. Returns the summary.
#[napi]
pub fn build_spec_index(
    repo: String,
    product: Option<String>,
    out_dir: Option<String>,
) -> Result<Value> {
    let product = product.unwrap_or_else(|| "Protheus".to_string());
    let out_dir = out_dir.unwrap_or_else(|| "ttalk-build".to_string());
    let build = ttalk_fast_core::build(Path::new(&repo), &product).map_err(err)?;
    ttalk_fast_core::write_build(&build, Path::new(&out_dir)).map_err(err)?;
    serde_json::to_value(&build.summary).map_err(err)
}

/// One decoded page: an Arrow IPC stream plus the validation report.
#[napi(object)]
pub struct DecodedPage {
    pub ipc: Buffer,
    pub report: Value,
}

/// Decode response pages of one operation into Arrow, validating every row
/// against the bundled schema and reporting violations and field demotions.
#[napi]
pub struct Decoder {
    inner: Arc<ttalk_fast_core::arrow::Decoder>,
}

pub struct DecodeTask {
    inner: Arc<ttalk_fast_core::arrow::Decoder>,
    body: Vec<u8>,
}

impl Task for DecodeTask {
    type Output = (Vec<u8>, Value);
    type JsValue = DecodedPage;

    fn compute(&mut self) -> Result<Self::Output> {
        let (ipc, report) = self.inner.decode_ipc(&self.body).map_err(err)?;
        Ok((ipc, serde_json::to_value(&report).map_err(err)?))
    }

    fn resolve(&mut self, _env: Env, (ipc, report): Self::Output) -> Result<Self::JsValue> {
        Ok(DecodedPage {
            ipc: ipc.into(),
            report,
        })
    }
}

#[napi]
impl Decoder {
    /// `bundleJson`: the bundled OpenAPI document (or just `{"components": {"schemas": …}}`)
    /// as a JSON string; `schemaName`: the response component name.
    #[napi(constructor)]
    pub fn new(
        bundle_json: String,
        schema_name: String,
        items_key: Option<String>,
        max_violations: Option<u32>,
        configured_limits: Option<DecoderLimits>,
    ) -> Result<Self> {
        let bundled: Value =
            serde_json::from_str(&bundle_json).map_err(|e| err(format!("bundleJson: {e}")))?;
        let mut limits = DecodeLimits::default();
        if let Some(configured) = configured_limits {
            configured.apply(&mut limits);
        }
        let inner = ttalk_fast_core::arrow::Decoder::with_limits(
            &bundled,
            &schema_name,
            items_key.as_deref().unwrap_or("items"),
            max_violations.unwrap_or(100) as usize,
            limits,
        )
        .map_err(err)?;
        Ok(Self {
            inner: Arc::new(inner),
        })
    }

    /// Decode one page synchronously.
    #[napi]
    pub fn decode(&self, body: Buffer) -> Result<DecodedPage> {
        let (ipc, report) = self.inner.decode_ipc(&body).map_err(err)?;
        Ok(DecodedPage {
            ipc: ipc.into(),
            report: serde_json::to_value(&report).map_err(err)?,
        })
    }

    /// Decode one page on the libuv thread pool; resolves to `{ ipc, report }`.
    #[napi(ts_return_type = "Promise<DecodedPage>")]
    pub fn decode_async(&self, body: Buffer) -> AsyncTask<DecodeTask> {
        AsyncTask::new(DecodeTask {
            inner: self.inner.clone(),
            body: body.to_vec(),
        })
    }

    /// Current Arrow schema (after any demotions) as `[{ name, type }]`.
    #[napi]
    pub fn fields(&self) -> Value {
        let schema = self.inner.schema();
        Value::Array(
            schema
                .fields()
                .iter()
                .map(
                    |f| serde_json::json!({"name": f.name(), "type": format!("{}", f.data_type())}),
                )
                .collect(),
        )
    }
}
