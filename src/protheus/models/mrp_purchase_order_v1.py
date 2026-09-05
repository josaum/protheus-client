"""Solicitação de Compra do MRP — generated from MRPPurchaseOrder_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"


class MRPPurchaseOrderBase(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    code: str | None = Field(None, description="Código da solicitação de compra", max_length=200)
    purchase: str | None = Field(None, description="Número da solicitação de compra", max_length=6)
    sequence: str | None = Field(None, description="Sequência da solicitação de compra", max_length=4)
    product: str | None = Field(None, description="Produto da solicitação de compra", max_length=90)
    production_order: str | None = Field(
        None, alias="productionOrder", description="Ordem de produção que gerou a solicitação de compra", max_length=14
    )
    delivery_date: date | None = Field(
        None, alias="deliveryDate", description="Data de entrega da solicitação de compra"
    )
    quantity: float | None = Field(None, description="Quantidade da solicitação de compra")
    received_quantity: float | None = Field(
        None, alias="receivedQuantity", description="Quantidade recebida da solicitação de compra"
    )
    warehouse: str | None = Field(None, description="Armazém da solicitação de compra", max_length=10)
    type: Type | None = Field(None, description="Tipo da solicitação de compra")


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPPurchaseOrderBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPPurchaseOrder(BaseModel):
    items: list[MRPPurchaseOrderBase] | None = None


class ListOfMessages(Paging):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPPurchaseOrder(Paging, ListOfMRPPurchaseOrder):
    pass


class MRPPurchaseOrderMultiple(ListOfMRPPurchaseOrder, ListOfMessages):
    pass
