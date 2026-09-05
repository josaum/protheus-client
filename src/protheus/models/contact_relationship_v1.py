"""Relacionamento de Contatos x Entidade — generated from ContactRelationship_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ContactType(BaseModel):
    contact_code: str | None = Field(None, alias="ContactCode", description="Código do Contato", examples=["000001"])
    contact_internal_id: str | None = Field(None, alias="ContactInternalId", description="InternalId do Contato")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListofContact(BaseModel):
    items: list[ContactType] | None = None


class ListOfContacts(BaseModel):
    list_of_contacts_type: list[ContactType] | None = Field(None, alias="ListOfContactsType")


class BusinessContentType(BaseModel):
    company_id: str | None = Field(
        None,
        alias="CompanyId",
        description="Código da Empresa ou Código do Grupo da Empresa",
        examples=["T1"],
        max_length=3,
    )
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa da empresa"
    )
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId da Relacionamento do Contato x Entidade no ERP",
        examples=["D MG    SA1D MG    00000101"],
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG"], max_length=12
    )
    code: str | None = Field(None, alias="Code", description="Código da Entidade", examples=["00000101"], max_length=55)
    entity: str | None = Field(None, alias="Entity", description="Entidade", examples=["SA1"], max_length=3)
    list_of_contacts: ListOfContacts | None = Field(None, alias="ListOfContacts", description="Lista os Contatos")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedContactType(Paging, ListofContact):
    pass


class ContactRelationship(BaseModel):
    items: list[BusinessContentType] | None = None


class PagedContactRelationship(Paging, ContactRelationship):
    pass
