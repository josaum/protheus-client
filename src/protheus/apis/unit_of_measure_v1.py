"""Unidade de Medida — generated from UnitOfMeasure_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class UnitOfMeasureV1(ApiGroup):
    """Unidade de Medida (/api/entradas/v1)."""

    api_id = "unit_of_measure_v1"
    base_path = "/api/entradas/v1"

    def list_unit_of_measures(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Unidade de Medida

        GET /UnitOfMeasures; operationId=getUnitOfMeasures; Protheus >= 12.1.21

        Retorna lista completa de Unidade de Medida

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.PagedUnitOfMeasure
        """
        return self._request(
            "unit_of_measure_v1.list_unit_of_measures",
            "GET",
            "/UnitOfMeasures",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_unit_of_measures(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Unidade de Medida

        POST /UnitOfMeasures; operationId=postUnitOfMeasure; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        Request model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return self._request(
            "unit_of_measure_v1.create_unit_of_measures",
            "POST",
            "/UnitOfMeasures",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_unit_of_measures_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Unidade de Medida pelo seu Código

        GET /UnitOfMeasures/{Code}; operationId=getUnitOfMeasure; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return self._request(
            "unit_of_measure_v1.get_unit_of_measures_by_code",
            "GET",
            "/UnitOfMeasures/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_unit_of_measures_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza cadastro de Unidade de Medida conforme dados enviados na requisição

        PUT /UnitOfMeasures/{Code}; operationId=putUnitOfMeasure; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        Request model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return self._request(
            "unit_of_measure_v1.update_unit_of_measures_by_code",
            "PUT",
            "/UnitOfMeasures/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_unit_of_measures_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui Unidade de Medida cadastrada conforme dados enviados na requisição

        DELETE /UnitOfMeasures/{Code}; operationId=DeleteUnitOfMeasure

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return self._request(
            "unit_of_measure_v1.delete_unit_of_measures_by_code",
            "DELETE",
            "/UnitOfMeasures/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncUnitOfMeasureV1(AsyncApiGroup):
    """Unidade de Medida (/api/entradas/v1)."""

    api_id = "unit_of_measure_v1"
    base_path = "/api/entradas/v1"

    async def list_unit_of_measures(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Unidade de Medida

        GET /UnitOfMeasures; operationId=getUnitOfMeasures; Protheus >= 12.1.21

        Retorna lista completa de Unidade de Medida

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.PagedUnitOfMeasure
        """
        return await self._request(
            "unit_of_measure_v1.list_unit_of_measures",
            "GET",
            "/UnitOfMeasures",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_unit_of_measures(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Unidade de Medida

        POST /UnitOfMeasures; operationId=postUnitOfMeasure; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        Request model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return await self._request(
            "unit_of_measure_v1.create_unit_of_measures",
            "POST",
            "/UnitOfMeasures",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_unit_of_measures_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Unidade de Medida pelo seu Código

        GET /UnitOfMeasures/{Code}; operationId=getUnitOfMeasure; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return await self._request(
            "unit_of_measure_v1.get_unit_of_measures_by_code",
            "GET",
            "/UnitOfMeasures/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_unit_of_measures_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza cadastro de Unidade de Medida conforme dados enviados na requisição

        PUT /UnitOfMeasures/{Code}; operationId=putUnitOfMeasure; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        Request model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return await self._request(
            "unit_of_measure_v1.update_unit_of_measures_by_code",
            "PUT",
            "/UnitOfMeasures/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_unit_of_measures_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui Unidade de Medida cadastrada conforme dados enviados na requisição

        DELETE /UnitOfMeasures/{Code}; operationId=DeleteUnitOfMeasure

        Response model: protheus.models.unit_of_measure_v1.UnitOfMeasureInfo
        """
        return await self._request(
            "unit_of_measure_v1.delete_unit_of_measures_by_code",
            "DELETE",
            "/UnitOfMeasures/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
