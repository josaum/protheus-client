"""Estrutura por Operação do MRP — generated from MRPBOMRouting_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpbomRoutingV1(ApiGroup):
    """Estrutura por Operação do MRP (/api/pcp/v1)."""

    api_id = "mrpbom_routing_v1"
    base_path = "/api/pcp/v1"

    def list_mrpbomrouting(self, *, branch_id: str | None = None, product: str | None = None, routing: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estrutura por operação do MRP

        GET /mrpbomrouting; operationId=getmrpbomrouting; Protheus >= 12.1.27

        Retorna lista de estrutura por operação do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.PagedMRPBOMRouting
        """
        return self._request(
            "mrpbom_routing_v1.list_mrpbomrouting",
            "GET",
            "/mrpbomrouting",
            path_params={},
            query={"branchId": branch_id, "product": product, "routing": routing, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpbomrouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais estrutura por operação do MRP

        POST /mrpbomrouting; operationId=postmrpbomrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.PagedMRPBOMRouting
        Request model: protheus.models.mrpbom_routing_v1.ListOfMRPBOMRouting
        """
        return self._request(
            "mrpbom_routing_v1.create_mrpbomrouting",
            "POST",
            "/mrpbomrouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpbomrouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais estruturas por operação do MRP

        DELETE /mrpbomrouting; operationId=deletemrpbomrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.MRPBOMRoutingMultiple
        Request model: protheus.models.mrpbom_routing_v1.ListOfMRPBOMRouting
        """
        return self._request(
            "mrpbom_routing_v1.delete_mrpbomrouting",
            "DELETE",
            "/mrpbomrouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpbomrouting_by_branch_id_and_product_and_routing_and_operation(self, branch_id: str, product: str, routing: str, operation: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a estrutura por operação do MRP

        GET /mrpbomrouting/{branchId}/{product}/{routing}/{operation}; operationId=getbomrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.MRPBOMRouting
        """
        return self._request(
            "mrpbom_routing_v1.get_mrpbomrouting_by_branch_id_and_product_and_routing_and_operation",
            "GET",
            "/mrpbomrouting/{branchId}/{product}/{routing}/{operation}",
            path_params={"branchId": branch_id, "product": product, "routing": routing, "operation": operation},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncMrpbomRoutingV1(AsyncApiGroup):
    """Estrutura por Operação do MRP (/api/pcp/v1)."""

    api_id = "mrpbom_routing_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpbomrouting(self, *, branch_id: str | None = None, product: str | None = None, routing: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de estrutura por operação do MRP

        GET /mrpbomrouting; operationId=getmrpbomrouting; Protheus >= 12.1.27

        Retorna lista de estrutura por operação do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.PagedMRPBOMRouting
        """
        return await self._request(
            "mrpbom_routing_v1.list_mrpbomrouting",
            "GET",
            "/mrpbomrouting",
            path_params={},
            query={"branchId": branch_id, "product": product, "routing": routing, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpbomrouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza uma ou mais estrutura por operação do MRP

        POST /mrpbomrouting; operationId=postmrpbomrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.PagedMRPBOMRouting
        Request model: protheus.models.mrpbom_routing_v1.ListOfMRPBOMRouting
        """
        return await self._request(
            "mrpbom_routing_v1.create_mrpbomrouting",
            "POST",
            "/mrpbomrouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpbomrouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove uma ou mais estruturas por operação do MRP

        DELETE /mrpbomrouting; operationId=deletemrpbomrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.MRPBOMRoutingMultiple
        Request model: protheus.models.mrpbom_routing_v1.ListOfMRPBOMRouting
        """
        return await self._request(
            "mrpbom_routing_v1.delete_mrpbomrouting",
            "DELETE",
            "/mrpbomrouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpbomrouting_by_branch_id_and_product_and_routing_and_operation(self, branch_id: str, product: str, routing: str, operation: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a estrutura por operação do MRP

        GET /mrpbomrouting/{branchId}/{product}/{routing}/{operation}; operationId=getbomrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrpbom_routing_v1.MRPBOMRouting
        """
        return await self._request(
            "mrpbom_routing_v1.get_mrpbomrouting_by_branch_id_and_product_and_routing_and_operation",
            "GET",
            "/mrpbomrouting/{branchId}/{product}/{routing}/{operation}",
            path_params={"branchId": branch_id, "product": product, "routing": routing, "operation": operation},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )
