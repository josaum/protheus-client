"""CottonGinBreaks — generated from CottonGinBreaks_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonGinBreaksV1(ApiGroup):
    """CottonGinBreaks (/api/agr/v1)."""

    api_id = "cotton_gin_breaks_v1"
    base_path = "/api/agr/v1"

    def list_cotton_gin_breaks(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Motivos de Parada da beneficiadora cadastrados.

        GET /CottonGinBreaks; operationId=getCottonGinBreaks; Protheus >= 12.1.23

        Retorna todos os Motivo de Parada da beneficiadora cadastrados.

        Response model: protheus.models.cotton_gin_breaks_v1.PagedCottonGinBreaks
        """
        return self._request(
            "cotton_gin_breaks_v1.list_cotton_gin_breaks",
            "GET",
            "/CottonGinBreaks",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cotton_gin_breaks(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um motivo de parada da beneficiadora.

        POST /CottonGinBreaks; operationId=postCottonGinBreaks; Protheus >= 12.1.23

        Inclui o motivo de parada da beneficiadora passado na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return self._request(
            "cotton_gin_breaks_v1.create_cotton_gin_breaks",
            "POST",
            "/CottonGinBreaks",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_cotton_gin_breaks_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o motivo de parada da beneficiadora.

        GET /CottonGinBreaks/{InternalId}; operationId=getCottonGinBreakID; Protheus >= 12.1.23

        Retorna o motivo de parada da beneficiadora correspondente ao parâmetro informado

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return self._request(
            "cotton_gin_breaks_v1.get_cotton_gin_breaks_by_internal_id",
            "GET",
            "/CottonGinBreaks/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_gin_breaks_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a descrição do motivo.

        PUT /CottonGinBreaks/{InternalId}; operationId=putCottonGinBreakID; Protheus >= 12.1.23

        Alterada a descrição do motivo em questão.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        Request model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return self._request(
            "cotton_gin_breaks_v1.update_cotton_gin_breaks_by_internal_id",
            "PUT",
            "/CottonGinBreaks/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_gin_breaks_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o motivo de parada da beneficiadora dos registros.

        DELETE /CottonGinBreaks/{InternalId}; operationId=DeleteCottonGinBreakID; Protheus >= 12.1.23

        Deleção do motivo de parada da beneficiadora dos registros.

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return self._request(
            "cotton_gin_breaks_v1.delete_cotton_gin_breaks_by_internal_id",
            "DELETE",
            "/CottonGinBreaks/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonGinBreaksV1(AsyncApiGroup):
    """CottonGinBreaks (/api/agr/v1)."""

    api_id = "cotton_gin_breaks_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_gin_breaks(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Motivos de Parada da beneficiadora cadastrados.

        GET /CottonGinBreaks; operationId=getCottonGinBreaks; Protheus >= 12.1.23

        Retorna todos os Motivo de Parada da beneficiadora cadastrados.

        Response model: protheus.models.cotton_gin_breaks_v1.PagedCottonGinBreaks
        """
        return await self._request(
            "cotton_gin_breaks_v1.list_cotton_gin_breaks",
            "GET",
            "/CottonGinBreaks",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cotton_gin_breaks(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um motivo de parada da beneficiadora.

        POST /CottonGinBreaks; operationId=postCottonGinBreaks; Protheus >= 12.1.23

        Inclui o motivo de parada da beneficiadora passado na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return await self._request(
            "cotton_gin_breaks_v1.create_cotton_gin_breaks",
            "POST",
            "/CottonGinBreaks",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_cotton_gin_breaks_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o motivo de parada da beneficiadora.

        GET /CottonGinBreaks/{InternalId}; operationId=getCottonGinBreakID; Protheus >= 12.1.23

        Retorna o motivo de parada da beneficiadora correspondente ao parâmetro informado

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return await self._request(
            "cotton_gin_breaks_v1.get_cotton_gin_breaks_by_internal_id",
            "GET",
            "/CottonGinBreaks/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_gin_breaks_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a descrição do motivo.

        PUT /CottonGinBreaks/{InternalId}; operationId=putCottonGinBreakID; Protheus >= 12.1.23

        Alterada a descrição do motivo em questão.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        Request model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return await self._request(
            "cotton_gin_breaks_v1.update_cotton_gin_breaks_by_internal_id",
            "PUT",
            "/CottonGinBreaks/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_gin_breaks_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o motivo de parada da beneficiadora dos registros.

        DELETE /CottonGinBreaks/{InternalId}; operationId=DeleteCottonGinBreakID; Protheus >= 12.1.23

        Deleção do motivo de parada da beneficiadora dos registros.

        Response model: protheus.models.cotton_gin_breaks_v1.CottonGinBreaksType
        """
        return await self._request(
            "cotton_gin_breaks_v1.delete_cotton_gin_breaks_by_internal_id",
            "DELETE",
            "/CottonGinBreaks/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
