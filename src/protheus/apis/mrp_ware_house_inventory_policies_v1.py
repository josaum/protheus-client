"""Políticas de Estoque por Grupo de Armazém do MRP — generated from MRPWareHouseInventoryPolicies_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpWareHouseInventoryPoliciesV1(ApiGroup):
    """Políticas de Estoque por Grupo de Armazém do MRP (/api/pcp/v1)."""

    api_id = "mrp_ware_house_inventory_policies_v1"
    base_path = "/api/pcp/v1"

    def list_mrpwarehouseinventorypolicies(self, *, branch_id: str | None = None, product: str | None = None, warehouse_group: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de políticas de estoque por grupo de armazém do MRP

        GET /mrpwarehouseinventorypolicies; operationId=getmrpwarehouseinventorypolicies; Protheus >= 12.1.27

        Retorna lista de políticas de estoque por grupo de armazém do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.PagedMRPWareHouseInventoryPolicies
        """
        return self._request(
            "mrp_ware_house_inventory_policies_v1.list_mrpwarehouseinventorypolicies",
            "GET",
            "/mrpwarehouseinventorypolicies",
            path_params={},
            query={"branchId": branch_id, "product": product, "warehouseGroup": warehouse_group, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpwarehouseinventorypolicies(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza as políticas de estoque por grupo de armazém do MRP

        POST /mrpwarehouseinventorypolicies; operationId=postmrpwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.PagedMRPWareHouseInventoryPolicies
        Request model: protheus.models.mrp_ware_house_inventory_policies_v1.ListOfMRPWareHouseInventoryPolicies
        """
        return self._request(
            "mrp_ware_house_inventory_policies_v1.create_mrpwarehouseinventorypolicies",
            "POST",
            "/mrpwarehouseinventorypolicies",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpwarehouseinventorypolicies(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove as políticas de estoque por grupo de armazém do MRP

        DELETE /mrpwarehouseinventorypolicies; operationId=deletemrpwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.MRPWareHouseInventoryPoliciesMultiple
        Request model: protheus.models.mrp_ware_house_inventory_policies_v1.ListOfMRPWareHouseInventoryPolicies
        """
        return self._request(
            "mrp_ware_house_inventory_policies_v1.delete_mrpwarehouseinventorypolicies",
            "DELETE",
            "/mrpwarehouseinventorypolicies",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpwarehouseinventorypolicies_by_branch_id_and_product_and_warehouse_group(self, branch_id: str, product: str, warehouse_group: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a política de estoque por grupo de armazém do MRP

        GET /mrpwarehouseinventorypolicies/{branchId}/{product}/{warehouseGroup}; operationId=getwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.MRPWareHouseInventoryPolicies
        """
        return self._request(
            "mrp_ware_house_inventory_policies_v1.get_mrpwarehouseinventorypolicies_by_branch_id_and_product_and_warehouse_group",
            "GET",
            "/mrpwarehouseinventorypolicies/{branchId}/{product}/{warehouseGroup}",
            path_params={"branchId": branch_id, "product": product, "warehouseGroup": warehouse_group},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpwarehouseinventorypolicies_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros da política de estoque por grupo de armazém do MRP

        POST /mrpwarehouseinventorypolicies/sync; operationId=syncmrpwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.PagedMRPWareHouseInventoryPolicies
        Request model: protheus.models.mrp_ware_house_inventory_policies_v1.ListOfMRPWareHouseInventoryPolicies
        """
        return self._request(
            "mrp_ware_house_inventory_policies_v1.create_mrpwarehouseinventorypolicies_sync",
            "POST",
            "/mrpwarehouseinventorypolicies/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpWareHouseInventoryPoliciesV1(AsyncApiGroup):
    """Políticas de Estoque por Grupo de Armazém do MRP (/api/pcp/v1)."""

    api_id = "mrp_ware_house_inventory_policies_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpwarehouseinventorypolicies(self, *, branch_id: str | None = None, product: str | None = None, warehouse_group: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de políticas de estoque por grupo de armazém do MRP

        GET /mrpwarehouseinventorypolicies; operationId=getmrpwarehouseinventorypolicies; Protheus >= 12.1.27

        Retorna lista de políticas de estoque por grupo de armazém do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.PagedMRPWareHouseInventoryPolicies
        """
        return await self._request(
            "mrp_ware_house_inventory_policies_v1.list_mrpwarehouseinventorypolicies",
            "GET",
            "/mrpwarehouseinventorypolicies",
            path_params={},
            query={"branchId": branch_id, "product": product, "warehouseGroup": warehouse_group, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpwarehouseinventorypolicies(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza as políticas de estoque por grupo de armazém do MRP

        POST /mrpwarehouseinventorypolicies; operationId=postmrpwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.PagedMRPWareHouseInventoryPolicies
        Request model: protheus.models.mrp_ware_house_inventory_policies_v1.ListOfMRPWareHouseInventoryPolicies
        """
        return await self._request(
            "mrp_ware_house_inventory_policies_v1.create_mrpwarehouseinventorypolicies",
            "POST",
            "/mrpwarehouseinventorypolicies",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpwarehouseinventorypolicies(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove as políticas de estoque por grupo de armazém do MRP

        DELETE /mrpwarehouseinventorypolicies; operationId=deletemrpwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.MRPWareHouseInventoryPoliciesMultiple
        Request model: protheus.models.mrp_ware_house_inventory_policies_v1.ListOfMRPWareHouseInventoryPolicies
        """
        return await self._request(
            "mrp_ware_house_inventory_policies_v1.delete_mrpwarehouseinventorypolicies",
            "DELETE",
            "/mrpwarehouseinventorypolicies",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpwarehouseinventorypolicies_by_branch_id_and_product_and_warehouse_group(self, branch_id: str, product: str, warehouse_group: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a política de estoque por grupo de armazém do MRP

        GET /mrpwarehouseinventorypolicies/{branchId}/{product}/{warehouseGroup}; operationId=getwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.MRPWareHouseInventoryPolicies
        """
        return await self._request(
            "mrp_ware_house_inventory_policies_v1.get_mrpwarehouseinventorypolicies_by_branch_id_and_product_and_warehouse_group",
            "GET",
            "/mrpwarehouseinventorypolicies/{branchId}/{product}/{warehouseGroup}",
            path_params={"branchId": branch_id, "product": product, "warehouseGroup": warehouse_group},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpwarehouseinventorypolicies_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros da política de estoque por grupo de armazém do MRP

        POST /mrpwarehouseinventorypolicies/sync; operationId=syncmrpwarehouseinventorypolicies; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_ware_house_inventory_policies_v1.PagedMRPWareHouseInventoryPolicies
        Request model: protheus.models.mrp_ware_house_inventory_policies_v1.ListOfMRPWareHouseInventoryPolicies
        """
        return await self._request(
            "mrp_ware_house_inventory_policies_v1.create_mrpwarehouseinventorypolicies_sync",
            "POST",
            "/mrpwarehouseinventorypolicies/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
