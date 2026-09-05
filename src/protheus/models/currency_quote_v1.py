"""Cambio — generated from CurrencyQuote_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date as date_aliased

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListOfCurrencyItem(BaseModel):
    code: int = Field(..., alias="Code", description="Código da moeda (número de 1 a 99)", ge=1, le=99)
    name: str | None = Field(None, alias="Name", description="Nome da moeda (Real, Dólar, Euro...)")
    symbol: str | None = Field(None, alias="Symbol", description="Súmbolo da moeda (R$, US$, €...)")
    quote: float = Field(..., alias="Quote", description="Cotação da moeda")


class CurrencyQuoteInfo(BaseModel):
    company_id: str = Field(..., alias="CompanyId", description="Código da Empresa", examples=["T1 "], max_length=3)
    branch_id: str = Field(..., alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12)
    company_internal_id: str = Field(..., alias="CompanyInternalId", description="Identificador da Empresa")
    date: date_aliased = Field(..., alias="Date", description="Data da cotação")
    list_of_currency: list[ListOfCurrencyItem] = Field(
        ..., alias="ListOfCurrency", description="Cotações das moedas", max_length=99
    )


class CurrencyType(BaseModel):
    code: int = Field(..., alias="Code", description="Código da moeda (número de 1 a 99)", ge=1, le=99)
    name: str | None = Field(None, alias="Name", description="Nome da moeda (Real, Dólar, Euro...)")
    symbol: str | None = Field(None, alias="Symbol", description="Súmbolo da moeda (R$, US$, €...)")
    quote: float = Field(..., alias="Quote", description="Cotação da moeda")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class CurrencyQuotes(BaseModel):
    items: list[CurrencyQuoteInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedCurrencyQuote(Paging, CurrencyQuotes):
    pass
