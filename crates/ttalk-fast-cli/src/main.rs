//! `ttalk-fast index <ttalk-repo> [--product Protheus] [--out DIR]`
//! `ttalk-fast decode <bundle.json> <SchemaName> <page.json> [--items items]`

use std::path::PathBuf;
use std::process::ExitCode;

fn usage() -> ExitCode {
    eprintln!(
        "usage:\n  ttalk-fast index <ttalk-repo> [--product Protheus] [--out DIR]\n  ttalk-fast decode <bundle.json> <SchemaName> <page.json> [--items items]"
    );
    ExitCode::from(2)
}

fn flag(args: &[String], name: &str) -> Option<String> {
    args.iter()
        .position(|a| a == name)
        .and_then(|i| args.get(i + 1).cloned())
}

fn main() -> ExitCode {
    let args: Vec<String> = std::env::args().skip(1).collect();
    match args.first().map(String::as_str) {
        Some("index") => {
            let Some(repo) = args.get(1) else {
                return usage();
            };
            let product = flag(&args, "--product").unwrap_or_else(|| "Protheus".to_string());
            let out =
                PathBuf::from(flag(&args, "--out").unwrap_or_else(|| "ttalk-build".to_string()));
            match ttalk_fast_core::build(&PathBuf::from(repo), &product) {
                Ok(build) => match ttalk_fast_core::write_build(&build, &out) {
                    Ok(()) => {
                        println!("{}", serde_json::to_string(&build.summary).unwrap());
                        ExitCode::SUCCESS
                    }
                    Err(e) => {
                        eprintln!("error: {e}");
                        ExitCode::FAILURE
                    }
                },
                Err(e) => {
                    eprintln!("error: {e}");
                    ExitCode::FAILURE
                }
            }
        }
        Some("decode") => {
            let (Some(bundle), Some(schema), Some(page)) = (args.get(1), args.get(2), args.get(3))
            else {
                return usage();
            };
            let items = flag(&args, "--items").unwrap_or_else(|| "items".to_string());
            let run = || -> Result<(), String> {
                let bundled: serde_json::Value =
                    serde_json::from_slice(&std::fs::read(bundle).map_err(|e| e.to_string())?)
                        .map_err(|e| e.to_string())?;
                let body = std::fs::read(page).map_err(|e| e.to_string())?;
                let decoder = ttalk_fast_core::arrow::Decoder::new(&bundled, schema, &items, 50)
                    .map_err(|e| e.to_string())?;
                let (batch, report) = decoder.decode(&body).map_err(|e| e.to_string())?;
                println!("{}", serde_json::to_string_pretty(&report).unwrap());
                eprintln!(
                    "{} rows x {} columns",
                    batch.num_rows(),
                    batch.num_columns()
                );
                Ok(())
            };
            match run() {
                Ok(()) => ExitCode::SUCCESS,
                Err(e) => {
                    eprintln!("error: {e}");
                    ExitCode::FAILURE
                }
            }
        }
        _ => usage(),
    }
}
