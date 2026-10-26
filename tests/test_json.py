from __future__ import annotations

import httpx
import pytest
from conftest import BASE_URL, Recorder

from protheus import AsyncProtheusClient, JsonLimits, JsonResourceError, ProtheusClient
from protheus._json import decode_json


def test_json_preflight_preserves_values_and_enforces_each_budget() -> None:
    payload = '{"text":"Região 🦀","items":[1,true,null]}'.encode()
    assert decode_json(payload, JsonLimits()) == {"text": "Região 🦀", "items": [1, True, None]}

    cases = [
        (JsonLimits(max_input_bytes=4), "input_bytes"),
        (JsonLimits(max_tokens=2), "tokens"),
        (JsonLimits(max_retained_bytes=32), "retained_bytes"),
    ]
    for limits, resource in cases:
        with pytest.raises(JsonResourceError) as info:
            decode_json(payload, limits)
        assert info.value.code == "resource_limit_exceeded"
        assert info.value.resource == resource
        assert info.value.observed > info.value.limit


def test_sync_client_applies_json_budgets_to_success_and_error_responses(recorder: Recorder) -> None:
    limits = JsonLimits(max_tokens=2)
    with ProtheusClient(
        BASE_URL, transport=httpx.MockTransport(recorder), json_limits=limits
    ) as client, pytest.raises(JsonResourceError, match="tokens"):
        client.user_v1.list_users()

    recorder.queue.append(httpx.Response(400, json={"code": "E1", "message": "invalid"}))
    with ProtheusClient(
        BASE_URL, transport=httpx.MockTransport(recorder), json_limits=JsonLimits(max_input_bytes=4)
    ) as client, pytest.raises(JsonResourceError, match="input_bytes"):
        client.user_v1.list_users()


def test_non_json_text_fallback_is_not_rejected_by_json_budgets(recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(200, text="plain text", headers={"content-type": "text/plain"}))
    with ProtheusClient(
        BASE_URL, transport=httpx.MockTransport(recorder), json_limits=JsonLimits(max_input_bytes=1)
    ) as client:
        assert client.user_v1.list_users() == "plain text"


async def test_async_client_applies_json_budgets(recorder: Recorder) -> None:
    async with AsyncProtheusClient(
        BASE_URL, transport=httpx.MockTransport(recorder), json_limits=JsonLimits(max_tokens=2)
    ) as client:
        with pytest.raises(JsonResourceError, match="tokens"):
            await client.user_v1.list_users()
