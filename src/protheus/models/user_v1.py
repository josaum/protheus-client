"""Usuário — generated from User_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class UserMetadata(BaseModel):
    resource_type: str | None = Field(None, alias="resourceType", description="Tipo do dado", examples=["User"])
    created: AwareDatetime | None = Field(None, description="Data de criação do usuário")
    last_modified: AwareDatetime | None = Field(None, alias="lastModified", description="Data de última modificação")


class UserFullName(BaseModel):
    formatted: str | None = Field(None, description="Nome do usuário com formatação")
    given_name: str | None = Field(None, alias="givenName", description="Primeiro nome")
    family_name: str | None = Field(None, alias="familyName", description="Sobrenome")


class PhoneNumbers(BaseModel):
    value: str | None = Field(None, description="Numero do telefone")
    type: str | None = Field(None, description="Tipo do telefone")


class Emails(BaseModel):
    value: str | None = Field(None, description="Email do usuário")
    type: str | None = Field(None, description="Tipo do Email")
    primary: bool | None = Field(None, description="Flag para saber se é o email principal")


class Groups(BaseModel):
    value: str | None = Field(None, description="Grupo do usuário")
    display: str | None = Field(None, description="Descrição do grupo")


class Action(StrEnum):
    up_sert = "UpSert"
    delete = "Delete"


class Roles(BaseModel):
    value: str | None = Field(None, description="Papeis do usuário")
    company: str | None = Field(None, description="Código de usuário")
    action: Action | None = Field(None, description="Ação: UpSert|Delete")


class Managers(BaseModel):
    manager_id: str | None = Field(None, alias="managerId", description="Id do Supervisor do usuário")
    display_name: str | None = Field(None, alias="displayName", description="Nome do supervisor")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class UserInfo(BaseModel):
    id: str | None = Field(None, description="Código do usuário")
    meta: UserMetadata | None = Field(None, description="Metadados do usuário")
    external_id: str | None = Field(None, alias="externalId", description="Identificador externo do usuário")
    name: UserFullName | None = Field(None, description="Nome do usuário")
    user_name: str | None = Field(None, alias="userName", description="Login do usuário")
    preferred_language: str | None = Field(None, alias="preferredLanguage", description="Idioma do usuário")
    phone_numbers: list[PhoneNumbers] | None = Field(None, alias="phoneNumbers")
    emails: list[Emails] | None = None
    active: bool | None = Field(None, description="Flag de usuário ativo")
    groups: list[Groups] | None = None
    roles: list[Roles] | None = None
    title: str | None = Field(None, description="Cargo do usuário")
    manager: list[Managers] | None = None


class PostUser(UserInfo):
    password: str | None = Field(None, description="Senha do usuário")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedUsers(Paging):
    items: list[UserInfo] | None = None
