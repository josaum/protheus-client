"""FreightDocuments — generated from FreightDocuments_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class FreightDocumentsV1(ApiGroup):
    """FreightDocuments (/api/gfe/v1)."""

    api_id = "freight_documents_v1"
    base_path = "/api/gfe/v1"

    def list_freight_documents(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os documentos de frete cadastrados.

        GET /FreightDocuments; operationId=getFreightDocuments; Protheus >= 12.1.30

        Response model: protheus.models.freight_documents_v1.PagedFreightDocuments
        """
        return self._request(
            "freight_documents_v1.list_freight_documents",
            "GET",
            "/FreightDocuments",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_freight_documents_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um documento de frete.

        GET /FreightDocuments/{InternalId}; operationId=getFreightDocumentsID; Protheus >= 12.1.30

        Retorna o documento de frete requerido.

        Response model: protheus.models.freight_documents_v1.FreightDocumentsType
        """
        return self._request(
            "freight_documents_v1.get_freight_documents_by_internal_id",
            "GET",
            "/FreightDocuments/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_freight_documents_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a situação de um documento de frete.

        PUT /FreightDocuments/{InternalId}; operationId=putFreightDocumentsID; Protheus >= 12.1.30

        Altera a situação do documento de frete, requerido através da chave do registro (InternalId).

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.freight_documents_v1.FreightDocumentsType
        Request model: protheus.models.freight_documents_v1.FreightDocumentsType
        """
        return self._request(
            "freight_documents_v1.update_freight_documents_by_internal_id",
            "PUT",
            "/FreightDocuments/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncFreightDocumentsV1(AsyncApiGroup):
    """FreightDocuments (/api/gfe/v1)."""

    api_id = "freight_documents_v1"
    base_path = "/api/gfe/v1"

    async def list_freight_documents(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os documentos de frete cadastrados.

        GET /FreightDocuments; operationId=getFreightDocuments; Protheus >= 12.1.30

        Response model: protheus.models.freight_documents_v1.PagedFreightDocuments
        """
        return await self._request(
            "freight_documents_v1.list_freight_documents",
            "GET",
            "/FreightDocuments",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_freight_documents_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um documento de frete.

        GET /FreightDocuments/{InternalId}; operationId=getFreightDocumentsID; Protheus >= 12.1.30

        Retorna o documento de frete requerido.

        Response model: protheus.models.freight_documents_v1.FreightDocumentsType
        """
        return await self._request(
            "freight_documents_v1.get_freight_documents_by_internal_id",
            "GET",
            "/FreightDocuments/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_freight_documents_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a situação de um documento de frete.

        PUT /FreightDocuments/{InternalId}; operationId=putFreightDocumentsID; Protheus >= 12.1.30

        Altera a situação do documento de frete, requerido através da chave do registro (InternalId).

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.freight_documents_v1.FreightDocumentsType
        Request model: protheus.models.freight_documents_v1.FreightDocumentsType
        """
        return await self._request(
            "freight_documents_v1.update_freight_documents_by_internal_id",
            "PUT",
            "/FreightDocuments/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
