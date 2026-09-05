"""Módulos do sistema — generated from SystemModules_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class BusinessContentType(BaseModel):
    id: str | None = Field(None, description="Código que identifica o recurso.")
    name: str | None = Field(None, description="Nome do módulo.")
    description: str | None = Field(None, description="Descrição do módulo.")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedBusiness(Paging):
    items: list[BusinessContentType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
