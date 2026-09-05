"""Armazéns do MRP — generated from MRPWarehouse_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpWarehouseV1(ApiGroup):
    """Armazéns do MRP (/api/pcp/v1)."""

    api_id = "mrp_warehouse_v1"
    base_path = "/api/pcp/v1"

    def list_mrp_warehouse(self, *, branch_id: str | None = None, code: str | None = None, warehouse: str | None = None, type: str | None = None, use_mrp: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Armazéns do MRP

        GET /MRPWarehouse; operationId=getMRPWarehouse2; Protheus >= 12.1.27

        Retorna lista de Armazéns do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.PagedMRPWarehouse
        """
        return self._request(
            "mrp_warehouse_v1.list_mrp_warehouse",
            "GET",
            "/MRPWarehouse",
            path_params={},
            query={"branchId": branch_id, "code": code, "warehouse": warehouse, "type": type, "useMRP": use_mrp, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrp_warehouse(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros de Armazéns do MRP

        POST /MRPWarehouse; operationId=postwarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.PagedMRPWarehouse
        Request model: protheus.models.mrp_warehouse_v1.ListOfMRPWarehouse
        """
        return self._request(
            "mrp_warehouse_v1.create_mrp_warehouse",
            "POST",
            "/MRPWarehouse",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrp_warehouse(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais armazéns do MRP

        DELETE /MRPWarehouse; operationId=deleteMRPWarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.MRPWarehouseMultiple
        Request model: protheus.models.mrp_warehouse_v1.ListOfMRPWarehouse
        """
        return self._request(
            "mrp_warehouse_v1.delete_mrp_warehouse",
            "DELETE",
            "/MRPWarehouse",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrp_warehouse_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Armazém do MRP

        GET /MRPWarehouse/{branchId}/{code}; operationId=getMRPWarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.MRPWarehouseBase
        """
        return self._request(
            "mrp_warehouse_v1.get_mrp_warehouse_by_branch_id_and_code",
            "GET",
            "/MRPWarehouse/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrp_warehouse_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no Armazém do MRP

        POST /MRPWarehouse/sync; operationId=syncwarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.PagedMRPWarehouse
        Request model: protheus.models.mrp_warehouse_v1.ListOfMRPWarehouse
        """
        return self._request(
            "mrp_warehouse_v1.create_mrp_warehouse_sync",
            "POST",
            "/MRPWarehouse/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpWarehouseV1(AsyncApiGroup):
    """Armazéns do MRP (/api/pcp/v1)."""

    api_id = "mrp_warehouse_v1"
    base_path = "/api/pcp/v1"

    async def list_mrp_warehouse(self, *, branch_id: str | None = None, code: str | None = None, warehouse: str | None = None, type: str | None = None, use_mrp: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Armazéns do MRP

        GET /MRPWarehouse; operationId=getMRPWarehouse2; Protheus >= 12.1.27

        Retorna lista de Armazéns do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.PagedMRPWarehouse
        """
        return await self._request(
            "mrp_warehouse_v1.list_mrp_warehouse",
            "GET",
            "/MRPWarehouse",
            path_params={},
            query={"branchId": branch_id, "code": code, "warehouse": warehouse, "type": type, "useMRP": use_mrp, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrp_warehouse(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros de Armazéns do MRP

        POST /MRPWarehouse; operationId=postwarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.PagedMRPWarehouse
        Request model: protheus.models.mrp_warehouse_v1.ListOfMRPWarehouse
        """
        return await self._request(
            "mrp_warehouse_v1.create_mrp_warehouse",
            "POST",
            "/MRPWarehouse",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrp_warehouse(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais armazéns do MRP

        DELETE /MRPWarehouse; operationId=deleteMRPWarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.MRPWarehouseMultiple
        Request model: protheus.models.mrp_warehouse_v1.ListOfMRPWarehouse
        """
        return await self._request(
            "mrp_warehouse_v1.delete_mrp_warehouse",
            "DELETE",
            "/MRPWarehouse",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrp_warehouse_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Armazém do MRP

        GET /MRPWarehouse/{branchId}/{code}; operationId=getMRPWarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.MRPWarehouseBase
        """
        return await self._request(
            "mrp_warehouse_v1.get_mrp_warehouse_by_branch_id_and_code",
            "GET",
            "/MRPWarehouse/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrp_warehouse_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no Armazém do MRP

        POST /MRPWarehouse/sync; operationId=syncwarehouse; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_warehouse_v1.PagedMRPWarehouse
        Request model: protheus.models.mrp_warehouse_v1.ListOfMRPWarehouse
        """
        return await self._request(
            "mrp_warehouse_v1.create_mrp_warehouse_sync",
            "POST",
            "/MRPWarehouse/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
