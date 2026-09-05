"""Impostos do Pedido de Venda — generated from SalesTaxes_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SalesTaxesV1(ApiGroup):
    """Impostos do Pedido de Venda (/api/fat/v1)."""

    api_id = "sales_taxes_v1"
    base_path = "/api/fat/v1"

    def get_sales_taxes_by_sales_order_id(self, sales_order_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar os Valores e Tributos de um Pedido de Venda

        GET /SalesTaxes/{SalesOrderId}; operationId=getSalesOrderId; Protheus >= 12.1.23

        Retorna uma lista com os Valores e Tributos de um Pedido de Venda gravado

        TOTVS note: Este verbo esta disponível com os parâmetros SalesOrderId e Authorization

        Response model: protheus.models.sales_taxes_v1.ReturnSalesTaxes
        """
        return self._request(
            "sales_taxes_v1.get_sales_taxes_by_sales_order_id",
            "GET",
            "/SalesTaxes/{SalesOrderId}",
            path_params={"SalesOrderId": sales_order_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_sales_taxes(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar os Valores e Tributos de uma Simulação de Pedido de Venda

        POST /SalesTaxes; operationId=postSalesTaxes

        Retorna uma lista com os Valores e Tributos de uma Simulação de Pedido de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields.

        Response model: protheus.models.sales_taxes_v1.ReturnSalesTaxes
        Request model: protheus.models.sales_taxes_v1.SalesOrderInfo
        """
        return self._request(
            "sales_taxes_v1.create_sales_taxes",
            "POST",
            "/SalesTaxes",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncSalesTaxesV1(AsyncApiGroup):
    """Impostos do Pedido de Venda (/api/fat/v1)."""

    api_id = "sales_taxes_v1"
    base_path = "/api/fat/v1"

    async def get_sales_taxes_by_sales_order_id(self, sales_order_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar os Valores e Tributos de um Pedido de Venda

        GET /SalesTaxes/{SalesOrderId}; operationId=getSalesOrderId; Protheus >= 12.1.23

        Retorna uma lista com os Valores e Tributos de um Pedido de Venda gravado

        TOTVS note: Este verbo esta disponível com os parâmetros SalesOrderId e Authorization

        Response model: protheus.models.sales_taxes_v1.ReturnSalesTaxes
        """
        return await self._request(
            "sales_taxes_v1.get_sales_taxes_by_sales_order_id",
            "GET",
            "/SalesTaxes/{SalesOrderId}",
            path_params={"SalesOrderId": sales_order_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_sales_taxes(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar os Valores e Tributos de uma Simulação de Pedido de Venda

        POST /SalesTaxes; operationId=postSalesTaxes

        Retorna uma lista com os Valores e Tributos de uma Simulação de Pedido de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields.

        Response model: protheus.models.sales_taxes_v1.ReturnSalesTaxes
        Request model: protheus.models.sales_taxes_v1.SalesOrderInfo
        """
        return await self._request(
            "sales_taxes_v1.create_sales_taxes",
            "POST",
            "/SalesTaxes",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )
