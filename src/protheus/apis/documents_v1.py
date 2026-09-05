"""Documentos — generated from Documents_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class DocumentsV1(ApiGroup):
    """Documentos (/api/crm/v1)."""

    api_id = "documents_v1"
    base_path = "/api/crm/v1"

    def list_documents(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os documentos das entidades armazenado no banco de conhecimento

        GET /documents; operationId=getdocuments; Protheus >= 12.1.21

        Response model: protheus.models.documents_v1.PagedDocument
        """
        return self._request(
            "documents_v1.list_documents",
            "GET",
            "/documents",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_documents(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um novo documentos no banco de conhecimento

        POST /documents; operationId=postdocuments; Protheus >= 12.1.21

        TOTVS note: Inclui um novo documentos no banco de conhecimento

        Response model: protheus.models.documents_v1.Documents
        Request model: protheus.models.documents_v1.Documents
        """
        return self._request(
            "documents_v1.create_documents",
            "POST",
            "/documents",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_documents_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o documento da entidade armazenado no banco de conhecimento

        GET /documents/{InternalId}; operationId=getDocuments; Protheus >= 12.1.21

        TOTVS note: Retorna o documento armazenado no banco de conhecimento

        Response model: protheus.models.documents_v1.Documents
        """
        return self._request(
            "documents_v1.get_documents_by_internal_id",
            "GET",
            "/documents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_documents_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o documento da entidade armazenado no banco de conhecimento

        PUT /documents/{InternalId}; operationId=putDocuments; Protheus >= 12.1.21

        Altera o documento armazenado no banco de conhecimento

        TOTVS note: Altera o documento armazenado no banco de conhecimento

        Response model: protheus.models.documents_v1.Documents
        Request model: protheus.models.documents_v1.Documents
        """
        return self._request(
            "documents_v1.update_documents_by_internal_id",
            "PUT",
            "/documents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_documents_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui o documento da entidade armazenado no banco de conhecimento

        DELETE /documents/{InternalId}; operationId=deleteDocuments; Protheus >= 12.1.21

        Exclui os documento armazenado no banco de conhecimento

        TOTVS note: Exclui o documento armazenado no banco de conhecimento
        """
        return self._request(
            "documents_v1.delete_documents_by_internal_id",
            "DELETE",
            "/documents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncDocumentsV1(AsyncApiGroup):
    """Documentos (/api/crm/v1)."""

    api_id = "documents_v1"
    base_path = "/api/crm/v1"

    async def list_documents(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os documentos das entidades armazenado no banco de conhecimento

        GET /documents; operationId=getdocuments; Protheus >= 12.1.21

        Response model: protheus.models.documents_v1.PagedDocument
        """
        return await self._request(
            "documents_v1.list_documents",
            "GET",
            "/documents",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_documents(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um novo documentos no banco de conhecimento

        POST /documents; operationId=postdocuments; Protheus >= 12.1.21

        TOTVS note: Inclui um novo documentos no banco de conhecimento

        Response model: protheus.models.documents_v1.Documents
        Request model: protheus.models.documents_v1.Documents
        """
        return await self._request(
            "documents_v1.create_documents",
            "POST",
            "/documents",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_documents_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o documento da entidade armazenado no banco de conhecimento

        GET /documents/{InternalId}; operationId=getDocuments; Protheus >= 12.1.21

        TOTVS note: Retorna o documento armazenado no banco de conhecimento

        Response model: protheus.models.documents_v1.Documents
        """
        return await self._request(
            "documents_v1.get_documents_by_internal_id",
            "GET",
            "/documents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_documents_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o documento da entidade armazenado no banco de conhecimento

        PUT /documents/{InternalId}; operationId=putDocuments; Protheus >= 12.1.21

        Altera o documento armazenado no banco de conhecimento

        TOTVS note: Altera o documento armazenado no banco de conhecimento

        Response model: protheus.models.documents_v1.Documents
        Request model: protheus.models.documents_v1.Documents
        """
        return await self._request(
            "documents_v1.update_documents_by_internal_id",
            "PUT",
            "/documents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_documents_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui o documento da entidade armazenado no banco de conhecimento

        DELETE /documents/{InternalId}; operationId=deleteDocuments; Protheus >= 12.1.21

        Exclui os documento armazenado no banco de conhecimento

        TOTVS note: Exclui o documento armazenado no banco de conhecimento
        """
        return await self._request(
            "documents_v1.delete_documents_by_internal_id",
            "DELETE",
            "/documents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
