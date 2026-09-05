"""CottonBalesOnTreadmills — generated from CottonBalesOnTreadmills_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonBalesOnTreadmillsV1(ApiGroup):
    """CottonBalesOnTreadmills (/api/agr/v1)."""

    api_id = "cotton_bales_on_treadmills_v1"
    base_path = "/api/agr/v1"

    def list_cotton_bales_on_treadmills(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas os vinculos esteira x fardão da base

        GET /CottonBalesOnTreadmills; operationId=getCottonBalesOnTreadmills; Protheus >= 12.1.23

        Retorna todos os vinculos de esteira x fardão da base

        Response model: protheus.models.cotton_bales_on_treadmills_v1.PagedCottonBalesOnTreadmills
        """
        return self._request(
            "cotton_bales_on_treadmills_v1.list_cotton_bales_on_treadmills",
            "GET",
            "/CottonBalesOnTreadmills",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_cotton_bales_on_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os fardões vinculados à esteira correspondente.

        GET /CottonBalesOnTreadmills/{InternalId}; operationId=getCottonBalesOnTreadmillID; Protheus >= 12.1.23

        Retorna os fardões vinculados à esteira correspondente ao parâmetro informado

        Response model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        """
        return self._request(
            "cotton_bales_on_treadmills_v1.get_cotton_bales_on_treadmills_by_internal_id",
            "GET",
            "/CottonBalesOnTreadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_bales_on_treadmills_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Vincula um fardão a uma esteira.

        PUT /CottonBalesOnTreadmills/{InternalId}; operationId=putCottonBalesOnTreadmillID; Protheus >= 12.1.23

        Vincula um fardão a esteira passada na requisição

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        Request model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        """
        return self._request(
            "cotton_bales_on_treadmills_v1.update_cotton_bales_on_treadmills_by_internal_id",
            "PUT",
            "/CottonBalesOnTreadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_bales_on_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção do vinculo do fardão da esteira a qual está vinculado.

        DELETE /CottonBalesOnTreadmills/{InternalId}; operationId=DeleteCottonBalesOnTreadmillID; Protheus >= 12.1.23

        Deleção do fardão informado da fila a qual pertence.

        Response model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        """
        return self._request(
            "cotton_bales_on_treadmills_v1.delete_cotton_bales_on_treadmills_by_internal_id",
            "DELETE",
            "/CottonBalesOnTreadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonBalesOnTreadmillsV1(AsyncApiGroup):
    """CottonBalesOnTreadmills (/api/agr/v1)."""

    api_id = "cotton_bales_on_treadmills_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_bales_on_treadmills(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas os vinculos esteira x fardão da base

        GET /CottonBalesOnTreadmills; operationId=getCottonBalesOnTreadmills; Protheus >= 12.1.23

        Retorna todos os vinculos de esteira x fardão da base

        Response model: protheus.models.cotton_bales_on_treadmills_v1.PagedCottonBalesOnTreadmills
        """
        return await self._request(
            "cotton_bales_on_treadmills_v1.list_cotton_bales_on_treadmills",
            "GET",
            "/CottonBalesOnTreadmills",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_cotton_bales_on_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os fardões vinculados à esteira correspondente.

        GET /CottonBalesOnTreadmills/{InternalId}; operationId=getCottonBalesOnTreadmillID; Protheus >= 12.1.23

        Retorna os fardões vinculados à esteira correspondente ao parâmetro informado

        Response model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        """
        return await self._request(
            "cotton_bales_on_treadmills_v1.get_cotton_bales_on_treadmills_by_internal_id",
            "GET",
            "/CottonBalesOnTreadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_bales_on_treadmills_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Vincula um fardão a uma esteira.

        PUT /CottonBalesOnTreadmills/{InternalId}; operationId=putCottonBalesOnTreadmillID; Protheus >= 12.1.23

        Vincula um fardão a esteira passada na requisição

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        Request model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        """
        return await self._request(
            "cotton_bales_on_treadmills_v1.update_cotton_bales_on_treadmills_by_internal_id",
            "PUT",
            "/CottonBalesOnTreadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_bales_on_treadmills_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção do vinculo do fardão da esteira a qual está vinculado.

        DELETE /CottonBalesOnTreadmills/{InternalId}; operationId=DeleteCottonBalesOnTreadmillID; Protheus >= 12.1.23

        Deleção do fardão informado da fila a qual pertence.

        Response model: protheus.models.cotton_bales_on_treadmills_v1.CottonBalesOnTreadmillsType
        """
        return await self._request(
            "cotton_bales_on_treadmills_v1.delete_cotton_bales_on_treadmills_by_internal_id",
            "DELETE",
            "/CottonBalesOnTreadmills/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
