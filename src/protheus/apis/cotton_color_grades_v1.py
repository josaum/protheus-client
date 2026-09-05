"""CottonColorGrades — generated from CottonColorGrades_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonColorGradesV1(ApiGroup):
    """CottonColorGrades (/api/agr/v1)."""

    api_id = "cotton_color_grades_v1"
    base_path = "/api/agr/v1"

    def list_cotton_color_grades(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os tipos de classificação do algodão cadastrados.

        GET /CottonColorGrades; operationId=getCottonColorGradesID; Protheus >= 12.1.23

        Response model: protheus.models.cotton_color_grades_v1.PagedCottonColorGrades
        """
        return self._request(
            "cotton_color_grades_v1.list_cotton_color_grades",
            "GET",
            "/CottonColorGrades",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cotton_color_grades(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um tipo de classificação.

        POST /CottonColorGrades; operationId=postCottonColorGradeID; Protheus >= 12.1.23

        Inclui o tipo de classificação passado na requisição.

        TOTVS note: Este verbo esta disponível com todos os parametros.

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return self._request(
            "cotton_color_grades_v1.create_cotton_color_grades",
            "POST",
            "/CottonColorGrades",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_cotton_color_grades_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o tipo de classificação.

        GET /CottonColorGrades/{InternalId}; operationId=getCottonColorGradeID; Protheus >= 12.1.23

        Retorna o tipo de classificação informado pelo parâmetro

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return self._request(
            "cotton_color_grades_v1.get_cotton_color_grades_by_internal_id",
            "GET",
            "/CottonColorGrades/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_color_grades_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o tipo de classificação.

        PUT /CottonColorGrades/{InternalId}; operationId=putCottonColorGradesID; Protheus >= 12.1.23

        Altera o tipo de classificação informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        Request model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return self._request(
            "cotton_color_grades_v1.update_cotton_color_grades_by_internal_id",
            "PUT",
            "/CottonColorGrades/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_color_grades_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o tipo de classificação.

        DELETE /CottonColorGrades/{InternalId}; operationId=DeleteCottonColorGradesID; Protheus >= 12.1.23

        Deleção do tipo de classificação dos registros.

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return self._request(
            "cotton_color_grades_v1.delete_cotton_color_grades_by_internal_id",
            "DELETE",
            "/CottonColorGrades/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonColorGradesV1(AsyncApiGroup):
    """CottonColorGrades (/api/agr/v1)."""

    api_id = "cotton_color_grades_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_color_grades(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os tipos de classificação do algodão cadastrados.

        GET /CottonColorGrades; operationId=getCottonColorGradesID; Protheus >= 12.1.23

        Response model: protheus.models.cotton_color_grades_v1.PagedCottonColorGrades
        """
        return await self._request(
            "cotton_color_grades_v1.list_cotton_color_grades",
            "GET",
            "/CottonColorGrades",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cotton_color_grades(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um tipo de classificação.

        POST /CottonColorGrades; operationId=postCottonColorGradeID; Protheus >= 12.1.23

        Inclui o tipo de classificação passado na requisição.

        TOTVS note: Este verbo esta disponível com todos os parametros.

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return await self._request(
            "cotton_color_grades_v1.create_cotton_color_grades",
            "POST",
            "/CottonColorGrades",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_cotton_color_grades_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o tipo de classificação.

        GET /CottonColorGrades/{InternalId}; operationId=getCottonColorGradeID; Protheus >= 12.1.23

        Retorna o tipo de classificação informado pelo parâmetro

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return await self._request(
            "cotton_color_grades_v1.get_cotton_color_grades_by_internal_id",
            "GET",
            "/CottonColorGrades/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_color_grades_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o tipo de classificação.

        PUT /CottonColorGrades/{InternalId}; operationId=putCottonColorGradesID; Protheus >= 12.1.23

        Altera o tipo de classificação informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        Request model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return await self._request(
            "cotton_color_grades_v1.update_cotton_color_grades_by_internal_id",
            "PUT",
            "/CottonColorGrades/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_color_grades_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o tipo de classificação.

        DELETE /CottonColorGrades/{InternalId}; operationId=DeleteCottonColorGradesID; Protheus >= 12.1.23

        Deleção do tipo de classificação dos registros.

        Response model: protheus.models.cotton_color_grades_v1.CottonColorGradesType
        """
        return await self._request(
            "cotton_color_grades_v1.delete_cotton_color_grades_by_internal_id",
            "DELETE",
            "/CottonColorGrades/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
