#!/usr/bin/env python3
"""Bind every release artifact to its SHA-256, SBOM, and exact source commit."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import zipfile
from datetime import UTC, datetime
from pathlib import Path

SCHEMA = "protheus-client.release.v1"
SUFFIXES = (".whl", ".tgz", ".tar.gz")


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def git(*arguments: str) -> str:
    return subprocess.run(["git", *arguments], check=True, text=True, capture_output=True).stdout.strip()


def sbom_for(path: Path) -> str:
    if path.name.startswith("ttalk-fast-cli-"):
        return "ttalk-fast-cli.cdx.json"
    if path.name.startswith("ttalk-fast-node-"):
        return "ttalk-fast-node.cdx.json"
    if path.name.startswith("totvs_protheus-"):
        return "totvs-protheus.cdx.json"
    if path.name.startswith("ttalk_fast-"):
        return "embedded:ttalk-fast-core.cyclonedx.json"
    raise ValueError(f"unrecognized release artifact: {path.name}")


def verify_native_wheel(path: Path) -> None:
    with zipfile.ZipFile(path) as archive:
        members = [name for name in archive.namelist() if "/sboms/" in name and name.endswith(".json")]
        if len(members) != 1 or not members[0].endswith("ttalk-fast-core.cyclonedx.json"):
            raise ValueError(f"{path.name} must contain exactly one core CycloneDX SBOM")
        if json.loads(archive.read(members[0])).get("bomFormat") != "CycloneDX":
            raise ValueError(f"{path.name} contains an invalid SBOM")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts", default="artifacts", type=Path)
    parser.add_argument("--sbom-dir", default="sboms", type=Path)
    parser.add_argument("--source-commit", default=None)
    parser.add_argument("--source-repository", default=None)
    parser.add_argument("--allow-dirty", action="store_true")
    args = parser.parse_args()

    commit = args.source_commit or git("rev-parse", "HEAD")
    repository = args.source_repository or git("remote", "get-url", "origin")
    dirty = bool(git("status", "--porcelain", "--untracked-files=no"))
    if dirty and not args.allow_dirty:
        raise SystemExit("source tree is dirty; commit before producing a release")
    files = sorted(path for path in args.artifacts.iterdir() if path.is_file() and path.name.endswith(SUFFIXES))
    if not files:
        raise SystemExit("no release artifacts found")

    sbom_names = sorted({sbom_for(path) for path in files if not sbom_for(path).startswith("embedded:")})
    sboms = []
    for name in sbom_names:
        path = args.sbom_dir / name
        document = json.loads(path.read_text(encoding="utf-8"))
        if document.get("bomFormat") != "CycloneDX":
            raise ValueError(f"{path} is not CycloneDX")
        sboms.append({"file": name, "sha256": digest(path), "bytes": path.stat().st_size})

    artifacts = []
    for path in files:
        if path.name.startswith("ttalk_fast-"):
            verify_native_wheel(path)
        artifacts.append(
            {
                "file": path.name,
                "bytes": path.stat().st_size,
                "sha256": digest(path),
                "sbom": sbom_for(path),
            }
        )
    manifest = {
        "schema_version": SCHEMA,
        "generated_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "source": {"repository": repository, "commit": commit, "dirty": dirty},
        "artifacts": artifacts,
        "sboms": sboms,
    }
    destination = args.artifacts / "release-manifest.json"
    destination.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {destination} for {len(artifacts)} artifacts at {commit}")


if __name__ == "__main__":
    main()
