"""TAF e-Social - Remover empregador da base de dados do RET — generated from TAFEsocialRemoveCompany_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class TafEsocialRemoveCompanyV1(ApiGroup):
    """TAF e-Social - Remover empregador da base de dados do RET (/api/rh/esocial/v1)."""

    api_id = "taf_esocial_remove_company_v1"
    base_path = "/api/rh/esocial/v1"

    def delete_taf_esocial_remove_company_by_company_id(self, company_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove os dados do empregador do e-Social da base de dados do RET

        DELETE /TAFEsocialRemoveCompany/{companyId}; operationId=delete; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com o parâmetro companyId

        Response model: protheus.models.taf_esocial_remove_company_v1.PagedItens
        """
        return self._request(
            "taf_esocial_remove_company_v1.delete_taf_esocial_remove_company_by_company_id",
            "DELETE",
            "/TAFEsocialRemoveCompany/{companyId}",
            path_params={"companyId": company_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncTafEsocialRemoveCompanyV1(AsyncApiGroup):
    """TAF e-Social - Remover empregador da base de dados do RET (/api/rh/esocial/v1)."""

    api_id = "taf_esocial_remove_company_v1"
    base_path = "/api/rh/esocial/v1"

    async def delete_taf_esocial_remove_company_by_company_id(self, company_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove os dados do empregador do e-Social da base de dados do RET

        DELETE /TAFEsocialRemoveCompany/{companyId}; operationId=delete; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com o parâmetro companyId

        Response model: protheus.models.taf_esocial_remove_company_v1.PagedItens
        """
        return await self._request(
            "taf_esocial_remove_company_v1.delete_taf_esocial_remove_company_by_company_id",
            "DELETE",
            "/TAFEsocialRemoveCompany/{companyId}",
            path_params={"companyId": company_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
