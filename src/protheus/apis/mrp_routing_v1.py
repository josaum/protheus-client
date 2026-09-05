"""Roteiro Produtivo do MRP — generated from MRPRouting_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpRoutingV1(ApiGroup):
    """Roteiro Produtivo do MRP (/api/pcp/v1)."""

    api_id = "mrp_routing_v1"
    base_path = "/api/pcp/v1"

    def list_mrprouting(self, *, branch_id: str | None = None, product: str | None = None, routing: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de roteiros do MRP

        GET /mrprouting; operationId=getmrprouting; Protheus >= 12.1.27

        Retorna lista de roteiros do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.PagedMRPRouting
        """
        return self._request(
            "mrp_routing_v1.list_mrprouting",
            "GET",
            "/mrprouting",
            path_params={},
            query={"branchId": branch_id, "product": product, "routing": routing, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrprouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais roteiro do MRP

        POST /mrprouting; operationId=postmrprouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.PagedMRPRouting
        Request model: protheus.models.mrp_routing_v1.ListOfMRPRouting
        """
        return self._request(
            "mrp_routing_v1.create_mrprouting",
            "POST",
            "/mrprouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrprouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais roteiro do MRP

        DELETE /mrprouting; operationId=deletemrprouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.MRPRouting
        Request model: protheus.models.mrp_routing_v1.ListOfMRPRouting
        """
        return self._request(
            "mrp_routing_v1.delete_mrprouting",
            "DELETE",
            "/mrprouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrprouting_by_branch_id_and_product_and_routing(self, branch_id: str, product: str, routing: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um roteiro do MRP

        GET /mrprouting/{branchId}/{product}/{routing}; operationId=getrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.MRPRouting
        """
        return self._request(
            "mrp_routing_v1.get_mrprouting_by_branch_id_and_product_and_routing",
            "GET",
            "/mrprouting/{branchId}/{product}/{routing}",
            path_params={"branchId": branch_id, "product": product, "routing": routing},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrprouting_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros do roteiro de produção do MRP

        POST /mrprouting/sync; operationId=syncrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.PagedMRPRouting
        Request model: protheus.models.mrp_routing_v1.ListOfMRPRouting
        """
        return self._request(
            "mrp_routing_v1.create_mrprouting_sync",
            "POST",
            "/mrprouting/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpRoutingV1(AsyncApiGroup):
    """Roteiro Produtivo do MRP (/api/pcp/v1)."""

    api_id = "mrp_routing_v1"
    base_path = "/api/pcp/v1"

    async def list_mrprouting(self, *, branch_id: str | None = None, product: str | None = None, routing: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de roteiros do MRP

        GET /mrprouting; operationId=getmrprouting; Protheus >= 12.1.27

        Retorna lista de roteiros do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.PagedMRPRouting
        """
        return await self._request(
            "mrp_routing_v1.list_mrprouting",
            "GET",
            "/mrprouting",
            path_params={},
            query={"branchId": branch_id, "product": product, "routing": routing, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrprouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais roteiro do MRP

        POST /mrprouting; operationId=postmrprouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.PagedMRPRouting
        Request model: protheus.models.mrp_routing_v1.ListOfMRPRouting
        """
        return await self._request(
            "mrp_routing_v1.create_mrprouting",
            "POST",
            "/mrprouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrprouting(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais roteiro do MRP

        DELETE /mrprouting; operationId=deletemrprouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.MRPRouting
        Request model: protheus.models.mrp_routing_v1.ListOfMRPRouting
        """
        return await self._request(
            "mrp_routing_v1.delete_mrprouting",
            "DELETE",
            "/mrprouting",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrprouting_by_branch_id_and_product_and_routing(self, branch_id: str, product: str, routing: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um roteiro do MRP

        GET /mrprouting/{branchId}/{product}/{routing}; operationId=getrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.MRPRouting
        """
        return await self._request(
            "mrp_routing_v1.get_mrprouting_by_branch_id_and_product_and_routing",
            "GET",
            "/mrprouting/{branchId}/{product}/{routing}",
            path_params={"branchId": branch_id, "product": product, "routing": routing},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrprouting_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Sincroniza os registros do roteiro de produção do MRP

        POST /mrprouting/sync; operationId=syncrouting; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_routing_v1.PagedMRPRouting
        Request model: protheus.models.mrp_routing_v1.ListOfMRPRouting
        """
        return await self._request(
            "mrp_routing_v1.create_mrprouting_sync",
            "POST",
            "/mrprouting/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
