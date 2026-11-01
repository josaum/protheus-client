"""Invariants of the vendored index that downstream catalogs rely on."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from protheus import spec

ROOT = Path(__file__).resolve().parents[1]


def test_provenance_is_pinned() -> None:
    prov = spec.provenance()
    assert prov["repository"].endswith("totvs/ttalk-standard-message")
    assert len(prov["commit"]) == 40 and prov["commit_date"]
    assert prov["product"] == "Protheus"
    assert prov["generator"].startswith("crates/ttalk-fast-core")


def test_archive_build_accepts_explicit_provenance(tmp_path: Path) -> None:
    """Source archives can be indexed without .git when provenance is supplied."""
    ttalk_fast = pytest.importorskip("ttalk_fast")
    api_dir = tmp_path / "jsonschema" / "apis"
    api_dir.mkdir(parents=True)
    minimal = {
        "openapi": "3.0.1",
        "info": {"x-totvs": {"productInformation": [{"product": "Protheus"}]}},
        "paths": {
            "/minimal": {
                "get": {
                    "operationId": "getMinimal",
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {"value": {"type": "string"}},
                                    }
                                }
                            },
                        }
                    },
                }
            }
        },
    }
    (api_dir / "minimal_v1_000.json").write_text(json.dumps(minimal), encoding="utf-8")
    provenance = {
        "repository": "https://example.test/archive",
        "commit": "abc123",
        "commit_date": "2026-01-02T03:04:05Z",
    }
    out_dir = tmp_path / "out"
    summary = json.loads(ttalk_fast.build_spec_index(str(tmp_path), "Protheus", str(out_dir), provenance))
    assert summary["apis"] == 1
    index = json.loads((out_dir / "spec-index.json").read_text(encoding="utf-8"))
    assert index["provenance"] == provenance
    with pytest.raises(ValueError, match="unknown provenance key"):
        ttalk_fast.build_spec_index(str(tmp_path), "Protheus", str(out_dir), provenance | {"unexpected": True})


def test_only_protheus_available_operations_are_indexed() -> None:
    for op in spec.iter_operations():
        assert op["availability"] in ("declared", "inherited")
        assert op["method"] in ("GET", "POST", "PUT", "PATCH", "DELETE")
        assert op["side_effect"] == (op["method"] != "GET")
        assert op["path"].startswith("/") and op["base_path"].startswith("/api/")


def test_known_totvs_facts_survive_generation() -> None:
    """Pin a few facts read straight from the specs; they guard the extraction logic."""
    cv = spec.get_operation("customer_vendor_v1.list_customer_vendor")
    assert cv["minimal_version"] == "12.1.21"
    assert "CustomerVendorEntity" in (cv["note"] or "")
    assert cv["standard_params"] == ["fields", "order", "page", "pageSize"]

    charge = spec.get_operation(
        "sales_charge_v1.get_sales_charge_by_internal_id_and_account_receivable_document_internal_id"
    )
    assert [p["name"] for p in charge["path_params"]] == ["InternalId", "AccountReceivableDocumentInternalId"]
    assert "E3_CODCLI" in charge["note"]

    # RetailSalesOrders declares Protheus at API level but no per-operation flag
    retail = spec.get_api("retail_sales_orders_v1")
    assert {op["availability"] for op in retail["operations"]} == {"inherited"}

    # explicit 'available: false' operations are excluded (Currency has none for Protheus)
    assert all(api["id"] != "currency_v1" for api in spec.apis())


def test_lookup_helpers() -> None:
    assert spec.get_api("user_v1")["base_path"] == "/api/framework/v1"
    with pytest.raises(KeyError):
        spec.get_api("nope")
    with pytest.raises(KeyError):
        spec.get_operation("nope.nope")
    side = list(spec.iter_operations(side_effect=True))
    assert side and all(op["method"] != "GET" for op in side)


@pytest.mark.skipif(not os.environ.get("TTALK_REPO"), reason="set TTALK_REPO to a ttalk-standard-message checkout")
def test_generator_is_deterministic(tmp_path: Path) -> None:
    """Regenerating from the same commit must reproduce the vendored index byte for byte."""
    index = ROOT / "src" / "protheus" / "spec" / "index.json"
    before = index.read_bytes()
    subprocess.run(
        [sys.executable, "-W", "ignore", str(ROOT / "tools" / "build.py"), os.environ["TTALK_REPO"]],
        check=True,
        capture_output=True,
    )
    assert index.read_bytes() == before


@pytest.mark.skipif(not os.environ.get("TTALK_REPO"), reason="set TTALK_REPO to a ttalk-standard-message checkout")
def test_complete_available_operation_coverage() -> None:
    subprocess.run([sys.executable, str(ROOT / "tools" / "coverage.py"), os.environ["TTALK_REPO"]], check=True)
