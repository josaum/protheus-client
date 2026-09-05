"""Estruturas do MRP — generated from MRPBillOfMaterial_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class FixedQuantity(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ConversionType(StrEnum):
    field_1 = "1"
    field_2 = "2"


class Inventory(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class MRPAlternativesOfBill(BaseModel):
    alternative: str | None = Field(None, description="Código do alternativo")
    conversion_type: ConversionType | None = Field(None, alias="conversionType", description="Tipo de conversão.")
    conversion_factor: float | None = Field(None, alias="conversionFactor", description="Fator de conversão")
    vigency: date | None = Field(None, description="Vigência do produto alternativo")
    inventory: Inventory | None = Field(None, description="Estoque.")
    sequence: str | None = Field(None, description="Sequência do alternativo")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class MRPComponentsOfBill(BaseModel):
    component: str | None = Field(None, description="Código do componente", max_length=90)
    sequence: str | None = Field(None, description="Sequência do componente", max_length=10)
    start_revison: str | None = Field(None, alias="startRevison", description="Revisão Inicial")
    end_revison: str | None = Field(None, alias="endRevison", description="Revisão Final")
    quantity: float | None = Field(None, description="Quantidade")
    start_date: date | None = Field(None, alias="startDate", description="Data início")
    end_date: date | None = Field(None, alias="endDate", description="Data fim")
    percentage_scrap: float | None = Field(None, alias="percentageScrap", description="Percentual de perda")
    fixed_quantity: FixedQuantity | None = Field(None, alias="fixedQuantity", description="Quantidade fixa?")
    optional_group: str | None = Field(None, alias="optionalGroup", description="Grupo de opcional")
    optional_item: str | None = Field(None, alias="optionalItem", description="Item opcional")
    potency: float | None = Field(None, description="Potência")
    warehouse: str | None = Field(None, description="Armazém de consumo")
    is_ghost_material: bool | None = Field(None, alias="isGhostMaterial", description="Fantasma?", examples=[False])
    code: str | None = Field(None, description="Id Estrutura")
    list_of_mrp_alternatives: list[MRPAlternativesOfBill] | None = Field(
        None, alias="listOfMRPAlternatives", description="Lista de alternativos relacionados ao componente"
    )


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class MRPBillOfMaterial(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Código do produto", max_length=90)
    item_amount: float | None = Field(None, alias="itemAmount", description="Quantidade base")
    list_of_mrp_components: list[MRPComponentsOfBill] | None = Field(
        None, alias="listOfMRPComponents", description="Lista de componentes do produto pai"
    )


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPBillOfMaterial | None = Field(None, alias="detailedMessage")


class ListOfMRPBillOfMaterial(BaseModel):
    items: list[MRPBillOfMaterial] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class PagedMRPBillOfMaterial(Paging, ListOfMRPBillOfMaterial):
    pass


class MRPBillOfMaterialMultiple(PagedMRPBillOfMaterial, ListOfMessages):
    pass
