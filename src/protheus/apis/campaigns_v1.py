"""Campanhas — generated from Campaigns_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CampaignsV1(ApiGroup):
    """Campanhas (/api/crm/v1)."""

    api_id = "campaigns_v1"
    base_path = "/api/crm/v1"

    def list_campaigns(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as campanhas cadastradas

        GET /campaigns; operationId=getcampaigns; Protheus >= 12.1.21

        Response model: protheus.models.campaigns_v1.PagedCampaigns
        """
        return self._request(
            "campaigns_v1.list_campaigns",
            "GET",
            "/campaigns",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_campaigns(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma nova campanha

        POST /campaigns; operationId=postcampaigns; Protheus >= 12.1.21

        TOTVS note: Inclui uma nova campanha

        Response model: protheus.models.campaigns_v1.CampaignsInfo
        Request model: protheus.models.campaigns_v1.CampaignsInfo
        """
        return self._request(
            "campaigns_v1.create_campaigns",
            "POST",
            "/campaigns",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_campaigns_by_code(self, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as informações da campanha informada

        GET /campaigns/{Code}; operationId=getCampaigns; Protheus >= 12.1.21

        TOTVS note: Retorna a camapnha informada

        Response model: protheus.models.campaigns_v1.CampaignsInfo
        """
        return self._request(
            "campaigns_v1.get_campaigns_by_code",
            "GET",
            "/campaigns/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_campaigns_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a camapnha informada

        PUT /campaigns/{Code}; operationId=putCampaigns; Protheus >= 12.1.21

        TOTVS note: Altera a camapnha informada

        Response model: protheus.models.campaigns_v1.CampaignsInfo
        Request model: protheus.models.campaigns_v1.CampaignsInfo
        """
        return self._request(
            "campaigns_v1.update_campaigns_by_code",
            "PUT",
            "/campaigns/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_campaigns_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui a campanha informada

        DELETE /campaigns/{Code}; operationId=deleteCampaigns; Protheus >= 12.1.21

        TOTVS note: Exclui a campanha informada
        """
        return self._request(
            "campaigns_v1.delete_campaigns_by_code",
            "DELETE",
            "/campaigns/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCampaignsV1(AsyncApiGroup):
    """Campanhas (/api/crm/v1)."""

    api_id = "campaigns_v1"
    base_path = "/api/crm/v1"

    async def list_campaigns(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as campanhas cadastradas

        GET /campaigns; operationId=getcampaigns; Protheus >= 12.1.21

        Response model: protheus.models.campaigns_v1.PagedCampaigns
        """
        return await self._request(
            "campaigns_v1.list_campaigns",
            "GET",
            "/campaigns",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_campaigns(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma nova campanha

        POST /campaigns; operationId=postcampaigns; Protheus >= 12.1.21

        TOTVS note: Inclui uma nova campanha

        Response model: protheus.models.campaigns_v1.CampaignsInfo
        Request model: protheus.models.campaigns_v1.CampaignsInfo
        """
        return await self._request(
            "campaigns_v1.create_campaigns",
            "POST",
            "/campaigns",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_campaigns_by_code(self, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as informações da campanha informada

        GET /campaigns/{Code}; operationId=getCampaigns; Protheus >= 12.1.21

        TOTVS note: Retorna a camapnha informada

        Response model: protheus.models.campaigns_v1.CampaignsInfo
        """
        return await self._request(
            "campaigns_v1.get_campaigns_by_code",
            "GET",
            "/campaigns/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_campaigns_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a camapnha informada

        PUT /campaigns/{Code}; operationId=putCampaigns; Protheus >= 12.1.21

        TOTVS note: Altera a camapnha informada

        Response model: protheus.models.campaigns_v1.CampaignsInfo
        Request model: protheus.models.campaigns_v1.CampaignsInfo
        """
        return await self._request(
            "campaigns_v1.update_campaigns_by_code",
            "PUT",
            "/campaigns/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_campaigns_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui a campanha informada

        DELETE /campaigns/{Code}; operationId=deleteCampaigns; Protheus >= 12.1.21

        TOTVS note: Exclui a campanha informada
        """
        return await self._request(
            "campaigns_v1.delete_campaigns_by_code",
            "DELETE",
            "/campaigns/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
