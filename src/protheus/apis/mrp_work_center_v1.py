"""Centro de trabalho do MRP — generated from MRPWorkCenter_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpWorkCenterV1(ApiGroup):
    """Centro de trabalho do MRP (/api/pcp/v1)."""

    api_id = "mrp_work_center_v1"
    base_path = "/api/pcp/v1"

    def list_mrpworkcenter(self, *, branch_id: str | None = None, workcenter: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de centros de trabalho do MRP

        GET /mrpworkcenter; operationId=getmrpworkcenter; Protheus >= 12.1.27

        Retorna lista de centros de trabalho do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.PagedMRPWorkCenter
        """
        return self._request(
            "mrp_work_center_v1.list_mrpworkcenter",
            "GET",
            "/mrpworkcenter",
            path_params={},
            query={"branchId": branch_id, "workcenter": workcenter, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpworkcenter(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais centro do trabalho do MRP

        POST /mrpworkcenter; operationId=postmrpworkcenter; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.PagedMRPWorkCenter
        Request model: protheus.models.mrp_work_center_v1.ListOfMRPWorkCenter
        """
        return self._request(
            "mrp_work_center_v1.create_mrpworkcenter",
            "POST",
            "/mrpworkcenter",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpworkcenter(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais centros de trabalho do MRP

        DELETE /mrpworkcenter; operationId=deletemrpworkcenter; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.MRPWorkCenterMultiple
        Request model: protheus.models.mrp_work_center_v1.ListOfMRPWorkCenter
        """
        return self._request(
            "mrp_work_center_v1.delete_mrpworkcenter",
            "DELETE",
            "/mrpworkcenter",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpworkcenter_by_branch_id_and_workcenter(self, branch_id: str, workcenter: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um centro de trabalho do MRP

        GET /mrpworkcenter/{branchId}/{workcenter}; operationId=getworkcenter; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.MRPWorkCenter
        """
        return self._request(
            "mrp_work_center_v1.get_mrpworkcenter_by_branch_id_and_workcenter",
            "GET",
            "/mrpworkcenter/{branchId}/{workcenter}",
            path_params={"branchId": branch_id, "workcenter": workcenter},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncMrpWorkCenterV1(AsyncApiGroup):
    """Centro de trabalho do MRP (/api/pcp/v1)."""

    api_id = "mrp_work_center_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpworkcenter(self, *, branch_id: str | None = None, workcenter: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de centros de trabalho do MRP

        GET /mrpworkcenter; operationId=getmrpworkcenter; Protheus >= 12.1.27

        Retorna lista de centros de trabalho do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.PagedMRPWorkCenter
        """
        return await self._request(
            "mrp_work_center_v1.list_mrpworkcenter",
            "GET",
            "/mrpworkcenter",
            path_params={},
            query={"branchId": branch_id, "workcenter": workcenter, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpworkcenter(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais centro do trabalho do MRP

        POST /mrpworkcenter; operationId=postmrpworkcenter; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.PagedMRPWorkCenter
        Request model: protheus.models.mrp_work_center_v1.ListOfMRPWorkCenter
        """
        return await self._request(
            "mrp_work_center_v1.create_mrpworkcenter",
            "POST",
            "/mrpworkcenter",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpworkcenter(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais centros de trabalho do MRP

        DELETE /mrpworkcenter; operationId=deletemrpworkcenter; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.MRPWorkCenterMultiple
        Request model: protheus.models.mrp_work_center_v1.ListOfMRPWorkCenter
        """
        return await self._request(
            "mrp_work_center_v1.delete_mrpworkcenter",
            "DELETE",
            "/mrpworkcenter",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpworkcenter_by_branch_id_and_workcenter(self, branch_id: str, workcenter: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um centro de trabalho do MRP

        GET /mrpworkcenter/{branchId}/{workcenter}; operationId=getworkcenter; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_work_center_v1.MRPWorkCenter
        """
        return await self._request(
            "mrp_work_center_v1.get_mrpworkcenter_by_branch_id_and_workcenter",
            "GET",
            "/mrpworkcenter/{branchId}/{workcenter}",
            path_params={"branchId": branch_id, "workcenter": workcenter},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )
