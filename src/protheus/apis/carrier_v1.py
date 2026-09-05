"""Transportadora — generated from Carrier_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CarrierV1(ApiGroup):
    """Transportadora (/api/fat/v1)."""

    api_id = "carrier_v1"
    base_path = "/api/fat/v1"

    def list_carrier(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Transportadoras

        GET /carrier; operationId=getCarrier; Protheus >= 12.1.21

        Retorna lista completa de Transportadoras

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.carrier_v1.PagedCarriers
        """
        return self._request(
            "carrier_v1.list_carrier",
            "GET",
            "/carrier",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_carrier(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma transportadora

        POST /carrier; operationId=postCarrier; Protheus >= 12.1.21

        Inclui uma Transportadora conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.carrier_v1.CarrierInfo
        Request model: protheus.models.carrier_v1.CarrierInfo
        """
        return self._request(
            "carrier_v1.create_carrier",
            "POST",
            "/carrier",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_carrier_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a Transportadora pelo seu Código

        GET /carrier/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a Transportadora conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.carrier_v1.CarrierInfo
        """
        return self._request(
            "carrier_v1.get_carrier_by_internal_id",
            "GET",
            "/carrier/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_carrier_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma transportadora

        PUT /carrier/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza cadastro de Transportadoras conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, InternalId e Fields

        Response model: protheus.models.carrier_v1.CarrierInfo
        Request model: protheus.models.carrier_v1.CarrierInfo
        """
        return self._request(
            "carrier_v1.update_carrier_by_internal_id",
            "PUT",
            "/carrier/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_carrier_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui uma transportadora

        DELETE /carrier/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui cadastro de Transportadora conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId

        Response model: protheus.models.carrier_v1.CarrierInfo
        """
        return self._request(
            "carrier_v1.delete_carrier_by_internal_id",
            "DELETE",
            "/carrier/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCarrierV1(AsyncApiGroup):
    """Transportadora (/api/fat/v1)."""

    api_id = "carrier_v1"
    base_path = "/api/fat/v1"

    async def list_carrier(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Transportadoras

        GET /carrier; operationId=getCarrier; Protheus >= 12.1.21

        Retorna lista completa de Transportadoras

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.carrier_v1.PagedCarriers
        """
        return await self._request(
            "carrier_v1.list_carrier",
            "GET",
            "/carrier",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_carrier(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma transportadora

        POST /carrier; operationId=postCarrier; Protheus >= 12.1.21

        Inclui uma Transportadora conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.carrier_v1.CarrierInfo
        Request model: protheus.models.carrier_v1.CarrierInfo
        """
        return await self._request(
            "carrier_v1.create_carrier",
            "POST",
            "/carrier",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_carrier_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a Transportadora pelo seu Código

        GET /carrier/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a Transportadora conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.carrier_v1.CarrierInfo
        """
        return await self._request(
            "carrier_v1.get_carrier_by_internal_id",
            "GET",
            "/carrier/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_carrier_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma transportadora

        PUT /carrier/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza cadastro de Transportadoras conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, InternalId e Fields

        Response model: protheus.models.carrier_v1.CarrierInfo
        Request model: protheus.models.carrier_v1.CarrierInfo
        """
        return await self._request(
            "carrier_v1.update_carrier_by_internal_id",
            "PUT",
            "/carrier/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_carrier_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui uma transportadora

        DELETE /carrier/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui cadastro de Transportadora conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId

        Response model: protheus.models.carrier_v1.CarrierInfo
        """
        return await self._request(
            "carrier_v1.delete_carrier_by_internal_id",
            "DELETE",
            "/carrier/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
