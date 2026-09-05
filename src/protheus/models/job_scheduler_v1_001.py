"""Agendamento de Serviço — generated from JobScheduler_v1_001.json (ttalk ca5e26a). Do not edit by hand."""

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
        None, alias="executionID", description="Identificador único da execução do processo", max_length=30
    )
    job_schedule_id: str | None = Field(
        None, alias="jobScheduleID", description="Identificador único do agendamento do processo", max_length=30
    )
    status: Status | None = Field(None, description="Indica o status da execução do processo")
    created_date: date | None = Field(
        None,
        alias="createdDate",
        description="Indica a data da última alteração do agendamento no momento da execução do processo",
    )
    started_date: date | None = Field(None, alias="startedDate", description="Indica a data de execução do processo")
    user: str | None = Field(None, description="Usuário responsável pelo agendamento", max_length=100)
    return_: dict[str, Any] | None = Field(None, alias="return", description="Resultado da execução do processo")
    error: str | None = Field(None, description="Mensagem de erro na execução do processo")


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
        None, alias="jobScheduleID", description="Identificador único do agendamento do processo", max_length=30
    )
    status: Status1 | None = Field(None, description="Indica o status da execução do processo")
    last_modified: date | None = Field(
        None, alias="lastModified", description="Data da última alteração no agendamento"
    )
    process_id: str | None = Field(
        None, alias="processID", description="Identificador do processo (rotina) que será executado", max_length=100
    )
    first_execution: str | None = Field(
        None, alias="firstExecution", description="Data prevista para início da execução do processo"
    )
    user: str | None = Field(None, description="Usuário responsável pelo agendamento", max_length=100)
    recurrent: bool | None = Field(None, description="indica se a execução do job deve ocorrer mais de uma vez")
    execution_parameter: dict[str, Any] | None = Field(
        None, alias="executionParameter", description="Parâmetros para execução do processo"
    )
    daily: DailyType | None = None
    weekly: WeeklyType | None = None
    monthly: MonthlyType | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedJobscheduler(Paging):
    items: list[JobSchedulerType] | None = None
