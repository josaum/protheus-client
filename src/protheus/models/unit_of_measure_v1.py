"""Unidade de Medida — generated from UnitOfMeasure_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class UnitOfMeasureInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa da empresa"
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId de Integração para o Grupo de Produto"
    )
    code: str | None = Field(None, alias="Code", description="Unidade de Medida")
    description: Any | None = Field(None, alias="Description", description="Descricao da Unidade de Medida")
    short_name: Any | None = Field(None, alias="ShortName", description="Descricao da Unidade de Medida")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedUnitOfMeasure(Paging):
    items: list[UnitOfMeasureInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
