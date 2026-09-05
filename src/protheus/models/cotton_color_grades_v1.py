"""CottonColorGrades — generated from CottonColorGrades_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CottonColorGradesType(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave do tipo da classificação.", examples=["99|21-1"]
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código da classificação.", examples=["21-1"])
    description: str | None = Field(
        None, alias="Description", description="Descrição do tipo de classificação.", examples=["STRICT MIDDLING"]
    )
    short_description: str | None = Field(
        None, alias="ShortDescription", description="Descrição abreviada.", examples=["SM"]
    )
    standard_universal_code: str | None = Field(
        None,
        alias="StandardUniversalCode",
        description="Código universal Standard da classificação.",
        examples=["000002"],
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


class PagedCottonColorGrades(Paging):
    items: list[CottonColorGradesType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
