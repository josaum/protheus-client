"""Processo de Venda — generated from SalesProcess_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class RegisterSituation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class Notify(StrEnum):
    field_1 = "1"
    field_2 = "2"


class FinancialEvaluation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ProspectEvaluation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ListofStages(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "])
    stage_internal_id: str | None = Field(
        None, alias="StageInternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 000001000001"]
    )
    stage_id: str | None = Field(None, alias="StageId", description="Estágio do Processo de Venda", examples=["000001"])
    stage_description: str | None = Field(
        None, alias="StageDescription", description="Descrição do Estágio do Processo de Venda", examples=["Descrição"]
    )
    contribute: float | None = Field(
        None, alias="Contribute", description="Contrinuição em %", examples=[1], ge=1.0, le=100.0
    )
    notify: Notify | None = Field(None, alias="Notify", description="Notifica responsável: 1=Sim;2=Não", examples=["1"])
    action: str | None = Field(None, alias="Action", description="Ação executada", examples=["Função()"])
    financial_evaluation: FinancialEvaluation | None = Field(
        None, alias="FinancialEvaluation", description="Realiza avaliação financeira: 1=Sim;2=Não", examples=["1"]
    )
    value_overdue: float | None = Field(
        None, alias="ValueOverdue", description="Valor limite para avaliação", examples=[1000], ge=0.0, le=999999999.99
    )
    days_overdue: float | None = Field(
        None, alias="DaysOverdue", description="Valor limite para avaliação", examples=[1], ge=0.0, le=999.0
    )
    prospect_evaluation: ProspectEvaluation | None = Field(
        None, alias="ProspectEvaluation", description="Avalia crédito para prospect: 1=Sim;2=Não", examples=["1"]
    )
    duration_days: float | None = Field(
        None, alias="DurationDays", description="Dias de duração do estágio", examples=[1], ge=0.0, le=999.0
    )
    duration_hours: str | None = Field(
        None, alias="DurationHours", description="Horas de duração do estágio", examples=["00:00"]
    )


class Operation(StrEnum):
    field_1 = "1"
    field_3 = "3"


class Action(StrEnum):
    field_1 = "1"
    field_3 = "3"


class ListofRules(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "])
    rule_internal_id: str | None = Field(
        None, alias="RuleInternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 00000101"]
    )
    rule_id: str | None = Field(None, alias="RuleId", description="Regra do Processo de Venda", examples=["01"])
    operation: Operation | None = Field(
        None, alias="Operation", description="Código da operação: 1=Inclusão;2=Alteração;3=Exclusão", examples=["1"]
    )
    event: str | None = Field(None, alias="Event", description="Código do evento", examples=["000001"])
    action: Action | None = Field(
        None,
        alias="Action",
        description="Código da ação: 1=Avança estágio;2=Vai para estágio;3=Retrocede estágio",
        examples=["1"],
    )
    stage: str | None = Field(None, alias="Stage", description="Estágio do processo", examples=["000001"])


class SalesProcessInfo(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "])
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="Código da Empresa", examples=["T1D MG 01 000001"]
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 000001"]
    )
    code: str | None = Field(None, alias="Code", description="Código do Processo de Venda", examples=["000001"])
    description: str | None = Field(
        None,
        alias="Description",
        description="Descrição do Processo de Venda",
        examples=["Processo de Venda Ex CO"],
        max_length=30,
    )
    register_situation: RegisterSituation | None = Field(
        None, alias="RegisterSituation", description="Status do registro: 1=Inativo;2=Ativo", examples=["1"]
    )
    listof_stages: list[list[Any] | ListofStages] | None = Field(
        None, alias="ListofStages", description="Lista dos Estágios"
    )
    listof_rules: list[list[Any] | ListofRules] | None = Field(
        None, alias="ListofRules", description="Lista das Regras"
    )


class StagesInfo(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "])
    stage_internal_id: str | None = Field(
        None, alias="StageInternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 000001000001"]
    )
    stage_id: str | None = Field(None, alias="StageId", description="Estágio do Processo de Venda", examples=["000001"])
    stage_description: str | None = Field(
        None, alias="StageDescription", description="Descrição do Estágio do Processo de Venda", examples=["Descrição"]
    )
    contribute: float | None = Field(
        None, alias="Contribute", description="Contrinuição em %", examples=[1], ge=1.0, le=100.0
    )
    notify: Notify | None = Field(None, alias="Notify", description="Notifica responsável: 1=Sim;2=Não", examples=["1"])
    action: str | None = Field(None, alias="Action", description="Ação executada", examples=["Função()"])
    financial_evaluation: FinancialEvaluation | None = Field(
        None, alias="FinancialEvaluation", description="Realiza avaliação financeira: 1=Sim;2=Não", examples=["1"]
    )
    value_overdue: float | None = Field(
        None, alias="ValueOverdue", description="Valor limite para avaliação", examples=[1000], ge=0.0, le=999999999.99
    )
    days_overdue: float | None = Field(
        None, alias="DaysOverdue", description="Valor limite para avaliação", examples=[1], ge=0.0, le=999.0
    )
    prospect_evaluation: ProspectEvaluation | None = Field(
        None, alias="ProspectEvaluation", description="Avalia crédito para prospect: 1=Sim;2=Não", examples=["1"]
    )
    duration_days: float | None = Field(
        None, alias="DurationDays", description="Dias de duração do estágio", examples=[1], ge=0.0, le=999.0
    )
    duration_hours: str | None = Field(
        None, alias="DurationHours", description="Horas de duração do estágio", examples=["00:00"]
    )


class RulesInfo(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "])
    rule_internal_id: str | None = Field(
        None, alias="RuleInternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 00000101"]
    )
    rule_id: str | None = Field(None, alias="RuleId", description="Regra do Processo de Venda", examples=["01"])
    operation: Operation | None = Field(
        None, alias="Operation", description="Código da operação: 1=Inclusão;2=Alteração;3=Exclusão", examples=["1"]
    )
    event: str | None = Field(None, alias="Event", description="Código do evento", examples=["000001"])
    action: Action | None = Field(
        None,
        alias="Action",
        description="Código da ação: 1=Avança estágio;2=Vai para estágio;3=Retrocede estágio",
        examples=["1"],
    )
    stage: str | None = Field(None, alias="Stage", description="Estágio do processo", examples=["000001"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Stages(BaseModel):
    items: list[StagesInfo] | None = None


class Rules(BaseModel):
    items: list[RulesInfo] | None = None


class SalesProcess(BaseModel):
    items: list[SalesProcessInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedStages(Paging, Stages):
    pass


class PagedRules(Paging, Rules):
    pass


class PagedSalesProcess(Paging, SalesProcess):
    pass
