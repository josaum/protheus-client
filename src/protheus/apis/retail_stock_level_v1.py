"""Saldo em Estoque — generated from RetailStockLevel_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RetailStockLevelV1(ApiGroup):
    """Saldo em Estoque (/api/retail/v1)."""

    api_id = "retail_stock_level_v1"
    base_path = "/api/retail/v1"

    def list_retail_stock_level(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com todos os Produtos com saldo em estoque

        GET /retailStockLevel; operationId=getStock; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_stock_level_v1.PagedItems
        """
        return self._request(
            "retail_stock_level_v1.list_retail_stock_level",
            "GET",
            "/retailStockLevel",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRetailStockLevelV1(AsyncApiGroup):
    """Saldo em Estoque (/api/retail/v1)."""

    api_id = "retail_stock_level_v1"
    base_path = "/api/retail/v1"

    async def list_retail_stock_level(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com todos os Produtos com saldo em estoque

        GET /retailStockLevel; operationId=getStock; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_stock_level_v1.PagedItems
        """
        return await self._request(
            "retail_stock_level_v1.list_retail_stock_level",
            "GET",
            "/retailStockLevel",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )
