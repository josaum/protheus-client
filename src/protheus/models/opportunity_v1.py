"""Oportunidades — generated from Opportunity_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ConsumerType(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ListofConsumer(BaseModel):
    consumer_type: ConsumerType | None = Field(
        None,
        alias="ConsumerType",
        description="Define o tipo de cliente da oportudade de venda. 1 - Cliente 2 - Prospect.",
    )
    consumer_id: str | None = Field(
        None, alias="ConsumerId", description="Código do Cliente|Prospect", examples=["CLI001"]
    )
    consumer_unit: str | None = Field(
        None, alias="ConsumerUnit", description="Loja do Cliente|Prospect", examples=["01"]
    )
    consumer_name: str | None = Field(
        None, alias="ConsumerName", description="Nome do Cliente|Prospect", examples=["Cliente Nome"]
    )


class Priority(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class Status(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_9 = "9"


class CommunicationInformation(BaseModel):
    phone_number: str | None = Field(None, alias="PhoneNumber", description="Número do telefone")
    phone_extension: str | None = Field(None, alias="PhoneExtension", description="Ramal")
    fax_number: str | None = Field(None, alias="FaxNumber", description="Número do FAX")
    fax_number_extension: str | None = Field(None, alias="FaxNumberExtension", description="Ramal do FAX")
    home_page: str | None = Field(None, alias="HomePage", description="Página da WEB")
    email: str | None = Field(None, alias="Email", description="Correio Eletrônico")


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


class OpportunityInfo(BaseModel):
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12
    )
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="Código da Empresa", examples=["T1D MG 01 000001"]
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 000001"]
    )
    code: str | None = Field(None, alias="Code", description="Código da Oportunidade", examples=["000001"])
    review: str | None = Field(None, alias="Review", description="Revisão da Oportunidade", examples=["01"])
    description: str | None = Field(
        None, alias="Description", description="Descrição da Oportunidade", examples=["Oportunidade 000001"]
    )
    seller: str | None = Field(None, alias="Seller", description="Código do Vendedor", examples=["VEND01"])
    seller_name: str | None = Field(
        None, alias="SellerName", description="Nome do Vendedor", examples=["Vendedor Nome"]
    )
    listof_consumer: list[list[Any] | ListofConsumer] | None = Field(
        None, alias="ListofConsumer", description="Informações do Cliente"
    )
    start_date: AwareDatetime | None = Field(
        None, alias="StartDate", description="Data de Inicio", examples=["1900-01-01T12:00:00Z"]
    )
    closing_date: AwareDatetime | None = Field(
        None, alias="ClosingDate", description="Data de Fechamento", examples=["1900-01-01T12:00:00Z"]
    )
    process: str | None = Field(None, alias="Process", description="Processo de Venda", examples=["000001"])
    stage: str | None = Field(None, alias="Stage", description="Estágio da Venda", examples=["000001"])
    notes: str | None = Field(None, alias="Notes", description="Notas", examples=["Anotacoes"])
    currency: float | None = Field(None, alias="Currency", description="Moeda da Verba", examples=[1], ge=1.0, le=99.0)
    priority: Priority | None = Field(
        None, alias="Priority", description="Prioridade. 1 - Baixa 2 - Media 3 - Alta.", examples=["1"]
    )
    success_factor: str | None = Field(
        None, alias="SuccessFactor", description="Fator Crítico de Sucesso", examples=["000001"]
    )
    failure_factor: str | None = Field(
        None, alias="FailureFactor", description="Fator Crítico Insucesso", examples=["000001"]
    )
    status: Status | None = Field(
        None,
        alias="Status",
        description="Status da Oportunidade. 1 - Aberto 2 - Perdido 3 - Suspenso 9 - Ganha.",
        examples=["1"],
    )
    ending: str | None = Field(None, alias="Ending", description="Código do Encerramento", examples=["000001"])
    reason: str | None = Field(
        None, alias="Reason", description="Motivo do Encerramento", examples=["Razao do Encerramento"]
    )
    date_signature: AwareDatetime | None = Field(
        None, alias="DateSignature", description="Data de Assinatura da Proposta", examples=["1900-01-01T12:00:00Z"]
    )
    comments: str | None = Field(None, alias="Comments", description="Observações da Proposta", examples=["Observacao"])
    list_of_contacts: list[ListOfContact] | None = Field(
        None, alias="ListOfContacts", description="Informações de Contato"
    )


class ConsumerData(BaseModel):
    consumer_type: ConsumerType | None = Field(
        None,
        alias="ConsumerType",
        description="Define o tipo de cliente da oportudade de venda. 1 - Cliente 2 - Prospect.",
    )
    consumer_id: str | None = Field(
        None, alias="ConsumerId", description="Código do Cliente|Prospect", examples=["CLI001"]
    )
    consumer_unit: str | None = Field(
        None, alias="ConsumerUnit", description="Loja do Cliente|Prospect", examples=["01"]
    )
    consumer_name: str | None = Field(
        None, alias="ConsumerName", description="Nome do Cliente|Prospect", examples=["Cliente Nome"]
    )


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


class Opportunity(BaseModel):
    items: list[OpportunityInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedOpportunity(Paging, Opportunity):
    pass
