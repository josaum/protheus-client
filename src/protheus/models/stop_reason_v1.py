"""Motivo de Parada — generated from StopReason_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class StopReason(BaseModel):
    id: str | None = Field(None, alias="Id", description="id")
    code: str | None = Field(None, alias="Code", description="Código Motivo Parada", max_length=10)
    description: str | None = Field(None, alias="Description", description="Descrição Parada", max_length=40)
    is_efficiency: bool | None = Field(None, alias="IsEfficiency", description="Altera Eficiência")
    is_email_equipment: bool | None = Field(None, alias="IsEmailEquipment", description="E-mail Planejador")
    is_service_request: bool | None = Field(None, alias="IsServiceRequest", description="Emite Solicitação Serviço")
    is_setup: bool | None = Field(None, alias="IsSetup", description="Parada Setup")


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


class PagedStopReasons(Paging):
    items: list[StopReason] | None = None
