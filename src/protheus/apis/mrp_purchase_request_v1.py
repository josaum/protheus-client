"""Pedido de Compra do MRP — generated from MRPPurchaseRequest_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpPurchaseRequestV1(ApiGroup):
    """Pedido de Compra do MRP (/api/pcp/v1)."""

    api_id = "mrp_purchase_request_v1"
    base_path = "/api/pcp/v1"

    def list_mrppurchaserequest(self, *, branch_id: str | None = None, code: str | None = None, request: str | None = None, sequence: str | None = None, product: str | None = None, production_order: str | None = None, delivery_date: str | None = None, quantity: str | None = None, received_quantity: str | None = None, warehouse: str | None = None, type: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de pedidos de compra do MRP

        GET /mrppurchaserequest; operationId=getmrppurchaserequest2; Protheus >= 12.1.27

        Retorna lista de pedidos de compra do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.PagedMRPPurchaseRequest
        """
        return self._request(
            "mrp_purchase_request_v1.list_mrppurchaserequest",
            "GET",
            "/mrppurchaserequest",
            path_params={},
            query={"branchId": branch_id, "code": code, "request": request, "sequence": sequence, "product": product, "productionOrder": production_order, "deliveryDate": delivery_date, "quantity": quantity, "receivedQuantity": received_quantity, "warehouse": warehouse, "type": type, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrppurchaserequest(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros do pedido de compra do MRP

        POST /mrppurchaserequest; operationId=postpurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.PagedMRPPurchaseRequest
        Request model: protheus.models.mrp_purchase_request_v1.ListOfMRPPurchaseRequest
        """
        return self._request(
            "mrp_purchase_request_v1.create_mrppurchaserequest",
            "POST",
            "/mrppurchaserequest",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrppurchaserequest(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais Pedido de compra do MRP

        DELETE /mrppurchaserequest; operationId=deletemrppurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.MRPPurchaseRequestMultiple
        Request model: protheus.models.mrp_purchase_request_v1.ListOfMRPPurchaseRequest
        """
        return self._request(
            "mrp_purchase_request_v1.delete_mrppurchaserequest",
            "DELETE",
            "/mrppurchaserequest",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrppurchaserequest_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Pedido de Compra do MRP

        GET /mrppurchaserequest/{branchId}/{code}; operationId=getmrppurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.MRPPurchaseRequestBase
        """
        return self._request(
            "mrp_purchase_request_v1.get_mrppurchaserequest_by_branch_id_and_code",
            "GET",
            "/mrppurchaserequest/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrppurchaserequest_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros do pedido de compra do MRP

        POST /mrppurchaserequest/sync; operationId=syncpurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.PagedMRPPurchaseRequest
        Request model: protheus.models.mrp_purchase_request_v1.ListOfMRPPurchaseRequest
        """
        return self._request(
            "mrp_purchase_request_v1.create_mrppurchaserequest_sync",
            "POST",
            "/mrppurchaserequest/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpPurchaseRequestV1(AsyncApiGroup):
    """Pedido de Compra do MRP (/api/pcp/v1)."""

    api_id = "mrp_purchase_request_v1"
    base_path = "/api/pcp/v1"

    async def list_mrppurchaserequest(self, *, branch_id: str | None = None, code: str | None = None, request: str | None = None, sequence: str | None = None, product: str | None = None, production_order: str | None = None, delivery_date: str | None = None, quantity: str | None = None, received_quantity: str | None = None, warehouse: str | None = None, type: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de pedidos de compra do MRP

        GET /mrppurchaserequest; operationId=getmrppurchaserequest2; Protheus >= 12.1.27

        Retorna lista de pedidos de compra do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.PagedMRPPurchaseRequest
        """
        return await self._request(
            "mrp_purchase_request_v1.list_mrppurchaserequest",
            "GET",
            "/mrppurchaserequest",
            path_params={},
            query={"branchId": branch_id, "code": code, "request": request, "sequence": sequence, "product": product, "productionOrder": production_order, "deliveryDate": delivery_date, "quantity": quantity, "receivedQuantity": received_quantity, "warehouse": warehouse, "type": type, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrppurchaserequest(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros do pedido de compra do MRP

        POST /mrppurchaserequest; operationId=postpurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.PagedMRPPurchaseRequest
        Request model: protheus.models.mrp_purchase_request_v1.ListOfMRPPurchaseRequest
        """
        return await self._request(
            "mrp_purchase_request_v1.create_mrppurchaserequest",
            "POST",
            "/mrppurchaserequest",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrppurchaserequest(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais Pedido de compra do MRP

        DELETE /mrppurchaserequest; operationId=deletemrppurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.MRPPurchaseRequestMultiple
        Request model: protheus.models.mrp_purchase_request_v1.ListOfMRPPurchaseRequest
        """
        return await self._request(
            "mrp_purchase_request_v1.delete_mrppurchaserequest",
            "DELETE",
            "/mrppurchaserequest",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrppurchaserequest_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Pedido de Compra do MRP

        GET /mrppurchaserequest/{branchId}/{code}; operationId=getmrppurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.MRPPurchaseRequestBase
        """
        return await self._request(
            "mrp_purchase_request_v1.get_mrppurchaserequest_by_branch_id_and_code",
            "GET",
            "/mrppurchaserequest/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrppurchaserequest_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros do pedido de compra do MRP

        POST /mrppurchaserequest/sync; operationId=syncpurchaserequest; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_purchase_request_v1.PagedMRPPurchaseRequest
        Request model: protheus.models.mrp_purchase_request_v1.ListOfMRPPurchaseRequest
        """
        return await self._request(
            "mrp_purchase_request_v1.create_mrppurchaserequest_sync",
            "POST",
            "/mrppurchaserequest/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
