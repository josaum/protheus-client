"""Tabela de Preços Varejo — generated from RetailPriceList_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RetailPriceListV1(ApiGroup):
    """Tabela de Preços Varejo (/api/retail/v1)."""

    api_id = "retail_price_list_v1"
    base_path = "/api/retail/v1"

    def list_retail_price_list(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com o cabeçalho de todas as Tabelas de Preço

        GET /retailPriceList; operationId=getHeaders; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_price_list_v1.PagedPriceListHeader
        """
        return self._request(
            "retail_price_list_v1.list_retail_price_list",
            "GET",
            "/retailPriceList",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_retail_price_list_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o cabeçalho de uma única Tabela de Preço a partir do internalId (identificador único da Tabela de Preço)

        GET /retailPriceList/{internalId}; operationId=getInternalIdHeader; Protheus >= 12.1.25

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Fields e InternalId.

        Response model: protheus.models.retail_price_list_v1.PriceListHeaderInfo
        """
        return self._request(
            "retail_price_list_v1.get_retail_price_list_by_internal_id",
            "GET",
            "/retailPriceList/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_retail_price_list_by_internal_id_itens_table_price(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os itens de uma única Tabela de Preço a partir do internalId (identificador único da Tabela de Preço)

        GET /retailPriceList/{internalId}/itensTablePrice/; operationId=getTableInternalIdItems; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_price_list_v1.PagedPriceListItem
        """
        return self._request(
            "retail_price_list_v1.list_retail_price_list_by_internal_id_itens_table_price",
            "GET",
            "/retailPriceList/{internalId}/itensTablePrice/",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRetailPriceListV1(AsyncApiGroup):
    """Tabela de Preços Varejo (/api/retail/v1)."""

    api_id = "retail_price_list_v1"
    base_path = "/api/retail/v1"

    async def list_retail_price_list(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com o cabeçalho de todas as Tabelas de Preço

        GET /retailPriceList; operationId=getHeaders; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_price_list_v1.PagedPriceListHeader
        """
        return await self._request(
            "retail_price_list_v1.list_retail_price_list",
            "GET",
            "/retailPriceList",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_retail_price_list_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o cabeçalho de uma única Tabela de Preço a partir do internalId (identificador único da Tabela de Preço)

        GET /retailPriceList/{internalId}; operationId=getInternalIdHeader; Protheus >= 12.1.25

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Fields e InternalId.

        Response model: protheus.models.retail_price_list_v1.PriceListHeaderInfo
        """
        return await self._request(
            "retail_price_list_v1.get_retail_price_list_by_internal_id",
            "GET",
            "/retailPriceList/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_retail_price_list_by_internal_id_itens_table_price(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os itens de uma única Tabela de Preço a partir do internalId (identificador único da Tabela de Preço)

        GET /retailPriceList/{internalId}/itensTablePrice/; operationId=getTableInternalIdItems; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_price_list_v1.PagedPriceListItem
        """
        return await self._request(
            "retail_price_list_v1.list_retail_price_list_by_internal_id_itens_table_price",
            "GET",
            "/retailPriceList/{internalId}/itensTablePrice/",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )
