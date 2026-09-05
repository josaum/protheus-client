"""CottonBales — generated from CottonBales_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class CottonBalesType(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="Código único do fardão",
        examples=["000570-1819           -000001-01-01               "],
    )
    source_branch: str | None = Field(None, alias="SourceBranch", description="Filial do Sistema", examples=["99"])
    code: str | None = Field(None, alias="Code", description="Código do Fardão", examples=["000001"])
    product_code: str | None = Field(
        None, alias="ProductCode", description="Código do Produto", examples=["0123456789012345"]
    )
    date_of_typing: AwareDatetime | None = Field(
        None, alias="DateOfTyping", description="Data de Digitação do Fardão", examples=["2018-09-23T12:20:34"]
    )
    ware_house: str | None = Field(None, alias="WareHouse", description="Armazém", examples=["01"])
    crop: str | None = Field(None, alias="Crop", description="Armazém", examples=["01"])
    entity: str | None = Field(None, alias="Entity", description="Entidade", examples=["000001"])
    entity_store: str | None = Field(None, alias="EntityStore", description="Entidade", examples=["01"])
    farm: str | None = Field(None, alias="Farm", description="Fazenda", examples=["01"])
    estimated_weight: str | None = Field(None, alias="EstimatedWeight", description="Peso Estimado", examples=[2300])
    type_of_press: str | None = Field(None, alias="TypeOfPress", description="Tipo de Prensagem", examples=["2"])
    margin: str | None = Field(None, alias="Margin", description="Bordadura", examples=["2"])
    unb: str | None = Field(None, alias="Unb", description="Unidade de Beneficiamento", examples=["01"])
    part_of_land: str | None = Field(None, alias="PartOfLand", description="Talhão", examples=["0123456"])
    agricultural_variety: str | None = Field(
        None, alias="AgriculturalVariety", description="Variedade", examples=["000001"]
    )
    intended_income: str | None = Field(
        None, alias="IntendedIncome", description="Rendimento Previsto", examples=[42.37]
    )
    annotation: str | None = Field(None, alias="Annotation", description="Observação", examples=["Observação de Teste"])
    harvest_order: str | None = Field(
        None, alias="HarvestOrder", description="Ordem de Colheita", examples=["0123456789"]
    )
    id_q_cotton: str | None = Field(
        None, alias="IdQCotton", description="Id do Fardão no Q Cotton", examples=["01234567890123456789"]
    )
    tag_q_cotton: str | None = Field(
        None, alias="TagQCotton", description="Etiqueta do Fardão no Q Cotton", examples=["012345678901"]
    )
    x_coordinate: str | None = Field(None, alias="XCoordinate", description="Coordenada X do Fardão", examples=["300"])
    y_coordinate: str | None = Field(None, alias="YCoordinate", description="Coordenada Y do Fardão", examples=["500"])
    z_coordinate: str | None = Field(None, alias="ZCoordinate", description="Coordenada Z do Fardão", examples=["200"])
    lot_number: str | None = Field(None, alias="LotNumber", description="Número do Lote", examples=["1819"])
    sub_lot_number: str | None = Field(None, alias="SubLotNumber", description="Número do SubLote", examples=["000001"])
    lot_address: str | None = Field(
        None, alias="LotAddress", description="Endereço do Fardão", examples=["000000000000001"]
    )
    start_harvest_forecast: AwareDatetime | None = Field(
        None,
        alias="StartHarvestForecast",
        description="Previsão de Início de Colheita",
        examples=["2018-11-03T17:30:39"],
    )
    closing_harvest_forecast: AwareDatetime | None = Field(
        None,
        alias="ClosingHarvestForecast",
        description="Previsão de Término de Colheita",
        examples=["2018-12-01T17:20:40"],
    )
    production_order: str | None = Field(
        None, alias="ProductionOrder", description="Ordem de Produção", examples=["00000000000001"]
    )
    tare_weight: str | None = Field(None, alias="TareWeight", description="Tara do Fardão", examples=[10.85])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
