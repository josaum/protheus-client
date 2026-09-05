"""Lista de filiais do grupo de empresas — generated from TSIBranches_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class TsiBranchesV1(ApiGroup):
    """Lista de filiais do grupo de empresas (/api/tsi/v1)."""

    api_id = "tsi_branches_v1"
    base_path = "/api/tsi/v1"

    def list_tsi_branches(self, *, company_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as filiais do grupo

        GET /TSIBranches; operationId=getTSIBranches; Protheus >= 12.1.27

        Retorna as filiais do grupo informado de acordo com o parâmetro 'companyId'.

        TOTVS note: Este verbo está disponível com O parâmetro 'companyId'.

        Response model: protheus.models.tsi_branches_v1.Branches
        """
        return self._request(
            "tsi_branches_v1.list_tsi_branches",
            "GET",
            "/TSIBranches",
            path_params={},
            query={"companyId": company_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncTsiBranchesV1(AsyncApiGroup):
    """Lista de filiais do grupo de empresas (/api/tsi/v1)."""

    api_id = "tsi_branches_v1"
    base_path = "/api/tsi/v1"

    async def list_tsi_branches(self, *, company_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as filiais do grupo

        GET /TSIBranches; operationId=getTSIBranches; Protheus >= 12.1.27

        Retorna as filiais do grupo informado de acordo com o parâmetro 'companyId'.

        TOTVS note: Este verbo está disponível com O parâmetro 'companyId'.

        Response model: protheus.models.tsi_branches_v1.Branches
        """
        return await self._request(
            "tsi_branches_v1.list_tsi_branches",
            "GET",
            "/TSIBranches",
            path_params={},
            query={"companyId": company_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )
