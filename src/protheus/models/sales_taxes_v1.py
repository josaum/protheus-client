"""Impostos do Pedido de Venda — generated from SalesTaxes_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class TaxesDetail(BaseModel):
    descricao: str | None = Field(None, description="Nome do Tributo", examples=["ICMS"])
    aliquota: float | None = Field(None, description="Aliquota do Tributo", examples=[12], ge=0.0, le=999999999.99)
    valor: float | None = Field(None, description="Valor do Tributo", examples=[120], ge=0.0, le=999999999.99)
    base_calculo: float | None = Field(
        None, description="Valor sobre qual o Tributo incide", examples=[1000], ge=0.0, le=999999999.99
    )
    imposto: str | None = Field(None, description="Identificador do Tributo", examples=["ICM"])


class Itens(BaseModel):
    valor_mercadoria: float | None = Field(
        None, description="Valor de Mercadoria do Item", examples=[1000], ge=0.0, le=999999999.99
    )
    valor_st: float | None = Field(None, description="Valor do ICMS-ST", examples=[100], ge=0.0, le=999999999.99)
    valor_total: float | None = Field(None, description="Valor Total do Item", examples=[1000], ge=0.0, le=999999999.99)
    seguro: float | None = Field(None, description="Valor de Seguro por Item", examples=[1000], ge=0.0, le=999999999.99)
    valor_csll: float | None = Field(None, description="Valor de CSLL", examples=[1000], ge=0.0, le=999999999.99)
    valor_unitario: float | None = Field(None, description="Valor Unitário", examples=[1000], ge=0.0, le=999999999.99)
    quantidade: float | None = Field(None, description="Quantidade do Item", examples=[10], ge=0.0, le=999999999.99)
    aliquota_pis: float | None = Field(
        None, description="Alíquota do PIS/PASEP", examples=[1.65], ge=0.0, le=999999999.99
    )
    aliquota_ipi: float | None = Field(None, description="Alíquota do IPI", examples=[10], ge=0.0, le=999999999.99)
    valor_pis: float | None = Field(None, description="Valor do PIS/PASEP", examples=[16.5], ge=0.0, le=999999999.99)
    aliquota_cofins: float | None = Field(
        None, description="Alíquota do COFINS", examples=[7.6], ge=0.0, le=999999999.99
    )
    valor_cofins: float | None = Field(None, description="Valor do COFINS", examples=[76], ge=0.0, le=999999999.99)
    aliquota_st: float | None = Field(None, description="Aliquota do ICMS-ST", examples=[2], ge=0.0, le=999999999.99)
    aliquota_icms: float | None = Field(None, description="Aliquota do ICMS", examples=[18], ge=0.0, le=999999999.99)
    frete: float | None = Field(None, description="Frete do Item", examples=[100], ge=0.0, le=999999999.99)
    codigo_produto: str | None = Field(
        None, description="Código do Produto", examples=["000000000000000000000000000001"]
    )
    aliquota_csll: float | None = Field(None, description="Aliquota do CSLL", examples=[3], ge=0.0, le=999999999.99)
    valor_icms: float | None = Field(None, description="Valor do ICMS", examples=[180], ge=0.0, le=999999999.99)
    valor_ipi: float | None = Field(None, description="Valor do IPI", examples=[100], ge=0.0, le=999999999.99)
    desconto: float | None = Field(None, description="Desconto do Item", examples=[10], ge=0.0, le=999999999.99)
    despesas_acessorias: float | None = Field(
        None, description="Despesas Acessórias do Item", examples=[10], ge=0.0, le=999999999.99
    )
    tes: str | None = Field(None, description="Tipo de Entrada/Saída do Item", examples=["501"])


class ReturnSalesTaxes(BaseModel):
    valor_contabil: float | None = Field(None, description="Total Contabil", examples=[135000], ge=0.0, le=999999999.99)
    valor_mercadoria: float | None = Field(
        None, description="Valor Total de Mercadorias", examples=[135000], ge=0.0, le=999999999.99
    )
    total_impostos_sem_incidencia: (
        float | None
    ) = Field(None, description="Valor de Tributos sem Incidência", examples=[0], ge=0.0, le=999999999.99)
    total_impostos_embutidos: float | None = Field(
        None, description="Total de Tributos Embutidos", examples=[13145.63], ge=0.0, le=999999999.99
    )
    total_impostos: float | None = Field(
        None, description="Total de Tributos", examples=[33783.76], ge=0.0, le=999999999.99
    )
    taxes_detail: TaxesDetail | None = Field(None, alias="TaxesDetail", description="Detalhamento dos Tributos")
    itens: Itens | None = Field(None, description="Detalhamento dos Tributos por Item do Documento Fiscal")
    desconto: float | None = Field(None, description="Total de Descontos", examples=[99.35], ge=0.0, le=999999999.99)
    base_duplicada: float | None = Field(
        None, description="Total do Título Financeiro", examples=[99.35], ge=0.0, le=999999999.99
    )
    seguro: float | None = Field(None, description="Total do Seguro", examples=[99.35], ge=0.0, le=999999999.99)
    frete: float | None = Field(None, description="Total do Frete", examples=[99.35], ge=0.0, le=999999999.99)
    despesas_acessorias: float | None = Field(
        None, description="Total das Despesas Acessórias", examples=[99.35], ge=0.0, le=999999999.99
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


class ListofProduct(BaseModel):
    item_id: str | None = Field(None, alias="ItemId", description="Numero do Item no Pedido", examples=["01"])
    product_id: str | None = Field(
        None, alias="ProductId", description="Código do Produto", examples=["000000000000000000000000000001"]
    )
    quantity: float | None = Field(
        None, alias="Quantity", description="Quantidade Vendida", examples=[10], ge=0.0, le=999999.99
    )
    unitary_value: float | None = Field(
        None, alias="UnitaryValue", description="Preco Unitario Liquido", examples=[100], ge=0.0, le=99999999.99
    )
    total_value: float | None = Field(
        None, alias="TotalValue", description="Valor Total do Item", examples=[1000], ge=0.0, le=999999999.99
    )
    tes: str | None = Field(None, alias="TES", description="Tipo de Saida do Item", examples=["001"])
    item_discount_percentage: float | None = Field(
        None,
        alias="ItemDiscountPercentage",
        description="Percentual de Desconto do Item",
        examples=[10],
        ge=0.0,
        le=99.99,
    )
    item_discount_value: float | None = Field(
        None,
        alias="ItemDiscountValue",
        description="Valor do Desconto do Item",
        examples=[100],
        ge=0.0,
        le=99999999999.99,
    )
    price_list: float | None = Field(
        None, alias="PriceList", description="Preco Unitario de Tabela", examples=[100], ge=0.0, le=99999999.99
    )
    operation_type: str | None = Field(
        None, alias="OperationType", description="Tipo de Operação do Item", examples=["01"]
    )


class SalesOrderInfo(BaseModel):
    sales_type: str | None = Field(None, alias="SalesType", description="Tipo de Pedido de Venda", examples=["N"])
    customer_id: str | None = Field(None, alias="CustomerId", description="Código do Cliente", examples=["000001"])
    customer_unit: str | None = Field(None, alias="CustomerUnit", description="Loja do Cliente", examples=["01"])
    customer_id_delivery: str | None = Field(
        None, alias="CustomerIdDelivery", description="Cliente de Entrega", examples=["000001"]
    )
    customer_unit_delivery: str | None = Field(
        None, alias="CustomerUnitDelivery", description="Codigo da Loja de Entrega", examples=["01"]
    )
    customer_type: str | None = Field(None, alias="CustomerType", description="Tipo do Cliente", examples=["F"])
    payment: str | None = Field(None, alias="Payment", description="Condição de Pagamento", examples=["001"])
    discount_percentage1: float | None = Field(
        None,
        alias="DiscountPercentage1",
        description="Percentual de desconto 1 em cascata",
        examples=[10.0],
        ge=0.0,
        le=99.99,
    )
    discount_percentage2: float | None = Field(
        None,
        alias="DiscountPercentage2",
        description="Percentual de desconto 2 em cascata",
        examples=[10.0],
        ge=0.0,
        le=99.99,
    )
    discount_percentage3: float | None = Field(
        None,
        alias="DiscountPercentage3",
        description="Percentual de desconto 3 em cascata",
        examples=[10.0],
        ge=0.0,
        le=99.99,
    )
    discount_percentage4: float | None = Field(
        None,
        alias="DiscountPercentage4",
        description="Percentual de desconto 4 em cascata",
        examples=[10.0],
        ge=0.0,
        le=99.99,
    )
    currency: float | None = Field(
        None, alias="Currency", description="Moeda do Pedido de Venda", examples=[1], ge=1.0, le=5.0
    )
    freight: float | None = Field(
        None, alias="Freight", description="Valor do Frete", examples=[10.0], ge=0.0, le=999999999.99
    )
    insurance: float | None = Field(
        None, alias="Insurance", description="Valor do Seguro", examples=[10.0], ge=0.0, le=999999999.99
    )
    expense: float | None = Field(
        None, alias="Expense", description="Valor de Despesa Acessória", examples=[10.0], ge=0.0, le=999999999.99
    )
    listof_products: list[ListofProduct] | None = Field(None, alias="ListofProducts")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
