"""Tabela de Preços Varejo — generated from RetailPriceList_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ActiveTablePrice(StrEnum):
    field_1 = "1"
    field_2 = "2"


class PriceListHeaderInfo(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da Filial")
    company_internal_id: str | None = Field(None, alias="companyInternalId", description="Chave completa da Empresa")
    code: str | None = Field(None, description="Código da tabela de preço", max_length=4)
    internal_id: str | None = Field(None, alias="internalId", description="Chave completa da Tabela de Preço")
    company_id: str | None = Field(None, alias="companyId", description="Código da Empresa")
    name: str | None = Field(None, description="Descrição da Tabela", max_length=40)
    initial_date: date | None = Field(
        None, alias="initialDate", description="Data Inicial da Vigência", examples=["20180719"], max_length=10
    )
    final_date: date | None = Field(
        None, alias="finalDate", description="Data Final da Vigência", examples=["20180719"]
    )
    initia_hour: AwareDatetime | None = Field(None, alias="initiaHour", description="Hora Inicial Vigencia")
    final_hour: AwareDatetime | None = Field(None, alias="finalHour", description="Hora Final Vigencia")
    active_table_price: ActiveTablePrice | None = Field(
        None, alias="activeTablePrice", description="Tabela de Preco Ativa?"
    )


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class TypePrice(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class ActiveItemPrice(StrEnum):
    field_1 = "1"
    field_2 = "2"


class PriceListItemInfo(BaseModel):
    company_id: str | None = Field(None, alias="companyId", description="Código da Empresa")
    branch_id: str | None = Field(None, alias="branchId", description="Código da Filial")
    company_internal_id: str | None = Field(None, alias="companyInternalId", description="Chave completa da Empresa")
    code: str | None = Field(None, description="Código da Tabela de Preço")
    internal_id: str | None = Field(None, alias="internalId", description="Chave completa da Tabela de Preço")
    item_list: str | None = Field(None, alias="itemList", description="Item da Tabela", max_length=4)
    item_code: str | None = Field(None, alias="itemCode", description="Código do Produto", max_length=30)
    item_internal_id: str | None = Field(
        None, alias="itemInternalId", description="Chave completa do Item da Tabela de Preço"
    )
    minimum_sales_price: float | None = Field(
        None, alias="minimumSalesPrice", description="Preco mínimo de venda do produto - Valor Sem Frete", max_length=12
    )
    discount_value: float | None = Field(None, alias="discountValue", description="Valor de Desconto", max_length=12)
    discount_factor: float | None = Field(
        None, alias="discountFactor", description="Percentual Acrescimo/Desconto", max_length=11
    )
    item_validity: date | None = Field(
        None, alias="itemValidity", description="Data Vigência do item", examples=["20180719"], max_length=10
    )
    type_price: TypePrice | None = Field(None, alias="typePrice", description="Tipo do Preço")
    active_item_price: ActiveItemPrice | None = Field(None, alias="activeItemPrice", description="Status do Item")


class PagedPriceListHeader(Paging):
    items: list[PriceListHeaderInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedPriceListItem(Paging):
    items: list[PriceListItemInfo] | None = None
