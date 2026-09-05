"""CottonBales — generated from CottonBales_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonBalesV1(ApiGroup):
    """CottonBales (/api/agr/v1)."""

    api_id = "cotton_bales_v1"
    base_path = "/api/agr/v1"

    def list_cotton_bales(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os fardões da base

        GET /CottonBales; operationId=getCottonBales; Protheus >= 12.1.23

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return self._request(
            "cotton_bales_v1.list_cotton_bales",
            "GET",
            "/CottonBales",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cotton_bales(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um fardão

        POST /CottonBales; operationId=postCottonBale; Protheus >= 12.1.23

        Inclui um fardão passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        Request model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return self._request(
            "cotton_bales_v1.create_cotton_bales",
            "POST",
            "/CottonBales",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_cotton_bales_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um fardão

        GET /CottonBales/{InternalId}; operationId=getCottonBaleID; Protheus >= 12.1.23

        Retorna o fardão correspondente ao código único informado

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return self._request(
            "cotton_bales_v1.get_cotton_bales_by_internal_id",
            "GET",
            "/CottonBales/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_bales_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o fardão

        PUT /CottonBales/{InternalId}; operationId=putCottonBaleID; Protheus >= 12.1.23

        Altera a Filial passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        Request model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return self._request(
            "cotton_bales_v1.update_cotton_bales_by_internal_id",
            "PUT",
            "/CottonBales/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_bales_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção de fardão

        DELETE /CottonBales/{InternalId}; operationId=DeleteCottonBaleID; Protheus >= 12.1.23

        Deleção do fardão informado

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return self._request(
            "cotton_bales_v1.delete_cotton_bales_by_internal_id",
            "DELETE",
            "/CottonBales/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonBalesV1(AsyncApiGroup):
    """CottonBales (/api/agr/v1)."""

    api_id = "cotton_bales_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_bales(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os fardões da base

        GET /CottonBales; operationId=getCottonBales; Protheus >= 12.1.23

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return await self._request(
            "cotton_bales_v1.list_cotton_bales",
            "GET",
            "/CottonBales",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cotton_bales(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um fardão

        POST /CottonBales; operationId=postCottonBale; Protheus >= 12.1.23

        Inclui um fardão passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        Request model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return await self._request(
            "cotton_bales_v1.create_cotton_bales",
            "POST",
            "/CottonBales",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_cotton_bales_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um fardão

        GET /CottonBales/{InternalId}; operationId=getCottonBaleID; Protheus >= 12.1.23

        Retorna o fardão correspondente ao código único informado

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return await self._request(
            "cotton_bales_v1.get_cotton_bales_by_internal_id",
            "GET",
            "/CottonBales/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_bales_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o fardão

        PUT /CottonBales/{InternalId}; operationId=putCottonBaleID; Protheus >= 12.1.23

        Altera a Filial passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        Request model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return await self._request(
            "cotton_bales_v1.update_cotton_bales_by_internal_id",
            "PUT",
            "/CottonBales/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_bales_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção de fardão

        DELETE /CottonBales/{InternalId}; operationId=DeleteCottonBaleID; Protheus >= 12.1.23

        Deleção do fardão informado

        Response model: protheus.models.cotton_bales_v1.CottonBalesType
        """
        return await self._request(
            "cotton_bales_v1.delete_cotton_bales_by_internal_id",
            "DELETE",
            "/CottonBales/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
