"""Vendas do Varejo — generated from RetailSales_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RetailSalesV1(ApiGroup):
    """Vendas do Varejo (/api/retail/v1)."""

    api_id = "retail_sales_v1"
    base_path = "/api/retail/v1"

    def create_retail_sales_by_internal_id_cancelation(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Cancela venda passada na requisição

        POST /RetailSales/{InternalId}/Cancelation; operationId=postInternalId; Protheus >= 12.1.23

        Cancela uma venda de acordo com os valores do parametro InternalId ''Filial|número da venda|operador|número cancelamento SAT'' *envie o número cancelamento SAT caso exista

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e InternalId

        Response model: protheus.models.retail_sales_v1.RetailSalesCancellationType
        """
        return self._request(
            "retail_sales_v1.create_retail_sales_by_internal_id_cancelation",
            "POST",
            "/RetailSales/{InternalId}/Cancelation",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRetailSalesV1(AsyncApiGroup):
    """Vendas do Varejo (/api/retail/v1)."""

    api_id = "retail_sales_v1"
    base_path = "/api/retail/v1"

    async def create_retail_sales_by_internal_id_cancelation(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Cancela venda passada na requisição

        POST /RetailSales/{InternalId}/Cancelation; operationId=postInternalId; Protheus >= 12.1.23

        Cancela uma venda de acordo com os valores do parametro InternalId ''Filial|número da venda|operador|número cancelamento SAT'' *envie o número cancelamento SAT caso exista

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e InternalId

        Response model: protheus.models.retail_sales_v1.RetailSalesCancellationType
        """
        return await self._request(
            "retail_sales_v1.create_retail_sales_by_internal_id_cancelation",
            "POST",
            "/RetailSales/{InternalId}/Cancelation",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
