"""DiscoveryStages — generated from DiscoveryStages_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class DiscoveryStageType(BaseModel):
    discoverystageid: str | None = Field(None, description="Internal ID", max_length=5)
    description: str | None = Field(None, description="Descrição do Stage", examples=["Desenvolvimento"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedDiscoveryStages(Paging):
    items: list[DiscoveryStageType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
