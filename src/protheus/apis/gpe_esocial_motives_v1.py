"""Motivos de Afastamento — generated from GPEEsocialMotives_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class GpeEsocialMotivesV1(ApiGroup):
    """Motivos de Afastamento (/api/rh/esocial/v1)."""

    api_id = "gpe_esocial_motives_v1"
    base_path = "/api/rh/esocial/v1"

    def list_esocial_motives(self, *, company_id: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Motivos de Afastamento

        GET /EsocialMotives; operationId=getMotives; Protheus >= 12.1.23

        Retorna lista completa com os motivos de afastamento

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.gpe_esocial_motives_v1.PagedItens
        """
        return self._request(
            "gpe_esocial_motives_v1.list_esocial_motives",
            "GET",
            "/EsocialMotives",
            path_params={},
            query={"companyId": company_id, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncGpeEsocialMotivesV1(AsyncApiGroup):
    """Motivos de Afastamento (/api/rh/esocial/v1)."""

    api_id = "gpe_esocial_motives_v1"
    base_path = "/api/rh/esocial/v1"

    async def list_esocial_motives(self, *, company_id: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Motivos de Afastamento

        GET /EsocialMotives; operationId=getMotives; Protheus >= 12.1.23

        Retorna lista completa com os motivos de afastamento

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.gpe_esocial_motives_v1.PagedItens
        """
        return await self._request(
            "gpe_esocial_motives_v1.list_esocial_motives",
            "GET",
            "/EsocialMotives",
            path_params={},
            query={"companyId": company_id, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )
