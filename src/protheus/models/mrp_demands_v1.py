"""Demandas do MRP — generated from MRPDemands_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date as date_aliased
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Source(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_9 = "9"


class Processed(StrEnum):
    field_1 = "1"
    field_2 = "2"


class OptionalItem(BaseModel):
    key: str | None = Field(None, description="Path da estrutura onde houve seleção de Opcionais", max_length=254)
    value: str | None = Field(
        None, description="Grupo e item de opcionais que foram selecionados para o path da estrutura", max_length=100
    )


class MRPDemandBase(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    code: str | None = Field(None, description="Código da demanda", max_length=200)
    date: date_aliased | None = Field(None, description="Data da demanda")
    product: str | None = Field(None, description="Produto da demanda", max_length=90)
    quantity: float | None = Field(None, description="Quantidade da demanda")
    warehouse: str | None = Field(None, description="Armazém da demanda", max_length=10)
    revision: str | None = Field(None, description="Revisão da demanda", max_length=3)
    document: str | None = Field(None, description="Documento da demanda", max_length=30)
    source: Source | None = Field(None, description="Origem da demanda.")
    processed: Processed | None = Field(None, description="Indicador de demanda já processada pelo MRP.")
    optional: list[OptionalItem] | None = Field(None, description="Opcionais da demanda")
    ticket: str | None = Field(None, description="Ticket do processamento do MRP", max_length=6)
    demand_code: str | None = Field(None, alias="demandCode", description="Demanda do MRP", max_length=15)


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPDemandBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPDemand(BaseModel):
    items: list[MRPDemandBase] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPDemands(Paging, ListOfMRPDemand):
    pass


class MRPDemandMultiple(PagedMRPDemands, ListOfMessages):
    pass
