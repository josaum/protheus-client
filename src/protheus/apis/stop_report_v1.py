"""Apontamentos de Parada — generated from StopReport_v1_003.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class StopReportV1(ApiGroup):
    """Apontamentos de Parada (/api/pcp/v1)."""

    api_id = "stop_report_v1"
    base_path = "/api/pcp/v1"

    def list_stop_reports(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Apontamentos de Parada

        GET /stopReports; operationId=getStopReports; Protheus >= 12.1.23

        Retorna lista de Apontamentos de Parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.PagedStopReports
        """
        return self._request(
            "stop_report_v1.list_stop_reports",
            "GET",
            "/stopReports",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_stop_reports(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Apontamento de Parada

        POST /stopReports; operationId=postStopReport; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.StopReport
        Request model: protheus.models.stop_report_v1.StopReport
        """
        return self._request(
            "stop_report_v1.create_stop_reports",
            "POST",
            "/stopReports",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_stop_reports_by_integration_report(self, integration_report: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Apontamento de Parada

        GET /stopReports/{IntegrationReport}; operationId=getStopReportID; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.StopReport
        """
        return self._request(
            "stop_report_v1.get_stop_reports_by_integration_report",
            "GET",
            "/stopReports/{IntegrationReport}",
            path_params={"IntegrationReport": integration_report},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def delete_stop_reports_by_integration_report_reversal(self, integration_report: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Estorna um apontamento de Parada

        DELETE /stopReports/{IntegrationReport}/reversal; operationId=deleteStopReportID; Protheus >= 12.1.23

        Estorna um Apontamento de Parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.StopReport
        """
        return self._request(
            "stop_report_v1.delete_stop_reports_by_integration_report_reversal",
            "DELETE",
            "/stopReports/{IntegrationReport}/reversal",
            path_params={"IntegrationReport": integration_report},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncStopReportV1(AsyncApiGroup):
    """Apontamentos de Parada (/api/pcp/v1)."""

    api_id = "stop_report_v1"
    base_path = "/api/pcp/v1"

    async def list_stop_reports(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Apontamentos de Parada

        GET /stopReports; operationId=getStopReports; Protheus >= 12.1.23

        Retorna lista de Apontamentos de Parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.PagedStopReports
        """
        return await self._request(
            "stop_report_v1.list_stop_reports",
            "GET",
            "/stopReports",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_stop_reports(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Apontamento de Parada

        POST /stopReports; operationId=postStopReport; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.StopReport
        Request model: protheus.models.stop_report_v1.StopReport
        """
        return await self._request(
            "stop_report_v1.create_stop_reports",
            "POST",
            "/stopReports",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_stop_reports_by_integration_report(self, integration_report: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Apontamento de Parada

        GET /stopReports/{IntegrationReport}; operationId=getStopReportID; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.StopReport
        """
        return await self._request(
            "stop_report_v1.get_stop_reports_by_integration_report",
            "GET",
            "/stopReports/{IntegrationReport}",
            path_params={"IntegrationReport": integration_report},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def delete_stop_reports_by_integration_report_reversal(self, integration_report: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Estorna um apontamento de Parada

        DELETE /stopReports/{IntegrationReport}/reversal; operationId=deleteStopReportID; Protheus >= 12.1.23

        Estorna um Apontamento de Parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_report_v1.StopReport
        """
        return await self._request(
            "stop_report_v1.delete_stop_reports_by_integration_report_reversal",
            "DELETE",
            "/stopReports/{IntegrationReport}/reversal",
            path_params={"IntegrationReport": integration_report},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
