"""Request assembly shared by the sync and async clients and the generated API groups."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

from pydantic import BaseModel

if TYPE_CHECKING:
    from protheus.client import AsyncProtheusClient, ProtheusClient

Body = Mapping[str, Any] | Sequence[Any] | BaseModel


class PreparedRequest:
    __slots__ = ("operation", "method", "path", "params", "headers", "json")

    def __init__(
        self,
        operation: str,
        method: str,
        path: str,
        params: dict[str, str],
        headers: dict[str, str],
        json: Any,
    ) -> None:
        self.operation = operation
        self.method = method
        self.path = path
        self.params = params
        self.headers = headers
        self.json = json

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"PreparedRequest({self.operation}: {self.method} {self.path} params={self.params})"


def _query_value(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple, set)):
        return ",".join(str(v) for v in value)
    return str(value)


def _body_json(body: Body | None) -> Any:
    if body is None:
        return None
    if isinstance(body, BaseModel):
        return body.model_dump(mode="json", by_alias=True, exclude_none=True)
    if isinstance(body, Mapping):
        return dict(body)
    return list(body)


def prepare(
    operation: str,
    method: str,
    base_path: str,
    path_template: str,
    *,
    path_params: Mapping[str, Any],
    query: Mapping[str, Any],
    headers: Mapping[str, Any],
    body: Body | None,
    extra_query: Mapping[str, Any] | None,
) -> PreparedRequest:
    path = path_template
    for name, value in path_params.items():
        if value is None or value == "":
            raise ValueError(f"{operation}: path parameter '{name}' is required")
        rendered = _query_value(value) or ""
        path = path.replace("{" + name + "}", quote(rendered, safe=""))
    params: dict[str, str] = {}
    for source in (query, extra_query or {}):
        for name, value in source.items():
            rendered = _query_value(value)
            if rendered is not None:
                params[name] = rendered
    rendered_headers = {k: str(v) for k, v in headers.items() if v is not None}
    return PreparedRequest(operation, method, base_path + path, params, rendered_headers, _body_json(body))


class ApiGroup:
    api_id: str
    base_path: str

    def __init__(self, client: ProtheusClient) -> None:
        self._client = client

    def _request(
        self,
        operation: str,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any],
        query: Mapping[str, Any],
        headers: Mapping[str, Any],
        body: Body | None,
        extra_query: Mapping[str, Any] | None,
    ) -> Any:
        prepared = prepare(
            operation,
            method,
            self.base_path,
            path,
            path_params=path_params,
            query=query,
            headers=headers,
            body=body,
            extra_query=extra_query,
        )
        return self._client.send(prepared)


class AsyncApiGroup:
    api_id: str
    base_path: str

    def __init__(self, client: AsyncProtheusClient) -> None:
        self._client = client

    async def _request(
        self,
        operation: str,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any],
        query: Mapping[str, Any],
        headers: Mapping[str, Any],
        body: Body | None,
        extra_query: Mapping[str, Any] | None,
    ) -> Any:
        prepared = prepare(
            operation,
            method,
            self.base_path,
            path,
            path_params=path_params,
            query=query,
            headers=headers,
            body=body,
            extra_query=extra_query,
        )
        return await self._client.send(prepared)
