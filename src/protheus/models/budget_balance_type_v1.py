"""Tipo de Saldo Orçamentário — generated from BudgetBalanceType_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class BusinessContentType(BaseModel):
    company_id: str = Field(..., alias="CompanyId")
    branch_id: str = Field(..., alias="BranchId")
    company_internal_id: str = Field(..., alias="CompanyInternalId")
    code: str = Field(
        ..., alias="Code", description="Código da operações da planilha orçamentária", max_length=2, min_length=1
    )
    internal_id: str = Field(..., alias="InternalId", description="InternalId de Integração")
    description: str | None = Field(
        None,
        alias="Description",
        description="Descrição da operações da planilha orçamentária",
        max_length=40,
        min_length=1,
    )


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class BudgetBalanceTypeInfo(BaseModel):
    items: list[BusinessContentType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedItems(Paging, BudgetBalanceTypeInfo):
    pass
