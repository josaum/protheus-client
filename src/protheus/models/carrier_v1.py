"""Transportadora — generated from Carrier_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class RegisterSituation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class Scope(StrEnum):
    federal = "Federal"
    state = "State"
    municipal = "Municipal"


class GovernamentalInformation(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class GovernamentalInformation1(BaseModel):
    pass


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class ListofComunicationInformation(BaseModel):
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


class CarrierType(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class GovernmentalInformation1(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class GovernmentalInformation(RootModel[list[GovernmentalInformation1]]):
    root: list[GovernmentalInformation1]


class GovernmentalInformationType(BaseModel):
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


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Addres(BaseModel):
    items: list[AddressType] | None = None


class CarrierInfo(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "])
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="Código da Empresa", examples=["T1D MG 01 000001"]
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 000001"]
    )
    code: str | None = Field(None, alias="Code", description="Código da Transportadora", examples=["000001"])
    name: str | None = Field(
        None, alias="Name", description="Nome da Transportadora", examples=["Transportadora Ex CO"], max_length=40
    )
    short_name: str | None = Field(
        None, alias="ShortName", description="Nome reduzido da transportadora", examples=["Transportadora Ex"]
    )
    register_situation: RegisterSituation | None = Field(
        None, alias="RegisterSituation", description="Registro bloqueado: 1=Sim;2=Não", examples=["1"]
    )
    governamental_information: list[list[GovernamentalInformation] | GovernamentalInformation1] | None = Field(
        None, alias="governamentalInformation", description="Informações Governamentais"
    )
    address: list[Addres] | None = Field(None, description="Informações de endereço")
    listof_comunication_information: list[ListofComunicationInformation] | None = Field(
        None, alias="listofComunicationInformation", description="Informações de comunicação"
    )
    carrier_type: CarrierType | None = Field(
        None,
        alias="CarrierType",
        description="Indica o tipo de transportador 1=Inscrito; 2=Não inscrito; 3=Autônomo",
        examples=["1"],
    )


class Address(BaseModel):
    items: list[AddressType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class Carrier(BaseModel):
    items: list[CarrierInfo] | None = None


class PagedCarriers(Paging, Carrier):
    pass
