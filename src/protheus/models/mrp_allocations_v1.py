"""Empenhos da Produção MRP — generated from MRPAllocations_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPAllocationsBase(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    code: str | None = Field(None, description="Código do empenho da ordem de produção", max_length=200)
    product: str | None = Field(None, description="Produto do empenho", max_length=90)
    production_order: str | None = Field(None, alias="productionOrder", description="Ordem de produção", max_length=14)
    production_order_orig: str | None = Field(
        None, alias="productionOrderOrig", description="Ordem de produção origem", max_length=14
    )
    allocation_date: date | None = Field(None, alias="allocationDate", description="Data do Empenho")
    sequence: str | None = Field(None, description="Sequência do produto", max_length=3)
    quantity: float | None = Field(None, description="Quantidade do Empenho")
    suspended_quantity: float | None = Field(
        None, alias="suspendedQuantity", description="Quantidade Suspensa do Empenho"
    )
    warehouse: str | None = Field(None, description="Armazém de Consumo do Empenho", max_length=10)


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPAllocationsBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPAllocations(Paging):
    items: list[MRPAllocationsBase] | None = None


class ListOfMessages(Paging):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPAllocations(ListOfMRPAllocations, Paging):
    pass


class MRPAllocationsMultiple(ListOfMRPAllocations, ListOfMessages):
    pass
