"""Líder Direto dos Empregados — generated from EmployeesManagerDataContent_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class EmployeesManagerDataContentV1(ApiGroup):
    """Líder Direto dos Empregados (/api/rh/v1)."""

    api_id = "employees_manager_data_content_v1"
    base_path = "/api/rh/v1"

    def list_employees_manager_data_content(self, *, company_id: str | None = None, branch_id: str | None = None, employee_code: str | None = None, employee_cost_center_code: str | None = None, vision_code: str | None = None, manager_change_date: str | None = None, tenant_id: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o líder direto dos empregados

        GET /employeesManagerDataContent; operationId=getEmployeesManagerDataContent; Protheus >= 12.1.2210

        Retornar a lista dos empregados com as informações do seu respectivo líder direto.

        TOTVS note: Este verbo está disponível e utiliza os parâmetros de filtro da API.

        Response model: protheus.models.employees_manager_data_content_v1.PagedEmployeesManagerDataContent
        """
        return self._request(
            "employees_manager_data_content_v1.list_employees_manager_data_content",
            "GET",
            "/employeesManagerDataContent",
            path_params={},
            query={"companyId": company_id, "branchId": branch_id, "employeeCode": employee_code, "employeeCostCenterCode": employee_cost_center_code, "visionCode": vision_code, "managerChangeDate": manager_change_date, "page": page, "pageSize": page_size},
            headers={"tenantId": tenant_id},
            body=None,
            extra_query=extra_query,
        )

class AsyncEmployeesManagerDataContentV1(AsyncApiGroup):
    """Líder Direto dos Empregados (/api/rh/v1)."""

    api_id = "employees_manager_data_content_v1"
    base_path = "/api/rh/v1"

    async def list_employees_manager_data_content(self, *, company_id: str | None = None, branch_id: str | None = None, employee_code: str | None = None, employee_cost_center_code: str | None = None, vision_code: str | None = None, manager_change_date: str | None = None, tenant_id: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o líder direto dos empregados

        GET /employeesManagerDataContent; operationId=getEmployeesManagerDataContent; Protheus >= 12.1.2210

        Retornar a lista dos empregados com as informações do seu respectivo líder direto.

        TOTVS note: Este verbo está disponível e utiliza os parâmetros de filtro da API.

        Response model: protheus.models.employees_manager_data_content_v1.PagedEmployeesManagerDataContent
        """
        return await self._request(
            "employees_manager_data_content_v1.list_employees_manager_data_content",
            "GET",
            "/employeesManagerDataContent",
            path_params={},
            query={"companyId": company_id, "branchId": branch_id, "employeeCode": employee_code, "employeeCostCenterCode": employee_cost_center_code, "visionCode": vision_code, "managerChangeDate": manager_change_date, "page": page, "pageSize": page_size},
            headers={"tenantId": tenant_id},
            body=None,
            extra_query=extra_query,
        )
