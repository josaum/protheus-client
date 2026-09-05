"""Produto do MRP — generated from MRPProduct_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpProductV1(ApiGroup):
    """Produto do MRP (/api/pcp/v1)."""

    api_id = "mrp_product_v1"
    base_path = "/api/pcp/v1"

    def list_mrpproduct(self, *, branch_id: str | None = None, product: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de produtos do MRP

        GET /mrpproduct; operationId=getmrpproduct; Protheus >= 12.1.28

        Retorna lista de produtos do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.PagedMRPProduct
        """
        return self._request(
            "mrp_product_v1.list_mrpproduct",
            "GET",
            "/mrpproduct",
            path_params={},
            query={"branchId": branch_id, "product": product, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproduct(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais produto do MRP

        POST /mrpproduct; operationId=postmrpproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.PagedMRPProduct
        Request model: protheus.models.mrp_product_v1.ListOfMRPProduct
        """
        return self._request(
            "mrp_product_v1.create_mrpproduct",
            "POST",
            "/mrpproduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpproduct(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais produtos do MRP

        DELETE /mrpproduct; operationId=deletemrpproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.MRPProductMultiple
        Request model: protheus.models.mrp_product_v1.ListOfMRPProduct
        """
        return self._request(
            "mrp_product_v1.delete_mrpproduct",
            "DELETE",
            "/mrpproduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpproduct_by_branch_id_and_product(self, branch_id: str, product: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um produto do MRP

        GET /mrpproduct/{branchId}/{product}; operationId=getproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.MRPProduct
        """
        return self._request(
            "mrp_product_v1.get_mrpproduct_by_branch_id_and_product",
            "GET",
            "/mrpproduct/{branchId}/{product}",
            path_params={"branchId": branch_id, "product": product},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproduct_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros do produto do MRP

        POST /mrpproduct/sync; operationId=syncproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.PagedMRPProduct
        Request model: protheus.models.mrp_product_v1.ListOfMRPProduct
        """
        return self._request(
            "mrp_product_v1.create_mrpproduct_sync",
            "POST",
            "/mrpproduct/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpProductV1(AsyncApiGroup):
    """Produto do MRP (/api/pcp/v1)."""

    api_id = "mrp_product_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpproduct(self, *, branch_id: str | None = None, product: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de produtos do MRP

        GET /mrpproduct; operationId=getmrpproduct; Protheus >= 12.1.28

        Retorna lista de produtos do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.PagedMRPProduct
        """
        return await self._request(
            "mrp_product_v1.list_mrpproduct",
            "GET",
            "/mrpproduct",
            path_params={},
            query={"branchId": branch_id, "product": product, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproduct(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais produto do MRP

        POST /mrpproduct; operationId=postmrpproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.PagedMRPProduct
        Request model: protheus.models.mrp_product_v1.ListOfMRPProduct
        """
        return await self._request(
            "mrp_product_v1.create_mrpproduct",
            "POST",
            "/mrpproduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpproduct(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais produtos do MRP

        DELETE /mrpproduct; operationId=deletemrpproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.MRPProductMultiple
        Request model: protheus.models.mrp_product_v1.ListOfMRPProduct
        """
        return await self._request(
            "mrp_product_v1.delete_mrpproduct",
            "DELETE",
            "/mrpproduct",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpproduct_by_branch_id_and_product(self, branch_id: str, product: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um produto do MRP

        GET /mrpproduct/{branchId}/{product}; operationId=getproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.MRPProduct
        """
        return await self._request(
            "mrp_product_v1.get_mrpproduct_by_branch_id_and_product",
            "GET",
            "/mrpproduct/{branchId}/{product}",
            path_params={"branchId": branch_id, "product": product},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproduct_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros do produto do MRP

        POST /mrpproduct/sync; operationId=syncproduct; Protheus >= 12.1.28

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_product_v1.PagedMRPProduct
        Request model: protheus.models.mrp_product_v1.ListOfMRPProduct
        """
        return await self._request(
            "mrp_product_v1.create_mrpproduct_sync",
            "POST",
            "/mrpproduct/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
