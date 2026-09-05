"""Perfil de Aprovação — generated from ApprovalProfile_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class TypeProfile(StrEnum):
    d = "D"
    s = "S"
    m = "M"


class ApprovalProfileInfo(BaseModel):
    company_internal_id: str | None = Field(
        None, alias="companyInternalId", description="InternalId da chave completa de empresa do produto."
    )
    branch_id: str | None = Field(None, alias="branchId", description="ID Filial", examples=["M SP 01"], max_length=12)
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId da entidade")
    code: str | None = Field(None, description="Código do Perfil de Aprovação", examples=["000001"], max_length=4)
    description_profile: str | None = Field(
        None, alias="descriptionProfile", description="Descrição do Perfil de Aprovação.", examples=[""], max_length=30
    )
    approve_value_limit_min: float | None = Field(
        None,
        alias="approveValueLimitMin",
        description="Valor Minimo do Limite de Aprovação do Perfil.",
        examples=["0.00"],
        max_length=17,
    )
    approve_value_limit_max: float | None = Field(
        None,
        alias="approveValueLimitMax",
        description="Valor Máximo do Limite de Aprovação do Perfil.",
        examples=["0.00"],
        max_length=17,
    )
    approve_limit_approver: float | None = Field(
        None, alias="approveLimitApprover", description="Limite do Aprovador", examples=["0.00"], max_length=14
    )
    type_profile: TypeProfile | None = Field(
        None,
        alias="typeProfile",
        description="Tipo de limite que sera atribuido D=Diario/S=Semanal/M=Mensal. O Padrão é D=Diario.",
        examples=["D - Diario, S - Semanal, M - Mensal."],
    )
    currency_profile_approve: float | None = Field(
        None, alias="currencyProfileApprove", description="Código de Moeda.", examples=[""], max_length=2
    )
    expense_type_initial: float | None = Field(
        None, alias="expenseTypeInitial", description="", examples=[""], max_length=4
    )
    expense_type_end: float | None = Field(None, alias="expenseTypeEnd", description="", examples=[""], max_length=4)
    version: float | None = Field(None, description="", examples=[""], max_length=3)
    situation: str | None = Field(None, description="Situação da grade de aprovação", max_length=1)


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedapprovalProfile(Paging):
    items: list[ApprovalProfileInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
