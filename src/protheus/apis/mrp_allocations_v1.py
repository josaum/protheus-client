"""Empenhos da Produção MRP — generated from MRPAllocations_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpAllocationsV1(ApiGroup):
    """Empenhos da Produção MRP (/api/pcp/v1)."""

    api_id = "mrp_allocations_v1"
    base_path = "/api/pcp/v1"

    def list_mrpallocations(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, production_order: str | None = None, production_order_orig: str | None = None, allocation_date: str | None = None, sequence: str | None = None, quantity: str | None = None, suspended_quantity: str | None = None, warehouse: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de empenhos da produção MRP

        GET /mrpallocations; operationId=getmrpallocations2; Protheus >= 12.1.27

        Retorna lista de empenhos da produção MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.PagedMRPAllocations
        """
        return self._request(
            "mrp_allocations_v1.list_mrpallocations",
            "GET",
            "/mrpallocations",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "productionOrder": production_order, "productionOrderOrig": production_order_orig, "allocationDate": allocation_date, "sequence": sequence, "quantity": quantity, "suspendedQuantity": suspended_quantity, "warehouse": warehouse, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpallocations(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros de empenho da produção MRP

        POST /mrpallocations; operationId=postallocations; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        Request model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        """
        return self._request(
            "mrp_allocations_v1.create_mrpallocations",
            "POST",
            "/mrpallocations",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpallocations(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais Empenho da ordem de produção do MRP

        DELETE /mrpallocations; operationId=deletemrpallocations; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.MRPAllocationsMultiple
        Request model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        """
        return self._request(
            "mrp_allocations_v1.delete_mrpallocations",
            "DELETE",
            "/mrpallocations",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpallocations_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Empenho da Ordem de Produção do MRP

        GET /mrpallocations/{branchId}/{code}; operationId=getmrpallocations; Protheus >= 12.1.27

        Retorna um Empenho da Ordem de Produção MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.MRPAllocationsBase
        """
        return self._request(
            "mrp_allocations_v1.get_mrpallocations_by_branch_id_and_code",
            "GET",
            "/mrpallocations/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpallocations_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros de empenho da produção MRP

        POST /mrpallocations/sync; operationId=syncallocations; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        Request model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        """
        return self._request(
            "mrp_allocations_v1.create_mrpallocations_sync",
            "POST",
            "/mrpallocations/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpAllocationsV1(AsyncApiGroup):
    """Empenhos da Produção MRP (/api/pcp/v1)."""

    api_id = "mrp_allocations_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpallocations(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, production_order: str | None = None, production_order_orig: str | None = None, allocation_date: str | None = None, sequence: str | None = None, quantity: str | None = None, suspended_quantity: str | None = None, warehouse: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de empenhos da produção MRP

        GET /mrpallocations; operationId=getmrpallocations2; Protheus >= 12.1.27

        Retorna lista de empenhos da produção MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.PagedMRPAllocations
        """
        return await self._request(
            "mrp_allocations_v1.list_mrpallocations",
            "GET",
            "/mrpallocations",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "productionOrder": production_order, "productionOrderOrig": production_order_orig, "allocationDate": allocation_date, "sequence": sequence, "quantity": quantity, "suspendedQuantity": suspended_quantity, "warehouse": warehouse, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpallocations(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros de empenho da produção MRP

        POST /mrpallocations; operationId=postallocations; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        Request model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        """
        return await self._request(
            "mrp_allocations_v1.create_mrpallocations",
            "POST",
            "/mrpallocations",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpallocations(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais Empenho da ordem de produção do MRP

        DELETE /mrpallocations; operationId=deletemrpallocations; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.MRPAllocationsMultiple
        Request model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        """
        return await self._request(
            "mrp_allocations_v1.delete_mrpallocations",
            "DELETE",
            "/mrpallocations",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpallocations_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Empenho da Ordem de Produção do MRP

        GET /mrpallocations/{branchId}/{code}; operationId=getmrpallocations; Protheus >= 12.1.27

        Retorna um Empenho da Ordem de Produção MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.MRPAllocationsBase
        """
        return await self._request(
            "mrp_allocations_v1.get_mrpallocations_by_branch_id_and_code",
            "GET",
            "/mrpallocations/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpallocations_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros de empenho da produção MRP

        POST /mrpallocations/sync; operationId=syncallocations; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        Request model: protheus.models.mrp_allocations_v1.ListOfMRPAllocations
        """
        return await self._request(
            "mrp_allocations_v1.create_mrpallocations_sync",
            "POST",
            "/mrpallocations/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
