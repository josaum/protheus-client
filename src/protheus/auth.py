"""Authentication schemes accepted by Protheus REST servers.

* :class:`BasicAuth` — HTTP Basic (the classic Protheus REST setup).
* :class:`BearerAuth` — a token obtained elsewhere, sent as ``Bearer``.
* :class:`OAuth2PasswordAuth` — the built-in ``/api/oauth2/v1/token`` flow
  (Protheus >= 12.1.23): password grant, cached token, refresh grant, and a
  single password re-grant when a request comes back 401.

Note: the TTALK spec (``Token_v1_000``) lists ``grant_type`` as
``PASSWORD``/``REFRESH_TOKEN``; TOTVS' own Protheus documentation and servers
use lowercase ``password``/``refresh_token``, which is what is sent here.
"""

from __future__ import annotations

import time
from collections.abc import Generator
from typing import Any

import httpx

BasicAuth = httpx.BasicAuth


class BearerAuth(httpx.Auth):
    def __init__(self, token: str) -> None:
        self.token = token

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"Bearer {self.token}"
        yield request


class OAuth2PasswordAuth(httpx.Auth):
    """OAuth2 password grant against Protheus' token endpoint.

    ``token_url`` is normally filled in by the client from its ``base_url``
    (``<base_url>/api/oauth2/v1/token``); pass it explicitly to override.
    """

    requires_response_body = True
    TOKEN_PATH = "/api/oauth2/v1/token"
    _SKEW_SECONDS = 30

    def __init__(
        self,
        username: str,
        password: str,
        *,
        token_url: str | None = None,
        default_expires_in: int = 3600,
    ) -> None:
        self.username = username
        self.password = password
        self.token_url = token_url
        self.default_expires_in = default_expires_in
        self.access_token: str | None = None
        self.refresh_token: str | None = None
        self.expires_at: float = 0.0

    # -- state -------------------------------------------------------------
    @property
    def token_valid(self) -> bool:
        return bool(self.access_token) and time.monotonic() < self.expires_at - self._SKEW_SECONDS

    def _store(self, response: httpx.Response) -> None:
        if response.status_code >= 400:
            from protheus.errors import ProtheusError

            raise ProtheusError.from_response(response, operation="oauth2.token")
        data: dict[str, Any] = response.json()
        self.access_token = data["access_token"]
        self.refresh_token = data.get("refresh_token") or self.refresh_token
        expires_in = data.get("expires_in")
        self.expires_at = time.monotonic() + (int(expires_in) if expires_in else self.default_expires_in)

    def _token_request(self, *, use_refresh: bool) -> httpx.Request:
        if not self.token_url:
            raise RuntimeError("OAuth2PasswordAuth.token_url is not set; construct it via ProtheusClient")
        if use_refresh and self.refresh_token:
            params = {"grant_type": "refresh_token", "refresh_token": self.refresh_token}
        else:
            params = {"grant_type": "password", "username": self.username, "password": self.password}
        # Protheus reads the grant from the query string (see module docstring).
        return httpx.Request("POST", self.token_url, params=params)

    # -- flow --------------------------------------------------------------
    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        if not self.token_valid:
            response = yield self._token_request(use_refresh=True)
            if response.status_code >= 400 and self.refresh_token:
                self.refresh_token = None
                response = yield self._token_request(use_refresh=False)
            self._store(response)
        request.headers["Authorization"] = f"Bearer {self.access_token}"
        response = yield request
        if response.status_code == 401:
            self.access_token = None
            self.refresh_token = None
            token_response = yield self._token_request(use_refresh=False)
            self._store(token_response)
            request.headers["Authorization"] = f"Bearer {self.access_token}"
            yield request
