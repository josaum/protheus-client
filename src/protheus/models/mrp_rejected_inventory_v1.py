"""Estoque Rejeitado do MRP — generated from MRPRejectedInventory_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPRejectedInventoryBase(BaseModel):
    code: str | None = Field(None, description="Código do estoque rejeitado", max_length=200)
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Código do produto", max_length=90)
    quantity: float | None = Field(None, description="Quantidade total no estoque rejeitado")
    warehouse: str | None = Field(None, description="Armazém do estoque", max_length=10)
    invoice_date: date | None = Field(None, alias="invoiceDate", description="Data de validade do estoque rejeitado")
    returned_quantity: float | None = Field(
        None, alias="returnedQuantity", description="Quantidade indisponível em estoque no MRP"
    )


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPRejectedInventoryBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class MRPRejectedInventoryBaseClear(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Código do Produto", max_length=90)
    warehouse: str | None = Field(None, description="Armazém do estoque", max_length=10)


class MessageBaseClear(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPRejectedInventoryBaseClear | None = Field(None, alias="detailedMessage")


class ListOfMRPRejectedInventory(BaseModel):
    items: list[MRPRejectedInventoryBase] | None = None


class ListOfMessages(Paging):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class ListOfMRPRejectedInventoryClear(BaseModel):
    items: list[MRPRejectedInventoryBaseClear] | None = None


class ListOfMessagesClear(Paging):
    field_messages: list[MessageBaseClear] | None = Field(None, alias="_messages")


class PagedMRPRejectedInventory(Paging, ListOfMRPRejectedInventory):
    pass


class MRPRejectedInventoryMultiple(ListOfMRPRejectedInventory, ListOfMessages):
    pass


class MRPRejectedInventoryMultipleClear(ListOfMRPRejectedInventoryClear, ListOfMessagesClear):
    pass
