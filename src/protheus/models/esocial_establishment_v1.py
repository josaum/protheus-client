"""S-1005 Estabelecimentos do eSocial — generated from EsocialEstablishment_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListEstablishment(BaseModel):
    registration_type__: str = Field(
        ...,
        alias="registrationType  ",
        description="Tipo de Inscrição (1 - CNPJ , 2 - CPF, 3 - CAEPF,  4 - CNO)",
        examples=["1"],
        max_length=1,
    )
    registration_number__: str = Field(
        ...,
        alias="registrationNumber  ",
        description="Número do de Inscrição do Estabelecimento",
        examples=["07.363.764/0002-71"],
        max_length=60,
    )
    description__: str = Field(
        ...,
        alias="description  ",
        description="Descrição do Estabelecimento",
        examples=["Pão de Açucar - Matriz RJ"],
        max_length=60,
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
    items: list[ListEstablishment] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
