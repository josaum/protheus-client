"""CottonGins — generated from CottonGins_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonGinsV1(ApiGroup):
    """CottonGins (/api/agr/v1)."""

    api_id = "cotton_gins_v1"
    base_path = "/api/agr/v1"

    def list_cotton_gins(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as unidades de beneficamento da base

        GET /CottonGins; operationId=getCottonGins; Protheus >= 12.1.23

        Response model: protheus.models.cotton_gins_v1.PagedBranches
        """
        return self._request(
            "cotton_gins_v1.list_cotton_gins",
            "GET",
            "/CottonGins",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cotton_gins(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma unidade de beneficamento

        POST /CottonGins; operationId=postCottonGin; Protheus >= 12.1.23

        Inclui uma unidade de beneficamento passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        Request model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return self._request(
            "cotton_gins_v1.create_cotton_gins",
            "POST",
            "/CottonGins",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_cotton_gins_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma unidade de beneficamento

        GET /CottonGins/{InternalId}; operationId=getCottonGinID; Protheus >= 12.1.23

        Retorna a unidade de beneficamento correspondente ao parametro informado

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return self._request(
            "cotton_gins_v1.get_cotton_gins_by_internal_id",
            "GET",
            "/CottonGins/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_gins_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a unidade de beneficamento

        PUT /CottonGins/{InternalId}; operationId=putCottonGinID; Protheus >= 12.1.23

        Altera a unidade de beneficamento passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        Request model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return self._request(
            "cotton_gins_v1.update_cotton_gins_by_internal_id",
            "PUT",
            "/CottonGins/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_gins_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção da unidade de beneficamento

        DELETE /CottonGins/{InternalId}; operationId=DeleteCottonGinID; Protheus >= 12.1.23

        Deleção da unidade de beneficamento informada

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return self._request(
            "cotton_gins_v1.delete_cotton_gins_by_internal_id",
            "DELETE",
            "/CottonGins/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonGinsV1(AsyncApiGroup):
    """CottonGins (/api/agr/v1)."""

    api_id = "cotton_gins_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_gins(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as unidades de beneficamento da base

        GET /CottonGins; operationId=getCottonGins; Protheus >= 12.1.23

        Response model: protheus.models.cotton_gins_v1.PagedBranches
        """
        return await self._request(
            "cotton_gins_v1.list_cotton_gins",
            "GET",
            "/CottonGins",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cotton_gins(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma unidade de beneficamento

        POST /CottonGins; operationId=postCottonGin; Protheus >= 12.1.23

        Inclui uma unidade de beneficamento passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        Request model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return await self._request(
            "cotton_gins_v1.create_cotton_gins",
            "POST",
            "/CottonGins",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_cotton_gins_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma unidade de beneficamento

        GET /CottonGins/{InternalId}; operationId=getCottonGinID; Protheus >= 12.1.23

        Retorna a unidade de beneficamento correspondente ao parametro informado

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return await self._request(
            "cotton_gins_v1.get_cotton_gins_by_internal_id",
            "GET",
            "/CottonGins/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_gins_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a unidade de beneficamento

        PUT /CottonGins/{InternalId}; operationId=putCottonGinID; Protheus >= 12.1.23

        Altera a unidade de beneficamento passada na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        Request model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return await self._request(
            "cotton_gins_v1.update_cotton_gins_by_internal_id",
            "PUT",
            "/CottonGins/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_gins_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção da unidade de beneficamento

        DELETE /CottonGins/{InternalId}; operationId=DeleteCottonGinID; Protheus >= 12.1.23

        Deleção da unidade de beneficamento informada

        Response model: protheus.models.cotton_gins_v1.CottonGinsType
        """
        return await self._request(
            "cotton_gins_v1.delete_cotton_gins_by_internal_id",
            "DELETE",
            "/CottonGins/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
