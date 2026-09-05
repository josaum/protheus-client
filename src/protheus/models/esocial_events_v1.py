"""Lista de eventos — generated from EsocialEvents_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListEvents(BaseModel):
    event_code: str = Field(..., alias="eventCode", description="Evento", examples=["S-1010"], max_length=10)
    event_description: str = Field(
        ..., alias="eventDescription", description="Descrição do Evento.", examples=["Tabela de Rubrica"], max_length=20
    )
    permission_event: bool = Field(..., alias="permissionEvent", description="Permissão do Evento.", examples=["true"])


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
    items: list[ListEvents] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
