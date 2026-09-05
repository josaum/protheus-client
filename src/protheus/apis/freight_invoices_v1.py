"""FreightInvoices — generated from FreightInvoices_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class FreightInvoicesV1(ApiGroup):
    """FreightInvoices (/api/gfe/v1)."""

    api_id = "freight_invoices_v1"
    base_path = "/api/gfe/v1"

    def list_freight_invoices(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as faturas de frete cadastradas.

        GET /FreightInvoices; operationId=getFreightInvoices; Protheus >= 12.1.30

        Response model: protheus.models.freight_invoices_v1.PagedFreightInvoices
        """
        return self._request(
            "freight_invoices_v1.list_freight_invoices",
            "GET",
            "/FreightInvoices",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_freight_invoices_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma fatura de frete.

        GET /FreightInvoices/{InternalId}; operationId=getFreightInvoicesID; Protheus >= 12.1.30

        Retorna apenas uma fatura de frete, requerida através da chave do registro (InternalId).

        Response model: protheus.models.freight_invoices_v1.FreightInvoicesType
        """
        return self._request(
            "freight_invoices_v1.get_freight_invoices_by_internal_id",
            "GET",
            "/FreightInvoices/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_freight_invoices_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a situação de uma fatura de frete.

        PUT /FreightInvoices/{InternalId}; operationId=putFreightInvoicesID; Protheus >= 12.1.30

        Altera a situação da fatura de frete informada através da chave (InternalId).

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.freight_invoices_v1.FreightInvoicesType
        Request model: protheus.models.freight_invoices_v1.FreightInvoicesType
        """
        return self._request(
            "freight_invoices_v1.update_freight_invoices_by_internal_id",
            "PUT",
            "/FreightInvoices/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncFreightInvoicesV1(AsyncApiGroup):
    """FreightInvoices (/api/gfe/v1)."""

    api_id = "freight_invoices_v1"
    base_path = "/api/gfe/v1"

    async def list_freight_invoices(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as faturas de frete cadastradas.

        GET /FreightInvoices; operationId=getFreightInvoices; Protheus >= 12.1.30

        Response model: protheus.models.freight_invoices_v1.PagedFreightInvoices
        """
        return await self._request(
            "freight_invoices_v1.list_freight_invoices",
            "GET",
            "/FreightInvoices",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_freight_invoices_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma fatura de frete.

        GET /FreightInvoices/{InternalId}; operationId=getFreightInvoicesID; Protheus >= 12.1.30

        Retorna apenas uma fatura de frete, requerida através da chave do registro (InternalId).

        Response model: protheus.models.freight_invoices_v1.FreightInvoicesType
        """
        return await self._request(
            "freight_invoices_v1.get_freight_invoices_by_internal_id",
            "GET",
            "/FreightInvoices/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_freight_invoices_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a situação de uma fatura de frete.

        PUT /FreightInvoices/{InternalId}; operationId=putFreightInvoicesID; Protheus >= 12.1.30

        Altera a situação da fatura de frete informada através da chave (InternalId).

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.freight_invoices_v1.FreightInvoicesType
        Request model: protheus.models.freight_invoices_v1.FreightInvoicesType
        """
        return await self._request(
            "freight_invoices_v1.update_freight_invoices_by_internal_id",
            "PUT",
            "/FreightInvoices/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
