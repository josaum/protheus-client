"""Produtos Varejo — generated from RetailItem_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ItemInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da Empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial")
    code: str | None = Field(None, alias="Code", description="Código do Produto")
    internal_id: str | None = Field(None, alias="InternalId", description="Chave completa do Produto")
    description: str | None = Field(None, alias="Description", description="Descrição do Produto")
    active: str | None = Field(None, alias="Active", description="Ativo")
    unit_of_measure_code: str | None = Field(None, alias="UnitOfMeasureCode", description="Unidade de Medida")
    standard_warehouse_code: str | None = Field(None, alias="StandardWarehouseCode", description="Armazém Padrão")
    economic_lot: float | None = Field(None, alias="EconomicLot", description="Lote Econômico")
    minimum_lot: float | None = Field(None, alias="MinimumLot", description="Lote Mínimo")
    net_weight: float | None = Field(None, alias="NetWeight", description="Peso Líquido")
    gross_weight: float | None = Field(None, alias="GrossWeight", description="Peso Bruto")
    family_code: str | None = Field(None, alias="FamilyCode", description="Código da Familia")
    origin: str | None = Field(None, alias="Origin", description="Origem")
    cost_center_code: str | None = Field(None, alias="CostCenterCode", description="Centro de Custo")
    account_item: str | None = Field(None, alias="AccountItem", description="Item Conta Contabíl")
    group_code: str | None = Field(None, alias="GroupCode", description="Grupo")
    second_unit_of_measure_code: (
        str | None
    ) = Field(None, alias="SecondUnitOfMeasureCode", description="Segunda Unidade de Medida")
    multiplication_factor_value: (
        float | None
    ) = Field(None, alias="MultiplicationFactorValue", description="Fator de Conversão")
    product_type: str | None = Field(None, alias="ProductType", description="Tipo de Produto")
    trail: str | None = Field(None, alias="Trail", description="Rastreabilidade Produto")
    addressing_control: str | None = Field(None, alias="AddressingControl", description="Controla Enderecamento")
    manufacturer: str | None = Field(None, alias="Manufacturer", description="Fabricante")
    icms_tax_rate: float | None = Field(None, alias="IcmsTaxRate", description="Alíquota de ICMS")
    ipi_tax_rate: float | None = Field(None, alias="IpiTaxRate", description="Alíquota de IPI")
    iss_tax_rate: float | None = Field(None, alias="IssTaxRate", description="Aliquota de ISS")
    mercosul_nomenclature: str | None = Field(
        None, alias="MercosulNomenclature", description="Nomenclatura Comum do Mercosul"
    )
    sales_price: float | None = Field(None, alias="SalesPrice", description="Preço de Venda")
    standard_cost: float | None = Field(None, alias="StandardCost", description="Custo Padrão")
    last_purchase_price: float | None = Field(None, alias="LastPurchasePrice", description="Último Preço de Compra")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedItems(Paging):
    items: list[ItemInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
