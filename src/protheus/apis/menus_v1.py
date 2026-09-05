"""Menus — generated from Menus_v1_001.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class MenusV1(ApiGroup):
    """Menus (/api/framework/v1)."""

    api_id = "menus_v1"
    base_path = "/api/framework/v1"

    def list_menus(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os resources

        GET /menus; operationId=getResources; Protheus >= 12.1.21

        Retorna todas os resources

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.menus_v1.PagedBusiness
        """
        return self._request(
            "menus_v1.list_menus",
            "GET",
            "/menus",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_menus_by_parent_id(self, parent_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os resources

        GET /menus/{parentId}; operationId=getResourcesId; Protheus >= 12.1.21

        Retorna todas os resources

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.menus_v1.PagedBusiness
        """
        return self._request(
            "menus_v1.get_menus_by_parent_id",
            "GET",
            "/menus/{parentId}",
            path_params={"parentId": parent_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncMenusV1(AsyncApiGroup):
    """Menus (/api/framework/v1)."""

    api_id = "menus_v1"
    base_path = "/api/framework/v1"

    async def list_menus(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os resources

        GET /menus; operationId=getResources; Protheus >= 12.1.21

        Retorna todas os resources

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.menus_v1.PagedBusiness
        """
        return await self._request(
            "menus_v1.list_menus",
            "GET",
            "/menus",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_menus_by_parent_id(self, parent_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os resources

        GET /menus/{parentId}; operationId=getResourcesId; Protheus >= 12.1.21

        Retorna todas os resources

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.menus_v1.PagedBusiness
        """
        return await self._request(
            "menus_v1.get_menus_by_parent_id",
            "GET",
            "/menus/{parentId}",
            path_params={"parentId": parent_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
