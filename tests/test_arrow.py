"""The Arrow path: raw bytes from the client, decoded and validated by ttalk_fast."""

from __future__ import annotations

import json

import httpx
import pytest
from conftest import BASE_URL, Recorder

from protheus import AsyncProtheusClient, ProtheusClient, ProtheusError
from protheus import arrow as parrow

pytestmark = pytest.mark.skipif(not parrow.AVAILABLE, reason="ttalk_fast extension not installed")
pyarrow = pytest.importorskip("pyarrow", reason="pyarrow needed to read IPC in tests")

OP = "region_groups_v1.list_regiongroups"


def _pages(request: httpx.Request) -> httpx.Response:
    page = int(request.url.params.get("page", "1"))
    rows = [
        {"Code": f"R{page}", "Description": "Sul", "ISSRate": 5.2},
        {"Code": f"Q{page}", "Description": "Norte", "ISSRate": "5,2", "TopGroup": 7},  # live-data style defects
    ]
    return httpx.Response(200, json={"hasNext": page < 2, "items": rows})


def test_decoder_validates_and_demotes_but_keeps_every_row() -> None:
    decoder = parrow.ArrowDecoder(OP)
    body = json.dumps(
        {"hasNext": False, "items": [{"Code": "R1", "ISSRate": 5.2}, {"Code": "Q1", "ISSRate": "5,2"}]}
    ).encode()
    page = decoder.decode(body)
    table = page.to_pyarrow()
    assert table.num_rows == 2 == page.rows
    assert page.report["invalid_rows"] == 1
    assert any(v["row"] == 1 and v["path"] == "/ISSRate" for v in page.report["violations"])
    assert page.report["demoted_fields"] == ["ISSRate"]
    assert table.schema.field("ISSRate").type == pyarrow.string()
    assert table.column("ISSRate").to_pylist() == ["5.2", "5,2"]
    # settled: a clean page keeps the demoted type, so batches concatenate
    clean = decoder.decode(json.dumps({"hasNext": False, "items": [{"Code": "R2", "ISSRate": 1.0}]}).encode(), 2)
    assert clean.to_pyarrow().schema.field("ISSRate").type == pyarrow.string()
    assert clean.report["demoted_fields"] == ["ISSRate"]


def test_typed_report_retains_mapping_compatibility() -> None:
    decoder = parrow.ArrowDecoder(OP, max_violations=0)
    body = json.dumps({"items": [{"Code": "TOOLONGCODE1"}, {"Code": "TOOLONGCODE2"}]}).encode()
    report = decoder.decode(body).report
    assert isinstance(report, parrow.DecodeReport)
    assert report.invalid_rows == report["invalid_rows"] == 2
    assert report.violation_count == 2
    assert report.violations == [] and report["violations"] == []
    assert report.violations_truncated
    assert report.to_dict()["violation_count"] == 2


def test_demotions_include_type_provenance() -> None:
    decoder = parrow.ArrowDecoder(OP)
    body = json.dumps({"items": [{"Code": "R1", "ISSRate": "5,2"}]}).encode()
    report = decoder.decode(body).report
    assert report.demoted_fields == ["ISSRate"]
    assert report.demotions == [
        parrow.DemotedField("ISSRate", "Float64", "Utf8", "invalid_number")
    ]
    # The native compatibility API still returns a JSON string.
    _, native_report = decoder._inner.decode(body)
    assert isinstance(native_report, str)
    assert json.loads(native_report)["demoted_fields"] == ["ISSRate"]


def test_resource_limits_and_decode_errors_are_distinct() -> None:
    decoder = parrow.ArrowDecoder(OP, limits=parrow.DecodeLimits(max_rows=1))
    body = json.dumps({"items": [{"Code": "R1"}, {"Code": "R2"}]}).encode()
    with pytest.raises(parrow.ResourceLimitError, match="resource_limit_exceeded: rows"):
        decoder.decode(body)
    with pytest.raises(parrow.DecodeError, match="decode_failed: invalid JSON"):
        decoder.decode(b'{"items":[}')
    with pytest.raises(ValueError, match="unknown decoder limit"):
        parrow.ArrowDecoder(OP, limits={"not_a_limit": 1})


def test_raw_group_and_paged_extraction(recorder: Recorder) -> None:
    recorder.rule = _pages
    with ProtheusClient(BASE_URL, transport=httpx.MockTransport(recorder)) as client:
        group = parrow.raw(client.region_groups_v1)
        assert isinstance(group.list_regiongroups(page=1), bytes)
        pages = list(parrow.iter_arrow_pages(group.list_regiongroups, OP, page_size=2))
    assert [p.number for p in pages] == [1, 2]
    assert [p.has_next for p in pages] == [True, False]
    assert [r.url.params["pageSize"] for r in recorder.requests[1:]] == ["2", "2"]
    table = pyarrow.concat_tables([p.to_pyarrow() for p in pages])
    assert table.num_rows == 4
    assert table.column("Code").to_pylist() == ["R1", "Q1", "R2", "Q2"]
    assert table.schema.field("ISSRate").type == pyarrow.string()  # demoted on page 1, stable on page 2


def test_raw_group_raises_protheus_error_on_http_error(recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(500, json={"code": "500", "message": "boom", "detailedMessage": "-"}))
    with ProtheusClient(BASE_URL, transport=httpx.MockTransport(recorder)) as client, pytest.raises(ProtheusError):
        parrow.raw(client.region_groups_v1).list_regiongroups()


async def test_async_paged_extraction(recorder: Recorder) -> None:
    recorder.rule = _pages
    async with AsyncProtheusClient(BASE_URL, transport=httpx.MockTransport(recorder)) as client:
        group = parrow.raw(client.region_groups_v1)
        pages = [p async for p in parrow.aiter_arrow_pages(group.list_regiongroups, OP, max_pages=1)]
    assert len(pages) == 1 and pages[0].rows == 2


def test_unknown_operation_and_missing_schema() -> None:
    with pytest.raises(KeyError):
        parrow.ArrowDecoder("nope.nope")
    with pytest.raises(ValueError):
        parrow.ArrowDecoder("accounting_calendar_v1.delete_accounting_calendar_by_internal_id")
