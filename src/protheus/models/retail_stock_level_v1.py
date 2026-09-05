"""Saldo em Estoque — generated from RetailStockLevel_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ItemInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da Empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial")
    item_internal_id: str | None = Field(None, alias="ItemInternalId", description="Codigo do Produto")
    current_stock_amount: float | None = Field(None, alias="CurrentStockAmount", description="Saldo Atual")
    warehouse_internal_id: str | None = Field(None, alias="WarehouseInternalID", description="Armazém")
    booked_stock_amount: float | None = Field(None, alias="BookedStockAmount", description="Qtde. Reserva")
    future_stock_amount: float | None = Field(None, alias="FutureStockAmount", description="Qtde. Prevista")
    valueof_current_stock_amount: (
        float | None
    ) = Field(None, alias="ValueofCurrentStockAmount", description="Saldo Atual Valor")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedItems(Paging):
    items: list[ItemInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
