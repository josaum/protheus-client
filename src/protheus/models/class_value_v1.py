"""Classe de Valor — generated from ClassValue_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Class(StrEnum):
    field_1 = "1"
    field_2 = "2"


class RegisterSituation(StrEnum):
    active = "Active"
    inactive = "Inactive"


class BusinessContentType(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da Empresa", max_length=3)
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    code: str = Field(..., alias="Code", description="Código da Classe de Valor")
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId de Integração")
    name: str | None = Field(None, alias="Name", description="Descrição da Classe de Valor", max_length=100)
    class_: Class | None = Field(
        None, alias="Class", description="Classe (Analítico ou Sintético) / 1 - Sintético / 2 - Analítico"
    )
    register_situation: RegisterSituation | None = Field(
        None, alias="RegisterSituation", description="Situação da Classe de Valor (Ativa ou Inativa)"
    )
    top_code: str | None = Field(None, alias="TopCode", description="Código da classe de valor superior")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ClassValueInfo(BaseModel):
    items: list[BusinessContentType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedItems(Paging, ClassValueInfo):
    pass
