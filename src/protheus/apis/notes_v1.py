"""Notas — generated from Notes_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class NotesV1(ApiGroup):
    """Notas (/api/crm/v1)."""

    api_id = "notes_v1"
    base_path = "/api/crm/v1"

    def list_notes(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Anotações

        GET /notes; operationId=getNotes; Protheus >= 12.1.21

        Retorna lista completa das Anotações

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.notes_v1.PagedNotes
        """
        return self._request(
            "notes_v1.list_notes",
            "GET",
            "/notes",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_notes(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma anotação

        POST /notes; operationId=postNotes; Protheus >= 12.1.21

        Inclui uma anotação conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.notes_v1.PagedNotes
        Request model: protheus.models.notes_v1.NotesInfo
        """
        return self._request(
            "notes_v1.create_notes",
            "POST",
            "/notes",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_notes_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma anotação específica de acordo com a chave de pesquisa

        GET /notes/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a anotação de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código da Anotação

        Response model: protheus.models.notes_v1.NotesInfo
        """
        return self._request(
            "notes_v1.get_notes_by_internal_id",
            "GET",
            "/notes/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_notes_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Anotação

        PUT /notes/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a anotação conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.notes_v1.NotesInfo
        Request model: protheus.models.notes_v1.NotesInfo
        """
        return self._request(
            "notes_v1.update_notes_by_internal_id",
            "PUT",
            "/notes/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_notes_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Anotação

        DELETE /notes/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui uma anotação conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "notes_v1.delete_notes_by_internal_id",
            "DELETE",
            "/notes/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncNotesV1(AsyncApiGroup):
    """Notas (/api/crm/v1)."""

    api_id = "notes_v1"
    base_path = "/api/crm/v1"

    async def list_notes(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Anotações

        GET /notes; operationId=getNotes; Protheus >= 12.1.21

        Retorna lista completa das Anotações

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.notes_v1.PagedNotes
        """
        return await self._request(
            "notes_v1.list_notes",
            "GET",
            "/notes",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_notes(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma anotação

        POST /notes; operationId=postNotes; Protheus >= 12.1.21

        Inclui uma anotação conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.notes_v1.PagedNotes
        Request model: protheus.models.notes_v1.NotesInfo
        """
        return await self._request(
            "notes_v1.create_notes",
            "POST",
            "/notes",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_notes_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma anotação específica de acordo com a chave de pesquisa

        GET /notes/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a anotação de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código da Anotação

        Response model: protheus.models.notes_v1.NotesInfo
        """
        return await self._request(
            "notes_v1.get_notes_by_internal_id",
            "GET",
            "/notes/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_notes_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Anotação

        PUT /notes/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a anotação conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.notes_v1.NotesInfo
        Request model: protheus.models.notes_v1.NotesInfo
        """
        return await self._request(
            "notes_v1.update_notes_by_internal_id",
            "PUT",
            "/notes/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_notes_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Anotação

        DELETE /notes/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui uma anotação conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "notes_v1.delete_notes_by_internal_id",
            "DELETE",
            "/notes/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
