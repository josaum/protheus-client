"""Usuário — generated from User_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class UserV1(ApiGroup):
    """Usuário (/api/framework/v1)."""

    api_id = "user_v1"
    base_path = "/api/framework/v1"

    def list_users(self, *, user_ids: str | None = None, name: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos usuários do sistema

        GET /users; operationId=getUsers; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.PagedUsers
        """
        return self._request(
            "user_v1.list_users",
            "GET",
            "/users",
            path_params={},
            query={"userIds": user_ids, "name": name, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_users(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui usuário passado na requisição

        POST /users; operationId=postUser; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.PostUser
        Request model: protheus.models.user_v1.PostUser
        """
        return self._request(
            "user_v1.create_users",
            "POST",
            "/users",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_users_by_id(self, id: str, *, found_by: str | None = None, domain_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o usuário do sistema indicado

        GET /users/{id}; operationId=getUserId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.UserInfo
        """
        return self._request(
            "user_v1.get_users_by_id",
            "GET",
            "/users/{id}",
            path_params={"id": id},
            query={"foundBy": found_by, "domainId": domain_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_users_by_id(self, id: str, *, body: Body, found_by: str | None = None, domain_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o usuário passado na requisição

        PUT /users/{id}; operationId=postUserId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.UserInfo
        Request model: protheus.models.user_v1.UserInfo
        """
        return self._request(
            "user_v1.update_users_by_id",
            "PUT",
            "/users/{id}",
            path_params={"id": id},
            query={"foundBy": found_by, "domainId": domain_id},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_users_by_id(self, id: str, *, found_by: str | None = None, domain_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de usuário da base

        DELETE /users/{id}; operationId=DeleteUserId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.UserInfo
        """
        return self._request(
            "user_v1.delete_users_by_id",
            "DELETE",
            "/users/{id}",
            path_params={"id": id},
            query={"foundBy": found_by, "domainId": domain_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncUserV1(AsyncApiGroup):
    """Usuário (/api/framework/v1)."""

    api_id = "user_v1"
    base_path = "/api/framework/v1"

    async def list_users(self, *, user_ids: str | None = None, name: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos usuários do sistema

        GET /users; operationId=getUsers; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.PagedUsers
        """
        return await self._request(
            "user_v1.list_users",
            "GET",
            "/users",
            path_params={},
            query={"userIds": user_ids, "name": name, "order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_users(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui usuário passado na requisição

        POST /users; operationId=postUser; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.PostUser
        Request model: protheus.models.user_v1.PostUser
        """
        return await self._request(
            "user_v1.create_users",
            "POST",
            "/users",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_users_by_id(self, id: str, *, found_by: str | None = None, domain_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o usuário do sistema indicado

        GET /users/{id}; operationId=getUserId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.UserInfo
        """
        return await self._request(
            "user_v1.get_users_by_id",
            "GET",
            "/users/{id}",
            path_params={"id": id},
            query={"foundBy": found_by, "domainId": domain_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_users_by_id(self, id: str, *, body: Body, found_by: str | None = None, domain_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o usuário passado na requisição

        PUT /users/{id}; operationId=postUserId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.UserInfo
        Request model: protheus.models.user_v1.UserInfo
        """
        return await self._request(
            "user_v1.update_users_by_id",
            "PUT",
            "/users/{id}",
            path_params={"id": id},
            query={"foundBy": found_by, "domainId": domain_id},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_users_by_id(self, id: str, *, found_by: str | None = None, domain_id: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão de usuário da base

        DELETE /users/{id}; operationId=DeleteUserId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.user_v1.UserInfo
        """
        return await self._request(
            "user_v1.delete_users_by_id",
            "DELETE",
            "/users/{id}",
            path_params={"id": id},
            query={"foundBy": found_by, "domainId": domain_id},
            headers={},
            body=None,
            extra_query=extra_query,
        )
