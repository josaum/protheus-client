"""Produtos Varejo — generated from RetailItem_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RetailItemV1(ApiGroup):
    """Produtos Varejo (/api/retail/v1)."""

    api_id = "retail_item_v1"
    base_path = "/api/retail/v1"

    def list_retail_item(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com todos os Produtos

        GET /retailItem; operationId=getItems; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_item_v1.PagedItems
        """
        return self._request(
            "retail_item_v1.list_retail_item",
            "GET",
            "/retailItem",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRetailItemV1(AsyncApiGroup):
    """Produtos Varejo (/api/retail/v1)."""

    api_id = "retail_item_v1"
    base_path = "/api/retail/v1"

    async def list_retail_item(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com todos os Produtos

        GET /retailItem; operationId=getItems; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros.

        Response model: protheus.models.retail_item_v1.PagedItems
        """
        return await self._request(
            "retail_item_v1.list_retail_item",
            "GET",
            "/retailItem",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )
