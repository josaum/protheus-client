"""CottonGinBreakPointings — generated from CottonGinBreakPointings_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Status(StrEnum):
    field_1___em_andamento = "1 - Em andamento"
    field_2___finalizado = "2 - Finalizado"


class CottonGinBreakPointingsType(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="Chave do apontamento de motivo de parada da esteira.",
        examples=["99|000003"],
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código do registro.", examples=["001"])
    cotton_gin_code: str | None = Field(
        None, alias="CottonGinCode", description="Código do conjunto.", examples=["000001"]
    )
    cotton_gin_break_code: str | None = Field(
        None, alias="CottonGinBreakCode", description="Código do motivo de parada.", examples=["001"]
    )
    shift_code: str | None = Field(None, alias="ShiftCode", description="Código do turno.", examples=["001"])
    start_date: str | None = Field(
        None, alias="StartDate", description="Data de início da parada.", examples=["20181022"]
    )
    start_time: str | None = Field(None, alias="StartTime", description="Hora de início da parada.", examples=["09:00"])
    end_date: str | None = Field(None, alias="EndDate", description="Data de término da parada.", examples=["20181022"])
    end_time: str | None = Field(None, alias="EndTime", description="Hora de término da parada.", examples=["11:00"])
    status: Status | None = Field(None, alias="Status", description="Status da parada.", examples=["1"])
    user_code: str | None = Field(None, alias="UserCode", description="Código do usuário.", examples=["0000000001"])
    note: str | None = Field(
        None, alias="Note", description="Observação da parada.", examples=["Esteira necessita de lavagem."]
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


class PagedCottonGinBreakPointings(Paging):
    items: list[CottonGinBreakPointingsType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
