"""Tópico de Auditorias — generated from AuditTopic_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AuditTopicV1(ApiGroup):
    """Tópico de Auditorias (/api/quality/v1)."""

    api_id = "audit_topic_v1"
    base_path = "/api/quality/v1"

    def get_audit_topic_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um único registro Topico de Auditoria

        GET /auditTopic/{internalId}; operationId=getauditTopicId; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return self._request(
            "audit_topic_v1.get_audit_topic_by_internal_id",
            "GET",
            "/auditTopic/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_audit_topic_by_internal_id(self, internal_id: str, item_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o cadastro de Topico de auditoria

        PUT /auditTopic/{internalId}; operationId=putauditTopicInternalId; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        Request model: protheus.models.audit_topic_v1.PagedTopic
        """
        return self._request(
            "audit_topic_v1.update_audit_topic_by_internal_id",
            "PUT",
            "/auditTopic/{internalId}",
            path_params={"internalId": internal_id, "itemId": item_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_audit_topic_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o Topico de auditoria

        DELETE /auditTopic/{internalId}; operationId=putauditQuestionnarieId; Protheus >= 12.1.23

        Deleta

        TOTVS note: Este verbo esta disponível com todos os parametro

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return self._request(
            "audit_topic_v1.delete_audit_topic_by_internal_id",
            "DELETE",
            "/auditTopic/{internalId}",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_audit_topic(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um único cadastro de topico de auditoria

        GET /auditTopic; operationId=getauditTopicIdCode; Protheus >= 12.1.23

        Retorna uma ficha de auditoria pelo número

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return self._request(
            "audit_topic_v1.list_audit_topic",
            "GET",
            "/auditTopic",
            path_params={"internalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_audit_topic(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Cadastra um único Topico de Auditoria

        POST /auditTopic; operationId=postauditTopic; Protheus >= 12.1.23

        Cadastra um Topico de Auditoria

        TOTVS note: Este verbo estiver disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return self._request(
            "audit_topic_v1.create_audit_topic",
            "POST",
            "/auditTopic",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_audit_topic_by_internal_id_itens_table_topic_by_item_id(self, internal_id: str, item_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o cadastro de Topico de auditoria

        PUT /auditTopic/{internalId}/itensTableTopic/{itemId}; operationId=putauditTopic; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.ItensTableTopicInfo
        Request model: protheus.models.audit_topic_v1.ItensTableTopicInfo
        """
        return self._request(
            "audit_topic_v1.update_audit_topic_by_internal_id_itens_table_topic_by_item_id",
            "PUT",
            "/auditTopic/{internalId}/itensTableTopic/{itemId}",
            path_params={"internalId": internal_id, "itemId": item_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncAuditTopicV1(AsyncApiGroup):
    """Tópico de Auditorias (/api/quality/v1)."""

    api_id = "audit_topic_v1"
    base_path = "/api/quality/v1"

    async def get_audit_topic_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um único registro Topico de Auditoria

        GET /auditTopic/{internalId}; operationId=getauditTopicId; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return await self._request(
            "audit_topic_v1.get_audit_topic_by_internal_id",
            "GET",
            "/auditTopic/{internalId}",
            path_params={"internalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_audit_topic_by_internal_id(self, internal_id: str, item_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o cadastro de Topico de auditoria

        PUT /auditTopic/{internalId}; operationId=putauditTopicInternalId; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        Request model: protheus.models.audit_topic_v1.PagedTopic
        """
        return await self._request(
            "audit_topic_v1.update_audit_topic_by_internal_id",
            "PUT",
            "/auditTopic/{internalId}",
            path_params={"internalId": internal_id, "itemId": item_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_audit_topic_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o Topico de auditoria

        DELETE /auditTopic/{internalId}; operationId=putauditQuestionnarieId; Protheus >= 12.1.23

        Deleta

        TOTVS note: Este verbo esta disponível com todos os parametro

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return await self._request(
            "audit_topic_v1.delete_audit_topic_by_internal_id",
            "DELETE",
            "/auditTopic/{internalId}",
            path_params={"internalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_audit_topic(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um único cadastro de topico de auditoria

        GET /auditTopic; operationId=getauditTopicIdCode; Protheus >= 12.1.23

        Retorna uma ficha de auditoria pelo número

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return await self._request(
            "audit_topic_v1.list_audit_topic",
            "GET",
            "/auditTopic",
            path_params={"internalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_audit_topic(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Cadastra um único Topico de Auditoria

        POST /auditTopic; operationId=postauditTopic; Protheus >= 12.1.23

        Cadastra um Topico de Auditoria

        TOTVS note: Este verbo estiver disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.PagedTopic
        """
        return await self._request(
            "audit_topic_v1.create_audit_topic",
            "POST",
            "/auditTopic",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_audit_topic_by_internal_id_itens_table_topic_by_item_id(self, internal_id: str, item_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o cadastro de Topico de auditoria

        PUT /auditTopic/{internalId}/itensTableTopic/{itemId}; operationId=putauditTopic; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.audit_topic_v1.ItensTableTopicInfo
        Request model: protheus.models.audit_topic_v1.ItensTableTopicInfo
        """
        return await self._request(
            "audit_topic_v1.update_audit_topic_by_internal_id_itens_table_topic_by_item_id",
            "PUT",
            "/auditTopic/{internalId}/itensTableTopic/{itemId}",
            path_params={"internalId": internal_id, "itemId": item_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
