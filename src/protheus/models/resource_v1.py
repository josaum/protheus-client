"""Recursos — generated from Resource_v1_001.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"


class Resource(BaseModel):
    resource_id: str | None = Field(None, alias="ResourceId", description="ID Recurso", max_length=10)
    code: str | None = Field(None, alias="Code", description="Código Recurso", max_length=20)
    type: Type | None = Field(
        None, alias="Type", description="Tipo Recurso / 1 - Operador / 2 - Ferramenta / 3 - Equipe / 4 - Equipamento"
    )
    name: str | None = Field(None, alias="Name", description="Nome Recurso", max_length=40)
    production_area_code: str | None = Field(
        None, alias="ProductionAreaCode", description="Codigo Área Produção", max_length=10
    )
    production_area_description: (
        str | None
    ) = Field(None, alias="ProductionAreaDescription", description="Descrição Área Produção", max_length=40)
    production_shift_number: str | None = Field(
        None, alias="ProductionShiftNumber", description="Número Turno", max_length=5
    )
    labor_code: str | None = Field(None, alias="LaborCode", description="Cóigo Mão de Obra Direta", max_length=8)
    start_expiration_date: date | None = Field(None, alias="StartExpirationDate", description="Data Início Validade")
    end_expiration_date: date | None = Field(None, alias="EndExpirationDate", description="Data Fim Validade")
    unit_cycle_quantity: int | None = Field(
        None, alias="UnitCycleQuantity", description="Unidades Ciclo", ge=-9999999, le=9999999
    )
    tool_code: str | None = Field(None, alias="ToolCode", description="Código Item Ferramenta", max_length=30)
    tool_description: str | None = Field(
        None, alias="ToolDescription", description="Descrição Item Ferramenta", max_length=40
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


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedResources(Paging):
    items: list[Resource] | None = None
