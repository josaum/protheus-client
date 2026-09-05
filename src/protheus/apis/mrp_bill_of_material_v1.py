"""Estruturas do MRP — generated from MRPBillOfMaterial_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpBillOfMaterialV1(ApiGroup):
    """Estruturas do MRP (/api/pcp/v1)."""

    api_id = "mrp_bill_of_material_v1"
    base_path = "/api/pcp/v1"

    def list_mrpbillofmaterial(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, component: str | None = None, sequence: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estruturas do MRP

        GET /mrpbillofmaterial; operationId=getmrpbillofmaterial; Protheus >= 12.1.27

        Retorna lista de estrutura do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.PagedMRPBillOfMaterial
        """
        return self._request(
            "mrp_bill_of_material_v1.list_mrpbillofmaterial",
            "GET",
            "/mrpbillofmaterial",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "component": component, "sequence": sequence, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpbillofmaterial(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais estruturas do MRP

        POST /mrpbillofmaterial; operationId=postmrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.PagedMRPBillOfMaterial
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return self._request(
            "mrp_bill_of_material_v1.create_mrpbillofmaterial",
            "POST",
            "/mrpbillofmaterial",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpbillofmaterial(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais estruturas do MRP

        DELETE /mrpbillofmaterial; operationId=deletemrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterialMultiple
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return self._request(
            "mrp_bill_of_material_v1.delete_mrpbillofmaterial",
            "DELETE",
            "/mrpbillofmaterial",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpbillofmaterial_by_branch_id_and_product(self, branch_id: str, product: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma estrutura do MRP

        GET /mrpbillofmaterial/{branchId}/{product}; operationId=getbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterial
        """
        return self._request(
            "mrp_bill_of_material_v1.get_mrpbillofmaterial_by_branch_id_and_product",
            "GET",
            "/mrpbillofmaterial/{branchId}/{product}",
            path_params={"branchId": branch_id, "product": product},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpbillofmaterial_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza as estruturas do MRP

        POST /mrpbillofmaterial/sync; operationId=syncmrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.PagedMRPBillOfMaterial
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return self._request(
            "mrp_bill_of_material_v1.create_mrpbillofmaterial_sync",
            "POST",
            "/mrpbillofmaterial/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpbillofmaterial_component(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais componentes das estruturas do MRP

        DELETE /mrpbillofmaterial/component; operationId=deletecomponentmrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterialMultiple
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return self._request(
            "mrp_bill_of_material_v1.delete_mrpbillofmaterial_component",
            "DELETE",
            "/mrpbillofmaterial/component",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpbillofmaterial_alternative(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais alternativos dos componentes das estruturas do MRP

        DELETE /mrpbillofmaterial/alternative; operationId=deletealternativemrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterialMultiple
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return self._request(
            "mrp_bill_of_material_v1.delete_mrpbillofmaterial_alternative",
            "DELETE",
            "/mrpbillofmaterial/alternative",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpBillOfMaterialV1(AsyncApiGroup):
    """Estruturas do MRP (/api/pcp/v1)."""

    api_id = "mrp_bill_of_material_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpbillofmaterial(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, component: str | None = None, sequence: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estruturas do MRP

        GET /mrpbillofmaterial; operationId=getmrpbillofmaterial; Protheus >= 12.1.27

        Retorna lista de estrutura do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.PagedMRPBillOfMaterial
        """
        return await self._request(
            "mrp_bill_of_material_v1.list_mrpbillofmaterial",
            "GET",
            "/mrpbillofmaterial",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "component": component, "sequence": sequence, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpbillofmaterial(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais estruturas do MRP

        POST /mrpbillofmaterial; operationId=postmrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.PagedMRPBillOfMaterial
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return await self._request(
            "mrp_bill_of_material_v1.create_mrpbillofmaterial",
            "POST",
            "/mrpbillofmaterial",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpbillofmaterial(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais estruturas do MRP

        DELETE /mrpbillofmaterial; operationId=deletemrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterialMultiple
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return await self._request(
            "mrp_bill_of_material_v1.delete_mrpbillofmaterial",
            "DELETE",
            "/mrpbillofmaterial",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpbillofmaterial_by_branch_id_and_product(self, branch_id: str, product: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma estrutura do MRP

        GET /mrpbillofmaterial/{branchId}/{product}; operationId=getbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterial
        """
        return await self._request(
            "mrp_bill_of_material_v1.get_mrpbillofmaterial_by_branch_id_and_product",
            "GET",
            "/mrpbillofmaterial/{branchId}/{product}",
            path_params={"branchId": branch_id, "product": product},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpbillofmaterial_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza as estruturas do MRP

        POST /mrpbillofmaterial/sync; operationId=syncmrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.PagedMRPBillOfMaterial
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return await self._request(
            "mrp_bill_of_material_v1.create_mrpbillofmaterial_sync",
            "POST",
            "/mrpbillofmaterial/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpbillofmaterial_component(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais componentes das estruturas do MRP

        DELETE /mrpbillofmaterial/component; operationId=deletecomponentmrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterialMultiple
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return await self._request(
            "mrp_bill_of_material_v1.delete_mrpbillofmaterial_component",
            "DELETE",
            "/mrpbillofmaterial/component",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpbillofmaterial_alternative(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais alternativos dos componentes das estruturas do MRP

        DELETE /mrpbillofmaterial/alternative; operationId=deletealternativemrpbillofmaterial; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_bill_of_material_v1.MRPBillOfMaterialMultiple
        Request model: protheus.models.mrp_bill_of_material_v1.ListOfMRPBillOfMaterial
        """
        return await self._request(
            "mrp_bill_of_material_v1.delete_mrpbillofmaterial_alternative",
            "DELETE",
            "/mrpbillofmaterial/alternative",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
