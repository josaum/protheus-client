//! `cargo run --release -p ttalk-fast-core --example profile <schemas.json> <SchemaName> <page.json>`
use std::time::Instant;
fn main() {
    let args: Vec<String> = std::env::args().collect();
    let bundled: serde_json::Value =
        serde_json::from_slice(&std::fs::read(&args[1]).unwrap()).unwrap();
    let body = std::fs::read(&args[3]).unwrap();
    let dec = ttalk_fast_core::arrow::Decoder::new(&bundled, &args[2], "items", 100).unwrap();
    let (batch, report) = dec.decode(&body).unwrap();
    println!(
        "rows={} cols={} invalid={} violations={} demoted={:?}",
        batch.num_rows(),
        batch.num_columns(),
        report.invalid_rows,
        report.violations.len(),
        report.demoted_fields
    );
    for _ in 0..3 {
        dec.decode(&body).unwrap();
    }
    let n = 20;
    let t = Instant::now();
    for _ in 0..n {
        dec.decode(&body).unwrap();
    }
    println!(
        "decode+validate: {:.2} ms/page",
        t.elapsed().as_secs_f64() * 1e3 / n as f64
    );
    let t = Instant::now();
    for _ in 0..n {
        dec.decode_ipc(&body).unwrap();
    }
    println!(
        "decode+validate+ipc: {:.2} ms/page",
        t.elapsed().as_secs_f64() * 1e3 / n as f64
    );
}
