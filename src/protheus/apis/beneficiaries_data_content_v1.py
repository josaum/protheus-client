"""Relação de Benficiários - Global — generated from BeneficiariesDataContent_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class BeneficiariesDataContentV1(ApiGroup):
    """Relação de Benficiários - Global (/api/rh/v1)."""

    api_id = "beneficiaries_data_content_v1"
    base_path = "/api/rh/v1"

    def list_beneficiaries_data_content(self, *, product: str | None = None, date_modified: str | None = None, companyid: str | None = None, branch_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de beneficiários

        GET /BeneficiariesDataContent; operationId=beneficiariesDataContent; Protheus >= 12.1.25

        Retorna todos os registros de beneficiários.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.beneficiaries_data_content_v1.PagedBeneficiariesDataContent
        """
        return self._request(
            "beneficiaries_data_content_v1.list_beneficiaries_data_content",
            "GET",
            "/BeneficiariesDataContent",
            path_params={},
            query={"product": product, "dateModified": date_modified, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncBeneficiariesDataContentV1(AsyncApiGroup):
    """Relação de Benficiários - Global (/api/rh/v1)."""

    api_id = "beneficiaries_data_content_v1"
    base_path = "/api/rh/v1"

    async def list_beneficiaries_data_content(self, *, product: str | None = None, date_modified: str | None = None, companyid: str | None = None, branch_id: str | None = None, page: int | None = None, page_size: int | None = None, order: str | list[str] | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os registros de beneficiários

        GET /BeneficiariesDataContent; operationId=beneficiariesDataContent; Protheus >= 12.1.25

        Retorna todos os registros de beneficiários.

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.beneficiaries_data_content_v1.PagedBeneficiariesDataContent
        """
        return await self._request(
            "beneficiaries_data_content_v1.list_beneficiaries_data_content",
            "GET",
            "/BeneficiariesDataContent",
            path_params={},
            query={"product": product, "dateModified": date_modified, "companyid": companyid, "branchId": branch_id, "page": page, "pageSize": page_size, "order": order},
            headers={},
            body=None,
            extra_query=extra_query,
        )
