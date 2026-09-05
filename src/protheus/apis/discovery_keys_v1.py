"""Chaves de configuracao de stages — generated from DiscoveryKeys_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class DiscoveryKeysV1(ApiGroup):
    """Chaves de configuracao de stages (/api/framework/v1)."""

    api_id = "discovery_keys_v1"
    base_path = "/api/framework/v1"

    def list_discovery_keys(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos as chaves

        GET /DiscoveryKeys; operationId=getDiscoveryKeys; Protheus >= 12.1.27

        Retorna todos as stageKeys

        TOTVS note: Este verbo esta disponivel com todos as chaves

        Response model: protheus.models.discovery_keys_v1.PagedDiscoveryKeys
        """
        return self._request(
            "discovery_keys_v1.list_discovery_keys",
            "GET",
            "/DiscoveryKeys",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_discovery_keys_by_name(self, name: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma chave específica.

        GET /DiscoveryKeys/{name}; operationId=getkeyname; Protheus >= 12.1.27

        TOTVS note: Este verbo esta disponivel com todos as chaves

        Response model: protheus.models.discovery_keys_v1.DiscoveryKeys
        """
        return self._request(
            "discovery_keys_v1.get_discovery_keys_by_name",
            "GET",
            "/DiscoveryKeys/{name}",
            path_params={"name": name},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncDiscoveryKeysV1(AsyncApiGroup):
    """Chaves de configuracao de stages (/api/framework/v1)."""

    api_id = "discovery_keys_v1"
    base_path = "/api/framework/v1"

    async def list_discovery_keys(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos as chaves

        GET /DiscoveryKeys; operationId=getDiscoveryKeys; Protheus >= 12.1.27

        Retorna todos as stageKeys

        TOTVS note: Este verbo esta disponivel com todos as chaves

        Response model: protheus.models.discovery_keys_v1.PagedDiscoveryKeys
        """
        return await self._request(
            "discovery_keys_v1.list_discovery_keys",
            "GET",
            "/DiscoveryKeys",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_discovery_keys_by_name(self, name: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma chave específica.

        GET /DiscoveryKeys/{name}; operationId=getkeyname; Protheus >= 12.1.27

        TOTVS note: Este verbo esta disponivel com todos as chaves

        Response model: protheus.models.discovery_keys_v1.DiscoveryKeys
        """
        return await self._request(
            "discovery_keys_v1.get_discovery_keys_by_name",
            "GET",
            "/DiscoveryKeys/{name}",
            path_params={"name": name},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
