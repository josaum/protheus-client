"""GrainQualityTestKinds — generated from GrainQualityTestKinds_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class GrainQualityTestKindsType(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave do tipo de desconto da classificação.", examples=["99|000003"]
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código do registro.", examples=["000001"])
    description: str | None = Field(
        None, alias="Description", description="Descrição do tipo de desconto.", examples=["Impurezas"]
    )
    product_code: str | None = Field(None, alias="ProductCode", description="Código do produto.", examples=["1006298"])
    measurement_unit: str | None = Field(
        None, alias="MeasurementUnit", description="Unidade de medida do produto.", examples=["KG"]
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


class PagedGrainQualityTestKinds(Paging):
    items: list[GrainQualityTestKindsType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
