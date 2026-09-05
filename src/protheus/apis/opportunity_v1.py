"""Oportunidades — generated from Opportunity_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class OpportunityV1(ApiGroup):
    """Oportunidades (/api/crm/v1)."""

    api_id = "opportunity_v1"
    base_path = "/api/crm/v1"

    def list_opportunities(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de oportunidades de venda

        GET /opportunities; operationId=getOpportunity; Protheus >= 12.1.21

        Retorna lista completa das oportunidades de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.opportunity_v1.PagedOpportunity
        """
        return self._request(
            "opportunity_v1.list_opportunities",
            "GET",
            "/opportunities",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_opportunities(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Oportunidade de Venda

        POST /opportunities; operationId=postOpportunity; Protheus >= 12.1.21

        Inclui uma oportunidade de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.opportunity_v1.PagedOpportunity
        Request model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return self._request(
            "opportunity_v1.create_opportunities",
            "POST",
            "/opportunities",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_opportunities_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a Oportunidade de Venda pelo Código

        GET /opportunities/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a oportunidade de venda pelo código

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return self._request(
            "opportunity_v1.get_opportunities_by_internal_id",
            "GET",
            "/opportunities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_opportunities_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma oportunidade de venda

        PUT /opportunities/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a oportunidade de venda conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.opportunity_v1.OpportunityInfo
        Request model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return self._request(
            "opportunity_v1.update_opportunities_by_internal_id",
            "PUT",
            "/opportunities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_opportunities_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui uma oportunidade de venda

        DELETE /opportunities/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui a oportunidade de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return self._request(
            "opportunity_v1.delete_opportunities_by_internal_id",
            "DELETE",
            "/opportunities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncOpportunityV1(AsyncApiGroup):
    """Oportunidades (/api/crm/v1)."""

    api_id = "opportunity_v1"
    base_path = "/api/crm/v1"

    async def list_opportunities(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de oportunidades de venda

        GET /opportunities; operationId=getOpportunity; Protheus >= 12.1.21

        Retorna lista completa das oportunidades de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.opportunity_v1.PagedOpportunity
        """
        return await self._request(
            "opportunity_v1.list_opportunities",
            "GET",
            "/opportunities",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_opportunities(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Oportunidade de Venda

        POST /opportunities; operationId=postOpportunity; Protheus >= 12.1.21

        Inclui uma oportunidade de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.opportunity_v1.PagedOpportunity
        Request model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return await self._request(
            "opportunity_v1.create_opportunities",
            "POST",
            "/opportunities",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_opportunities_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a Oportunidade de Venda pelo Código

        GET /opportunities/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a oportunidade de venda pelo código

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return await self._request(
            "opportunity_v1.get_opportunities_by_internal_id",
            "GET",
            "/opportunities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_opportunities_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma oportunidade de venda

        PUT /opportunities/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a oportunidade de venda conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.opportunity_v1.OpportunityInfo
        Request model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return await self._request(
            "opportunity_v1.update_opportunities_by_internal_id",
            "PUT",
            "/opportunities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_opportunities_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui uma oportunidade de venda

        DELETE /opportunities/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui a oportunidade de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.opportunity_v1.OpportunityInfo
        """
        return await self._request(
            "opportunity_v1.delete_opportunities_by_internal_id",
            "DELETE",
            "/opportunities/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
