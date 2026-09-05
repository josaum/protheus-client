"""Tipo de Saldo Orçamentário — generated from BudgetBalanceType_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class BudgetBalanceTypeV1(ApiGroup):
    """Tipo de Saldo Orçamentário (/api/pco/v1)."""

    api_id = "budget_balance_type_v1"
    base_path = "/api/pco/v1"

    def list_budget_balance_type(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Lista do Tipo de Saldo Orçamentário

        GET /BudgetBalanceType; operationId=getBudgetBalanceType; Protheus >= 12.1.23

        Retorna Cadastro de Tipo de Saldo Orçamentário

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.budget_balance_type_v1.PagedItems
        """
        return self._request(
            "budget_balance_type_v1.list_budget_balance_type",
            "GET",
            "/BudgetBalanceType",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_budget_balance_type(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Incluir um Tipo de Saldo Orçamentário

        POST /BudgetBalanceType; operationId=postBudgetBalanceType; Protheus >= 12.1.23

        Incluir um Tipo de Saldo Orçamentário conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os paramêtros Authorization e Fields

        Response model: protheus.models.budget_balance_type_v1.BusinessContentType
        Request model: protheus.models.budget_balance_type_v1.BusinessContentType
        """
        return self._request(
            "budget_balance_type_v1.create_budget_balance_type",
            "POST",
            "/BudgetBalanceType",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_budget_balance_type_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Tipo de Saldo Orçamentário específico de acordo com a chave de pesquisa

        GET /BudgetBalanceType/{InternalId}; operationId=getInternalId; Protheus >= 12.1.23

        Retorna o Tipo de Saldo Orçamentário de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por Filial + Código do Tipo de Saldo Orçamentário

        Response model: protheus.models.budget_balance_type_v1.BusinessContentType
        """
        return self._request(
            "budget_balance_type_v1.get_budget_balance_type_by_internal_id",
            "GET",
            "/BudgetBalanceType/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_budget_balance_type_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Tipo de Saldo Orçamentário

        PUT /BudgetBalanceType/{InternalId}; operationId=putInternalId; Protheus >= 12.1.23

        Atualiza o Tipo de Saldo Orçamentário conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os paramêtros Authorization, InternalId e Fields

        Response model: protheus.models.budget_balance_type_v1.BusinessContentType
        Request model: protheus.models.budget_balance_type_v1.BusinessContentType
        """
        return self._request(
            "budget_balance_type_v1.update_budget_balance_type_by_internal_id",
            "PUT",
            "/BudgetBalanceType/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_budget_balance_type_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Tipo de Saldo Orçamentário

        DELETE /BudgetBalanceType/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.23

        Exclui um Tipo de Saldo Orçamentário conforme dados enviados na requisição.

        TOTVS note: Este verbo está disponível com os paramêtros Authorization e Fields
        """
        return self._request(
            "budget_balance_type_v1.delete_budget_balance_type_by_internal_id",
            "DELETE",
            "/BudgetBalanceType/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncBudgetBalanceTypeV1(AsyncApiGroup):
    """Tipo de Saldo Orçamentário (/api/pco/v1)."""

    api_id = "budget_balance_type_v1"
    base_path = "/api/pco/v1"

    async def list_budget_balance_type(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Lista do Tipo de Saldo Orçamentário

        GET /BudgetBalanceType; operationId=getBudgetBalanceType; Protheus >= 12.1.23

        Retorna Cadastro de Tipo de Saldo Orçamentário

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.budget_balance_type_v1.PagedItems
        """
        return await self._request(
            "budget_balance_type_v1.list_budget_balance_type",
            "GET",
            "/BudgetBalanceType",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_budget_balance_type(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Incluir um Tipo de Saldo Orçamentário

        POST /BudgetBalanceType; operationId=postBudgetBalanceType; Protheus >= 12.1.23

        Incluir um Tipo de Saldo Orçamentário conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os paramêtros Authorization e Fields

        Response model: protheus.models.budget_balance_type_v1.BusinessContentType
        Request model: protheus.models.budget_balance_type_v1.BusinessContentType
        """
        return await self._request(
            "budget_balance_type_v1.create_budget_balance_type",
            "POST",
            "/BudgetBalanceType",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_budget_balance_type_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Tipo de Saldo Orçamentário específico de acordo com a chave de pesquisa

        GET /BudgetBalanceType/{InternalId}; operationId=getInternalId; Protheus >= 12.1.23

        Retorna o Tipo de Saldo Orçamentário de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por Filial + Código do Tipo de Saldo Orçamentário

        Response model: protheus.models.budget_balance_type_v1.BusinessContentType
        """
        return await self._request(
            "budget_balance_type_v1.get_budget_balance_type_by_internal_id",
            "GET",
            "/BudgetBalanceType/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_budget_balance_type_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Tipo de Saldo Orçamentário

        PUT /BudgetBalanceType/{InternalId}; operationId=putInternalId; Protheus >= 12.1.23

        Atualiza o Tipo de Saldo Orçamentário conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os paramêtros Authorization, InternalId e Fields

        Response model: protheus.models.budget_balance_type_v1.BusinessContentType
        Request model: protheus.models.budget_balance_type_v1.BusinessContentType
        """
        return await self._request(
            "budget_balance_type_v1.update_budget_balance_type_by_internal_id",
            "PUT",
            "/BudgetBalanceType/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_budget_balance_type_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Tipo de Saldo Orçamentário

        DELETE /BudgetBalanceType/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.23

        Exclui um Tipo de Saldo Orçamentário conforme dados enviados na requisição.

        TOTVS note: Este verbo está disponível com os paramêtros Authorization e Fields
        """
        return await self._request(
            "budget_balance_type_v1.delete_budget_balance_type_by_internal_id",
            "DELETE",
            "/BudgetBalanceType/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
