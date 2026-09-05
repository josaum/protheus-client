"""Grupo de Compras — generated from PurchaseGroups_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class PurchaseGroupsV1(ApiGroup):
    """Grupo de Compras (/api/purchasegroups/v1)."""

    api_id = "purchase_groups_v1"
    base_path = "/api/purchasegroups/v1"

    def list_purchase_groups(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Grupos de Compras (purchaseGroups).

        GET /purchaseGroups; operationId=getpurchaseGroups; Protheus >= 12.1.21

        Retorna todos os Grupo Compras (purchaseGroups) do Protheus.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PagedPurchasesGroups
        """
        return self._request(
            "purchase_groups_v1.list_purchase_groups",
            "GET",
            "/purchaseGroups",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_purchase_groups(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Grupo de Compras (purchaseGroups).

        POST /purchaseGroups; operationId=postPurchaseGroups; Protheus >= 12.1.21

        Inclui um Grupo de Compras (purchaseGroups), com base nos dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return self._request(
            "purchase_groups_v1.create_purchase_groups",
            "POST",
            "/purchaseGroups",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_purchase_groups_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Grupo de Compras (purchaseGroup).

        GET /purchaseGroups/{InternalId}; operationId=getcode; Protheus >= 12.1.21

        Retorna um Grupo de Compras (purchaseGroup), especifico com base nas informações enviadas na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return self._request(
            "purchase_groups_v1.get_purchase_groups_by_internal_id",
            "GET",
            "/purchaseGroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_purchase_groups_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Grupo de Compras (purchaseGroup).

        PUT /purchaseGroups/{InternalId}; operationId=putcode; Protheus >= 12.1.21

        Altera um Grupo de Compras (purchaseGroup), especifico com base nos dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return self._request(
            "purchase_groups_v1.update_purchase_groups_by_internal_id",
            "PUT",
            "/purchaseGroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_purchase_groups_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão do Grupo de Compras (purchaseGroup).

        DELETE /purchaseGroups/{InternalId}; operationId=deletecode

        Exclusão de um Grupo de Compras, baseado nas informações enviadas na requisição.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return self._request(
            "purchase_groups_v1.delete_purchase_groups_by_internal_id",
            "DELETE",
            "/purchaseGroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_purchase_groups_by_internal_id_purchase_groups_itens(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Compradores (Buyers) cadastrados no Grupo de Compras (purchaseGroup) especifico.

        GET /purchaseGroups/{InternalId}/purchaseGroupsItens/; operationId=getpurchaseGroupsItens; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return self._request(
            "purchase_groups_v1.list_purchase_groups_by_internal_id_purchase_groups_itens",
            "GET",
            "/purchaseGroups/{InternalId}/purchaseGroupsItens/",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_purchase_groups_by_internal_id_purchase_groups_itens(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroup) especifico.

        POST /purchaseGroups/{InternalId}/purchaseGroupsItens/; operationId=postPurchaseGroupsListItem; Protheus >= 12.1.21

        Inclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroup) existente, baseado nos dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return self._request(
            "purchase_groups_v1.create_purchase_groups_by_internal_id_purchase_groups_itens",
            "POST",
            "/purchaseGroups/{InternalId}/purchaseGroupsItens/",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence(self, internal_id: str, itemsequence: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup).

        GET /purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}; operationId=getPurchaseGroupsListItem; Protheus >= 12.1.21

        Retorna o Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup), baseado na requisição enviada.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return self._request(
            "purchase_groups_v1.get_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence",
            "GET",
            "/purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}",
            path_params={"InternalId": internal_id, "itemsequence": itemsequence},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence(self, internal_id: str, itemsequence: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup).

        PUT /purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}; operationId=putPurchaseGroupsListItem; Protheus >= 12.1.21

        Altera um Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup), baseando nas informações passadas na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return self._request(
            "purchase_groups_v1.update_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence",
            "PUT",
            "/purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}",
            path_params={"InternalId": internal_id, "itemsequence": itemsequence},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence(self, internal_id: str, itemsequence: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroups).

        DELETE /purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}; operationId=deletePurchaseGroupsListItem

        Exclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroups) baseado nos dados enviados na requisição.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return self._request(
            "purchase_groups_v1.delete_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence",
            "DELETE",
            "/purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}",
            path_params={"InternalId": internal_id, "itemsequence": itemsequence},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncPurchaseGroupsV1(AsyncApiGroup):
    """Grupo de Compras (/api/purchasegroups/v1)."""

    api_id = "purchase_groups_v1"
    base_path = "/api/purchasegroups/v1"

    async def list_purchase_groups(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Grupos de Compras (purchaseGroups).

        GET /purchaseGroups; operationId=getpurchaseGroups; Protheus >= 12.1.21

        Retorna todos os Grupo Compras (purchaseGroups) do Protheus.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PagedPurchasesGroups
        """
        return await self._request(
            "purchase_groups_v1.list_purchase_groups",
            "GET",
            "/purchaseGroups",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_purchase_groups(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Grupo de Compras (purchaseGroups).

        POST /purchaseGroups; operationId=postPurchaseGroups; Protheus >= 12.1.21

        Inclui um Grupo de Compras (purchaseGroups), com base nos dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return await self._request(
            "purchase_groups_v1.create_purchase_groups",
            "POST",
            "/purchaseGroups",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_purchase_groups_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Grupo de Compras (purchaseGroup).

        GET /purchaseGroups/{InternalId}; operationId=getcode; Protheus >= 12.1.21

        Retorna um Grupo de Compras (purchaseGroup), especifico com base nas informações enviadas na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return await self._request(
            "purchase_groups_v1.get_purchase_groups_by_internal_id",
            "GET",
            "/purchaseGroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_purchase_groups_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Grupo de Compras (purchaseGroup).

        PUT /purchaseGroups/{InternalId}; operationId=putcode; Protheus >= 12.1.21

        Altera um Grupo de Compras (purchaseGroup), especifico com base nos dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return await self._request(
            "purchase_groups_v1.update_purchase_groups_by_internal_id",
            "PUT",
            "/purchaseGroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_purchase_groups_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão do Grupo de Compras (purchaseGroup).

        DELETE /purchaseGroups/{InternalId}; operationId=deletecode

        Exclusão de um Grupo de Compras, baseado nas informações enviadas na requisição.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupsInfo
        """
        return await self._request(
            "purchase_groups_v1.delete_purchase_groups_by_internal_id",
            "DELETE",
            "/purchaseGroups/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_purchase_groups_by_internal_id_purchase_groups_itens(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Compradores (Buyers) cadastrados no Grupo de Compras (purchaseGroup) especifico.

        GET /purchaseGroups/{InternalId}/purchaseGroupsItens/; operationId=getpurchaseGroupsItens; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return await self._request(
            "purchase_groups_v1.list_purchase_groups_by_internal_id_purchase_groups_itens",
            "GET",
            "/purchaseGroups/{InternalId}/purchaseGroupsItens/",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_purchase_groups_by_internal_id_purchase_groups_itens(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroup) especifico.

        POST /purchaseGroups/{InternalId}/purchaseGroupsItens/; operationId=postPurchaseGroupsListItem; Protheus >= 12.1.21

        Inclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroup) existente, baseado nos dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return await self._request(
            "purchase_groups_v1.create_purchase_groups_by_internal_id_purchase_groups_itens",
            "POST",
            "/purchaseGroups/{InternalId}/purchaseGroupsItens/",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence(self, internal_id: str, itemsequence: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup).

        GET /purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}; operationId=getPurchaseGroupsListItem; Protheus >= 12.1.21

        Retorna o Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup), baseado na requisição enviada.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return await self._request(
            "purchase_groups_v1.get_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence",
            "GET",
            "/purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}",
            path_params={"InternalId": internal_id, "itemsequence": itemsequence},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence(self, internal_id: str, itemsequence: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup).

        PUT /purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}; operationId=putPurchaseGroupsListItem; Protheus >= 12.1.21

        Altera um Comprador (Buyer) especifico do Grupo de Compras (purchaseGroup), baseando nas informações passadas na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        Request model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return await self._request(
            "purchase_groups_v1.update_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence",
            "PUT",
            "/purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}",
            path_params={"InternalId": internal_id, "itemsequence": itemsequence},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence(self, internal_id: str, itemsequence: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroups).

        DELETE /purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}; operationId=deletePurchaseGroupsListItem

        Exclui um Comprador (Buyer) em um Grupo de Compras (purchaseGroups) baseado nos dados enviados na requisição.

        Response model: protheus.models.purchase_groups_v1.PurchaseGroupListBuyers
        """
        return await self._request(
            "purchase_groups_v1.delete_purchase_groups_by_internal_id_purchase_groups_item_by_itemsequence",
            "DELETE",
            "/purchaseGroups/{InternalId}/purchaseGroupsItem/{itemsequence}",
            path_params={"InternalId": internal_id, "itemsequence": itemsequence},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
