"""Comissão de Venda — generated from SalesCharge_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class SalesChargeInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da Empresa", max_length=3)
    branch_id: str | None = Field(None, alias="BranchId", description="Filial", examples=["D MG 01"])
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId das informações da empresa"
    )
    internal_id: str | None = Field(None, alias="InternalId", description="Identificador único da Comissão")
    seller_internal_id: str | None = Field(None, alias="SellerInternalId", description="InternalId do Vendedor")
    seller_id: str | None = Field(None, alias="SellerId", description="Código do Vendedor")
    account_receivable_document_internal_id: (
        str | None
    ) = (
        Field(None, alias="AccountReceivableDocumentInternalId", description="InternalId do Título a Receber que originou a comissão")
    )
    account_receivable_document_prefix: (
        str | None
    ) = (
        Field(None, alias="AccountReceivableDocumentPrefix", description="Prefixo do Título a Receber que originou a comissão")
    )
    account_receivable_document_number: (
        str | None
    ) = (
        Field(None, alias="AccountReceivableDocumentNumber", description="Número do Título a Receber que originou a comissão")
    )
    account_receivable_document_parcel: (
        str | None
    ) = (
        Field(None, alias="AccountReceivableDocumentParcel", description="Parcela do Título a Receber que originou a comissão")
    )
    account_receivable_document_type_code: (
        str | None
    ) = (
        Field(None, alias="AccountReceivableDocumentTypeCode", description="Tipo do Título a Receber que originou a comissão")
    )
    customer_vendor_internal_id: (
        str | None
    ) = (
        Field(None, alias="CustomerVendorInternalId", description="Identificador único do Cliente do título a Receber que originou a comissão")
    )
    customer_vendor_code: str | None = Field(
        None, alias="CustomerVendorCode", description="Código do Cliente do título a Receber que originou a comissão"
    )
    customer_vendor_store: str | None = Field(
        None, alias="CustomerVendorStore", description="Loja do Cliente do título a Receber que originou a comissão"
    )
    issue_date: str | None = Field(None, alias="IssueDate", description="Data de Emissão da Comissão")
    base_value: float | None = Field(None, alias="BaseValue", description="Valor Base da Comissão")
    sales_charge_percentage: float | None = Field(
        None, alias="SalesChargePercentage", description="Percentual de comissão sobre valor base"
    )
    value: float | None = Field(None, alias="Value", description="Valor da Comissão")
    due_date: str | None = Field(None, alias="DueDate", description="Data de Vencimento da Comissão")
    currency_internal_id: str | None = Field(
        None, alias="CurrencyInternalId", description="InternalId da Moeda da Comissão"
    )
    currency: str | None = Field(None, alias="Currency", description="Moeda da Comissão")
    hotel_invoice_internal_id: (
        str | None
    ) = Field(None, alias="HotelInvoiceInternalID", description="Identificador único da fatura de hotel")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class SalesCharge(BaseModel):
    sales_charge: list[SalesChargeInfo] | None = Field(None, alias="SalesCharge")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedSalesCharge(Paging, SalesCharge):
    pass
