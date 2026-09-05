"""Apontamento de Visita — generated from Annotation_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AnnotationV1(ApiGroup):
    """Apontamento de Visita (/api/crm/v1)."""

    api_id = "annotation_v1"
    base_path = "/api/crm/v1"

    def list_annotations(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de apontamentos de visita

        GET /annotations; operationId=getAnnotation; Protheus >= 12.1.21

        Retorna lista completa dos apontamentos de visita

        TOTVS note: Este verbo este disponível com os parametros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.annotation_v1.PagedAnnotation
        """
        return self._request(
            "annotation_v1.list_annotations",
            "GET",
            "/annotations",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_annotations(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Apontamemto de Visita

        POST /annotations; operationId=postAnnotation; Protheus >= 12.1.21

        Inclui um apontamento de visita conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.annotation_v1.AnnotationInfo
        Request model: protheus.models.annotation_v1.AnnotationInfo
        """
        return self._request(
            "annotation_v1.create_annotations",
            "POST",
            "/annotations",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_annotations_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Apontamento de Visita pelo Id

        GET /annotations/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o apontamento de visita pelo InternalId

        TOTVS note: Este verbo este disponivel com todos os parametros

        Response model: protheus.models.annotation_v1.AnnotationInfo
        """
        return self._request(
            "annotation_v1.get_annotations_by_internal_id",
            "GET",
            "/annotations/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_annotations_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma apontamento de visita pelo InternalId

        PUT /annotations/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o apontamento de visita conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.annotation_v1.AnnotationInfo
        Request model: protheus.models.annotation_v1.AnnotationInfo
        """
        return self._request(
            "annotation_v1.update_annotations_by_internal_id",
            "PUT",
            "/annotations/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_annotations_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma apontamento de visita pelo InternalId

        DELETE /annotations/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui a apontamento de visita conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return self._request(
            "annotation_v1.delete_annotations_by_internal_id",
            "DELETE",
            "/annotations/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncAnnotationV1(AsyncApiGroup):
    """Apontamento de Visita (/api/crm/v1)."""

    api_id = "annotation_v1"
    base_path = "/api/crm/v1"

    async def list_annotations(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de apontamentos de visita

        GET /annotations; operationId=getAnnotation; Protheus >= 12.1.21

        Retorna lista completa dos apontamentos de visita

        TOTVS note: Este verbo este disponível com os parametros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.annotation_v1.PagedAnnotation
        """
        return await self._request(
            "annotation_v1.list_annotations",
            "GET",
            "/annotations",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_annotations(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Apontamemto de Visita

        POST /annotations; operationId=postAnnotation; Protheus >= 12.1.21

        Inclui um apontamento de visita conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.annotation_v1.AnnotationInfo
        Request model: protheus.models.annotation_v1.AnnotationInfo
        """
        return await self._request(
            "annotation_v1.create_annotations",
            "POST",
            "/annotations",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_annotations_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Apontamento de Visita pelo Id

        GET /annotations/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o apontamento de visita pelo InternalId

        TOTVS note: Este verbo este disponivel com todos os parametros

        Response model: protheus.models.annotation_v1.AnnotationInfo
        """
        return await self._request(
            "annotation_v1.get_annotations_by_internal_id",
            "GET",
            "/annotations/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_annotations_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma apontamento de visita pelo InternalId

        PUT /annotations/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza o apontamento de visita conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.annotation_v1.AnnotationInfo
        Request model: protheus.models.annotation_v1.AnnotationInfo
        """
        return await self._request(
            "annotation_v1.update_annotations_by_internal_id",
            "PUT",
            "/annotations/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_annotations_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma apontamento de visita pelo InternalId

        DELETE /annotations/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui a apontamento de visita conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields
        """
        return await self._request(
            "annotation_v1.delete_annotations_by_internal_id",
            "DELETE",
            "/annotations/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
