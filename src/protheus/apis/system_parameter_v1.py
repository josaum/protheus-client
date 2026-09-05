"""Parametros de Sistema — generated from SystemParameter_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SystemParameterV1(ApiGroup):
    """Parametros de Sistema (/api/framework/v1)."""

    api_id = "system_parameter_v1"
    base_path = "/api/framework/v1"

    def list_system_parameters(self, *, codes: str | None = None, description: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os parâmetros do sistema

        GET /systemParameters; operationId=getSystemParameters; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_parameter_v1.PagedParameters
        """
        return self._request(
            "system_parameter_v1.list_system_parameters",
            "GET",
            "/systemParameters",
            path_params={},
            query={"codes": codes, "description": description, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_system_parameters(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o parâmetro passado na requisição

        POST /systemParameters; operationId=postParameter; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_parameter_v1.PagedParameters
        Request model: protheus.models.system_parameter_v1.ParameterInfo
        """
        return self._request(
            "system_parameter_v1.create_system_parameters",
            "POST",
            "/systemParameters",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def update_system_parameters_by_system_parameter_id(self, system_parameter_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o parâmetro passado na requisição

        PUT /systemParameters/{systemParameterId}; operationId=postParameterId; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_parameter_v1.ParameterInfo
        Request model: protheus.models.system_parameter_v1.ParameterInfo
        """
        return self._request(
            "system_parameter_v1.update_system_parameters_by_system_parameter_id",
            "PUT",
            "/systemParameters/{systemParameterId}",
            path_params={"systemParameterId": system_parameter_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_system_parameters_by_system_parameter_id(self, system_parameter_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de parâmetro da base

        DELETE /systemParameters/{systemParameterId}; operationId=DeleteParameterId

        Response model: protheus.models.system_parameter_v1.ParameterInfo
        """
        return self._request(
            "system_parameter_v1.delete_system_parameters_by_system_parameter_id",
            "DELETE",
            "/systemParameters/{systemParameterId}",
            path_params={"systemParameterId": system_parameter_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSystemParameterV1(AsyncApiGroup):
    """Parametros de Sistema (/api/framework/v1)."""

    api_id = "system_parameter_v1"
    base_path = "/api/framework/v1"

    async def list_system_parameters(self, *, codes: str | None = None, description: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os parâmetros do sistema

        GET /systemParameters; operationId=getSystemParameters; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_parameter_v1.PagedParameters
        """
        return await self._request(
            "system_parameter_v1.list_system_parameters",
            "GET",
            "/systemParameters",
            path_params={},
            query={"codes": codes, "description": description, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_system_parameters(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui o parâmetro passado na requisição

        POST /systemParameters; operationId=postParameter; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_parameter_v1.PagedParameters
        Request model: protheus.models.system_parameter_v1.ParameterInfo
        """
        return await self._request(
            "system_parameter_v1.create_system_parameters",
            "POST",
            "/systemParameters",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def update_system_parameters_by_system_parameter_id(self, system_parameter_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o parâmetro passado na requisição

        PUT /systemParameters/{systemParameterId}; operationId=postParameterId; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_parameter_v1.ParameterInfo
        Request model: protheus.models.system_parameter_v1.ParameterInfo
        """
        return await self._request(
            "system_parameter_v1.update_system_parameters_by_system_parameter_id",
            "PUT",
            "/systemParameters/{systemParameterId}",
            path_params={"systemParameterId": system_parameter_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_system_parameters_by_system_parameter_id(self, system_parameter_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de parâmetro da base

        DELETE /systemParameters/{systemParameterId}; operationId=DeleteParameterId

        Response model: protheus.models.system_parameter_v1.ParameterInfo
        """
        return await self._request(
            "system_parameter_v1.delete_system_parameters_by_system_parameter_id",
            "DELETE",
            "/systemParameters/{systemParameterId}",
            path_params={"systemParameterId": system_parameter_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
