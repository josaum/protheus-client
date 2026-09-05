"""Relação de Funcionários - Global — generated from EmployeeDataContent_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class EmployeeDataContentV1(ApiGroup):
    """Relação de Funcionários - Global (/api/rh/v1)."""

    api_id = "employee_data_content_v1"
    base_path = "/api/rh/v1"

    def list_employee_data_content(self, *, product: str | None = None, date_modified: str | None = None, companyid: str | None = None, branch_id: str | None = None, tenant_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de funcionários e seus respectivos dados complementares

        GET /employeeDataContent; operationId=getEmployeeDataContent; Protheus >= 12.1.25

        Retorna todos os registros de funcionários e seus respectvos departamentos, centro de custos, cargos, funções e demais informações. Para funcionamento correto no Protheus, os campos de logs de auditoria RA_USERLGA e RA_USERLGI devem estar habilitados no módulo SIGACFG.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.employee_data_content_v1.PagedEmployeeDataContent
        """
        return self._request(
            "employee_data_content_v1.list_employee_data_content",
            "GET",
            "/employeeDataContent",
            path_params={},
            query={"product": product, "dateModified": date_modified, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={"tenantId": tenant_id},
            body=None,
            extra_query=extra_query,
        )

class AsyncEmployeeDataContentV1(AsyncApiGroup):
    """Relação de Funcionários - Global (/api/rh/v1)."""

    api_id = "employee_data_content_v1"
    base_path = "/api/rh/v1"

    async def list_employee_data_content(self, *, product: str | None = None, date_modified: str | None = None, companyid: str | None = None, branch_id: str | None = None, tenant_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de funcionários e seus respectivos dados complementares

        GET /employeeDataContent; operationId=getEmployeeDataContent; Protheus >= 12.1.25

        Retorna todos os registros de funcionários e seus respectvos departamentos, centro de custos, cargos, funções e demais informações. Para funcionamento correto no Protheus, os campos de logs de auditoria RA_USERLGA e RA_USERLGI devem estar habilitados no módulo SIGACFG.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.employee_data_content_v1.PagedEmployeeDataContent
        """
        return await self._request(
            "employee_data_content_v1.list_employee_data_content",
            "GET",
            "/employeeDataContent",
            path_params={},
            query={"product": product, "dateModified": date_modified, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={"tenantId": tenant_id},
            body=None,
            extra_query=extra_query,
        )
