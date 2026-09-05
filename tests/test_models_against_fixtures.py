"""Generated models versus the examples the TOTVS schemas themselves provide.

The fixture bodies are derived from the specs' ``example``/``examples`` values
by the generator. Where an example contradicts its own schema (an upstream
defect) the generator records it on the operation as
``example_validation.ok == False``; this test pins that verdict both ways, so a
regenerated index and a stale fixture file can never disagree silently.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any

import pytest
from pydantic import ValidationError

from protheus import spec

CASES = [op for op in spec.iter_operations() if op["response_model"]]


@pytest.mark.parametrize("op", CASES, ids=[op["id"] for op in CASES])
def test_response_model_matches_index_verdict(op: dict[str, Any], responses: dict[str, Any]) -> None:
    fixture = responses.get(op["id"])
    verdict = op["example_validation"]
    if fixture is None:
        assert verdict is None, "index claims a verdict but no fixture exists"
        pytest.skip("no example derivable from the spec")
    assert verdict is not None, "fixture exists but the index has no verdict"

    model = getattr(import_module(f"protheus.models.{op['api_id']}"), op["response_model"])
    try:
        parsed = model.model_validate(fixture["body"])
    except (ValidationError, TypeError) as exc:
        assert not verdict["ok"], f"index says the example validates, but: {exc}"
        pytest.xfail(f"upstream example defect: {verdict['error']}")
    assert verdict["ok"], "example now validates; regenerate the index"
    # round-trip keeps wire names, so a parsed model can be sent back as a body
    model.model_validate(parsed.model_dump(mode="json", by_alias=True, exclude_none=True))


def test_defect_count_matches_summary() -> None:
    recorded = sum(
        1 for op in spec.iter_operations() if op["example_validation"] and not op["example_validation"]["ok"]
    )
    assert recorded == spec.load_index()["summary"]["response_examples_violating_own_schema"]
