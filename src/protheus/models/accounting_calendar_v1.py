"""Calendário Contábil — generated from AccountingCalendar_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class PeriodStatus(StrEnum):
    field_1 = "1"
    field_4 = "4"


class Code(StrEnum):
    atf001 = "ATF001"
    com001 = "COM001"
    ctb001 = "CTB001"
    est001 = "EST001"
    fin001 = "FIN001"
    fin002 = "FIN002"
    fis001 = "FIS001"
    gct001 = "GCT001"
    gpe001 = "GPE001"
    pls000 = "PLS000"
    pls001 = "PLS001"
    pls002 = "PLS002"
    pls003 = "PLS003"
    pls004 = "PLS004"
    pls005 = "PLS005"
    pls006 = "PLS006"
    pls007 = "PLS007"
    pls008 = "PLS008"
    pls009 = "PLS009"
    pls010 = "PLS010"
    pls011 = "PLS011"
    pls012 = "PLS012"
    tur001 = "TUR001"


class Status(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class ListOfProces(BaseModel):
    code: Code = Field(
        ...,
        alias="Code",
        description="Bloqueio de Processo / ATF001 - Ativo fixo / COM001 - Compras / CTB001 - Contábil / EST001 - Estoque / FIN001 - Financeiro (contas a pagar) / FIN002 - Financeiro (contas a receber) / FIS001 - Livros fiscais / GCT001 - Gestão de contratos / GPE001 - Gestão pessoal / PLS000 - Planos de saúde (geral) / PLS001 - Planos de saúde (liberação para pagamento) / PLS002 - Planos de saúde (recurso de glosa) / PLS003 - Planos de saúde (cancelamento de protocolo) / PLS004 - Planos de saúde (consolidação de coparticipação) / PLS005 - Planos de saúde (recálculo da coparticipação) / PLS006 - Planos de saúde (estorno de pagamento) / PLS007 - Planos de saúde (clone de guias) / PLS008 - Planos de saúde (liberação para pagamento da autorização) / PLS009 - Planos de saúde (acerto de reembolso) / PLS010 - Planos de saúde (cancelamento de reembolso) / PLS011 - Planos de saúde (digitação de contas) / PLS012 - Planos de saúde (reconsolidação individual) / TUR001 - Gestão de viagens e turismo",
    )
    status: Status = Field(
        ...,
        alias="Status",
        description="Status do Processo / 1 - Aberto / 2 - Fechado / 3 - Transportado / 4 - Bloqueado / 5 - Período",
    )
    start_date: date | None = Field(None, alias="StartDate", description="Data Inicial do Período Bloqueio")
    end_date: date | None = Field(None, alias="EndDate", description="Data Final do Período Bloqueio")


class ListOfAccountingPeriod(BaseModel):
    period_code: str = Field(..., alias="PeriodCode", description="Código Periodo Contabil", max_length=2)
    initial_date: date = Field(..., alias="InitialDate", description="Data Inicial do Período")
    final_date: date = Field(..., alias="FinalDate", description="Data Final do Período")
    period_status: PeriodStatus = Field(
        ...,
        alias="PeriodStatus",
        description="Status do Período PROTHEUS: ( 1.Aberto 4.Bloqueado) / 1 - Aberto / 4 - Bloqueado",
    )
    list_of_process: list[ListOfProces] | None = Field(None, alias="ListOfProcess", description="Lista de processos")


class BusinessContentType(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da Empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    calendar_code: str | None = Field(None, alias="CalendarCode", description="Código do Calendário", max_length=3)
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do CalendarCode")
    financial_year: str = Field(..., alias="FinancialYear", description="Exercicio Contábil", max_length=4)
    list_of_accounting_periods: list[ListOfAccountingPeriod] | None = Field(
        None, alias="ListOfAccountingPeriods", description="Periodos Contábeis"
    )


class ListOfProces1(BaseModel):
    code: Code = Field(
        ...,
        alias="Code",
        description="Bloqueio de Processo / ATF001 - Ativo fixo / COM001 - Compras / CTB001 - Contábil / EST001 - Estoque / FIN001 - Financeiro (contas a pagar) / FIN002 - Financeiro (contas a receber) / FIS001 - Livros fiscais / GCT001 - Gestão de contratos / GPE001 - Gestão pessoal / PLS000 - Planos de saúde (geral) / PLS001 - Planos de saúde (liberação para pagamento) / PLS002 - Planos de saúde (recurso de glosa) / PLS003 - Planos de saúde (cancelamento de protocolo) / PLS004 - Planos de saúde (consolidação de coparticipação) / PLS005 - Planos de saúde (recálculo da coparticipação) / PLS006 - Planos de saúde (estorno de pagamento) / PLS007 - Planos de saúde (clone de guias) / PLS008 - Planos de saúde (liberação para pagamento da autorização) / PLS009 - Planos de saúde (acerto de reembolso) / PLS010 - Planos de saúde (cancelamento de reembolso) / PLS011 - Planos de saúde (digitação de contas) / PLS012 - Planos de saúde (reconsolidação individual) / TUR001 - Gestão de viagens e turismo",
    )
    status: Status = Field(
        ...,
        alias="Status",
        description="Status do Processo / 1 - Aberto / 2 - Fechado / 3 - Transportado / 4 - Bloqueado / 5 - Período",
    )
    start_date: date | None = Field(None, alias="StartDate", description="Data Inicial do Período Bloqueio")
    end_date: date | None = Field(None, alias="EndDate", description="Data Final do Período Bloqueio")


class PeriodOfAccountType(BaseModel):
    period_code: str = Field(..., alias="PeriodCode", description="Código Periodo Contabil", max_length=2)
    initial_date: date = Field(..., alias="InitialDate", description="Data Inicial do Período")
    final_date: date = Field(..., alias="FinalDate", description="Data Final do Período")
    period_status: PeriodStatus = Field(
        ...,
        alias="PeriodStatus",
        description="Status do Período PROTHEUS: ( 1.Aberto 4.Bloqueado) / 1 - Aberto / 4 - Bloqueado",
    )
    list_of_process: list[ListOfProces1] | None = Field(None, alias="ListOfProcess", description="Lista de processos")


class ProcessType(BaseModel):
    code: Code = Field(
        ...,
        alias="Code",
        description="Bloqueio de Processo / ATF001 - Ativo fixo / COM001 - Compras / CTB001 - Contábil / EST001 - Estoque / FIN001 - Financeiro (contas a pagar) / FIN002 - Financeiro (contas a receber) / FIS001 - Livros fiscais / GCT001 - Gestão de contratos / GPE001 - Gestão pessoal / PLS000 - Planos de saúde (geral) / PLS001 - Planos de saúde (liberação para pagamento) / PLS002 - Planos de saúde (recurso de glosa) / PLS003 - Planos de saúde (cancelamento de protocolo) / PLS004 - Planos de saúde (consolidação de coparticipação) / PLS005 - Planos de saúde (recálculo da coparticipação) / PLS006 - Planos de saúde (estorno de pagamento) / PLS007 - Planos de saúde (clone de guias) / PLS008 - Planos de saúde (liberação para pagamento da autorização) / PLS009 - Planos de saúde (acerto de reembolso) / PLS010 - Planos de saúde (cancelamento de reembolso) / PLS011 - Planos de saúde (digitação de contas) / PLS012 - Planos de saúde (reconsolidação individual) / TUR001 - Gestão de viagens e turismo",
    )
    status: Status = Field(
        ...,
        alias="Status",
        description="Status do Processo / 1 - Aberto / 2 - Fechado / 3 - Transportado / 4 - Bloqueado / 5 - Período",
    )
    start_date: date | None = Field(None, alias="StartDate", description="Data Inicial do Período Bloqueio")
    end_date: date | None = Field(None, alias="EndDate", description="Data Final do Período Bloqueio")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class AccountingCalendarInfo(BaseModel):
    items: list[BusinessContentType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedItems(Paging, AccountingCalendarInfo):
    pass
