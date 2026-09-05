"""Versão da Produção MRP — generated from MrpProdVersion_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpProdVersionV1(ApiGroup):
    """Versão da Produção MRP (/api/pcp/v1)."""

    api_id = "mrp_prod_version_v1"
    base_path = "/api/pcp/v1"

    def list_mrpproductionversion(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, start_date: str | None = None, end_date: str | None = None, start_quantity: str | None = None, end_quantity: str | None = None, revision: str | None = None, routing: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de versão da produção MRP

        GET /mrpproductionversion; operationId=getmrpprodversion; Protheus >= 12.1.27

        Retorna lista de versões da produção MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.PagedMRPProdVersion
        """
        return self._request(
            "mrp_prod_version_v1.list_mrpproductionversion",
            "GET",
            "/mrpproductionversion",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "startDate": start_date, "endDate": end_date, "startQuantity": start_quantity, "endQuantity": end_quantity, "revision": revision, "routing": routing, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproductionversion(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros de versão da produção MRP

        POST /mrpproductionversion; operationId=postprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        Request model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        """
        return self._request(
            "mrp_prod_version_v1.create_mrpproductionversion",
            "POST",
            "/mrpproductionversion",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpproductionversion(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Versões da produção MRP

        DELETE /mrpproductionversion; operationId=deletemrpprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.MRPProdVersionMultiple
        Request model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        """
        return self._request(
            "mrp_prod_version_v1.delete_mrpproductionversion",
            "DELETE",
            "/mrpproductionversion",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpproductionversion_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Versão da Produção MRP

        GET /mrpproductionversion/{branchId}/{code}; operationId=getprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.MRPProdVersionBase
        """
        return self._request(
            "mrp_prod_version_v1.get_mrpproductionversion_by_branch_id_and_code",
            "GET",
            "/mrpproductionversion/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpproductionversion_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros da versão da produção MRP

        POST /mrpproductionversion/sync; operationId=syncprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        Request model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        """
        return self._request(
            "mrp_prod_version_v1.create_mrpproductionversion_sync",
            "POST",
            "/mrpproductionversion/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpProdVersionV1(AsyncApiGroup):
    """Versão da Produção MRP (/api/pcp/v1)."""

    api_id = "mrp_prod_version_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpproductionversion(self, *, branch_id: str | None = None, code: str | None = None, product: str | None = None, start_date: str | None = None, end_date: str | None = None, start_quantity: str | None = None, end_quantity: str | None = None, revision: str | None = None, routing: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de versão da produção MRP

        GET /mrpproductionversion; operationId=getmrpprodversion; Protheus >= 12.1.27

        Retorna lista de versões da produção MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.PagedMRPProdVersion
        """
        return await self._request(
            "mrp_prod_version_v1.list_mrpproductionversion",
            "GET",
            "/mrpproductionversion",
            path_params={},
            query={"branchId": branch_id, "code": code, "product": product, "startDate": start_date, "endDate": end_date, "startQuantity": start_quantity, "endQuantity": end_quantity, "revision": revision, "routing": routing, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproductionversion(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros de versão da produção MRP

        POST /mrpproductionversion; operationId=postprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        Request model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        """
        return await self._request(
            "mrp_prod_version_v1.create_mrpproductionversion",
            "POST",
            "/mrpproductionversion",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpproductionversion(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais Versões da produção MRP

        DELETE /mrpproductionversion; operationId=deletemrpprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.MRPProdVersionMultiple
        Request model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        """
        return await self._request(
            "mrp_prod_version_v1.delete_mrpproductionversion",
            "DELETE",
            "/mrpproductionversion",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpproductionversion_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Versão da Produção MRP

        GET /mrpproductionversion/{branchId}/{code}; operationId=getprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.MRPProdVersionBase
        """
        return await self._request(
            "mrp_prod_version_v1.get_mrpproductionversion_by_branch_id_and_code",
            "GET",
            "/mrpproductionversion/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpproductionversion_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros da versão da produção MRP

        POST /mrpproductionversion/sync; operationId=syncprodversion; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        Request model: protheus.models.mrp_prod_version_v1.ListOfMRPProdVersion
        """
        return await self._request(
            "mrp_prod_version_v1.create_mrpproductionversion_sync",
            "POST",
            "/mrpproductionversion/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
