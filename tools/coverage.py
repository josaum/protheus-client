#!/usr/bin/env python3
"""Prove the vendored client covers every available Protheus operation."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from pathlib import Path

METHODS = ("get", "post", "put", "patch", "delete")


def audit(repo: Path, index_path: Path) -> dict[str, object]:
    index = json.loads(index_path.read_text(encoding="utf-8"))
    available = 0
    unavailable = 0
    listed = 0
    usable_apis = 0
    response_types: Counter[str] = Counter()
    request_types: Counter[str] = Counter()
    for path in sorted((repo / "jsonschema" / "apis").glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        infos = raw.get("info", {}).get("x-totvs", {}).get("productInformation", [])
        if not any(info.get("product") == "Protheus" for info in infos):
            continue
        listed += 1
        api_available = 0
        for item in (raw.get("paths") or {}).values():
            for method in METHODS:
                operation = item.get(method)
                if not isinstance(operation, dict) or not operation:
                    continue
                op_infos = operation.get("x-totvs", {}).get("productInformation", [])
                explicit = next((info for info in op_infos if info.get("product") == "Protheus"), None)
                if explicit and explicit.get("available") is False:
                    unavailable += 1
                    continue
                available += 1
                api_available += 1
                for response in (operation.get("responses") or {}).values():
                    response_types.update((response.get("content") or {}).keys())
                request_types.update((operation.get("requestBody") or {}).get("content", {}).keys())
        if api_available:
            usable_apis += 1

    generated_operations = sum(len(api["operations"]) for api in index["apis"])
    generated_apis = len(index["apis"])
    commit = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    unsupported_responses = sorted(set(response_types) - {"application/json"})
    unsupported_requests = sorted(set(request_types) - {"application/json"})
    return {
        "source_commit": commit,
        "vendored_commit": index["provenance"]["commit"],
        "source_matches_vendored": commit == index["provenance"]["commit"],
        "protheus_listed_apis": listed,
        "usable_protheus_apis": usable_apis,
        "generated_apis": generated_apis,
        "available_operations": available,
        "generated_operations": generated_operations,
        "explicitly_unavailable_operations": unavailable,
        "operation_coverage_percent": round(generated_operations / available * 100, 3) if available else 100.0,
        "unsupported_request_content_types": unsupported_requests,
        "unsupported_response_content_types": unsupported_responses,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path, help="ttalk-standard-message checkout")
    parser.add_argument("--index", type=Path, default=Path("src/protheus/spec/index.json"))
    args = parser.parse_args()
    report = audit(args.repo, args.index)
    print(json.dumps(report, indent=2))
    failures = []
    if not report["source_matches_vendored"]:
        failures.append("vendored index is not at the source commit")
    for dimension in ("apis", "operations"):
        expected = report[f"usable_protheus_{dimension}"] if dimension == "apis" else report["available_operations"]
        if report[f"generated_{dimension}"] != expected:
            failures.append(f"generated {dimension} differ from available {dimension}")
    if report["unsupported_request_content_types"] or report["unsupported_response_content_types"]:
        failures.append("available operations contain unsupported content types")
    if failures:
        raise SystemExit("; ".join(failures))


if __name__ == "__main__":
    main()
