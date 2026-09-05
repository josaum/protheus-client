"""Painel de Impressão da CAT — generated from CatReport_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CatReportV1(ApiGroup):
    """Painel de Impressão da CAT (/api/rh/esocial/v1)."""

    api_id = "cat_report_v1"
    base_path = "/api/rh/esocial/v1"

    def create_cat_report(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inicia o processamento do Painel de Impressão da CAT

        POST /CatReport; operationId=postCatReport; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.CatReportItems
        Request model: protheus.models.cat_report_v1.CatReportItems
        """
        return self._request(
            "cat_report_v1.create_cat_report",
            "POST",
            "/CatReport",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def list_cat_report_status(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o percentual de execução do Painel de Impressão da CAT

        GET /CatReport/status/; operationId=GetStatus; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.StatusItems
        Request model: protheus.models.cat_report_v1.StatusItems
        """
        return self._request(
            "cat_report_v1.list_cat_report_status",
            "GET",
            "/CatReport/status/",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def create_cat_report_cat_values(self, *, body: Body, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o resultado do Painel de Impressão da CAT

        POST /CatReport/catValues; operationId=PostCatValues; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.CatValuesItems
        Request model: protheus.models.cat_report_v1.CatValuesItems
        """
        return self._request(
            "cat_report_v1.create_cat_report_cat_values",
            "POST",
            "/CatReport/catValues",
            path_params={},
            query={"page": page, "pageSize": page_size},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def create_cat_report_cat_monitor_values(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o resultado do Painel do e-Social para impressão PDF

        POST /CatReport/catMonitorValues; operationId=PostcatMonitorValues; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.CatValuesItems
        Request model: protheus.models.cat_report_v1.CatValuesItems
        """
        return self._request(
            "cat_report_v1.create_cat_report_cat_monitor_values",
            "POST",
            "/CatReport/catMonitorValues",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncCatReportV1(AsyncApiGroup):
    """Painel de Impressão da CAT (/api/rh/esocial/v1)."""

    api_id = "cat_report_v1"
    base_path = "/api/rh/esocial/v1"

    async def create_cat_report(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inicia o processamento do Painel de Impressão da CAT

        POST /CatReport; operationId=postCatReport; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.CatReportItems
        Request model: protheus.models.cat_report_v1.CatReportItems
        """
        return await self._request(
            "cat_report_v1.create_cat_report",
            "POST",
            "/CatReport",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def list_cat_report_status(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o percentual de execução do Painel de Impressão da CAT

        GET /CatReport/status/; operationId=GetStatus; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.StatusItems
        Request model: protheus.models.cat_report_v1.StatusItems
        """
        return await self._request(
            "cat_report_v1.list_cat_report_status",
            "GET",
            "/CatReport/status/",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def create_cat_report_cat_values(self, *, body: Body, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o resultado do Painel de Impressão da CAT

        POST /CatReport/catValues; operationId=PostCatValues; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.CatValuesItems
        Request model: protheus.models.cat_report_v1.CatValuesItems
        """
        return await self._request(
            "cat_report_v1.create_cat_report_cat_values",
            "POST",
            "/CatReport/catValues",
            path_params={},
            query={"page": page, "pageSize": page_size},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def create_cat_report_cat_monitor_values(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o resultado do Painel do e-Social para impressão PDF

        POST /CatReport/catMonitorValues; operationId=PostcatMonitorValues; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.cat_report_v1.CatValuesItems
        Request model: protheus.models.cat_report_v1.CatValuesItems
        """
        return await self._request(
            "cat_report_v1.create_cat_report_cat_monitor_values",
            "POST",
            "/CatReport/catMonitorValues",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
