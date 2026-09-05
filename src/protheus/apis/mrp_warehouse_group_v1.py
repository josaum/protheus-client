"""Grupo de Armazém do MRP — generated from MRPWarehouseGroup_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpWarehouseGroupV1(ApiGroup):
    """Grupo de Armazém do MRP (/api/pcp/v1)."""

    api_id = "mrp_warehouse_group_v1"
    base_path = "/api/pcp/v1"

    def list_mrpwarehousegroup(self, *, branch_id: str | None = None, code: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de grupos de armazéns do MRP

        GET /mrpwarehousegroup; operationId=getmrpwarehousegroup; Protheus >= 12.1.27

        Retorna lista de grupos de armazéns do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.PagedMRPWarehouseGroup
        """
        return self._request(
            "mrp_warehouse_group_v1.list_mrpwarehousegroup",
            "GET",
            "/mrpwarehousegroup",
            path_params={},
            query={"branchId": branch_id, "code": code, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpwarehousegroup(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais grupo de armazém do MRP

        POST /mrpwarehousegroup; operationId=postmrpwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.PagedMRPWarehouseGroup
        Request model: protheus.models.mrp_warehouse_group_v1.ListOfMRPWarehouseGroup
        """
        return self._request(
            "mrp_warehouse_group_v1.create_mrpwarehousegroup",
            "POST",
            "/mrpwarehousegroup",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpwarehousegroup(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais grupo de armazém do MRP

        DELETE /mrpwarehousegroup; operationId=deletemrpwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.MRPWarehouseGroupMultiple
        Request model: protheus.models.mrp_warehouse_group_v1.ListOfMRPWarehouseGroup
        """
        return self._request(
            "mrp_warehouse_group_v1.delete_mrpwarehousegroup",
            "DELETE",
            "/mrpwarehousegroup",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpwarehousegroup_by_branch_id_and_warehouse_group(self, branch_id: str, warehouse_group: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um grupo de armazém do MRP

        GET /mrpwarehousegroup/{branchId}/{warehouseGroup}; operationId=getwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.MRPWarehouseGroup
        """
        return self._request(
            "mrp_warehouse_group_v1.get_mrpwarehousegroup_by_branch_id_and_warehouse_group",
            "GET",
            "/mrpwarehousegroup/{branchId}/{warehouseGroup}",
            path_params={"branchId": branch_id, "warehouseGroup": warehouse_group},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpwarehousegroup_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros do grupo de armazém do MRP

        POST /mrpwarehousegroup/sync; operationId=syncwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.PagedMRPWarehouseGroup
        Request model: protheus.models.mrp_warehouse_group_v1.ListOfMRPWarehouseGroup
        """
        return self._request(
            "mrp_warehouse_group_v1.create_mrpwarehousegroup_sync",
            "POST",
            "/mrpwarehousegroup/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpWarehouseGroupV1(AsyncApiGroup):
    """Grupo de Armazém do MRP (/api/pcp/v1)."""

    api_id = "mrp_warehouse_group_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpwarehousegroup(self, *, branch_id: str | None = None, code: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de grupos de armazéns do MRP

        GET /mrpwarehousegroup; operationId=getmrpwarehousegroup; Protheus >= 12.1.27

        Retorna lista de grupos de armazéns do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.PagedMRPWarehouseGroup
        """
        return await self._request(
            "mrp_warehouse_group_v1.list_mrpwarehousegroup",
            "GET",
            "/mrpwarehousegroup",
            path_params={},
            query={"branchId": branch_id, "code": code, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpwarehousegroup(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais grupo de armazém do MRP

        POST /mrpwarehousegroup; operationId=postmrpwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.PagedMRPWarehouseGroup
        Request model: protheus.models.mrp_warehouse_group_v1.ListOfMRPWarehouseGroup
        """
        return await self._request(
            "mrp_warehouse_group_v1.create_mrpwarehousegroup",
            "POST",
            "/mrpwarehousegroup",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpwarehousegroup(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais grupo de armazém do MRP

        DELETE /mrpwarehousegroup; operationId=deletemrpwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.MRPWarehouseGroupMultiple
        Request model: protheus.models.mrp_warehouse_group_v1.ListOfMRPWarehouseGroup
        """
        return await self._request(
            "mrp_warehouse_group_v1.delete_mrpwarehousegroup",
            "DELETE",
            "/mrpwarehousegroup",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpwarehousegroup_by_branch_id_and_warehouse_group(self, branch_id: str, warehouse_group: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um grupo de armazém do MRP

        GET /mrpwarehousegroup/{branchId}/{warehouseGroup}; operationId=getwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.MRPWarehouseGroup
        """
        return await self._request(
            "mrp_warehouse_group_v1.get_mrpwarehousegroup_by_branch_id_and_warehouse_group",
            "GET",
            "/mrpwarehousegroup/{branchId}/{warehouseGroup}",
            path_params={"branchId": branch_id, "warehouseGroup": warehouse_group},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpwarehousegroup_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros do grupo de armazém do MRP

        POST /mrpwarehousegroup/sync; operationId=syncwarehousegroup; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_group_v1.PagedMRPWarehouseGroup
        Request model: protheus.models.mrp_warehouse_group_v1.ListOfMRPWarehouseGroup
        """
        return await self._request(
            "mrp_warehouse_group_v1.create_mrpwarehousegroup_sync",
            "POST",
            "/mrpwarehousegroup/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
