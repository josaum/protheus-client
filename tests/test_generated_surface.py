"""Every operation in the index must be callable and produce the request the spec describes.

This is the contract between the vendored index, the generated facade and the
request builder: if the generator drifts (renamed method, lost parameter,
wrong base path), one of these parametrized cases fails and names the operation.
"""

from __future__ import annotations

import inspect
import re
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from protheus import ProtheusClient, spec
from protheus.apis import API_IDS

from conftest import BASE_URL, Recorder

OPERATIONS = list(spec.iter_operations())
STANDARD_TO_PYTHON = {
    "fields": "fields",
    "order": "order",
    "page": "page",
    "pageSize": "page_size",
    "filter": "filter",
    "expand": "expand",
}


def _placeholder(type_name: str) -> Any:
    return {"int": 7, "float": 1.5, "bool": True, "list[str]": ["a", "b"], "dict[str, Any]": {"k": "v"}}.get(
        type_name, "val"
    )


def test_api_ids_match_index() -> None:
    assert tuple(a["id"] for a in spec.apis()) == API_IDS
    assert len(set(API_IDS)) == len(API_IDS)


def test_operation_ids_unique() -> None:
    ids = [op["id"] for op in OPERATIONS]
    assert len(ids) == len(set(ids)) == spec.load_index()["summary"]["operations"]


@pytest.mark.parametrize("op", OPERATIONS, ids=[op["id"] for op in OPERATIONS])
def test_operation_builds_declared_request(op: dict[str, Any]) -> None:
    recorder = Recorder(rule=lambda r: httpx.Response(200, json={"ok": True}))
    with ProtheusClient(BASE_URL, transport=httpx.MockTransport(recorder)) as client:
        group = getattr(client, op["api_id"])
        method = getattr(group, op["name"])
        assert not inspect.iscoroutinefunction(method)

        kwargs: dict[str, Any] = {p["python"]: _placeholder(p["type"]) for p in op["path_params"]}
        for p in op["query_params"] + op["header_params"]:
            kwargs[p["python"]] = _placeholder(p["type"])
        for name in op["standard_params"]:
            kwargs[STANDARD_TO_PYTHON[name]] = 3 if name in ("page", "pageSize") else "x"
        if op["request_body"]:
            kwargs["body"] = {"field": 1}
        result = method(**kwargs)

    assert result == {"ok": True}
    req = recorder.last
    assert req.method == op["method"]

    expected_path = op["path"]
    for p in op["path_params"]:
        expected_path = expected_path.replace("{" + p["name"] + "}", str(_placeholder(p["type"])).replace("'", ""))
    if any(p["type"] == "list[str]" for p in op["path_params"]):
        # list path params are comma-joined by the builder
        expected_path = re.sub(r"\[.*?\]", "a,b", expected_path)
    assert req.url.path == "/rest" + op["base_path"] + expected_path.replace(",", "%2C")

    sent = parse_qs(req.url.query.decode())
    declared = {p["name"] for p in op["query_params"]} | set(op["standard_params"])
    assert set(sent) == declared, f"query drift: sent={set(sent)} declared={declared}"
    for p in op["header_params"]:
        assert req.headers.get(p["name"]) is not None
    if op["request_body"]:
        assert req.headers.get("content-type", "").startswith("application/json")
        assert req.content
    else:
        assert not req.content


@pytest.mark.parametrize("api_id", API_IDS)
def test_async_group_mirrors_sync_group(api_id: str) -> None:
    from importlib import import_module

    module = import_module(f"protheus.apis.{api_id}")
    api = spec.get_api(api_id)
    sync_cls = getattr(module, api["class_name"])
    async_cls = getattr(module, "Async" + api["class_name"])
    for op in api["operations"]:
        s, a = getattr(sync_cls, op["name"]), getattr(async_cls, op["name"])
        assert inspect.signature(s) == inspect.signature(a)
        assert inspect.iscoroutinefunction(a) and not inspect.iscoroutinefunction(s)
