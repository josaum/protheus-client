"""Perfil/Grade de Aprovação — generated from ApprovalProfile_v2_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ApprovalProfileV2(ApiGroup):
    """Perfil/Grade de Aprovação (/api/supply/v2)."""

    api_id = "approval_profile_v2"
    base_path = "/api/supply/v2"

    def list_approval_profile(self, *, company_internal_id: str | None = None, approve_value_limit_min: float | None = None, approve_value_limit_max: float | None = None, currency_profile_approve: float | None = None, expense_type_initial: float | None = None, expense_type_end: float | None = None, version: float | None = None, situation: str | None = None, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Perfis de Aprovação.

        GET /approvalProfile; operationId=getapprovalProfile; Protheus >= 12.1.21

        Retorna lista completa de Perfis de Aprovação.

        Response model: protheus.models.approval_profile_v2.PagedapprovalProfile
        """
        return self._request(
            "approval_profile_v2.list_approval_profile",
            "GET",
            "/approvalProfile",
            path_params={},
            query={"companyInternalId": company_internal_id, "approveValueLimitMin": approve_value_limit_min, "approveValueLimitMax": approve_value_limit_max, "currencyProfileApprove": currency_profile_approve, "expenseTypeInitial": expense_type_initial, "expenseTypeEnd": expense_type_end, "version": version, "situation": situation, "order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_approval_profile(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Perfil de Aprovador

        POST /approvalProfile; operationId=postApprovalProfile; Protheus >= 12.1.21

        Inclui um Perfil de Aprovador conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v2.PagedapprovalProfile
        Request model: protheus.models.approval_profile_v2.PagedapprovalProfile
        """
        return self._request(
            "approval_profile_v2.create_approval_profile",
            "POST",
            "/approvalProfile",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_approval_profile_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Perfil de Aprovador

        GET /approvalProfile/{code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parametros Authorization e code.

        Response model: protheus.models.approval_profile_v2.ApprovalProfileInfo
        """
        return self._request(
            "approval_profile_v2.get_approval_profile_by_code",
            "GET",
            "/approvalProfile/{code}",
            path_params={"code": code},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_approval_profile_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Perfil de Aprovação

        PUT /approvalProfile/{code}; operationId=putCode; Protheus >= 12.1.21

        Response model: protheus.models.approval_profile_v2.PagedapprovalProfile
        Request model: protheus.models.approval_profile_v2.PagedapprovalProfile
        """
        return self._request(
            "approval_profile_v2.update_approval_profile_by_code",
            "PUT",
            "/approvalProfile/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_approval_profile_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Perfil de Aprovação

        DELETE /approvalProfile/{code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Perfil de Aprovação conforme dados enviados na requisição.
        """
        return self._request(
            "approval_profile_v2.delete_approval_profile_by_code",
            "DELETE",
            "/approvalProfile/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncApprovalProfileV2(AsyncApiGroup):
    """Perfil/Grade de Aprovação (/api/supply/v2)."""

    api_id = "approval_profile_v2"
    base_path = "/api/supply/v2"

    async def list_approval_profile(self, *, company_internal_id: str | None = None, approve_value_limit_min: float | None = None, approve_value_limit_max: float | None = None, currency_profile_approve: float | None = None, expense_type_initial: float | None = None, expense_type_end: float | None = None, version: float | None = None, situation: str | None = None, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Perfis de Aprovação.

        GET /approvalProfile; operationId=getapprovalProfile; Protheus >= 12.1.21

        Retorna lista completa de Perfis de Aprovação.

        Response model: protheus.models.approval_profile_v2.PagedapprovalProfile
        """
        return await self._request(
            "approval_profile_v2.list_approval_profile",
            "GET",
            "/approvalProfile",
            path_params={},
            query={"companyInternalId": company_internal_id, "approveValueLimitMin": approve_value_limit_min, "approveValueLimitMax": approve_value_limit_max, "currencyProfileApprove": currency_profile_approve, "expenseTypeInitial": expense_type_initial, "expenseTypeEnd": expense_type_end, "version": version, "situation": situation, "order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_approval_profile(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Perfil de Aprovador

        POST /approvalProfile; operationId=postApprovalProfile; Protheus >= 12.1.21

        Inclui um Perfil de Aprovador conforme dados enviados na requisição.

        Response model: protheus.models.approval_profile_v2.PagedapprovalProfile
        Request model: protheus.models.approval_profile_v2.PagedapprovalProfile
        """
        return await self._request(
            "approval_profile_v2.create_approval_profile",
            "POST",
            "/approvalProfile",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_approval_profile_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Perfil de Aprovador

        GET /approvalProfile/{code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parametros Authorization e code.

        Response model: protheus.models.approval_profile_v2.ApprovalProfileInfo
        """
        return await self._request(
            "approval_profile_v2.get_approval_profile_by_code",
            "GET",
            "/approvalProfile/{code}",
            path_params={"code": code},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_approval_profile_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Perfil de Aprovação

        PUT /approvalProfile/{code}; operationId=putCode; Protheus >= 12.1.21

        Response model: protheus.models.approval_profile_v2.PagedapprovalProfile
        Request model: protheus.models.approval_profile_v2.PagedapprovalProfile
        """
        return await self._request(
            "approval_profile_v2.update_approval_profile_by_code",
            "PUT",
            "/approvalProfile/{code}",
            path_params={"code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_approval_profile_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Perfil de Aprovação

        DELETE /approvalProfile/{code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui um Perfil de Aprovação conforme dados enviados na requisição.
        """
        return await self._request(
            "approval_profile_v2.delete_approval_profile_by_code",
            "DELETE",
            "/approvalProfile/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
