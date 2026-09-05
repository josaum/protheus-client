"""Líder Direto dos Empregados — generated from EmployeesManagerDataContent_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class EmployeesManagerDataContentItem(BaseModel):
    manager_branch: str | None = Field(None, alias="managerBranch", description="Filial do líder")
    manager_code: str | None = Field(None, alias="managerCode", description="Matrícula do líder")
    manager_name: str | None = Field(None, alias="managerName", description="Nome do líder")
    manager_full_name: str | None = Field(None, alias="managerFullName", description="Nome completo do líder")
    manager_email: str | None = Field(None, alias="managerEmail", description="E-mail do líder")
    manager_department_code: str | None = Field(
        None, alias="managerDepartmentCode", description="Código do departamento do líder"
    )
    manager_department_description: (
        str | None
    ) = Field(None, alias="managerDepartmentDescription", description="Descrição do departamento do líder")
    manager_cost_center_code: str | None = Field(
        None, alias="managerCostCenterCode", description="Código do centro de custo do líder"
    )
    manager_cost_center_description: (
        str | None
    ) = Field(None, alias="managerCostCenterDescription", description="Descrição do centro de custo do líder")
    employee_branch: str | None = Field(None, alias="employeeBranch", description="Filial do empregado")
    employee_code: str | None = Field(None, alias="employeeCode", description="Matrícula do empregado")
    employee_name: str | None = Field(None, alias="employeeName", description="Nome do empregado")
    employee_full_name: str | None = Field(None, alias="employeeFullName", description="Nome completo do empregado")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedEmployeesManagerDataContent(Paging):
    total: Any | None = Field(None, description="Indica o total de registros retornados.", examples=["1"])
    items: list[EmployeesManagerDataContentItem] | None = Field(
        None, description="Lista dos líderes diretos dos empregados."
    )


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
