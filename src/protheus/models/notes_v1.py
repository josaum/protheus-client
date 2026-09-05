"""Notas — generated from Notes_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Bloqued(StrEnum):
    field_1 = "1"
    field_2 = "2"


class NotesInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa", max_length=3)
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12
    )
    company_internal_id: str | None = Field(None, alias="CompanyInternalId", description="Código da Empresa")
    code: str | None = Field(None, alias="Code", description="Código da Anotação.", examples=["000001"], max_length=6)
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da anotação no ERP", examples=["T1D MG 01 000001"]
    )
    description: str | None = Field(
        None,
        alias="Description",
        description="Descrição da anotação",
        examples=["Anotações do Cliente XPTO"],
        max_length=250,
    )
    resource_type: str | None = Field(
        None, alias="ResourceType", description="Código da Entidade", examples=["SA1"], max_length=9
    )
    resource_code: str | None = Field(
        None, alias="ResourceCode", description="Chave da Entidade", examples=["00000101"], max_length=100
    )
    date: AwareDatetime | None = Field(None, alias="Date", description="Data da Anotação", examples=["20180101"])
    content: str | None = Field(
        None, alias="Content", description="Conteúdo da Anotação", examples=["Anotações necessárias."], max_length=250
    )
    bloqued: Bloqued | None = Field(None, alias="Bloqued", description="Registro Bloqueado", examples=["1"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Notes(BaseModel):
    items: list[NotesInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedNotes(Paging, Notes):
    pass
