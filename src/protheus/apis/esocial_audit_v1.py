"""Painel de Auditoria do eSocial — generated from EsocialAudit_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class EsocialAuditV1(ApiGroup):
    """Painel de Auditoria do eSocial (/api/rh/esocial/v1)."""

    api_id = "esocial_audit_v1"
    base_path = "/api/rh/esocial/v1"

    def create_esocial_audit(self, *, body: Body, company_id: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui a entidade evento passado na requisição

        POST /EsocialAudit; operationId=postEsocialAudit; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.PagedItens
        Request model: protheus.models.esocial_audit_v1.PagedItens
        """
        return self._request(
            "esocial_audit_v1.create_esocial_audit",
            "POST",
            "/EsocialAudit",
            path_params={},
            query={"companyId": company_id, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def list_esocial_audit_status(self, *, company_id: str | None = None, request_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o percentual de execução do Painel de Auditoria do eSocial

        GET /EsocialAudit/status/; operationId=GetStatus; Protheus >= 12.1.27

        Retorna lista de eventos dentro/fora do prazo para transmissão do governo

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.StatusItems
        """
        return self._request(
            "esocial_audit_v1.list_esocial_audit_status",
            "GET",
            "/EsocialAudit/status/",
            path_params={},
            query={"companyId": company_id, "requestId": request_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_esocial_audit_audit_values(self, *, company_id: str | None = None, request_id: str | None = None, status: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o resultado do Painel de Auditoria do eSocial

        GET /EsocialAudit/auditValues; operationId=GetauditValues; Protheus >= 12.1.27

        Retorna lista de eventos dentro/fora do prazo para transmissão do governo

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.AuditValueItems
        """
        return self._request(
            "esocial_audit_v1.list_esocial_audit_audit_values",
            "GET",
            "/EsocialAudit/auditValues",
            path_params={},
            query={"companyId": company_id, "requestId": request_id, "status": status, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_esocial_audit_chart_values(self, *, company_id: str | None = None, request_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna informações do gráfico do Painel de Auditoria do eSocial

        GET /EsocialAudit/chartValues; operationId=GetchartValues; Protheus >= 12.1.27

        Retorna lista de eventos dentro/fora do prazo para transmissão do governo

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.ChartValueItems
        """
        return self._request(
            "esocial_audit_v1.list_esocial_audit_chart_values",
            "GET",
            "/EsocialAudit/chartValues",
            path_params={},
            query={"companyId": company_id, "requestId": request_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncEsocialAuditV1(AsyncApiGroup):
    """Painel de Auditoria do eSocial (/api/rh/esocial/v1)."""

    api_id = "esocial_audit_v1"
    base_path = "/api/rh/esocial/v1"

    async def create_esocial_audit(self, *, body: Body, company_id: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui a entidade evento passado na requisição

        POST /EsocialAudit; operationId=postEsocialAudit; Protheus >= 12.1.27

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.PagedItens
        Request model: protheus.models.esocial_audit_v1.PagedItens
        """
        return await self._request(
            "esocial_audit_v1.create_esocial_audit",
            "POST",
            "/EsocialAudit",
            path_params={},
            query={"companyId": company_id, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def list_esocial_audit_status(self, *, company_id: str | None = None, request_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o percentual de execução do Painel de Auditoria do eSocial

        GET /EsocialAudit/status/; operationId=GetStatus; Protheus >= 12.1.27

        Retorna lista de eventos dentro/fora do prazo para transmissão do governo

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.StatusItems
        """
        return await self._request(
            "esocial_audit_v1.list_esocial_audit_status",
            "GET",
            "/EsocialAudit/status/",
            path_params={},
            query={"companyId": company_id, "requestId": request_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_esocial_audit_audit_values(self, *, company_id: str | None = None, request_id: str | None = None, status: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o resultado do Painel de Auditoria do eSocial

        GET /EsocialAudit/auditValues; operationId=GetauditValues; Protheus >= 12.1.27

        Retorna lista de eventos dentro/fora do prazo para transmissão do governo

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.AuditValueItems
        """
        return await self._request(
            "esocial_audit_v1.list_esocial_audit_audit_values",
            "GET",
            "/EsocialAudit/auditValues",
            path_params={},
            query={"companyId": company_id, "requestId": request_id, "status": status, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_esocial_audit_chart_values(self, *, company_id: str | None = None, request_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna informações do gráfico do Painel de Auditoria do eSocial

        GET /EsocialAudit/chartValues; operationId=GetchartValues; Protheus >= 12.1.27

        Retorna lista de eventos dentro/fora do prazo para transmissão do governo

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.esocial_audit_v1.ChartValueItems
        """
        return await self._request(
            "esocial_audit_v1.list_esocial_audit_chart_values",
            "GET",
            "/EsocialAudit/chartValues",
            path_params={},
            query={"companyId": company_id, "requestId": request_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )
