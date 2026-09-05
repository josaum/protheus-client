"""Questionário de Auditoria — generated from AuditQuestionnaire_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AuditQuestionnaireV1(ApiGroup):
    """Questionário de Auditoria (/api/quality/v1)."""

    api_id = "audit_questionnaire_v1"
    base_path = "/api/quality/v1"

    def list_audit_questionnaire(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com Questionário de auditorias

        GET /AuditQuestionnaire; operationId=getAuditQuestionnaire; Protheus >= 12.1.23

        Retorna uma lista com questionário de auditorias

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.PagedAuditQuest
        """
        return self._request(
            "audit_questionnaire_v1.list_audit_questionnaire",
            "GET",
            "/AuditQuestionnaire",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_audit_questionnaire(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Insere um Questionário de auditoria

        POST /AuditQuestionnaire; operationId=postAuditQuestionnaire; Protheus >= 12.1.23

        Insere um questionário de auditoria

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return self._request(
            "audit_questionnaire_v1.create_audit_questionnaire",
            "POST",
            "/AuditQuestionnaire",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_audit_questionnaire_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Questionário de auditoria

        GET /AuditQuestionnaire/{internalId}; operationId=getAuditQuestionnaireId; Protheus >= 12.1.23

        Retorna um questionário de auditoria pelo ID

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return self._request(
            "audit_questionnaire_v1.get_audit_questionnaire_by_internal_id",
            "GET",
            "/AuditQuestionnaire/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_audit_questionnaire_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Questionário de auditoria

        PUT /AuditQuestionnaire/{internalId}; operationId=putAuditQuestionnaireId; Protheus >= 12.1.23

        Altera o cadastro de questionário de auditoria conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.PagedAuditQuest
        Request model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return self._request(
            "audit_questionnaire_v1.update_audit_questionnaire_by_internal_id",
            "PUT",
            "/AuditQuestionnaire/{internalId}",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_audit_questionnaire_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Questionário de auditoria

        DELETE /AuditQuestionnaire/{internalId}; operationId=deleteAuditQuestionnaireId; Protheus >= 12.1.23

        Exclui um questionário pelo código

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return self._request(
            "audit_questionnaire_v1.delete_audit_questionnaire_by_internal_id",
            "DELETE",
            "/AuditQuestionnaire/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncAuditQuestionnaireV1(AsyncApiGroup):
    """Questionário de Auditoria (/api/quality/v1)."""

    api_id = "audit_questionnaire_v1"
    base_path = "/api/quality/v1"

    async def list_audit_questionnaire(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista com Questionário de auditorias

        GET /AuditQuestionnaire; operationId=getAuditQuestionnaire; Protheus >= 12.1.23

        Retorna uma lista com questionário de auditorias

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.PagedAuditQuest
        """
        return await self._request(
            "audit_questionnaire_v1.list_audit_questionnaire",
            "GET",
            "/AuditQuestionnaire",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_audit_questionnaire(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Insere um Questionário de auditoria

        POST /AuditQuestionnaire; operationId=postAuditQuestionnaire; Protheus >= 12.1.23

        Insere um questionário de auditoria

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return await self._request(
            "audit_questionnaire_v1.create_audit_questionnaire",
            "POST",
            "/AuditQuestionnaire",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_audit_questionnaire_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Questionário de auditoria

        GET /AuditQuestionnaire/{internalId}; operationId=getAuditQuestionnaireId; Protheus >= 12.1.23

        Retorna um questionário de auditoria pelo ID

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return await self._request(
            "audit_questionnaire_v1.get_audit_questionnaire_by_internal_id",
            "GET",
            "/AuditQuestionnaire/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_audit_questionnaire_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Questionário de auditoria

        PUT /AuditQuestionnaire/{internalId}; operationId=putAuditQuestionnaireId; Protheus >= 12.1.23

        Altera o cadastro de questionário de auditoria conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.PagedAuditQuest
        Request model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return await self._request(
            "audit_questionnaire_v1.update_audit_questionnaire_by_internal_id",
            "PUT",
            "/AuditQuestionnaire/{internalId}",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_audit_questionnaire_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Questionário de auditoria

        DELETE /AuditQuestionnaire/{internalId}; operationId=deleteAuditQuestionnaireId; Protheus >= 12.1.23

        Exclui um questionário pelo código

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.audit_questionnaire_v1.AuditQuestType
        """
        return await self._request(
            "audit_questionnaire_v1.delete_audit_questionnaire_by_internal_id",
            "DELETE",
            "/AuditQuestionnaire/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )
