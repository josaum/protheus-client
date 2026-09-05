"""Vendas do Varejo — generated from RetailSales_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date as date_aliased
from datetime import time
from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel


class RetailSalesCancellationType(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Codigo da Empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Codigo da Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa de cancelamento da venda "
    )
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do Cancelamento")
    retail_sales_internal_id: str | None = Field(
        None, alias="RetailSalesInternalId", description="Codigo InternalId da Venda"
    )
    operator_code: str | None = Field(None, alias="OperatorCode", description="Código do Operador", max_length=3)
    cancel_date: AwareDatetime | None = Field(None, alias="CancelDate", description="Data do Cancelamento")
    nfce_cancel_protocol: str | None = Field(
        None, alias="NfceCancelProtocol", description="Protocolo de cancelamento NFCe", max_length=15
    )
    cancellation_document: str | None = Field(
        None, alias="CancellationDocument", description="Número do documento de cancelamento", max_length=15
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


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Taxe(StrEnum):
    itf = "ITF"
    cofins = "COFINS"
    csll = "CSLL"
    fabov = "FABOV"
    facs = "FACS"
    inss_pf = "INSS-PF"
    inss_pj = "INSS-PJ"
    inss_rur = "INSS-RUR"
    iof = "IOF"
    ir_carreteiro = "IR-CARRETEIRO"
    irrf_pf = "IRRF–PF"
    irrf_pj = "IRRF–PJ"
    iss = "ISS"
    iss_arq_elet = "ISS-ARQ-ELET"
    pis = "PIS"
    pis_cofins_csll = "PIS/COFINS/CSLL"
    pis_cofins_cred = "PIS/COFINS-CRED"
    pis_cofins_prod = "PIS/COFINS-PROD"
    sest_senat = "SEST/SENAT"
    icm = "ICM"
    ipi = "IPI"
    ii = "II"
    imp_cana = "IMP_CANA"
    icms_st = "ICMS_ST"
    recolh_inss = "RECOLH_INSS"
    reten_iss = "RETEN_ISS"
    reten_inss = "RETEN_INSS"
    reten_inss_rur = "RETEN_INSS_RUR"
    reten_sest_senat = "RETEN_SEST_SENAT"


class Reason(StrEnum):
    field_001 = "001"
    field_002 = "002"
    field_003 = "003"


class IncidenceType(StrEnum):
    c = "C"
    i = "I"
    o = "O"
    e = "E"
    n = "N"
    u = "U"
    d = "D"
    s = "S"


class Kind(StrEnum):
    d = "D"
    r = "R"


class ListOfTax(BaseModel):
    taxe: Taxe | None = Field(
        None,
        alias="Taxe",
        description="Nome do Imposto (ITF, COFINS, CSLL, FABOV, FACS, INSS-PF, INSS-PJ, INSS-RUR, IOF, IR-CARRETEIRO, IR-PF, IR-PJ, IRRF–PF, IRRF–PJ, ISS, ISS-ARQ-ELET, PIS, PIS/COFINS/CSLL, PIS/COFINS-CRED, PIS/COFINS-PROD, SEST/SENAT,ICM, IPI, II, IMP_CANA, ICMS_ST, RECOLH_INSS, RETEN_ISS, RETEN_INSS, RETEN_INSS_RUR, RETEN_SEST_SENAT) / ITF - -Imposto sobre movimentação financeira / COFINS - COFINS / CSLL - CSLL / FABOV - FABOV / FACS - FACS / INSS-PF - INSS-PF / INSS-PJ - INSS-PJ / INSS-RUR - INSS-RUR / IOF - IOF / IR-CARRETEIRO - IR-CARRETEIRO / IRRF–PF - IRRF–PF / IRRF–PJ - IRRF–PJ / ISS - ISS / ISS-ARQ-ELET - ISS-ARQ-ELET / PIS - PIS / PIS/COFINS/CSLL - PIS/COFINS/CSLL / PIS/COFINS-CRED - PIS/COFINS-CRED / PIS/COFINS-PROD - PIS/COFINS-PROD / SEST/SENAT - SEST/SENAT / ICM - ICM / IPI - IPI / II - II - Imposto de Importação / IMP_CANA - IMP_CANA - Imposto da Cana / ICMS_ST - ICMS_ST - ICMS Substituicao Tributaria / RECOLH_INSS - RECOLH_INSS - Recolhimento INSS / RETEN_ISS - RETEN_ISS - Retenção ISS / RETEN_INSS - RETEN_INSS - Retenção INSS / RETEN_INSS_RUR - RETEN_INSS_RUR - Retenção INSS Rural / RETEN_SEST_SENAT - RETEN_SEST_SENAT - Retenção SEST SENAT",
    )
    country_code: str | None = Field(None, alias="CountryCode", description="Código do País")
    country_internal_id: str | None = Field(None, alias="CountryInternalId", description="InternalId do CountryCode")
    state_code: str | None = Field(None, alias="StateCode", description="Código da Unidade Federativa")
    state_internal_id: str | None = Field(None, alias="StateInternalId", description="InternalId do StateCode")
    city_code: str | None = Field(None, alias="CityCode", description="Código da Cidade")
    city_internal_id: str | None = Field(None, alias="CityInternalId", description="InternalId do CityCode")
    calculation_basis: float | None = Field(
        None, alias="CalculationBasis", description="Base de Cálculo para o Imposto"
    )
    percentage: float | None = Field(None, alias="Percentage", description="Percentual do Imposto")
    reduction_based_percent: float | None = Field(
        None, alias="ReductionBasedPercent", description="Percentual de Redução de Base"
    )
    value: float | None = Field(None, alias="Value", description="Valor do Imposto")
    reason: Reason | None = Field(
        None,
        alias="Reason",
        description="Motivo da Retenção 1-Autopeças, 2-Órgãos Públicos, 3–Serviço / 001 - Autopeças / 002 - Órgãos Públicos / 003 - Serviço",
    )
    deferral_percentage: float | None = Field(
        None, alias="DeferralPercentage", description="Percentual do Diferimento - Somente para ICMS"
    )
    deferral_value: float | None = Field(
        None, alias="DeferralValue", description="Valor do Diferimento - Somente para ICMS"
    )
    presumed_credit_percentage: (
        float | None
    ) = Field(None, alias="PresumedCreditPercentage", description="Percentual do Crédito Presumido")
    presumed_credit_value: float | None = Field(
        None, alias="PresumedCreditValue", description="Valor do Crédito Presumido"
    )
    especific_calculation_basis: (
        float | None
    ) = Field(None, alias="EspecificCalculationBasis", description="Base de Cálculo para Alíquota Específica")
    especific_aliquot: float | None = Field(None, alias="EspecificAliquot", description="Alíquota Específica")
    increase_percentage: float | None = Field(
        None, alias="IncreasePercentage", description="Percentual de Majoração do Imposto"
    )
    increase_value: float | None = Field(None, alias="IncreaseValue", description="Valor de Majoração do Imposto")
    recalculate: bool | None = Field(None, alias="Recalculate", description="Recalcular?")
    code_tax_situation: str | None = Field(None, alias="CodeTaxSituation", description="CST do imposto")
    with_holding_tax: bool | None = Field(None, alias="WithHoldingTax", description="É retenção?")
    has_tax: bool | None = Field(None, alias="HasTax", description="Indicador se possui o imposto")
    incidence_type: IncidenceType | None = Field(
        None,
        alias="IncidenceType",
        description="Tipo da incidência C-crédito I-isento O-outros E=espec N-não tribut U-suspenso D-diferida S-sem aproveitamento crédito / C - Com crédito / I - Isento / O - Outros / E - Específico / N - Não tributado / U - Suspenso / D - Diferido / S - Sem aproveitamento de crédito",
    )
    value_type: float | None = Field(None, alias="ValueType", description="Tipo de valor")
    date: date_aliased | None = Field(None, alias="Date", description="Data de referência")
    kind: Kind | None = Field(None, alias="Kind", description="Tipo do imposto / D - Devido / R - Retido")
    value_due_with_held: float | None = Field(None, alias="ValueDueWithHeld", description="Valor devido/retido")
    aggregated_percentage: float | None = Field(None, alias="AggregatedPercentage", description="Percentual agregado")


class ListOfTaxes(BaseModel):
    pass


class BoardBasisInformation(BaseModel):
    board_basis_type: str | None = Field(None, alias="BoardBasisType", description="Tipo de Pensao")
    board_basis_value: float | None = Field(
        None,
        alias="BoardBasisValue",
        description="Valor da Pensao",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    breakfast_value: float | None = Field(
        None,
        alias="BreakfastValue",
        description="Valor do café da manhã",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    date_of_movement: date_aliased | None = Field(
        None, alias="DateOfMovement", description="Data de lançamento do serviço"
    )


class ItemDeliveryType(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"


class ListOfSaleItemItem(BaseModel):
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do Item da Venda")
    item_internal_id: str | None = Field(None, alias="ItemInternalId", description="InternalId do Produto")
    item_code: str | None = Field(None, alias="ItemCode", description="Código do Produto", max_length=30)
    item_order: str | None = Field(None, alias="ItemOrder", description="Ordem do Item", max_length=2)
    document_code: str | None = Field(
        None, alias="DocumentCode", description="Numero da Nota Fiscal no Item", max_length=9
    )
    serie_code: str | None = Field(
        None, alias="SerieCode", description="Numero da Serie na Nota Fiscal do Item", max_length=3
    )
    station_code: str | None = Field(None, alias="StationCode", description="Numero do PDV no Item", max_length=10)
    quantity: float | None = Field(
        None,
        alias="Quantity",
        description="Quantidade do Item",
        ge=-999999999999.999,
        le=999999999999.999,
        multiple_of=0.001,
    )
    unit_price: float | None = Field(
        None,
        alias="UnitPrice",
        description="Preço Unitário do Item",
        ge=-999999999999.999,
        le=999999999999.999,
        multiple_of=0.001,
    )
    item_price: float | None = Field(
        None,
        alias="ItemPrice",
        description="Valor do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_percentage: float | None = Field(
        None,
        alias="DiscountPercentage",
        description="Percentual de Desconto do Item",
        ge=-999.9999,
        le=999.9999,
        multiple_of=0.0001,
    )
    discount_amount: float | None = Field(
        None,
        alias="DiscountAmount",
        description="Valor do Desconto do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_total_prorated: float | None = Field(
        None,
        alias="DiscountTotalProrated",
        description="Valor do Desconto Total Rateado",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    operation_code: str | None = Field(
        None, alias="OperationCode", description="Código Fiscal de Operações e Prestações"
    )
    item_sold: str | None = Field(None, alias="ItemSold", description="Status de Vendido")
    list_of_taxes: list[list[ListOfTax] | ListOfTaxes] | None = Field(
        None, alias="ListOfTaxes", description="Lista de Impostos do Item"
    )
    increase: float | None = Field(
        None,
        alias="Increase",
        description="Valor de Acréscimo do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    lodging: str | None = Field(None, alias="Lodging", description="Produto é Diaria", max_length=1)
    is_canceled: bool | None = Field(None, alias="IsCanceled", description="Informa se o item esta cancelado")
    unit_of_measure_code: str | None = Field(None, alias="UnitOfMeasureCode", description="Unidade de Medida")
    unit_of_measure_internal_id: (
        str | None
    ) = Field(None, alias="UnitOfMeasureInternalId", description="Id de integração da Unidade de Medida")
    warehouse_code: str | None = Field(None, alias="WarehouseCode", description="Codigo do Local de Estoque(Armazem)")
    warehouse_internal_id: str | None = Field(
        None, alias="WarehouseInternalId", description="Id de integração do Local de Estoque(Armazem)"
    )
    store_identification_code: (
        str | None
    ) = Field(None, alias="StoreIdentificationCode", description="Código da Identificação da Loja de Reserva")
    ecf_taxing_code: str | None = Field(
        None, alias="ECFTaxingCode", description="Código da Tributação ECF", max_length=10
    )
    board_basis_information: BoardBasisInformation | None = Field(
        None, alias="BoardBasisInformation", description="Informações dos itens de Reserva (hotelaria)"
    )
    source_document: str | None = Field(
        None, alias="SourceDocument", description="Numero do Documento Origem", max_length=9
    )
    source_document_serie: str | None = Field(
        None, alias="SourceDocumentSerie", description="Serie de Origem do Documento de Entrada", max_length=3
    )
    source_document_item: str | None = Field(
        None, alias="SourceDocumentItem", description="Item de Origem nota de entrada", max_length=3
    )
    item_reserve_internal_id: str | None = Field(
        None, alias="ItemReserveInternalId", description="Id da Reserva do item"
    )
    item_reserve_code: str | None = Field(
        None, alias="ItemReserveCode", description="Codigo da Reserva do Item", max_length=6
    )
    item_delivery_type: ItemDeliveryType | None = Field(
        None,
        alias="ItemDeliveryType",
        description="Tipo de Entrega do Item / 1 - Retira Posterior / 2 - Retira / 3 - Entrega / 4 - Retira Posterior com Pedido",
    )
    item_delivery_date: AwareDatetime | None = Field(
        None, alias="ItemDeliveryDate", description="Data de Entrega do Item"
    )
    lot_number: str | None = Field(None, alias="LotNumber", description="Número do Lote do Produto", max_length=10)
    sub_lot_number: str | None = Field(
        None, alias="SubLotNumber", description="Número do SubLote do Produto", max_length=6
    )
    address_item: str | None = Field(
        None, alias="AddressItem", description="Endereço do produto no estoque", max_length=15
    )
    series_item: str | None = Field(None, alias="SeriesItem", description="Número de Série do Produto", max_length=20)
    item_carrier_code: str | None = Field(
        None, alias="ItemCarrierCode", description="Código da Transportadora do Item", max_length=15
    )
    item_carrier_internal_id: str | None = Field(
        None, alias="ItemCarrierInternalId", description="InternalId da Transportadora no Item", max_length=50
    )


class ListOfSaleItem(BaseModel):
    pass


class ListOfSaleConditionItem(BaseModel):
    account_receivable_document_internal_id: (
        str | None
    ) = Field(None, alias="AccountReceivableDocumentInternalId", description="InternalId do RA do cliente")
    date_of_payment: str | None = Field(None, alias="DateOfPayment", description="Data de Vencimento da Parcela")
    payment_value: float | None = Field(
        None,
        alias="PaymentValue",
        description="Valor do Pagamento",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    payment_method_code: str | None = Field(
        None, alias="PaymentMethodCode", description="Forma de Pagamento", max_length=15
    )
    payment_method_internal_id: (
        str | None
    ) = Field(None, alias="PaymentMethodInternalId", description="Chave de Integração de Forma de Pagamento")
    financial_manager_code: str | None = Field(
        None, alias="FinancialManagerCode", description="Código da Administradora Financeira", max_length=1
    )
    card_number: str | None = Field(None, alias="CardNumber", description="Numeração do Cheque", max_length=30)
    serie_check: str | None = Field(None, alias="SerieCheck", description="Série do Cheque", max_length=6)
    bank_check: str | None = Field(None, alias="BankCheck", description="Banco do Cheque", max_length=4)
    agency_check: str | None = Field(None, alias="AgencyCheck", description="Agência Bancária do Cheque", max_length=8)
    account_check: str | None = Field(
        None, alias="AccountCheck", description="Número da Conta do Cheque", max_length=20
    )
    document_of_identification: (
        str | None
    ) = (
        Field(None, alias="DocumentOfIdentification", description="Documento de Identidade do Cliente - Cheque", max_length=20)
    )
    phone_number: str | None = Field(
        None, alias="PhoneNumber", description="Telefone do Cliente - Cheque", max_length=15
    )
    eft_date: AwareDatetime | None = Field(None, alias="EftDate", description="Data do Pagamento - TEF")
    eft_document: str | None = Field(
        None, alias="EftDocument", description="Documento de Identificação TEF", max_length=9
    )
    eft_autorization: str | None = Field(
        None, alias="EftAutorization", description="Código de Autorização TEF", max_length=6
    )
    eft_cancellation_date: AwareDatetime | None = Field(
        None, alias="EftCancellationDate", description="Data de Cancelamento TEF"
    )
    eft_cancellation_document: (
        str | None
    ) = Field(None, alias="EftCancellationDocument", description="Número do Cancelamento TEF", max_length=9)
    eft_institute: str | None = Field(None, alias="EftInstitute", description="Código do Instituto TEF", max_length=16)
    unique_serial_number: str | None = Field(
        None, alias="UniqueSerialNumber", description="Código NSU - TEF", max_length=12
    )
    eft_parcel: str | None = Field(None, alias="EftParcel", description="Parcelamento TEF", max_length=3)
    financial_document_code: str | None = Field(
        None, alias="FinancialDocumentCode", description="Número do documento Financeiro", max_length=20
    )
    payment_term_code_internal_id: (
        str | None
    ) = Field(None, alias="PaymentTermCodeInternalID", description="InternalId da condição de pagamento", max_length=50)
    payment_term_code: str | None = Field(
        None, alias="PaymentTermCode", description="Condição de pagamento", max_length=3
    )
    installments: float | None = Field(None, alias="Installments", description="Quantidade de Parcelas")


class ListOfSaleCondition(BaseModel):
    pass


class ListOfTax1(BaseModel):
    taxe: Taxe | None = Field(
        None,
        alias="Taxe",
        description="Nome do Imposto (ITF, COFINS, CSLL, FABOV, FACS, INSS-PF, INSS-PJ, INSS-RUR, IOF, IR-CARRETEIRO, IR-PF, IR-PJ, IRRF–PF, IRRF–PJ, ISS, ISS-ARQ-ELET, PIS, PIS/COFINS/CSLL, PIS/COFINS-CRED, PIS/COFINS-PROD, SEST/SENAT,ICM, IPI, II, IMP_CANA, ICMS_ST, RECOLH_INSS, RETEN_ISS, RETEN_INSS, RETEN_INSS_RUR, RETEN_SEST_SENAT) / ITF - -Imposto sobre movimentação financeira / COFINS - COFINS / CSLL - CSLL / FABOV - FABOV / FACS - FACS / INSS-PF - INSS-PF / INSS-PJ - INSS-PJ / INSS-RUR - INSS-RUR / IOF - IOF / IR-CARRETEIRO - IR-CARRETEIRO / IRRF–PF - IRRF–PF / IRRF–PJ - IRRF–PJ / ISS - ISS / ISS-ARQ-ELET - ISS-ARQ-ELET / PIS - PIS / PIS/COFINS/CSLL - PIS/COFINS/CSLL / PIS/COFINS-CRED - PIS/COFINS-CRED / PIS/COFINS-PROD - PIS/COFINS-PROD / SEST/SENAT - SEST/SENAT / ICM - ICM / IPI - IPI / II - II - Imposto de Importação / IMP_CANA - IMP_CANA - Imposto da Cana / ICMS_ST - ICMS_ST - ICMS Substituicao Tributaria / RECOLH_INSS - RECOLH_INSS - Recolhimento INSS / RETEN_ISS - RETEN_ISS - Retenção ISS / RETEN_INSS - RETEN_INSS - Retenção INSS / RETEN_INSS_RUR - RETEN_INSS_RUR - Retenção INSS Rural / RETEN_SEST_SENAT - RETEN_SEST_SENAT - Retenção SEST SENAT",
    )
    country_code: str | None = Field(None, alias="CountryCode", description="Código do País")
    country_internal_id: str | None = Field(None, alias="CountryInternalId", description="InternalId do CountryCode")
    state_code: str | None = Field(None, alias="StateCode", description="Código da Unidade Federativa")
    state_internal_id: str | None = Field(None, alias="StateInternalId", description="InternalId do StateCode")
    city_code: str | None = Field(None, alias="CityCode", description="Código da Cidade")
    city_internal_id: str | None = Field(None, alias="CityInternalId", description="InternalId do CityCode")
    calculation_basis: float | None = Field(
        None, alias="CalculationBasis", description="Base de Cálculo para o Imposto"
    )
    percentage: float | None = Field(None, alias="Percentage", description="Percentual do Imposto")
    reduction_based_percent: float | None = Field(
        None, alias="ReductionBasedPercent", description="Percentual de Redução de Base"
    )
    value: float | None = Field(None, alias="Value", description="Valor do Imposto")
    reason: Reason | None = Field(
        None,
        alias="Reason",
        description="Motivo da Retenção 1-Autopeças, 2-Órgãos Públicos, 3–Serviço / 001 - Autopeças / 002 - Órgãos Públicos / 003 - Serviço",
    )
    deferral_percentage: float | None = Field(
        None, alias="DeferralPercentage", description="Percentual do Diferimento - Somente para ICMS"
    )
    deferral_value: float | None = Field(
        None, alias="DeferralValue", description="Valor do Diferimento - Somente para ICMS"
    )
    presumed_credit_percentage: (
        float | None
    ) = Field(None, alias="PresumedCreditPercentage", description="Percentual do Crédito Presumido")
    presumed_credit_value: float | None = Field(
        None, alias="PresumedCreditValue", description="Valor do Crédito Presumido"
    )
    especific_calculation_basis: (
        float | None
    ) = Field(None, alias="EspecificCalculationBasis", description="Base de Cálculo para Alíquota Específica")
    especific_aliquot: float | None = Field(None, alias="EspecificAliquot", description="Alíquota Específica")
    increase_percentage: float | None = Field(
        None, alias="IncreasePercentage", description="Percentual de Majoração do Imposto"
    )
    increase_value: float | None = Field(None, alias="IncreaseValue", description="Valor de Majoração do Imposto")
    recalculate: bool | None = Field(None, alias="Recalculate", description="Recalcular?")
    code_tax_situation: str | None = Field(None, alias="CodeTaxSituation", description="CST do imposto")
    with_holding_tax: bool | None = Field(None, alias="WithHoldingTax", description="É retenção?")
    has_tax: bool | None = Field(None, alias="HasTax", description="Indicador se possui o imposto")
    incidence_type: IncidenceType | None = Field(
        None,
        alias="IncidenceType",
        description="Tipo da incidência C-crédito I-isento O-outros E=espec N-não tribut U-suspenso D-diferida S-sem aproveitamento crédito / C - Com crédito / I - Isento / O - Outros / E - Específico / N - Não tributado / U - Suspenso / D - Diferido / S - Sem aproveitamento de crédito",
    )
    value_type: float | None = Field(None, alias="ValueType", description="Tipo de valor")
    date: date_aliased | None = Field(None, alias="Date", description="Data de referência")
    kind: Kind | None = Field(None, alias="Kind", description="Tipo do imposto / D - Devido / R - Retido")
    value_due_with_held: float | None = Field(None, alias="ValueDueWithHeld", description="Valor devido/retido")
    aggregated_percentage: float | None = Field(None, alias="AggregatedPercentage", description="Percentual agregado")


class SaleType(StrEnum):
    v = "V"
    s = "S"
    d = "D"
    b = "B"


class BookingInformation(BaseModel):
    hotel_account_code: str | None = Field(
        None, alias="HotelAccountCode", description="Codigo de Reserva do Hospede", max_length=32
    )
    checkin_date: date_aliased | None = Field(None, alias="CheckinDate", description="Data de Checkin da Reserva")
    habitational_unit_type: str | None = Field(
        None, alias="HabitationalUnitType", description="Tipo da Unidade Habitacional"
    )
    habitational_unit_number: str | None = Field(
        None, alias="HabitationalUnitNumber", description="Número da Unidade Habitacional"
    )
    main_guest_name: str | None = Field(None, alias="MainGuestName", description="Nome do hóspede principal da reserva")
    additional_guest_name: str | None = Field(
        None, alias="AdditionalGuestName", description="Nomes de todos os hóspedes da reseva, com exeção do principal"
    )
    group_name: str | None = Field(None, alias="GroupName", description="Nome do Grupo da Reserva")
    event_name: str | None = Field(None, alias="EventName", description="Nome do Evento")


class RetailSalesType(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa da venda"
    )
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId da Venda")
    seller_internal_id: str | None = Field(None, alias="SellerInternalId", description="InternalId do Vendedor")
    comission_percent: float | None = Field(
        None, alias="ComissionPercent", description="Percentual da Comissão", ge=-999.99, le=999.99, multiple_of=0.01
    )
    customer_vendor_internal_id: (
        str | None
    ) = Field(None, alias="CustomerVendorInternalId", description="InternalId do Código do Cliente")
    total_price: float | None = Field(
        None,
        alias="TotalPrice",
        description="Valor Total da Venda",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_value: float | None = Field(
        None,
        alias="DiscountValue",
        description="Valor Total de Desconto",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    increase_value: float | None = Field(
        None,
        alias="IncreaseValue",
        description="Valor de Acréscimo",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    net_price: float | None = Field(
        None,
        alias="NetPrice",
        description="Valor Liquido da Venda",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    cash_value: float | None = Field(
        None,
        alias="CashValue",
        description="Valor Pago em Dinheiro",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    checks_value: float | None = Field(
        None,
        alias="ChecksValue",
        description="Valor Pago em Cheques",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    cards_value: float | None = Field(
        None,
        alias="CardsValue",
        description="Valor Pago em Cartões de Crédito",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    debit_value: float | None = Field(
        None,
        alias="DebitValue",
        description="Valor Pago em Cartões de Débito",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    covenant_value: float | None = Field(
        None,
        alias="CovenantValue",
        description="Valor Pago com Convênio",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    vouchers_value: float | None = Field(
        None,
        alias="VouchersValue",
        description="Valor Pago com Vales",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    financed_value: float | None = Field(
        None,
        alias="FinancedValue",
        description="Valor Pago com Financiamento",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    others_value: float | None = Field(
        None,
        alias="OthersValue",
        description="Valor Pago com Outras Formas",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    input_value: float | None = Field(
        None,
        alias="InputValue",
        description="Valor de Entrada",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    issue_date_document: AwareDatetime | None = Field(
        None, alias="IssueDateDocument", description="Data de Emissão da Venda"
    )
    emis_nf: AwareDatetime | None = Field(None, alias="EmisNf", description="Data de Emissao da Nota Fiscal")
    date_time: time | None = Field(None, alias="DateTime", description="Hora de Emissao da Nota Fiscal")
    invoice_messages: str | None = Field(
        None, alias="InvoiceMessages", description="Mensagem da Nota Fiscal", max_length=60
    )
    document_code: str | None = Field(None, alias="DocumentCode", description="Numero do Documento", max_length=9)
    serie_code: str | None = Field(None, alias="SerieCode", description="Serie do Documento", max_length=5)
    num_c_fis: str | None = Field(None, alias="NumCFis", description="Numero do Cupom Fiscal", max_length=9)
    gross_price: float | None = Field(
        None,
        alias="GrossPrice",
        description="Valor Bruto da Venda",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    commodity_price: float | None = Field(
        None,
        alias="CommodityPrice",
        description="Valor Total da Mercadoria",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_percent: float | None = Field(
        None,
        alias="DiscountPercent",
        description="Percentual de Desconto da Venda",
        ge=-999.99,
        le=999.99,
        multiple_of=0.01,
    )
    operator_code: str | None = Field(None, alias="OperatorCode", description="Codigo do Operador", max_length=3)
    operator_internal_id: str | None = Field(
        None, alias="OperatorInternalId", description="InternalId do Operador", max_length=50
    )
    currency_rate: float | None = Field(
        None, alias="CurrencyRate", description="Taxa da Moeda", ge=-9999999.9999, le=9999999.9999, multiple_of=0.0001
    )
    change: float | None = Field(
        None,
        alias="Change",
        description="Valor do Troco na Venda",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    station_code: str | None = Field(None, alias="StationCode", description="Código da Estacao", max_length=3)
    discount_payment_term: float | None = Field(
        None,
        alias="DiscountPaymentTerm",
        description="Desconto Financeiro na Venda",
        ge=-999999999999.99,
        le=999999999999.99,
        multiple_of=0.01,
    )
    credit_value: float | None = Field(
        None,
        alias="CreditValue",
        description="Valor de Crédito da Venda",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    kind_of_document: str | None = Field(None, alias="KindOfDocument", description="Tipo do Documento", max_length=15)
    carrier_code: str | None = Field(None, alias="CarrierCode", description="Código da Transportadora", max_length=15)
    carrier_internal_id: str | None = Field(
        None, alias="CarrierInternalId", description="InternalId da Transportadora", max_length=50
    )
    md5: str | None = Field(None, alias="Md5", description="Código Md5", max_length=60)
    movement_number: str | None = Field(
        None, alias="MovementNumber", description="Numero do movimento do Dia", max_length=5
    )
    electronic_invoice_complement: (
        str | None
    ) = Field(None, alias="ElectronicInvoiceComplement", description="Informações Complementares NFCe", max_length=60)
    personal_identification: str | None = Field(
        None, alias="PersonalIdentification", description="CPF/CGC do Cliente", max_length=20
    )
    purchaser_name: str | None = Field(None, alias="PurchaserName", description="Nome do Adquirente", max_length=40)
    doc_foreign_purchase: str | None = Field(
        None, alias="DocForeignPurchase", description="Nome do Adquirente", max_length=40
    )
    is_canceled: bool | None = Field(None, alias="IsCanceled", description="Informa se venda esta cancelada")
    nfce_protocol: str | None = Field(None, alias="NfceProtocol", description="Protocolo NFCe", max_length=15)
    list_of_sale_item: list[list[ListOfSaleItemItem] | ListOfSaleItem] | None = Field(
        None, alias="ListOfSaleItem", description="Lista de Itens da Venda"
    )
    list_of_sale_condition: list[list[ListOfSaleConditionItem] | ListOfSaleCondition] | None = Field(
        None, alias="ListOfSaleCondition", description="Condições de Pagamento da Venda"
    )
    list_of_taxes: list[list[ListOfTax1] | ListOfTaxes] | None = Field(
        None, alias="ListOfTaxes", description="Lista de Impostos da Venda"
    )
    station_sale_point_code: str | None = Field(
        None, alias="StationSalePointCode", description="Código Ponto de Venda", max_length=30
    )
    station_sale_point_internal_id: (
        str | None
    ) = Field(None, alias="StationSalePointInternalId", description="InternalId do Ponto de Venda")
    serial_number_sat_equipament: (
        str | None
    ) = Field(None, alias="SerialNumberSATEquipament", description="Número de Série do equipamento SAT")
    sale_type: SaleType | None = Field(
        None,
        alias="SaleType",
        description="Tipo do Documento / V - Venda Cupom Fiscal / S - SAT - Sistema de Autenticação e Transmissão de Cupom Fiscal Eletrônico / D - Devolucao de Compra / B - Utiliza Fornecedor",
    )
    key_acess_n_fe: str | None = Field(None, alias="KeyAcessNFe", description="Chave de acesso NFe")
    state_tax_burden: float | None = Field(None, alias="StateTaxBurden", description="Carga Tributária Estadual")
    municipal_tax_burden: float | None = Field(
        None, alias="MunicipalTaxBurden", description="Carga Tributária Municipal"
    )
    federal_tax_burden: float | None = Field(None, alias="FederalTaxBurden", description="Carga Tributária Federal")
    tax_source: str | None = Field(None, alias="TaxSource", description="Fonte Tributária")
    booking_information: BookingInformation | None = Field(
        None, alias="BookingInformation", description="Informações de Reserva (hotelaria)"
    )
    presencial_indicator: str | None = Field(None, alias="PresencialIndicator", description="Presença Comprador")
    intermediary_code: str | None = Field(None, alias="IntermediaryCode", description="Codigo Intermediador")


class ListOfTax2(BaseModel):
    taxe: Taxe | None = Field(
        None,
        alias="Taxe",
        description="Nome do Imposto (ITF, COFINS, CSLL, FABOV, FACS, INSS-PF, INSS-PJ, INSS-RUR, IOF, IR-CARRETEIRO, IR-PF, IR-PJ, IRRF–PF, IRRF–PJ, ISS, ISS-ARQ-ELET, PIS, PIS/COFINS/CSLL, PIS/COFINS-CRED, PIS/COFINS-PROD, SEST/SENAT,ICM, IPI, II, IMP_CANA, ICMS_ST, RECOLH_INSS, RETEN_ISS, RETEN_INSS, RETEN_INSS_RUR, RETEN_SEST_SENAT) / ITF - -Imposto sobre movimentação financeira / COFINS - COFINS / CSLL - CSLL / FABOV - FABOV / FACS - FACS / INSS-PF - INSS-PF / INSS-PJ - INSS-PJ / INSS-RUR - INSS-RUR / IOF - IOF / IR-CARRETEIRO - IR-CARRETEIRO / IRRF–PF - IRRF–PF / IRRF–PJ - IRRF–PJ / ISS - ISS / ISS-ARQ-ELET - ISS-ARQ-ELET / PIS - PIS / PIS/COFINS/CSLL - PIS/COFINS/CSLL / PIS/COFINS-CRED - PIS/COFINS-CRED / PIS/COFINS-PROD - PIS/COFINS-PROD / SEST/SENAT - SEST/SENAT / ICM - ICM / IPI - IPI / II - II - Imposto de Importação / IMP_CANA - IMP_CANA - Imposto da Cana / ICMS_ST - ICMS_ST - ICMS Substituicao Tributaria / RECOLH_INSS - RECOLH_INSS - Recolhimento INSS / RETEN_ISS - RETEN_ISS - Retenção ISS / RETEN_INSS - RETEN_INSS - Retenção INSS / RETEN_INSS_RUR - RETEN_INSS_RUR - Retenção INSS Rural / RETEN_SEST_SENAT - RETEN_SEST_SENAT - Retenção SEST SENAT",
    )
    country_code: str | None = Field(None, alias="CountryCode", description="Código do País")
    country_internal_id: str | None = Field(None, alias="CountryInternalId", description="InternalId do CountryCode")
    state_code: str | None = Field(None, alias="StateCode", description="Código da Unidade Federativa")
    state_internal_id: str | None = Field(None, alias="StateInternalId", description="InternalId do StateCode")
    city_code: str | None = Field(None, alias="CityCode", description="Código da Cidade")
    city_internal_id: str | None = Field(None, alias="CityInternalId", description="InternalId do CityCode")
    calculation_basis: float | None = Field(
        None, alias="CalculationBasis", description="Base de Cálculo para o Imposto"
    )
    percentage: float | None = Field(None, alias="Percentage", description="Percentual do Imposto")
    reduction_based_percent: float | None = Field(
        None, alias="ReductionBasedPercent", description="Percentual de Redução de Base"
    )
    value: float | None = Field(None, alias="Value", description="Valor do Imposto")
    reason: Reason | None = Field(
        None,
        alias="Reason",
        description="Motivo da Retenção 1-Autopeças, 2-Órgãos Públicos, 3–Serviço / 001 - Autopeças / 002 - Órgãos Públicos / 003 - Serviço",
    )
    deferral_percentage: float | None = Field(
        None, alias="DeferralPercentage", description="Percentual do Diferimento - Somente para ICMS"
    )
    deferral_value: float | None = Field(
        None, alias="DeferralValue", description="Valor do Diferimento - Somente para ICMS"
    )
    presumed_credit_percentage: (
        float | None
    ) = Field(None, alias="PresumedCreditPercentage", description="Percentual do Crédito Presumido")
    presumed_credit_value: float | None = Field(
        None, alias="PresumedCreditValue", description="Valor do Crédito Presumido"
    )
    especific_calculation_basis: (
        float | None
    ) = Field(None, alias="EspecificCalculationBasis", description="Base de Cálculo para Alíquota Específica")
    especific_aliquot: float | None = Field(None, alias="EspecificAliquot", description="Alíquota Específica")
    increase_percentage: float | None = Field(
        None, alias="IncreasePercentage", description="Percentual de Majoração do Imposto"
    )
    increase_value: float | None = Field(None, alias="IncreaseValue", description="Valor de Majoração do Imposto")
    recalculate: bool | None = Field(None, alias="Recalculate", description="Recalcular?")
    code_tax_situation: str | None = Field(None, alias="CodeTaxSituation", description="CST do imposto")
    with_holding_tax: bool | None = Field(None, alias="WithHoldingTax", description="É retenção?")
    has_tax: bool | None = Field(None, alias="HasTax", description="Indicador se possui o imposto")
    incidence_type: IncidenceType | None = Field(
        None,
        alias="IncidenceType",
        description="Tipo da incidência C-crédito I-isento O-outros E=espec N-não tribut U-suspenso D-diferida S-sem aproveitamento crédito / C - Com crédito / I - Isento / O - Outros / E - Específico / N - Não tributado / U - Suspenso / D - Diferido / S - Sem aproveitamento de crédito",
    )
    value_type: float | None = Field(None, alias="ValueType", description="Tipo de valor")
    date: date_aliased | None = Field(None, alias="Date", description="Data de referência")
    kind: Kind | None = Field(None, alias="Kind", description="Tipo do imposto / D - Devido / R - Retido")
    value_due_with_held: float | None = Field(None, alias="ValueDueWithHeld", description="Valor devido/retido")
    aggregated_percentage: float | None = Field(None, alias="AggregatedPercentage", description="Percentual agregado")


class ListOfSaleItemTypeItem(BaseModel):
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do Item da Venda")
    item_internal_id: str | None = Field(None, alias="ItemInternalId", description="InternalId do Produto")
    item_code: str | None = Field(None, alias="ItemCode", description="Código do Produto", max_length=30)
    item_order: str | None = Field(None, alias="ItemOrder", description="Ordem do Item", max_length=2)
    document_code: str | None = Field(
        None, alias="DocumentCode", description="Numero da Nota Fiscal no Item", max_length=9
    )
    serie_code: str | None = Field(
        None, alias="SerieCode", description="Numero da Serie na Nota Fiscal do Item", max_length=3
    )
    station_code: str | None = Field(None, alias="StationCode", description="Numero do PDV no Item", max_length=10)
    quantity: float | None = Field(
        None,
        alias="Quantity",
        description="Quantidade do Item",
        ge=-999999999999.999,
        le=999999999999.999,
        multiple_of=0.001,
    )
    unit_price: float | None = Field(
        None,
        alias="UnitPrice",
        description="Preço Unitário do Item",
        ge=-999999999999.999,
        le=999999999999.999,
        multiple_of=0.001,
    )
    item_price: float | None = Field(
        None,
        alias="ItemPrice",
        description="Valor do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_percentage: float | None = Field(
        None,
        alias="DiscountPercentage",
        description="Percentual de Desconto do Item",
        ge=-999.9999,
        le=999.9999,
        multiple_of=0.0001,
    )
    discount_amount: float | None = Field(
        None,
        alias="DiscountAmount",
        description="Valor do Desconto do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_total_prorated: float | None = Field(
        None,
        alias="DiscountTotalProrated",
        description="Valor do Desconto Total Rateado",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    operation_code: str | None = Field(
        None, alias="OperationCode", description="Código Fiscal de Operações e Prestações"
    )
    item_sold: str | None = Field(None, alias="ItemSold", description="Status de Vendido")
    list_of_taxes: list[list[ListOfTax2] | ListOfTaxes] | None = Field(
        None, alias="ListOfTaxes", description="Lista de Impostos do Item"
    )
    increase: float | None = Field(
        None,
        alias="Increase",
        description="Valor de Acréscimo do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    lodging: str | None = Field(None, alias="Lodging", description="Produto é Diaria", max_length=1)
    is_canceled: bool | None = Field(None, alias="IsCanceled", description="Informa se o item esta cancelado")
    unit_of_measure_code: str | None = Field(None, alias="UnitOfMeasureCode", description="Unidade de Medida")
    unit_of_measure_internal_id: (
        str | None
    ) = Field(None, alias="UnitOfMeasureInternalId", description="Id de integração da Unidade de Medida")
    warehouse_code: str | None = Field(None, alias="WarehouseCode", description="Codigo do Local de Estoque(Armazem)")
    warehouse_internal_id: str | None = Field(
        None, alias="WarehouseInternalId", description="Id de integração do Local de Estoque(Armazem)"
    )
    store_identification_code: (
        str | None
    ) = Field(None, alias="StoreIdentificationCode", description="Código da Identificação da Loja de Reserva")
    ecf_taxing_code: str | None = Field(
        None, alias="ECFTaxingCode", description="Código da Tributação ECF", max_length=10
    )
    board_basis_information: BoardBasisInformation | None = Field(
        None, alias="BoardBasisInformation", description="Informações dos itens de Reserva (hotelaria)"
    )
    source_document: str | None = Field(
        None, alias="SourceDocument", description="Numero do Documento Origem", max_length=9
    )
    source_document_serie: str | None = Field(
        None, alias="SourceDocumentSerie", description="Serie de Origem do Documento de Entrada", max_length=3
    )
    source_document_item: str | None = Field(
        None, alias="SourceDocumentItem", description="Item de Origem nota de entrada", max_length=3
    )
    item_reserve_internal_id: str | None = Field(
        None, alias="ItemReserveInternalId", description="Id da Reserva do item"
    )
    item_reserve_code: str | None = Field(
        None, alias="ItemReserveCode", description="Codigo da Reserva do Item", max_length=6
    )
    item_delivery_type: ItemDeliveryType | None = Field(
        None,
        alias="ItemDeliveryType",
        description="Tipo de Entrega do Item / 1 - Retira Posterior / 2 - Retira / 3 - Entrega / 4 - Retira Posterior com Pedido",
    )
    item_delivery_date: AwareDatetime | None = Field(
        None, alias="ItemDeliveryDate", description="Data de Entrega do Item"
    )
    lot_number: str | None = Field(None, alias="LotNumber", description="Número do Lote do Produto", max_length=10)
    sub_lot_number: str | None = Field(
        None, alias="SubLotNumber", description="Número do SubLote do Produto", max_length=6
    )
    address_item: str | None = Field(
        None, alias="AddressItem", description="Endereço do produto no estoque", max_length=15
    )
    series_item: str | None = Field(None, alias="SeriesItem", description="Número de Série do Produto", max_length=20)
    item_carrier_code: str | None = Field(
        None, alias="ItemCarrierCode", description="Código da Transportadora do Item", max_length=15
    )
    item_carrier_internal_id: str | None = Field(
        None, alias="ItemCarrierInternalId", description="InternalId da Transportadora no Item", max_length=50
    )


class ListOfSaleItemType(RootModel[list[ListOfSaleItemTypeItem]]):
    root: list[ListOfSaleItemTypeItem]


class ListOfTax3(BaseModel):
    taxe: Taxe | None = Field(
        None,
        alias="Taxe",
        description="Nome do Imposto (ITF, COFINS, CSLL, FABOV, FACS, INSS-PF, INSS-PJ, INSS-RUR, IOF, IR-CARRETEIRO, IR-PF, IR-PJ, IRRF–PF, IRRF–PJ, ISS, ISS-ARQ-ELET, PIS, PIS/COFINS/CSLL, PIS/COFINS-CRED, PIS/COFINS-PROD, SEST/SENAT,ICM, IPI, II, IMP_CANA, ICMS_ST, RECOLH_INSS, RETEN_ISS, RETEN_INSS, RETEN_INSS_RUR, RETEN_SEST_SENAT) / ITF - -Imposto sobre movimentação financeira / COFINS - COFINS / CSLL - CSLL / FABOV - FABOV / FACS - FACS / INSS-PF - INSS-PF / INSS-PJ - INSS-PJ / INSS-RUR - INSS-RUR / IOF - IOF / IR-CARRETEIRO - IR-CARRETEIRO / IRRF–PF - IRRF–PF / IRRF–PJ - IRRF–PJ / ISS - ISS / ISS-ARQ-ELET - ISS-ARQ-ELET / PIS - PIS / PIS/COFINS/CSLL - PIS/COFINS/CSLL / PIS/COFINS-CRED - PIS/COFINS-CRED / PIS/COFINS-PROD - PIS/COFINS-PROD / SEST/SENAT - SEST/SENAT / ICM - ICM / IPI - IPI / II - II - Imposto de Importação / IMP_CANA - IMP_CANA - Imposto da Cana / ICMS_ST - ICMS_ST - ICMS Substituicao Tributaria / RECOLH_INSS - RECOLH_INSS - Recolhimento INSS / RETEN_ISS - RETEN_ISS - Retenção ISS / RETEN_INSS - RETEN_INSS - Retenção INSS / RETEN_INSS_RUR - RETEN_INSS_RUR - Retenção INSS Rural / RETEN_SEST_SENAT - RETEN_SEST_SENAT - Retenção SEST SENAT",
    )
    country_code: str | None = Field(None, alias="CountryCode", description="Código do País")
    country_internal_id: str | None = Field(None, alias="CountryInternalId", description="InternalId do CountryCode")
    state_code: str | None = Field(None, alias="StateCode", description="Código da Unidade Federativa")
    state_internal_id: str | None = Field(None, alias="StateInternalId", description="InternalId do StateCode")
    city_code: str | None = Field(None, alias="CityCode", description="Código da Cidade")
    city_internal_id: str | None = Field(None, alias="CityInternalId", description="InternalId do CityCode")
    calculation_basis: float | None = Field(
        None, alias="CalculationBasis", description="Base de Cálculo para o Imposto"
    )
    percentage: float | None = Field(None, alias="Percentage", description="Percentual do Imposto")
    reduction_based_percent: float | None = Field(
        None, alias="ReductionBasedPercent", description="Percentual de Redução de Base"
    )
    value: float | None = Field(None, alias="Value", description="Valor do Imposto")
    reason: Reason | None = Field(
        None,
        alias="Reason",
        description="Motivo da Retenção 1-Autopeças, 2-Órgãos Públicos, 3–Serviço / 001 - Autopeças / 002 - Órgãos Públicos / 003 - Serviço",
    )
    deferral_percentage: float | None = Field(
        None, alias="DeferralPercentage", description="Percentual do Diferimento - Somente para ICMS"
    )
    deferral_value: float | None = Field(
        None, alias="DeferralValue", description="Valor do Diferimento - Somente para ICMS"
    )
    presumed_credit_percentage: (
        float | None
    ) = Field(None, alias="PresumedCreditPercentage", description="Percentual do Crédito Presumido")
    presumed_credit_value: float | None = Field(
        None, alias="PresumedCreditValue", description="Valor do Crédito Presumido"
    )
    especific_calculation_basis: (
        float | None
    ) = Field(None, alias="EspecificCalculationBasis", description="Base de Cálculo para Alíquota Específica")
    especific_aliquot: float | None = Field(None, alias="EspecificAliquot", description="Alíquota Específica")
    increase_percentage: float | None = Field(
        None, alias="IncreasePercentage", description="Percentual de Majoração do Imposto"
    )
    increase_value: float | None = Field(None, alias="IncreaseValue", description="Valor de Majoração do Imposto")
    recalculate: bool | None = Field(None, alias="Recalculate", description="Recalcular?")
    code_tax_situation: str | None = Field(None, alias="CodeTaxSituation", description="CST do imposto")
    with_holding_tax: bool | None = Field(None, alias="WithHoldingTax", description="É retenção?")
    has_tax: bool | None = Field(None, alias="HasTax", description="Indicador se possui o imposto")
    incidence_type: IncidenceType | None = Field(
        None,
        alias="IncidenceType",
        description="Tipo da incidência C-crédito I-isento O-outros E=espec N-não tribut U-suspenso D-diferida S-sem aproveitamento crédito / C - Com crédito / I - Isento / O - Outros / E - Específico / N - Não tributado / U - Suspenso / D - Diferido / S - Sem aproveitamento de crédito",
    )
    value_type: float | None = Field(None, alias="ValueType", description="Tipo de valor")
    date: date_aliased | None = Field(None, alias="Date", description="Data de referência")
    kind: Kind | None = Field(None, alias="Kind", description="Tipo do imposto / D - Devido / R - Retido")
    value_due_with_held: float | None = Field(None, alias="ValueDueWithHeld", description="Valor devido/retido")
    aggregated_percentage: float | None = Field(None, alias="AggregatedPercentage", description="Percentual agregado")


class SaleItemType(BaseModel):
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do Item da Venda")
    item_internal_id: str | None = Field(None, alias="ItemInternalId", description="InternalId do Produto")
    item_code: str | None = Field(None, alias="ItemCode", description="Código do Produto", max_length=30)
    item_order: str | None = Field(None, alias="ItemOrder", description="Ordem do Item", max_length=2)
    document_code: str | None = Field(
        None, alias="DocumentCode", description="Numero da Nota Fiscal no Item", max_length=9
    )
    serie_code: str | None = Field(
        None, alias="SerieCode", description="Numero da Serie na Nota Fiscal do Item", max_length=3
    )
    station_code: str | None = Field(None, alias="StationCode", description="Numero do PDV no Item", max_length=10)
    quantity: float | None = Field(
        None,
        alias="Quantity",
        description="Quantidade do Item",
        ge=-999999999999.999,
        le=999999999999.999,
        multiple_of=0.001,
    )
    unit_price: float | None = Field(
        None,
        alias="UnitPrice",
        description="Preço Unitário do Item",
        ge=-999999999999.999,
        le=999999999999.999,
        multiple_of=0.001,
    )
    item_price: float | None = Field(
        None,
        alias="ItemPrice",
        description="Valor do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_percentage: float | None = Field(
        None,
        alias="DiscountPercentage",
        description="Percentual de Desconto do Item",
        ge=-999.9999,
        le=999.9999,
        multiple_of=0.0001,
    )
    discount_amount: float | None = Field(
        None,
        alias="DiscountAmount",
        description="Valor do Desconto do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    discount_total_prorated: float | None = Field(
        None,
        alias="DiscountTotalProrated",
        description="Valor do Desconto Total Rateado",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    operation_code: str | None = Field(
        None, alias="OperationCode", description="Código Fiscal de Operações e Prestações"
    )
    item_sold: str | None = Field(None, alias="ItemSold", description="Status de Vendido")
    list_of_taxes: list[list[ListOfTax3] | ListOfTaxes] | None = Field(
        None, alias="ListOfTaxes", description="Lista de Impostos do Item"
    )
    increase: float | None = Field(
        None,
        alias="Increase",
        description="Valor de Acréscimo do Item",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    lodging: str | None = Field(None, alias="Lodging", description="Produto é Diaria", max_length=1)
    is_canceled: bool | None = Field(None, alias="IsCanceled", description="Informa se o item esta cancelado")
    unit_of_measure_code: str | None = Field(None, alias="UnitOfMeasureCode", description="Unidade de Medida")
    unit_of_measure_internal_id: (
        str | None
    ) = Field(None, alias="UnitOfMeasureInternalId", description="Id de integração da Unidade de Medida")
    warehouse_code: str | None = Field(None, alias="WarehouseCode", description="Codigo do Local de Estoque(Armazem)")
    warehouse_internal_id: str | None = Field(
        None, alias="WarehouseInternalId", description="Id de integração do Local de Estoque(Armazem)"
    )
    store_identification_code: (
        str | None
    ) = Field(None, alias="StoreIdentificationCode", description="Código da Identificação da Loja de Reserva")
    ecf_taxing_code: str | None = Field(
        None, alias="ECFTaxingCode", description="Código da Tributação ECF", max_length=10
    )
    board_basis_information: BoardBasisInformation | None = Field(
        None, alias="BoardBasisInformation", description="Informações dos itens de Reserva (hotelaria)"
    )
    source_document: str | None = Field(
        None, alias="SourceDocument", description="Numero do Documento Origem", max_length=9
    )
    source_document_serie: str | None = Field(
        None, alias="SourceDocumentSerie", description="Serie de Origem do Documento de Entrada", max_length=3
    )
    source_document_item: str | None = Field(
        None, alias="SourceDocumentItem", description="Item de Origem nota de entrada", max_length=3
    )
    item_reserve_internal_id: str | None = Field(
        None, alias="ItemReserveInternalId", description="Id da Reserva do item"
    )
    item_reserve_code: str | None = Field(
        None, alias="ItemReserveCode", description="Codigo da Reserva do Item", max_length=6
    )
    item_delivery_type: ItemDeliveryType | None = Field(
        None,
        alias="ItemDeliveryType",
        description="Tipo de Entrega do Item / 1 - Retira Posterior / 2 - Retira / 3 - Entrega / 4 - Retira Posterior com Pedido",
    )
    item_delivery_date: AwareDatetime | None = Field(
        None, alias="ItemDeliveryDate", description="Data de Entrega do Item"
    )
    lot_number: str | None = Field(None, alias="LotNumber", description="Número do Lote do Produto", max_length=10)
    sub_lot_number: str | None = Field(
        None, alias="SubLotNumber", description="Número do SubLote do Produto", max_length=6
    )
    address_item: str | None = Field(
        None, alias="AddressItem", description="Endereço do produto no estoque", max_length=15
    )
    series_item: str | None = Field(None, alias="SeriesItem", description="Número de Série do Produto", max_length=20)
    item_carrier_code: str | None = Field(
        None, alias="ItemCarrierCode", description="Código da Transportadora do Item", max_length=15
    )
    item_carrier_internal_id: str | None = Field(
        None, alias="ItemCarrierInternalId", description="InternalId da Transportadora no Item", max_length=50
    )


class ListOfTaxesTypeItem(BaseModel):
    taxe: Taxe | None = Field(
        None,
        alias="Taxe",
        description="Nome do Imposto (ITF, COFINS, CSLL, FABOV, FACS, INSS-PF, INSS-PJ, INSS-RUR, IOF, IR-CARRETEIRO, IR-PF, IR-PJ, IRRF–PF, IRRF–PJ, ISS, ISS-ARQ-ELET, PIS, PIS/COFINS/CSLL, PIS/COFINS-CRED, PIS/COFINS-PROD, SEST/SENAT,ICM, IPI, II, IMP_CANA, ICMS_ST, RECOLH_INSS, RETEN_ISS, RETEN_INSS, RETEN_INSS_RUR, RETEN_SEST_SENAT) / ITF - -Imposto sobre movimentação financeira / COFINS - COFINS / CSLL - CSLL / FABOV - FABOV / FACS - FACS / INSS-PF - INSS-PF / INSS-PJ - INSS-PJ / INSS-RUR - INSS-RUR / IOF - IOF / IR-CARRETEIRO - IR-CARRETEIRO / IRRF–PF - IRRF–PF / IRRF–PJ - IRRF–PJ / ISS - ISS / ISS-ARQ-ELET - ISS-ARQ-ELET / PIS - PIS / PIS/COFINS/CSLL - PIS/COFINS/CSLL / PIS/COFINS-CRED - PIS/COFINS-CRED / PIS/COFINS-PROD - PIS/COFINS-PROD / SEST/SENAT - SEST/SENAT / ICM - ICM / IPI - IPI / II - II - Imposto de Importação / IMP_CANA - IMP_CANA - Imposto da Cana / ICMS_ST - ICMS_ST - ICMS Substituicao Tributaria / RECOLH_INSS - RECOLH_INSS - Recolhimento INSS / RETEN_ISS - RETEN_ISS - Retenção ISS / RETEN_INSS - RETEN_INSS - Retenção INSS / RETEN_INSS_RUR - RETEN_INSS_RUR - Retenção INSS Rural / RETEN_SEST_SENAT - RETEN_SEST_SENAT - Retenção SEST SENAT",
    )
    country_code: str | None = Field(None, alias="CountryCode", description="Código do País")
    country_internal_id: str | None = Field(None, alias="CountryInternalId", description="InternalId do CountryCode")
    state_code: str | None = Field(None, alias="StateCode", description="Código da Unidade Federativa")
    state_internal_id: str | None = Field(None, alias="StateInternalId", description="InternalId do StateCode")
    city_code: str | None = Field(None, alias="CityCode", description="Código da Cidade")
    city_internal_id: str | None = Field(None, alias="CityInternalId", description="InternalId do CityCode")
    calculation_basis: float | None = Field(
        None, alias="CalculationBasis", description="Base de Cálculo para o Imposto"
    )
    percentage: float | None = Field(None, alias="Percentage", description="Percentual do Imposto")
    reduction_based_percent: float | None = Field(
        None, alias="ReductionBasedPercent", description="Percentual de Redução de Base"
    )
    value: float | None = Field(None, alias="Value", description="Valor do Imposto")
    reason: Reason | None = Field(
        None,
        alias="Reason",
        description="Motivo da Retenção 1-Autopeças, 2-Órgãos Públicos, 3–Serviço / 001 - Autopeças / 002 - Órgãos Públicos / 003 - Serviço",
    )
    deferral_percentage: float | None = Field(
        None, alias="DeferralPercentage", description="Percentual do Diferimento - Somente para ICMS"
    )
    deferral_value: float | None = Field(
        None, alias="DeferralValue", description="Valor do Diferimento - Somente para ICMS"
    )
    presumed_credit_percentage: (
        float | None
    ) = Field(None, alias="PresumedCreditPercentage", description="Percentual do Crédito Presumido")
    presumed_credit_value: float | None = Field(
        None, alias="PresumedCreditValue", description="Valor do Crédito Presumido"
    )
    especific_calculation_basis: (
        float | None
    ) = Field(None, alias="EspecificCalculationBasis", description="Base de Cálculo para Alíquota Específica")
    especific_aliquot: float | None = Field(None, alias="EspecificAliquot", description="Alíquota Específica")
    increase_percentage: float | None = Field(
        None, alias="IncreasePercentage", description="Percentual de Majoração do Imposto"
    )
    increase_value: float | None = Field(None, alias="IncreaseValue", description="Valor de Majoração do Imposto")
    recalculate: bool | None = Field(None, alias="Recalculate", description="Recalcular?")
    code_tax_situation: str | None = Field(None, alias="CodeTaxSituation", description="CST do imposto")
    with_holding_tax: bool | None = Field(None, alias="WithHoldingTax", description="É retenção?")
    has_tax: bool | None = Field(None, alias="HasTax", description="Indicador se possui o imposto")
    incidence_type: IncidenceType | None = Field(
        None,
        alias="IncidenceType",
        description="Tipo da incidência C-crédito I-isento O-outros E=espec N-não tribut U-suspenso D-diferida S-sem aproveitamento crédito / C - Com crédito / I - Isento / O - Outros / E - Específico / N - Não tributado / U - Suspenso / D - Diferido / S - Sem aproveitamento de crédito",
    )
    value_type: float | None = Field(None, alias="ValueType", description="Tipo de valor")
    date: date_aliased | None = Field(None, alias="Date", description="Data de referência")
    kind: Kind | None = Field(None, alias="Kind", description="Tipo do imposto / D - Devido / R - Retido")
    value_due_with_held: float | None = Field(None, alias="ValueDueWithHeld", description="Valor devido/retido")
    aggregated_percentage: float | None = Field(None, alias="AggregatedPercentage", description="Percentual agregado")


class ListOfTaxesType(RootModel[list[ListOfTaxesTypeItem]]):
    root: list[ListOfTaxesTypeItem]


class TaxesType(BaseModel):
    taxe: Taxe | None = Field(
        None,
        alias="Taxe",
        description="Nome do Imposto (ITF, COFINS, CSLL, FABOV, FACS, INSS-PF, INSS-PJ, INSS-RUR, IOF, IR-CARRETEIRO, IR-PF, IR-PJ, IRRF–PF, IRRF–PJ, ISS, ISS-ARQ-ELET, PIS, PIS/COFINS/CSLL, PIS/COFINS-CRED, PIS/COFINS-PROD, SEST/SENAT,ICM, IPI, II, IMP_CANA, ICMS_ST, RECOLH_INSS, RETEN_ISS, RETEN_INSS, RETEN_INSS_RUR, RETEN_SEST_SENAT) / ITF - -Imposto sobre movimentação financeira / COFINS - COFINS / CSLL - CSLL / FABOV - FABOV / FACS - FACS / INSS-PF - INSS-PF / INSS-PJ - INSS-PJ / INSS-RUR - INSS-RUR / IOF - IOF / IR-CARRETEIRO - IR-CARRETEIRO / IRRF–PF - IRRF–PF / IRRF–PJ - IRRF–PJ / ISS - ISS / ISS-ARQ-ELET - ISS-ARQ-ELET / PIS - PIS / PIS/COFINS/CSLL - PIS/COFINS/CSLL / PIS/COFINS-CRED - PIS/COFINS-CRED / PIS/COFINS-PROD - PIS/COFINS-PROD / SEST/SENAT - SEST/SENAT / ICM - ICM / IPI - IPI / II - II - Imposto de Importação / IMP_CANA - IMP_CANA - Imposto da Cana / ICMS_ST - ICMS_ST - ICMS Substituicao Tributaria / RECOLH_INSS - RECOLH_INSS - Recolhimento INSS / RETEN_ISS - RETEN_ISS - Retenção ISS / RETEN_INSS - RETEN_INSS - Retenção INSS / RETEN_INSS_RUR - RETEN_INSS_RUR - Retenção INSS Rural / RETEN_SEST_SENAT - RETEN_SEST_SENAT - Retenção SEST SENAT",
    )
    country_code: str | None = Field(None, alias="CountryCode", description="Código do País")
    country_internal_id: str | None = Field(None, alias="CountryInternalId", description="InternalId do CountryCode")
    state_code: str | None = Field(None, alias="StateCode", description="Código da Unidade Federativa")
    state_internal_id: str | None = Field(None, alias="StateInternalId", description="InternalId do StateCode")
    city_code: str | None = Field(None, alias="CityCode", description="Código da Cidade")
    city_internal_id: str | None = Field(None, alias="CityInternalId", description="InternalId do CityCode")
    calculation_basis: float | None = Field(
        None, alias="CalculationBasis", description="Base de Cálculo para o Imposto"
    )
    percentage: float | None = Field(None, alias="Percentage", description="Percentual do Imposto")
    reduction_based_percent: float | None = Field(
        None, alias="ReductionBasedPercent", description="Percentual de Redução de Base"
    )
    value: float | None = Field(None, alias="Value", description="Valor do Imposto")
    reason: Reason | None = Field(
        None,
        alias="Reason",
        description="Motivo da Retenção 1-Autopeças, 2-Órgãos Públicos, 3–Serviço / 001 - Autopeças / 002 - Órgãos Públicos / 003 - Serviço",
    )
    deferral_percentage: float | None = Field(
        None, alias="DeferralPercentage", description="Percentual do Diferimento - Somente para ICMS"
    )
    deferral_value: float | None = Field(
        None, alias="DeferralValue", description="Valor do Diferimento - Somente para ICMS"
    )
    presumed_credit_percentage: (
        float | None
    ) = Field(None, alias="PresumedCreditPercentage", description="Percentual do Crédito Presumido")
    presumed_credit_value: float | None = Field(
        None, alias="PresumedCreditValue", description="Valor do Crédito Presumido"
    )
    especific_calculation_basis: (
        float | None
    ) = Field(None, alias="EspecificCalculationBasis", description="Base de Cálculo para Alíquota Específica")
    especific_aliquot: float | None = Field(None, alias="EspecificAliquot", description="Alíquota Específica")
    increase_percentage: float | None = Field(
        None, alias="IncreasePercentage", description="Percentual de Majoração do Imposto"
    )
    increase_value: float | None = Field(None, alias="IncreaseValue", description="Valor de Majoração do Imposto")
    recalculate: bool | None = Field(None, alias="Recalculate", description="Recalcular?")
    code_tax_situation: str | None = Field(None, alias="CodeTaxSituation", description="CST do imposto")
    with_holding_tax: bool | None = Field(None, alias="WithHoldingTax", description="É retenção?")
    has_tax: bool | None = Field(None, alias="HasTax", description="Indicador se possui o imposto")
    incidence_type: IncidenceType | None = Field(
        None,
        alias="IncidenceType",
        description="Tipo da incidência C-crédito I-isento O-outros E=espec N-não tribut U-suspenso D-diferida S-sem aproveitamento crédito / C - Com crédito / I - Isento / O - Outros / E - Específico / N - Não tributado / U - Suspenso / D - Diferido / S - Sem aproveitamento de crédito",
    )
    value_type: float | None = Field(None, alias="ValueType", description="Tipo de valor")
    date: date_aliased | None = Field(None, alias="Date", description="Data de referência")
    kind: Kind | None = Field(None, alias="Kind", description="Tipo do imposto / D - Devido / R - Retido")
    value_due_with_held: float | None = Field(None, alias="ValueDueWithHeld", description="Valor devido/retido")
    aggregated_percentage: float | None = Field(None, alias="AggregatedPercentage", description="Percentual agregado")


class BoardBasisInformationType(BaseModel):
    board_basis_type: str | None = Field(None, alias="BoardBasisType", description="Tipo de Pensao")
    board_basis_value: float | None = Field(
        None,
        alias="BoardBasisValue",
        description="Valor da Pensao",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    breakfast_value: float | None = Field(
        None,
        alias="BreakfastValue",
        description="Valor do café da manhã",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    date_of_movement: date_aliased | None = Field(
        None, alias="DateOfMovement", description="Data de lançamento do serviço"
    )


class ListOfSaleConditionTypeItem(BaseModel):
    account_receivable_document_internal_id: (
        str | None
    ) = Field(None, alias="AccountReceivableDocumentInternalId", description="InternalId do RA do cliente")
    date_of_payment: str | None = Field(None, alias="DateOfPayment", description="Data de Vencimento da Parcela")
    payment_value: float | None = Field(
        None,
        alias="PaymentValue",
        description="Valor do Pagamento",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    payment_method_code: str | None = Field(
        None, alias="PaymentMethodCode", description="Forma de Pagamento", max_length=15
    )
    payment_method_internal_id: (
        str | None
    ) = Field(None, alias="PaymentMethodInternalId", description="Chave de Integração de Forma de Pagamento")
    financial_manager_code: str | None = Field(
        None, alias="FinancialManagerCode", description="Código da Administradora Financeira", max_length=1
    )
    card_number: str | None = Field(None, alias="CardNumber", description="Numeração do Cheque", max_length=30)
    serie_check: str | None = Field(None, alias="SerieCheck", description="Série do Cheque", max_length=6)
    bank_check: str | None = Field(None, alias="BankCheck", description="Banco do Cheque", max_length=4)
    agency_check: str | None = Field(None, alias="AgencyCheck", description="Agência Bancária do Cheque", max_length=8)
    account_check: str | None = Field(
        None, alias="AccountCheck", description="Número da Conta do Cheque", max_length=20
    )
    document_of_identification: (
        str | None
    ) = (
        Field(None, alias="DocumentOfIdentification", description="Documento de Identidade do Cliente - Cheque", max_length=20)
    )
    phone_number: str | None = Field(
        None, alias="PhoneNumber", description="Telefone do Cliente - Cheque", max_length=15
    )
    eft_date: AwareDatetime | None = Field(None, alias="EftDate", description="Data do Pagamento - TEF")
    eft_document: str | None = Field(
        None, alias="EftDocument", description="Documento de Identificação TEF", max_length=9
    )
    eft_autorization: str | None = Field(
        None, alias="EftAutorization", description="Código de Autorização TEF", max_length=6
    )
    eft_cancellation_date: AwareDatetime | None = Field(
        None, alias="EftCancellationDate", description="Data de Cancelamento TEF"
    )
    eft_cancellation_document: (
        str | None
    ) = Field(None, alias="EftCancellationDocument", description="Número do Cancelamento TEF", max_length=9)
    eft_institute: str | None = Field(None, alias="EftInstitute", description="Código do Instituto TEF", max_length=16)
    unique_serial_number: str | None = Field(
        None, alias="UniqueSerialNumber", description="Código NSU - TEF", max_length=12
    )
    eft_parcel: str | None = Field(None, alias="EftParcel", description="Parcelamento TEF", max_length=3)
    financial_document_code: str | None = Field(
        None, alias="FinancialDocumentCode", description="Número do documento Financeiro", max_length=20
    )
    payment_term_code_internal_id: (
        str | None
    ) = Field(None, alias="PaymentTermCodeInternalID", description="InternalId da condição de pagamento", max_length=50)
    payment_term_code: str | None = Field(
        None, alias="PaymentTermCode", description="Condição de pagamento", max_length=3
    )
    installments: float | None = Field(None, alias="Installments", description="Quantidade de Parcelas")


class ListOfSaleConditionType(RootModel[list[ListOfSaleConditionTypeItem]]):
    root: list[ListOfSaleConditionTypeItem]


class SaleConditionType(BaseModel):
    account_receivable_document_internal_id: (
        str | None
    ) = Field(None, alias="AccountReceivableDocumentInternalId", description="InternalId do RA do cliente")
    date_of_payment: str | None = Field(None, alias="DateOfPayment", description="Data de Vencimento da Parcela")
    payment_value: float | None = Field(
        None,
        alias="PaymentValue",
        description="Valor do Pagamento",
        ge=-9999999999999.99,
        le=9999999999999.99,
        multiple_of=0.01,
    )
    payment_method_code: str | None = Field(
        None, alias="PaymentMethodCode", description="Forma de Pagamento", max_length=15
    )
    payment_method_internal_id: (
        str | None
    ) = Field(None, alias="PaymentMethodInternalId", description="Chave de Integração de Forma de Pagamento")
    financial_manager_code: str | None = Field(
        None, alias="FinancialManagerCode", description="Código da Administradora Financeira", max_length=1
    )
    card_number: str | None = Field(None, alias="CardNumber", description="Numeração do Cheque", max_length=30)
    serie_check: str | None = Field(None, alias="SerieCheck", description="Série do Cheque", max_length=6)
    bank_check: str | None = Field(None, alias="BankCheck", description="Banco do Cheque", max_length=4)
    agency_check: str | None = Field(None, alias="AgencyCheck", description="Agência Bancária do Cheque", max_length=8)
    account_check: str | None = Field(
        None, alias="AccountCheck", description="Número da Conta do Cheque", max_length=20
    )
    document_of_identification: (
        str | None
    ) = (
        Field(None, alias="DocumentOfIdentification", description="Documento de Identidade do Cliente - Cheque", max_length=20)
    )
    phone_number: str | None = Field(
        None, alias="PhoneNumber", description="Telefone do Cliente - Cheque", max_length=15
    )
    eft_date: AwareDatetime | None = Field(None, alias="EftDate", description="Data do Pagamento - TEF")
    eft_document: str | None = Field(
        None, alias="EftDocument", description="Documento de Identificação TEF", max_length=9
    )
    eft_autorization: str | None = Field(
        None, alias="EftAutorization", description="Código de Autorização TEF", max_length=6
    )
    eft_cancellation_date: AwareDatetime | None = Field(
        None, alias="EftCancellationDate", description="Data de Cancelamento TEF"
    )
    eft_cancellation_document: (
        str | None
    ) = Field(None, alias="EftCancellationDocument", description="Número do Cancelamento TEF", max_length=9)
    eft_institute: str | None = Field(None, alias="EftInstitute", description="Código do Instituto TEF", max_length=16)
    unique_serial_number: str | None = Field(
        None, alias="UniqueSerialNumber", description="Código NSU - TEF", max_length=12
    )
    eft_parcel: str | None = Field(None, alias="EftParcel", description="Parcelamento TEF", max_length=3)
    financial_document_code: str | None = Field(
        None, alias="FinancialDocumentCode", description="Número do documento Financeiro", max_length=20
    )
    payment_term_code_internal_id: (
        str | None
    ) = Field(None, alias="PaymentTermCodeInternalID", description="InternalId da condição de pagamento", max_length=50)
    payment_term_code: str | None = Field(
        None, alias="PaymentTermCode", description="Condição de pagamento", max_length=3
    )
    installments: float | None = Field(None, alias="Installments", description="Quantidade de Parcelas")


class BookingInformationType(BaseModel):
    hotel_account_code: str | None = Field(
        None, alias="HotelAccountCode", description="Codigo de Reserva do Hospede", max_length=32
    )
    checkin_date: date_aliased | None = Field(None, alias="CheckinDate", description="Data de Checkin da Reserva")
    habitational_unit_type: str | None = Field(
        None, alias="HabitationalUnitType", description="Tipo da Unidade Habitacional"
    )
    habitational_unit_number: str | None = Field(
        None, alias="HabitationalUnitNumber", description="Número da Unidade Habitacional"
    )
    main_guest_name: str | None = Field(None, alias="MainGuestName", description="Nome do hóspede principal da reserva")
    additional_guest_name: str | None = Field(
        None, alias="AdditionalGuestName", description="Nomes de todos os hóspedes da reseva, com exeção do principal"
    )
    group_name: str | None = Field(None, alias="GroupName", description="Nome do Grupo da Reserva")
    event_name: str | None = Field(None, alias="EventName", description="Nome do Evento")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedRetailSales(Paging):
    items: list[RetailSalesType] | None = None
