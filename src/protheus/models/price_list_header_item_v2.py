"""Tabela de Preços — generated from PriceListHeaderItem_v2_005.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class IncludedIpi(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ActiveTablePrice(StrEnum):
    field_1 = "1"
    field_2 = "2"


class IncludedFreight(StrEnum):
    field_1 = "1"
    field_2 = "2"


class TypePrice(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class ActiveItemPrice(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ItensTablePriceItem(BaseModel):
    identify_price_list_items: (
        str | None
    ) = (
        Field(None, alias="identifyPriceListItems", description="Identificador da Tabela de Preços recebida na mensagem.")
    )
    provider: str | None = Field(None, description="Fornecedor da Tabela de Preços")
    code: str | None = Field(None, description="Código da Tabela de Preço")
    payment_terms: str | None = Field(
        None, alias="paymentTerms", description="Condição de Pagamento da Tabela de Preço"
    )
    company: str | None = Field(None, description="Estabelecimento da Tabela de Preço")
    currency: str | None = Field(None, description="Moeda da Tabela de Preço")
    item_list: str | None = Field(None, alias="itemList", description="Item da Tabela", max_length=4)
    item_code: str | None = Field(None, alias="itemCode", description="Código do Produto", max_length=30)
    item_internal_id: str | None = Field(
        None, alias="itemInternalId", description="InternalId da chave completa do Item"
    )
    reference_code: str | None = Field(
        None, alias="referenceCode", description="Código da Referência do Produto", max_length=8
    )
    unit_of_measure_code: str | None = Field(
        None, alias="unitOfMeasureCode", description="Código da Unidade de Medida de Venda", max_length=2
    )
    minimum_sales_price: float | None = Field(
        None, alias="minimumSalesPrice", description="Preco mínimo de venda do produto - Valor Sem Frete", max_length=12
    )
    item_price: float | None = Field(None, alias="itemPrice", description="Preco do Item", max_length=16)
    aliquot_ipi: float | None = Field(None, alias="aliquotIPI", description="Alíquota do IPI", max_length=6)
    minimum_sales_price_fob: float | None = Field(
        None, alias="minimumSalesPriceFOB", description="Preco de minimo de venda do produto - FOB", max_length=12
    )
    discount_value: float | None = Field(
        None, alias="discountValue", description="Valor de Desconto em reais", max_length=12
    )
    discount_amount: float | None = Field(
        None, alias="discountAmount", description="Desconto por quantidade", max_length=9
    )
    discount_factor: float | None = Field(
        None, alias="discountFactor", description="Fator de Acresc./Desconto%", max_length=11
    )
    minimum_amount: float | None = Field(None, alias="minimumAmount", description="Quantidade Mínima", max_length=12)
    cif_price: float | None = Field(None, alias="cifPrice", description="Preco CIF", max_length=11)
    fob_price: float | None = Field(None, alias="fobPrice", description="Preco FOB", max_length=11)
    item_validity: date | None = Field(
        None,
        alias="itemValidity",
        description="Data Vigência do item AAAA-MM-DD",
        examples=["2018-07-19"],
        max_length=10,
    )
    aliquot_icms: float | None = Field(None, alias="aliquotICMS", description="Alíquota do ICMS", max_length=6)
    correction_group: str | None = Field(None, alias="correctionGroup", description="Grupo de Correções", max_length=3)
    type_price: TypePrice | None = Field(
        None,
        alias="typePrice",
        description="Tipo da Tabela de Preço: 1 = Preco Venda , 2 = Venda Consumidor, 3 = Atacado , 4 = Varejo, 5 = Promocao",
    )
    active_item_price: ActiveItemPrice | None = Field(
        None, alias="activeItemPrice", description="Status do Item da Tabela de Preço: 1 = Sim; 2 = Não"
    )


class ItensTablePrice(BaseModel):
    pass


class PriceListHeaderItemsInfo(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="ID Filial")
    company_internal_id: str | None = Field(
        None, alias="companyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    identify_price_list: str | None = Field(
        None, alias="identifyPriceList", description="Identificador da Tabela de Preços recebida na mensagem."
    )
    code: str | None = Field(None, description="Código da tabela de preço", max_length=4)
    internal_id: str | None = Field(
        None, alias="internalId", description="InternalId da chave completa da tabela de preço"
    )
    company_id: str | None = Field(None, alias="companyId", description="Código da empresa")
    name: str | None = Field(None, description="Descrição da Tabela", max_length=40)
    provider: str | None = Field(None, description="Fornecedor da Tabela de Preços")
    payment_terms: str | None = Field(
        None, alias="paymentTerms", description="Condição de Pagamento da Tabela de Preço"
    )
    company: str | None = Field(None, description="Estabelecimento da Tabela de Preço")
    initial_date: date | None = Field(
        None,
        alias="initialDate",
        description="Data Inicial da Vigência AAAA-MM-DD",
        examples=["2018-07-19"],
        max_length=10,
    )
    final_date: date | None = Field(
        None, alias="finalDate", description="Data Final da Vigência AAAAMMDD", examples=["20180719"]
    )
    initia_hour: AwareDatetime | None = Field(None, alias="initiaHour", description="Hora Inicial Vigencia HH:MM:SS")
    final_hour: AwareDatetime | None = Field(None, alias="finalHour", description="Hora Final Vigencia HH:MM:SS")
    currency: str | None = Field(None, description="Moeda da Tabela de Preço")
    included_ipi: IncludedIpi | None = Field(None, alias="IncludedIPI", description="IPI Incluso? 1 = Sim; 2 = Não")
    value_descount: float | None = Field(
        None, alias="valueDescount", description="Desconto Tabela de Preço", max_length=12
    )
    discount_factor: float | None = Field(
        None, alias="discountFactor", description="Percentual de Desconto", max_length=5
    )
    active_table_price: ActiveTablePrice | None = Field(
        None, alias="activeTablePrice", description="Tabela de Preco Ativo? 1 = Sim; 2 = Não"
    )
    freight_value: float | None = Field(None, alias="freightValue", description="Valor do Frete", max_length=14)
    included_freight: IncludedFreight | None = Field(
        None, alias="IncludedFreight", description="Frete Incluso? 1 = Sim; 2 = Não"
    )
    aliquot_icms: float | None = Field(None, alias="aliquotICMS", description="Alíquota do ICMS", max_length=6)
    note: str | None = Field(None, description="Observação da Tabela de Preço", max_length=2000)
    itens_table_price: list[ItensTablePriceItem] | ItensTablePrice | None = Field(None, alias="itensTablePrice")


class ItensTablePriceInfoItem(BaseModel):
    identify_price_list_items: (
        str | None
    ) = (
        Field(None, alias="identifyPriceListItems", description="Identificador da Tabela de Preços recebida na mensagem.")
    )
    provider: str | None = Field(None, description="Fornecedor da Tabela de Preços")
    code: str | None = Field(None, description="Código da Tabela de Preço")
    payment_terms: str | None = Field(
        None, alias="paymentTerms", description="Condição de Pagamento da Tabela de Preço"
    )
    company: str | None = Field(None, description="Estabelecimento da Tabela de Preço")
    currency: str | None = Field(None, description="Moeda da Tabela de Preço")
    item_list: str | None = Field(None, alias="itemList", description="Item da Tabela", max_length=4)
    item_code: str | None = Field(None, alias="itemCode", description="Código do Produto", max_length=30)
    item_internal_id: str | None = Field(
        None, alias="itemInternalId", description="InternalId da chave completa do Item"
    )
    reference_code: str | None = Field(
        None, alias="referenceCode", description="Código da Referência do Produto", max_length=8
    )
    unit_of_measure_code: str | None = Field(
        None, alias="unitOfMeasureCode", description="Código da Unidade de Medida de Venda", max_length=2
    )
    minimum_sales_price: float | None = Field(
        None, alias="minimumSalesPrice", description="Preco mínimo de venda do produto - Valor Sem Frete", max_length=12
    )
    item_price: float | None = Field(None, alias="itemPrice", description="Preco do Item", max_length=16)
    aliquot_ipi: float | None = Field(None, alias="aliquotIPI", description="Alíquota do IPI", max_length=6)
    minimum_sales_price_fob: float | None = Field(
        None, alias="minimumSalesPriceFOB", description="Preco de minimo de venda do produto - FOB", max_length=12
    )
    discount_value: float | None = Field(
        None, alias="discountValue", description="Valor de Desconto em reais", max_length=12
    )
    discount_amount: float | None = Field(
        None, alias="discountAmount", description="Desconto por quantidade", max_length=9
    )
    discount_factor: float | None = Field(
        None, alias="discountFactor", description="Fator de Acresc./Desconto%", max_length=11
    )
    minimum_amount: float | None = Field(None, alias="minimumAmount", description="Quantidade Mínima", max_length=12)
    cif_price: float | None = Field(None, alias="cifPrice", description="Preco CIF", max_length=11)
    fob_price: float | None = Field(None, alias="fobPrice", description="Preco FOB", max_length=11)
    item_validity: date | None = Field(
        None,
        alias="itemValidity",
        description="Data Vigência do item AAAA-MM-DD",
        examples=["2018-07-19"],
        max_length=10,
    )
    aliquot_icms: float | None = Field(None, alias="aliquotICMS", description="Alíquota do ICMS", max_length=6)
    correction_group: str | None = Field(None, alias="correctionGroup", description="Grupo de Correções", max_length=3)
    type_price: TypePrice | None = Field(
        None,
        alias="typePrice",
        description="Tipo da Tabela de Preço: 1 = Preco Venda , 2 = Venda Consumidor, 3 = Atacado , 4 = Varejo, 5 = Promocao",
    )
    active_item_price: ActiveItemPrice | None = Field(
        None, alias="activeItemPrice", description="Status do Item da Tabela de Preço: 1 = Sim; 2 = Não"
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


class ItensTablePrices(BaseModel):
    items: list[ItensTablePriceInfoItem] | None = None


class PagedPriceListHeaderItems(Paging):
    items: list[PriceListHeaderItemsInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedItensTablePrice(Paging, ItensTablePrices):
    pass
