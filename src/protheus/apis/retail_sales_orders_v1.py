"""Pedidos de Venda do Varejo — generated from RetailSalesOrders_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RetailSalesOrdersV1(ApiGroup):
    """Pedidos de Venda do Varejo (/api/retail/v1)."""

    api_id = "retail_sales_orders_v1"
    base_path = "/api/retail/v1"

    def list_retail_sales_orders(self, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Lista pedidos de venda do varejo

        GET /retailSalesOrders; operationId=getRetailSalesOrders; availability inherited from API level

        Lista todos os pedidos de venda do faturamento (SC5) relacionados ao varejo.
        """
        return self._request(
            "retail_sales_orders_v1.list_retail_sales_orders",
            "GET",
            "/retailSalesOrders",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_retail_sales_orders_by_internal_id_items(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Lista itens do pedido de venda do varejo

        GET /retailSalesOrders/{internalId}/items; operationId=getRetailSalesOrderItems; availability inherited from API level

        Exibe os detalhes dos itens do pedido de venda (SC6) para o pedido informado.
        """
        return self._request(
            "retail_sales_orders_v1.list_retail_sales_orders_by_internal_id_items",
            "GET",
            "/retailSalesOrders/{internalId}/items",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRetailSalesOrdersV1(AsyncApiGroup):
    """Pedidos de Venda do Varejo (/api/retail/v1)."""

    api_id = "retail_sales_orders_v1"
    base_path = "/api/retail/v1"

    async def list_retail_sales_orders(self, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Lista pedidos de venda do varejo

        GET /retailSalesOrders; operationId=getRetailSalesOrders; availability inherited from API level

        Lista todos os pedidos de venda do faturamento (SC5) relacionados ao varejo.
        """
        return await self._request(
            "retail_sales_orders_v1.list_retail_sales_orders",
            "GET",
            "/retailSalesOrders",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_retail_sales_orders_by_internal_id_items(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Lista itens do pedido de venda do varejo

        GET /retailSalesOrders/{internalId}/items; operationId=getRetailSalesOrderItems; availability inherited from API level

        Exibe os detalhes dos itens do pedido de venda (SC6) para o pedido informado.
        """
        return await self._request(
            "retail_sales_orders_v1.list_retail_sales_orders_by_internal_id_items",
            "GET",
            "/retailSalesOrders/{internalId}/items",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
