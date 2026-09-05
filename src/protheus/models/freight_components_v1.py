"""Freight Components — generated from FreightComponents_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class AttributeForCalculation(StrEnum):
    field_01 = "01"
    field_02 = "02"
    field_03 = "03"
    field_04 = "04"
    field_05 = "05"
    field_06 = "06"
    field_07 = "07"
    field_08 = "08"
    field_09 = "09"
    field_10 = "10"
    field_11 = "11"
    field_12 = "12"


class SuframaTable(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class ValueCategory(StrEnum):
    field_1 = "1"
    field_2 = "2"


class Service(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ValuePerLoadManifest(StrEnum):
    field_1 = "1"
    field_2 = "2"


class DailyValueFreelanceCalculation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class GroupValues(StrEnum):
    field_1 = "1"
    field_2 = "2"


class CalculateService(StrEnum):
    field_1 = "1"
    field_2 = "2"


class FreightComponents(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1"], max_length=3
    )
    code: str | None = Field(None, alias="Code", description="Codigo do Componente", max_length=20)
    branch_id: str | None = Field(
        None, alias="BranchId", description="Codigo da Filial", examples=["D MG 01 "], max_length=8
    )
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="Codigo da Empresa", max_length=16
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId do Solicitante no ERP", max_length=28
    )
    description: str | None = Field(None, alias="Description", description="Descrição Componente", max_length=50)
    attribute_for_calculation: (
        AttributeForCalculation | None
    ) = (
        Field(None, alias="AttributeForCalculation", description="Atributo para cálculo (01-Peso, 02-Valor Carga, 03-Quantidade de Itens, 04-Volume, 05-Quantidade de Volumes, 06-Distancia, 07-Quantidade de Entrega, 08-Valor Fixo, 09-Valor Frete, 10-Peso Liquido, 11-Quantidade de ServiÃ§os, 12-Valor Liquido)")
    )
    suframa_table: SuframaTable | None = Field(
        None,
        alias="SuframaTable",
        description="Suframa (1-Não se aplica, 2-Tarifa da Tabela de Frete, 3-Tabela Suframa)",
    )
    value_category: ValueCategory | None = Field(
        None,
        alias="ValueCategory",
        description="Categoria do Valor (1-Frete Unidade, 2-Frete Valor, 3-Taxas, 4-Pedagio)",
    )
    service: Service | None = Field(None, alias="Service", description="Cálculo de Serviço (1-Sim, 2-Nao)")
    value_per_load_manifest: ValuePerLoadManifest | None = Field(
        None, alias="ValuePerLoadManifest", description="Valor por Romaneio de Carga (1-Sim, 2-Nao)"
    )
    daily_value_freelance_calculation: (
        DailyValueFreelanceCalculation | None
    ) = (
        Field(None, alias="DailyValueFreelanceCalculation", description="CÃ¡lculo do Valor Diário Autônomo (1-Sim, 2-Nao)")
    )
    group_values: GroupValues | None = Field(
        None, alias="GroupValues", description="Agrupa Valores Por (1-Entrega, 2-Romaneio)"
    )
    service_type_code: str | None = Field(None, alias="ServiceTypeCode", description="Codigo Tipo Serviço")
    calculate_service: CalculateService | None = Field(
        None, alias="CalculateService", description="Calcula Serviço (1-Por Ocorrência, 2-Por Romaneio)"
    )
    calculation_unitizing: str | None = Field(None, alias="CalculationUnitizing", description="Unitizador para Cálculo")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedFreightComponent(Paging):
    items: list[FreightComponents] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
