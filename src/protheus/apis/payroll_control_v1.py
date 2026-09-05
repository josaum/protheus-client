"""Folha de pagamento para linha de produtos totvs - Global — generated from PayrollControl_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class PayrollControlV1(ApiGroup):
    """Folha de pagamento para linha de produtos totvs - Global (/api/rh/v1)."""

    api_id = "payroll_control_v1"
    base_path = "/api/rh/v1"

    def list_payroll_control(self, *, product: str | None = None, datemodified: str | None = None, provider_type: str | None = None, companyid: str | None = None, branch_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de funcionários e seus respectivos dados complementares(Ex:Departamento, Centro de Custo)

        GET /PayrollControl; operationId=getPayrollControl; Protheus >= 12.1.25

        Retorna os dados da folha de pagamento de benefícios(Assitência Médica e Odontológica)

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.payroll_control_v1.PagedPayrollControl
        """
        return self._request(
            "payroll_control_v1.list_payroll_control",
            "GET",
            "/PayrollControl",
            path_params={},
            query={"product": product, "datemodified": datemodified, "providerType": provider_type, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncPayrollControlV1(AsyncApiGroup):
    """Folha de pagamento para linha de produtos totvs - Global (/api/rh/v1)."""

    api_id = "payroll_control_v1"
    base_path = "/api/rh/v1"

    async def list_payroll_control(self, *, product: str | None = None, datemodified: str | None = None, provider_type: str | None = None, companyid: str | None = None, branch_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de funcionários e seus respectivos dados complementares(Ex:Departamento, Centro de Custo)

        GET /PayrollControl; operationId=getPayrollControl; Protheus >= 12.1.25

        Retorna os dados da folha de pagamento de benefícios(Assitência Médica e Odontológica)

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.payroll_control_v1.PagedPayrollControl
        """
        return await self._request(
            "payroll_control_v1.list_payroll_control",
            "GET",
            "/PayrollControl",
            path_params={},
            query={"product": product, "datemodified": datemodified, "providerType": provider_type, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )
