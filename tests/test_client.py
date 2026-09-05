from __future__ import annotations

import httpx
import pytest
from pydantic import BaseModel, Field

from protheus import AsyncProtheusClient, ProtheusClient, ProtheusError, ProtheusTransportError
from protheus._base import prepare

from conftest import BASE_URL, Recorder


# ----------------------------------------------------------------- prepare()
def test_prepare_encodes_path_and_drops_none_query() -> None:
    req = prepare(
        "op",
        "GET",
        "/api/crm/v1",
        "/customerVendor/{entityType}/{id}",
        path_params={"entityType": "customer", "id": "D MG 01/000001"},
        query={"fields": None, "order": ["-code", "name"], "page": 2, "active": True},
        headers={"X-Trace": None, "X-Tenant": "t1"},
        body=None,
        extra_query={"branchId": "01"},
    )
    assert req.path == "/api/crm/v1/customerVendor/customer/D%20MG%2001%2F000001"
    assert req.params == {"order": "-code,name", "page": "2", "active": "true", "branchId": "01"}
    assert req.headers == {"X-Tenant": "t1"}
    assert req.json is None


def test_prepare_rejects_missing_path_param() -> None:
    with pytest.raises(ValueError, match="path parameter 'id' is required"):
        prepare("op", "GET", "/b", "/x/{id}", path_params={"id": ""}, query={}, headers={}, body=None, extra_query=None)


def test_prepare_serialises_pydantic_body_by_alias_without_none() -> None:
    class Info(BaseModel):
        customer_id: str = Field(alias="customerId")
        name: str | None = None

    req = prepare(
        "op", "POST", "/b", "/x", path_params={}, query={}, headers={}, body=Info(customerId="1"), extra_query=None
    )
    assert req.json == {"customerId": "1"}


# ------------------------------------------------------------------- client
def test_client_sends_defaults_and_decodes_json(client: ProtheusClient, recorder: Recorder) -> None:
    result = client.customer_vendor_v1.get_customer_vendor_by_entity_type("customer")
    assert result == {"hasNext": False, "items": []}
    req = recorder.last
    assert str(req.url) == f"{BASE_URL}/api/crm/v1/customerVendor/customer"
    assert req.headers["accept"] == "application/json"


def test_accept_language_and_custom_headers(recorder: Recorder) -> None:
    with ProtheusClient(
        BASE_URL, accept_language="pt-BR", headers={"X-Tenant": "acme"}, transport=httpx.MockTransport(recorder)
    ) as client:
        client.user_v1.list_users()
    assert recorder.last.headers["accept-language"] == "pt-BR"
    assert recorder.last.headers["x-tenant"] == "acme"


def test_no_content_returns_none(client: ProtheusClient, recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(204))
    assert (
        client.customer_vendor_v1.delete_customer_vendor_by_entity_type_and_customer_vendor_id("customer", "1") is None
    )
    assert recorder.last.method == "DELETE"


def test_ttalk_error_envelope(client: ProtheusClient, recorder: Recorder) -> None:
    recorder.queue.append(
        httpx.Response(
            400,
            json={
                "code": "E001",
                "message": "Registro inválido",
                "detailedMessage": "Campo A1_COD obrigatório",
                "helpUrl": "https://tdn.totvs.com/x",
                "details": [{"code": "A1_COD", "message": "obrigatório", "detailedMessage": "-"}],
            },
        )
    )
    with pytest.raises(ProtheusError) as info:
        client.customer_vendor_v1.create_customer_vendor(body={"code": ""})
    err = info.value
    assert (err.status_code, err.code, err.message) == (400, "E001", "Registro inválido")
    assert err.detailed_message == "Campo A1_COD obrigatório"
    assert err.details[0]["code"] == "A1_COD"
    assert err.operation == "customer_vendor_v1.create_customer_vendor"
    assert "E001" in str(err) and "create_customer_vendor" in str(err)


def test_non_ttalk_error_body_is_kept_raw(client: ProtheusClient, recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(502, text="<html>Bad Gateway</html>"))
    with pytest.raises(ProtheusError) as info:
        client.user_v1.list_users()
    assert info.value.code == "502"
    assert info.value.body == "<html>Bad Gateway</html>"
    assert not info.value.is_auth_error


def test_transport_error_is_wrapped() -> None:
    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("refused", request=request)

    with ProtheusClient(BASE_URL, transport=httpx.MockTransport(boom)) as client:
        with pytest.raises(ProtheusTransportError) as info:
            client.user_v1.list_users()
    assert info.value.operation == "user_v1.list_users"
    assert isinstance(info.value.cause, httpx.ConnectError)


def test_non_json_success_body_returns_text(client: ProtheusClient, recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(200, text="OK", headers={"content-type": "text/plain"}))
    assert client.user_v1.list_users() == "OK"


async def test_async_client_same_surface(aclient: AsyncProtheusClient, recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(200, json={"hasNext": True, "items": [{"code": "1"}]}))
    result = await aclient.customer_vendor_v1.get_customer_vendor_by_entity_type("vendor", page=3)
    assert result["items"][0]["code"] == "1"
    assert recorder.last.url.params["page"] == "3"


async def test_async_error_envelope(aclient: AsyncProtheusClient, recorder: Recorder) -> None:
    recorder.queue.append(httpx.Response(404, json={"code": "404", "message": "nope", "detailedMessage": "-"}))
    with pytest.raises(ProtheusError) as info:
        await aclient.user_v1.get_users_by_id("x")
    assert info.value.is_not_found
