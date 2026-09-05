"""Ordens de produção do MRP — generated from MRPProductionOrders_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_9 = "9"


class Situation(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class OptionalItem(BaseModel):
    key: str | None = Field(None, description="Path da estrutura onde houve seleção de Opcionais", max_length=254)
    value: str | None = Field(
        None, description="Grupo e item de opcionais que foram selecionados para o path da estrutura", max_length=100
    )


class MRPProductionOrderBase(BaseModel):
    branch_id: str | None = Field(
        None, alias="branchId", description="Código da filial da ordem de produção", max_length=2
    )
    production_order: str | None = Field(
        None, alias="productionOrder", description="Número da ordem de produção", max_length=14
    )
    code: str | None = Field(None, description="Código da ordem de produção", max_length=200)
    product: str | None = Field(None, description="Produto da ordem de produção", max_length=90)
    warehouse: str | None = Field(None, description="Armazém da ordem de produção", max_length=10)
    quantity: float | None = Field(None, description="Quantidade da ordem de produção")
    production_amount: float | None = Field(
        None, alias="productionAmount", description="Quantidade de saldo da ordem de produção"
    )
    start_date: date | None = Field(None, alias="startDate", description="Data de início da ordem de produção")
    delivery_date: date | None = Field(None, alias="deliveryDate", description="Data de entrega da ordem de produção")
    type: Type | None = Field(None, description="Tipo da ordem.")
    situation: Situation | None = Field(None, description="Situação da ordem.")
    optional: list[OptionalItem] | None = Field(None, description="Opcionais da ordem de produção")


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPProductionOrderBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPProductionOrders(BaseModel):
    items: list[MRPProductionOrderBase] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPProductionOrders(Paging, ListOfMRPProductionOrders):
    pass


class MRPProductionOrdersMultiple(PagedMRPProductionOrders, ListOfMessages):
    pass
