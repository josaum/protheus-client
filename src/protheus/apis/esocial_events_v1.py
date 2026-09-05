"""Lista de eventos — generated from EsocialEvents_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class EsocialEventsV1(ApiGroup):
    """Lista de eventos (/api/rh/esocial/v1)."""

    api_id = "esocial_events_v1"
    base_path = "/api/rh/esocial/v1"

    def list_esocial_events(self, *, company_id: str | None = None, events_check_permissions: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a lista de eventos do TAF

        GET /EsocialEvents; operationId=GetEvents; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_events_v1.PagedItens
        """
        return self._request(
            "esocial_events_v1.list_esocial_events",
            "GET",
            "/EsocialEvents",
            path_params={},
            query={"companyId": company_id, "eventsCheckPermissions": events_check_permissions},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncEsocialEventsV1(AsyncApiGroup):
    """Lista de eventos (/api/rh/esocial/v1)."""

    api_id = "esocial_events_v1"
    base_path = "/api/rh/esocial/v1"

    async def list_esocial_events(self, *, company_id: str | None = None, events_check_permissions: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a lista de eventos do TAF

        GET /EsocialEvents; operationId=GetEvents; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_events_v1.PagedItens
        """
        return await self._request(
            "esocial_events_v1.list_esocial_events",
            "GET",
            "/EsocialEvents",
            path_params={},
            query={"companyId": company_id, "eventsCheckPermissions": events_check_permissions},
            headers={},
            body=None,
            extra_query=extra_query,
        )
