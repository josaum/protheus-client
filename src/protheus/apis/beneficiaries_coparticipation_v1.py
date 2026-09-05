"""Relação de Coparticipações dos Beneficiários e seus dependentes - Global — generated from BeneficiariesCoparticipation_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class BeneficiariesCoparticipationV1(ApiGroup):
    """Relação de Coparticipações dos Beneficiários e seus dependentes - Global (/api/rh/v1)."""

    api_id = "beneficiaries_coparticipation_v1"
    base_path = "/api/rh/v1"

    def list_beneficiaries_coparticipation(self, *, product: str | None = None, date_modified: str | None = None, companyid: str | None = None, branch_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de Coparticipações dos Beneficiários e seus dependentes.

        GET /BeneficiariesCoparticipation; operationId=getBeneficiariesCoparticipation; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.beneficiaries_coparticipation_v1.PagedBeneficiariesCoparticipation
        """
        return self._request(
            "beneficiaries_coparticipation_v1.list_beneficiaries_coparticipation",
            "GET",
            "/BeneficiariesCoparticipation",
            path_params={},
            query={"product": product, "dateModified": date_modified, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncBeneficiariesCoparticipationV1(AsyncApiGroup):
    """Relação de Coparticipações dos Beneficiários e seus dependentes - Global (/api/rh/v1)."""

    api_id = "beneficiaries_coparticipation_v1"
    base_path = "/api/rh/v1"

    async def list_beneficiaries_coparticipation(self, *, product: str | None = None, date_modified: str | None = None, companyid: str | None = None, branch_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de Coparticipações dos Beneficiários e seus dependentes.

        GET /BeneficiariesCoparticipation; operationId=getBeneficiariesCoparticipation; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.beneficiaries_coparticipation_v1.PagedBeneficiariesCoparticipation
        """
        return await self._request(
            "beneficiaries_coparticipation_v1.list_beneficiaries_coparticipation",
            "GET",
            "/BeneficiariesCoparticipation",
            path_params={},
            query={"product": product, "dateModified": date_modified, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )
