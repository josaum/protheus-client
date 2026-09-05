"""Solicitante — generated from Requesters_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RequestersV1(ApiGroup):
    """Solicitante (/api/tms/v1)."""

    api_id = "requesters_v1"
    base_path = "/api/tms/v1"

    def list_requesters(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Solicitante

        GET /Requesters; operationId=getRequesters; Protheus >= 12.1.21

        Retorna lista completa do Solicitante

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.requesters_v1.PagedRequesters
        """
        return self._request(
            "requesters_v1.list_requesters",
            "GET",
            "/Requesters",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_requesters(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Solicitante

        POST /Requesters; operationId=postRequesters; Protheus >= 12.1.21

        Inclui um Solicitante conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.requesters_v1.PagedRequesters
        Request model: protheus.models.requesters_v1.RequestersInfo
        """
        return self._request(
            "requesters_v1.create_requesters",
            "POST",
            "/Requesters",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_requesters_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Solicitante específica de acordo com a chave de pesquisa

        GET /Requesters/{InternalId}; operationId=getCode; Protheus >= 12.1.21

        Retorna o Solicitante de acordo com o ID de pesquisa

        TOTVS note: o Code é composto por filial + Código do Solicitante

        Response model: protheus.models.requesters_v1.RequestersInfo
        """
        return self._request(
            "requesters_v1.get_requesters_by_internal_id",
            "GET",
            "/Requesters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_requesters_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Solicitante

        PUT /Requesters/{InternalId}; operationId=putCode; Protheus >= 12.1.21

        Atualiza o Solicitante conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.requesters_v1.RequestersInfo
        Request model: protheus.models.requesters_v1.RequestersInfo
        """
        return self._request(
            "requesters_v1.update_requesters_by_internal_id",
            "PUT",
            "/Requesters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_requesters_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Solicitante

        DELETE /Requesters/{InternalId}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Solicitante conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "requesters_v1.delete_requesters_by_internal_id",
            "DELETE",
            "/Requesters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRequestersV1(AsyncApiGroup):
    """Solicitante (/api/tms/v1)."""

    api_id = "requesters_v1"
    base_path = "/api/tms/v1"

    async def list_requesters(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Solicitante

        GET /Requesters; operationId=getRequesters; Protheus >= 12.1.21

        Retorna lista completa do Solicitante

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.requesters_v1.PagedRequesters
        """
        return await self._request(
            "requesters_v1.list_requesters",
            "GET",
            "/Requesters",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_requesters(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Solicitante

        POST /Requesters; operationId=postRequesters; Protheus >= 12.1.21

        Inclui um Solicitante conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.requesters_v1.PagedRequesters
        Request model: protheus.models.requesters_v1.RequestersInfo
        """
        return await self._request(
            "requesters_v1.create_requesters",
            "POST",
            "/Requesters",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_requesters_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Solicitante específica de acordo com a chave de pesquisa

        GET /Requesters/{InternalId}; operationId=getCode; Protheus >= 12.1.21

        Retorna o Solicitante de acordo com o ID de pesquisa

        TOTVS note: o Code é composto por filial + Código do Solicitante

        Response model: protheus.models.requesters_v1.RequestersInfo
        """
        return await self._request(
            "requesters_v1.get_requesters_by_internal_id",
            "GET",
            "/Requesters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_requesters_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Solicitante

        PUT /Requesters/{InternalId}; operationId=putCode; Protheus >= 12.1.21

        Atualiza o Solicitante conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Code e Fields

        Response model: protheus.models.requesters_v1.RequestersInfo
        Request model: protheus.models.requesters_v1.RequestersInfo
        """
        return await self._request(
            "requesters_v1.update_requesters_by_internal_id",
            "PUT",
            "/Requesters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_requesters_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Solicitante

        DELETE /Requesters/{InternalId}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Solicitante conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "requesters_v1.delete_requesters_by_internal_id",
            "DELETE",
            "/Requesters/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
