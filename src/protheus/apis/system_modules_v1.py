"""Módulos do sistema — generated from SystemModules_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SystemModulesV1(ApiGroup):
    """Módulos do sistema (/api/framework/v1)."""

    api_id = "system_modules_v1"
    base_path = "/api/framework/v1"

    def list_system_modules(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os SystemModules

        GET /systemModules; operationId=getSystemModules; Protheus >= 12.1.25

        Retorna todas os SystemModules

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_modules_v1.PagedBusiness
        """
        return self._request(
            "system_modules_v1.list_system_modules",
            "GET",
            "/systemModules",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_system_modules_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um SystemModules

        GET /systemModules/{id}; operationId=getSystemModulesId; Protheus >= 12.1.25

        Retorna todas os SystemModules

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_modules_v1.BusinessContentType
        """
        return self._request(
            "system_modules_v1.get_system_modules_by_id",
            "GET",
            "/systemModules/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSystemModulesV1(AsyncApiGroup):
    """Módulos do sistema (/api/framework/v1)."""

    api_id = "system_modules_v1"
    base_path = "/api/framework/v1"

    async def list_system_modules(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os SystemModules

        GET /systemModules; operationId=getSystemModules; Protheus >= 12.1.25

        Retorna todas os SystemModules

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_modules_v1.PagedBusiness
        """
        return await self._request(
            "system_modules_v1.list_system_modules",
            "GET",
            "/systemModules",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_system_modules_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um SystemModules

        GET /systemModules/{id}; operationId=getSystemModulesId; Protheus >= 12.1.25

        Retorna todas os SystemModules

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.system_modules_v1.BusinessContentType
        """
        return await self._request(
            "system_modules_v1.get_system_modules_by_id",
            "GET",
            "/systemModules/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
