"""Ordens de produção do MRP — generated from MRPProductionOrders_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpProductionOrdersV1(ApiGroup):
    """Ordens de produção do MRP (/api/pcp/v1)."""

    api_id = "mrp_production_orders_v1"
    base_path = "/api/pcp/v1"

    def list_mrpproductionorders(self, *, branch_id: str | None = None, production_order: str | None = None, code: str | None = None, delivery_date: str | None = None, start_date: str | None = None, product: str | None = None, warehouse: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de ordens de produção do MRP

        GET /mrpproductionorders; operationId=getmrpproductionorders; Protheus >= 12.1.27

        Retorna lista de ordens de produção do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.PagedMRPProductionOrders
        """
        return self._request(
            "mrp_production_orders_v1.list_mrpproductionorders",
            "GET",
            "/mrpproductionorders",
            path_params={},
            query={"branchId": branch_id, "productionOrder": production_order, "code": code, "deliveryDate": delivery_date, "startDate": start_date, "product": product, "warehouse": warehouse, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproductionorders(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais ordens de produção do MRP

        POST /mrpproductionorders; operationId=postproductionorders; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.PagedMRPProductionOrders
        Request model: protheus.models.mrp_production_orders_v1.ListOfMRPProductionOrders
        """
        return self._request(
            "mrp_production_orders_v1.create_mrpproductionorders",
            "POST",
            "/mrpproductionorders",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpproductionorders(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Ordens de produção do MRP

        DELETE /mrpproductionorders; operationId=deletemrpproductionorders; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.MRPProductionOrdersMultiple
        Request model: protheus.models.mrp_production_orders_v1.ListOfMRPProductionOrders
        """
        return self._request(
            "mrp_production_orders_v1.delete_mrpproductionorders",
            "DELETE",
            "/mrpproductionorders",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpproductionorders_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma ordem de produção do MRP

        GET /mrpproductionorders/{branchId}/{code}; operationId=getproductionorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.MRPProductionOrderBase
        """
        return self._request(
            "mrp_production_orders_v1.get_mrpproductionorders_by_branch_id_and_code",
            "GET",
            "/mrpproductionorders/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproductionorders_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza as ordens de produção do MRP

        POST /mrpproductionorders/sync; operationId=syncproductionorders; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.PagedMRPProductionOrders
        Request model: protheus.models.mrp_production_orders_v1.ListOfMRPProductionOrders
        """
        return self._request(
            "mrp_production_orders_v1.create_mrpproductionorders_sync",
            "POST",
            "/mrpproductionorders/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpProductionOrdersV1(AsyncApiGroup):
    """Ordens de produção do MRP (/api/pcp/v1)."""

    api_id = "mrp_production_orders_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpproductionorders(self, *, branch_id: str | None = None, production_order: str | None = None, code: str | None = None, delivery_date: str | None = None, start_date: str | None = None, product: str | None = None, warehouse: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de ordens de produção do MRP

        GET /mrpproductionorders; operationId=getmrpproductionorders; Protheus >= 12.1.27

        Retorna lista de ordens de produção do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.PagedMRPProductionOrders
        """
        return await self._request(
            "mrp_production_orders_v1.list_mrpproductionorders",
            "GET",
            "/mrpproductionorders",
            path_params={},
            query={"branchId": branch_id, "productionOrder": production_order, "code": code, "deliveryDate": delivery_date, "startDate": start_date, "product": product, "warehouse": warehouse, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproductionorders(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais ordens de produção do MRP

        POST /mrpproductionorders; operationId=postproductionorders; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.PagedMRPProductionOrders
        Request model: protheus.models.mrp_production_orders_v1.ListOfMRPProductionOrders
        """
        return await self._request(
            "mrp_production_orders_v1.create_mrpproductionorders",
            "POST",
            "/mrpproductionorders",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpproductionorders(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Ordens de produção do MRP

        DELETE /mrpproductionorders; operationId=deletemrpproductionorders; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.MRPProductionOrdersMultiple
        Request model: protheus.models.mrp_production_orders_v1.ListOfMRPProductionOrders
        """
        return await self._request(
            "mrp_production_orders_v1.delete_mrpproductionorders",
            "DELETE",
            "/mrpproductionorders",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpproductionorders_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma ordem de produção do MRP

        GET /mrpproductionorders/{branchId}/{code}; operationId=getproductionorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.MRPProductionOrderBase
        """
        return await self._request(
            "mrp_production_orders_v1.get_mrpproductionorders_by_branch_id_and_code",
            "GET",
            "/mrpproductionorders/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproductionorders_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza as ordens de produção do MRP

        POST /mrpproductionorders/sync; operationId=syncproductionorders; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_production_orders_v1.PagedMRPProductionOrders
        Request model: protheus.models.mrp_production_orders_v1.ListOfMRPProductionOrders
        """
        return await self._request(
            "mrp_production_orders_v1.create_mrpproductionorders_sync",
            "POST",
            "/mrpproductionorders/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
