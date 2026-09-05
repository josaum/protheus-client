"""Grupo de Região — generated from RegionGroups_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RegionGroupsV1(ApiGroup):
    """Grupo de Região (/api/tms/v1)."""

    api_id = "region_groups_v1"
    base_path = "/api/tms/v1"

    def list_regiongroups(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Grupo de Região

        GET /regiongroups; operationId=getRegionGroups; Protheus >= 12.1.21

        Retorna lista completa do Grupo de Região

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.region_groups_v1.PagedRegionGroups
        """
        return self._request(
            "region_groups_v1.list_regiongroups",
            "GET",
            "/regiongroups",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_regiongroups(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Grupo de Região

        POST /regiongroups; operationId=postRegionGroups; Protheus >= 12.1.21

        Inclui um Grupo de Região conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.region_groups_v1.PagedRegionGroups
        Request model: protheus.models.region_groups_v1.RegionGroupsInfo
        """
        return self._request(
            "region_groups_v1.create_regiongroups",
            "POST",
            "/regiongroups",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_regiongroups_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Grupo de Região específica de acordo com a chave de pesquisa

        GET /regiongroups/{InternalId}; operationId=getCode; Protheus >= 12.1.21

        Retorna o Grupo de Região de acordo com o ID de pesquisa

        TOTVS note: o Code é composto por filial + Código do Grupo de Região

        Response model: protheus.models.region_groups_v1.RegionGroupsInfo
        """
        return self._request(
            "region_groups_v1.get_regiongroups_by_internal_id",
            "GET",
            "/regiongroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_regiongroups_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Grupo de Região

        PUT /regiongroups/{InternalId}; operationId=putCode; Protheus >= 12.1.21

        Atualiza o Grupo de Região conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.region_groups_v1.RegionGroupsInfo
        Request model: protheus.models.region_groups_v1.RegionGroupsInfo
        """
        return self._request(
            "region_groups_v1.update_regiongroups_by_internal_id",
            "PUT",
            "/regiongroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_regiongroups_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Grupo de Região

        DELETE /regiongroups/{InternalId}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Grupo de Região conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "region_groups_v1.delete_regiongroups_by_internal_id",
            "DELETE",
            "/regiongroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRegionGroupsV1(AsyncApiGroup):
    """Grupo de Região (/api/tms/v1)."""

    api_id = "region_groups_v1"
    base_path = "/api/tms/v1"

    async def list_regiongroups(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Grupo de Região

        GET /regiongroups; operationId=getRegionGroups; Protheus >= 12.1.21

        Retorna lista completa do Grupo de Região

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.region_groups_v1.PagedRegionGroups
        """
        return await self._request(
            "region_groups_v1.list_regiongroups",
            "GET",
            "/regiongroups",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_regiongroups(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Grupo de Região

        POST /regiongroups; operationId=postRegionGroups; Protheus >= 12.1.21

        Inclui um Grupo de Região conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.region_groups_v1.PagedRegionGroups
        Request model: protheus.models.region_groups_v1.RegionGroupsInfo
        """
        return await self._request(
            "region_groups_v1.create_regiongroups",
            "POST",
            "/regiongroups",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_regiongroups_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Grupo de Região específica de acordo com a chave de pesquisa

        GET /regiongroups/{InternalId}; operationId=getCode; Protheus >= 12.1.21

        Retorna o Grupo de Região de acordo com o ID de pesquisa

        TOTVS note: o Code é composto por filial + Código do Grupo de Região

        Response model: protheus.models.region_groups_v1.RegionGroupsInfo
        """
        return await self._request(
            "region_groups_v1.get_regiongroups_by_internal_id",
            "GET",
            "/regiongroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_regiongroups_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Grupo de Região

        PUT /regiongroups/{InternalId}; operationId=putCode; Protheus >= 12.1.21

        Atualiza o Grupo de Região conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.region_groups_v1.RegionGroupsInfo
        Request model: protheus.models.region_groups_v1.RegionGroupsInfo
        """
        return await self._request(
            "region_groups_v1.update_regiongroups_by_internal_id",
            "PUT",
            "/regiongroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_regiongroups_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Grupo de Região

        DELETE /regiongroups/{InternalId}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Grupo de Região conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "region_groups_v1.delete_regiongroups_by_internal_id",
            "DELETE",
            "/regiongroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
