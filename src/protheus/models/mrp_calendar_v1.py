"""Calendário do MRP — generated from MRPCalendar_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date as date_aliased

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPCalendarBase(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    code: str | None = Field(None, description="Id único do calendário do MRP", max_length=200)
    calendar: str | None = Field(None, description="Código do Calendário", max_length=10)
    date: date_aliased | None = Field(None, description="Data do calendário do MRP")
    start_time: str | None = Field(None, alias="startTime", description="Hora de início do perído do MRP", max_length=5)
    end_time: str | None = Field(None, alias="endTime", description="Hora de término do período do MRP", max_length=5)
    interval: str | None = Field(None, description="Tempo de intervalo do período do MRP", max_length=5)
    total_hours: str | None = Field(None, alias="totalHours", description="Tempo total do período do MRP", max_length=5)


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPCalendarBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPCalendar(BaseModel):
    items: list[MRPCalendarBase] | None = None


class ListOfMessages(Paging):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPCalendar(Paging, ListOfMRPCalendar):
    pass


class MRPCalendarMultiple(ListOfMRPCalendar, ListOfMessages):
    pass
