"""Consulta os erros da integração TSI — generated from TSIIntegrationErrors_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class TsiIntegrationErrorsV1(ApiGroup):
    """Consulta os erros da integração TSI (/api/tsi/v1)."""

    api_id = "tsi_integration_errors_v1"
    base_path = "/api/tsi/v1"

    def list_tsi_integration_errors(self, *, company_id: str | None = None, branch_code: str | None = None, type_filter: str | None = None, date_of: str | None = None, date_up: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consulta os erros da integração TSI

        GET /TSIIntegrationErrors; operationId=getTSIIntegrationErrors; Protheus >= 12.1.27

        Consulta os erros ocorridos durante a integração dos dados entre o ERP e o TAF.

        TOTVS note: Este verbo está disponível com o parâmetro companyId, dateOf, dateUp e typeFilter

        Response model: protheus.models.tsi_integration_errors_v1.PagedItens
        """
        return self._request(
            "tsi_integration_errors_v1.list_tsi_integration_errors",
            "GET",
            "/TSIIntegrationErrors",
            path_params={},
            query={"companyId": company_id, "branchCode": branch_code, "typeFilter": type_filter, "dateOf": date_of, "dateUp": date_up, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncTsiIntegrationErrorsV1(AsyncApiGroup):
    """Consulta os erros da integração TSI (/api/tsi/v1)."""

    api_id = "tsi_integration_errors_v1"
    base_path = "/api/tsi/v1"

    async def list_tsi_integration_errors(self, *, company_id: str | None = None, branch_code: str | None = None, type_filter: str | None = None, date_of: str | None = None, date_up: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consulta os erros da integração TSI

        GET /TSIIntegrationErrors; operationId=getTSIIntegrationErrors; Protheus >= 12.1.27

        Consulta os erros ocorridos durante a integração dos dados entre o ERP e o TAF.

        TOTVS note: Este verbo está disponível com o parâmetro companyId, dateOf, dateUp e typeFilter

        Response model: protheus.models.tsi_integration_errors_v1.PagedItens
        """
        return await self._request(
            "tsi_integration_errors_v1.list_tsi_integration_errors",
            "GET",
            "/TSIIntegrationErrors",
            path_params={},
            query={"companyId": company_id, "branchCode": branch_code, "typeFilter": type_filter, "dateOf": date_of, "dateUp": date_up, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )
