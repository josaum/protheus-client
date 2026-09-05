"""Malha de Distribuição do MRP — generated from MRPTransportingLanes_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpTransportingLanesV1(ApiGroup):
    """Malha de Distribuição do MRP (/api/pcp/v1)."""

    api_id = "mrp_transporting_lanes_v1"
    base_path = "/api/pcp/v1"

    def list_mrptransportinglanes(self, *, branch_id: str | None = None, code: str | None = None, start_warehouse_group: str | None = None, branch_id_dest: str | None = None, end_warehouse_group: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de malhas de distribuição do MRP

        GET /mrptransportinglanes; operationId=getmrptransportinglanes; Protheus >= 12.1.27

        Retorna lista de malhas de distribuição do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.PagedMRPTransportingLanes
        """
        return self._request(
            "mrp_transporting_lanes_v1.list_mrptransportinglanes",
            "GET",
            "/mrptransportinglanes",
            path_params={},
            query={"branchId": branch_id, "code": code, "startWarehouseGroup": start_warehouse_group, "branchIdDest": branch_id_dest, "endWarehouseGroup": end_warehouse_group, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrptransportinglanes(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais malha de distribuição do MRP

        POST /mrptransportinglanes; operationId=postmrptransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.PagedMRPTransportingLanes
        Request model: protheus.models.mrp_transporting_lanes_v1.ListOfMRPTransportingLanes
        """
        return self._request(
            "mrp_transporting_lanes_v1.create_mrptransportinglanes",
            "POST",
            "/mrptransportinglanes",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrptransportinglanes(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais malhas de distribuição do MRP

        DELETE /mrptransportinglanes; operationId=deletemrptransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.MRPTransportingLanesMultiple
        Request model: protheus.models.mrp_transporting_lanes_v1.ListOfMRPTransportingLanes
        """
        return self._request(
            "mrp_transporting_lanes_v1.delete_mrptransportinglanes",
            "DELETE",
            "/mrptransportinglanes",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrptransportinglanes_by_branch_id_and_start_warehouse_group_and_end_warehouse_group(self, branch_id: str, start_warehouse_group: str, end_warehouse_group: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma malha de distribuição do MRP

        GET /mrptransportinglanes/{branchId}/{startWarehouseGroup}/{endWarehouseGroup}; operationId=gettransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.MRPTransportingLanes
        """
        return self._request(
            "mrp_transporting_lanes_v1.get_mrptransportinglanes_by_branch_id_and_start_warehouse_group_and_end_warehouse_group",
            "GET",
            "/mrptransportinglanes/{branchId}/{startWarehouseGroup}/{endWarehouseGroup}",
            path_params={"branchId": branch_id, "startWarehouseGroup": start_warehouse_group, "endWarehouseGroup": end_warehouse_group},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrptransportinglanes_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros da malha da distribuição do MRP

        POST /mrptransportinglanes/sync; operationId=synctransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.PagedMRPTransportingLanes
        Request model: protheus.models.mrp_transporting_lanes_v1.ListOfMRPTransportingLanes
        """
        return self._request(
            "mrp_transporting_lanes_v1.create_mrptransportinglanes_sync",
            "POST",
            "/mrptransportinglanes/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpTransportingLanesV1(AsyncApiGroup):
    """Malha de Distribuição do MRP (/api/pcp/v1)."""

    api_id = "mrp_transporting_lanes_v1"
    base_path = "/api/pcp/v1"

    async def list_mrptransportinglanes(self, *, branch_id: str | None = None, code: str | None = None, start_warehouse_group: str | None = None, branch_id_dest: str | None = None, end_warehouse_group: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de malhas de distribuição do MRP

        GET /mrptransportinglanes; operationId=getmrptransportinglanes; Protheus >= 12.1.27

        Retorna lista de malhas de distribuição do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.PagedMRPTransportingLanes
        """
        return await self._request(
            "mrp_transporting_lanes_v1.list_mrptransportinglanes",
            "GET",
            "/mrptransportinglanes",
            path_params={},
            query={"branchId": branch_id, "code": code, "startWarehouseGroup": start_warehouse_group, "branchIdDest": branch_id_dest, "endWarehouseGroup": end_warehouse_group, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrptransportinglanes(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais malha de distribuição do MRP

        POST /mrptransportinglanes; operationId=postmrptransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.PagedMRPTransportingLanes
        Request model: protheus.models.mrp_transporting_lanes_v1.ListOfMRPTransportingLanes
        """
        return await self._request(
            "mrp_transporting_lanes_v1.create_mrptransportinglanes",
            "POST",
            "/mrptransportinglanes",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrptransportinglanes(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais malhas de distribuição do MRP

        DELETE /mrptransportinglanes; operationId=deletemrptransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.MRPTransportingLanesMultiple
        Request model: protheus.models.mrp_transporting_lanes_v1.ListOfMRPTransportingLanes
        """
        return await self._request(
            "mrp_transporting_lanes_v1.delete_mrptransportinglanes",
            "DELETE",
            "/mrptransportinglanes",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrptransportinglanes_by_branch_id_and_start_warehouse_group_and_end_warehouse_group(self, branch_id: str, start_warehouse_group: str, end_warehouse_group: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma malha de distribuição do MRP

        GET /mrptransportinglanes/{branchId}/{startWarehouseGroup}/{endWarehouseGroup}; operationId=gettransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.MRPTransportingLanes
        """
        return await self._request(
            "mrp_transporting_lanes_v1.get_mrptransportinglanes_by_branch_id_and_start_warehouse_group_and_end_warehouse_group",
            "GET",
            "/mrptransportinglanes/{branchId}/{startWarehouseGroup}/{endWarehouseGroup}",
            path_params={"branchId": branch_id, "startWarehouseGroup": start_warehouse_group, "endWarehouseGroup": end_warehouse_group},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrptransportinglanes_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros da malha da distribuição do MRP

        POST /mrptransportinglanes/sync; operationId=synctransportinglanes; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_transporting_lanes_v1.PagedMRPTransportingLanes
        Request model: protheus.models.mrp_transporting_lanes_v1.ListOfMRPTransportingLanes
        """
        return await self._request(
            "mrp_transporting_lanes_v1.create_mrptransportinglanes_sync",
            "POST",
            "/mrptransportinglanes/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
