"""Sync and async clients.

``base_url`` is the Protheus REST root — everything before ``/api/...``. On a
standard install that includes the REST path prefix, e.g.
``http://erp.example.com:8080/rest``; the TTALK specs write it as ``{{host}}``.
"""

from __future__ import annotations

from collections.abc import Mapping
from types import TracebackType
from typing import Any

import httpx

from protheus._base import PreparedRequest
from protheus.apis import AsyncApis, SyncApis
from protheus.auth import OAuth2PasswordAuth
from protheus.errors import ProtheusError, ProtheusTransportError

DEFAULT_TIMEOUT = 30.0
_JSON_HEADERS = {"Accept": "application/json"}


def _bind_auth(auth: httpx.Auth | None, base_url: str) -> httpx.Auth | None:
    if isinstance(auth, OAuth2PasswordAuth) and not auth.token_url:
        auth.token_url = base_url + OAuth2PasswordAuth.TOKEN_PATH
    return auth


def _decode(response: httpx.Response) -> Any:
    if response.status_code == 204 or not response.content:
        return None
    content_type = response.headers.get("content-type", "")
    if "json" in content_type:
        return response.json()
    try:
        return response.json()
    except ValueError:
        return response.text


class _ClientBase:
    def __init__(
        self,
        base_url: str,
        *,
        auth: httpx.Auth | None = None,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        headers: Mapping[str, str] | None = None,
        accept_language: str | None = None,
        verify: bool | str = True,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.auth = _bind_auth(auth, self.base_url)
        default_headers = dict(_JSON_HEADERS)
        if accept_language:
            default_headers["Accept-Language"] = accept_language
        if headers:
            default_headers.update(headers)
        self._default_headers = default_headers
        self._timeout = timeout
        self._verify = verify

    def _kwargs(self, prepared: PreparedRequest) -> dict[str, Any]:
        headers = dict(prepared.headers)
        kwargs: dict[str, Any] = {"params": prepared.params, "headers": headers}
        if prepared.json is not None:
            kwargs["json"] = prepared.json
        return kwargs

    @staticmethod
    def _check(response: httpx.Response, operation: str) -> httpx.Response:
        if response.status_code >= 400:
            raise ProtheusError.from_response(response, operation)
        return response

    @classmethod
    def _finish(cls, response: httpx.Response, operation: str) -> Any:
        return _decode(cls._check(response, operation))


class ProtheusClient(_ClientBase, SyncApis):
    """Synchronous client. Generated API groups hang off it, e.g.
    ``client.customer_vendor_v1.list_customer_vendor_by_entity_type("customer")``."""

    def __init__(
        self,
        base_url: str,
        *,
        auth: httpx.Auth | None = None,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        headers: Mapping[str, str] | None = None,
        accept_language: str | None = None,
        verify: bool | str = True,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        super().__init__(
            base_url, auth=auth, timeout=timeout, headers=headers, accept_language=accept_language, verify=verify
        )
        self._http = httpx.Client(
            base_url=self.base_url,
            auth=self.auth,
            timeout=timeout,
            headers=self._default_headers,
            verify=verify,
            transport=transport,
        )

    def _send(self, prepared: PreparedRequest) -> httpx.Response:
        try:
            return self._http.request(prepared.method, prepared.path, **self._kwargs(prepared))
        except httpx.RequestError as exc:
            raise ProtheusTransportError(exc, prepared.operation) from exc

    def send(self, prepared: PreparedRequest) -> Any:
        return self._finish(self._send(prepared), prepared.operation)

    def send_bytes(self, prepared: PreparedRequest) -> bytes:
        """Like :meth:`send` but returns the undecoded body (for the Arrow decoder)."""
        return self._check(self._send(prepared), prepared.operation).content

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> ProtheusClient:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()


class AsyncProtheusClient(_ClientBase, AsyncApis):
    """Asynchronous client with the same surface as :class:`ProtheusClient`."""

    def __init__(
        self,
        base_url: str,
        *,
        auth: httpx.Auth | None = None,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        headers: Mapping[str, str] | None = None,
        accept_language: str | None = None,
        verify: bool | str = True,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        super().__init__(
            base_url, auth=auth, timeout=timeout, headers=headers, accept_language=accept_language, verify=verify
        )
        self._http = httpx.AsyncClient(
            base_url=self.base_url,
            auth=self.auth,
            timeout=timeout,
            headers=self._default_headers,
            verify=verify,
            transport=transport,
        )

    async def _send(self, prepared: PreparedRequest) -> httpx.Response:
        try:
            return await self._http.request(prepared.method, prepared.path, **self._kwargs(prepared))
        except httpx.RequestError as exc:
            raise ProtheusTransportError(exc, prepared.operation) from exc

    async def send(self, prepared: PreparedRequest) -> Any:
        return self._finish(await self._send(prepared), prepared.operation)

    async def send_bytes(self, prepared: PreparedRequest) -> bytes:
        """Like :meth:`send` but returns the undecoded body (for the Arrow decoder)."""
        return self._check(await self._send(prepared), prepared.operation).content

    async def aclose(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> AsyncProtheusClient:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.aclose()
