"""Demandas do MRP — generated from MRPDemands_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpDemandsV1(ApiGroup):
    """Demandas do MRP (/api/pcp/v1)."""

    api_id = "mrp_demands_v1"
    base_path = "/api/pcp/v1"

    def list_mrpdemands(self, *, branch_id: str | None = None, code: str | None = None, date: str | None = None, product: str | None = None, warehouse: str | None = None, revision: str | None = None, document: str | None = None, source: str | None = None, processed: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de demandas do MRP

        GET /mrpdemands; operationId=getmrpdemands; Protheus >= 12.1.27

        Retorna lista de demandas do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.PagedMRPDemands
        """
        return self._request(
            "mrp_demands_v1.list_mrpdemands",
            "GET",
            "/mrpdemands",
            path_params={},
            query={"branchId": branch_id, "code": code, "date": date, "product": product, "warehouse": warehouse, "revision": revision, "document": document, "source": source, "processed": processed, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpdemands(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais demandas do MRP

        POST /mrpdemands; operationId=postdemands; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.PagedMRPDemands
        Request model: protheus.models.mrp_demands_v1.ListOfMRPDemand
        """
        return self._request(
            "mrp_demands_v1.create_mrpdemands",
            "POST",
            "/mrpdemands",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpdemands(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Demandas do MRP

        DELETE /mrpdemands; operationId=deletemrpdemands; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.MRPDemandMultiple
        Request model: protheus.models.mrp_demands_v1.ListOfMRPDemand
        """
        return self._request(
            "mrp_demands_v1.delete_mrpdemands",
            "DELETE",
            "/mrpdemands",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpdemands_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma demanda do MRP

        GET /mrpdemands/{branchId}/{code}; operationId=getDemand; Protheus >= 12.1.27

        Retorna uma Demanda do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.MRPDemandBase
        """
        return self._request(
            "mrp_demands_v1.get_mrpdemands_by_branch_id_and_code",
            "GET",
            "/mrpdemands/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpdemands_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros de demandas do MRP

        POST /mrpdemands/sync; operationId=syncDemand; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.PagedMRPDemands
        Request model: protheus.models.mrp_demands_v1.ListOfMRPDemand
        """
        return self._request(
            "mrp_demands_v1.create_mrpdemands_sync",
            "POST",
            "/mrpdemands/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpDemandsV1(AsyncApiGroup):
    """Demandas do MRP (/api/pcp/v1)."""

    api_id = "mrp_demands_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpdemands(self, *, branch_id: str | None = None, code: str | None = None, date: str | None = None, product: str | None = None, warehouse: str | None = None, revision: str | None = None, document: str | None = None, source: str | None = None, processed: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de demandas do MRP

        GET /mrpdemands; operationId=getmrpdemands; Protheus >= 12.1.27

        Retorna lista de demandas do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.PagedMRPDemands
        """
        return await self._request(
            "mrp_demands_v1.list_mrpdemands",
            "GET",
            "/mrpdemands",
            path_params={},
            query={"branchId": branch_id, "code": code, "date": date, "product": product, "warehouse": warehouse, "revision": revision, "document": document, "source": source, "processed": processed, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpdemands(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais demandas do MRP

        POST /mrpdemands; operationId=postdemands; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.PagedMRPDemands
        Request model: protheus.models.mrp_demands_v1.ListOfMRPDemand
        """
        return await self._request(
            "mrp_demands_v1.create_mrpdemands",
            "POST",
            "/mrpdemands",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpdemands(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Demandas do MRP

        DELETE /mrpdemands; operationId=deletemrpdemands; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.MRPDemandMultiple
        Request model: protheus.models.mrp_demands_v1.ListOfMRPDemand
        """
        return await self._request(
            "mrp_demands_v1.delete_mrpdemands",
            "DELETE",
            "/mrpdemands",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpdemands_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma demanda do MRP

        GET /mrpdemands/{branchId}/{code}; operationId=getDemand; Protheus >= 12.1.27

        Retorna uma Demanda do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.MRPDemandBase
        """
        return await self._request(
            "mrp_demands_v1.get_mrpdemands_by_branch_id_and_code",
            "GET",
            "/mrpdemands/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpdemands_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros de demandas do MRP

        POST /mrpdemands/sync; operationId=syncDemand; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_demands_v1.PagedMRPDemands
        Request model: protheus.models.mrp_demands_v1.ListOfMRPDemand
        """
        return await self._request(
            "mrp_demands_v1.create_mrpdemands_sync",
            "POST",
            "/mrpdemands/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
