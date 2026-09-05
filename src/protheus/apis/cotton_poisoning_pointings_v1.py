"""CottonPoisoningPointings — generated from CottonPoisoningPointings_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonPoisoningPointingsV1(ApiGroup):
    """CottonPoisoningPointings (/api/agr/v1)."""

    api_id = "cotton_poisoning_pointings_v1"
    base_path = "/api/agr/v1"

    def list_cotton_poisoning_pointings(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os lançamentos de contaminantes em algodão cadastrados.

        GET /CottonPoisoningPointings; operationId=getCottonPoisoningPointingsID; Protheus >= 12.1.23

        Response model: protheus.models.cotton_poisoning_pointings_v1.PagedCottonPoisoningPointings
        """
        return self._request(
            "cotton_poisoning_pointings_v1.list_cotton_poisoning_pointings",
            "GET",
            "/CottonPoisoningPointings",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cotton_poisoning_pointings(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Efetua o lançamento de contaminante.

        POST /CottonPoisoningPointings; operationId=postCottonPoisoningPointingID; Protheus >= 12.1.23

        Efetua o lançamento de contaminante para algodão.

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return self._request(
            "cotton_poisoning_pointings_v1.create_cotton_poisoning_pointings",
            "POST",
            "/CottonPoisoningPointings",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_cotton_poisoning_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um lançamento.

        GET /CottonPoisoningPointings/{InternalId}; operationId=getCottonPoisoningPointingID; Protheus >= 12.1.23

        Retorna o lançamento requerido.

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return self._request(
            "cotton_poisoning_pointings_v1.get_cotton_poisoning_pointings_by_internal_id",
            "GET",
            "/CottonPoisoningPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_poisoning_pointings_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o lançamento.

        PUT /CottonPoisoningPointings/{InternalId}; operationId=putCottonPoisoningPointingID; Protheus >= 12.1.23

        Altera o lançamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        Request model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return self._request(
            "cotton_poisoning_pointings_v1.update_cotton_poisoning_pointings_by_internal_id",
            "PUT",
            "/CottonPoisoningPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_poisoning_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui o lançamento.

        DELETE /CottonPoisoningPointings/{InternalId}; operationId=deleteCottonPoisoningPointingID; Protheus >= 12.1.23

        Exclui o lançamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return self._request(
            "cotton_poisoning_pointings_v1.delete_cotton_poisoning_pointings_by_internal_id",
            "DELETE",
            "/CottonPoisoningPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonPoisoningPointingsV1(AsyncApiGroup):
    """CottonPoisoningPointings (/api/agr/v1)."""

    api_id = "cotton_poisoning_pointings_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_poisoning_pointings(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os lançamentos de contaminantes em algodão cadastrados.

        GET /CottonPoisoningPointings; operationId=getCottonPoisoningPointingsID; Protheus >= 12.1.23

        Response model: protheus.models.cotton_poisoning_pointings_v1.PagedCottonPoisoningPointings
        """
        return await self._request(
            "cotton_poisoning_pointings_v1.list_cotton_poisoning_pointings",
            "GET",
            "/CottonPoisoningPointings",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cotton_poisoning_pointings(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Efetua o lançamento de contaminante.

        POST /CottonPoisoningPointings; operationId=postCottonPoisoningPointingID; Protheus >= 12.1.23

        Efetua o lançamento de contaminante para algodão.

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return await self._request(
            "cotton_poisoning_pointings_v1.create_cotton_poisoning_pointings",
            "POST",
            "/CottonPoisoningPointings",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_cotton_poisoning_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um lançamento.

        GET /CottonPoisoningPointings/{InternalId}; operationId=getCottonPoisoningPointingID; Protheus >= 12.1.23

        Retorna o lançamento requerido.

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return await self._request(
            "cotton_poisoning_pointings_v1.get_cotton_poisoning_pointings_by_internal_id",
            "GET",
            "/CottonPoisoningPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_poisoning_pointings_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o lançamento.

        PUT /CottonPoisoningPointings/{InternalId}; operationId=putCottonPoisoningPointingID; Protheus >= 12.1.23

        Altera o lançamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        Request model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return await self._request(
            "cotton_poisoning_pointings_v1.update_cotton_poisoning_pointings_by_internal_id",
            "PUT",
            "/CottonPoisoningPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_poisoning_pointings_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui o lançamento.

        DELETE /CottonPoisoningPointings/{InternalId}; operationId=deleteCottonPoisoningPointingID; Protheus >= 12.1.23

        Exclui o lançamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_poisoning_pointings_v1.CottonPoisoningPointingsType
        """
        return await self._request(
            "cotton_poisoning_pointings_v1.delete_cotton_poisoning_pointings_by_internal_id",
            "DELETE",
            "/CottonPoisoningPointings/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
