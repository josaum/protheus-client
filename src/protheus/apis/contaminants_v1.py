"""Contaminants — generated from Contaminants_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ContaminantsV1(ApiGroup):
    """Contaminants (/api/agr/v1)."""

    api_id = "contaminants_v1"
    base_path = "/api/agr/v1"

    def list_contaminants(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas os contaminantes da base

        GET /Contaminants; operationId=getContaminants; Protheus >= 12.1.23

        Retorna todos os contaminantes da base

        Response model: protheus.models.contaminants_v1.PagedContaminants
        """
        return self._request(
            "contaminants_v1.list_contaminants",
            "GET",
            "/Contaminants",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_contaminants(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um contaminante.

        POST /Contaminants; operationId=postContaminant; Protheus >= 12.1.23

        Inclui um contaminante passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.contaminants_v1.ContaminantsType
        Request model: protheus.models.contaminants_v1.ContaminantsType
        """
        return self._request(
            "contaminants_v1.create_contaminants",
            "POST",
            "/Contaminants",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_contaminants_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o contaminante.

        GET /Contaminants/{InternalId}; operationId=getContaminantID; Protheus >= 12.1.23

        Retorna o contaminante correspondente ao parametro informado

        Response model: protheus.models.contaminants_v1.ContaminantsType
        """
        return self._request(
            "contaminants_v1.get_contaminants_by_internal_id",
            "GET",
            "/Contaminants/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_contaminants_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o contaminante.

        PUT /Contaminants/{InternalId}; operationId=putContaminantID; Protheus >= 12.1.23

        Altera o contaminante passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.contaminants_v1.ContaminantsType
        Request model: protheus.models.contaminants_v1.ContaminantsType
        """
        return self._request(
            "contaminants_v1.update_contaminants_by_internal_id",
            "PUT",
            "/Contaminants/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_contaminants_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção do contaminante

        DELETE /Contaminants/{InternalId}; operationId=DeleteContaminantID; Protheus >= 12.1.23

        Deleção do contaminante informado.

        Response model: protheus.models.contaminants_v1.ContaminantsType
        """
        return self._request(
            "contaminants_v1.delete_contaminants_by_internal_id",
            "DELETE",
            "/Contaminants/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncContaminantsV1(AsyncApiGroup):
    """Contaminants (/api/agr/v1)."""

    api_id = "contaminants_v1"
    base_path = "/api/agr/v1"

    async def list_contaminants(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas os contaminantes da base

        GET /Contaminants; operationId=getContaminants; Protheus >= 12.1.23

        Retorna todos os contaminantes da base

        Response model: protheus.models.contaminants_v1.PagedContaminants
        """
        return await self._request(
            "contaminants_v1.list_contaminants",
            "GET",
            "/Contaminants",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_contaminants(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um contaminante.

        POST /Contaminants; operationId=postContaminant; Protheus >= 12.1.23

        Inclui um contaminante passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.contaminants_v1.ContaminantsType
        Request model: protheus.models.contaminants_v1.ContaminantsType
        """
        return await self._request(
            "contaminants_v1.create_contaminants",
            "POST",
            "/Contaminants",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_contaminants_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o contaminante.

        GET /Contaminants/{InternalId}; operationId=getContaminantID; Protheus >= 12.1.23

        Retorna o contaminante correspondente ao parametro informado

        Response model: protheus.models.contaminants_v1.ContaminantsType
        """
        return await self._request(
            "contaminants_v1.get_contaminants_by_internal_id",
            "GET",
            "/Contaminants/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_contaminants_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o contaminante.

        PUT /Contaminants/{InternalId}; operationId=putContaminantID; Protheus >= 12.1.23

        Altera o contaminante passado na requisição

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.contaminants_v1.ContaminantsType
        Request model: protheus.models.contaminants_v1.ContaminantsType
        """
        return await self._request(
            "contaminants_v1.update_contaminants_by_internal_id",
            "PUT",
            "/Contaminants/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_contaminants_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleção do contaminante

        DELETE /Contaminants/{InternalId}; operationId=DeleteContaminantID; Protheus >= 12.1.23

        Deleção do contaminante informado.

        Response model: protheus.models.contaminants_v1.ContaminantsType
        """
        return await self._request(
            "contaminants_v1.delete_contaminants_by_internal_id",
            "DELETE",
            "/Contaminants/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
