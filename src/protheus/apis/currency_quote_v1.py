"""Cambio — generated from CurrencyQuote_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CurrencyQuoteV1(ApiGroup):
    """Cambio (/api/fin/v1)."""

    api_id = "currency_quote_v1"
    base_path = "/api/fin/v1"

    def list_currency_quotes(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Cotações de Moedas

        GET /CurrencyQuotes; operationId=getCurrencyQuotes; Protheus >= 12.1.21

        Retorna lista completa das Cotações de Moedas

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.currency_quote_v1.PagedCurrencyQuote
        """
        return self._request(
            "currency_quote_v1.list_currency_quotes",
            "GET",
            "/CurrencyQuotes",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_currency_quotes(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Cotações de Moedas

        POST /CurrencyQuotes; operationId=postCurrencyQuotes; Protheus >= 12.1.21

        Inclui cotações de moedas conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        Request model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        """
        return self._request(
            "currency_quote_v1.create_currency_quotes",
            "POST",
            "/CurrencyQuotes",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_currency_quotes_by_date(self, date: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna cotações de uma Data específica de acordo com a chave de pesquisa

        GET /CurrencyQuotes/{Date}; operationId=getDate; Protheus >= 12.1.21

        Retorna cotações de uma Data de acordo com o ID de pesquisa

        TOTVS note: o Date é composto Data da Cotação

        Response model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        """
        return self._request(
            "currency_quote_v1.get_currency_quotes_by_date",
            "GET",
            "/CurrencyQuotes/{Date}",
            path_params={"Date": date},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_currency_quotes_by_date(self, date: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera Cotações de Moedas

        PUT /CurrencyQuotes/{Date}; operationId=putDate; Protheus >= 12.1.21

        Atualiza as cotações por Data conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Date e Fields

        Response model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        Request model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        """
        return self._request(
            "currency_quote_v1.update_currency_quotes_by_date",
            "PUT",
            "/CurrencyQuotes/{Date}",
            path_params={"Date": date},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_currency_quotes_by_date(self, date: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui Cotações de Moedas

        DELETE /CurrencyQuotes/{Date}; operationId=deleteDate; Protheus >= 12.1.21

        Exclui as cotações por Data conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "currency_quote_v1.delete_currency_quotes_by_date",
            "DELETE",
            "/CurrencyQuotes/{Date}",
            path_params={"Date": date},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCurrencyQuoteV1(AsyncApiGroup):
    """Cambio (/api/fin/v1)."""

    api_id = "currency_quote_v1"
    base_path = "/api/fin/v1"

    async def list_currency_quotes(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Cotações de Moedas

        GET /CurrencyQuotes; operationId=getCurrencyQuotes; Protheus >= 12.1.21

        Retorna lista completa das Cotações de Moedas

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.currency_quote_v1.PagedCurrencyQuote
        """
        return await self._request(
            "currency_quote_v1.list_currency_quotes",
            "GET",
            "/CurrencyQuotes",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_currency_quotes(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Cotações de Moedas

        POST /CurrencyQuotes; operationId=postCurrencyQuotes; Protheus >= 12.1.21

        Inclui cotações de moedas conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        Request model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        """
        return await self._request(
            "currency_quote_v1.create_currency_quotes",
            "POST",
            "/CurrencyQuotes",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_currency_quotes_by_date(self, date: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna cotações de uma Data específica de acordo com a chave de pesquisa

        GET /CurrencyQuotes/{Date}; operationId=getDate; Protheus >= 12.1.21

        Retorna cotações de uma Data de acordo com o ID de pesquisa

        TOTVS note: o Date é composto Data da Cotação

        Response model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        """
        return await self._request(
            "currency_quote_v1.get_currency_quotes_by_date",
            "GET",
            "/CurrencyQuotes/{Date}",
            path_params={"Date": date},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_currency_quotes_by_date(self, date: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera Cotações de Moedas

        PUT /CurrencyQuotes/{Date}; operationId=putDate; Protheus >= 12.1.21

        Atualiza as cotações por Data conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, Date e Fields

        Response model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        Request model: protheus.models.currency_quote_v1.CurrencyQuoteInfo
        """
        return await self._request(
            "currency_quote_v1.update_currency_quotes_by_date",
            "PUT",
            "/CurrencyQuotes/{Date}",
            path_params={"Date": date},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_currency_quotes_by_date(self, date: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui Cotações de Moedas

        DELETE /CurrencyQuotes/{Date}; operationId=deleteDate; Protheus >= 12.1.21

        Exclui as cotações por Data conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "currency_quote_v1.delete_currency_quotes_by_date",
            "DELETE",
            "/CurrencyQuotes/{Date}",
            path_params={"Date": date},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
