"""Cliente/Fornecedor — generated from CustomerVendor_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class TotvsApiTypesBasePaging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class EntityType(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"


class Marketsegment(BaseModel):
    market_segment_code: str | None = Field(None, alias="marketSegmentCode", description="Código do segmento")
    market_segment_internal_id: (
        str | None
    ) = Field(None, alias="marketSegmentInternalId", description="InternalId do MarketSegmentCode")
    market_segment_description: (
        str | None
    ) = Field(None, alias="marketSegmentDescription", description="Descrição do segmento")


class RegisterSituation(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class Scope(StrEnum):
    federal = "Federal"
    state = "State"
    municipal = "Municipal"


class GovernmentalInformation(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class City(BaseModel):
    city_code: str | None = Field(None, alias="cityCode", description="Código da cidade")
    city_internal_id: str | None = Field(None, alias="cityInternalId", description="InternalId da Cidade no ERP")
    city_description: str | None = Field(None, alias="cityDescription", description="Nome da cidade")


class State(BaseModel):
    state_id: str | None = Field(None, alias="stateId", description="Código do estado")
    state_internal_id: str | None = Field(None, alias="stateInternalId", description="InternalId do Estado no ERP")
    state_description: str | None = Field(None, alias="stateDescription", description="Nome do estado")


class Country(BaseModel):
    country_code: str | None = Field(None, alias="countryCode", description="Código do país")
    country_internal_id: str | None = Field(None, alias="countryInternalId", description="InternalId do país no ERP")
    country_description: str | None = Field(None, alias="countryDescription", description="Nome do país")


class Address(BaseModel):
    address: str | None = Field(
        None, description="endereço", examples=["Rua, Avenida, Rodovia, etc. Ex.: Avenida Braz Leme"]
    )
    number: str | None = Field(None, description="Número do endereço")
    complement: str | None = Field(None, description="Informações complementares do endereço")
    city: City | None = None
    district: str | None = Field(None, description="Bairro", examples=["Casa Verde"])
    state: State | None = None
    country: Country | None = None
    zip_code: str | None = Field(None, alias="zipCode", description="CEP", examples=["02022010"])
    region: str | None = Field(None, description="Região", examples=["Zona Norte"])
    po_box: str | None = Field(None, alias="poBox", description="Caixa postal")
    main_address: bool | None = Field(None, alias="mainAddress", description="Endereço principal?", examples=[True])
    shipping_address: bool | None = Field(
        None, alias="shippingAddress", description="Endereço de entregas?", examples=[False]
    )
    billing_address: bool | None = Field(
        None, alias="billingAddress", description="Endereço de cobrança?", examples=[True]
    )


class ShippingAddress(BaseModel):
    address: str | None = Field(
        None, description="endereço", examples=["Rua, Avenida, Rodovia, etc. Ex.: Avenida Braz Leme"]
    )
    number: str | None = Field(None, description="Número do endereço")
    complement: str | None = Field(None, description="Informações complementares do endereço")
    city: City | None = None
    district: str | None = Field(None, description="Bairro", examples=["Casa Verde"])
    state: State | None = None
    country: Country | None = None
    zip_code: str | None = Field(None, alias="zipCode", description="CEP", examples=["02022010"])
    region: str | None = Field(None, description="Região", examples=["Zona Norte"])
    po_box: str | None = Field(None, alias="poBox", description="Caixa postal")
    main_address: bool | None = Field(None, alias="mainAddress", description="Endereço principal?", examples=[True])
    shipping_address: bool | None = Field(
        None, alias="shippingAddress", description="Endereço de entregas?", examples=[False]
    )
    billing_address: bool | None = Field(
        None, alias="billingAddress", description="Endereço de cobrança?", examples=[True]
    )


class Type1(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class ListOfCommunicationInformation(BaseModel):
    type: Type1 | None = Field(
        None,
        alias="Type",
        description="Tipo do telefone / 1 - Comercial / 2 - Residencial / 3 - Fax Comercial / 4 - Fax Residencial / 5 - Celular",
    )
    phone_number: str | None = Field(None, alias="PhoneNumber", description="Número do telefone")
    phone_extension: str | None = Field(None, alias="PhoneExtension", description="Ramal")
    fax_number: str | None = Field(None, alias="FaxNumber", description="Número do FAX")
    fax_number_extension: str | None = Field(None, alias="FaxNumberExtension", description="Ramal do FAX")
    home_page: str | None = Field(None, alias="HomePage", description="Página da WEB")
    email: str | None = Field(None, alias="Email", description="Correio Eletrônico")
    dialling_code: str | None = Field(None, alias="DiallingCode", description="DDD - Discagem Direta a Distancia")
    international_dialling_code: (
        str | None
    ) = Field(None, alias="InternationalDiallingCode", description="DDI - Discagem Direta Internal")


class CommunicationInformation(BaseModel):
    phone_number: str | None = Field(None, alias="PhoneNumber", description="Número do telefone")
    phone_extension: str | None = Field(None, alias="PhoneExtension", description="Ramal")
    fax_number: str | None = Field(None, alias="FaxNumber", description="Número do FAX")
    fax_number_extension: str | None = Field(None, alias="FaxNumberExtension", description="Ramal do FAX")
    home_page: str | None = Field(None, alias="HomePage", description="Página da WEB")
    email: str | None = Field(None, alias="Email", description="Correio Eletrônico")


class ContactInformationAddress(BaseModel):
    address: str | None = Field(None, alias="Address", description="Rua, Avenida, Rodovia, etc. Ex.: Rua Nações Unidas")
    number: str | None = Field(None, alias="Number", description="Número do Endereço.")
    complement: str | None = Field(None, alias="Complement", description="Informações complementares do endereço.")
    city: City | None = Field(None, alias="City", description="Informações do Município")
    district: str | None = Field(None, alias="District", description="Bairro")
    state: State | None = Field(None, alias="State", description="Distrito")
    country: Country | None = Field(None, alias="Country", description="País")
    zip_code: str | None = Field(None, alias="ZIPCode", description="CEP")
    region: str | None = Field(None, alias="Region", description="Região")
    po_box: str | None = Field(None, alias="POBox", description="Caixa Postal")


class ListOfContact(BaseModel):
    contact_information_code: str | None = Field(None, alias="ContactInformationCode", description="Código do Contato")
    contact_information_internal_id: (
        str | None
    ) = Field(None, alias="ContactInformationInternalId", description="InternalId do ContactInformationCode")
    contact_information_title: (
        str | None
    ) = Field(None, alias="ContactInformationTitle", description="Título do Contato")
    contact_information_name: str | None = Field(None, alias="ContactInformationName", description="Nome do Contato")
    contact_information_department: (
        str | None
    ) = Field(None, alias="ContactInformationDepartment", description="Departamento do Contato")
    communication_information: (
        CommunicationInformation | None
    ) = Field(None, alias="CommunicationInformation", description="Informações para Contato")
    contact_information_address: (
        ContactInformationAddress | None
    ) = Field(None, alias="ContactInformationAddress", description="Endereço do Contato")


class CheckingAccountType(StrEnum):
    field_1 = "1"
    field_2 = "2"


class MainAccount(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ListOfBankingInformation(BaseModel):
    bank_code: int | None = Field(None, alias="bankCode", description="Código do Banco")
    bank_internal_id: str | None = Field(None, alias="bankInternalId", description="InternalId do BankCode")
    bank_name: str | None = Field(
        None, alias="bankName", description="Nome do Banco", examples=["Caixa Econômica Federal"], max_length=30
    )
    branch_code: str | None = Field(None, alias="branchCode", max_length=8)
    branch_key: str | None = Field(
        None, alias="branchKey", description="Dígito Verificador da Agência Bancária", max_length=10
    )
    checking_account_number: str | None = Field(
        None, alias="checkingAccountNumber", description="Conta Bancária do Cliente/Fornecedor", max_length=20
    )
    checking_account_number_key: (
        str | None
    ) = (
        Field(None, alias="checkingAccountNumberKey", description="Digito Conta Bancária do Cliente/Fornecedor", max_length=2)
    )
    checking_account_type: CheckingAccountType | None = Field(
        None, alias="checkingAccountType", description="Tipo da Conta Bancária do Cliente/Fornecedor"
    )
    main_account: MainAccount | None = Field(None, alias="mainAccount", description="Conta Bancária Principal")
    currency_account: str | None = Field(
        None, alias="currencyAccount", description="Moeda utilizada para os processos com a conta Bancária"
    )


class Address1(BaseModel):
    address: str | None = Field(
        None, description="endereço", examples=["Rua, Avenida, Rodovia, etc. Ex.: Avenida Braz Leme"]
    )
    number: str | None = Field(None, description="Número do endereço")
    complement: str | None = Field(None, description="Informações complementares do endereço")
    city: City | None = None
    district: str | None = Field(None, description="Bairro", examples=["Casa Verde"])
    state: State | None = None
    country: Country | None = None
    zip_code: str | None = Field(None, alias="zipCode", description="CEP", examples=["02022010"])
    region: str | None = Field(None, description="Região", examples=["Zona Norte"])
    po_box: str | None = Field(None, alias="poBox", description="Caixa postal")
    main_address: bool | None = Field(None, alias="mainAddress", description="Endereço principal?", examples=[True])
    shipping_address: bool | None = Field(
        None, alias="shippingAddress", description="Endereço de entregas?", examples=[False]
    )
    billing_address: bool | None = Field(
        None, alias="billingAddress", description="Endereço de cobrança?", examples=[True]
    )


class BillingInformation(BaseModel):
    billing_customer_code: int | None = Field(
        None, alias="billingCustomerCode", description="Código do usuário de cobrança"
    )
    billing_customer_internal_id: (
        str | None
    ) = Field(None, alias="billingCustomerInternalId", description="Billing Customer InternalId")
    address: Address1 | None = None


class VendorClassification(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"


class VendorInformation(BaseModel):
    vendor_classification: VendorClassification | None = Field(
        None, alias="vendorClassification", description="1 - Raw Material, 2 - Service, 3 - Both, 4 - Generic"
    )
    vendor_type_code: str = Field(..., alias="vendorTypeCode", description="Código do Vendedor")
    vendor_type_internal_id: str = Field(..., alias="vendorTypeInternalId", description="InternalId do VendorTypeCode")
    vendor_type_description: str | None = Field(
        None, alias="vendorTypeDescription", description="Nome/Descrição do Vendedor"
    )


class TaxPayerItem(BaseModel):
    tax_name: str | None = Field(None, alias="taxName")
    is_payer: bool | None = Field(None, alias="isPayer")
    mode: str | None = None


class FiscalInformation(BaseModel):
    category: str | None = Field(None, description="Categoria da informação fiscal", max_length=3)
    is_retention_agent: bool | None = Field(None, alias="isRetentionAgent", description="Retem impostos")
    tax_payer: list[TaxPayerItem] | None = Field(None, alias="taxPayer")


class CreditInformation(BaseModel):
    credit_indicator: int | None = Field(None, alias="creditIndicator", description="Indicador de Crédito")
    credit_evaluation: int | None = Field(None, alias="creditEvaluation", description="Avaliação de Crédito")
    shipment_credit_evaluation: (
        int | None
    ) = Field(None, alias="shipmentCreditEvaluation", description="Avaliação de Crédito para venda")
    credit_limit: float | None = Field(None, alias="creditLimit", description="Limite de Crédito")
    credit_limit_currency: int | None = Field(
        None, alias="creditLimitCurrency", description="Moeda do Limite de Crédito"
    )
    credit_limit_date: AwareDatetime | None = Field(
        None,
        alias="creditLimitDate",
        description="Data de vencimento do Limite de Crédito",
        examples=["2018-06-29T09:34:30Z"],
    )
    additional_credit_limit: float | None = Field(
        None, alias="additionalCreditLimit", description="Limite de Crédito adicional"
    )
    additional_credit_limit_currency: (
        str | None
    ) = Field(None, alias="additionalCreditLimitCurrency", description="Moeda do Limite de Crédito adicional")
    additional_credit_limit_date: (
        AwareDatetime | None
    ) = (
        Field(None, alias="additionalCreditLimitDate", description="Data de vencimento do Limite de Crédito adicional", examples=["2018-06-29T09:34:30Z"])
    )
    late_periods: int | None = Field(None, alias="latePeriods")
    balance_of_credit: float | None = Field(
        None, alias="balanceOfCredit", description="Valor do saldo restante do Cliente"
    )


class StrategicCustomerType(StrEnum):
    f = "F"
    l = "L"
    r = "R"
    s = "S"
    x = "X"


class ComplementaryFields(BaseModel):
    codcoligada: int | None = Field(None, description="Código da Coligada")
    cod_cfo: str | None = Field(None, alias="codCfo", description="Código Cliente Fornecedor")
    vendedor: str | None = Field(None, description="Nome do Vendedor")
    comprador: str | None = Field(None, description="Nome do Comprador")
    dias_atraso: int | None = Field(None, alias="diasAtraso", description="Número de Dias em Atraso")
    rec_created_by: str | None = Field(None, alias="recCreatedBy", description="Usuário criador do registro")
    rec_created_on: AwareDatetime | None = Field(
        None, alias="recCreatedOn", description="Data de criação do registro", examples=["2018-06-29T09:34:30Z"]
    )
    rec_modified_by: str | None = Field(None, alias="recModifiedBy", description="Usuário modificador do registro")
    rec_modified_on: AwareDatetime | None = Field(
        None, alias="recModifiedOn", description="Data de modificação do registro", examples=["2018-06-29T09:34:30Z"]
    )


class CustomerVendorInfo(BaseModel):
    customer_vendor_id: str | None = Field(None, alias="customerVendorId", description="customerVendorId")
    company_id: str | None = Field(None, alias="companyId", description="Empresa")
    branch_id: str | None = Field(None, alias="branchId", description="Filial", examples=["D MG 01"])
    company_internal_id: str | None = Field(
        None, alias="companyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    code: str | None = Field(None, description="Código do Cliente/Fornecedor", examples=["000001"])
    store_id: str | None = Field(None, alias="storeId", description="Loja do cliente/fornecedor", examples=["01"])
    internal_id: str | None = Field(None, alias="internalId", description="InternalId da entidade")
    short_name: str | None = Field(None, alias="shortName", description="Nome reduzido ", examples=["JOHN M. CO"])
    name: str | None = Field(None, description="Nome da entidade", examples=["JOHN & MARY CO"], max_length=40)
    type: Type | None = Field(None, description="Tipo de Entidade", examples=["1"])
    entity_type: EntityType | None = Field(
        None, alias="entityType", description="Situação Jurídica da Entidade", examples=["1-Company"]
    )
    marketsegment: Marketsegment | None = Field(None, description="Segmento de Mercado")
    registerdate: AwareDatetime | None = Field(
        None, description="Data da implantação do registro", examples=["2018-06-29T09:34:30Z"]
    )
    register_situation: RegisterSituation | None = Field(
        None,
        alias="registerSituation",
        description="Status: 1 - Ativo, 2 - Inativo, 3 - Cancelado, 4 - Pendente, 5 -Suspenso",
        examples=["1"],
    )
    comments: str | None = Field(
        None, description="Observações", examples=["Lorem ipsum dolor sit amet, consectetur adipiscing elit."]
    )
    governmental_information: list[GovernmentalInformation] | None = Field(None, alias="governmentalInformation")
    address: Address | None = Field(None, description="Endereço Principal")
    shipping_address: ShippingAddress | None = Field(None, alias="shippingAddress", description="Endereço de entrega")
    list_of_communication_information: list[ListOfCommunicationInformation] | None = Field(
        None, alias="listOfCommunicationInformation", description="Informações de comunicação"
    )
    list_of_contacts: list[ListOfContact] | None = Field(
        None, alias="listOfContacts", description="Informações de Contato"
    )
    list_of_banking_information: list[ListOfBankingInformation] | None = Field(None, alias="listOfBankingInformation")
    billing_information: BillingInformation | None = Field(None, alias="billingInformation")
    vendor_information: VendorInformation | None = Field(
        None, alias="vendorInformation", description="Dados do Vendedor vinculado ao Cliente"
    )
    fiscal_information: FiscalInformation | None = Field(
        None, alias="fiscalInformation", description="Informações Fiscais"
    )
    credit_information: CreditInformation | None = Field(
        None, alias="creditInformation", description="Informações de Crédito"
    )
    payment_condition_code: str | None = Field(
        None, alias="paymentConditionCode", description="Código do Prazo de Pagamento", max_length=3
    )
    payment_condition_internal_id: (
        str | None
    ) = Field(None, alias="paymentConditionInternalId", description="InternalId do PaymentConditionCode")
    price_list_header_item_code: (
        str | None
    ) = Field(None, alias="priceListHeaderItemCode", description="Código da Tabela de Preço", max_length=3)
    price_list_header_item_internal_id: (
        str | None
    ) = Field(None, alias="priceListHeaderItemInternalId", description="InternalId do PriceListHeaderItemCode")
    carrier_code: int | None = Field(
        None, alias="carrierCode", description="Código da Transportadora default do Cliente"
    )
    strategic_customer_type: StrategicCustomerType | None = Field(
        None, alias="strategicCustomerType", description="Tipo estratégico da Entidade", examples=["3=Revendedor"]
    )
    rate_discount: float | None = Field(None, alias="rateDiscount", description="Percentual de Desconto|Bonificação")
    seller_code: str | None = Field(None, alias="sellerCode", description="Código do representante")
    seller_internal_id: str | None = Field(None, alias="sellerInternalId", description="InternalId do SellerCode")
    classification: str | None = Field(None, description="Classificação do tipo de Lançamento Cliente Fornecedor")
    rec_created_by: str | None = Field(None, alias="recCreatedBy", description="Usuário criador do registro")
    rec_created_on: AwareDatetime | None = Field(
        None, alias="recCreatedOn", description="Data de criação do registro", examples=["2018-06-29T09:34:30Z"]
    )
    rec_modified_by: str | None = Field(None, alias="recModifiedBy", description="Usuário modificador do registro")
    rec_modified_on: AwareDatetime | None = Field(
        None, alias="recModifiedOn", description="Data de modificação do registro", examples=["2018-06-29T09:34:30Z"]
    )
    credit_limit: float | None = Field(None, alias="creditLimit", description="Limite de Crédito")
    last_change_date: AwareDatetime | None = Field(
        None, alias="lastChangeDate", description="Data da Útima Alteração", examples=["2018-06-29T09:34:30Z"]
    )
    optional_value1: float | None = Field(None, alias="optionalValue1", description="Valor Opcional 1")
    optional_value2: float | None = Field(None, alias="optionalValue2", description="Valor Opcional 2")
    optional_value3: float | None = Field(None, alias="optionalValue3", description="Valor Opcional 3")
    patrimony: float | None = Field(None, description="Valor Patrimonial")
    employees_number: int | None = Field(None, alias="employeesNumber", description="Número de Funcionários")
    classification_company_id: (
        int | None
    ) = Field(None, alias="classificationCompanyId", description="Coligada do Tipo de Cliente Fornecedor")
    contributor: int | None = Field(None, description="Contribuinte")
    blocked: int | None = Field(None, description="Bloqueado")
    provider_shipping_price: float | None = Field(None, alias="providerShippingPrice", description="Valor do Frete")
    taker_type: int | None = Field(None, alias="takerType", description="Tomador")
    iss_contributor: int | None = Field(None, alias="issContributor", description="Contribuinte ISS")
    dependents_number: int | None = Field(None, alias="dependentsNumber", description="Número de Dependentes")
    public_body: int | None = Field(None, alias="publicBody", description="Orgão Público")
    self_employed_category: int | None = Field(None, alias="selfEmployedCategory", description="Categoria do Autonômo")
    customer_vendor_identity_id: (
        int | None
    ) = (
        Field(None, alias="customerVendorIdentityId", description="ID do Cliente/Fornecedor com auto incremento na base")
    )
    other_deductions_irrf_calculations: (
        float | None
    ) = (
        Field(None, alias="otherDeductionsIRRFCalculations", description="Valor de outras deduções para cálculo de IRRF")
    )
    iss_regime: str | None = Field(None, alias="issRegime", description="Regime de ISS")
    iss_retention_responsible: str | None = Field(None, alias="issRetentionResponsible", description="Retenção de ISS")
    fuel_operation_type: int | None = Field(
        None, alias="fuelOperationType", description="Tipo de Operação com Combustível"
    )
    size: int | None = Field(None, description="Porte da Empresa")
    activity_branch: int | None = Field(None, alias="activityBranch", description="Ramo de Atividade")
    type_contributor_inss: int | None = Field(
        None, alias="typeContributorINSS", description="Tipo de Contribuinte de INSS"
    )
    nationality: int | None = Field(None, description="Nacionalidade do Cliente Fornecedor")
    tax_code_colcfo: int | None = Field(None, alias="taxCodeColcfo", description="Coligada da Classificação Fiscal")
    calculates_avp: int | None = Field(None, alias="calculatesAVP", description="Calcula AVP")
    nif: str | None = Field(None, description="Classificação fiscal")
    nif_situation: int | None = Field(None, alias="nifSituation", description="Situação do NIF")
    income_type: str | None = Field(None, alias="incomeType", description="Tipo de Rendimento")
    taxation_form: str | None = Field(None, alias="taxationForm", description="Forma de Tributação")
    innovate_auto: int | None = Field(
        None, description="Campo para a geração da rotina Inovar Auto, implementado no Aplicativos Gestão Fiscal"
    )
    formula_application: str | None = Field(
        None, alias="formulaApplication", description="Código da Aplicação da Fórmula"
    )
    automatic_debit_checker_type: (
        str | None
    ) = (
        Field(None, alias="automaticDebitCheckerType", description="Dígito verificador do identificador de débito automático")
    )
    executing_entity_paa: str | None = Field(
        None,
        alias="executingEntityPaa",
        description="Entidade é executora do Programa de Aquisição de Alimentos – PAA (Sim ou Não)",
    )
    own_work: int | None = Field(None, alias="ownWork", description="Obra Própria")
    retired_pensioner: int | None = Field(
        None, alias="retiredPensioner", description="Identifica o aposentado ou pensionista"
    )
    social_category_id: int | None = Field(None, alias="socialCategoryId", description="Categoria e-Social")
    cooperative_partner: int | None = Field(None, alias="cooperativePartner", description="Sócio Cooperado")
    complementary_fields: ComplementaryFields | None = Field(
        None, alias="complementaryFields", description="Campos Complementares"
    )


class GovernmentalInformationType(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class AddressType(BaseModel):
    address: str | None = Field(
        None, description="endereço", examples=["Rua, Avenida, Rodovia, etc. Ex.: Avenida Braz Leme"]
    )
    number: str | None = Field(None, description="Número do endereço")
    complement: str | None = Field(None, description="Informações complementares do endereço")
    city: City | None = None
    district: str | None = Field(None, description="Bairro", examples=["Casa Verde"])
    state: State | None = None
    country: Country | None = None
    zip_code: str | None = Field(None, alias="zipCode", description="CEP", examples=["02022010"])
    region: str | None = Field(None, description="Região", examples=["Zona Norte"])
    po_box: str | None = Field(None, alias="poBox", description="Caixa postal")
    main_address: bool | None = Field(None, alias="mainAddress", description="Endereço principal?", examples=[True])
    shipping_address: bool | None = Field(
        None, alias="shippingAddress", description="Endereço de entregas?", examples=[False]
    )
    billing_address: bool | None = Field(
        None, alias="billingAddress", description="Endereço de cobrança?", examples=[True]
    )


class CityType(BaseModel):
    city_code: str | None = Field(None, alias="cityCode", description="Código da cidade")
    city_internal_id: str | None = Field(None, alias="cityInternalId", description="InternalId da Cidade no ERP")
    city_description: str | None = Field(None, alias="cityDescription", description="Nome da cidade")


class StateType(BaseModel):
    state_id: str | None = Field(None, alias="stateId", description="Código do estado")
    state_internal_id: str | None = Field(None, alias="stateInternalId", description="InternalId do Estado no ERP")
    state_description: str | None = Field(None, alias="stateDescription", description="Nome do estado")


class CountryType(BaseModel):
    country_code: str | None = Field(None, alias="countryCode", description="Código do país")
    country_internal_id: str | None = Field(None, alias="countryInternalId", description="InternalId do país no ERP")
    country_description: str | None = Field(None, alias="countryDescription", description="Nome do país")


class CommunicationInformationType(BaseModel):
    type: Type1 | None = Field(
        None,
        alias="Type",
        description="Tipo do telefone / 1 - Comercial / 2 - Residencial / 3 - Fax Comercial / 4 - Fax Residencial / 5 - Celular",
    )
    phone_number: str | None = Field(None, alias="PhoneNumber", description="Número do telefone")
    phone_extension: str | None = Field(None, alias="PhoneExtension", description="Ramal")
    fax_number: str | None = Field(None, alias="FaxNumber", description="Número do FAX")
    fax_number_extension: str | None = Field(None, alias="FaxNumberExtension", description="Ramal do FAX")
    home_page: str | None = Field(None, alias="HomePage", description="Página da WEB")
    email: str | None = Field(None, alias="Email", description="Correio Eletrônico")
    dialling_code: str | None = Field(None, alias="DiallingCode", description="DDD - Discagem Direta a Distancia")
    international_dialling_code: (
        str | None
    ) = Field(None, alias="InternationalDiallingCode", description="DDI - Discagem Direta Internal")


class ContactInformationAddress1(BaseModel):
    address: str | None = Field(None, alias="Address", description="Rua, Avenida, Rodovia, etc. Ex.: Rua Nações Unidas")
    number: str | None = Field(None, alias="Number", description="Número do Endereço.")
    complement: str | None = Field(None, alias="Complement", description="Informações complementares do endereço.")
    city: City | None = Field(None, alias="City", description="Informações do Município")
    district: str | None = Field(None, alias="District", description="Bairro")
    state: State | None = Field(None, alias="State", description="Distrito")
    country: Country | None = Field(None, alias="Country", description="País")
    zip_code: str | None = Field(None, alias="ZIPCode", description="CEP")
    region: str | None = Field(None, alias="Region", description="Região")
    po_box: str | None = Field(None, alias="POBox", description="Caixa Postal")


class ContactInformationType(BaseModel):
    contact_information_code: str | None = Field(None, alias="ContactInformationCode", description="Código do Contato")
    contact_information_internal_id: (
        str | None
    ) = Field(None, alias="ContactInformationInternalId", description="InternalId do ContactInformationCode")
    contact_information_title: (
        str | None
    ) = Field(None, alias="ContactInformationTitle", description="Título do Contato")
    contact_information_name: str | None = Field(None, alias="ContactInformationName", description="Nome do Contato")
    contact_information_department: (
        str | None
    ) = Field(None, alias="ContactInformationDepartment", description="Departamento do Contato")
    communication_information: (
        CommunicationInformation | None
    ) = Field(None, alias="CommunicationInformation", description="Informações para Contato")
    contact_information_address: (
        ContactInformationAddress1 | None
    ) = Field(None, alias="ContactInformationAddress", description="Endereço do Contato")


class CommunicationInformationCommunicationInformationType(BaseModel):
    phone_number: str | None = Field(None, alias="PhoneNumber", description="Número do telefone")
    phone_extension: str | None = Field(None, alias="PhoneExtension", description="Ramal")
    fax_number: str | None = Field(None, alias="FaxNumber", description="Número do FAX")
    fax_number_extension: str | None = Field(None, alias="FaxNumberExtension", description="Ramal do FAX")
    home_page: str | None = Field(None, alias="HomePage", description="Página da WEB")
    email: str | None = Field(None, alias="Email", description="Correio Eletrônico")


class AddressAddressType(BaseModel):
    address: str | None = Field(None, alias="Address", description="Rua, Avenida, Rodovia, etc. Ex.: Rua Nações Unidas")
    number: str | None = Field(None, alias="Number", description="Número do Endereço.")
    complement: str | None = Field(None, alias="Complement", description="Informações complementares do endereço.")
    city: City | None = Field(None, alias="City", description="Informações do Município")
    district: str | None = Field(None, alias="District", description="Bairro")
    state: State | None = Field(None, alias="State", description="Distrito")
    country: Country | None = Field(None, alias="Country", description="País")
    zip_code: str | None = Field(None, alias="ZIPCode", description="CEP")
    region: str | None = Field(None, alias="Region", description="Região")
    po_box: str | None = Field(None, alias="POBox", description="Caixa Postal")


class BankingInformation(BaseModel):
    bank_code: int | None = Field(None, alias="bankCode", description="Código do Banco")
    bank_internal_id: str | None = Field(None, alias="bankInternalId", description="InternalId do BankCode")
    bank_name: str | None = Field(
        None, alias="bankName", description="Nome do Banco", examples=["Caixa Econômica Federal"], max_length=30
    )
    branch_code: str | None = Field(None, alias="branchCode", max_length=8)
    branch_key: str | None = Field(
        None, alias="branchKey", description="Dígito Verificador da Agência Bancária", max_length=10
    )
    checking_account_number: str | None = Field(
        None, alias="checkingAccountNumber", description="Conta Bancária do Cliente/Fornecedor", max_length=20
    )
    checking_account_number_key: (
        str | None
    ) = (
        Field(None, alias="checkingAccountNumberKey", description="Digito Conta Bancária do Cliente/Fornecedor", max_length=2)
    )
    checking_account_type: CheckingAccountType | None = Field(
        None, alias="checkingAccountType", description="Tipo da Conta Bancária do Cliente/Fornecedor"
    )
    main_account: MainAccount | None = Field(None, alias="mainAccount", description="Conta Bancária Principal")
    currency_account: str | None = Field(
        None, alias="currencyAccount", description="Moeda utilizada para os processos com a conta Bancária"
    )


class TaxPayerType(BaseModel):
    tax_name: str | None = Field(None, alias="taxName")
    is_payer: bool | None = Field(None, alias="isPayer")
    mode: str | None = None


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class CustomerVendors(TotvsApiTypesBasePaging):
    items: list[CustomerVendorInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedCustomerVendors(Paging, CustomerVendors):
    pass
