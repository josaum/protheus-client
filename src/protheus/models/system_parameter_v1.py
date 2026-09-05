"""Parametros de Sistema — generated from SystemParameter_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Scope(StrEnum):
    global_ = "global"
    company = "company"
    company_user = "companyUser"
    user = "user"


class Group(BaseModel):
    name: str | None = None
    display_name: dict[str, Any] | None = Field(None, alias="displayName")
    custom_data: dict[str, Any] | None = Field(None, alias="customData")


class ParameterDescription(BaseModel):
    language: str | None = Field(
        None,
        description="Idioma da descrição do paramêtro - deverá obedecer a ISO6391 (exemplo em https://www.andiamo.co.uk/resources/iso-language-codes)",
    )
    description_text: str | None = Field(None, alias="descriptionText", description="Texto da descrição do paramêtro")


class ParameterValues(BaseModel):
    language: str | None = Field(None, description="Idioma do valor do paramêtro")
    parameter_value: str | None = Field(None, alias="parameterValue", description="Valor do paramêtro")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ParameterInfo(BaseModel):
    system_parameter_id: str | None = Field(
        None, alias="systemParameterId", description="Identificador parâmetro de sistema"
    )
    company_id: str | None = Field(None, alias="companyID", description="Código da empresa")
    branch_id: str | None = Field(None, alias="branchID", description="Código da Filial")
    code: str = Field(..., description="Código do parâmetro")
    type: str = Field(..., description="Tipo do paramêtro")
    description: list[ParameterDescription]
    value: list[ParameterValues] | None = None
    scope: Scope | None = None
    group: Group | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class SystemParameters(BaseModel):
    items: list[ParameterInfo] | None = None


class PagedParameters(Paging, SystemParameters):
    pass
