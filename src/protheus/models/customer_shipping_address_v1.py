"""Endereços de Entrega do Cliente — generated from CustomerShippingAddress_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

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


class ShippingAddressInformation(BaseModel):
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


class ShippingAddres(BaseModel):
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


class CustomerShippingAddressInfo(BaseModel):
    customer_code: str | None = Field(
        None, alias="CustomerCode", description="Código do cliente/fornecedor", max_length=20
    )
    governmental_information: list[GovernmentalInformation] | GovernmentalInformation1 | None = Field(
        None, alias="GovernmentalInformation"
    )
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId da entidade")
    code: str | None = Field(None, alias="Code", description="Código do Local de Entrega")
    external_id: str | None = Field(None, alias="ExternalId", description="Id Externo do local de entrega")
    shipping_address_information: (
        ShippingAddressInformation | None
    ) = (
        Field(None, alias="ShippingAddressInformation", description="Informações do endereço de entrega - CNPJ - Inscrição Estadual")
    )
    shipping_address: list[ShippingAddres] | None = Field(
        None,
        alias="ShippingAddress",
        description="Datasul: Address = loc-entr.endereco(40), Number = ???, Complement = loc-entr.endereco_text, CityCode = ???, CityName = loc-entr.cidade(25), District = loc-entr.bairro(30), State = loc-entr.estado(4), CountryCode = loc-entr.pais, ZIPCode = loc-entr.cep(12), Region=???, POBox=loc-entr.caixa-postal",
    )
    carrier_code: str | None = Field(
        None, alias="CarrierCode", description="Código da transportadora informada no local de entrega do cliente"
    )


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


class AddressType(BaseModel):
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


class CustomerShippingAddress(BaseModel):
    items: list[CustomerShippingAddressInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedCustomerShippingAddress(Paging, CustomerShippingAddress):
    pass
