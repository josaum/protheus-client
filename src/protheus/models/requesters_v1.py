"""Solicitante — generated from Requesters_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
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


class ContactInfo(BaseModel):
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


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class CommunicationInfo(BaseModel):
    type: Type | None = Field(
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


class PickupType(StrEnum):
    field_1 = "1"
    field_2 = "2"


class PickupDays(BaseModel):
    monday: bool | None = Field(None, alias="Monday", description="Coleta segunda-feira?", examples=[False])
    tuesday: bool | None = Field(None, alias="Tuesday", description="Coleta terça-feira?", examples=[False])
    wednesday: bool | None = Field(None, alias="Wednesday", description="Coleta quarta-feira?", examples=[False])
    thursday: bool | None = Field(None, alias="Thursday", description="Coleta quinta-feira?", examples=[False])
    friday: bool | None = Field(None, alias="Friday", description="Coleta sexta-feira?", examples=[False])
    saturday: bool | None = Field(None, alias="Saturday", description="Coleta sábado?", examples=[False])
    sunday: bool | None = Field(None, alias="Sunday", description="Coleta Domingo?", examples=[False])


class PickupInfo(BaseModel):
    transport_type_code: str | None = Field(
        None, alias="TransportTypeCode", description="Código de Tipo de Transporte", examples=["1"]
    )
    transport_type: str | None = Field(
        None, alias="TransportType", description="Descrição de Tipo de Transporte", examples=["string"]
    )
    pickup_type: PickupType | None = Field(None, alias="PickupType", description="Tipo de Coleta ", examples=["1"])
    pickup_start: str | None = Field(
        None, alias="PickupStart", description="Horário de Início de Coleta", examples=["string"]
    )
    pickup_ends: str | None = Field(
        None, alias="PickupEnds", description="Horário de Fim de Coleta", examples=["string"]
    )
    pickup_days: PickupDays | None = Field(None, alias="pickupDays", description="Requester Area Code")


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


class Scope(StrEnum):
    federal = "Federal"
    state = "State"
    municipal = "Municipal"


class GovernmentalInformation1(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class GovernmentalInformationType(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


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


class CommunicationInformationType(BaseModel):
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


class CommunicationInformationCommunicationInformationType(BaseModel):
    type: Type | None = Field(
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


class RequestersItemsInfo(BaseModel):
    product_code: str | None = Field(None, alias="ProductCode", description="Código de Produto", examples=["000001"])
    product: str | None = Field(
        None, alias="Product", description="Descrição do Produto", examples=["Produto Genérico"]
    )
    package_code: str | None = Field(None, alias="PackageCode", description="Código de Embalagem", examples=["UNI"])
    package: str | None = Field(None, alias="Package", description="Descrição da Embalagem", examples=["Unidade"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class RequestersInfo(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1"], max_length=3
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12
    )
    company_internal_id: str | None = Field(None, alias="CompanyInternalId", description="Código da Empresa")
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do Solicitante no ERP")
    code: str | None = Field(None, description="Código do Solicitante", examples=["000000099"])
    customer_code: str | None = Field(None, alias="CustomerCode", description="Código do Cliente/Fornecedor")
    customer_store_id: str | None = Field(None, alias="CustomerStoreId", description="Loja")
    name: str | None = Field(None, description="Nome do Cliente", examples=["Roberto da Silva"])
    short_name: str | None = Field(
        None, alias="shortName", description="Nome Abreviado do Cliente", examples=["Roberto"]
    )
    address: Address | None = None
    governmental_information: list[GovernmentalInformation1] | None = Field(None, alias="GovernmentalInformation")
    contact_info: ContactInfo | None = Field(
        None, alias="contactInfo", description="Tipo Genérico para informações de Contato."
    )
    communication_info: CommunicationInfo | None = Field(
        None, alias="communicationInfo", description="Informações para comunicação"
    )
    region_group_code: str | None = Field(
        None, alias="regionGroupCode", description="Código do Grupo de Região ", examples=["Q50308"]
    )
    region_group: str | None = Field(
        None, alias="regionGroup", description="Descrição Grupo de Região", examples=["string"]
    )
    pickup_info: PickupInfo | None = Field(None, alias="pickupInfo", description="PickUp Info")
    products: list[RequestersItemsInfo] | None = Field(None, alias="Products")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class Requesters(BaseModel):
    items: list[RequestersInfo] | None = None


class PagedRequesters(Paging, Requesters):
    pass
