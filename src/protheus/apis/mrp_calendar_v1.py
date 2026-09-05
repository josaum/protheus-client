"""Calendário do MRP — generated from MRPCalendar_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MrpCalendarV1(ApiGroup):
    """Calendário do MRP (/api/pcp/v1)."""

    api_id = "mrp_calendar_v1"
    base_path = "/api/pcp/v1"

    def list_mrpcalendar(self, *, branch_id: str | None = None, code: str | None = None, calendar: str | None = None, date: str | None = None, start_time: str | None = None, end_time: str | None = None, interval: str | None = None, total_hours: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de calendário do MRP

        GET /mrpcalendar; operationId=getmrpcalendar2; Protheus >= 12.1.27

        Retorna lista de calendário do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.PagedMRPCalendar
        """
        return self._request(
            "mrp_calendar_v1.list_mrpcalendar",
            "GET",
            "/mrpcalendar",
            path_params={},
            query={"branchId": branch_id, "code": code, "calendar": calendar, "date": date, "startTime": start_time, "endTime": end_time, "interval": interval, "totalHours": total_hours, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpcalendar(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no calendário do MRP

        POST /mrpcalendar; operationId=postcalendar; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.PagedMRPCalendar
        Request model: protheus.models.mrp_calendar_v1.ListOfMRPCalendar
        """
        return self._request(
            "mrp_calendar_v1.create_mrpcalendar",
            "POST",
            "/mrpcalendar",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_mrpcalendar(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais período do calendário do MRP

        DELETE /mrpcalendar; operationId=deletemrpcalendar; Protheus >= 12.1.27

        Remove um ou mais período do Calendário do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.MRPCalendarMultiple
        Request model: protheus.models.mrp_calendar_v1.ListOfMRPCalendar
        """
        return self._request(
            "mrp_calendar_v1.delete_mrpcalendar",
            "DELETE",
            "/mrpcalendar",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_mrpcalendar_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Calendário do MRP

        GET /mrpcalendar/{branchId}/{code}; operationId=getmrpcalendar; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.MRPCalendarBase
        """
        return self._request(
            "mrp_calendar_v1.get_mrpcalendar_by_branch_id_and_code",
            "GET",
            "/mrpcalendar/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_mrpcalendar_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no calendário do MRP

        POST /mrpcalendar/sync; operationId=synccalendar; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.PagedMRPCalendar
        Request model: protheus.models.mrp_calendar_v1.ListOfMRPCalendar
        """
        return self._request(
            "mrp_calendar_v1.create_mrpcalendar_sync",
            "POST",
            "/mrpcalendar/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncMrpCalendarV1(AsyncApiGroup):
    """Calendário do MRP (/api/pcp/v1)."""

    api_id = "mrp_calendar_v1"
    base_path = "/api/pcp/v1"

    async def list_mrpcalendar(self, *, branch_id: str | None = None, code: str | None = None, calendar: str | None = None, date: str | None = None, start_time: str | None = None, end_time: str | None = None, interval: str | None = None, total_hours: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de calendário do MRP

        GET /mrpcalendar; operationId=getmrpcalendar2; Protheus >= 12.1.27

        Retorna lista de calendário do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.PagedMRPCalendar
        """
        return await self._request(
            "mrp_calendar_v1.list_mrpcalendar",
            "GET",
            "/mrpcalendar",
            path_params={},
            query={"branchId": branch_id, "code": code, "calendar": calendar, "date": date, "startTime": start_time, "endTime": end_time, "interval": interval, "totalHours": total_hours, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpcalendar(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no calendário do MRP

        POST /mrpcalendar; operationId=postcalendar; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.PagedMRPCalendar
        Request model: protheus.models.mrp_calendar_v1.ListOfMRPCalendar
        """
        return await self._request(
            "mrp_calendar_v1.create_mrpcalendar",
            "POST",
            "/mrpcalendar",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_mrpcalendar(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um ou mais período do calendário do MRP

        DELETE /mrpcalendar; operationId=deletemrpcalendar; Protheus >= 12.1.27

        Remove um ou mais período do Calendário do MRP

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.MRPCalendarMultiple
        Request model: protheus.models.mrp_calendar_v1.ListOfMRPCalendar
        """
        return await self._request(
            "mrp_calendar_v1.delete_mrpcalendar",
            "DELETE",
            "/mrpcalendar",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_mrpcalendar_by_branch_id_and_code(self, branch_id: str, code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Calendário do MRP

        GET /mrpcalendar/{branchId}/{code}; operationId=getmrpcalendar; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.MRPCalendarBase
        """
        return await self._request(
            "mrp_calendar_v1.get_mrpcalendar_by_branch_id_and_code",
            "GET",
            "/mrpcalendar/{branchId}/{code}",
            path_params={"branchId": branch_id, "code": code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_mrpcalendar_sync(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui ou atualiza um ou mais registros no calendário do MRP

        POST /mrpcalendar/sync; operationId=synccalendar; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.mrp_calendar_v1.PagedMRPCalendar
        Request model: protheus.models.mrp_calendar_v1.ListOfMRPCalendar
        """
        return await self._request(
            "mrp_calendar_v1.create_mrpcalendar_sync",
            "POST",
            "/mrpcalendar/sync",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
