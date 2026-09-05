"""Agendamento de Serviço — generated from JobScheduler_v1_100.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Status(StrEnum):
    pending = "pending"
    failure = "failure"
    success = "success"
    running_ = "running "
    canceled = "canceled"


class JobExecutionType(BaseModel):
    execution_id: str | None = Field(
        None, alias="executionID", description="Identificador Ãºnico da execuÃ§Ã£o do processo", max_length=30
    )
    job_schedule_id: str | None = Field(
        None, alias="jobScheduleID", description="Identificador Ãºnico do agendamento do processo", max_length=30
    )
    status: Status | None = Field(None, description="Indica o status da execuÃ§Ã£o do processo")
    created_date: date | None = Field(
        None,
        alias="createdDate",
        description="Indica a data da Ãºltima alteraÃ§Ã£o do agendamento no momento da execuÃ§Ã£o do processo",
    )
    started_date: date | None = Field(None, alias="startedDate", description="Indica a data de execuÃ§Ã£o do processo")
    user: str | None = Field(None, description="UsuÃ¡rio responsÃ¡vel pelo agendamento", max_length=100)
    return_: dict[str, Any] | None = Field(None, alias="return", description="Resultado da execuÃ§Ã£o do processo")
    error: str | None = Field(None, description="Mensagem de erro na execuÃ§Ã£o do processo")
    hour: str | None = Field(None, description="Hora de execução do processo (HH:mm)", max_length=5)


class Status1(StrEnum):
    active = "active"
    inactive = "inactive"
    completed = "completed"


class DailyType(BaseModel):
    year: int | None = None
    month: int | None = None
    day: int | None = None
    hour: int | None = None
    minute: int | None = None


class DaysOfWeekEnum(StrEnum):
    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class WeeklyType(BaseModel):
    days_of_week: list[DaysOfWeekEnum] | None = Field(None, alias="daysOfWeek")
    hour: int | None = None
    minute: int | None = None


class MonthlyType(BaseModel):
    day: int | None = None
    hour: int | None = None
    minute: int | None = None


class Type(StrEnum):
    day = "day"
    hour = "hour"
    minute = "minute"


class Frequency(BaseModel):
    type: Type | None = Field(
        None,
        description="Indica qual o tipo de repetiÃ§Ã£o para os horÃ¡rios a serem gerados. Se 'day', gerarÃ¡ horÃ¡rios incrementando dias; se 'hour', gerarÃ¡ horÃ¡rios incrementando horas; se 'minute', gerarÃ¡ horÃ¡rios incrementando minutos",
    )
    value: int | None = Field(None, description="Frequencia do tipo do intervalo")


class RangeLimit(BaseModel):
    day: int | None = Field(None, description="Dia limite para tÃ©rmino da agenda (vÃ¡lido somente para Monthly)")
    hour: int | None = Field(None, description="Hora limite para tÃ©rmino da agenda")
    minute: int | None = Field(None, description="Minuto limite, pertencente Ã\xa0 hora, para tÃ©rmino da agenda")


class RangeExecutionsType(BaseModel):
    frequency: Frequency | None = None
    range_limit: RangeLimit | None = Field(None, alias="rangeLimit")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedExecutionJobscheduler(Paging):
    items: list[JobExecutionType] | None = None


class JobSchedulerType(BaseModel):
    job_schedule_id: str | None = Field(
        None, alias="jobScheduleID", description="Identificador Ãºnico do agendamento do processo", max_length=30
    )
    status: Status1 | None = Field(None, description="Indica o status da execuÃ§Ã£o do processo")
    last_modified: date | None = Field(
        None, alias="lastModified", description="Data da Ãºltima alteraÃ§Ã£o no agendamento"
    )
    process_id: str | None = Field(
        None, alias="processID", description="Identificador do processo (rotina) que serÃ¡ executado", max_length=100
    )
    first_execution: str | None = Field(
        None, alias="firstExecution", description="Data prevista para inÃ\xadcio da execuÃ§Ã£o do processo"
    )
    user: str | None = Field(None, description="UsuÃ¡rio responsÃ¡vel pelo agendamento", max_length=100)
    recurrent: bool | None = Field(None, description="indica se a execuÃ§Ã£o do job deve ocorrer mais de uma vez")
    execution_parameter: dict[str, Any] | None = Field(
        None, alias="executionParameter", description="ParÃ¢metros para execuÃ§Ã£o do processo"
    )
    daily: DailyType | None = None
    weekly: WeeklyType | None = None
    monthly: MonthlyType | None = None
    range_executions: RangeExecutionsType | None = Field(None, alias="rangeExecutions")
    execs: int | None = Field(None, description="Número de execuções no mesmo dia")
    enddate: str | None = Field(None, description="Data de término do processo")
    discard: bool | None = Field(None, description="Identifica se as tarefas atrasadas serão descartadas")
    interval: str | None = Field(None, description="Intervalo entre cada execução no mesmo dia (HH:mm)")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedJobscheduler(Paging):
    items: list[JobSchedulerType] | None = None
