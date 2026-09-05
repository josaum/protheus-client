"""Chaves de configuracao de stages — generated from DiscoveryKeys_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class DiscoveryKeys(BaseModel):
    type: str | None = Field(None, description="Key data type", examples=["boolean"], max_length=1)
    name: str | None = Field(None, description="Key name 2", examples=["STAGECFG"], max_length=20)
    default: str | None = Field(None, description="Key default value", examples=["true"], max_length=30)
    description: str | None = Field(
        None,
        description="Key description",
        examples=["Acesso às operações tradicionais do configurador"],
        max_length=30,
    )
    display: str | None = Field(
        None, description="Texto para interface", examples=["Permite acesso às operações tradicionais do configurador?"]
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


class PagedDiscoveryKeys(Paging):
    items: list[DiscoveryKeys] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
