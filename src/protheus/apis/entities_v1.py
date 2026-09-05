"""Entities — generated from Entities_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class EntitiesV1(ApiGroup):
    """Entities (/api/agr/v1)."""

    api_id = "entities_v1"
    base_path = "/api/agr/v1"

    def list_entities(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as entidades cadastradas.

        GET /Entities; operationId=getEntitiesID; Protheus >= 12.1.23

        Response model: protheus.models.entities_v1.PagedEntities
        """
        return self._request(
            "entities_v1.list_entities",
            "GET",
            "/Entities",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_entities(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma entidade.

        POST /Entities; operationId=postEntityID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.entities_v1.EntitiesType
        """
        return self._request(
            "entities_v1.create_entities",
            "POST",
            "/Entities",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_entities_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma entidade.

        GET /Entities/{InternalId}; operationId=getEntityID; Protheus >= 12.1.23

        Retorna a entidade requerida.

        Response model: protheus.models.entities_v1.EntitiesType
        """
        return self._request(
            "entities_v1.get_entities_by_internal_id",
            "GET",
            "/Entities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_entities_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a entidade.

        PUT /Entities/{InternalId}; operationId=putEntityID; Protheus >= 12.1.23

        Altera a entidade informada.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.entities_v1.EntitiesType
        Request model: protheus.models.entities_v1.EntitiesType
        """
        return self._request(
            "entities_v1.update_entities_by_internal_id",
            "PUT",
            "/Entities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_entities_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta a entidade.

        DELETE /Entities/{InternalId}; operationId=DeleteEntityID; Protheus >= 12.1.23

        Deleção da entidade informada.

        Response model: protheus.models.entities_v1.EntitiesType
        """
        return self._request(
            "entities_v1.delete_entities_by_internal_id",
            "DELETE",
            "/Entities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncEntitiesV1(AsyncApiGroup):
    """Entities (/api/agr/v1)."""

    api_id = "entities_v1"
    base_path = "/api/agr/v1"

    async def list_entities(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as entidades cadastradas.

        GET /Entities; operationId=getEntitiesID; Protheus >= 12.1.23

        Response model: protheus.models.entities_v1.PagedEntities
        """
        return await self._request(
            "entities_v1.list_entities",
            "GET",
            "/Entities",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_entities(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma entidade.

        POST /Entities; operationId=postEntityID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.entities_v1.EntitiesType
        """
        return await self._request(
            "entities_v1.create_entities",
            "POST",
            "/Entities",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_entities_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma entidade.

        GET /Entities/{InternalId}; operationId=getEntityID; Protheus >= 12.1.23

        Retorna a entidade requerida.

        Response model: protheus.models.entities_v1.EntitiesType
        """
        return await self._request(
            "entities_v1.get_entities_by_internal_id",
            "GET",
            "/Entities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_entities_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a entidade.

        PUT /Entities/{InternalId}; operationId=putEntityID; Protheus >= 12.1.23

        Altera a entidade informada.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.entities_v1.EntitiesType
        Request model: protheus.models.entities_v1.EntitiesType
        """
        return await self._request(
            "entities_v1.update_entities_by_internal_id",
            "PUT",
            "/Entities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_entities_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta a entidade.

        DELETE /Entities/{InternalId}; operationId=DeleteEntityID; Protheus >= 12.1.23

        Deleção da entidade informada.

        Response model: protheus.models.entities_v1.EntitiesType
        """
        return await self._request(
            "entities_v1.delete_entities_by_internal_id",
            "DELETE",
            "/Entities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
