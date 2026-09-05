"""Cliente/Fornecedor — generated from CustomerVendor_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CustomerVendorV1(ApiGroup):
    """Cliente/Fornecedor (/api/crm/v1)."""

    api_id = "customer_vendor_v1"
    base_path = "/api/crm/v1"

    def list_customer_vendor(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos Clientes/Fornecedores

        GET /customerVendor; operationId=getcustomerVendor; Protheus >= 12.1.21

        Retorna todos clientes e/ou fornecedores

        TOTVS note: Este verbo não está diponível no protheus. Utilize a consulta CustomerVendorEntity

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        """
        return self._request(
            "customer_vendor_v1.list_customer_vendor",
            "GET",
            "/customerVendor",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_customer_vendor(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Cliente/Fornecedor passada na requisição

        POST /customerVendor; operationId=postcustomerVendor

        Inclui a entidade Cliente/Fornecedor passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields. O protheus não é compatível com a opção Both. Cadastre o cliente e vendedor separadamente.

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        Request model: protheus.models.customer_vendor_v1.CustomerVendorInfo
        """
        return self._request(
            "customer_vendor_v1.create_customer_vendor",
            "POST",
            "/customerVendor",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_customer_vendor_by_entity_type(self, entity_type: str, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de uma entidade específica

        GET /customerVendor/{entityType}; operationId=getentityType; Protheus >= 12.1.21

        Retorna todos os registros de uma entidade específica - Customer ou Vendor

        TOTVS note: Este verbo está disponível com os parâmetros EntityType, Authorization, Fields, Order, Page e PageSize

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        """
        return self._request(
            "customer_vendor_v1.get_customer_vendor_by_entity_type",
            "GET",
            "/customerVendor/{entityType}",
            path_params={"entityType": entity_type},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_customer_vendor_by_entity_type_and_customer_vendor_id(self, entity_type: str, customer_vendor_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Cliente/Fornecedor

        GET /customerVendor/{entityType}/{customerVendorId}; operationId=getcustomerVendorId; Protheus >= 12.1.21

        Retorna  Cliente ou Fornecedor com base no código da entidade

        TOTVS note: Este verbo está disponível com os parâmetros CustomerVendorId,EntityType, Fields e Authorization

        Response model: protheus.models.customer_vendor_v1.CustomerVendorInfo
        """
        return self._request(
            "customer_vendor_v1.get_customer_vendor_by_entity_type_and_customer_vendor_id",
            "GET",
            "/customerVendor/{entityType}/{customerVendorId}",
            path_params={"entityType": entity_type, "customerVendorId": customer_vendor_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_customer_vendor_by_entity_type_and_customer_vendor_id(self, entity_type: str, customer_vendor_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza Cliente/Fornecedor informado na requisição

        PUT /customerVendor/{entityType}/{customerVendorId}; operationId=putcustomerVendorId; Protheus >= 12.1.21

        Atualiza a entidade Cliente/Fornecedor informada na requisição

        TOTVS note: Este verbo esta disponivel com os parâmetros authorization, customervendorID e Fields

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        Request model: protheus.models.customer_vendor_v1.CustomerVendorInfo
        """
        return self._request(
            "customer_vendor_v1.update_customer_vendor_by_entity_type_and_customer_vendor_id",
            "PUT",
            "/customerVendor/{entityType}/{customerVendorId}",
            path_params={"entityType": entity_type, "customerVendorId": customer_vendor_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_customer_vendor_by_entity_type_and_customer_vendor_id(self, entity_type: str, customer_vendor_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui o Cliente/Fornecedor passada na requisição

        DELETE /customerVendor/{entityType}/{customerVendorId}; operationId=deletecustomerVendorId; Protheus >= 12.1.21

        Exclui a entidade Cliente/Fornecedor passada na requisição

        TOTVS note: Este verbo esta disponivel com os parâmetros Authorization e CustomerVendorId

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        """
        return self._request(
            "customer_vendor_v1.delete_customer_vendor_by_entity_type_and_customer_vendor_id",
            "DELETE",
            "/customerVendor/{entityType}/{customerVendorId}",
            path_params={"entityType": entity_type, "customerVendorId": customer_vendor_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCustomerVendorV1(AsyncApiGroup):
    """Cliente/Fornecedor (/api/crm/v1)."""

    api_id = "customer_vendor_v1"
    base_path = "/api/crm/v1"

    async def list_customer_vendor(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos Clientes/Fornecedores

        GET /customerVendor; operationId=getcustomerVendor; Protheus >= 12.1.21

        Retorna todos clientes e/ou fornecedores

        TOTVS note: Este verbo não está diponível no protheus. Utilize a consulta CustomerVendorEntity

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        """
        return await self._request(
            "customer_vendor_v1.list_customer_vendor",
            "GET",
            "/customerVendor",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_customer_vendor(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Cliente/Fornecedor passada na requisição

        POST /customerVendor; operationId=postcustomerVendor

        Inclui a entidade Cliente/Fornecedor passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields. O protheus não é compatível com a opção Both. Cadastre o cliente e vendedor separadamente.

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        Request model: protheus.models.customer_vendor_v1.CustomerVendorInfo
        """
        return await self._request(
            "customer_vendor_v1.create_customer_vendor",
            "POST",
            "/customerVendor",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_customer_vendor_by_entity_type(self, entity_type: str, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de uma entidade específica

        GET /customerVendor/{entityType}; operationId=getentityType; Protheus >= 12.1.21

        Retorna todos os registros de uma entidade específica - Customer ou Vendor

        TOTVS note: Este verbo está disponível com os parâmetros EntityType, Authorization, Fields, Order, Page e PageSize

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        """
        return await self._request(
            "customer_vendor_v1.get_customer_vendor_by_entity_type",
            "GET",
            "/customerVendor/{entityType}",
            path_params={"entityType": entity_type},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_customer_vendor_by_entity_type_and_customer_vendor_id(self, entity_type: str, customer_vendor_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Cliente/Fornecedor

        GET /customerVendor/{entityType}/{customerVendorId}; operationId=getcustomerVendorId; Protheus >= 12.1.21

        Retorna  Cliente ou Fornecedor com base no código da entidade

        TOTVS note: Este verbo está disponível com os parâmetros CustomerVendorId,EntityType, Fields e Authorization

        Response model: protheus.models.customer_vendor_v1.CustomerVendorInfo
        """
        return await self._request(
            "customer_vendor_v1.get_customer_vendor_by_entity_type_and_customer_vendor_id",
            "GET",
            "/customerVendor/{entityType}/{customerVendorId}",
            path_params={"entityType": entity_type, "customerVendorId": customer_vendor_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_customer_vendor_by_entity_type_and_customer_vendor_id(self, entity_type: str, customer_vendor_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza Cliente/Fornecedor informado na requisição

        PUT /customerVendor/{entityType}/{customerVendorId}; operationId=putcustomerVendorId; Protheus >= 12.1.21

        Atualiza a entidade Cliente/Fornecedor informada na requisição

        TOTVS note: Este verbo esta disponivel com os parâmetros authorization, customervendorID e Fields

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        Request model: protheus.models.customer_vendor_v1.CustomerVendorInfo
        """
        return await self._request(
            "customer_vendor_v1.update_customer_vendor_by_entity_type_and_customer_vendor_id",
            "PUT",
            "/customerVendor/{entityType}/{customerVendorId}",
            path_params={"entityType": entity_type, "customerVendorId": customer_vendor_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_customer_vendor_by_entity_type_and_customer_vendor_id(self, entity_type: str, customer_vendor_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui o Cliente/Fornecedor passada na requisição

        DELETE /customerVendor/{entityType}/{customerVendorId}; operationId=deletecustomerVendorId; Protheus >= 12.1.21

        Exclui a entidade Cliente/Fornecedor passada na requisição

        TOTVS note: Este verbo esta disponivel com os parâmetros Authorization e CustomerVendorId

        Response model: protheus.models.customer_vendor_v1.PagedCustomerVendors
        """
        return await self._request(
            "customer_vendor_v1.delete_customer_vendor_by_entity_type_and_customer_vendor_id",
            "DELETE",
            "/customerVendor/{entityType}/{customerVendorId}",
            path_params={"entityType": entity_type, "customerVendorId": customer_vendor_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
