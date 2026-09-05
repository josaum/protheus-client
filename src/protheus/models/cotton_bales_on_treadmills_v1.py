"""CottonBalesOnTreadmills — generated from CottonBalesOnTreadmills_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CottonBalesOnTreadmillsType(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="Chave da esteira que contêm os fardões vinculados.",
        examples=["D MG 01 |000001|000197|1819           |000001|01|01"],
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código da esteira.", examples=["000001"])
    crop: str | None = Field(None, alias="Crop", description="Safra do vínculo.", examples=["1819"])
    agricultural_owner_code: str | None = Field(
        None, alias="AgriculturalOwnerCode", description="Código do produtor do fardão.", examples=["000001"]
    )
    agricultural_owner_store_code: (
        str | None
    ) = Field(None, alias="AgriculturalOwnerStoreCode", description="Código da loja do produtor.", examples=["01"])
    farm_code: str | None = Field(None, alias="FarmCode", description="Código da fazenda do fardão.", examples=["01"])
    order: str | None = Field(
        None, alias="Order", description="Ordem do fardão na esteira.", examples=["05"], ge=0, le=999
    )
    cotton_bale_code: str | None = Field(
        None, alias="CottonBaleCode", description="Código do fardão.", examples=["000120"]
    )
    product_code: str | None = Field(None, alias="ProductCode", description="Código do produto.", examples=["1006312"])
    part_of_land: str | None = Field(None, alias="PartOfLand", description="Talhão do fardão.", examples=["TLH000001"])
    variety: str | None = Field(None, alias="Variety", description="Variedade do fardão.", examples=["000001"])
    net_weight: float | None = Field(
        None, alias="NetWeight", description="Peso líquido", examples=["99,999,999,999.99"], ge=0.0, le=99999999999.99
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


class PagedCottonBalesOnTreadmills(Paging):
    items: list[CottonBalesOnTreadmillsType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
