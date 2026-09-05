"""Proposta Comercial — generated from CommercialProposal_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CommercialProposalV1(ApiGroup):
    """Proposta Comercial (/api/crm/v1)."""

    api_id = "commercial_proposal_v1"
    base_path = "/api/crm/v1"

    def list_opportunities_by_opportunity_id_commercialproposal(self, opportunity_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Propostas Comerciais relacionadas a uma Oportunidade de Venda

        GET /opportunities/{OpportunityId}/commercialproposal; operationId=getCommercialProposal; Protheus >= 12.1.21

        Retorna uma lista de Propostas Comerciais relacionadas a uma Oportunidade de Venda pelo OpportunityId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Order, Page, PageSize, Fields e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.PagedCommercialProposal
        """
        return self._request(
            "commercial_proposal_v1.list_opportunities_by_opportunity_id_commercialproposal",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal",
            path_params={"OpportunityId": opportunity_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_opportunities_by_opportunity_id_commercialproposal(self, opportunity_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Proposta Comercial

        POST /opportunities/{OpportunityId}/commercialproposal; operationId=postCommercialProposal; Protheus >= 12.1.21

        Inclui uma Proposta Comercial relacionada a uma Oportunidade de Venda pelo OpportunityId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        Request model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        """
        return self._request(
            "commercial_proposal_v1.create_opportunities_by_opportunity_id_commercialproposal",
            "POST",
            "/opportunities/{OpportunityId}/commercialproposal",
            path_params={"OpportunityId": opportunity_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_opportunities_by_opportunity_id_commercialproposal_by_internal_id(self, opportunity_id: str, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Proposta Comercial

        GET /opportunities/{OpportunityId}/commercialproposal/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna uma Proposta Comercial pelo InternalId relacionada a uma Oportunidade de Venda

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        """
        return self._request(
            "commercial_proposal_v1.get_opportunities_by_opportunity_id_commercialproposal_by_internal_id",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_opportunities_by_opportunity_id_commercialproposal_by_internal_id(self, opportunity_id: str, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Proposta Comercial

        PUT /opportunities/{OpportunityId}/commercialproposal/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Altera uma Proposta Comercial pelo InternalId relacionada a uma Oportunidade de Venda

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        Request model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        """
        return self._request(
            "commercial_proposal_v1.update_opportunities_by_opportunity_id_commercialproposal_by_internal_id",
            "PUT",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id(self, opportunity_id: str, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Proposta Comercial

        DELETE /opportunities/{OpportunityId}/commercialproposal/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui uma Proposta Comercial pelo InternalId relacionada a uma Oportunidade de Venda

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e OpportunityId
        """
        return self._request(
            "commercial_proposal_v1.delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id",
            "DELETE",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products(self, opportunity_id: str, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Itens relacionados a uma Proposta comercial

        GET /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts; operationId=getListofProducts; Protheus >= 12.1.21

        Retorna uma lista de Itens de uma Proposta Comercial relacionados pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Order, Page, PageSize, Fields, InternalId, e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.PagedListofProducts
        """
        return self._request(
            "commercial_proposal_v1.list_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products(self, opportunity_id: str, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item em uma Proposta Comercial

        POST /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts; operationId=postListofProducts; Protheus >= 12.1.21

        Inclui um item em uma Proposta Comercial relacionada a uma Oportunidade de Venda pelo OpportunityId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId, e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        Request model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        """
        return self._request(
            "commercial_proposal_v1.create_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products",
            "POST",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id(self, opportunity_id: str, internal_id: str, item_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Item de uma Proposta Comercial

        GET /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}; operationId=getItemId; Protheus >= 12.1.21

        Retorna um item de uma Proposta Comercial pelo ItemId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId, ItemId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        """
        return self._request(
            "commercial_proposal_v1.get_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id(self, opportunity_id: str, internal_id: str, item_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Item de uma Proposta Comercial

        PUT /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}; operationId=putItemId; Protheus >= 12.1.21

        Altera uma Proposta Comercial pelo ItemId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId, ItemId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        Request model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        """
        return self._request(
            "commercial_proposal_v1.update_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id",
            "PUT",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id(self, opportunity_id: str, internal_id: str, item_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Item de uma Proposta Comercial

        DELETE /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}; operationId=deleteItemId; Protheus >= 12.1.21

        Exclui uma Proposta Comercial pelo ItemId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId, ItemId e OpportunityId
        """
        return self._request(
            "commercial_proposal_v1.delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id",
            "DELETE",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id, "ItemId": item_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCommercialProposalV1(AsyncApiGroup):
    """Proposta Comercial (/api/crm/v1)."""

    api_id = "commercial_proposal_v1"
    base_path = "/api/crm/v1"

    async def list_opportunities_by_opportunity_id_commercialproposal(self, opportunity_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Propostas Comerciais relacionadas a uma Oportunidade de Venda

        GET /opportunities/{OpportunityId}/commercialproposal; operationId=getCommercialProposal; Protheus >= 12.1.21

        Retorna uma lista de Propostas Comerciais relacionadas a uma Oportunidade de Venda pelo OpportunityId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Order, Page, PageSize, Fields e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.PagedCommercialProposal
        """
        return await self._request(
            "commercial_proposal_v1.list_opportunities_by_opportunity_id_commercialproposal",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal",
            path_params={"OpportunityId": opportunity_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_opportunities_by_opportunity_id_commercialproposal(self, opportunity_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Proposta Comercial

        POST /opportunities/{OpportunityId}/commercialproposal; operationId=postCommercialProposal; Protheus >= 12.1.21

        Inclui uma Proposta Comercial relacionada a uma Oportunidade de Venda pelo OpportunityId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        Request model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        """
        return await self._request(
            "commercial_proposal_v1.create_opportunities_by_opportunity_id_commercialproposal",
            "POST",
            "/opportunities/{OpportunityId}/commercialproposal",
            path_params={"OpportunityId": opportunity_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_opportunities_by_opportunity_id_commercialproposal_by_internal_id(self, opportunity_id: str, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Proposta Comercial

        GET /opportunities/{OpportunityId}/commercialproposal/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna uma Proposta Comercial pelo InternalId relacionada a uma Oportunidade de Venda

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        """
        return await self._request(
            "commercial_proposal_v1.get_opportunities_by_opportunity_id_commercialproposal_by_internal_id",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_opportunities_by_opportunity_id_commercialproposal_by_internal_id(self, opportunity_id: str, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Proposta Comercial

        PUT /opportunities/{OpportunityId}/commercialproposal/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Altera uma Proposta Comercial pelo InternalId relacionada a uma Oportunidade de Venda

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        Request model: protheus.models.commercial_proposal_v1.CommercialProposalInfo
        """
        return await self._request(
            "commercial_proposal_v1.update_opportunities_by_opportunity_id_commercialproposal_by_internal_id",
            "PUT",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id(self, opportunity_id: str, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Proposta Comercial

        DELETE /opportunities/{OpportunityId}/commercialproposal/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui uma Proposta Comercial pelo InternalId relacionada a uma Oportunidade de Venda

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e OpportunityId
        """
        return await self._request(
            "commercial_proposal_v1.delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id",
            "DELETE",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products(self, opportunity_id: str, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Itens relacionados a uma Proposta comercial

        GET /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts; operationId=getListofProducts; Protheus >= 12.1.21

        Retorna uma lista de Itens de uma Proposta Comercial relacionados pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Order, Page, PageSize, Fields, InternalId, e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.PagedListofProducts
        """
        return await self._request(
            "commercial_proposal_v1.list_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products(self, opportunity_id: str, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item em uma Proposta Comercial

        POST /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts; operationId=postListofProducts; Protheus >= 12.1.21

        Inclui um item em uma Proposta Comercial relacionada a uma Oportunidade de Venda pelo OpportunityId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId, e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        Request model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        """
        return await self._request(
            "commercial_proposal_v1.create_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products",
            "POST",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id(self, opportunity_id: str, internal_id: str, item_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Item de uma Proposta Comercial

        GET /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}; operationId=getItemId; Protheus >= 12.1.21

        Retorna um item de uma Proposta Comercial pelo ItemId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId, ItemId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        """
        return await self._request(
            "commercial_proposal_v1.get_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id",
            "GET",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id(self, opportunity_id: str, internal_id: str, item_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Item de uma Proposta Comercial

        PUT /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}; operationId=putItemId; Protheus >= 12.1.21

        Altera uma Proposta Comercial pelo ItemId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId, ItemId e OpportunityId

        Response model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        Request model: protheus.models.commercial_proposal_v1.ListofProductsInfo
        """
        return await self._request(
            "commercial_proposal_v1.update_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id",
            "PUT",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id(self, opportunity_id: str, internal_id: str, item_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Item de uma Proposta Comercial

        DELETE /opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}; operationId=deleteItemId; Protheus >= 12.1.21

        Exclui uma Proposta Comercial pelo ItemId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId, ItemId e OpportunityId
        """
        return await self._request(
            "commercial_proposal_v1.delete_opportunities_by_opportunity_id_commercialproposal_by_internal_id_listof_products_by_item_id",
            "DELETE",
            "/opportunities/{OpportunityId}/commercialproposal/{InternalId}/ListofProducts/{ItemId}",
            path_params={"OpportunityId": opportunity_id, "InternalId": internal_id, "ItemId": item_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
