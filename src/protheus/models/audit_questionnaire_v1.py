"""Questionário de Auditoria — generated from AuditQuestionnaire_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class UseOption(StrEnum):
    field_1 = "1"
    field_2 = "2"


class AuditQuestType(BaseModel):
    company_id: str | None = Field(None, alias="companyId", description="Empresa", max_length=3)
    branch_id: str | None = Field(None, alias="branchId", description="Filial", examples=["D MG 01"])
    checklist: str | None = Field(None, description="Número do Checklist", le=6)
    revision: str | None = Field(None, description="Revisão do Checklist", max_length=2)
    topic: str | None = Field(None, description="Topico do Checklist", max_length=10)
    question_number: str | None = Field(None, alias="questionNumber", description="Número da Questão", max_length=3)
    question_text: str | None = Field(None, alias="questionText", description="Texto da Questão")
    observations: str | None = Field(None, description="Observações")
    requirements: str | None = Field(None, description="Requisitos")
    init_range: float | None = Field(None, alias="initRange", description="Faixa Inicial")
    fin_range: float | None = Field(None, alias="finRange", description="Faixa Final")
    last_revis: date | None = Field(None, alias="lastRevis", description="Ultima Revisão")
    question_value: float | None = Field(None, alias="questionValue", description="Peso da Questão")
    use_option: UseOption | None = Field(None, alias="useOption", description="Usa Alternativa (1-Sim/2-Não)")
    internal_id: str | None = Field(None, alias="internalId", description="Chave do Questionário de Auditoria")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedAuditQuest(Paging):
    items: list[AuditQuestType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
