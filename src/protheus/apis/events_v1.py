"""Eventos — generated from Events_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class EventsV1(ApiGroup):
    """Eventos (/api/crm/v1)."""

    api_id = "events_v1"
    base_path = "/api/crm/v1"

    def list_events(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os eventos cadastrados

        GET /events; operationId=getevents; Protheus >= 12.1.21

        Response model: protheus.models.events_v1.PagedEvent
        """
        return self._request(
            "events_v1.list_events",
            "GET",
            "/events",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_events(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um novo evento

        POST /events; operationId=postevents; Protheus >= 12.1.21

        TOTVS note: Inclui um novo evento

        Response model: protheus.models.events_v1.EventsInfo
        Request model: protheus.models.events_v1.EventsInfo
        """
        return self._request(
            "events_v1.create_events",
            "POST",
            "/events",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_events_by_code(self, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as informações do evento informado

        GET /events/{Code}; operationId=getEvents; Protheus >= 12.1.21

        TOTVS note: Retorna o evento informado

        Response model: protheus.models.events_v1.EventsInfo
        """
        return self._request(
            "events_v1.get_events_by_code",
            "GET",
            "/events/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_events_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o evento informado

        PUT /events/{Code}; operationId=putEvents; Protheus >= 12.1.21

        TOTVS note: Altera o evento informado

        Response model: protheus.models.events_v1.EventsInfo
        Request model: protheus.models.events_v1.EventsInfo
        """
        return self._request(
            "events_v1.update_events_by_code",
            "PUT",
            "/events/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_events_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui o evento informado

        DELETE /events/{Code}; operationId=deleteEvents; Protheus >= 12.1.21

        TOTVS note: Exclui o evento informado
        """
        return self._request(
            "events_v1.delete_events_by_code",
            "DELETE",
            "/events/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncEventsV1(AsyncApiGroup):
    """Eventos (/api/crm/v1)."""

    api_id = "events_v1"
    base_path = "/api/crm/v1"

    async def list_events(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os eventos cadastrados

        GET /events; operationId=getevents; Protheus >= 12.1.21

        Response model: protheus.models.events_v1.PagedEvent
        """
        return await self._request(
            "events_v1.list_events",
            "GET",
            "/events",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_events(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um novo evento

        POST /events; operationId=postevents; Protheus >= 12.1.21

        TOTVS note: Inclui um novo evento

        Response model: protheus.models.events_v1.EventsInfo
        Request model: protheus.models.events_v1.EventsInfo
        """
        return await self._request(
            "events_v1.create_events",
            "POST",
            "/events",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_events_by_code(self, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna as informações do evento informado

        GET /events/{Code}; operationId=getEvents; Protheus >= 12.1.21

        TOTVS note: Retorna o evento informado

        Response model: protheus.models.events_v1.EventsInfo
        """
        return await self._request(
            "events_v1.get_events_by_code",
            "GET",
            "/events/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_events_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o evento informado

        PUT /events/{Code}; operationId=putEvents; Protheus >= 12.1.21

        TOTVS note: Altera o evento informado

        Response model: protheus.models.events_v1.EventsInfo
        Request model: protheus.models.events_v1.EventsInfo
        """
        return await self._request(
            "events_v1.update_events_by_code",
            "PUT",
            "/events/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_events_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui o evento informado

        DELETE /events/{Code}; operationId=deleteEvents; Protheus >= 12.1.21

        TOTVS note: Exclui o evento informado
        """
        return await self._request(
            "events_v1.delete_events_by_code",
            "DELETE",
            "/events/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
