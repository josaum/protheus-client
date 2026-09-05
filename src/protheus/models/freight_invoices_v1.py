"""FreightInvoices — generated from FreightInvoices_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ApprovalStatus(StrEnum):
    field_1___recebida = "1 - Recebida"
    field_2___bloqueada = "2 - Bloqueada"
    field_3___aprovada_sistema = "3 - Aprovada Sistema"
    field_4___aprovada_usuário = "4 - Aprovada Usuário"


class FinancialStatus(StrEnum):
    field_1___não_enviada = "1 - Não Enviada"
    field_2___pendente = "2 - Pendente"
    field_3___rejeitada = "3 - Rejeitada"
    field_4___atualizada = "4 - Atualizada"
    field_5___pendente_desatualização = "5 - Pendente Desatualização"


class FreightInvoicesType(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="Chave da fatura de frete.",
        examples=["D MG 01 |77785         |1    |F201909133      |20190913"],
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["D MG 01 "])
    issuer_code: str | None = Field(None, alias="IssuerCode", description="Emissor do Documento.", examples=["77785"])
    invoice_series: str | None = Field(None, alias="InvoiceSeries", description="Série da fatura.", examples=["001"])
    invoice_number: str | None = Field(None, alias="InvoiceNumber", description="Numero da fatura.", examples=["001"])
    issue_date: str | None = Field(None, alias="IssueDate", description="Data de Emissão.", examples=["20191010"])
    invoice_gross_value: str | None = Field(
        None, alias="InvoiceGrossValue", description="Valor da Fatura.", examples=["48,00"], ge=0, le=999999999.99
    )
    discount_value: str | None = Field(
        None, alias="DiscountValue", description="Valor do Desconto.", examples=["48,00"], ge=0, le=999999999.99
    )
    compensatory_discount: str | None = Field(
        None,
        alias="CompensatoryDiscount",
        description="Desconto Indenizatório.",
        examples=["48,00"],
        ge=0,
        le=999999999.99,
    )
    document_serie: str | None = Field(None, alias="DocumentSerie", description="Série do Documento.", examples=["001"])
    document_number: str | None = Field(
        None, alias="DocumentNumber", description="Número do Documento.", examples=["9999999"]
    )
    electronic_access_key: str | None = Field(
        None,
        alias="ElectronicAccessKey",
        description="Chave do CT-e.",
        examples=["421405354489484514654546545645615615616589400011"],
    )
    icms_value: str | None = Field(
        None, alias="ICMSValue", description="Valor de ICMS.", examples=["42,00"], ge=0, le=999999999.99
    )
    withheld_icms_value: str | None = Field(
        None, alias="WithheldICMSValue", description="Valor de ICMS Retido.", examples=["42,00"], ge=0, le=999999999.99
    )
    iss_value: str | None = Field(
        None, alias="ISSValue", description="Valor de ISS.", examples=["42,00"], ge=0, le=999999999.99
    )
    withheld_iss_value: str | None = Field(
        None, alias="WithheldISSValue", description="Valor de ISS Retido.", examples=["42,00"], ge=0, le=999999999.99
    )
    interest_value: str | None = Field(
        None, alias="InterestValue", description="Valor de Juros.", examples=["42,00"], ge=0, le=999999999.99
    )
    input_date: str | None = Field(None, alias="InputDate", description="Data de Criação.", examples=["20191010"])
    expiration_date: str | None = Field(
        None, alias="ExpirationDate", description="Data de Vencimento.", examples=["20191010"]
    )
    approval_status: ApprovalStatus | None = Field(
        None, alias="ApprovalStatus", description="Situação Aprovação.", examples=["1"]
    )
    approval_date: str | None = Field(
        None, alias="ApprovalDate", description="Data de Aprovação.", examples=["20191010"]
    )
    approval_time: str | None = Field(None, alias="ApprovalTime", description="Hora de Aprovação.", examples=["10:25"])
    approval_user: str | None = Field(
        None, alias="ApprovalUser", description="Usuário de Aprovação.", examples=["admin"]
    )
    blockage_date: str | None = Field(
        None, alias="BlockageDate", description="Data de Bloqueio.", examples=["20191010"]
    )
    blockage_time: str | None = Field(None, alias="BlockageTime", description="Hora de Bloqueio.", examples=["10:25"])
    input_user: str | None = Field(None, alias="InputUser", description="Usuário de Entrada.", examples=["admin"])
    blockage_user: str | None = Field(
        None, alias="BlockageUser", description="Usuário de Bloqueio.", examples=["admin"]
    )
    blockage_reason: str | None = Field(
        None, alias="BlockageReason", description="Motivo de Bloqueio.", examples=["Fatura bloqueada"]
    )
    note: str | None = Field(
        None,
        alias="Note",
        description="Observação.",
        examples=["Total de descontos R$ 150,00 maior que o valor Fatura R$ 149,00."],
    )
    withheld_icms_tax_code: str | None = Field(
        None, alias="WithheldICMSTaxCode", description="Código Imposto ICMS Ret.", examples=["1005"]
    )
    withheld_icms_tax_category: (
        str | None
    ) = Field(None, alias="WithheldICMSTaxCategory", description="Class Imposto ICMS Ret.", examples=["1005"])
    withheld_iss_tax_code: str | None = Field(
        None, alias="WithheldISSTaxCode", description="Código Imposto ISS Ret.", examples=["1005"]
    )
    withheld_iss_tax_category: (
        str | None
    ) = Field(None, alias="WithheldISSTaxCategory", description="Classificação Imposto ISS Retido.", examples=["A"])
    withheld_iss_tax_catgory: str | None = Field(
        None, alias="WithheldISSTaxCatgory", description="Class Imposto ISS Ret.", examples=["1005"]
    )
    financial_date: str | None = Field(
        None, alias="FinancialDate", description="Data envio ao Financeiro.", examples=["20191010"]
    )
    financial_time: str | None = Field(
        None, alias="FinancialTime", description="Hora envio ao Financeiro.", examples=["10:25"]
    )
    financial_status: FinancialStatus | None = Field(
        None, alias="FinancialStatus", description="Situação no Financeiro.", examples=[1]
    )
    financial_user: str | None = Field(
        None, alias="FinancialUser", description="Usuário Envio ao Financeiro.", examples=["admin"]
    )
    financial_rejection_reason: (
        str | None
    ) = (
        Field(None, alias="FinancialRejectionReason", description="Motivo Rejeição Financeiro.", examples=["Fornecedor não cadastrado no Protheus."])
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


class PagedFreightInvoices(Paging):
    items: list[FreightInvoicesType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
