"""Motivos de Refugo — generated from WasteReason_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class WasteReasonV1(ApiGroup):
    """Motivos de Refugo (/api/pcp/v1)."""

    api_id = "waste_reason_v1"
    base_path = "/api/pcp/v1"

    def list_waste_reasons(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Motivos de Refugo

        GET /wasteReasons; operationId=getWasteReasons; Protheus >= 12.1.23

        Retorna lista de motivos de refugo

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.PagedWasteReasons
        """
        return self._request(
            "waste_reason_v1.list_waste_reasons",
            "GET",
            "/wasteReasons",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_waste_reasons(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Motivo de Refugo

        POST /wasteReasons; operationId=postWasteReason; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        Request model: protheus.models.waste_reason_v1.WasteReason
        """
        return self._request(
            "waste_reason_v1.create_waste_reasons",
            "POST",
            "/wasteReasons",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_waste_reasons_by_code(self, code: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Motivo de Refugo

        GET /wasteReasons/{Code}; operationId=getWasteReasonCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        """
        return self._request(
            "waste_reason_v1.get_waste_reasons_by_code",
            "GET",
            "/wasteReasons/{Code}",
            path_params={"Code": code},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_waste_reasons_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um Motivo de Refugo

        PUT /wasteReasons/{Code}; operationId=putWasteReasonCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        Request model: protheus.models.waste_reason_v1.WasteReason
        """
        return self._request(
            "waste_reason_v1.update_waste_reasons_by_code",
            "PUT",
            "/wasteReasons/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_waste_reasons_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um Motivo de Refugo

        DELETE /wasteReasons/{Code}; operationId=deleteWasteReasonCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        """
        return self._request(
            "waste_reason_v1.delete_waste_reasons_by_code",
            "DELETE",
            "/wasteReasons/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncWasteReasonV1(AsyncApiGroup):
    """Motivos de Refugo (/api/pcp/v1)."""

    api_id = "waste_reason_v1"
    base_path = "/api/pcp/v1"

    async def list_waste_reasons(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Lista de Motivos de Refugo

        GET /wasteReasons; operationId=getWasteReasons; Protheus >= 12.1.23

        Retorna lista de motivos de refugo

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.PagedWasteReasons
        """
        return await self._request(
            "waste_reason_v1.list_waste_reasons",
            "GET",
            "/wasteReasons",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_waste_reasons(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Adiciona novo Motivo de Refugo

        POST /wasteReasons; operationId=postWasteReason; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        Request model: protheus.models.waste_reason_v1.WasteReason
        """
        return await self._request(
            "waste_reason_v1.create_waste_reasons",
            "POST",
            "/wasteReasons",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_waste_reasons_by_code(self, code: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Motivo de Refugo

        GET /wasteReasons/{Code}; operationId=getWasteReasonCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        """
        return await self._request(
            "waste_reason_v1.get_waste_reasons_by_code",
            "GET",
            "/wasteReasons/{Code}",
            path_params={"Code": code},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_waste_reasons_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um Motivo de Refugo

        PUT /wasteReasons/{Code}; operationId=putWasteReasonCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        Request model: protheus.models.waste_reason_v1.WasteReason
        """
        return await self._request(
            "waste_reason_v1.update_waste_reasons_by_code",
            "PUT",
            "/wasteReasons/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_waste_reasons_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Remove um Motivo de Refugo

        DELETE /wasteReasons/{Code}; operationId=deleteWasteReasonCode; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.waste_reason_v1.WasteReason
        """
        return await self._request(
            "waste_reason_v1.delete_waste_reasons_by_code",
            "DELETE",
            "/wasteReasons/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
