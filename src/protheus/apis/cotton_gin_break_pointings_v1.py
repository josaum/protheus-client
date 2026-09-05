"""CottonGinBreakPointings — generated from CottonGinBreakPointings_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonGinBreakPointingsV1(ApiGroup):
    """CottonGinBreakPointings (/api/agr/v1)."""

    api_id = "cotton_gin_break_pointings_v1"
    base_path = "/api/agr/v1"

    def list_cotton_gin_break_pointings(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os apontamentos de parada da beneficiadora cadastrados.

        GET /CottonGinBreakPointings; operationId=getCottonGinBreakPointings; Protheus >= 12.1.23

        Retorna todos os Motivo de Parada da beneficiadora.

        Response model: protheus.models.cotton_gin_break_pointings_v1.PagedCottonGinBreakPointings
        """
        return self._request(
            "cotton_gin_break_pointings_v1.list_cotton_gin_break_pointings",
            "GET",
            "/CottonGinBreakPointings",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cotton_gin_break_pointings(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um apontamento de parada da beneficiadora.

        POST /CottonGinBreakPointings; operationId=postCottonGinBreakPointings; Protheus >= 12.1.23

        Inclui o apontamento de motivo de parada para a beneficiadora passada na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return self._request(
            "cotton_gin_break_pointings_v1.create_cotton_gin_break_pointings",
            "POST",
            "/CottonGinBreakPointings",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_cotton_gin_break_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o apontamento de motivo de parada da beneficiadora.

        GET /CottonGinBreakPointings/{InternalId}; operationId=getCottonGinBreakPointingID; Protheus >= 12.1.23

        Retorna os apontamentos de parada da beneficiadora informada pelo parâmetro

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return self._request(
            "cotton_gin_break_pointings_v1.get_cotton_gin_break_pointings_by_internal_id",
            "GET",
            "/CottonGinBreakPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_gin_break_pointings_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o apontamento de motivo de parada da beneficiadora.

        PUT /CottonGinBreakPointings/{InternalId}; operationId=putCottonGinBreakPointingID; Protheus >= 12.1.23

        Altera o apontamento de motivo de parada da beneficiadora informada.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        Request model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return self._request(
            "cotton_gin_break_pointings_v1.update_cotton_gin_break_pointings_by_internal_id",
            "PUT",
            "/CottonGinBreakPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_gin_break_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o o apontamento de motivo de parada da beneficiadora.

        DELETE /CottonGinBreakPointings/{InternalId}; operationId=DeleteCottonGinBreakPointingID; Protheus >= 12.1.23

        Deleção do apontamento de parada da beneficiadora dos registros.

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return self._request(
            "cotton_gin_break_pointings_v1.delete_cotton_gin_break_pointings_by_internal_id",
            "DELETE",
            "/CottonGinBreakPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonGinBreakPointingsV1(AsyncApiGroup):
    """CottonGinBreakPointings (/api/agr/v1)."""

    api_id = "cotton_gin_break_pointings_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_gin_break_pointings(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os apontamentos de parada da beneficiadora cadastrados.

        GET /CottonGinBreakPointings; operationId=getCottonGinBreakPointings; Protheus >= 12.1.23

        Retorna todos os Motivo de Parada da beneficiadora.

        Response model: protheus.models.cotton_gin_break_pointings_v1.PagedCottonGinBreakPointings
        """
        return await self._request(
            "cotton_gin_break_pointings_v1.list_cotton_gin_break_pointings",
            "GET",
            "/CottonGinBreakPointings",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cotton_gin_break_pointings(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um apontamento de parada da beneficiadora.

        POST /CottonGinBreakPointings; operationId=postCottonGinBreakPointings; Protheus >= 12.1.23

        Inclui o apontamento de motivo de parada para a beneficiadora passada na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return await self._request(
            "cotton_gin_break_pointings_v1.create_cotton_gin_break_pointings",
            "POST",
            "/CottonGinBreakPointings",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_cotton_gin_break_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o apontamento de motivo de parada da beneficiadora.

        GET /CottonGinBreakPointings/{InternalId}; operationId=getCottonGinBreakPointingID; Protheus >= 12.1.23

        Retorna os apontamentos de parada da beneficiadora informada pelo parâmetro

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return await self._request(
            "cotton_gin_break_pointings_v1.get_cotton_gin_break_pointings_by_internal_id",
            "GET",
            "/CottonGinBreakPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_gin_break_pointings_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o apontamento de motivo de parada da beneficiadora.

        PUT /CottonGinBreakPointings/{InternalId}; operationId=putCottonGinBreakPointingID; Protheus >= 12.1.23

        Altera o apontamento de motivo de parada da beneficiadora informada.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        Request model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return await self._request(
            "cotton_gin_break_pointings_v1.update_cotton_gin_break_pointings_by_internal_id",
            "PUT",
            "/CottonGinBreakPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_gin_break_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o o apontamento de motivo de parada da beneficiadora.

        DELETE /CottonGinBreakPointings/{InternalId}; operationId=DeleteCottonGinBreakPointingID; Protheus >= 12.1.23

        Deleção do apontamento de parada da beneficiadora dos registros.

        Response model: protheus.models.cotton_gin_break_pointings_v1.CottonGinBreakPointingsType
        """
        return await self._request(
            "cotton_gin_break_pointings_v1.delete_cotton_gin_break_pointings_by_internal_id",
            "DELETE",
            "/CottonGinBreakPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
