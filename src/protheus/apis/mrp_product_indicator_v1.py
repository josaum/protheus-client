"""Indicadores do Produto do MRP — generated from MRPProductIndicator_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpProductIndicatorV1(ApiGroup):
    """Indicadores do Produto do MRP (/api/pcp/v1)."""

    api_id = "mrp_product_indicator_v1"
    base_path = "/api/pcp/v1"

    def list_mrpproductindicator(self, *, branch_id: str | None = None, product: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de indicadores do produto do MRP

        GET /mrpproductindicator; operationId=getmrpproductindicator; Protheus >= 12.1.27

        Retorna lista de indicadores do produto do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.PagedMRPProductIndicator
        """
        return self._request(
            "mrp_product_indicator_v1.list_mrpproductindicator",
            "GET",
            "/mrpproductindicator",
            path_params={},
            query={"branchId": branch_id, "product": product, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproductindicator(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza indicadores do produto do MRP

        POST /mrpproductindicator; operationId=postmrpproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.PagedMRPProductIndicator
        Request model: protheus.models.mrp_product_indicator_v1.ListOfMRPProductIndicator
        """
        return self._request(
            "mrp_product_indicator_v1.create_mrpproductindicator",
            "POST",
            "/mrpproductindicator",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpproductindicator(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove os indicadores dos produtos do MRP

        DELETE /mrpproductindicator; operationId=deletemrpproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.MRPProductIndicatorMultiple
        Request model: protheus.models.mrp_product_indicator_v1.ListOfMRPProductIndicator
        """
        return self._request(
            "mrp_product_indicator_v1.delete_mrpproductindicator",
            "DELETE",
            "/mrpproductindicator",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpproductindicator_by_branch_id_and_product(self, branch_id: str, product: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os indicadores do produto do MRP

        GET /mrpproductindicator/{branchId}/{product}; operationId=getproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.MRPProductIndicator
        """
        return self._request(
            "mrp_product_indicator_v1.get_mrpproductindicator_by_branch_id_and_product",
            "GET",
            "/mrpproductindicator/{branchId}/{product}",
            path_params={"branchId": branch_id, "product": product},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproductindicator_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros dos indicadores do produto do MRP

        POST /mrpproductindicator/sync; operationId=syncproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.PagedMRPProductIndicator
        Request model: protheus.models.mrp_product_indicator_v1.ListOfMRPProductIndicator
        """
        return self._request(
            "mrp_product_indicator_v1.create_mrpproductindicator_sync",
            "POST",
            "/mrpproductindicator/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpProductIndicatorV1(AsyncApiGroup):
    """Indicadores do Produto do MRP (/api/pcp/v1)."""

    api_id = "mrp_product_indicator_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpproductindicator(self, *, branch_id: str | None = None, product: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de indicadores do produto do MRP

        GET /mrpproductindicator; operationId=getmrpproductindicator; Protheus >= 12.1.27

        Retorna lista de indicadores do produto do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.PagedMRPProductIndicator
        """
        return await self._request(
            "mrp_product_indicator_v1.list_mrpproductindicator",
            "GET",
            "/mrpproductindicator",
            path_params={},
            query={"branchId": branch_id, "product": product, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproductindicator(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza indicadores do produto do MRP

        POST /mrpproductindicator; operationId=postmrpproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.PagedMRPProductIndicator
        Request model: protheus.models.mrp_product_indicator_v1.ListOfMRPProductIndicator
        """
        return await self._request(
            "mrp_product_indicator_v1.create_mrpproductindicator",
            "POST",
            "/mrpproductindicator",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpproductindicator(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove os indicadores dos produtos do MRP

        DELETE /mrpproductindicator; operationId=deletemrpproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.MRPProductIndicatorMultiple
        Request model: protheus.models.mrp_product_indicator_v1.ListOfMRPProductIndicator
        """
        return await self._request(
            "mrp_product_indicator_v1.delete_mrpproductindicator",
            "DELETE",
            "/mrpproductindicator",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpproductindicator_by_branch_id_and_product(self, branch_id: str, product: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os indicadores do produto do MRP

        GET /mrpproductindicator/{branchId}/{product}; operationId=getproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.MRPProductIndicator
        """
        return await self._request(
            "mrp_product_indicator_v1.get_mrpproductindicator_by_branch_id_and_product",
            "GET",
            "/mrpproductindicator/{branchId}/{product}",
            path_params={"branchId": branch_id, "product": product},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproductindicator_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros dos indicadores do produto do MRP

        POST /mrpproductindicator/sync; operationId=syncproductindicator; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_indicator_v1.PagedMRPProductIndicator
        Request model: protheus.models.mrp_product_indicator_v1.ListOfMRPProductIndicator
        """
        return await self._request(
            "mrp_product_indicator_v1.create_mrpproductindicator_sync",
            "POST",
            "/mrpproductindicator/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
