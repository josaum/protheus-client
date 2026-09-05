"""Contaminants — generated from Contaminants_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Status(StrEnum):
    field_1___ativo = "1 - Ativo"
    field_2___inativo = "2 - Inativo"


class ResultType(StrEnum):
    field_1___numerico = "1 - Numerico"
    field_2___texto = "2 - Texto"
    field_3___data = "3 - Data"
    field_4___lista = "4 - Lista"
    field_5___faixa = "5 - Faixa"


class WsAvailable(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class ContaminantValuesType(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código do contaminante", examples=["000001"])
    sequence: str | None = Field(None, alias="Sequence", description="Sequencia da Faixa / Lista", examples=["01"])
    result: str | None = Field(
        None, alias="Result", description="Valor do contaminante", examples=["Mediana contaminação"]
    )
    start_range: str | None = Field(
        None,
        alias="StartRange",
        description="Faixa inicial",
        examples=["9,999,999,999.99999"],
        ge=0,
        le=9999999999.99999,
    )
    end_range: Any | None = Field(
        None, alias="EndRange", description="Faixa Final", examples=["9,999,999,999.99999"], ge=0, le=9999999999.99999
    )
    inclusion_date_value: Any | None = Field(
        None, alias="InclusionDateValue", description="Data de inclusão", examples=["20181105"]
    )
    inclusion_hour_value: Any | None = Field(
        None, alias="InclusionHourValue", description="Hora de inclusão", examples=["17:54:31"]
    )
    update_date_value: Any | None = Field(
        None, alias="UpdateDateValue", description="Data de atualização", examples=["20181105"]
    )
    update_hour_value: Any | None = Field(
        None, alias="UpdateHourValue", description="Hora de atualização", examples=["17:59:01"]
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


class ListOfContaminantValues(BaseModel):
    items: list[ContaminantValuesType] | None = None


class ContaminantsType(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave do contaminante", examples=["99|000001"]
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código do contaminante", examples=["000001"])
    name: str | None = Field(None, alias="Name", description="Nome do contaminante", examples=["Pegajosidade"])
    description: str | None = Field(
        None, alias="Description", description="Descrição do contaminante", examples=["Pegajosidade"]
    )
    status: Status | None = Field(
        None, alias="Status", description="Informa se o contaminante está ativo para uso.", examples=["1"]
    )
    result_type: ResultType | None = Field(None, alias="ResultType", description="Tipo do contaminante", examples=["4"])
    result_size: str | None = Field(
        None, alias="ResultSize", description="Descrição do contaminante", examples=["14"], ge=0, le=14
    )
    result_precision: str | None = Field(
        None, alias="ResultPrecision", description="Descrição do contaminante", examples=["3"], ge=0, le=5
    )
    ws_available: WsAvailable | None = Field(
        None, alias="WSAvailable", description="Informa se contaminante é disponível via Web Service", examples=["1"]
    )
    propagation_level: str | None = Field(
        None, alias="PropagationLevel", description="Nível de propagação", examples=["99"], ge=1, le=99
    )
    inclusion_date: Any | None = Field(
        None, alias="InclusionDate", description="Data de inclusão", examples=["20181105"]
    )
    inclusion_hour: Any | None = Field(
        None, alias="InclusionHour", description="Hora de inclusão", examples=["17:54:31"]
    )
    update_date: Any | None = Field(None, alias="UpdateDate", description="Data de atualização", examples=["20181105"])
    update_hour: Any | None = Field(None, alias="UpdateHour", description="Hora de atualização", examples=["17:59:00"])
    list_of_contaminant_values: (
        ListOfContaminantValues | None
    ) = Field(None, alias="ListOfContaminantValues", description="Lista dos valores do contaminante.")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedContaminants(Paging):
    items: list[ContaminantsType] | None = None
