"""Motivo de Parada — generated from StopReason_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class StopReasonV1(ApiGroup):
    """Motivo de Parada (/api/pcp/v1)."""

    api_id = "stop_reason_v1"
    base_path = "/api/pcp/v1"

    def list_stop_reasons(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Motivos de Parada

        GET /stopReasons; operationId=getStopReasons; Protheus >= 12.1.23

        Retorna lista de motivos de parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.PagedStopReasons
        """
        return self._request(
            "stop_reason_v1.list_stop_reasons",
            "GET",
            "/stopReasons",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_stop_reasons(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Motivo de Parada

        POST /stopReasons; operationId=postStopReason; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        Request model: protheus.models.stop_reason_v1.StopReason
        """
        return self._request(
            "stop_reason_v1.create_stop_reasons",
            "POST",
            "/stopReasons",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_stop_reasons_by_id(self, id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Recupera um Motivo de Parada

        GET /stopReasons/{Id}; operationId=getStopReasonID; Protheus >= 12.1.23

        Retorna um único motivo de parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        """
        return self._request(
            "stop_reason_v1.get_stop_reasons_by_id",
            "GET",
            "/stopReasons/{Id}",
            path_params={"Id": id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_stop_reasons_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um Motivo de Parada

        PUT /stopReasons/{Id}; operationId=putStopReasonID; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        Request model: protheus.models.stop_reason_v1.StopReason
        """
        return self._request(
            "stop_reason_v1.update_stop_reasons_by_id",
            "PUT",
            "/stopReasons/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_stop_reasons_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um Motivo de Parada

        DELETE /stopReasons/{Id}; operationId=deleteStopReasonID; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        """
        return self._request(
            "stop_reason_v1.delete_stop_reasons_by_id",
            "DELETE",
            "/stopReasons/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncStopReasonV1(AsyncApiGroup):
    """Motivo de Parada (/api/pcp/v1)."""

    api_id = "stop_reason_v1"
    base_path = "/api/pcp/v1"

    async def list_stop_reasons(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Motivos de Parada

        GET /stopReasons; operationId=getStopReasons; Protheus >= 12.1.23

        Retorna lista de motivos de parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.PagedStopReasons
        """
        return await self._request(
            "stop_reason_v1.list_stop_reasons",
            "GET",
            "/stopReasons",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_stop_reasons(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Motivo de Parada

        POST /stopReasons; operationId=postStopReason; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        Request model: protheus.models.stop_reason_v1.StopReason
        """
        return await self._request(
            "stop_reason_v1.create_stop_reasons",
            "POST",
            "/stopReasons",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_stop_reasons_by_id(self, id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Recupera um Motivo de Parada

        GET /stopReasons/{Id}; operationId=getStopReasonID; Protheus >= 12.1.23

        Retorna um único motivo de parada

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        """
        return await self._request(
            "stop_reason_v1.get_stop_reasons_by_id",
            "GET",
            "/stopReasons/{Id}",
            path_params={"Id": id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_stop_reasons_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um Motivo de Parada

        PUT /stopReasons/{Id}; operationId=putStopReasonID; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        Request model: protheus.models.stop_reason_v1.StopReason
        """
        return await self._request(
            "stop_reason_v1.update_stop_reasons_by_id",
            "PUT",
            "/stopReasons/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_stop_reasons_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um Motivo de Parada

        DELETE /stopReasons/{Id}; operationId=deleteStopReasonID; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.stop_reason_v1.StopReason
        """
        return await self._request(
            "stop_reason_v1.delete_stop_reasons_by_id",
            "DELETE",
            "/stopReasons/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
