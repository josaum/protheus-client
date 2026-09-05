"""Recursos — generated from Resource_v1_001.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ResourceV1(ApiGroup):
    """Recursos (/api/sfc/v1)."""

    api_id = "resource_v1"
    base_path = "/api/sfc/v1"

    def list_resources(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Recursos

        GET /resources; operationId=getResources; Protheus >= 12.1.23

        Retorna lista de Recursos

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.PagedResources
        """
        return self._request(
            "resource_v1.list_resources",
            "GET",
            "/resources",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_resources(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Recurso

        POST /resources; operationId=postResource; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        Request model: protheus.models.resource_v1.Resource
        """
        return self._request(
            "resource_v1.create_resources",
            "POST",
            "/resources",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_resources_by_resource_id(self, resource_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Recurso

        GET /resources/{ResourceId}; operationId=getResourceCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        """
        return self._request(
            "resource_v1.get_resources_by_resource_id",
            "GET",
            "/resources/{ResourceId}",
            path_params={"ResourceId": resource_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_resources_by_resource_id(self, resource_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um Recurso

        PUT /resources/{ResourceId}; operationId=putResourceCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        Request model: protheus.models.resource_v1.Resource
        """
        return self._request(
            "resource_v1.update_resources_by_resource_id",
            "PUT",
            "/resources/{ResourceId}",
            path_params={"ResourceId": resource_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_resources_by_resource_id(self, resource_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um Recurso

        DELETE /resources/{ResourceId}; operationId=deleteResourceCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        """
        return self._request(
            "resource_v1.delete_resources_by_resource_id",
            "DELETE",
            "/resources/{ResourceId}",
            path_params={"ResourceId": resource_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncResourceV1(AsyncApiGroup):
    """Recursos (/api/sfc/v1)."""

    api_id = "resource_v1"
    base_path = "/api/sfc/v1"

    async def list_resources(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Recursos

        GET /resources; operationId=getResources; Protheus >= 12.1.23

        Retorna lista de Recursos

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.PagedResources
        """
        return await self._request(
            "resource_v1.list_resources",
            "GET",
            "/resources",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_resources(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Recurso

        POST /resources; operationId=postResource; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        Request model: protheus.models.resource_v1.Resource
        """
        return await self._request(
            "resource_v1.create_resources",
            "POST",
            "/resources",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_resources_by_resource_id(self, resource_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Recurso

        GET /resources/{ResourceId}; operationId=getResourceCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        """
        return await self._request(
            "resource_v1.get_resources_by_resource_id",
            "GET",
            "/resources/{ResourceId}",
            path_params={"ResourceId": resource_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_resources_by_resource_id(self, resource_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um Recurso

        PUT /resources/{ResourceId}; operationId=putResourceCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        Request model: protheus.models.resource_v1.Resource
        """
        return await self._request(
            "resource_v1.update_resources_by_resource_id",
            "PUT",
            "/resources/{ResourceId}",
            path_params={"ResourceId": resource_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_resources_by_resource_id(self, resource_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um Recurso

        DELETE /resources/{ResourceId}; operationId=deleteResourceCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.resource_v1.Resource
        """
        return await self._request(
            "resource_v1.delete_resources_by_resource_id",
            "DELETE",
            "/resources/{ResourceId}",
            path_params={"ResourceId": resource_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
