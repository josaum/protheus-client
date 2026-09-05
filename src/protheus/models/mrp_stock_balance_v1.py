"""Estoque do MRP — generated from MRPStockBalance_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPStockBalanceBase(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    code: str | None = Field(None, description="Código do saldo em estoque do MRP", max_length=200)
    product: str | None = Field(None, description="Código do Produto", max_length=90)
    warehouse: str | None = Field(None, description="Armazém do estoque", max_length=10)
    lot: str | None = Field(None, description="Lote do saldo em estoque do MRP", max_length=10)
    sublot: str | None = Field(None, description="Sublote do saldo em estoque do MRP", max_length=6)
    expiration_date: date | None = Field(None, alias="expirationDate", description="Data de validade do estoque do MRP")
    available_quantity: float | None = Field(
        None, alias="availableQuantity", description="Quantidade disponível em estoque no MRP"
    )
    consigned_out: float | None = Field(None, alias="consignedOut", description="Quantidade em terceiro")
    consigned_in: float | None = Field(None, alias="consignedIn", description="Quantidade de terceiro")
    unavailable_quantity: float | None = Field(
        None, alias="unavailableQuantity", description="Quantidade indisponível em estoque no MRP"
    )
    quality_control_balance: float | None = Field(
        None, alias="qualityControlBalance", description="Saldo em Controle de Qualidade"
    )
    blocked_balance: float | None = Field(None, alias="blockedBalance", description="Saldo bloqueado")


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPStockBalanceBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class MRPStockBalanceBaseClear(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Código do Produto", max_length=90)
    warehouse: str | None = Field(None, description="Armazém do estoque", max_length=10)


class MessageBaseClear(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPStockBalanceBaseClear | None = Field(None, alias="detailedMessage")


class ListOfMRPStockBalance(BaseModel):
    items: list[MRPStockBalanceBase] | None = None


class ListOfMessages(Paging):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class ListOfMRPStockBalanceClear(BaseModel):
    items: list[MRPStockBalanceBaseClear] | None = None


class ListOfMessagesClear(Paging):
    field_messages: list[MessageBaseClear] | None = Field(None, alias="_messages")


class PagedMRPStockBalance(Paging, ListOfMRPStockBalance):
    pass


class MRPStockBalanceMultiple(ListOfMRPStockBalance, ListOfMessages):
    pass


class MRPStockBalanceMultipleClear(ListOfMRPStockBalanceClear, ListOfMessagesClear):
    pass
