"""Contatos — generated from Contact_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date
from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


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


class GovernmentalInformation1(BaseModel):
    pass


class Gender(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_ = ""


class Requester(StrEnum):
    field_1 = "1"
    field_2 = "2"


class Situation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class GovernmentalInformation2(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")
    scope: Scope = Field(..., description="Federal - Federal / State - Estadual / Municipal - Municipal")
    name: str
    issue_on: date | None = Field(None, alias="issueOn")
    expires_on: date | None = Field(None, alias="expiresOn")


class GovernmentalInformationModel(RootModel[list[GovernmentalInformation2]]):
    root: list[GovernmentalInformation2]


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
    phone_ddd: str | None = Field(None, alias="PhoneDDD")
    phone_number: str | None = Field(None, alias="PhoneNumber")
    phone_extension: str | None = Field(None, alias="PhoneExtension")
    fax_ddd: str | None = Field(None, alias="FaxDDD")
    fax_number: str | None = Field(None, alias="FaxNumber")
    fax_number_extension: str | None = Field(None, alias="FaxNumberExtension")
    home_page: str | None = Field(None, alias="HomePage")
    email: str | None = Field(None, alias="Email")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ContactInfo(BaseModel):
    contact_id: str | None = Field(None, alias="contactId", description="contactId")
    company_id: str | None = Field(None, alias="companyId", description="Código da Filial")
    branch_id: str | None = Field(
        None, alias="branchId", description="Código da Empresa ou Código do Grupo da Empresa", examples=["D MG    "]
    )
    company_internal_id: str | None = Field(
        None, alias="companyInternalId", description="InternalId da chave completa da empresa"
    )
    code: str | None = Field(None, description="Código do Contato", examples=["000001"])
    internal_id: str | None = Field(None, alias="internalId", description="InternalId de Integração")
    name: str | None = Field(None, description="Nome do Contato", examples=["JOHN SMITH"])
    governmental_information: list[GovernmentalInformation] | GovernmentalInformation1 | None = Field(
        None, alias="governmentalInformation", description="Informações Governamentais"
    )
    address: list[AddressType] | None = None
    list_of_communication_information: list[CommunicationInformationType] | None = Field(
        None, alias="listOfCommunicationInformation", description="Informações de comunicação"
    )
    treatment: str | None = Field(None, description="Tratamento do Contato", examples=["01"])
    gender: Gender | None = Field(None, description="Genero : 1= Masculino;2= Feminino", examples=["1"])
    birthday: str | None = Field(None, description="Data de Nascimento", examples=["19000101"])
    requester: Requester | None = Field(None, description="Solicitante? : 1-Sim;2-Não", examples=["2"])
    situation: Situation | None = Field(None, description="Situação: 1-Ativo / 2-Bloqueado", examples=["2"])


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedContacts(Paging):
    items: list[ContactInfo] | None = None
