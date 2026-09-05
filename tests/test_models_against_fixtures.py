"""Generated models versus the examples the TOTVS schemas themselves provide.

The fixture bodies are derived from the specs' ``example``/``examples`` values
by the engine. Each operation carries two verdicts on its example:
``example_validation.schema`` (JSON Schema, computed in Rust) and
``example_validation.model`` (pydantic, computed here). Where an example
contradicts its own schema (an upstream defect) the verdict is ``ok == False``;
this test pins the pydantic verdict both ways, so a regenerated index and a
stale fixture file can never disagree silently.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any

import pytest
from pydantic import ValidationError

from protheus import spec

CASES = [op for op in spec.iter_operations() if op["response_model"]]
WITH_FIXTURE = [op for op in spec.iter_operations() if op["example_validation"]]


@pytest.mark.parametrize("op", CASES, ids=[op["id"] for op in CASES])
def test_response_model_matches_index_verdict(op: dict[str, Any], responses: dict[str, Any]) -> None:
    fixture = responses.get(op["id"])
    verdict = (op["example_validation"] or {}).get("model")
    if fixture is None:
        assert verdict is None, "index claims a verdict but no fixture exists"
        pytest.skip("no example derivable from the spec")
    assert verdict is not None, "fixture exists but the index has no pydantic verdict"

    model = getattr(import_module(f"protheus.models.{op['api_id']}"), op["response_model"])
    try:
        parsed = model.model_validate(fixture["body"])
    except (ValidationError, TypeError) as exc:
        assert not verdict["ok"], f"index says the example validates, but: {exc}"
        pytest.xfail(f"upstream example defect: {verdict['error']}")
    assert verdict["ok"], "example now validates; regenerate the index"
    # round-trip keeps wire names, so a parsed model can be sent back as a body
    model.model_validate(parsed.model_dump(mode="json", by_alias=True, exclude_none=True))


def test_defect_counts_match_summary() -> None:
    summary = spec.load_index()["summary"]
    model = sum(
        1 for op in WITH_FIXTURE if "model" in op["example_validation"] and not op["example_validation"]["model"]["ok"]
    )
    schema = sum(1 for op in WITH_FIXTURE if not op["example_validation"]["schema"]["ok"])
    assert model == summary["response_examples_violating_pydantic_model"]
    assert schema == summary["response_examples_violating_json_schema"]


@pytest.mark.parametrize("op", WITH_FIXTURE, ids=[op["id"] for op in WITH_FIXTURE])
def test_schema_verdict_is_well_formed(op: dict[str, Any], responses: dict[str, Any]) -> None:
    """Every fixture has a JSON-Schema verdict from the engine; a failing one names a location."""
    verdict = op["example_validation"]["schema"]
    assert op["id"] in responses
    assert isinstance(verdict["ok"], bool)
    if verdict["ok"]:
        assert verdict["error"] is None
    else:
        assert verdict["error"] and " at " in verdict["error"]
