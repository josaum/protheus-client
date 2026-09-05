"""Checklist de Auditoria — generated from AuditChecklist_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AuditChecklistV1(ApiGroup):
    """Checklist de Auditoria (/api/quality/v1)."""

    api_id = "audit_checklist_v1"
    base_path = "/api/quality/v1"

    def get_audit_checklist_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Checklist de auditoria

        GET /auditChecklist/{internalId}; operationId=getAuditChecklistId; Protheus >= 12.1.23

        Retorna uma ficha de checklist pelo Número

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.ChecklistType
        """
        return self._request(
            "audit_checklist_v1.get_audit_checklist_by_internal_id",
            "GET",
            "/auditChecklist/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_audit_checklist_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Checklist de auditoria

        PUT /auditChecklist/{internalId}; operationId=putAuditChecklistId; Protheus >= 12.1.23

        Altera o cadastro de Checklist de auditoria conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.PagedChecklist
        Request model: protheus.models.audit_checklist_v1.ChecklistType
        """
        return self._request(
            "audit_checklist_v1.update_audit_checklist_by_internal_id",
            "PUT",
            "/auditChecklist/{internalId}",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_audit_checklist_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Checklist de auditoria

        DELETE /auditChecklist/{internalId}; operationId=deleteAuditChecklistId; Protheus >= 12.1.23

        Exclui um checklist pelo código

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.ChecklistType
        """
        return self._request(
            "audit_checklist_v1.delete_audit_checklist_by_internal_id",
            "DELETE",
            "/auditChecklist/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_audit_checklist(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com Checklist de auditorias

        GET /AuditChecklist/; operationId=getAuditChecklist; Protheus >= 12.1.23

        Retorna uma lista com Checklist de auditorias pendentes

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.PagedChecklist
        """
        return self._request(
            "audit_checklist_v1.list_audit_checklist",
            "GET",
            "/AuditChecklist/",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_audit_checklist(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Insere um checklist de auditoria

        POST /AuditChecklist/; operationId=postAuditChecklist; Protheus >= 12.1.23

        insere

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.PagedChecklist
        """
        return self._request(
            "audit_checklist_v1.create_audit_checklist",
            "POST",
            "/AuditChecklist/",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncAuditChecklistV1(AsyncApiGroup):
    """Checklist de Auditoria (/api/quality/v1)."""

    api_id = "audit_checklist_v1"
    base_path = "/api/quality/v1"

    async def get_audit_checklist_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Checklist de auditoria

        GET /auditChecklist/{internalId}; operationId=getAuditChecklistId; Protheus >= 12.1.23

        Retorna uma ficha de checklist pelo Número

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.ChecklistType
        """
        return await self._request(
            "audit_checklist_v1.get_audit_checklist_by_internal_id",
            "GET",
            "/auditChecklist/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_audit_checklist_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Checklist de auditoria

        PUT /auditChecklist/{internalId}; operationId=putAuditChecklistId; Protheus >= 12.1.23

        Altera o cadastro de Checklist de auditoria conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.PagedChecklist
        Request model: protheus.models.audit_checklist_v1.ChecklistType
        """
        return await self._request(
            "audit_checklist_v1.update_audit_checklist_by_internal_id",
            "PUT",
            "/auditChecklist/{internalId}",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_audit_checklist_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Checklist de auditoria

        DELETE /auditChecklist/{internalId}; operationId=deleteAuditChecklistId; Protheus >= 12.1.23

        Exclui um checklist pelo código

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.ChecklistType
        """
        return await self._request(
            "audit_checklist_v1.delete_audit_checklist_by_internal_id",
            "DELETE",
            "/auditChecklist/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_audit_checklist(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com Checklist de auditorias

        GET /AuditChecklist/; operationId=getAuditChecklist; Protheus >= 12.1.23

        Retorna uma lista com Checklist de auditorias pendentes

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.PagedChecklist
        """
        return await self._request(
            "audit_checklist_v1.list_audit_checklist",
            "GET",
            "/AuditChecklist/",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_audit_checklist(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Insere um checklist de auditoria

        POST /AuditChecklist/; operationId=postAuditChecklist; Protheus >= 12.1.23

        insere

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_checklist_v1.PagedChecklist
        """
        return await self._request(
            "audit_checklist_v1.create_audit_checklist",
            "POST",
            "/AuditChecklist/",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )
