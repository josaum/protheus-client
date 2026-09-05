"""Token — generated from Token_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class TokenV1(ApiGroup):
    """Token (/api/oauth2/v1)."""

    api_id = "token_v1"
    base_path = "/api/oauth2/v1"

    def create_token(self, *, grant_type: str | None = None, username: str | None = None, password: str | None = None, refresh_token: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna token de acesso

        POST /token; operationId=getResources; Protheus >= 12.1.23

        Aplicativos realizam a requisição ao endpoint inserindo os parâmetros descritos a seguir

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.token_v1.BusinessContentType
        """
        return self._request(
            "token_v1.create_token",
            "POST",
            "/token",
            path_params={},
            query={"grant_type": grant_type, "username": username, "password": password, "refresh_token": refresh_token},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncTokenV1(AsyncApiGroup):
    """Token (/api/oauth2/v1)."""

    api_id = "token_v1"
    base_path = "/api/oauth2/v1"

    async def create_token(self, *, grant_type: str | None = None, username: str | None = None, password: str | None = None, refresh_token: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna token de acesso

        POST /token; operationId=getResources; Protheus >= 12.1.23

        Aplicativos realizam a requisição ao endpoint inserindo os parâmetros descritos a seguir

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.token_v1.BusinessContentType
        """
        return await self._request(
            "token_v1.create_token",
            "POST",
            "/token",
            path_params={},
            query={"grant_type": grant_type, "username": username, "password": password, "refresh_token": refresh_token},
            headers={},
            body=None,
            extra_query=extra_query,
        )
