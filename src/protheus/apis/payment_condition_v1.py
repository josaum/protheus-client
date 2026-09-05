"""Condição de Pagamento — generated from PaymentCondition_v1_00.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class PaymentConditionV1(ApiGroup):
    """Condição de Pagamento (/api/fat/v1)."""

    api_id = "payment_condition_v1"
    base_path = "/api/fat/v1"

    def list_paymentcondition(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Condições de pagamento

        GET /paymentcondition; operationId=getPaymentCondition; Protheus >= 12.1.21

        Retorna lista completa das condições de pagamento

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.payment_condition_v1.PagedPaymentCondition
        """
        return self._request(
            "payment_condition_v1.list_paymentcondition",
            "GET",
            "/paymentcondition",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_paymentcondition(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Condição de Pagamento

        POST /paymentcondition; operationId=postPaymentCondition; Protheus >= 12.1.21

        Inclui uma condição de pagamento conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.payment_condition_v1.PaymentConditionInfo
        Request model: protheus.models.payment_condition_v1.PaymentConditionInfo
        """
        return self._request(
            "payment_condition_v1.create_paymentcondition",
            "POST",
            "/paymentcondition",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_paymentcondition_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a condição de pagamento pelo InternalId

        GET /paymentcondition/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros, Authorization, Fields e InternalId

        Response model: protheus.models.payment_condition_v1.PaymentConditionInfo
        """
        return self._request(
            "payment_condition_v1.get_paymentcondition_by_internal_id",
            "GET",
            "/paymentcondition/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_paymentcondition_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma condição de pagamento

        PUT /paymentcondition/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a condição de pagamento conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Fields e InternalId

        Response model: protheus.models.payment_condition_v1.PaymentConditionInfo
        Request model: protheus.models.payment_condition_v1.PaymentConditionInfo
        """
        return self._request(
            "payment_condition_v1.update_paymentcondition_by_internal_id",
            "PUT",
            "/paymentcondition/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_paymentcondition_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma condição de pagamento

        DELETE /paymentcondition/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui a condição de pagamento conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e InternalId
        """
        return self._request(
            "payment_condition_v1.delete_paymentcondition_by_internal_id",
            "DELETE",
            "/paymentcondition/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncPaymentConditionV1(AsyncApiGroup):
    """Condição de Pagamento (/api/fat/v1)."""

    api_id = "payment_condition_v1"
    base_path = "/api/fat/v1"

    async def list_paymentcondition(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Condições de pagamento

        GET /paymentcondition; operationId=getPaymentCondition; Protheus >= 12.1.21

        Retorna lista completa das condições de pagamento

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.payment_condition_v1.PagedPaymentCondition
        """
        return await self._request(
            "payment_condition_v1.list_paymentcondition",
            "GET",
            "/paymentcondition",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_paymentcondition(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Condição de Pagamento

        POST /paymentcondition; operationId=postPaymentCondition; Protheus >= 12.1.21

        Inclui uma condição de pagamento conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.payment_condition_v1.PaymentConditionInfo
        Request model: protheus.models.payment_condition_v1.PaymentConditionInfo
        """
        return await self._request(
            "payment_condition_v1.create_paymentcondition",
            "POST",
            "/paymentcondition",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_paymentcondition_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a condição de pagamento pelo InternalId

        GET /paymentcondition/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros, Authorization, Fields e InternalId

        Response model: protheus.models.payment_condition_v1.PaymentConditionInfo
        """
        return await self._request(
            "payment_condition_v1.get_paymentcondition_by_internal_id",
            "GET",
            "/paymentcondition/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_paymentcondition_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma condição de pagamento

        PUT /paymentcondition/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a condição de pagamento conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Fields e InternalId

        Response model: protheus.models.payment_condition_v1.PaymentConditionInfo
        Request model: protheus.models.payment_condition_v1.PaymentConditionInfo
        """
        return await self._request(
            "payment_condition_v1.update_paymentcondition_by_internal_id",
            "PUT",
            "/paymentcondition/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_paymentcondition_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma condição de pagamento

        DELETE /paymentcondition/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui a condição de pagamento conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e InternalId
        """
        return await self._request(
            "payment_condition_v1.delete_paymentcondition_by_internal_id",
            "DELETE",
            "/paymentcondition/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
