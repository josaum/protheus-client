"""DiscoveryStages — generated from DiscoveryStages_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class DiscoveryStagesV1(ApiGroup):
    """DiscoveryStages (/api/framework/v1)."""

    api_id = "discovery_stages_v1"
    base_path = "/api/framework/v1"

    def list_discovery_stages(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os stages cadastrados

        GET /DiscoveryStages; operationId=getStages; Protheus >= 12.1.27

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_stages_v1.PagedDiscoveryStages
        """
        return self._request(
            "discovery_stages_v1.list_discovery_stages",
            "GET",
            "/DiscoveryStages",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_discovery_stages(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o stage passado na requisição

        POST /DiscoveryStages; operationId=postDiscoveryStage; Protheus >= 12.1.27

        Inclui o stage passada na requisição

        TOTVS note: Este verbo esta disponivel nessa versão

        Response model: protheus.models.discovery_stages_v1.PagedDiscoveryStages
        Request model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return self._request(
            "discovery_stages_v1.create_discovery_stages",
            "POST",
            "/DiscoveryStages",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_discovery_stages_by_discoverystageid(self, discoverystageid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Stage específico.

        GET /DiscoveryStages/{discoverystageid}; operationId=getStageID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return self._request(
            "discovery_stages_v1.get_discovery_stages_by_discoverystageid",
            "GET",
            "/DiscoveryStages/{discoverystageid}",
            path_params={"discoverystageid": discoverystageid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_discovery_stages_by_discoverystageid(self, discoverystageid: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o ambiente passado na requisição

        PUT /DiscoveryStages/{discoverystageid}; operationId=postdiscoverystageid; Protheus >= 12.1.27

        TOTVS note: Este verbo  esta disponível nessa versão

        Response model: protheus.models.discovery_stages_v1.PagedDiscoveryStages
        Request model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return self._request(
            "discovery_stages_v1.update_discovery_stages_by_discoverystageid",
            "PUT",
            "/DiscoveryStages/{discoverystageid}",
            path_params={"discoverystageid": discoverystageid},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_discovery_stages_by_discoverystageid(self, discoverystageid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de ambiente

        DELETE /DiscoveryStages/{discoverystageid}; operationId=Deletediscoverystageid

        TOTVS note: Este verbo esta disponivel

        Response model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return self._request(
            "discovery_stages_v1.delete_discovery_stages_by_discoverystageid",
            "DELETE",
            "/DiscoveryStages/{discoverystageid}",
            path_params={"discoverystageid": discoverystageid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncDiscoveryStagesV1(AsyncApiGroup):
    """DiscoveryStages (/api/framework/v1)."""

    api_id = "discovery_stages_v1"
    base_path = "/api/framework/v1"

    async def list_discovery_stages(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os stages cadastrados

        GET /DiscoveryStages; operationId=getStages; Protheus >= 12.1.27

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_stages_v1.PagedDiscoveryStages
        """
        return await self._request(
            "discovery_stages_v1.list_discovery_stages",
            "GET",
            "/DiscoveryStages",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_discovery_stages(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o stage passado na requisição

        POST /DiscoveryStages; operationId=postDiscoveryStage; Protheus >= 12.1.27

        Inclui o stage passada na requisição

        TOTVS note: Este verbo esta disponivel nessa versão

        Response model: protheus.models.discovery_stages_v1.PagedDiscoveryStages
        Request model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return await self._request(
            "discovery_stages_v1.create_discovery_stages",
            "POST",
            "/DiscoveryStages",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_discovery_stages_by_discoverystageid(self, discoverystageid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Stage específico.

        GET /DiscoveryStages/{discoverystageid}; operationId=getStageID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return await self._request(
            "discovery_stages_v1.get_discovery_stages_by_discoverystageid",
            "GET",
            "/DiscoveryStages/{discoverystageid}",
            path_params={"discoverystageid": discoverystageid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_discovery_stages_by_discoverystageid(self, discoverystageid: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o ambiente passado na requisição

        PUT /DiscoveryStages/{discoverystageid}; operationId=postdiscoverystageid; Protheus >= 12.1.27

        TOTVS note: Este verbo  esta disponível nessa versão

        Response model: protheus.models.discovery_stages_v1.PagedDiscoveryStages
        Request model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return await self._request(
            "discovery_stages_v1.update_discovery_stages_by_discoverystageid",
            "PUT",
            "/DiscoveryStages/{discoverystageid}",
            path_params={"discoverystageid": discoverystageid},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_discovery_stages_by_discoverystageid(self, discoverystageid: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de ambiente

        DELETE /DiscoveryStages/{discoverystageid}; operationId=Deletediscoverystageid

        TOTVS note: Este verbo esta disponivel

        Response model: protheus.models.discovery_stages_v1.DiscoveryStageType
        """
        return await self._request(
            "discovery_stages_v1.delete_discovery_stages_by_discoverystageid",
            "DELETE",
            "/DiscoveryStages/{discoverystageid}",
            path_params={"discoverystageid": discoverystageid},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
