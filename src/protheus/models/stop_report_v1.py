"""Apontamentos de Parada — generated from StopReport_v1_003.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class StopType(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ListOfDirectLabor(BaseModel):
    operator_code: str | None = Field(None, alias="OperatorCode", description="Código Operador", max_length=20)
    stop_reason_code: str | None = Field(None, alias="StopReasonCode", description="Código Motivo Parada", max_length=8)
    production_shift_code: str | None = Field(
        None, alias="ProductionShiftCode", description="Código Modelo Turno", max_length=8
    )
    production_shift_number: int | None = Field(
        None, alias="ProductionShiftNumber", description="Número Turno", ge=-99999, le=99999
    )
    start_date_time: AwareDatetime | None = Field(None, alias="StartDateTime", description="Data/Hora Início")
    end_date_time: AwareDatetime | None = Field(None, alias="EndDateTime", description="Data/Hora Fim")


class StopReport(BaseModel):
    machine_code: str | None = Field(None, alias="MachineCode", description="Código Máquina", max_length=20)
    production_order: str | None = Field(None, alias="ProductionOrder", description="Ordem de produção", max_length=20)
    activity_code: str | None = Field(None, alias="ActivityCode", description="Código da operação", max_length=10)
    activity_id: str | None = Field(None, alias="ActivityId", description="ID da operação", max_length=10)
    machine_description: str | None = Field(
        None, alias="MachineDescription", description="Descrição Máquina", max_length=40
    )
    stop_reason_code: str | None = Field(None, alias="StopReasonCode", description="Código Motivo Parada", max_length=8)
    stop_reason_description: str | None = Field(
        None, alias="StopReasonDescription", description="Descrição Motivo Parada", max_length=40
    )
    start_date_time: AwareDatetime | None = Field(None, alias="StartDateTime", description="Data/Hora Início")
    end_date_time: AwareDatetime | None = Field(None, alias="EndDateTime", description="Data/Hora Fim")
    tool_code: str | None = Field(None, alias="ToolCode", description="Código Ferramenta", max_length=20)
    tool_description: str | None = Field(
        None, alias="ToolDescription", description="Descrição Ferramenta", max_length=40
    )
    production_team_code: str | None = Field(
        None, alias="ProductionTeamCode", description="Código Equipe", max_length=20
    )
    production_team_name: str | None = Field(None, alias="ProductionTeamName", description="Nome Equipe", max_length=40)
    operator_code: str | None = Field(None, alias="OperatorCode", description="Código Operador", max_length=20)
    operator_name: str | None = Field(None, alias="OperatorName", description="Nome Operador", max_length=40)
    production_shift_code: str | None = Field(
        None, alias="ProductionShiftCode", description="Código Modelo Turno", max_length=8
    )
    production_shift_description: (
        str | None
    ) = Field(None, alias="ProductionShiftDescription", description="Descrição Turno", max_length=40)
    production_shift_number: int | None = Field(
        None, alias="ProductionShiftNumber", description="Número Turno", ge=-99999, le=99999
    )
    stop_type: StopType | None = Field(
        None, alias="StopType", description="Tipo Parada / 1 - Programada / 2 - Não Programada"
    )
    report_date_time: AwareDatetime | None = Field(None, alias="ReportDateTime", description="Data/Hora Reporte")
    general_stop_code: str | None = Field(
        None, alias="GeneralStopCode", description="Código Parada Geral", max_length=10
    )
    report_sequence: int | None = Field(
        None, alias="ReportSequence", description="Sequência Reporte", ge=-999999999999999, le=999999999999999
    )
    reversed_report: bool | None = Field(None, alias="ReversedReport", description="Reporte Estornado")
    integration_report: str | None = Field(
        None, alias="IntegrationReport", description="Reporte Integração", max_length=10
    )
    list_of_direct_labors: list[ListOfDirectLabor] | None = Field(None, alias="ListOfDirectLabors")
    document_code: str | None = Field(None, alias="DocumentCode", description="Codigo da Movimentação", max_length=20)
    stop_cause_code: str | None = Field(None, alias="StopCauseCode", description="Causa da Parada")
    observation: str | None = Field(None, alias="Observation", description="Observação")


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


class PagedStopReports(Paging):
    items: list[StopReport] | None = None
