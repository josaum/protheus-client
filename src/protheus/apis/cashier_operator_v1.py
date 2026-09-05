"""Operador de Caixa — generated from CashierOperator_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CashierOperatorV1(ApiGroup):
    """Operador de Caixa (/api/retail/v1)."""

    api_id = "cashier_operator_v1"
    base_path = "/api/retail/v1"

    def list_cashier_operators(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os operadores de caixa

        GET /CashierOperators; operationId=getCashierOperator; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize, Fields

        Response model: protheus.models.cashier_operator_v1.PagedCashierOperators
        """
        return self._request(
            "cashier_operator_v1.list_cashier_operators",
            "GET",
            "/CashierOperators",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cashier_operators(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui operador de caixa passado na requisição

        POST /CashierOperators; operationId=postCashierOperator; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        Request model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return self._request(
            "cashier_operator_v1.create_cashier_operators",
            "POST",
            "/CashierOperators",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_cashier_operators_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Buscar operador de caixa por InternalId que é constituido dos valores de filial e codigo do operador  D MG 01|01

        GET /CashierOperators/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna os dados do operador de caixa de acordo com a filial e código do operador passados por parametro

        TOTVS note: Este verbo está disponível com os parâmetros InternalId, Authorization

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return self._request(
            "cashier_operator_v1.get_cashier_operators_by_internal_id",
            "GET",
            "/CashierOperators/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cashier_operators_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um operador de caixa passado na requisição

        PUT /CashierOperators/{InternalId}; operationId=putcashierOperator; Protheus >= 12.1.21

        Atualiza a entidade operador de caixa passado na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        Request model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return self._request(
            "cashier_operator_v1.update_cashier_operators_by_internal_id",
            "PUT",
            "/CashierOperators/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cashier_operators_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta operador de caixa passado na requisição

        DELETE /CashierOperators/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Deleta a entidade CashierOperator passado na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return self._request(
            "cashier_operator_v1.delete_cashier_operators_by_internal_id",
            "DELETE",
            "/CashierOperators/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCashierOperatorV1(AsyncApiGroup):
    """Operador de Caixa (/api/retail/v1)."""

    api_id = "cashier_operator_v1"
    base_path = "/api/retail/v1"

    async def list_cashier_operators(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os operadores de caixa

        GET /CashierOperators; operationId=getCashierOperator; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize, Fields

        Response model: protheus.models.cashier_operator_v1.PagedCashierOperators
        """
        return await self._request(
            "cashier_operator_v1.list_cashier_operators",
            "GET",
            "/CashierOperators",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cashier_operators(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui operador de caixa passado na requisição

        POST /CashierOperators; operationId=postCashierOperator; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        Request model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return await self._request(
            "cashier_operator_v1.create_cashier_operators",
            "POST",
            "/CashierOperators",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_cashier_operators_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Buscar operador de caixa por InternalId que é constituido dos valores de filial e codigo do operador  D MG 01|01

        GET /CashierOperators/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna os dados do operador de caixa de acordo com a filial e código do operador passados por parametro

        TOTVS note: Este verbo está disponível com os parâmetros InternalId, Authorization

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return await self._request(
            "cashier_operator_v1.get_cashier_operators_by_internal_id",
            "GET",
            "/CashierOperators/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cashier_operators_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um operador de caixa passado na requisição

        PUT /CashierOperators/{InternalId}; operationId=putcashierOperator; Protheus >= 12.1.21

        Atualiza a entidade operador de caixa passado na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        Request model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return await self._request(
            "cashier_operator_v1.update_cashier_operators_by_internal_id",
            "PUT",
            "/CashierOperators/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cashier_operators_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta operador de caixa passado na requisição

        DELETE /CashierOperators/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Deleta a entidade CashierOperator passado na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization

        Response model: protheus.models.cashier_operator_v1.CashierOperatorType
        """
        return await self._request(
            "cashier_operator_v1.delete_cashier_operators_by_internal_id",
            "DELETE",
            "/CashierOperators/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
