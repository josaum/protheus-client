"""Metas de Vendas — generated from SalesTargets_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SalesTargetsV1(ApiGroup):
    """Metas de Vendas (/api/crm/v1)."""

    api_id = "sales_targets_v1"
    base_path = "/api/crm/v1"

    def list_sales_target(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista com todas Metas de Vendas

        GET /salesTarget; operationId=getSalesTarget; Protheus >= 12.1.21

        Retorna uma lista completa de Metas de Vendas

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.sales_targets_v1.PagedSalesTargets
        """
        return self._request(
            "sales_targets_v1.list_sales_target",
            "GET",
            "/salesTarget",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_sales_target(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Meta de venda

        POST /salesTarget; operationId=postSalesTarget; Protheus >= 12.1.21

        Inclui uma Meta de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.sales_targets_v1.SalesTargetsInfo
        Request model: protheus.models.sales_targets_v1.SalesTargetsInfo
        """
        return self._request(
            "sales_targets_v1.create_sales_target",
            "POST",
            "/salesTarget",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_sales_target_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Meta de Venda pelo InternalId

        GET /salesTarget/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.sales_targets_v1.SalesTargetsInfo
        """
        return self._request(
            "sales_targets_v1.get_sales_target_by_internal_id",
            "GET",
            "/salesTarget/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_sales_target_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Meta de Venda pelo InternalId

        PUT /salesTarget/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.sales_targets_v1.SalesTargetsInfo
        Request model: protheus.models.sales_targets_v1.SalesTargetsInfo
        """
        return self._request(
            "sales_targets_v1.update_sales_target_by_internal_id",
            "PUT",
            "/salesTarget/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_sales_target_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Meta de Venda pelo InternalId

        DELETE /salesTarget/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return self._request(
            "sales_targets_v1.delete_sales_target_by_internal_id",
            "DELETE",
            "/salesTarget/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_sales_target_by_internal_id_itens_sales_target(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista com todos Itens das Metas de Vendas

        GET /salesTarget/{InternalId}/itensSalesTarget/; operationId=getItemSalesTarget; Protheus >= 12.1.21

        Retorna uma lista completa dos Itens das Metas de Vendas

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize, Fields e internalId

        Response model: protheus.models.sales_targets_v1.PagedItensSalesTargets
        """
        return self._request(
            "sales_targets_v1.list_sales_target_by_internal_id_itens_sales_target",
            "GET",
            "/salesTarget/{InternalId}/itensSalesTarget/",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_sales_target_by_internal_id_itens_sales_target(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item de uma Meta de venda

        POST /salesTarget/{InternalId}/itensSalesTarget/; operationId=postItemSalesTarget; Protheus >= 12.1.21

        Inclui um item de uma Meta de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e internalId
        """
        return self._request(
            "sales_targets_v1.create_sales_target_by_internal_id_itens_sales_target",
            "POST",
            "/salesTarget/{InternalId}/itensSalesTarget/",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_sales_target_by_internal_id_itens_sales_target_by_item_id(self, internal_id: str, item_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um item de uma Meta de Venda de venda especifica pelo ItemId

        GET /salesTarget/{InternalId}/itensSalesTarget/{ItemId}; operationId=getItemId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e ItemId
        """
        return self._request(
            "sales_targets_v1.get_sales_target_by_internal_id_itens_sales_target_by_item_id",
            "GET",
            "/salesTarget/{InternalId}/itensSalesTarget/{ItemId}",
            path_params={"InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_sales_target_by_internal_id_itens_sales_target_by_item_id(self, internal_id: str, item_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um item de uma Meta de Venda de venda especifica pelo ItemId

        PUT /salesTarget/{InternalId}/itensSalesTarget/{ItemId}; operationId=putItemId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e ItemId
        """
        return self._request(
            "sales_targets_v1.update_sales_target_by_internal_id_itens_sales_target_by_item_id",
            "PUT",
            "/salesTarget/{InternalId}/itensSalesTarget/{ItemId}",
            path_params={"InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_sales_target_by_internal_id_itens_sales_target_by_item_id(self, internal_id: str, item_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um item de uma Meta de Venda de venda especifica pelo ItemId

        DELETE /salesTarget/{InternalId}/itensSalesTarget/{ItemId}; operationId=deleteItemId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e ItemId
        """
        return self._request(
            "sales_targets_v1.delete_sales_target_by_internal_id_itens_sales_target_by_item_id",
            "DELETE",
            "/salesTarget/{InternalId}/itensSalesTarget/{ItemId}",
            path_params={"InternalId": internal_id, "ItemId": item_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSalesTargetsV1(AsyncApiGroup):
    """Metas de Vendas (/api/crm/v1)."""

    api_id = "sales_targets_v1"
    base_path = "/api/crm/v1"

    async def list_sales_target(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista com todas Metas de Vendas

        GET /salesTarget; operationId=getSalesTarget; Protheus >= 12.1.21

        Retorna uma lista completa de Metas de Vendas

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.sales_targets_v1.PagedSalesTargets
        """
        return await self._request(
            "sales_targets_v1.list_sales_target",
            "GET",
            "/salesTarget",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_sales_target(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Meta de venda

        POST /salesTarget; operationId=postSalesTarget; Protheus >= 12.1.21

        Inclui uma Meta de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.sales_targets_v1.SalesTargetsInfo
        Request model: protheus.models.sales_targets_v1.SalesTargetsInfo
        """
        return await self._request(
            "sales_targets_v1.create_sales_target",
            "POST",
            "/salesTarget",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_sales_target_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Meta de Venda pelo InternalId

        GET /salesTarget/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.sales_targets_v1.SalesTargetsInfo
        """
        return await self._request(
            "sales_targets_v1.get_sales_target_by_internal_id",
            "GET",
            "/salesTarget/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_sales_target_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Meta de Venda pelo InternalId

        PUT /salesTarget/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.sales_targets_v1.SalesTargetsInfo
        Request model: protheus.models.sales_targets_v1.SalesTargetsInfo
        """
        return await self._request(
            "sales_targets_v1.update_sales_target_by_internal_id",
            "PUT",
            "/salesTarget/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_sales_target_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Meta de Venda pelo InternalId

        DELETE /salesTarget/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return await self._request(
            "sales_targets_v1.delete_sales_target_by_internal_id",
            "DELETE",
            "/salesTarget/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_sales_target_by_internal_id_itens_sales_target(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista com todos Itens das Metas de Vendas

        GET /salesTarget/{InternalId}/itensSalesTarget/; operationId=getItemSalesTarget; Protheus >= 12.1.21

        Retorna uma lista completa dos Itens das Metas de Vendas

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize, Fields e internalId

        Response model: protheus.models.sales_targets_v1.PagedItensSalesTargets
        """
        return await self._request(
            "sales_targets_v1.list_sales_target_by_internal_id_itens_sales_target",
            "GET",
            "/salesTarget/{InternalId}/itensSalesTarget/",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_sales_target_by_internal_id_itens_sales_target(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item de uma Meta de venda

        POST /salesTarget/{InternalId}/itensSalesTarget/; operationId=postItemSalesTarget; Protheus >= 12.1.21

        Inclui um item de uma Meta de venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e internalId
        """
        return await self._request(
            "sales_targets_v1.create_sales_target_by_internal_id_itens_sales_target",
            "POST",
            "/salesTarget/{InternalId}/itensSalesTarget/",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_sales_target_by_internal_id_itens_sales_target_by_item_id(self, internal_id: str, item_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um item de uma Meta de Venda de venda especifica pelo ItemId

        GET /salesTarget/{InternalId}/itensSalesTarget/{ItemId}; operationId=getItemId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e ItemId
        """
        return await self._request(
            "sales_targets_v1.get_sales_target_by_internal_id_itens_sales_target_by_item_id",
            "GET",
            "/salesTarget/{InternalId}/itensSalesTarget/{ItemId}",
            path_params={"InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_sales_target_by_internal_id_itens_sales_target_by_item_id(self, internal_id: str, item_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um item de uma Meta de Venda de venda especifica pelo ItemId

        PUT /salesTarget/{InternalId}/itensSalesTarget/{ItemId}; operationId=putItemId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e ItemId
        """
        return await self._request(
            "sales_targets_v1.update_sales_target_by_internal_id_itens_sales_target_by_item_id",
            "PUT",
            "/salesTarget/{InternalId}/itensSalesTarget/{ItemId}",
            path_params={"InternalId": internal_id, "ItemId": item_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_sales_target_by_internal_id_itens_sales_target_by_item_id(self, internal_id: str, item_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um item de uma Meta de Venda de venda especifica pelo ItemId

        DELETE /salesTarget/{InternalId}/itensSalesTarget/{ItemId}; operationId=deleteItemId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e ItemId
        """
        return await self._request(
            "sales_targets_v1.delete_sales_target_by_internal_id_itens_sales_target_by_item_id",
            "DELETE",
            "/salesTarget/{InternalId}/itensSalesTarget/{ItemId}",
            path_params={"InternalId": internal_id, "ItemId": item_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
