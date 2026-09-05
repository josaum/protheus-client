"""FreightAccountingBatches — generated from FreightAccountingBatches_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class FinancialStatus(StrEnum):
    field_1___não_enviado = "1 - Não Enviado"
    field_2___pendente = "2 - Pendente"
    field_3___rejeitado = "3 - Rejeitado"
    field_4___atualizado = "4 - Atualizado"
    field_5___pendente_estorno = "5 - Pendente Estorno"
    field_6___estornado = "6 - Estornado"
    field_7___pendente_estorno_parcial = "7 - Pendente Estorno Parcial"
    field_8___estornado_parcial = "8 - Estornado Parcial"


class EntryType(StrEnum):
    field_1___db = "1 - DB"
    field_2___cr = "2 - CR"


class AccountingProvisionEntry(BaseModel):
    cost_center: str | None = Field(None, alias="CostCenter", description="Centro Custo Debito", examples=["9999999"])
    ledger_account: str | None = Field(None, alias="LedgerAccount", description="Conta Contabil", examples=["4132301"])
    business_unit: str | None = Field(None, alias="BusinessUnit", description="Unidade de Negocio.", examples=["001"])
    value_: str | None = Field(
        None, alias="Value ", description="Valor do Lancamento", examples=["30,00"], ge=0, le=999999999.99
    )
    entry_type: EntryType | None = Field(None, alias="EntryType", description="Tipo de Lancamento", examples=["1"])


class FinancialStatus1(StrEnum):
    field_1___não_enviado = "1 - Não Enviado"
    field_2___pendente = "2 - Pendente"
    field_3___rejeitado = "3 - Rejeitado"
    field_4___atualizado = "4 - Atualizado"
    field_5___pendente_desatualização = "5 - Pendente Desatualização"
    field_6___estornado = "6 - Estornado"


class ReversalProvisionSubBatch(BaseModel):
    code: str | None = Field(None, alias="Code", description="Codigo Sublote de Estorno", examples=["99999999"])
    period: str | None = Field(None, alias="Period", description="Periodo", examples=["2019/10"])
    creation_date: str | None = Field(None, alias="CreationDate", description="Data Criacao", examples=["20191010"])
    financial_status: FinancialStatus1 | None = Field(
        None, alias="FinancialStatus", description="Situacao da Integracao", examples=["2"]
    )
    creation_user: str | None = Field(
        None, alias="CreationUser", description="Usuario de Criacao", examples=["Administrador"]
    )


class ReversalEntry(BaseModel):
    entry_date: str | None = Field(None, alias="EntryDate", description="Data do Lançamento", examples=["20191010"])
    cost_center: str | None = Field(None, alias="CostCenter", description="Centro Custo Debito", examples=["9999999"])
    ledger_account: str | None = Field(None, alias="LedgerAccount", description="Conta Contabil", examples=["4132301"])
    business_unit: str | None = Field(None, alias="BusinessUnit", description="Unidade de Negocio.", examples=["001"])
    value: str | None = Field(
        None, alias="Value", description="Valor do Lancamento", examples=["30,00"], ge=0, le=999999999.99
    )
    entry_type: EntryType | None = Field(None, alias="EntryType", description="Tipo de Lancamento", examples=["1"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class AccountingProvisionEntryModel(BaseModel):
    items: list[AccountingProvisionEntry] | None = None


class ReversalProvisionSubBatchModel(BaseModel):
    items: list[ReversalProvisionSubBatch] | None = None


class ReversalEntryModel(BaseModel):
    items: list[ReversalEntry] | None = None


class FreightAccountingBatchesType(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave do lote de provisão.", examples=["99 |00000025"]
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    issuer_code: str | None = Field(None, alias="IssuerCode", description="Emissor do Documento.", examples=["77785"])
    account_lot_code: str | None = Field(
        None, alias="AccountLotCode", description="Codigo do Lote", examples=["00000025"]
    )
    period: str | None = Field(None, alias="Period", description="Periodo", examples=["2019/10"])
    financial_status: FinancialStatus | None = Field(
        None, alias="FinancialStatus", description="Situacao da Integracao", examples=["2"]
    )
    financial_date: str | None = Field(
        None, alias="FinancialDate", description="Data Envio Financeiro", examples=["20191010"]
    )
    financial_rejection_reason: (
        str | None
    ) = Field(None, alias="FinancialRejectionReason", description="Motivo Rejeição Financeiro", examples=["Teste"])
    accounting_provision_entry: (
        AccountingProvisionEntryModel | None
    ) = Field(None, alias="AccountingProvisionEntry", description="Lançamento Provisão Contábil")
    reversal_provision_sub_batch: (
        ReversalProvisionSubBatchModel | None
    ) = Field(None, alias="ReversalProvisionSubBatch", description="Sublote Estorno de Provisão")
    reversal_entry: ReversalEntryModel | None = Field(None, alias="ReversalEntry", description="Lançamento de estornos")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedFreightAccountingBatches(Paging):
    items: list[FreightAccountingBatchesType] | None = None
