"""Segmentos de Mercado — generated from MarketSegment_v2_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MarketSegmentV2(ApiGroup):
    """Segmentos de Mercado (/api/services/crm/v2)."""

    api_id = "market_segment_v2"
    base_path = "/api/services/crm/v2"

    def list_market_segment(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos Segmentos

        GET /marketSegment; operationId=getmarketSegment; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.market_segment_v2.PagedMarketSegments
        """
        return self._request(
            "market_segment_v2.list_market_segment",
            "GET",
            "/marketSegment",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_market_segment(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Segmento enviado na requisição

        POST /marketSegment; operationId=postmarketSegmentID

        Inclui segmento passado na requisição

        TOTVS note: Este verbo está disponível com o parâmetros Authorization

        Response model: protheus.models.market_segment_v2.MarketSegmentsInfo
        Request model: protheus.models.market_segment_v2.MarketSegmentsInfo
        """
        return self._request(
            "market_segment_v2.create_market_segment",
            "POST",
            "/marketSegment",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_market_segment_by_market_segment_id(self, market_segment_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Segmento

        GET /marketSegment/{marketSegmentID}; operationId=getmarketSegmentID; Protheus >= 12.1.21

        Retorna  Segmento com base em seu Código

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e MarketSegmentId

        Response model: protheus.models.market_segment_v2.MarketSegmentsInfo
        """
        return self._request(
            "market_segment_v2.get_market_segment_by_market_segment_id",
            "GET",
            "/marketSegment/{marketSegmentID}",
            path_params={"marketSegmentID": market_segment_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_market_segment_by_market_segment_id(self, market_segment_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza registro de segmento passado na requisição

        PUT /marketSegment/{marketSegmentID}; operationId=putmarketSegmentID; Protheus >= 12.1.21

        Atualiza o segmento informado na requisição

        TOTVS note: Este verbo está disponível com os parâmetros authorization e MarketSegmentId

        Response model: protheus.models.market_segment_v2.MarketSegmentsInfo
        Request model: protheus.models.market_segment_v2.MarketSegmentsInfo
        """
        return self._request(
            "market_segment_v2.update_market_segment_by_market_segment_id",
            "PUT",
            "/marketSegment/{marketSegmentID}",
            path_params={"marketSegmentID": market_segment_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_market_segment_by_market_segment_id(self, market_segment_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui o segmento passado na requisição

        DELETE /marketSegment/{marketSegmentID}; operationId=deletemarketSegmentID; Protheus >= 12.1.21

        Exclui o cadastro de segmento passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros authorization e MarketSegmentId
        """
        return self._request(
            "market_segment_v2.delete_market_segment_by_market_segment_id",
            "DELETE",
            "/marketSegment/{marketSegmentID}",
            path_params={"marketSegmentID": market_segment_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncMarketSegmentV2(AsyncApiGroup):
    """Segmentos de Mercado (/api/services/crm/v2)."""

    api_id = "market_segment_v2"
    base_path = "/api/services/crm/v2"

    async def list_market_segment(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos Segmentos

        GET /marketSegment; operationId=getmarketSegment; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.market_segment_v2.PagedMarketSegments
        """
        return await self._request(
            "market_segment_v2.list_market_segment",
            "GET",
            "/marketSegment",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_market_segment(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Segmento enviado na requisição

        POST /marketSegment; operationId=postmarketSegmentID

        Inclui segmento passado na requisição

        TOTVS note: Este verbo está disponível com o parâmetros Authorization

        Response model: protheus.models.market_segment_v2.MarketSegmentsInfo
        Request model: protheus.models.market_segment_v2.MarketSegmentsInfo
        """
        return await self._request(
            "market_segment_v2.create_market_segment",
            "POST",
            "/marketSegment",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_market_segment_by_market_segment_id(self, market_segment_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Segmento

        GET /marketSegment/{marketSegmentID}; operationId=getmarketSegmentID; Protheus >= 12.1.21

        Retorna  Segmento com base em seu Código

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e MarketSegmentId

        Response model: protheus.models.market_segment_v2.MarketSegmentsInfo
        """
        return await self._request(
            "market_segment_v2.get_market_segment_by_market_segment_id",
            "GET",
            "/marketSegment/{marketSegmentID}",
            path_params={"marketSegmentID": market_segment_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_market_segment_by_market_segment_id(self, market_segment_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza registro de segmento passado na requisição

        PUT /marketSegment/{marketSegmentID}; operationId=putmarketSegmentID; Protheus >= 12.1.21

        Atualiza o segmento informado na requisição

        TOTVS note: Este verbo está disponível com os parâmetros authorization e MarketSegmentId

        Response model: protheus.models.market_segment_v2.MarketSegmentsInfo
        Request model: protheus.models.market_segment_v2.MarketSegmentsInfo
        """
        return await self._request(
            "market_segment_v2.update_market_segment_by_market_segment_id",
            "PUT",
            "/marketSegment/{marketSegmentID}",
            path_params={"marketSegmentID": market_segment_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_market_segment_by_market_segment_id(self, market_segment_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui o segmento passado na requisição

        DELETE /marketSegment/{marketSegmentID}; operationId=deletemarketSegmentID; Protheus >= 12.1.21

        Exclui o cadastro de segmento passada na requisição

        TOTVS note: Este verbo está disponível com os parâmetros authorization e MarketSegmentId
        """
        return await self._request(
            "market_segment_v2.delete_market_segment_by_market_segment_id",
            "DELETE",
            "/marketSegment/{marketSegmentID}",
            path_params={"marketSegmentID": market_segment_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
