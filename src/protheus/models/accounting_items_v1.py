"""Item Contábil — generated from AccountingItems_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Class(StrEnum):
    field_1 = "1"
    field_2 = "2"


class RegisterSituation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class BusinessContentType(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da Empresa", max_length=3)
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    code: str = Field(..., alias="Code", description="Código do Item Contábil")
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId de Integração")
    description: str | None = Field(None, alias="Description", description="Descrição do item contábil", max_length=100)
    class_: Class | None = Field(
        None, alias="Class", description="Classe (Analítico ou Sintético) / 1 - Sintético / 2 - Analítico"
    )
    register_situation: RegisterSituation | None = Field(
        None,
        alias="RegisterSituation",
        description="Situação do item contábil (Ativa ou Inativa) / 1 - Ativo / 2 - Inativo",
    )
    top_code: str = Field(..., alias="TopCode", description="Código do item contábil superior")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ItemsInfo(BaseModel):
    items: list[BusinessContentType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedItems(Paging, ItemsInfo):
    pass
