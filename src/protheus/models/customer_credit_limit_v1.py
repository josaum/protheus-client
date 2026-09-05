"""Limite de credito do Cliente — generated from CustomerCreditLimit_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CustomerCreditLimitInfo(BaseModel):
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="Código da Empresa", examples=["D "]
    )
    customer_internal_id: str | None = Field(
        None, alias="CustomerInternalId", description="Código interno da Cliente no ERP", examples=["D MG    00000101"]
    )
    description: str | None = Field(
        None, alias="Description", description="Campo informativo", examples=["Saldo disponivel do Cliente"]
    )
    document_type: str | None = Field(None, alias="DocumentType", description="Tipo do Documento", examples=[""])
    limit_date: AwareDatetime | None = Field(
        None, alias="LimitDate", description="Vencimento do Lim. Credit", examples=["1900-01-01T12:00:00Z"]
    )
    total_credit_limit: float | None = Field(
        None,
        alias="TotalCreditLimit",
        description="Total de limite de crédito concedido ao cliente",
        examples=[6000.61],
        ge=0.0,
        le=999999999.99,
    )
    credit_limit: float | None = Field(
        None,
        alias="CreditLimit",
        description="Limite de Credito do cliente",
        examples=[5162.81],
        ge=0.0,
        le=999999999.99,
    )
    credit_limit_used_by_billing: (
        float | None
    ) = (
        Field(None, alias="CreditLimitUsedByBilling", description="Limite de crédito usado por faturamento", examples=[7000.71], ge=0.0, le=999999999.99)
    )
    credit_limit_used_by_sales_orders: (
        float | None
    ) = (
        Field(None, alias="CreditLimitUsedBySalesOrders", description="Limite de crédito usado por pedidos de venda em aberto/liberados", examples=[8000.81], ge=0.0, le=999999999.99)
    )
    credit_limit_used_by_orders_and_finance: (
        float | None
    ) = (
        Field(None, alias="CreditLimitUsedByOrdersAndFinance", description="Limite de crédito usado por pedidos e financeiro", examples=[9000.92], ge=0.0, le=999999999.99)
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


class CustomerCreditLimit(BaseModel):
    items: list[CustomerCreditLimitInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedCustomerCreditLimit(Paging, CustomerCreditLimit):
    pass
