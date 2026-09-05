"""Endereços de Entrega do Cliente — generated from CustomerShippingAddress_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CustomerShippingAddressV1(ApiGroup):
    """Endereços de Entrega do Cliente (/api/tms/v1)."""

    api_id = "customer_shipping_address_v1"
    base_path = "/api/tms/v1"

    def list_customer_shipping_address(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Endereços de Entrega do Cliente

        GET /CustomerShippingAddress; operationId=getCustomerShippingAddress; Protheus >= 12.1.21

        Retorna lista completa do Endereço de Entrega do Cliente

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.customer_shipping_address_v1.PagedCustomerShippingAddress
        """
        return self._request(
            "customer_shipping_address_v1.list_customer_shipping_address",
            "GET",
            "/CustomerShippingAddress",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_customer_shipping_address(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Endereço de Entrega do Cliente

        POST /CustomerShippingAddress; operationId=postCustomerShippingAddress; Protheus >= 12.1.21

        Inclui um Endereço de Entrega do Cliente conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.customer_shipping_address_v1.PagedCustomerShippingAddress
        Request model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        """
        return self._request(
            "customer_shipping_address_v1.create_customer_shipping_address",
            "POST",
            "/CustomerShippingAddress",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_customer_shipping_address_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Endereço de Entrega do Cliente específica de acordo com a chave de pesquisa

        GET /CustomerShippingAddress/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o Endereço de Entrega do Cliente de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código do Endereço de Entrega do Cliente

        Response model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        """
        return self._request(
            "customer_shipping_address_v1.get_customer_shipping_address_by_internal_id",
            "GET",
            "/CustomerShippingAddress/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_customer_shipping_address_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Endereço de Entrega do Cliente

        PUT /CustomerShippingAddress/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o Endereço de Entrega do Cliente conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        Request model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        """
        return self._request(
            "customer_shipping_address_v1.update_customer_shipping_address_by_internal_id",
            "PUT",
            "/CustomerShippingAddress/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_customer_shipping_address_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Endereço de Entrega do Cliente

        DELETE /CustomerShippingAddress/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Endereço de Entrega do Cliente conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "customer_shipping_address_v1.delete_customer_shipping_address_by_internal_id",
            "DELETE",
            "/CustomerShippingAddress/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCustomerShippingAddressV1(AsyncApiGroup):
    """Endereços de Entrega do Cliente (/api/tms/v1)."""

    api_id = "customer_shipping_address_v1"
    base_path = "/api/tms/v1"

    async def list_customer_shipping_address(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Endereços de Entrega do Cliente

        GET /CustomerShippingAddress; operationId=getCustomerShippingAddress; Protheus >= 12.1.21

        Retorna lista completa do Endereço de Entrega do Cliente

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.customer_shipping_address_v1.PagedCustomerShippingAddress
        """
        return await self._request(
            "customer_shipping_address_v1.list_customer_shipping_address",
            "GET",
            "/CustomerShippingAddress",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_customer_shipping_address(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Endereço de Entrega do Cliente

        POST /CustomerShippingAddress; operationId=postCustomerShippingAddress; Protheus >= 12.1.21

        Inclui um Endereço de Entrega do Cliente conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.customer_shipping_address_v1.PagedCustomerShippingAddress
        Request model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        """
        return await self._request(
            "customer_shipping_address_v1.create_customer_shipping_address",
            "POST",
            "/CustomerShippingAddress",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_customer_shipping_address_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Endereço de Entrega do Cliente específica de acordo com a chave de pesquisa

        GET /CustomerShippingAddress/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o Endereço de Entrega do Cliente de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código do Endereço de Entrega do Cliente

        Response model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        """
        return await self._request(
            "customer_shipping_address_v1.get_customer_shipping_address_by_internal_id",
            "GET",
            "/CustomerShippingAddress/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_customer_shipping_address_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Endereço de Entrega do Cliente

        PUT /CustomerShippingAddress/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o Endereço de Entrega do Cliente conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        Request model: protheus.models.customer_shipping_address_v1.CustomerShippingAddressInfo
        """
        return await self._request(
            "customer_shipping_address_v1.update_customer_shipping_address_by_internal_id",
            "PUT",
            "/CustomerShippingAddress/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_customer_shipping_address_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Endereço de Entrega do Cliente

        DELETE /CustomerShippingAddress/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Endereço de Entrega do Cliente conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "customer_shipping_address_v1.delete_customer_shipping_address_by_internal_id",
            "DELETE",
            "/CustomerShippingAddress/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
