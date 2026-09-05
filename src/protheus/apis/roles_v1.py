"""Papeis — generated from Roles_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class RolesV1(ApiGroup):
    """Papeis (/api/framework/v1)."""

    api_id = "roles_v1"
    base_path = "/api/framework/v1"

    def list_roles(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Papeis

        GET /roles; operationId=getRoles; Protheus >= 12.1.21

        Retorna todas os Roles

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.roles_v1.PagedRoles
        """
        return self._request(
            "roles_v1.list_roles",
            "GET",
            "/roles",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncRolesV1(AsyncApiGroup):
    """Papeis (/api/framework/v1)."""

    api_id = "roles_v1"
    base_path = "/api/framework/v1"

    async def list_roles(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Papeis

        GET /roles; operationId=getRoles; Protheus >= 12.1.21

        Retorna todas os Roles

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.roles_v1.PagedRoles
        """
        return await self._request(
            "roles_v1.list_roles",
            "GET",
            "/roles",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )
