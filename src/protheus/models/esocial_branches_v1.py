"""Filiais — generated from EsocialBranches_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListBranches(BaseModel):
    branch_code: str = Field(
        ..., alias="branchCode", description="Código da filial", examples=["D MG 01"], max_length=10
    )
    branch_description: str = Field(
        ..., alias="branchDescription", description="Descrição da Filial", examples=["Belo Horizonte"], max_length=20
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


class PagedItens(Paging):
    items: list[ListBranches] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
