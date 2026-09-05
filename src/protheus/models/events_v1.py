"""Eventos — generated from Events_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Status(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"


class ListOfEvent(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId do item da Eventos no ERP", examples="D MG 01 000001GRADE1"
    )
    grade_description: str | None = Field(
        None,
        alias="GradeDescription",
        description="Descrição da grade do evento.",
        examples=["Abertura do evento"],
        max_length=20,
    )
    theme_description: str | None = Field(
        None, alias="ThemeDescription", description="Assunto da atividade.", examples=["Valor agregado"], max_length=40
    )
    initial_time_grade: str | None = Field(
        None, alias="InitialTimeGrade", description="Hora início da grade.", examples=["08:30"], max_length=4
    )
    end_time_grade: str | None = Field(
        None, alias="EndTimeGrade", description="Hora final da grade.", examples=["11:30"], max_length=4
    )
    responsible: str | None = Field(
        None, alias="Responsible", description="Responsavel pelo evento", examples=["Anderson José"], max_length=30
    )
    room: str | None = Field(None, alias="Room", description="Sala do evento", examples=["Sala 10"], max_length=10)
    room_capacity: float | None = Field(
        None, alias="RoomCapacity", description="Capacidade da Sala", examples=["200"], max_length=999999
    )
    grade_init_date: str | None = Field(
        None,
        alias="GradeInitDate",
        description="Data início da grade do evento.",
        examples=["10/10/2018"],
        max_length=8,
    )
    margin: float | None = Field(
        None,
        alias="Margin",
        description="Percentual de margem de segurança.",
        examples=["100.00"],
        ge=-999.99,
        le=999.99,
    )
    status: Status | None = Field(
        None,
        alias="Status",
        description="Status da grade de eventos.(1-Aberto,2-Lotado,3-Finalizado,4-Cancelado )",
        examples=["1"],
    )


class ListOfEvents(BaseModel):
    pass


class EventsInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa", max_length=3)
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01"], max_length=8
    )
    company_internal_id: str | None = Field(None, alias="CompanyInternalId", description="Código da Empresa")
    code: str | None = Field(
        None, alias="Code", description="Código do evento a ser cadastrado.", examples=["000001"], max_length=6
    )
    description: str | None = Field(
        None, alias="Description", description="Descrição do evento.", examples=["Evento nova API"], max_length=30
    )
    location: str | None = Field(
        None, alias="Location", description="Local do evento.", examples=["Local do evento"], max_length=40
    )
    init_date: str | None = Field(
        None, alias="InitDate", description="Data início do evento.", examples=["10/10/2018"], max_length=8
    )
    end_date: str | None = Field(
        None, alias="EndDate", description="Data final do evento.", examples=["11/10/2018"], max_length=8
    )
    initial_time: str | None = Field(
        None, alias="InitialTime", description="Hora início do evento.", examples=["08:00"], max_length=4
    )
    end_time: str | None = Field(
        None, alias="EndTime", description="Hora final do evento.", examples=["22:00"], max_length=4
    )
    blocked: str | None = Field(
        None,
        alias="Blocked",
        description="Evento bloqueado para uso (1-bloqueado 2-não bloqueado).",
        examples=["1"],
        max_length=1,
    )
    list_of_events: list[ListOfEvent] | ListOfEvents | None = Field(
        None, alias="ListOfEvents", description="Descreve a grade do evento"
    )


class ListEvent(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId do item da Eventos no ERP", examples="D MG 01 000001GRADE1"
    )
    grade_description: str | None = Field(
        None,
        alias="GradeDescription",
        description="Descrição da grade do evento.",
        examples=["Abertura do evento"],
        max_length=20,
    )
    theme_description: str | None = Field(
        None, alias="ThemeDescription", description="Assunto da atividade.", examples=["Valor agregado"], max_length=40
    )
    initial_time_grade: str | None = Field(
        None, alias="InitialTimeGrade", description="Hora início da grade.", examples=["08:30"], max_length=4
    )
    end_time_grade: str | None = Field(
        None, alias="EndTimeGrade", description="Hora final da grade.", examples=["11:30"], max_length=4
    )
    responsible: str | None = Field(
        None, alias="Responsible", description="Responsavel pelo evento", examples=["Anderson José"], max_length=30
    )
    room: str | None = Field(None, alias="Room", description="Sala do evento", examples=["Sala 10"], max_length=10)
    room_capacity: float | None = Field(
        None, alias="RoomCapacity", description="Capacidade da Sala", examples=["200"], max_length=999999
    )
    grade_init_date: str | None = Field(
        None,
        alias="GradeInitDate",
        description="Data início da grade do evento.",
        examples=["10/10/2018"],
        max_length=8,
    )
    margin: float | None = Field(
        None,
        alias="Margin",
        description="Percentual de margem de segurança.",
        examples=["100.00"],
        ge=-999.99,
        le=999.99,
    )
    status: Status | None = Field(
        None,
        alias="Status",
        description="Status da grade de eventos.(1-Aberto,2-Lotado,3-Finalizado,4-Cancelado )",
        examples=["1"],
    )


class ListEvents(RootModel[list[ListEvent]]):
    root: list[ListEvent] = Field(..., description="Descreve a grade do evento")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Events(BaseModel):
    items: list[EventsInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedEvent(Paging, Events):
    pass
