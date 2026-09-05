"""DiscoveryEnvironments — generated from DiscoveryEnvironments_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class DiscoveryEnvironmentsV1(ApiGroup):
    """DiscoveryEnvironments (/api/framework/v1)."""

    api_id = "discovery_environments_v1"
    base_path = "/api/framework/v1"

    def list_discovery_environments(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os ambientes cadastrados

        GET /DiscoveryEnvironments; operationId=getEnvironments; Protheus >= 12.1.27

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_environments_v1.PagedDiscoveryEnvironments
        """
        return self._request(
            "discovery_environments_v1.list_discovery_environments",
            "GET",
            "/DiscoveryEnvironments",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_discovery_environments(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o ambiente passado na requisição

        POST /DiscoveryEnvironments; operationId=postDiscoveryEnvironment; Protheus >= 12.1.27

        Inclui a ambiente passada na requisição

        TOTVS note: Este verbo esta disponivel nessa versão

        Response model: protheus.models.discovery_environments_v1.PagedDiscoveryEnvironments
        Request model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return self._request(
            "discovery_environments_v1.create_discovery_environments",
            "POST",
            "/DiscoveryEnvironments",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_discovery_environments_by_discoveryenvironmentid(self, discoveryenvironmentid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o ambiente específico.

        GET /DiscoveryEnvironments/{discoveryenvironmentid}; operationId=getdiscoveryenvironmentid; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return self._request(
            "discovery_environments_v1.get_discovery_environments_by_discoveryenvironmentid",
            "GET",
            "/DiscoveryEnvironments/{discoveryenvironmentid}",
            path_params={"discoveryenvironmentid": discoveryenvironmentid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_discovery_environments_by_discoveryenvironmentid(self, discoveryenvironmentid: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o ambiente passado na requisição

        PUT /DiscoveryEnvironments/{discoveryenvironmentid}; operationId=postdiscoveryenvironmentid; Protheus >= 12.1.27

        TOTVS note: Este verbo  esta disponível nessa versão

        Response model: protheus.models.discovery_environments_v1.PagedDiscoveryEnvironments
        Request model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return self._request(
            "discovery_environments_v1.update_discovery_environments_by_discoveryenvironmentid",
            "PUT",
            "/DiscoveryEnvironments/{discoveryenvironmentid}",
            path_params={"discoveryenvironmentid": discoveryenvironmentid},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_discovery_environments_by_discoveryenvironmentid(self, discoveryenvironmentid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de ambiente

        DELETE /DiscoveryEnvironments/{discoveryenvironmentid}; operationId=Deletediscoveryenvironmentid; DEPRECATED

        TOTVS note: Este verbo esta disponivel

        Response model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return self._request(
            "discovery_environments_v1.delete_discovery_environments_by_discoveryenvironmentid",
            "DELETE",
            "/DiscoveryEnvironments/{discoveryenvironmentid}",
            path_params={"discoveryenvironmentid": discoveryenvironmentid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncDiscoveryEnvironmentsV1(AsyncApiGroup):
    """DiscoveryEnvironments (/api/framework/v1)."""

    api_id = "discovery_environments_v1"
    base_path = "/api/framework/v1"

    async def list_discovery_environments(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os ambientes cadastrados

        GET /DiscoveryEnvironments; operationId=getEnvironments; Protheus >= 12.1.27

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_environments_v1.PagedDiscoveryEnvironments
        """
        return await self._request(
            "discovery_environments_v1.list_discovery_environments",
            "GET",
            "/DiscoveryEnvironments",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_discovery_environments(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o ambiente passado na requisição

        POST /DiscoveryEnvironments; operationId=postDiscoveryEnvironment; Protheus >= 12.1.27

        Inclui a ambiente passada na requisição

        TOTVS note: Este verbo esta disponivel nessa versão

        Response model: protheus.models.discovery_environments_v1.PagedDiscoveryEnvironments
        Request model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return await self._request(
            "discovery_environments_v1.create_discovery_environments",
            "POST",
            "/DiscoveryEnvironments",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_discovery_environments_by_discoveryenvironmentid(self, discoveryenvironmentid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o ambiente específico.

        GET /DiscoveryEnvironments/{discoveryenvironmentid}; operationId=getdiscoveryenvironmentid; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return await self._request(
            "discovery_environments_v1.get_discovery_environments_by_discoveryenvironmentid",
            "GET",
            "/DiscoveryEnvironments/{discoveryenvironmentid}",
            path_params={"discoveryenvironmentid": discoveryenvironmentid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_discovery_environments_by_discoveryenvironmentid(self, discoveryenvironmentid: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o ambiente passado na requisição

        PUT /DiscoveryEnvironments/{discoveryenvironmentid}; operationId=postdiscoveryenvironmentid; Protheus >= 12.1.27

        TOTVS note: Este verbo  esta disponível nessa versão

        Response model: protheus.models.discovery_environments_v1.PagedDiscoveryEnvironments
        Request model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return await self._request(
            "discovery_environments_v1.update_discovery_environments_by_discoveryenvironmentid",
            "PUT",
            "/DiscoveryEnvironments/{discoveryenvironmentid}",
            path_params={"discoveryenvironmentid": discoveryenvironmentid},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_discovery_environments_by_discoveryenvironmentid(self, discoveryenvironmentid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de ambiente

        DELETE /DiscoveryEnvironments/{discoveryenvironmentid}; operationId=Deletediscoveryenvironmentid; DEPRECATED

        TOTVS note: Este verbo esta disponivel

        Response model: protheus.models.discovery_environments_v1.DiscoveryEnvironmentType
        """
        return await self._request(
            "discovery_environments_v1.delete_discovery_environments_by_discoveryenvironmentid",
            "DELETE",
            "/DiscoveryEnvironments/{discoveryenvironmentid}",
            path_params={"discoveryenvironmentid": discoveryenvironmentid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
