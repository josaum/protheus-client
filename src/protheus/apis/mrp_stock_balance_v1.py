"""Estoque do MRP — generated from MRPStockBalance_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpStockBalanceV1(ApiGroup):
    """Estoque do MRP (/api/pcp/v1)."""

    api_id = "mrp_stock_balance_v1"
    base_path = "/api/pcp/v1"

    def list_mrpstockbalance(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, warehouse: str | None = None, lot: str | None = None, sublot: str | None = None, expiration_date: str | None = None, available_quantity: str | None = None, consigned_out: str | None = None, consigned_in: str | None = None, unavailable_quantity: str | None = None, quality_control_balance: str | None = None, blocked_balance: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estoques do MRP

        GET /mrpstockbalance; operationId=getmrpstockbalance2; Protheus >= 12.1.27

        Retorna lista de estoques do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.PagedMRPStockBalance
        """
        return self._request(
            "mrp_stock_balance_v1.list_mrpstockbalance",
            "GET",
            "/mrpstockbalance",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "warehouse": warehouse, "lot": lot, "sublot": sublot, "expirationDate": expiration_date, "availableQuantity": available_quantity, "consignedOut": consigned_out, "consignedIn": consigned_in, "unavailableQuantity": unavailable_quantity, "qualityControlBalance": quality_control_balance, "blockedBalance": blocked_balance, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpstockbalance(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no estoque do MRP

        POST /mrpstockbalance; operationId=poststockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.PagedMRPStockBalance
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalance
        """
        return self._request(
            "mrp_stock_balance_v1.create_mrpstockbalance",
            "POST",
            "/mrpstockbalance",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpstockbalance(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais saldo em Estoque do MRP

        DELETE /mrpstockbalance; operationId=deletemrpstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.MRPStockBalanceMultiple
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalance
        """
        return self._request(
            "mrp_stock_balance_v1.delete_mrpstockbalance",
            "DELETE",
            "/mrpstockbalance",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpstockbalance_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Estoque do MRP

        GET /mrpstockbalance/{branchId}/{code}; operationId=getmrpstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.MRPStockBalanceBase
        """
        return self._request(
            "mrp_stock_balance_v1.get_mrpstockbalance_by_branch_id_and_code",
            "GET",
            "/mrpstockbalance/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def delete_mrpstockbalance_clear_product(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Zera os saldos de um ou mais produtos em um determinado armazém

        DELETE /mrpstockbalance/clearProduct; operationId=clearmrpstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.MRPStockBalanceMultipleClear
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalanceClear
        """
        return self._request(
            "mrp_stock_balance_v1.delete_mrpstockbalance_clear_product",
            "DELETE",
            "/mrpstockbalance/clearProduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def create_mrpstockbalance_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros no estoque do MRP

        POST /mrpstockbalance/sync; operationId=syncstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.PagedMRPStockBalance
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalance
        """
        return self._request(
            "mrp_stock_balance_v1.create_mrpstockbalance_sync",
            "POST",
            "/mrpstockbalance/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpStockBalanceV1(AsyncApiGroup):
    """Estoque do MRP (/api/pcp/v1)."""

    api_id = "mrp_stock_balance_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpstockbalance(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, warehouse: str | None = None, lot: str | None = None, sublot: str | None = None, expiration_date: str | None = None, available_quantity: str | None = None, consigned_out: str | None = None, consigned_in: str | None = None, unavailable_quantity: str | None = None, quality_control_balance: str | None = None, blocked_balance: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estoques do MRP

        GET /mrpstockbalance; operationId=getmrpstockbalance2; Protheus >= 12.1.27

        Retorna lista de estoques do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.PagedMRPStockBalance
        """
        return await self._request(
            "mrp_stock_balance_v1.list_mrpstockbalance",
            "GET",
            "/mrpstockbalance",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "warehouse": warehouse, "lot": lot, "sublot": sublot, "expirationDate": expiration_date, "availableQuantity": available_quantity, "consignedOut": consigned_out, "consignedIn": consigned_in, "unavailableQuantity": unavailable_quantity, "qualityControlBalance": quality_control_balance, "blockedBalance": blocked_balance, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpstockbalance(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no estoque do MRP

        POST /mrpstockbalance; operationId=poststockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.PagedMRPStockBalance
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalance
        """
        return await self._request(
            "mrp_stock_balance_v1.create_mrpstockbalance",
            "POST",
            "/mrpstockbalance",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpstockbalance(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais saldo em Estoque do MRP

        DELETE /mrpstockbalance; operationId=deletemrpstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.MRPStockBalanceMultiple
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalance
        """
        return await self._request(
            "mrp_stock_balance_v1.delete_mrpstockbalance",
            "DELETE",
            "/mrpstockbalance",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpstockbalance_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Estoque do MRP

        GET /mrpstockbalance/{branchId}/{code}; operationId=getmrpstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.MRPStockBalanceBase
        """
        return await self._request(
            "mrp_stock_balance_v1.get_mrpstockbalance_by_branch_id_and_code",
            "GET",
            "/mrpstockbalance/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def delete_mrpstockbalance_clear_product(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Zera os saldos de um ou mais produtos em um determinado armazém

        DELETE /mrpstockbalance/clearProduct; operationId=clearmrpstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.MRPStockBalanceMultipleClear
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalanceClear
        """
        return await self._request(
            "mrp_stock_balance_v1.delete_mrpstockbalance_clear_product",
            "DELETE",
            "/mrpstockbalance/clearProduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def create_mrpstockbalance_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza registros no estoque do MRP

        POST /mrpstockbalance/sync; operationId=syncstockbalance; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_stock_balance_v1.PagedMRPStockBalance
        Request model: protheus.models.mrp_stock_balance_v1.ListOfMRPStockBalance
        """
        return await self._request(
            "mrp_stock_balance_v1.create_mrpstockbalance_sync",
            "POST",
            "/mrpstockbalance/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
