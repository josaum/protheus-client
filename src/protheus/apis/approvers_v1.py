"""Aprovadores — generated from Approvers_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ApproversV1(ApiGroup):
    """Aprovadores (/api/supply/v1)."""

    api_id = "approvers_v1"
    base_path = "/api/supply/v1"

    def list_approvers(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Aprovadores do sistema.

        GET /approvers; operationId=getApprovers; Protheus >= 12.1.21

        Retorna todos Aprovadores do sistema

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.approvers_v1.PagedApprove
        """
        return self._request(
            "approvers_v1.list_approvers",
            "GET",
            "/approvers",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_approvers(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Aprovadores passado na requisição.

        POST /approvers; operationId=postApprover; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.approvers_v1.ApproversInfo
        Request model: protheus.models.approvers_v1.ApproversInfo
        """
        return self._request(
            "approvers_v1.create_approvers",
            "POST",
            "/approvers",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_approvers_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o usuário do sistema indicado.

        GET /approvers/{code}; operationId=getApproverID; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.approvers_v1.ApproversInfo
        """
        return self._request(
            "approvers_v1.get_approvers_by_code",
            "GET",
            "/approvers/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_approvers_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Aprovador passado na requisição.

        PUT /approvers/{code}; operationId=putApproversId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.approvers_v1.ApproversInfo
        Request model: protheus.models.approvers_v1.ApproversInfo
        """
        return self._request(
            "approvers_v1.update_approvers_by_code",
            "PUT",
            "/approvers/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_approvers_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão do Aprovador.

        DELETE /approvers/{code}; operationId=deleteApproverId

        Response model: protheus.models.approvers_v1.ApproversInfo
        """
        return self._request(
            "approvers_v1.delete_approvers_by_code",
            "DELETE",
            "/approvers/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncApproversV1(AsyncApiGroup):
    """Aprovadores (/api/supply/v1)."""

    api_id = "approvers_v1"
    base_path = "/api/supply/v1"

    async def list_approvers(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os Aprovadores do sistema.

        GET /approvers; operationId=getApprovers; Protheus >= 12.1.21

        Retorna todos Aprovadores do sistema

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.approvers_v1.PagedApprove
        """
        return await self._request(
            "approvers_v1.list_approvers",
            "GET",
            "/approvers",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_approvers(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui Aprovadores passado na requisição.

        POST /approvers; operationId=postApprover; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.approvers_v1.ApproversInfo
        Request model: protheus.models.approvers_v1.ApproversInfo
        """
        return await self._request(
            "approvers_v1.create_approvers",
            "POST",
            "/approvers",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_approvers_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o usuário do sistema indicado.

        GET /approvers/{code}; operationId=getApproverID; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.approvers_v1.ApproversInfo
        """
        return await self._request(
            "approvers_v1.get_approvers_by_code",
            "GET",
            "/approvers/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_approvers_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Aprovador passado na requisição.

        PUT /approvers/{code}; operationId=putApproversId; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros.

        Response model: protheus.models.approvers_v1.ApproversInfo
        Request model: protheus.models.approvers_v1.ApproversInfo
        """
        return await self._request(
            "approvers_v1.update_approvers_by_code",
            "PUT",
            "/approvers/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_approvers_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclusão do Aprovador.

        DELETE /approvers/{code}; operationId=deleteApproverId

        Response model: protheus.models.approvers_v1.ApproversInfo
        """
        return await self._request(
            "approvers_v1.delete_approvers_by_code",
            "DELETE",
            "/approvers/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
