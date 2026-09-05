"""Endereços — generated from AddressStock_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class AddressStockInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa da empresa"
    )
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId da localização")
    warehouse_code: str | None = Field(None, alias="WarehouseCode", description="Código do Armazém/Depósito")
    location_code: str | None = Field(None, alias="LocationCode", description="Endereço/Localização")
    address_stock_description: (
        str | None
    ) = Field(None, alias="AddressStockDescription", description="Descrição do endereço")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedAddressStock(Paging):
    items: list[AddressStockInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
