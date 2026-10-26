#!/usr/bin/env python3
"""Verify release provenance, artifact completeness, SBOMs, and SHA256SUMS."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from release_manifest import SCHEMA, digest, verify_native_wheel


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts", default="artifacts", type=Path)
    parser.add_argument("--sbom-dir", default="sboms", type=Path)
    parser.add_argument("--allow-dirty", action="store_true")
    args = parser.parse_args()

    manifest = json.loads((args.artifacts / "release-manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != SCHEMA:
        raise SystemExit("unexpected release manifest schema")
    source = manifest.get("source", {})
    if not re.fullmatch(r"[0-9a-f]{40}", source.get("commit", "")):
        raise SystemExit("manifest has no full source commit")
    if source.get("dirty") and not args.allow_dirty:
        raise SystemExit("manifest records a dirty source tree")

    declared = {item["file"]: item for item in manifest["artifacts"]}
    present = {
        path.name: path
        for path in args.artifacts.iterdir()
        if path.is_file() and path.name.endswith((".whl", ".tgz", ".tar.gz"))
    }
    if declared.keys() != present.keys():
        raise SystemExit(f"artifact set differs: declared={sorted(declared)}, present={sorted(present)}")
    for name, item in declared.items():
        path = present[name]
        if digest(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            raise SystemExit(f"hash or size mismatch: {name}")
        if name.startswith("ttalk_fast-"):
            verify_native_wheel(path)

    for item in manifest["sboms"]:
        path = args.sbom_dir / item["file"]
        if digest(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            raise SystemExit(f"SBOM hash or size mismatch: {item['file']}")

    checksum_path = args.artifacts / "SHA256SUMS"
    checksums = dict(reversed(line.split("  ", 1)) for line in checksum_path.read_text().splitlines())
    expected = {
        path.name: path
        for path in args.artifacts.iterdir()
        if path.is_file() and path.name != "SHA256SUMS"
    }
    if checksums.keys() != expected.keys():
        raise SystemExit("SHA256SUMS file set differs from release directory")
    for name, expected_hash in checksums.items():
        if digest(expected[name]) != expected_hash:
            raise SystemExit(f"SHA256SUMS mismatch: {name}")
    print(f"ok: {len(declared)} artifacts and {len(manifest['sboms'])} SBOMs match {source['commit']}")


if __name__ == "__main__":
    main()
