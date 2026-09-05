"""Suspects — generated from Suspects_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class EntityType(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"


class StrategicType(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class Origin(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_6 = "6"
    field_7 = "7"
    field_8 = "8"
    field_9 = "9"
    field_10 = "10"
    field_11 = "11"
    field_12 = "12"
    field_13 = "13"


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class ContactInformation(BaseModel):
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


class Employees(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_6 = "6"


class CompanyInfo(BaseModel):
    cnae: str | None = Field(None, alias="CNAE", description="Código CNAE", examples=["0111-3/01"], max_length=9)
    annualbilling: float | None = Field(None, alias="Annualbilling", description="Faturamento Anual", max_length=14)
    employees: Employees | None = Field(None, alias="Employees", description="Quantidade de funcionários")


class Reserv(StrEnum):
    field_1 = "1"
    field_2 = "2"


class InternalInformation(BaseModel):
    vendor_type_code: str | None = Field(None, alias="VendorTypeCode", description="Código do Vendedor")
    reserv: Reserv | None = Field(None, alias="Reserv", description="Suspect Reservado")


class MarketSegment(BaseModel):
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


class Scope(StrEnum):
    federal = "Federal"
    state = "State"
    municipal = "Municipal"


class GovernmentalInformation(BaseModel):
    id: str | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class SuspectInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Empresa")
    branch_id: str | None = Field(None, alias="BranchId", description="Filial", examples=["D MG 01"])
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    code: str | None = Field(None, alias="Code", description="Código do Suspect", examples=["000001"])
    store_id: str | None = Field(None, alias="StoreId", description="Loja do Suspect", examples=["01"])
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId da entidade")
    short_name: str | None = Field(None, alias="ShortName", description="Nome reduzido", examples=["JOHN M. CO"])
    name: str | None = Field(None, alias="Name", description="Nome da entidade", examples=["JOHN & MARY CO"])
    entity_type: EntityType | None = Field(
        None, alias="EntityType", description="Situação Jurídica da Entidade", examples=["1-Company"]
    )
    strategic_type: StrategicType | None = Field(
        None, alias="StrategicType", description="Tipo do Suspect", examples=["3"]
    )
    origin: Origin | None = Field(None, alias="Origin", description="Origem do Suspect", examples=["1"])
    origin_entity: str | None = Field(
        None, alias="OriginEntity", description="Informa a entidade relacionada à origem do Suspect", max_length=6
    )
    contact_information: ContactInformation | None = Field(
        None, alias="ContactInformation", description="Informações de Contato"
    )
    address: list[Any] | Address | None = Field(None, alias="Address", description="Endereço Principal")
    company_info: CompanyInfo | None = Field(None, alias="CompanyInfo", description="Dados da Empresa")
    internal_information: InternalInformation | None = Field(
        None, alias="InternalInformation", description="Informações Internas"
    )
    market_segment: MarketSegment | None = Field(None, alias="MarketSegment", description="Segmento de Mercado")
    register_situation: RegisterSituation | None = Field(
        None, alias="RegisterSituation", description="Status: 1 - Ativo, 2 - Inativo", examples=["1"]
    )
    suspect_situation: str | None = Field(
        None, alias="SuspectSituation", description="Status Atual.", examples=["1"], max_length=9
    )
    governmental_information: list[GovernmentalInformation] | None = Field(None, alias="GovernmentalInformation")


class CommunicationInformationType(BaseModel):
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


class GovernmentalInformationType(BaseModel):
    id: str | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Suspects(BaseModel):
    suspects: list[SuspectInfo] | None = Field(None, alias="Suspects")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedSuspects(Paging, Suspects):
    pass
