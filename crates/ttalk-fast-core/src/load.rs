//! Reading TTALK files and repository provenance.

use crate::Error;
use serde_json::Value;
use std::path::Path;
use std::process::Command;

/// Parse a TTALK JSON file. Files are UTF-8 (optionally with BOM); one
/// schema in the corpus (StopReport) is Latin-1, so decoding falls back.
pub fn load_json(path: &Path) -> Result<Value, Error> {
    let bytes = std::fs::read(path).map_err(|e| Error::Io(path.display().to_string(), e))?;
    let text = match std::str::from_utf8(&bytes) {
        Ok(s) => s.trim_start_matches('\u{feff}').to_string(),
        Err(_) => bytes.iter().map(|&b| b as char).collect(),
    };
    serde_json::from_str(&text).map_err(|e| Error::Json(path.display().to_string(), e))
}

#[derive(Debug, Clone, serde::Serialize)]
pub struct Provenance {
    pub repository: String,
    pub commit: String,
    pub commit_date: String,
}

pub fn git_provenance(repo: &Path) -> Result<Provenance, Error> {
    let git = |args: &[&str]| -> Result<String, Error> {
        let out = Command::new("git")
            .arg("-C")
            .arg(repo)
            .args(args)
            .output()
            .map_err(|e| Error::Io("git".into(), e))?;
        if !out.status.success() {
            return Err(Error::Provenance(
                String::from_utf8_lossy(&out.stderr).trim().to_string(),
            ));
        }
        Ok(String::from_utf8_lossy(&out.stdout).trim().to_string())
    };
    Ok(Provenance {
        repository: "https://github.com/totvs/ttalk-standard-message".to_string(),
        commit: git(&["rev-parse", "HEAD"])?,
        commit_date: git(&["log", "-1", "--format=%cI"])?,
    })
}
