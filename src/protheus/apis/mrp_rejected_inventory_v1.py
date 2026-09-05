"""Estoque Rejeitado do MRP — generated from MRPRejectedInventory_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpRejectedInventoryV1(ApiGroup):
    """Estoque Rejeitado do MRP (/api/pcp/v1)."""

    api_id = "mrp_rejected_inventory_v1"
    base_path = "/api/pcp/v1"

    def list_mrprejectedinventory(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, warehouse: str | None = None, invoice_date: str | None = None, quantity: str | None = None, returned_quantity: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estoques rejeitados do MRP

        GET /mrprejectedinventory; operationId=getmrprejectedinventory; Protheus >= 12.1.27

        Retorna lista de estoques rejeitados do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.PagedMRPRejectedInventory
        """
        return self._request(
            "mrp_rejected_inventory_v1.list_mrprejectedinventory",
            "GET",
            "/mrprejectedinventory",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "warehouse": warehouse, "invoiceDate": invoice_date, "quantity": quantity, "returnedQuantity": returned_quantity, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrprejectedinventory(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no estoque rejeitado do MRP

        POST /mrprejectedinventory; operationId=postrejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.PagedMRPRejectedInventory
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventory
        """
        return self._request(
            "mrp_rejected_inventory_v1.create_mrprejectedinventory",
            "POST",
            "/mrprejectedinventory",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrprejectedinventory(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais saldo rejeitado em Estoque do MRP

        DELETE /mrprejectedinventory; operationId=deletemrprejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.MRPRejectedInventoryMultiple
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventory
        """
        return self._request(
            "mrp_rejected_inventory_v1.delete_mrprejectedinventory",
            "DELETE",
            "/mrprejectedinventory",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrprejectedinventory_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Estoque Rejeitado do MRP

        GET /mrprejectedinventory/{branchId}/{code}; operationId=getmrprejectedinventory1; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.MRPRejectedInventoryBase
        """
        return self._request(
            "mrp_rejected_inventory_v1.get_mrprejectedinventory_by_branch_id_and_code",
            "GET",
            "/mrprejectedinventory/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def delete_mrprejectedinventory_clear_product(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Zera os saldos de um ou mais produtos em um determinado armazém

        DELETE /mrprejectedinventory/clearProduct; operationId=clearmrprejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.MRPRejectedInventoryMultipleClear
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventoryClear
        """
        return self._request(
            "mrp_rejected_inventory_v1.delete_mrprejectedinventory_clear_product",
            "DELETE",
            "/mrprejectedinventory/clearProduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def create_mrprejectedinventory_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros do estoque rejeitado do MRP

        POST /mrprejectedinventory/sync; operationId=syncmrprejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.PagedMRPRejectedInventory
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventory
        """
        return self._request(
            "mrp_rejected_inventory_v1.create_mrprejectedinventory_sync",
            "POST",
            "/mrprejectedinventory/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpRejectedInventoryV1(AsyncApiGroup):
    """Estoque Rejeitado do MRP (/api/pcp/v1)."""

    api_id = "mrp_rejected_inventory_v1"
    base_path = "/api/pcp/v1"

    async def list_mrprejectedinventory(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, warehouse: str | None = None, invoice_date: str | None = None, quantity: str | None = None, returned_quantity: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estoques rejeitados do MRP

        GET /mrprejectedinventory; operationId=getmrprejectedinventory; Protheus >= 12.1.27

        Retorna lista de estoques rejeitados do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.PagedMRPRejectedInventory
        """
        return await self._request(
            "mrp_rejected_inventory_v1.list_mrprejectedinventory",
            "GET",
            "/mrprejectedinventory",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "warehouse": warehouse, "invoiceDate": invoice_date, "quantity": quantity, "returnedQuantity": returned_quantity, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrprejectedinventory(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no estoque rejeitado do MRP

        POST /mrprejectedinventory; operationId=postrejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.PagedMRPRejectedInventory
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventory
        """
        return await self._request(
            "mrp_rejected_inventory_v1.create_mrprejectedinventory",
            "POST",
            "/mrprejectedinventory",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrprejectedinventory(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais saldo rejeitado em Estoque do MRP

        DELETE /mrprejectedinventory; operationId=deletemrprejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.MRPRejectedInventoryMultiple
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventory
        """
        return await self._request(
            "mrp_rejected_inventory_v1.delete_mrprejectedinventory",
            "DELETE",
            "/mrprejectedinventory",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrprejectedinventory_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Estoque Rejeitado do MRP

        GET /mrprejectedinventory/{branchId}/{code}; operationId=getmrprejectedinventory1; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.MRPRejectedInventoryBase
        """
        return await self._request(
            "mrp_rejected_inventory_v1.get_mrprejectedinventory_by_branch_id_and_code",
            "GET",
            "/mrprejectedinventory/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def delete_mrprejectedinventory_clear_product(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Zera os saldos de um ou mais produtos em um determinado armazém

        DELETE /mrprejectedinventory/clearProduct; operationId=clearmrprejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.MRPRejectedInventoryMultipleClear
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventoryClear
        """
        return await self._request(
            "mrp_rejected_inventory_v1.delete_mrprejectedinventory_clear_product",
            "DELETE",
            "/mrprejectedinventory/clearProduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def create_mrprejectedinventory_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros do estoque rejeitado do MRP

        POST /mrprejectedinventory/sync; operationId=syncmrprejectedinventory; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_rejected_inventory_v1.PagedMRPRejectedInventory
        Request model: protheus.models.mrp_rejected_inventory_v1.ListOfMRPRejectedInventory
        """
        return await self._request(
            "mrp_rejected_inventory_v1.create_mrprejectedinventory_sync",
            "POST",
            "/mrprejectedinventory/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
