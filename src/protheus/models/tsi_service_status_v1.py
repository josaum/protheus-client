"""Consulta o status do serviço — generated from TSIServiceStatus_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Status(BaseModel):
    configured_service: bool = Field(..., alias="configuredService", description="Serviço configurado", examples=[True])
    active_service__: bool = Field(..., alias="activeService  ", description="Serviço ativo", examples=[True])


class Status1(BaseModel):
    status: Status | None = None


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")
