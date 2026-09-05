"""Limite de credito do Cliente — generated from CustomerCreditLimit_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CustomerCreditLimitV1(ApiGroup):
    """Limite de credito do Cliente (/api/fat/v1)."""

    api_id = "customer_credit_limit_v1"
    base_path = "/api/fat/v1"

    def list_customer_credit_limit(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar o limite de credito de todos os Clientes

        GET /CustomerCreditLimit; operationId=getCustomerCreditLimit; Protheus >= 12.1.23

        Retorna uma lista com o Limite de credito de todos os Clientes

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.customer_credit_limit_v1.PagedCustomerCreditLimit
        """
        return self._request(
            "customer_credit_limit_v1.list_customer_credit_limit",
            "GET",
            "/CustomerCreditLimit",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_customer_credit_limit_by_customer_internal_id(self, customer_internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar o Limite de crédito de um Cliente especifico

        GET /CustomerCreditLimit/{CustomerInternalId}; operationId=getCustomerInternalId; Protheus >= 12.1.23

        Retorna o Limite de credito de um Cliente

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e CustomerInternalId

        Response model: protheus.models.customer_credit_limit_v1.CustomerCreditLimitInfo
        """
        return self._request(
            "customer_credit_limit_v1.get_customer_credit_limit_by_customer_internal_id",
            "GET",
            "/CustomerCreditLimit/{CustomerInternalId}",
            path_params={"CustomerInternalId": customer_internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCustomerCreditLimitV1(AsyncApiGroup):
    """Limite de credito do Cliente (/api/fat/v1)."""

    api_id = "customer_credit_limit_v1"
    base_path = "/api/fat/v1"

    async def list_customer_credit_limit(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar o limite de credito de todos os Clientes

        GET /CustomerCreditLimit; operationId=getCustomerCreditLimit; Protheus >= 12.1.23

        Retorna uma lista com o Limite de credito de todos os Clientes

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.customer_credit_limit_v1.PagedCustomerCreditLimit
        """
        return await self._request(
            "customer_credit_limit_v1.list_customer_credit_limit",
            "GET",
            "/CustomerCreditLimit",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_customer_credit_limit_by_customer_internal_id(self, customer_internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consultar o Limite de crédito de um Cliente especifico

        GET /CustomerCreditLimit/{CustomerInternalId}; operationId=getCustomerInternalId; Protheus >= 12.1.23

        Retorna o Limite de credito de um Cliente

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e CustomerInternalId

        Response model: protheus.models.customer_credit_limit_v1.CustomerCreditLimitInfo
        """
        return await self._request(
            "customer_credit_limit_v1.get_customer_credit_limit_by_customer_internal_id",
            "GET",
            "/CustomerCreditLimit/{CustomerInternalId}",
            path_params={"CustomerInternalId": customer_internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )
