"""Compradores — generated from Buyers_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class BuyersV1(ApiGroup):
    """Compradores (/api/supply/v1)."""

    api_id = "buyers_v1"
    base_path = "/api/supply/v1"

    def list_buyers(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Compradores do sistema

        GET /buyers; operationId=getBuyers; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.PagedBuyers
        """
        return self._request(
            "buyers_v1.list_buyers",
            "GET",
            "/buyers",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_buyers(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona Comprador passado na requisição

        POST /buyers; operationId=postBuyer; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.PostBuyer
        Request model: protheus.models.buyers_v1.PostBuyer
        """
        return self._request(
            "buyers_v1.create_buyers",
            "POST",
            "/buyers",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_buyers_by_buyer_id(self, buyer_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Comprador do sistema através de seu código

        GET /buyers/{BuyerId}; operationId=getBuyerId; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.BuyerInfo
        """
        return self._request(
            "buyers_v1.get_buyers_by_buyer_id",
            "GET",
            "/buyers/{BuyerId}",
            path_params={"BuyerId": buyer_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_buyers_by_buyer_id(self, buyer_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o comprador passado na requisição

        PUT /buyers/{BuyerId}; operationId=putBuyerId; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.BuyerInfo
        Request model: protheus.models.buyers_v1.BuyerInfo
        """
        return self._request(
            "buyers_v1.update_buyers_by_buyer_id",
            "PUT",
            "/buyers/{BuyerId}",
            path_params={"BuyerId": buyer_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_buyers_by_buyer_id(self, buyer_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de Comprador da base

        DELETE /buyers/{BuyerId}; operationId=DeleteBuyer; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.BuyerInfo
        """
        return self._request(
            "buyers_v1.delete_buyers_by_buyer_id",
            "DELETE",
            "/buyers/{BuyerId}",
            path_params={"BuyerId": buyer_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncBuyersV1(AsyncApiGroup):
    """Compradores (/api/supply/v1)."""

    api_id = "buyers_v1"
    base_path = "/api/supply/v1"

    async def list_buyers(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Compradores do sistema

        GET /buyers; operationId=getBuyers; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.PagedBuyers
        """
        return await self._request(
            "buyers_v1.list_buyers",
            "GET",
            "/buyers",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_buyers(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona Comprador passado na requisição

        POST /buyers; operationId=postBuyer; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.PostBuyer
        Request model: protheus.models.buyers_v1.PostBuyer
        """
        return await self._request(
            "buyers_v1.create_buyers",
            "POST",
            "/buyers",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_buyers_by_buyer_id(self, buyer_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Comprador do sistema através de seu código

        GET /buyers/{BuyerId}; operationId=getBuyerId; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.BuyerInfo
        """
        return await self._request(
            "buyers_v1.get_buyers_by_buyer_id",
            "GET",
            "/buyers/{BuyerId}",
            path_params={"BuyerId": buyer_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_buyers_by_buyer_id(self, buyer_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o comprador passado na requisição

        PUT /buyers/{BuyerId}; operationId=putBuyerId; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.BuyerInfo
        Request model: protheus.models.buyers_v1.BuyerInfo
        """
        return await self._request(
            "buyers_v1.update_buyers_by_buyer_id",
            "PUT",
            "/buyers/{BuyerId}",
            path_params={"BuyerId": buyer_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_buyers_by_buyer_id(self, buyer_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de Comprador da base

        DELETE /buyers/{BuyerId}; operationId=DeleteBuyer; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível para o Protheus.

        Response model: protheus.models.buyers_v1.BuyerInfo
        """
        return await self._request(
            "buyers_v1.delete_buyers_by_buyer_id",
            "DELETE",
            "/buyers/{BuyerId}",
            path_params={"BuyerId": buyer_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
