"""Consulta o status do serviço — generated from TSIServiceStatus_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class TsiServiceStatusV1(ApiGroup):
    """Consulta o status do serviço (/api/tsi/v1)."""

    api_id = "tsi_service_status_v1"
    base_path = "/api/tsi/v1"

    def list_tsi_service_status(self, *, company_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consulta o status do serviço

        GET /TSIServiceStatus; operationId=getTSIServiceStatus; Protheus >= 12.1.23

        Consulta o status do serviço, se está configurado e/ou ativo.

        TOTVS note: Este verbo está disponível com o parâmetro companyId

        Response model: protheus.models.tsi_service_status_v1.Status1
        """
        return self._request(
            "tsi_service_status_v1.list_tsi_service_status",
            "GET",
            "/TSIServiceStatus",
            path_params={},
            query={"companyId": company_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncTsiServiceStatusV1(AsyncApiGroup):
    """Consulta o status do serviço (/api/tsi/v1)."""

    api_id = "tsi_service_status_v1"
    base_path = "/api/tsi/v1"

    async def list_tsi_service_status(self, *, company_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Consulta o status do serviço

        GET /TSIServiceStatus; operationId=getTSIServiceStatus; Protheus >= 12.1.23

        Consulta o status do serviço, se está configurado e/ou ativo.

        TOTVS note: Este verbo está disponível com o parâmetro companyId

        Response model: protheus.models.tsi_service_status_v1.Status1
        """
        return await self._request(
            "tsi_service_status_v1.list_tsi_service_status",
            "GET",
            "/TSIServiceStatus",
            path_params={},
            query={"companyId": company_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )
