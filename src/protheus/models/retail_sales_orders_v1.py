"""Pedidos de Venda do Varejo — generated from RetailSalesOrders_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class RetailSalesOrdersType(BaseModel):
    seller_code1: str | None = Field(None, alias="sellerCode1", description="Codigo do Vendedor 1")
    budget_number: str | None = Field(None, alias="budgetNumber", description="Numero do Orcamento")
    generate_wms: str | None = Field(None, alias="generateWms", description="Gera O.S./WMS")
    class_volume1: str | None = Field(None, alias="classVolume1", description="Especie do Volume tipo 1")
    register_date: str | None = Field(None, alias="registerDate", description="Data da Emissao")
    ecommerce_tracking_code: str | None = Field(
        None, alias="ecommerceTrackingCode", description="Rastreio do Pedido E-com."
    )
    currency: float | None = Field(
        None, description="Moeda do Pedido de Venda", ge=-9999999999999.99, le=9999999999999.99, multiple_of=0.01
    )
    invoice_number: str | None = Field(None, alias="invoiceNumber", description="Numero da Nota Fiscal")
    invoice_series: str | None = Field(None, alias="invoiceSeries", description="Serie da Nota Fiscal")
    company_id: str | None = Field(None, alias="companyId", description="ID da empresa")
    company_internal_id: str | None = Field(None, alias="companyInternalId", description="Chave da Empresa/Filial")
    order: str | None = Field(None, description="Numero do Pedido")
    branch_id: str | None = Field(None, alias="branchId", description="Filial do Sistema")
    freight_value: float | None = Field(
        None,
        alias="freightValue",
        description="Valor do Frete",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    expense_value: float | None = Field(
        None,
        alias="expenseValue",
        description="Valor Despesa Acessoria",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    volume_amount: float | None = Field(
        None,
        alias="volumeAmount",
        description="Qtde de Volumes tipo 1",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_value1: float | None = Field(
        None,
        alias="discountValue1",
        description="Desconto 1",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    customer_store: str | None = Field(None, alias="customerStore", description="Loja do Cliente")
    invoice_message: str | None = Field(None, alias="invoiceMessage", description="Mensagem para Nota Fiscal")
    type_freight: str | None = Field(None, alias="typeFreight", description="Tipo do Frete Utilizado")
    customer_code: str | None = Field(None, alias="customerCode", description="Codigo do Cliente")
    ecommerce_order: str | None = Field(None, alias="ecommerceOrder", description="Pedido E-Commerce")
    ecommerce_status: str | None = Field(None, alias="ecommerceStatus", description="Status E-Commerce")
    internal_id: str | None = Field(None, alias="internalId", description="internalId do pedido")
    gross_weight: float | None = Field(
        None, alias="grossWeight", description="Peso Bruto", ge=-9999999999999.99, le=9999999999999.99, multiple_of=0.01
    )
    insurance_value: float | None = Field(
        None,
        alias="insuranceValue",
        description="Valor do Seguro",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    load: str | None = Field(None, description="Carga")
    release_type: str | None = Field(None, alias="releaseType", description="Tipo de Liberacao")
    origin: str | None = Field(None, description="Origem do Pedido")
    carrier_code: str | None = Field(None, alias="carrierCode", description="Codigo da Transportadora")
    commission_seller1: float | None = Field(
        None,
        alias="commissionSeller1",
        description="Comissao do Vendedor 1",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    net_weight: float | None = Field(
        None, alias="netWeight", description="Peso Liquido", ge=-9999999999999.99, le=9999999999999.99, multiple_of=0.01
    )
    payment_term: str | None = Field(None, alias="paymentTerm", description="Condicao de Pagamento", max_length=3)


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class RetailSalesOrderItemType(BaseModel):
    type_production_order: str | None = Field(
        None, alias="typeProductionOrder", description="Tipo da Ordem de Produção"
    )
    part_type: str | None = Field(None, alias="partType", description="Tipo Peça")
    company_id: str | None = Field(None, alias="companyId", description="ID da empresa")
    company_internal_id: str | None = Field(None, alias="companyInternalId", description="Chave da Empresa/Filial")
    product_code: str | None = Field(None, alias="productCode", description="Código do Produto")
    unitary_price: float | None = Field(
        None,
        alias="unitaryPrice",
        description="Preço Unitário Líquido",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    total_value: float | None = Field(
        None,
        alias="totalValue",
        description="Valor Total do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    item: str | None = Field(None, description="Número do Item no Pedido")
    order: str | None = Field(None, description="Número do Pedido")
    branch_id: str | None = Field(None, alias="branchId", description="Filial do Sistema")
    delivery_date: str | None = Field(None, alias="deliveryDate", description="Data da Entrega")
    extended_warranty: str | None = Field(None, alias="extendedWarranty", description="Item Garantia Estendida")
    shift: str | None = Field(None, description="Manhã,Tarde e Noite")
    extended_warranty_quot: str | None = Field(
        None, alias="extendedWarrantyQuot", description="Orçamento Garantia Estendida"
    )
    customer_store: str | None = Field(None, alias="customerStore", description="Loja do Cliente")
    wms_block: str | None = Field(None, alias="wmsBlock", description="Bloqueio TMS")
    description: str | None = Field(None, description="Descricao Auxiliar")
    warehouse_internal_id: str | None = Field(None, alias="warehouseInternalId", description="Armazem")
    customer_code: str | None = Field(None, alias="customerCode", description="Codigo do Cliente")
    fci_code: str | None = Field(None, alias="fciCode", description="Código FCI")
    lot: str | None = Field(None, description="Lote")
    approved_amount: float | None = Field(
        None,
        alias="approvedAmount",
        description="Quantidade Liberada",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    stock_block: str | None = Field(None, alias="stockBlock", description="Cod.Bloqueio ref.estoque")
    block_information: str | None = Field(None, alias="blockInformation", description="Informação de bloqueio")
    internal_id: str | None = Field(None, alias="internalId", description="internalId do pedido")
    import_value: float | None = Field(
        None,
        alias="importValue",
        description="Valor da Importação",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    taxation_status: str | None = Field(None, alias="taxationStatus", description="Situacao Tributaria")
    measure_unit: str | None = Field(None, alias="measureUnit", description="Unidade de Medida Primaria")
    price_list: float | None = Field(
        None,
        alias="priceList",
        description="Preco Unitario de Tabela",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    tms_block: str | None = Field(None, alias="tmsBlock", description="Bloqueio do WMS")
    quantity: float | None = Field(
        None, description="Quantidade Vendida", ge=-9999999999999.99, le=9999999999999.99, multiple_of=0.01
    )
    fiscal_code: str | None = Field(None, alias="fiscalCode", description="Código Fiscal da Operação")
    outflow_type: str | None = Field(None, alias="outflowType", description="Tipo de Saída do Item")
    block: str | None = Field(None, description="Bloqueio")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
