"""Filiais — generated from EsocialBranches_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class EsocialBranchesV1(ApiGroup):
    """Filiais (/api/rh/esocial/v1)."""

    api_id = "esocial_branches_v1"
    base_path = "/api/rh/esocial/v1"

    def list_esocial_branches(self, *, company_id: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o código da empresa e código da filial no TAF

        GET /EsocialBranches; operationId=GetBranches; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_branches_v1.PagedItens
        """
        return self._request(
            "esocial_branches_v1.list_esocial_branches",
            "GET",
            "/EsocialBranches",
            path_params={},
            query={"companyId": company_id, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncEsocialBranchesV1(AsyncApiGroup):
    """Filiais (/api/rh/esocial/v1)."""

    api_id = "esocial_branches_v1"
    base_path = "/api/rh/esocial/v1"

    async def list_esocial_branches(self, *, company_id: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o código da empresa e código da filial no TAF

        GET /EsocialBranches; operationId=GetBranches; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_branches_v1.PagedItens
        """
        return await self._request(
            "esocial_branches_v1.list_esocial_branches",
            "GET",
            "/EsocialBranches",
            path_params={},
            query={"companyId": company_id, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )
