"""Motivos de Refugo — generated from WasteReason_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class WasteReason(BaseModel):
    code: str | None = Field(None, alias="Code", description="Código Refugo", max_length=8)
    description: str | None = Field(None, alias="Description", description="Descrição Refugo", max_length=40)
    is_rework: bool | None = Field(None, alias="IsRework", description="Retrabalho")
    is_scrap_material: bool | None = Field(None, alias="IsScrapMaterial", description="Refugo Material")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedWasteReasons(Paging):
    items: list[WasteReason] | None = None
