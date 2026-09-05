"""Treadmills — generated from Treadmills_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class TreadmillsType(BaseModel):
    internal_id: str | None = Field(None, alias="InternalId", description="Chave da esteira", examples=["99|000031"])
    source_branch: str | None = Field(None, alias="SourceBranch", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código da Esteira'", examples=["000001"])
    description: str | None = Field(
        None, alias="Description", description="Descrição da Esteira", examples=["Esteira Belo Horizonte"]
    )
    cotton_gin: str | None = Field(
        None, alias="CottonGin", description="Código da unidade de beneficiamento", examples=["01"]
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


class PagedTreadmills(Paging):
    items: list[TreadmillsType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
