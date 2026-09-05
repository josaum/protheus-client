"""Comissão de Venda — generated from SalesCharge_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SalesChargeV1(ApiGroup):
    """Comissão de Venda (/api/fat/v1)."""

    api_id = "sales_charge_v1"
    base_path = "/api/fat/v1"

    def list_sales_charge(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as comissões dos vendedores

        GET /salesCharge; operationId=getsalesCharge; Protheus >= 12.1.21

        Retorna todos as comissões dos vendedores

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return self._request(
            "sales_charge_v1.list_sales_charge",
            "GET",
            "/salesCharge",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_sales_charge(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma comissão para um determinado vendedor

        POST /salesCharge; operationId=postsalesCarge; Protheus >= 12.1.21

        TOTVS note: Inclui uma comissão para um determinado vendedor

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        Request model: protheus.models.sales_charge_v1.SalesChargeInfo
        """
        return self._request(
            "sales_charge_v1.create_sales_charge",
            "POST",
            "/salesCharge",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_sales_charge_by_internal_id(self, internal_id: str, *, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as comissões do vendedor

        GET /salesCharge/{InternalId}; operationId=getsalesChargeId; Protheus >= 12.1.21

        TOTVS note: Retorna todas as comissões do vendedor

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return self._request(
            "sales_charge_v1.get_sales_charge_by_internal_id",
            "GET",
            "/salesCharge/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_sales_charge_by_internal_id_and_account_receivable_document_internal_id(self, internal_id: str, account_receivable_document_internal_id: str, *, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a comissão do vendedor, com base nos parâmetros passados

        GET /salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}; operationId=getsalesChargeIdTitleId; Protheus >= 12.1.21

        TOTVS note: O Protheus considera o titleId como a concatenação dos seguintes campos E3_CODCLI+E3_LOJA+E3_PREFIXO+E3_NUM+E3_PARCELA+E3_TIPO

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return self._request(
            "sales_charge_v1.get_sales_charge_by_internal_id_and_account_receivable_document_internal_id",
            "GET",
            "/salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}",
            path_params={"InternalId": internal_id, "AccountReceivableDocumentInternalId": account_receivable_document_internal_id},
            query={"fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_sales_charge_by_internal_id_and_account_receivable_document_internal_id(self, internal_id: str, account_receivable_document_internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza a comissão do vendedor, com base nos parâmetros passados

        PUT /salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}; operationId=putsalesChargeId; Protheus >= 12.1.21

        TOTVS note: O Protheus considera o titleId como a concatenação dos seguintes campos E3_CODCLI+E3_LOJA+E3_PREFIXO+E3_NUM+E3_PARCELA+E3_TIPO

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        Request model: protheus.models.sales_charge_v1.SalesChargeInfo
        """
        return self._request(
            "sales_charge_v1.update_sales_charge_by_internal_id_and_account_receivable_document_internal_id",
            "PUT",
            "/salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}",
            path_params={"InternalId": internal_id, "AccountReceivableDocumentInternalId": account_receivable_document_internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_sales_charge_by_internal_id_and_account_receivable_document_internal_id(self, internal_id: str, account_receivable_document_internal_id: str, *, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui a comissão do vendedor, com base nos parâmetros passados

        DELETE /salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}; operationId=deletsalesChargeId; Protheus >= 12.1.21

        TOTVS note: O Protheus considera o titleId como a concatenação dos seguintes campos E3_CODCLI+E3_LOJA+E3_PREFIXO+E3_NUM+E3_PARCELA+E3_TIPO

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return self._request(
            "sales_charge_v1.delete_sales_charge_by_internal_id_and_account_receivable_document_internal_id",
            "DELETE",
            "/salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}",
            path_params={"InternalId": internal_id, "AccountReceivableDocumentInternalId": account_receivable_document_internal_id},
            query={"order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSalesChargeV1(AsyncApiGroup):
    """Comissão de Venda (/api/fat/v1)."""

    api_id = "sales_charge_v1"
    base_path = "/api/fat/v1"

    async def list_sales_charge(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as comissões dos vendedores

        GET /salesCharge; operationId=getsalesCharge; Protheus >= 12.1.21

        Retorna todos as comissões dos vendedores

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return await self._request(
            "sales_charge_v1.list_sales_charge",
            "GET",
            "/salesCharge",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_sales_charge(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma comissão para um determinado vendedor

        POST /salesCharge; operationId=postsalesCarge; Protheus >= 12.1.21

        TOTVS note: Inclui uma comissão para um determinado vendedor

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        Request model: protheus.models.sales_charge_v1.SalesChargeInfo
        """
        return await self._request(
            "sales_charge_v1.create_sales_charge",
            "POST",
            "/salesCharge",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_sales_charge_by_internal_id(self, internal_id: str, *, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as comissões do vendedor

        GET /salesCharge/{InternalId}; operationId=getsalesChargeId; Protheus >= 12.1.21

        TOTVS note: Retorna todas as comissões do vendedor

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return await self._request(
            "sales_charge_v1.get_sales_charge_by_internal_id",
            "GET",
            "/salesCharge/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_sales_charge_by_internal_id_and_account_receivable_document_internal_id(self, internal_id: str, account_receivable_document_internal_id: str, *, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a comissão do vendedor, com base nos parâmetros passados

        GET /salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}; operationId=getsalesChargeIdTitleId; Protheus >= 12.1.21

        TOTVS note: O Protheus considera o titleId como a concatenação dos seguintes campos E3_CODCLI+E3_LOJA+E3_PREFIXO+E3_NUM+E3_PARCELA+E3_TIPO

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return await self._request(
            "sales_charge_v1.get_sales_charge_by_internal_id_and_account_receivable_document_internal_id",
            "GET",
            "/salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}",
            path_params={"InternalId": internal_id, "AccountReceivableDocumentInternalId": account_receivable_document_internal_id},
            query={"fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_sales_charge_by_internal_id_and_account_receivable_document_internal_id(self, internal_id: str, account_receivable_document_internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza a comissão do vendedor, com base nos parâmetros passados

        PUT /salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}; operationId=putsalesChargeId; Protheus >= 12.1.21

        TOTVS note: O Protheus considera o titleId como a concatenação dos seguintes campos E3_CODCLI+E3_LOJA+E3_PREFIXO+E3_NUM+E3_PARCELA+E3_TIPO

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        Request model: protheus.models.sales_charge_v1.SalesChargeInfo
        """
        return await self._request(
            "sales_charge_v1.update_sales_charge_by_internal_id_and_account_receivable_document_internal_id",
            "PUT",
            "/salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}",
            path_params={"InternalId": internal_id, "AccountReceivableDocumentInternalId": account_receivable_document_internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_sales_charge_by_internal_id_and_account_receivable_document_internal_id(self, internal_id: str, account_receivable_document_internal_id: str, *, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui a comissão do vendedor, com base nos parâmetros passados

        DELETE /salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}; operationId=deletsalesChargeId; Protheus >= 12.1.21

        TOTVS note: O Protheus considera o titleId como a concatenação dos seguintes campos E3_CODCLI+E3_LOJA+E3_PREFIXO+E3_NUM+E3_PARCELA+E3_TIPO

        Response model: protheus.models.sales_charge_v1.PagedSalesCharge
        """
        return await self._request(
            "sales_charge_v1.delete_sales_charge_by_internal_id_and_account_receivable_document_internal_id",
            "DELETE",
            "/salesCharge/{InternalId}/{AccountReceivableDocumentInternalId}",
            path_params={"InternalId": internal_id, "AccountReceivableDocumentInternalId": account_receivable_document_internal_id},
            query={"order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )
