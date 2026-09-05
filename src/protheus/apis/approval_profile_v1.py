"""Perfil de Aprovação — generated from ApprovalProfile_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ApprovalProfileV1(ApiGroup):
    """Perfil de Aprovação (/api/framework/v1)."""

    api_id = "approval_profile_v1"
    base_path = "/api/framework/v1"

    def list_supply_approval_profile_info(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Perfis de Aprovação.

        GET /supply/approvalProfileInfo; operationId=getapprovalProfile; Protheus >= 12.1.21

        Retorna lista completa de Perfis de Aprovação.

        Response model: protheus.models.approval_profile_v1.PagedapprovalProfile
        """
        return self._request(
            "approval_profile_v1.list_supply_approval_profile_info",
            "GET",
            "/supply/approvalProfileInfo",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_supply_approval_profile_info(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Perfil de Aprovador

        POST /supply/approvalProfileInfo; operationId=approvalProfile; Protheus >= 12.1.21

        Inclui um Perfil de Aprovador conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v1.PagedapprovalProfile
        Request model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return self._request(
            "approval_profile_v1.create_supply_approval_profile_info",
            "POST",
            "/supply/approvalProfileInfo",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_supply_approval_profile_info_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Perfil de Aprovador

        GET /supply/approvalProfileInfo/{code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parametros Authorization e code.

        Response model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return self._request(
            "approval_profile_v1.get_supply_approval_profile_info_by_code",
            "GET",
            "/supply/approvalProfileInfo/{code}",
            path_params={"code": code},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_supply_approval_profile_info_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Perfil de Aprovação

        PUT /supply/approvalProfileInfo/{code}; operationId=putCode; Protheus >= 12.1.21

        Atualiza o Vlr. Minimo e Vlr. Maximo do Perfil de Aprovador conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        Request model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return self._request(
            "approval_profile_v1.update_supply_approval_profile_info_by_code",
            "PUT",
            "/supply/approvalProfileInfo/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_supply_approval_profile_info_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Perfil de Aprovação

        DELETE /supply/approvalProfileInfo/{code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Perfil de Aprovação conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return self._request(
            "approval_profile_v1.delete_supply_approval_profile_info_by_code",
            "DELETE",
            "/supply/approvalProfileInfo/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncApprovalProfileV1(AsyncApiGroup):
    """Perfil de Aprovação (/api/framework/v1)."""

    api_id = "approval_profile_v1"
    base_path = "/api/framework/v1"

    async def list_supply_approval_profile_info(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Perfis de Aprovação.

        GET /supply/approvalProfileInfo; operationId=getapprovalProfile; Protheus >= 12.1.21

        Retorna lista completa de Perfis de Aprovação.

        Response model: protheus.models.approval_profile_v1.PagedapprovalProfile
        """
        return await self._request(
            "approval_profile_v1.list_supply_approval_profile_info",
            "GET",
            "/supply/approvalProfileInfo",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_supply_approval_profile_info(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Perfil de Aprovador

        POST /supply/approvalProfileInfo; operationId=approvalProfile; Protheus >= 12.1.21

        Inclui um Perfil de Aprovador conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v1.PagedapprovalProfile
        Request model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return await self._request(
            "approval_profile_v1.create_supply_approval_profile_info",
            "POST",
            "/supply/approvalProfileInfo",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_supply_approval_profile_info_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Perfil de Aprovador

        GET /supply/approvalProfileInfo/{code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parametros Authorization e code.

        Response model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return await self._request(
            "approval_profile_v1.get_supply_approval_profile_info_by_code",
            "GET",
            "/supply/approvalProfileInfo/{code}",
            path_params={"code": code},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_supply_approval_profile_info_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Perfil de Aprovação

        PUT /supply/approvalProfileInfo/{code}; operationId=putCode; Protheus >= 12.1.21

        Atualiza o Vlr. Minimo e Vlr. Maximo do Perfil de Aprovador conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        Request model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return await self._request(
            "approval_profile_v1.update_supply_approval_profile_info_by_code",
            "PUT",
            "/supply/approvalProfileInfo/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_supply_approval_profile_info_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Perfil de Aprovação

        DELETE /supply/approvalProfileInfo/{code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Perfil de Aprovação conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v1.ApprovalProfileInfo
        """
        return await self._request(
            "approval_profile_v1.delete_supply_approval_profile_info_by_code",
            "DELETE",
            "/supply/approvalProfileInfo/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
