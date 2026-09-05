"""CottonPoisoningPointings — generated from CottonPoisoningPointings_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class VariableType(StrEnum):
    field_1___numérico = "1 - Numérico"
    field_2___texto = "2 - Texto"
    field_3___data = "3 - Data"
    field_4___lista = "4 - Lista"
    field_5___faixa = "5 - Faixa"


class IncomeTax(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class Active(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class ClassificationPackingListType(StrEnum):
    field_1___visual = "1 - Visual"
    field_2___hvi = "2 - HVI"


class CottonPoisoningPointingsType(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="Chave do lançamento de contaminante.",
        examples=["99|1819|1006312|DXL602|000001|000001|1"],
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    crop_code: str | None = Field(None, alias="CropCode", description="Código da safra.", examples=["1819"])
    product_code: str | None = Field(None, alias="ProductCode", description="Código do produto.", examples=["1006312"])
    lot: str | None = Field(None, alias="Lot", description="Lote do registro.", examples=["DXL602"])
    analysis_type: str | None = Field(
        None, alias="AnalysisType", description="Código do tipo de análise.", examples=["000001"]
    )
    sequence: str | None = Field(None, alias="Sequence", description="Sequência do registro.", examples=["1"])
    analysis_variable: str | None = Field(
        None, alias="AnalysisVariable", description="Código da variável de análise.", examples=["000001"]
    )
    variable_description: str | None = Field(
        None, alias="VariableDescription", description="Descrição da variável de análise.", examples=["Pegajosidade"]
    )
    variable_type: VariableType | None = Field(
        None, alias="VariableType", description="Tipo da variável de análise.", examples=["1"]
    )
    result_value: float | None = Field(
        None, alias="ResultValue", description="Valor resultado da análise.", examples=[15], ge=0.0, le=9999999.99
    )
    result_text: str | None = Field(
        None, alias="ResultText", description="Texto resultado da análise.", examples=["BAIXA CONTAMINACAO"]
    )
    result_date: Any | None = Field(
        None, alias="ResultDate", description="Data resultado da análise.", examples=[20181101]
    )
    income_tax: IncomeTax | None = Field(None, alias="IncomeTax", description="Imposto de renda?", examples=["1"])
    active: Active | None = Field(None, alias="Active", description="Lançamento ativo?", examples=["1"])
    update_date: Any | None = Field(
        None, alias="UpdateDate", description="Data de atualização do lançamento.", examples=[20181115]
    )
    update_user: str | None = Field(
        None, alias="UpdateUser", description="Usuário que efetuou a alteração no registro.", examples=["Administrador"]
    )
    case_unique_code: str | None = Field(
        None, alias="CaseUniqueCode", description="Código único da mala.", examples=["D MG 01 -1819-000226-2-ML"]
    )
    block_unique_code: str | None = Field(
        None, alias="BlockUniqueCode", description="Código único do bloco.", examples=["D MG 01 -1819-000002-BL"]
    )
    cotton_wrap_unique_code: str | None = Field(
        None, alias="CottonWrapUniqueCode", description="Etiqueta do fardinho.", examples=["00078985358310000014"]
    )
    cotton_bale_unique_code: str | None = Field(
        None,
        alias="CottonBaleUniqueCode",
        description="Código único do fardão.",
        examples=["000455-1819           -000001-01-01"],
    )
    cotton_bale_code: str | None = Field(
        None, alias="CottonBaleCode", description="Código do fardão.", examples=["000003"]
    )
    block_code: str | None = Field(None, alias="BlockCode", description="Código do bloco.", examples=["000002"])
    classification_packing_list: (
        str | None
    ) = (
        Field(None, alias="ClassificationPackingList", description="Código do romaneio de classificação.", examples=["000226"])
    )
    entity_code: str | None = Field(None, alias="EntityCode", description="Código da entidade.", examples=["000001"])
    entity_store_code: str | None = Field(
        None, alias="EntityStoreCode", description="Código da loja da entidade.", examples=["01"]
    )
    entity_farm: str | None = Field(
        None, alias="EntityFarm", description="Código da fazenda da entidade.", examples=["01"]
    )
    cotton_wrap_code: str | None = Field(
        None, alias="CottonWrapCode", description="Código do fardinho.", examples=["000001"]
    )
    classification_packing_list_type: (
        ClassificationPackingListType | None
    ) = Field(None, alias="ClassificationPackingListType", description="Tipo da mala de classificação.", examples=["1"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedCottonPoisoningPointings(Paging):
    items: list[CottonPoisoningPointingsType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
