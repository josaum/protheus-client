"""CottonGins — generated from CottonGins_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CottonGinsType(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave da unidade de beneficiamento", examples=["99|01"]
    )
    source_branch: str | None = Field(None, alias="SourceBranch", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código da unidade de beneficiamento'", examples=["01"])
    description: str | None = Field(
        None, alias="Description", description="Nome da unidade de beneficiamento", examples=["Esteira Belo Horizonte"]
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


class PagedBranches(Paging):
    items: list[CottonGinsType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
