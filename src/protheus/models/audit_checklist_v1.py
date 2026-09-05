"""Checklist de Auditoria — generated from AuditChecklist_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Accomplished(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class ChecklistType(BaseModel):
    company_id: str | None = Field(None, alias="companyId", description="Empresa", max_length=3)
    branch_id: str | None = Field(None, alias="branchId", description="Filial", examples=["D MG 01"])
    checklist: str | None = Field(None, description="Número do Checklist", le=6)
    revision: str | None = Field(None, description="Revisão do Checklist", le=2)
    internal_id: str | None = Field(None, alias="internalId", description="InternalId do Checklist de Auditoria")
    description: str | None = Field(None, description="Descrição do Checklist", le=50)
    notes: str | None = Field(None, description="Oberservação do Checklist", le=50)
    last_revision: date | None = Field(
        None, alias="lastRevision", description="Data da última revisão", examples=["01-01-2018"]
    )
    accomplished: Accomplished | None = Field(
        None, description="Flag de efetivação \n Tipo: \n    1 - Vigente\n    2 - Pendente\n    3 - Obsoleto\n"
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


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedChecklist(Paging):
    items: list[ChecklistType] | None = None
