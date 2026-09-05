"""Solicitação de Compra do MRP — generated from MRPPurchaseOrder_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpPurchaseOrderV1(ApiGroup):
    """Solicitação de Compra do MRP (/api/pcp/v1)."""

    api_id = "mrp_purchase_order_v1"
    base_path = "/api/pcp/v1"

    def list_mrppurchaseorder(self, *, branch_id: str | None = None, code: str | None = None, purchase: str | None = None, sequence: str | None = None, product: str | None = None, production_order: str | None = None, delivery_date: str | None = None, quantity: str | None = None, received_quantity: str | None = None, warehouse: str | None = None, type: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de solicitação de compra do MRP

        GET /mrppurchaseorder; operationId=getmrppurchaseorder2; Protheus >= 12.1.27

        Retorna lista de solicitação de compra do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.PagedMRPPurchaseOrder
        """
        return self._request(
            "mrp_purchase_order_v1.list_mrppurchaseorder",
            "GET",
            "/mrppurchaseorder",
            path_params={},
            query={"branchId": branch_id, "code": code, "purchase": purchase, "sequence": sequence, "product": product, "productionOrder": production_order, "deliveryDate": delivery_date, "quantity": quantity, "receivedQuantity": received_quantity, "warehouse": warehouse, "type": type, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrppurchaseorder(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros da solicitação de compra do MRP

        POST /mrppurchaseorder; operationId=postpurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.PagedMRPPurchaseOrder
        Request model: protheus.models.mrp_purchase_order_v1.ListOfMRPPurchaseOrder
        """
        return self._request(
            "mrp_purchase_order_v1.create_mrppurchaseorder",
            "POST",
            "/mrppurchaseorder",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrppurchaseorder(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Solicitação de compra do MRP

        DELETE /mrppurchaseorder; operationId=deletemrppurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.MRPPurchaseOrderMultiple
        Request model: protheus.models.mrp_purchase_order_v1.ListOfMRPPurchaseOrder
        """
        return self._request(
            "mrp_purchase_order_v1.delete_mrppurchaseorder",
            "DELETE",
            "/mrppurchaseorder",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrppurchaseorder_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a Solicitação de Compra do MRP

        GET /mrppurchaseorder/{branchId}/{code}; operationId=getmrppurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.MRPPurchaseOrderBase
        """
        return self._request(
            "mrp_purchase_order_v1.get_mrppurchaseorder_by_branch_id_and_code",
            "GET",
            "/mrppurchaseorder/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrppurchaseorder_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros da solicitação de compra do MRP

        POST /mrppurchaseorder/sync; operationId=syncpurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.PagedMRPPurchaseOrder
        Request model: protheus.models.mrp_purchase_order_v1.ListOfMRPPurchaseOrder
        """
        return self._request(
            "mrp_purchase_order_v1.create_mrppurchaseorder_sync",
            "POST",
            "/mrppurchaseorder/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpPurchaseOrderV1(AsyncApiGroup):
    """Solicitação de Compra do MRP (/api/pcp/v1)."""

    api_id = "mrp_purchase_order_v1"
    base_path = "/api/pcp/v1"

    async def list_mrppurchaseorder(self, *, branch_id: str | None = None, code: str | None = None, purchase: str | None = None, sequence: str | None = None, product: str | None = None, production_order: str | None = None, delivery_date: str | None = None, quantity: str | None = None, received_quantity: str | None = None, warehouse: str | None = None, type: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de solicitação de compra do MRP

        GET /mrppurchaseorder; operationId=getmrppurchaseorder2; Protheus >= 12.1.27

        Retorna lista de solicitação de compra do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.PagedMRPPurchaseOrder
        """
        return await self._request(
            "mrp_purchase_order_v1.list_mrppurchaseorder",
            "GET",
            "/mrppurchaseorder",
            path_params={},
            query={"branchId": branch_id, "code": code, "purchase": purchase, "sequence": sequence, "product": product, "productionOrder": production_order, "deliveryDate": delivery_date, "quantity": quantity, "receivedQuantity": received_quantity, "warehouse": warehouse, "type": type, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrppurchaseorder(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros da solicitação de compra do MRP

        POST /mrppurchaseorder; operationId=postpurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.PagedMRPPurchaseOrder
        Request model: protheus.models.mrp_purchase_order_v1.ListOfMRPPurchaseOrder
        """
        return await self._request(
            "mrp_purchase_order_v1.create_mrppurchaseorder",
            "POST",
            "/mrppurchaseorder",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrppurchaseorder(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Solicitação de compra do MRP

        DELETE /mrppurchaseorder; operationId=deletemrppurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.MRPPurchaseOrderMultiple
        Request model: protheus.models.mrp_purchase_order_v1.ListOfMRPPurchaseOrder
        """
        return await self._request(
            "mrp_purchase_order_v1.delete_mrppurchaseorder",
            "DELETE",
            "/mrppurchaseorder",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrppurchaseorder_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a Solicitação de Compra do MRP

        GET /mrppurchaseorder/{branchId}/{code}; operationId=getmrppurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.MRPPurchaseOrderBase
        """
        return await self._request(
            "mrp_purchase_order_v1.get_mrppurchaseorder_by_branch_id_and_code",
            "GET",
            "/mrppurchaseorder/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrppurchaseorder_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros da solicitação de compra do MRP

        POST /mrppurchaseorder/sync; operationId=syncpurchaseorder; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_order_v1.PagedMRPPurchaseOrder
        Request model: protheus.models.mrp_purchase_order_v1.ListOfMRPPurchaseOrder
        """
        return await self._request(
            "mrp_purchase_order_v1.create_mrppurchaseorder_sync",
            "POST",
            "/mrppurchaseorder/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
