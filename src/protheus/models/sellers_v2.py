"""Vendedor — generated from Sellers_v2_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


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


class SalesChargeInterface(StrEnum):
    s = "S"
    f = "F"
    n = "N"


class SalesChargeInformation(BaseModel):
    customer_vendor_internal_id: (
        str | None
    ) = (
        Field(None, alias="customerVendorInternalId", description="Código de fornecedor do vendedor para processamento de comissões")
    )
    sales_charge_interface: SalesChargeInterface | None = Field(
        None,
        alias="salesChargeInterface",
        description="Formato de cobrança de comissões: S-Contas a Pagar;F-Folha de Pagamento;N-Sem Interface",
    )
    indirect_seller: str | None = Field(
        None, alias="indirectSeller", description="Código do vendedor indireto", max_length=16
    )
    indirect_seller_internal_id: (
        str | None
    ) = Field(None, alias="indirectSellerInternalId", description="InternalId do Vendedor Indireto")


class RepresentativeType(StrEnum):
    i = "I"
    e = "E"
    p = "P"


class SellerInfo(BaseModel):
    company_id: str | None = Field(None, alias="companyId", description="Empresa")
    branch_id: str | None = Field(None, alias="branchID", description="Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    code: str | None = Field(None, description="Código do vendedor", max_length=16)
    internal_id: str | None = Field(None, alias="internalId", description="InternalId da entidade")
    name: str | None = Field(None, description="Nome do vendedor", max_length=80)
    short_name: str | None = Field(None, alias="shortName", description="login do vendedor", max_length=25)
    personal_identification: str | None = Field(
        None, alias="personalIdentification", description="CPF do vendedor", max_length=25
    )
    seller_pass_word: str | None = Field(None, alias="sellerPassWord", description="Senha do vendedor", max_length=6)
    seller_phone_ddd: str | None = Field(None, alias="sellerPhoneDDD", description="DDD do vendedor", max_length=3)
    seller_phone: str | None = Field(None, alias="sellerPhone", description="Telefone do vendedor", max_length=15)
    seller_email: str | None = Field(None, alias="sellerEmail", description="E-mail do vendedor", max_length=80)
    address: Address | None = Field(None, description="Endereço do Vendedor")
    sales_charge_information: SalesChargeInformation | None = Field(
        None, alias="salesChargeInformation", description="Informações de comissões"
    )
    active: bool | None = Field(None, description="Vendedor ativo?", examples=[True])
    representative_type: RepresentativeType | None = Field(
        None, alias="representativeType", description="Tipo de representate: I=Interno;E=Externo;P=Parceiro"
    )


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


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Sellers(BaseModel):
    seller: list[SellerInfo] | None = Field(None, alias="Seller")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedSellers(Paging, Sellers):
    pass
