"""GrainQualityTestKinds — generated from GrainQualityTestKinds_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class GrainQualityTestKindsV1(ApiGroup):
    """GrainQualityTestKinds (/api/agr/v1)."""

    api_id = "grain_quality_test_kinds_v1"
    base_path = "/api/agr/v1"

    def list_grain_quality_test_kinds(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os tipos de desconto da classificação cadastrados.

        GET /GrainQualityTestKinds; operationId=getGrainQualityTestKindsID; Protheus >= 12.1.23

        Retorna todos os tipos de desconto da classificação.

        Response model: protheus.models.grain_quality_test_kinds_v1.PagedGrainQualityTestKinds
        """
        return self._request(
            "grain_quality_test_kinds_v1.list_grain_quality_test_kinds",
            "GET",
            "/GrainQualityTestKinds",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_grain_quality_test_kinds(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um tipo de desconto da classificação.

        POST /GrainQualityTestKinds; operationId=postGrainQualityTestKinds; Protheus >= 12.1.23

        Inclui o tipo de desconto passado na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return self._request(
            "grain_quality_test_kinds_v1.create_grain_quality_test_kinds",
            "POST",
            "/GrainQualityTestKinds",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_grain_quality_test_kinds_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o tipo de desconto.

        GET /GrainQualityTestKinds/{InternalId}; operationId=getGrainQualityTestKindID; Protheus >= 12.1.23

        Retorna o tipo de desconto informado pelo parâmetro

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return self._request(
            "grain_quality_test_kinds_v1.get_grain_quality_test_kinds_by_internal_id",
            "GET",
            "/GrainQualityTestKinds/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_grain_quality_test_kinds_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o tipo de desconto.

        PUT /GrainQualityTestKinds/{InternalId}; operationId=putGrainQualityTestKindsID; Protheus >= 12.1.23

        Altera o tipo de desconto informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        Request model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return self._request(
            "grain_quality_test_kinds_v1.update_grain_quality_test_kinds_by_internal_id",
            "PUT",
            "/GrainQualityTestKinds/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_grain_quality_test_kinds_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o tipo de desconto.

        DELETE /GrainQualityTestKinds/{InternalId}; operationId=DeleteGrainQualityTestKindsID; Protheus >= 12.1.23

        Deleção do tipo de desconto dos registros.

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return self._request(
            "grain_quality_test_kinds_v1.delete_grain_quality_test_kinds_by_internal_id",
            "DELETE",
            "/GrainQualityTestKinds/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncGrainQualityTestKindsV1(AsyncApiGroup):
    """GrainQualityTestKinds (/api/agr/v1)."""

    api_id = "grain_quality_test_kinds_v1"
    base_path = "/api/agr/v1"

    async def list_grain_quality_test_kinds(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os tipos de desconto da classificação cadastrados.

        GET /GrainQualityTestKinds; operationId=getGrainQualityTestKindsID; Protheus >= 12.1.23

        Retorna todos os tipos de desconto da classificação.

        Response model: protheus.models.grain_quality_test_kinds_v1.PagedGrainQualityTestKinds
        """
        return await self._request(
            "grain_quality_test_kinds_v1.list_grain_quality_test_kinds",
            "GET",
            "/GrainQualityTestKinds",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_grain_quality_test_kinds(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um tipo de desconto da classificação.

        POST /GrainQualityTestKinds; operationId=postGrainQualityTestKinds; Protheus >= 12.1.23

        Inclui o tipo de desconto passado na requisição.

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return await self._request(
            "grain_quality_test_kinds_v1.create_grain_quality_test_kinds",
            "POST",
            "/GrainQualityTestKinds",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_grain_quality_test_kinds_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o tipo de desconto.

        GET /GrainQualityTestKinds/{InternalId}; operationId=getGrainQualityTestKindID; Protheus >= 12.1.23

        Retorna o tipo de desconto informado pelo parâmetro

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return await self._request(
            "grain_quality_test_kinds_v1.get_grain_quality_test_kinds_by_internal_id",
            "GET",
            "/GrainQualityTestKinds/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_grain_quality_test_kinds_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o tipo de desconto.

        PUT /GrainQualityTestKinds/{InternalId}; operationId=putGrainQualityTestKindsID; Protheus >= 12.1.23

        Altera o tipo de desconto informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        Request model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return await self._request(
            "grain_quality_test_kinds_v1.update_grain_quality_test_kinds_by_internal_id",
            "PUT",
            "/GrainQualityTestKinds/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_grain_quality_test_kinds_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Deleta o tipo de desconto.

        DELETE /GrainQualityTestKinds/{InternalId}; operationId=DeleteGrainQualityTestKindsID; Protheus >= 12.1.23

        Deleção do tipo de desconto dos registros.

        Response model: protheus.models.grain_quality_test_kinds_v1.GrainQualityTestKindsType
        """
        return await self._request(
            "grain_quality_test_kinds_v1.delete_grain_quality_test_kinds_by_internal_id",
            "DELETE",
            "/GrainQualityTestKinds/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
