"""Treadmills — generated from Treadmills_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class TreadmillsV1(ApiGroup):
    """Treadmills (/api/agr/v1)."""

    api_id = "treadmills_v1"
    base_path = "/api/agr/v1"

    def list_treadmills(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos as esteiras da base

        GET /Treadmills; operationId=getTreadmills; Protheus >= 12.1.23

        Response model: protheus.models.treadmills_v1.PagedTreadmills
        """
        return self._request(
            "treadmills_v1.list_treadmills",
            "GET",
            "/Treadmills",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_treadmills(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma esteira

        POST /Treadmills; operationId=postTreadmill; Protheus >= 12.1.23

        Inclui uma esteira passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.treadmills_v1.TreadmillsType
        Request model: protheus.models.treadmills_v1.TreadmillsType
        """
        return self._request(
            "treadmills_v1.create_treadmills",
            "POST",
            "/Treadmills",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma esteira

        GET /Treadmills/{InternalId}; operationId=getTreadmillID; Protheus >= 12.1.23

        Retorna a esteira correspondente ao código único informado

        Response model: protheus.models.treadmills_v1.TreadmillsType
        """
        return self._request(
            "treadmills_v1.get_treadmills_by_internal_id",
            "GET",
            "/Treadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_treadmills_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a esteira

        PUT /Treadmills/{InternalId}; operationId=putTreadmillID; Protheus >= 12.1.23

        Altera a esteira passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.treadmills_v1.TreadmillsType
        Request model: protheus.models.treadmills_v1.TreadmillsType
        """
        return self._request(
            "treadmills_v1.update_treadmills_by_internal_id",
            "PUT",
            "/Treadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção da esteira

        DELETE /Treadmills/{InternalId}; operationId=DeleteTreadmillID; Protheus >= 12.1.23

        Deleção da esteira informada

        Response model: protheus.models.treadmills_v1.TreadmillsType
        """
        return self._request(
            "treadmills_v1.delete_treadmills_by_internal_id",
            "DELETE",
            "/Treadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncTreadmillsV1(AsyncApiGroup):
    """Treadmills (/api/agr/v1)."""

    api_id = "treadmills_v1"
    base_path = "/api/agr/v1"

    async def list_treadmills(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos as esteiras da base

        GET /Treadmills; operationId=getTreadmills; Protheus >= 12.1.23

        Response model: protheus.models.treadmills_v1.PagedTreadmills
        """
        return await self._request(
            "treadmills_v1.list_treadmills",
            "GET",
            "/Treadmills",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_treadmills(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma esteira

        POST /Treadmills; operationId=postTreadmill; Protheus >= 12.1.23

        Inclui uma esteira passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.treadmills_v1.TreadmillsType
        Request model: protheus.models.treadmills_v1.TreadmillsType
        """
        return await self._request(
            "treadmills_v1.create_treadmills",
            "POST",
            "/Treadmills",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma esteira

        GET /Treadmills/{InternalId}; operationId=getTreadmillID; Protheus >= 12.1.23

        Retorna a esteira correspondente ao código único informado

        Response model: protheus.models.treadmills_v1.TreadmillsType
        """
        return await self._request(
            "treadmills_v1.get_treadmills_by_internal_id",
            "GET",
            "/Treadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_treadmills_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a esteira

        PUT /Treadmills/{InternalId}; operationId=putTreadmillID; Protheus >= 12.1.23

        Altera a esteira passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.treadmills_v1.TreadmillsType
        Request model: protheus.models.treadmills_v1.TreadmillsType
        """
        return await self._request(
            "treadmills_v1.update_treadmills_by_internal_id",
            "PUT",
            "/Treadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção da esteira

        DELETE /Treadmills/{InternalId}; operationId=DeleteTreadmillID; Protheus >= 12.1.23

        Deleção da esteira informada

        Response model: protheus.models.treadmills_v1.TreadmillsType
        """
        return await self._request(
            "treadmills_v1.delete_treadmills_by_internal_id",
            "DELETE",
            "/Treadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
