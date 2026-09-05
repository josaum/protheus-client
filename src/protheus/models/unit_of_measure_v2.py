"""Unidade de Medida — generated from UnitOfMeasure_v2_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class BusinessContentType(BaseModel):
    code: str | None = Field(None, alias="Code", description="Código da Unidade de Medida", max_length=6)
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId de Integração")
    description: str | None = Field(None, alias="Description", description="Descrição da Unidade de Medida")
    short_name: str | None = Field(None, alias="ShortName", description="Descrição Abreviada da Unidade de Medida")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
