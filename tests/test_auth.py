from __future__ import annotations

import time

import httpx
import pytest

from protheus import BearerAuth, OAuth2PasswordAuth, ProtheusClient, ProtheusError

from conftest import BASE_URL, Recorder

TOKEN_URL = f"{BASE_URL}/api/oauth2/v1/token"


def token_response(token: str, refresh: str = "r1", expires_in: int = 3600) -> httpx.Response:
    return httpx.Response(
        200,
        json={
            "access_token": token,
            "refresh_token": refresh,
            "scope": "default",
            "token_type": "Bearer",
            "expires_in": expires_in,
        },
    )


def test_bearer_auth_header(recorder: Recorder) -> None:
    with ProtheusClient(BASE_URL, auth=BearerAuth("abc"), transport=httpx.MockTransport(recorder)) as client:
        client.user_v1.list_users()
    assert recorder.last.headers["authorization"] == "Bearer abc"


def test_oauth2_password_grant_uses_query_string_and_caches(recorder: Recorder) -> None:
    recorder.queue += [
        token_response("t1"),
        httpx.Response(200, json={"items": []}),
        httpx.Response(200, json={"items": []}),
    ]
    auth = OAuth2PasswordAuth("admin", "s3cret")
    with ProtheusClient(BASE_URL, auth=auth, transport=httpx.MockTransport(recorder)) as client:
        assert auth.token_url == TOKEN_URL
        client.user_v1.list_users()
        client.user_v1.list_users()
    token_req, first, second = recorder.requests
    assert token_req.method == "POST" and str(token_req.url).startswith(TOKEN_URL)
    assert dict(token_req.url.params) == {"grant_type": "password", "username": "admin", "password": "s3cret"}
    assert not token_req.content
    assert first.headers["authorization"] == "Bearer t1"
    assert second.headers["authorization"] == "Bearer t1"
    assert len(recorder.requests) == 3, "token must be fetched once"


def test_oauth2_refresh_grant_when_expired(recorder: Recorder) -> None:
    auth = OAuth2PasswordAuth("admin", "s3cret", token_url=TOKEN_URL)
    auth.access_token, auth.refresh_token, auth.expires_at = "old", "r-old", time.monotonic() - 1
    recorder.queue += [token_response("t2", refresh="r2"), httpx.Response(200, json={})]
    with ProtheusClient(BASE_URL, auth=auth, transport=httpx.MockTransport(recorder)) as client:
        client.user_v1.list_users()
    refresh_req = recorder.requests[0]
    assert dict(refresh_req.url.params) == {"grant_type": "refresh_token", "refresh_token": "r-old"}
    assert recorder.requests[1].headers["authorization"] == "Bearer t2"
    assert auth.refresh_token == "r2"


def test_oauth2_refresh_failure_falls_back_to_password(recorder: Recorder) -> None:
    auth = OAuth2PasswordAuth("admin", "s3cret", token_url=TOKEN_URL)
    auth.access_token, auth.refresh_token, auth.expires_at = "old", "r-old", 0.0
    recorder.queue += [
        httpx.Response(401, json={"code": "401", "message": "refresh expired", "detailedMessage": "-"}),
        token_response("t3"),
        httpx.Response(200, json={}),
    ]
    with ProtheusClient(BASE_URL, auth=auth, transport=httpx.MockTransport(recorder)) as client:
        client.user_v1.list_users()
    grants = [dict(r.url.params).get("grant_type") for r in recorder.requests[:2]]
    assert grants == ["refresh_token", "password"]
    assert recorder.requests[2].headers["authorization"] == "Bearer t3"


def test_oauth2_regrants_once_on_401(recorder: Recorder) -> None:
    auth = OAuth2PasswordAuth("admin", "s3cret", token_url=TOKEN_URL)
    auth.access_token, auth.expires_at = "stale", time.monotonic() + 3600
    recorder.queue += [
        httpx.Response(401, json={"code": "401", "message": "token revoked", "detailedMessage": "-"}),
        token_response("fresh"),
        httpx.Response(200, json={"ok": True}),
    ]
    with ProtheusClient(BASE_URL, auth=auth, transport=httpx.MockTransport(recorder)) as client:
        assert client.user_v1.list_users() == {"ok": True}
    assert [h.get("authorization") for h in recorder.headers] == ["Bearer stale", None, "Bearer fresh"]


def test_oauth2_bad_credentials_raise_protheus_error(recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(401, json={"code": "401", "message": "invalid_grant", "detailedMessage": "-"}))
    with ProtheusClient(
        BASE_URL, auth=OAuth2PasswordAuth("admin", "wrong"), transport=httpx.MockTransport(recorder)
    ) as client:
        with pytest.raises(ProtheusError) as info:
            client.user_v1.list_users()
    assert info.value.operation == "oauth2.token"
    assert info.value.is_auth_error


async def test_oauth2_works_with_async_client(recorder: Recorder) -> None:
    from protheus import AsyncProtheusClient

    recorder.queue += [token_response("ta"), httpx.Response(200, json={"items": [1]})]
    async with AsyncProtheusClient(
        BASE_URL, auth=OAuth2PasswordAuth("u", "p"), transport=httpx.MockTransport(recorder)
    ) as client:
        assert await client.user_v1.list_users() == {"items": [1]}
    assert recorder.requests[1].headers["authorization"] == "Bearer ta"
