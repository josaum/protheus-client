"""Painel de Auditoria do eSocial — generated from EsocialAudit_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListAudit(BaseModel):
    branch: str = Field(..., description="Código da filial", examples=["D MG 01"], max_length=10)
    event_description: str = Field(
        ..., alias="eventDescription", description="Evento", examples=["S-1200 - Folha de Pagamento"], max_length=20
    )
    type_origin: str = Field(..., alias="typeOrigin", description="Tipo", examples=["Original"], max_length=10)
    ind_apur: str = Field(..., alias="indApur", description="Indicador de Apuração", examples=["Mensal"], max_length=10)
    period_event: str = Field(
        ..., alias="periodEvent", description="Data do Evento", examples=["03/2021"], max_length=10
    )
    cpf: str = Field(..., description="CPF", examples=["111.111.111-11"], max_length=10)
    registration: str = Field(..., description="Matricula", examples=["123456789-00"], max_length=10)
    name: str = Field(..., description="Nome", examples=["Fulano da Silva"], max_length=10)
    period_trans: str = Field(
        ..., alias="periodTrans", description="Data de Transmissão", examples=["15/03/2021"], max_length=10
    )
    period_limit: str = Field(
        ..., alias="periodLimit", description="Data Limite de Transmissão", examples=["20/03/2021"], max_length=10
    )
    receipt: str = Field(..., description="Recibo", examples=["1.2.23145615616"], max_length=20)
    status: str = Field(..., description="Status do evento", examples=["Dentro ou Fora do prazo"], max_length=25)
    rule_description: str = Field(
        ...,
        alias="ruleDescription",
        description="Descrição da regra em qual o evento se enquadra",
        examples=[""],
        max_length=25,
    )
    deadline_description: str = Field(
        ..., alias="deadlineDescription", description="Tempo para envio do evento", examples=[""], max_length=25
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


class ListStatus(BaseModel):
    finished: bool | None = Field(None, description="Finalizado", examples=["true"], max_length=10)
    percent: str | None = Field(None, description="Percentual", examples=["100%"], max_length=20)


class ListAuditValue(BaseModel):
    items: Any | None = Field(None, description="Array com os itens a ser retornado", max_length=20)
    has_next: bool | None = Field(
        None,
        alias="hasNext",
        description="Indica se tem uma página para mostrar",
        examples=["'hasNext': false"],
        max_length=20,
    )


class ListAuditChart(BaseModel):
    transm_in_deadline: float | None = Field(
        None, alias="transmInDeadline", description="Prazo de transmissão", max_length=20
    )
    transm_out_deadline: float | None = Field(
        None, alias="transmOutDeadline", description="Transmissão fora do prazo", max_length=20
    )
    not_transm_in_deadline: float | None = Field(
        None, alias="notTransmInDeadline", description="Não transmitido dentro do prazo", max_length=20
    )
    not_transm_out_deadline: float | None = Field(
        None, alias="notTransmOutDeadline", description="Não transmitido fora do prazo", max_length=20
    )


class PagedItens(Paging):
    items: list[ListAudit] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class StatusItems(Paging):
    items: list[ListStatus] | None = None


class AuditValueItems(Paging):
    items: list[ListAuditValue] | None = None


class ChartValueItems(Paging):
    items: list[ListAuditChart] | None = None
