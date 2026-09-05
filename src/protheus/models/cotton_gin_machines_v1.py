"""CottonGinMachines — generated from CottonGinMachines_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ExceedIncome(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class WeightScale(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class MoveStock(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class AdditionalItemsType(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    item_code: str | None = Field(None, alias="ItemCode", description="Código do item.", examples=["001"])
    product_code: str | None = Field(None, alias="ProductCode", description="Código do produto.", examples=["1006298"])
    product_description: str | None = Field(
        None, alias="ProductDescription", description="Descrição do produto.", examples=["Caroço de algodão"]
    )
    product_amount_: str | None = Field(
        None, alias="ProductAmount ", description="Quantidade do produto.", examples=["30"], ge=0, le=99999999999.99
    )
    unit_weight_: str | None = Field(
        None, alias="UnitWeight ", description="Peso unitário do produto.", examples=["0.44"], ge=0, le=9999.99
    )
    warehouse_code: str | None = Field(
        None, alias="WarehouseCode", description="Código do local de estoque.", examples=["01"]
    )
    weight_scale: WeightScale | None = Field(
        None, alias="WeightScale", description="Compoe peso da balança?", examples=["1"]
    )
    cotton_gin_machine_code: str | None = Field(
        None, alias="CottonGinMachineCode", description="Código do conjunto.", examples=["000002"]
    )
    move_stock: MoveStock | None = Field(None, alias="MoveStock", description="Movimenta estoque?", examples=["1"])
    transaction_type: str | None = Field(
        None, alias="TransactionType", description="Tipo de movimentação.", examples=["514"]
    )
    product_lot: str | None = Field(None, alias="ProductLot", description="Lote do produto.", examples=["LT20180516"])
    product_sub_lot: str | None = Field(
        None, alias="ProductSubLot", description="Sub-lote do produto.", examples=["30"]
    )
    product_adress: str | None = Field(
        None, alias="ProductAdress", description="Endereço do lote do produto.", examples=["30"]
    )


class CottonFeather(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class SeparationType(StrEnum):
    field_1___fixo = "1 - Fixo"
    field_2___variável = "2 - Variável"
    field_3___realizado = "3 - Realizado"


class GenerateProduction(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class ProductType(StrEnum):
    field_1___pluma = "1 - Pluma"
    field_2___caroço = "2 - Caroço"
    field_3___fibrilha = "3 - Fibrilha"
    field_4___casquinha = "4 - Casquinha"
    field_5___resíduo = "5 - Resíduo"


class ItemsPercentualSeparationType(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    cotton_gin_machine_code: str | None = Field(
        None, alias="CottonGinMachineCode", description="Código do conjunto.", examples=["000001"]
    )
    item: str | None = Field(None, alias="Item", description="Número do item.", examples=["001"])
    productcode: str | None = Field(None, alias="Productcode", description="Código do produto.", examples=["1066091"])
    product_description: str | None = Field(
        None, alias="ProductDescription", description="Descrição do produto.", examples=["Caroço de algodão"]
    )
    warehouse_code_: str | None = Field(
        None, alias="WarehouseCode ", description="Código do local de estoque.", examples=["05"]
    )
    cotton_feather: CottonFeather | None = Field(
        None, alias="CottonFeather", description="Pluma de algodão?", examples=["1"]
    )
    separation_type: SeparationType | None = Field(
        None, alias="SeparationType", description="Tipo de separação", examples=["1"]
    )
    separation_percentual: str | None = Field(
        None, alias="SeparationPercentual", description="Percentual de separação", examples=["50.00"], ge=0, le=100
    )
    cost_sharing: str | None = Field(
        None, alias="CostSharing", description="Percentual de rateio de custo", examples=["85.0000"], ge=0, le=99.9999
    )
    generate_production: GenerateProduction | None = Field(
        None, alias="GenerateProduction", description="Gera produção?", examples=["1"]
    )
    production_product_code: str | None = Field(
        None,
        alias="ProductionProductCode",
        description="Código do produto acabado que será produzido após a desmontagem",
        examples=["1006310"],
    )
    production_product_description: (
        str | None
    ) = (
        Field(None, alias="ProductionProductDescription", description="Descrição do produto acabado que será produzido após a desmontagem", examples=["Algodao em pluma"])
    )
    production_warehouse: str | None = Field(
        None, alias="ProductionWarehouse", description="Local de estoque da produção", examples=["09"]
    )
    transaction_type: str | None = Field(
        None, alias="TransactionType", description="Tipo de movimentação usada para produção", examples=["101"]
    )
    product_lot: str | None = Field(None, alias="ProductLot", description="Lote do produto.", examples=["LT20180516"])
    product_sub_lot: str | None = Field(
        None, alias="ProductSubLot", description="Sub-Lote do produto.", examples=["001"]
    )
    product_adress: str | None = Field(
        None, alias="ProductAdress", description="Endereço do produto.", examples=["LT20180516"]
    )
    production_product_lot: str | None = Field(
        None,
        alias="ProductionProductLot",
        description="Lote do produto acabado que será produzido após a desmontagem",
        examples=["LT20180517"],
    )
    production_product_sub_lot: (
        str | None
    ) = (
        Field(None, alias="ProductionProductSubLot", description="Sub-Lote do produto acabado que será produzido após a desmontagem", examples=["002"])
    )
    production_product_adress: (
        str | None
    ) = (
        Field(None, alias="ProductionProductAdress", description="Endereço do produto acabado que será produzido após a desmontagem", examples=["0000000001"])
    )
    product_type: ProductType | None = Field(None, alias="ProductType", description="Tipo do produto", examples=["1"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class AdditionalItems(BaseModel):
    items: list[AdditionalItemsType] | None = None


class ItemsPercentualSeparation(BaseModel):
    items: list[ItemsPercentualSeparationType] | None = None


class CottonGinMachinesType(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave do lançamento de contaminante.", examples=["99|000002"]
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    cotton_gin_machine_code: str | None = Field(
        None, alias="CottonGinMachineCode", description="Código do conjunto.", examples=["000002"]
    )
    description: str | None = Field(
        None, alias="Description", description="Descrição do conjunto.", examples=["Beneficiadora Belo Horizonte"]
    )
    sai_code: str | None = Field(
        None, alias="SAICode", description="Código do Sistema Abrapa de Identificação.", examples=["0007898535831"]
    )
    cotton_gin_code: str | None = Field(
        None, alias="CottonGinCode", description="Código da unidade de beneficamento.", examples=["01"]
    )
    cotton_gin_name: str | None = Field(
        None,
        alias="CottonGinName",
        description="Nome da unidade de beneficiamento.",
        examples=["Beneficiamento Belo Horizonte"],
    )
    additional_balance_weight: (
        str | None
    ) = (
        Field(None, alias="AdditionalBalanceWeight", description="Peso adicional da balança.", examples=["120.50"], ge=0, le=999.99)
    )
    minimum_weight: str | None = Field(
        None,
        alias="MinimumWeight",
        description="Peso mínimo permitido para este conjunto.",
        examples=["150.00"],
        ge=0,
        le=999.99,
    )
    maximum_weight: str | None = Field(
        None,
        alias="MaximumWeight",
        description="Peso máximo permitido para este conjunto.",
        examples=["250,00"],
        ge=0,
        le=999.99,
    )
    minimum_yield: str | None = Field(
        None, alias="MinimumYield", description="Porcentagem de rendimento mínimo.", examples=["38.50"], ge=0, le=99.99
    )
    maximum_yield: str | None = Field(
        None, alias="MaximumYield", description="Porcentagem de rendimento máximo.", examples=["48,00"], ge=0, le=99.99
    )
    average_yield: str | None = Field(
        None, alias="AverageYield", description="Porcentagem de rendimento médio.", examples=["42,00"], ge=0, le=99.99
    )
    expected_start_date: str | None = Field(
        None, alias="ExpectedStartDate", description="Data prevista do início do beneficiamento.", examples=[20180301]
    )
    expected_end_date: str | None = Field(
        None, alias="ExpectedEndDate", description="Data prevista do término do beneficiamento.", examples=[20190201]
    )
    number_saws: str | None = Field(
        None, alias="NumberSaws", description="Número de serras.", examples=["2,000"], ge=0, le=9.999
    )
    kilos_per_hour: str | None = Field(
        None, alias="KilosPerHour", description="Kilos por hora.", examples=["530.00"], ge=0, le=999.99
    )
    productive_hours: str | None = Field(
        None,
        alias="ProductiveHours",
        description="Quantidade de horas produtivas do conjunto.",
        examples=["20"],
        ge=0,
        le=24,
    )
    cotton_bales_per_day: str | None = Field(
        None, alias="CottonBalesPerDay", description="Quantidade de fardos por dia.", examples=["9,000"], ge=0, le=9.999
    )
    exceed_income: ExceedIncome | None = Field(
        None, alias="ExceedIncome", description="Ultrapassa rendimento?", examples=["1"]
    )
    additional_items: AdditionalItems | None = Field(
        None, alias="AdditionalItems", description="Itens adicionais do conjunto."
    )
    items_percentual_separation: (
        ItemsPercentualSeparation | None
    ) = Field(None, alias="ItemsPercentualSeparation", description="Percentual de separação do itens.")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedCottonGinMachines(Paging):
    items: list[CottonGinMachinesType] | None = None
