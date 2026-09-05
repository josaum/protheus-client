"""Lista de filiais do grupo de empresas — generated from TSIBranches_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class ListBranches(BaseModel):
    branch_code: str = Field(..., alias="branchCode", description="Código da filial", examples=["D MG 01"])
    branch_description__: str = Field(
        ..., alias="branchDescription  ", description="Nome da filial", examples=["Filial BELO HOR"]
    )


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class Branches(BaseModel):
    branches: list[ListBranches] | None = None
