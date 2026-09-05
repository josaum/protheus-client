"""Total de Nota de Saída — generated from TotalOutputDocument_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class TotalOutputDocumentV1(ApiGroup):
    """Total de Nota de Saída (/api/retail/v1)."""

    api_id = "total_output_document_v1"
    base_path = "/api/retail/v1"

    def list_total_output_document(self, *, branche_internal_id: str | None = None, from_date: str | None = None, to_date: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna quantidade e total de Nota de saída

        GET /TotalOutputDocument; operationId=getTotalOutputDocument; Protheus >= 12.1.21

        QueryString Tags - "Branches" Range de Filials "FromDate" data inicial de busca formato "AAAA-MM-DD" , "ToDate" data final de busca formato "AAAA-MM-DD". Caso não exista nenhum parâmetro será retornado os valores Default "Fromdate" = (Data do Dia - 30 dias) e "Todate" = Data do Dia, para "Branches" = Filial configurada.

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields

        Response model: protheus.models.total_output_document_v1.TotalOutputDocument
        """
        return self._request(
            "total_output_document_v1.list_total_output_document",
            "GET",
            "/TotalOutputDocument",
            path_params={},
            query={"BrancheInternalId": branche_internal_id, "FromDate": from_date, "ToDate": to_date, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_total_output_document_canceled(self, *, branche_internal_id: str | None = None, from_date: str | None = None, to_date: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna quantidade e total de Nota de saída canceladas

        GET /TotalOutputDocument/canceled; operationId=getCanceledSales; Protheus >= 12.1.21

        QueryString Tags - "Branches" Range de Filials "FromDate" data inicial de busca formato "AAAA-MM-DD" , "ToDate" data final de busca formato "AAAA-MM-DD". Caso não exista nenhum parâmetro será retornado os valores Default "Fromdate" = (Data do Dia - 30 dias) e "Todate" = Data do Dia, para "Branches" = Filial configurada.

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields

        Response model: protheus.models.total_output_document_v1.TotalOutputDocument
        """
        return self._request(
            "total_output_document_v1.list_total_output_document_canceled",
            "GET",
            "/TotalOutputDocument/canceled",
            path_params={},
            query={"BrancheInternalId": branche_internal_id, "FromDate": from_date, "ToDate": to_date, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncTotalOutputDocumentV1(AsyncApiGroup):
    """Total de Nota de Saída (/api/retail/v1)."""

    api_id = "total_output_document_v1"
    base_path = "/api/retail/v1"

    async def list_total_output_document(self, *, branche_internal_id: str | None = None, from_date: str | None = None, to_date: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna quantidade e total de Nota de saída

        GET /TotalOutputDocument; operationId=getTotalOutputDocument; Protheus >= 12.1.21

        QueryString Tags - "Branches" Range de Filials "FromDate" data inicial de busca formato "AAAA-MM-DD" , "ToDate" data final de busca formato "AAAA-MM-DD". Caso não exista nenhum parâmetro será retornado os valores Default "Fromdate" = (Data do Dia - 30 dias) e "Todate" = Data do Dia, para "Branches" = Filial configurada.

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields

        Response model: protheus.models.total_output_document_v1.TotalOutputDocument
        """
        return await self._request(
            "total_output_document_v1.list_total_output_document",
            "GET",
            "/TotalOutputDocument",
            path_params={},
            query={"BrancheInternalId": branche_internal_id, "FromDate": from_date, "ToDate": to_date, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_total_output_document_canceled(self, *, branche_internal_id: str | None = None, from_date: str | None = None, to_date: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna quantidade e total de Nota de saída canceladas

        GET /TotalOutputDocument/canceled; operationId=getCanceledSales; Protheus >= 12.1.21

        QueryString Tags - "Branches" Range de Filials "FromDate" data inicial de busca formato "AAAA-MM-DD" , "ToDate" data final de busca formato "AAAA-MM-DD". Caso não exista nenhum parâmetro será retornado os valores Default "Fromdate" = (Data do Dia - 30 dias) e "Todate" = Data do Dia, para "Branches" = Filial configurada.

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields

        Response model: protheus.models.total_output_document_v1.TotalOutputDocument
        """
        return await self._request(
            "total_output_document_v1.list_total_output_document_canceled",
            "GET",
            "/TotalOutputDocument/canceled",
            path_params={},
            query={"BrancheInternalId": branche_internal_id, "FromDate": from_date, "ToDate": to_date, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )
