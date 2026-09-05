"""Atividade do Vendedor — generated from SellerActivity_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SellerActivityV1(ApiGroup):
    """Atividade do Vendedor (/api/crm/v1)."""

    api_id = "seller_activity_v1"
    base_path = "/api/crm/v1"

    def list_selleractivity(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Atividades

        GET /selleractivity; operationId=getselleractivity; Protheus >= 12.1.21

        Retorna uma lista completa de Atividades dos vendedores

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.seller_activity_v1.PagedSellerActivity
        """
        return self._request(
            "seller_activity_v1.list_selleractivity",
            "GET",
            "/selleractivity",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_selleractivity(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Atividade

        POST /selleractivity; operationId=postselleractivity; Protheus >= 12.1.21

        Inclui uma Atividade conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.seller_activity_v1.SellerActivityInfo
        Request model: protheus.models.seller_activity_v1.SellerActivityInfo
        """
        return self._request(
            "seller_activity_v1.create_selleractivity",
            "POST",
            "/selleractivity",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_selleractivity_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Atividade pelo InternalId

        GET /selleractivity/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.seller_activity_v1.SellerActivityInfo
        """
        return self._request(
            "seller_activity_v1.get_selleractivity_by_internal_id",
            "GET",
            "/selleractivity/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_selleractivity_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Atividade pelo InternalId

        PUT /selleractivity/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.seller_activity_v1.SellerActivityInfo
        Request model: protheus.models.seller_activity_v1.SellerActivityInfo
        """
        return self._request(
            "seller_activity_v1.update_selleractivity_by_internal_id",
            "PUT",
            "/selleractivity/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_selleractivity_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Atividade pelo InternalId

        DELETE /selleractivity/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return self._request(
            "seller_activity_v1.delete_selleractivity_by_internal_id",
            "DELETE",
            "/selleractivity/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSellerActivityV1(AsyncApiGroup):
    """Atividade do Vendedor (/api/crm/v1)."""

    api_id = "seller_activity_v1"
    base_path = "/api/crm/v1"

    async def list_selleractivity(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Atividades

        GET /selleractivity; operationId=getselleractivity; Protheus >= 12.1.21

        Retorna uma lista completa de Atividades dos vendedores

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.seller_activity_v1.PagedSellerActivity
        """
        return await self._request(
            "seller_activity_v1.list_selleractivity",
            "GET",
            "/selleractivity",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_selleractivity(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Atividade

        POST /selleractivity; operationId=postselleractivity; Protheus >= 12.1.21

        Inclui uma Atividade conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.seller_activity_v1.SellerActivityInfo
        Request model: protheus.models.seller_activity_v1.SellerActivityInfo
        """
        return await self._request(
            "seller_activity_v1.create_selleractivity",
            "POST",
            "/selleractivity",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_selleractivity_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Atividade pelo InternalId

        GET /selleractivity/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.seller_activity_v1.SellerActivityInfo
        """
        return await self._request(
            "seller_activity_v1.get_selleractivity_by_internal_id",
            "GET",
            "/selleractivity/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_selleractivity_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Atividade pelo InternalId

        PUT /selleractivity/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.seller_activity_v1.SellerActivityInfo
        Request model: protheus.models.seller_activity_v1.SellerActivityInfo
        """
        return await self._request(
            "seller_activity_v1.update_selleractivity_by_internal_id",
            "PUT",
            "/selleractivity/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_selleractivity_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Atividade pelo InternalId

        DELETE /selleractivity/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return await self._request(
            "seller_activity_v1.delete_selleractivity_by_internal_id",
            "DELETE",
            "/selleractivity/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
