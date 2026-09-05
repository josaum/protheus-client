"""Item Contábil — generated from AccountingItems_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AccountingItemsV1(ApiGroup):
    """Item Contábil (/api/ctb/v1)."""

    api_id = "accounting_items_v1"
    base_path = "/api/ctb/v1"

    def list_accounting_items(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Itens Contábeis

        GET /AccountingItems; operationId=getAccountingItems; Protheus >= 12.1.21

        Retorna lista completa de itens contábeis

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.accounting_items_v1.PagedItems
        """
        return self._request(
            "accounting_items_v1.list_accounting_items",
            "GET",
            "/AccountingItems",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_accounting_items(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item contábil

        POST /AccountingItems; operationId=postAccountingItems; Protheus >= 12.1.21

        Inclui um item contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.accounting_items_v1.BusinessContentType
        Request model: protheus.models.accounting_items_v1.BusinessContentType
        """
        return self._request(
            "accounting_items_v1.create_accounting_items",
            "POST",
            "/AccountingItems",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_accounting_items_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um item contábil específico de acordo com a chave de pesquisa

        GET /AccountingItems/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o item contábil de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código da Anotação

        Response model: protheus.models.accounting_items_v1.BusinessContentType
        """
        return self._request(
            "accounting_items_v1.get_accounting_items_by_internal_id",
            "GET",
            "/AccountingItems/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_accounting_items_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Item Contábil

        PUT /AccountingItems/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o item contábil conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.accounting_items_v1.BusinessContentType
        Request model: protheus.models.accounting_items_v1.BusinessContentType
        """
        return self._request(
            "accounting_items_v1.update_accounting_items_by_internal_id",
            "PUT",
            "/AccountingItems/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_accounting_items_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Item Contábil

        DELETE /AccountingItems/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Item Contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "accounting_items_v1.delete_accounting_items_by_internal_id",
            "DELETE",
            "/AccountingItems/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncAccountingItemsV1(AsyncApiGroup):
    """Item Contábil (/api/ctb/v1)."""

    api_id = "accounting_items_v1"
    base_path = "/api/ctb/v1"

    async def list_accounting_items(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Itens Contábeis

        GET /AccountingItems; operationId=getAccountingItems; Protheus >= 12.1.21

        Retorna lista completa de itens contábeis

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.accounting_items_v1.PagedItems
        """
        return await self._request(
            "accounting_items_v1.list_accounting_items",
            "GET",
            "/AccountingItems",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_accounting_items(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item contábil

        POST /AccountingItems; operationId=postAccountingItems; Protheus >= 12.1.21

        Inclui um item contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.accounting_items_v1.BusinessContentType
        Request model: protheus.models.accounting_items_v1.BusinessContentType
        """
        return await self._request(
            "accounting_items_v1.create_accounting_items",
            "POST",
            "/AccountingItems",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_accounting_items_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um item contábil específico de acordo com a chave de pesquisa

        GET /AccountingItems/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o item contábil de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código da Anotação

        Response model: protheus.models.accounting_items_v1.BusinessContentType
        """
        return await self._request(
            "accounting_items_v1.get_accounting_items_by_internal_id",
            "GET",
            "/AccountingItems/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_accounting_items_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Item Contábil

        PUT /AccountingItems/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o item contábil conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.accounting_items_v1.BusinessContentType
        Request model: protheus.models.accounting_items_v1.BusinessContentType
        """
        return await self._request(
            "accounting_items_v1.update_accounting_items_by_internal_id",
            "PUT",
            "/AccountingItems/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_accounting_items_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Item Contábil

        DELETE /AccountingItems/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Item Contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "accounting_items_v1.delete_accounting_items_by_internal_id",
            "DELETE",
            "/AccountingItems/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
