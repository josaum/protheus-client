#!/usr/bin/env python3
"""Generate a runtime-only CycloneDX SBOM for the pure Python package."""

from __future__ import annotations

import argparse
import json
import re
import tomllib
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()

    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    name = project["name"]
    version = project["version"]
    package_ref = f"pkg:pypi/{name}@{version}"
    components = []
    dependencies = []
    for requirement in project.get("dependencies", []):
        dependency = re.split(r"[<>=!~;\s]", requirement, maxsplit=1)[0]
        reference = f"pkg:pypi/{dependency}"
        components.append(
            {
                "bom-ref": reference,
                "type": "library",
                "name": dependency,
                "purl": reference,
                "properties": [{"name": "protheus:requirement", "value": requirement}],
            }
        )
        dependencies.append(reference)
    document = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, f'{package_ref}@{args.source_commit}')}",
        "version": 1,
        "metadata": {
            "component": {
                "bom-ref": package_ref,
                "type": "library",
                "name": name,
                "version": version,
                "purl": package_ref,
            }
        },
        "components": components,
        "dependencies": [{"ref": package_ref, "dependsOn": dependencies}],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
