"""Vendedor — generated from Sellers_v2_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SellersV2(ApiGroup):
    """Vendedor (/api/crm/v2)."""

    api_id = "sellers_v2"
    base_path = "/api/crm/v2"

    def list_seller(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Vendedores

        GET /seller; operationId=getseller; Protheus >= 12.1.21

        Retorna lista completa de vendedores

        TOTVS note: Este verbo não está disponível com o parâmetro code

        Response model: protheus.models.sellers_v2.PagedSellers
        """
        return self._request(
            "sellers_v2.list_seller",
            "GET",
            "/seller",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_seller(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um vendedor

        POST /seller; operationId=postCode; Protheus >= 12.1.25

        Inclui um vendedor conforme dados enviados na requisição.

        TOTVS note: Este verbo não está disponível com o parâmetro code

        Response model: protheus.models.sellers_v2.PagedSellers
        Request model: protheus.models.sellers_v2.SellerInfo
        """
        return self._request(
            "sellers_v2.create_seller",
            "POST",
            "/seller",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_seller_by_code(self, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna vendedor pelo seu Código

        GET /seller/{code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Code.

        Response model: protheus.models.sellers_v2.SellerInfo
        """
        return self._request(
            "sellers_v2.get_seller_by_code",
            "GET",
            "/seller/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_seller_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um vendedor

        PUT /seller/{code}; operationId=putCode; Protheus >= 12.1.25

        Atualiza cadastro de vendedor conforme dados enviados na requisição

        TOTVS note: Este verbo não está disponível com o parâmetro code

        Response model: protheus.models.sellers_v2.SellerInfo
        Request model: protheus.models.sellers_v2.SellerInfo
        """
        return self._request(
            "sellers_v2.update_seller_by_code",
            "PUT",
            "/seller/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_seller_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um vendedor

        DELETE /seller/{code}; operationId=deleteCode; Protheus >= 12.1.25

        Exclui cadastro de vendedor conforme dados enviados na requisição.

        TOTVS note: Este verbo não está disponível com o parâmetro code
        """
        return self._request(
            "sellers_v2.delete_seller_by_code",
            "DELETE",
            "/seller/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSellersV2(AsyncApiGroup):
    """Vendedor (/api/crm/v2)."""

    api_id = "sellers_v2"
    base_path = "/api/crm/v2"

    async def list_seller(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Vendedores

        GET /seller; operationId=getseller; Protheus >= 12.1.21

        Retorna lista completa de vendedores

        TOTVS note: Este verbo não está disponível com o parâmetro code

        Response model: protheus.models.sellers_v2.PagedSellers
        """
        return await self._request(
            "sellers_v2.list_seller",
            "GET",
            "/seller",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_seller(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um vendedor

        POST /seller; operationId=postCode; Protheus >= 12.1.25

        Inclui um vendedor conforme dados enviados na requisição.

        TOTVS note: Este verbo não está disponível com o parâmetro code

        Response model: protheus.models.sellers_v2.PagedSellers
        Request model: protheus.models.sellers_v2.SellerInfo
        """
        return await self._request(
            "sellers_v2.create_seller",
            "POST",
            "/seller",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_seller_by_code(self, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna vendedor pelo seu Código

        GET /seller/{code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Code.

        Response model: protheus.models.sellers_v2.SellerInfo
        """
        return await self._request(
            "sellers_v2.get_seller_by_code",
            "GET",
            "/seller/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_seller_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um vendedor

        PUT /seller/{code}; operationId=putCode; Protheus >= 12.1.25

        Atualiza cadastro de vendedor conforme dados enviados na requisição

        TOTVS note: Este verbo não está disponível com o parâmetro code

        Response model: protheus.models.sellers_v2.SellerInfo
        Request model: protheus.models.sellers_v2.SellerInfo
        """
        return await self._request(
            "sellers_v2.update_seller_by_code",
            "PUT",
            "/seller/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_seller_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um vendedor

        DELETE /seller/{code}; operationId=deleteCode; Protheus >= 12.1.25

        Exclui cadastro de vendedor conforme dados enviados na requisição.

        TOTVS note: Este verbo não está disponível com o parâmetro code
        """
        return await self._request(
            "sellers_v2.delete_seller_by_code",
            "DELETE",
            "/seller/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
