"""Freight Components — generated from FreightComponents_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class FreightComponentsV1(ApiGroup):
    """Freight Components (/api/gfe/v1)."""

    api_id = "freight_components_v1"
    base_path = "/api/gfe/v1"

    def list_freight_components(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Freight Components list

        GET /freightComponents; operationId=getFreightComponents; Protheus >= 12.1.24

        Retorna lista de componentes de frete

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.PagedFreightComponent
        """
        return self._request(
            "freight_components_v1.list_freight_components",
            "GET",
            "/freightComponents",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_freight_components(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Add Freight Components

        POST /freightComponents; operationId=postFreightComponents; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        Request model: protheus.models.freight_components_v1.FreightComponents
        """
        return self._request(
            "freight_components_v1.create_freight_components",
            "POST",
            "/freightComponents",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_freight_components_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Return the Freight Components

        GET /freightComponents/{InternalId}; operationId=getFreightComponentsId; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        """
        return self._request(
            "freight_components_v1.get_freight_components_by_internal_id",
            "GET",
            "/freightComponents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_freight_components_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Edit Freight Components

        PUT /freightComponents/{InternalId}; operationId=putFreightComponentsId; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        Request model: protheus.models.freight_components_v1.FreightComponents
        """
        return self._request(
            "freight_components_v1.update_freight_components_by_internal_id",
            "PUT",
            "/freightComponents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_freight_components_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Delete Freight Components

        DELETE /freightComponents/{InternalId}; operationId=deleteFreightComponents; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        """
        return self._request(
            "freight_components_v1.delete_freight_components_by_internal_id",
            "DELETE",
            "/freightComponents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncFreightComponentsV1(AsyncApiGroup):
    """Freight Components (/api/gfe/v1)."""

    api_id = "freight_components_v1"
    base_path = "/api/gfe/v1"

    async def list_freight_components(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Freight Components list

        GET /freightComponents; operationId=getFreightComponents; Protheus >= 12.1.24

        Retorna lista de componentes de frete

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.PagedFreightComponent
        """
        return await self._request(
            "freight_components_v1.list_freight_components",
            "GET",
            "/freightComponents",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_freight_components(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Add Freight Components

        POST /freightComponents; operationId=postFreightComponents; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        Request model: protheus.models.freight_components_v1.FreightComponents
        """
        return await self._request(
            "freight_components_v1.create_freight_components",
            "POST",
            "/freightComponents",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_freight_components_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Return the Freight Components

        GET /freightComponents/{InternalId}; operationId=getFreightComponentsId; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        """
        return await self._request(
            "freight_components_v1.get_freight_components_by_internal_id",
            "GET",
            "/freightComponents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_freight_components_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Edit Freight Components

        PUT /freightComponents/{InternalId}; operationId=putFreightComponentsId; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        Request model: protheus.models.freight_components_v1.FreightComponents
        """
        return await self._request(
            "freight_components_v1.update_freight_components_by_internal_id",
            "PUT",
            "/freightComponents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_freight_components_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Delete Freight Components

        DELETE /freightComponents/{InternalId}; operationId=deleteFreightComponents; Protheus >= 12.1.24

        TOTVS note: This service is available to recover data

        Response model: protheus.models.freight_components_v1.FreightComponents
        """
        return await self._request(
            "freight_components_v1.delete_freight_components_by_internal_id",
            "DELETE",
            "/freightComponents/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
