"""Reservas de Produto — generated from ItemReserve_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ItemReserveV1(ApiGroup):
    """Reservas de Produto (/api/retail/v1)."""

    api_id = "item_reserve_v1"
    base_path = "/api/retail/v1"

    def list_item_reserves(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as reservas de produtos

        GET /ItemReserves; operationId=getItemReserve; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize, Fields

        Response model: protheus.models.item_reserve_v1.PagedItemReserves
        """
        return self._request(
            "item_reserve_v1.list_item_reserves",
            "GET",
            "/ItemReserves",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_item_reserves(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui reserva passada na requisição

        POST /ItemReserves; operationId=postItemReserve; Protheus >= 12.1.21

        Inclui a entidade ItemReserve passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        Request model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return self._request(
            "item_reserve_v1.create_item_reserves",
            "POST",
            "/ItemReserves",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_item_reserves_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Buscar reserva por InternalId que é constituido dos valores de documento da reserva e filial  D MG 01|01

        GET /ItemReserves/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna os dados da reserva de acordo com o número do documento da reserva e filial passadas por parametro

        TOTVS note: Este verbo está disponível com os parâmetros InternalId, Authorization

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return self._request(
            "item_reserve_v1.get_item_reserves_by_internal_id",
            "GET",
            "/ItemReserves/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_item_reserves_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza uma reserva passada na requisição

        PUT /ItemReserves/{InternalId}; operationId=putitemReserve; Protheus >= 12.1.21

        Atualiza a entidade ItemReserve passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        Request model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return self._request(
            "item_reserve_v1.update_item_reserves_by_internal_id",
            "PUT",
            "/ItemReserves/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_item_reserves_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta reserva passada na requisição

        DELETE /ItemReserves/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Deleta a entidade ItemReserve passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return self._request(
            "item_reserve_v1.delete_item_reserves_by_internal_id",
            "DELETE",
            "/ItemReserves/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncItemReserveV1(AsyncApiGroup):
    """Reservas de Produto (/api/retail/v1)."""

    api_id = "item_reserve_v1"
    base_path = "/api/retail/v1"

    async def list_item_reserves(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as reservas de produtos

        GET /ItemReserves; operationId=getItemReserve; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize, Fields

        Response model: protheus.models.item_reserve_v1.PagedItemReserves
        """
        return await self._request(
            "item_reserve_v1.list_item_reserves",
            "GET",
            "/ItemReserves",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_item_reserves(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui reserva passada na requisição

        POST /ItemReserves; operationId=postItemReserve; Protheus >= 12.1.21

        Inclui a entidade ItemReserve passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        Request model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return await self._request(
            "item_reserve_v1.create_item_reserves",
            "POST",
            "/ItemReserves",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_item_reserves_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Buscar reserva por InternalId que é constituido dos valores de documento da reserva e filial  D MG 01|01

        GET /ItemReserves/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna os dados da reserva de acordo com o número do documento da reserva e filial passadas por parametro

        TOTVS note: Este verbo está disponível com os parâmetros InternalId, Authorization

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return await self._request(
            "item_reserve_v1.get_item_reserves_by_internal_id",
            "GET",
            "/ItemReserves/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_item_reserves_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza uma reserva passada na requisição

        PUT /ItemReserves/{InternalId}; operationId=putitemReserve; Protheus >= 12.1.21

        Atualiza a entidade ItemReserve passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        Request model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return await self._request(
            "item_reserve_v1.update_item_reserves_by_internal_id",
            "PUT",
            "/ItemReserves/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_item_reserves_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta reserva passada na requisição

        DELETE /ItemReserves/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Deleta a entidade ItemReserve passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.item_reserve_v1.ItemReserveType
        """
        return await self._request(
            "item_reserve_v1.delete_item_reserves_by_internal_id",
            "DELETE",
            "/ItemReserves/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
