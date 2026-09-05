"""Centro de Custo — generated from CostCenter_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CostCenterV1(ApiGroup):
    """Centro de Custo (/api/ctb/v1)."""

    api_id = "cost_center_v1"
    base_path = "/api/ctb/v1"

    def list_costcenters(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Centro de Custo

        GET /costcenters; operationId=getCostCenters; Protheus >= 12.1.21

        Retorna lista completa dos Centro de Custos

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.cost_center_v1.PagedCostCenters
        """
        return self._request(
            "cost_center_v1.list_costcenters",
            "GET",
            "/costcenters",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_costcenters(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Centro de Custo

        POST /costcenters; operationId=postCostCenters; Protheus >= 12.1.21

        Inclui um Centro de Custo conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        Request model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return self._request(
            "cost_center_v1.create_costcenters",
            "POST",
            "/costcenters",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_costcenters_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um centro de custo específica de acordo com a chave de pesquisa

        GET /costcenters/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna um centro de custo de acordo com o ID de pesquisa

        TOTVS note: o Code é composto por filial + Código do Centro de Custo

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return self._request(
            "cost_center_v1.get_costcenters_by_internal_id",
            "GET",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_costcenters_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Centro de Custo

        PUT /costcenters/{InternalId}; operationId=putInternalId; Protheus >=  12.1.21

        Atualiza centro de custo conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        Request model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return self._request(
            "cost_center_v1.update_costcenters_by_internal_id",
            "PUT",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def patch_costcenters_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Centro de Custo

        PATCH /costcenters/{InternalId}; operationId=patchtInternalId; Protheus >=  12.1.21

        Atualiza centro de custo somente com os dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        Request model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return self._request(
            "cost_center_v1.patch_costcenters_by_internal_id",
            "PATCH",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_costcenters_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Centro de Custo

        DELETE /costcenters/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Centro de Custo conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "cost_center_v1.delete_costcenters_by_internal_id",
            "DELETE",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCostCenterV1(AsyncApiGroup):
    """Centro de Custo (/api/ctb/v1)."""

    api_id = "cost_center_v1"
    base_path = "/api/ctb/v1"

    async def list_costcenters(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Centro de Custo

        GET /costcenters; operationId=getCostCenters; Protheus >= 12.1.21

        Retorna lista completa dos Centro de Custos

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.cost_center_v1.PagedCostCenters
        """
        return await self._request(
            "cost_center_v1.list_costcenters",
            "GET",
            "/costcenters",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_costcenters(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Centro de Custo

        POST /costcenters; operationId=postCostCenters; Protheus >= 12.1.21

        Inclui um Centro de Custo conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        Request model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return await self._request(
            "cost_center_v1.create_costcenters",
            "POST",
            "/costcenters",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_costcenters_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um centro de custo específica de acordo com a chave de pesquisa

        GET /costcenters/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna um centro de custo de acordo com o ID de pesquisa

        TOTVS note: o Code é composto por filial + Código do Centro de Custo

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return await self._request(
            "cost_center_v1.get_costcenters_by_internal_id",
            "GET",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_costcenters_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Centro de Custo

        PUT /costcenters/{InternalId}; operationId=putInternalId; Protheus >=  12.1.21

        Atualiza centro de custo conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        Request model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return await self._request(
            "cost_center_v1.update_costcenters_by_internal_id",
            "PUT",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def patch_costcenters_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Centro de Custo

        PATCH /costcenters/{InternalId}; operationId=patchtInternalId; Protheus >=  12.1.21

        Atualiza centro de custo somente com os dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.cost_center_v1.CostCentersInfo
        Request model: protheus.models.cost_center_v1.CostCentersInfo
        """
        return await self._request(
            "cost_center_v1.patch_costcenters_by_internal_id",
            "PATCH",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_costcenters_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Centro de Custo

        DELETE /costcenters/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Centro de Custo conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "cost_center_v1.delete_costcenters_by_internal_id",
            "DELETE",
            "/costcenters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
