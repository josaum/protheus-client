"""Calendário Contábil — generated from AccountingCalendar_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AccountingCalendarV1(ApiGroup):
    """Calendário Contábil (/api/ctb/v1)."""

    api_id = "accounting_calendar_v1"
    base_path = "/api/ctb/v1"

    def list_accounting_calendar(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Cadastro do Calendário Contábil

        GET /AccountingCalendar; operationId=getAccountingCalendar; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.accounting_calendar_v1.PagedItems
        """
        return self._request(
            "accounting_calendar_v1.list_accounting_calendar",
            "GET",
            "/AccountingCalendar",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_accounting_calendar(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Incluir um Calendário Contábil

        POST /AccountingCalendar; operationId=postAccountingCalendar; Protheus >= 12.1.21

        Incluir um Calendário Contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.accounting_calendar_v1.PagedItems
        Request model: protheus.models.accounting_calendar_v1.BusinessContentType
        """
        return self._request(
            "accounting_calendar_v1.create_accounting_calendar",
            "POST",
            "/AccountingCalendar",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_accounting_calendar_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Calendário Contábil específico de acordo com a chave de pesquisa

        GET /AccountingCalendar/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a Calendário Contábil de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código do Calendário + Ano de Exercicío + Periodo

        Response model: protheus.models.accounting_calendar_v1.BusinessContentType
        """
        return self._request(
            "accounting_calendar_v1.get_accounting_calendar_by_internal_id",
            "GET",
            "/AccountingCalendar/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_accounting_calendar_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Calendário Contábil

        PUT /AccountingCalendar/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o Calendário Contábil conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.accounting_calendar_v1.BusinessContentType
        Request model: protheus.models.accounting_calendar_v1.BusinessContentType
        """
        return self._request(
            "accounting_calendar_v1.update_accounting_calendar_by_internal_id",
            "PUT",
            "/AccountingCalendar/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_accounting_calendar_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Calendário Contábil

        DELETE /AccountingCalendar/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Calendário Contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parametros Authorization e Fields
        """
        return self._request(
            "accounting_calendar_v1.delete_accounting_calendar_by_internal_id",
            "DELETE",
            "/AccountingCalendar/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncAccountingCalendarV1(AsyncApiGroup):
    """Calendário Contábil (/api/ctb/v1)."""

    api_id = "accounting_calendar_v1"
    base_path = "/api/ctb/v1"

    async def list_accounting_calendar(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Cadastro do Calendário Contábil

        GET /AccountingCalendar; operationId=getAccountingCalendar; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.accounting_calendar_v1.PagedItems
        """
        return await self._request(
            "accounting_calendar_v1.list_accounting_calendar",
            "GET",
            "/AccountingCalendar",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_accounting_calendar(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Incluir um Calendário Contábil

        POST /AccountingCalendar; operationId=postAccountingCalendar; Protheus >= 12.1.21

        Incluir um Calendário Contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.accounting_calendar_v1.PagedItems
        Request model: protheus.models.accounting_calendar_v1.BusinessContentType
        """
        return await self._request(
            "accounting_calendar_v1.create_accounting_calendar",
            "POST",
            "/AccountingCalendar",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_accounting_calendar_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Calendário Contábil específico de acordo com a chave de pesquisa

        GET /AccountingCalendar/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a Calendário Contábil de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código do Calendário + Ano de Exercicío + Periodo

        Response model: protheus.models.accounting_calendar_v1.BusinessContentType
        """
        return await self._request(
            "accounting_calendar_v1.get_accounting_calendar_by_internal_id",
            "GET",
            "/AccountingCalendar/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_accounting_calendar_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Calendário Contábil

        PUT /AccountingCalendar/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o Calendário Contábil conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.accounting_calendar_v1.BusinessContentType
        Request model: protheus.models.accounting_calendar_v1.BusinessContentType
        """
        return await self._request(
            "accounting_calendar_v1.update_accounting_calendar_by_internal_id",
            "PUT",
            "/AccountingCalendar/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_accounting_calendar_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Calendário Contábil

        DELETE /AccountingCalendar/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Calendário Contábil conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parametros Authorization e Fields
        """
        return await self._request(
            "accounting_calendar_v1.delete_accounting_calendar_by_internal_id",
            "DELETE",
            "/AccountingCalendar/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
