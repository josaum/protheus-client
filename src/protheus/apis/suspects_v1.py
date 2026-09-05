"""Suspects — generated from Suspects_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SuspectsV1(ApiGroup):
    """Suspects (/api/crm/v1)."""

    api_id = "suspects_v1"
    base_path = "/api/crm/v1"

    def list_suspects(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Suspects

        GET /suspects; operationId=getsuspects; Protheus >= 12.1.21

        Retorna lista completa de Suspects

        Response model: protheus.models.suspects_v1.PagedSuspects
        """
        return self._request(
            "suspects_v1.list_suspects",
            "GET",
            "/suspects",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_suspects(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um suspect

        POST /suspects; operationId=postCode; Protheus >= 12.1.21

        Inclui um Suspect conforme dados enviados na requisição.

        Response model: protheus.models.suspects_v1.SuspectInfo
        Request model: protheus.models.suspects_v1.SuspectInfo
        """
        return self._request(
            "suspects_v1.create_suspects",
            "POST",
            "/suspects",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_suspects_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Suspect pelo seu Código

        GET /suspects/{Code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Code.

        Response model: protheus.models.suspects_v1.SuspectInfo
        """
        return self._request(
            "suspects_v1.get_suspects_by_code",
            "GET",
            "/suspects/{Code}",
            path_params={"Code": code},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_suspects_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Suspect

        PUT /suspects/{Code}; operationId=putCode; Protheus >= 12.1.21

        Atualiza cadastro de Suspect conforme dados enviados na requisição

        Response model: protheus.models.suspects_v1.SuspectInfo
        Request model: protheus.models.suspects_v1.SuspectInfo
        """
        return self._request(
            "suspects_v1.update_suspects_by_code",
            "PUT",
            "/suspects/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_suspects_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Suspect

        DELETE /suspects/{Code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui cadastro de Suspect conforme dados enviados na requisição.

        Response model: protheus.models.suspects_v1.PagedSuspects
        """
        return self._request(
            "suspects_v1.delete_suspects_by_code",
            "DELETE",
            "/suspects/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSuspectsV1(AsyncApiGroup):
    """Suspects (/api/crm/v1)."""

    api_id = "suspects_v1"
    base_path = "/api/crm/v1"

    async def list_suspects(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Suspects

        GET /suspects; operationId=getsuspects; Protheus >= 12.1.21

        Retorna lista completa de Suspects

        Response model: protheus.models.suspects_v1.PagedSuspects
        """
        return await self._request(
            "suspects_v1.list_suspects",
            "GET",
            "/suspects",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_suspects(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um suspect

        POST /suspects; operationId=postCode; Protheus >= 12.1.21

        Inclui um Suspect conforme dados enviados na requisição.

        Response model: protheus.models.suspects_v1.SuspectInfo
        Request model: protheus.models.suspects_v1.SuspectInfo
        """
        return await self._request(
            "suspects_v1.create_suspects",
            "POST",
            "/suspects",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_suspects_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Suspect pelo seu Código

        GET /suspects/{Code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Code.

        Response model: protheus.models.suspects_v1.SuspectInfo
        """
        return await self._request(
            "suspects_v1.get_suspects_by_code",
            "GET",
            "/suspects/{Code}",
            path_params={"Code": code},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_suspects_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Suspect

        PUT /suspects/{Code}; operationId=putCode; Protheus >= 12.1.21

        Atualiza cadastro de Suspect conforme dados enviados na requisição

        Response model: protheus.models.suspects_v1.SuspectInfo
        Request model: protheus.models.suspects_v1.SuspectInfo
        """
        return await self._request(
            "suspects_v1.update_suspects_by_code",
            "PUT",
            "/suspects/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_suspects_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Suspect

        DELETE /suspects/{Code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui cadastro de Suspect conforme dados enviados na requisição.

        Response model: protheus.models.suspects_v1.PagedSuspects
        """
        return await self._request(
            "suspects_v1.delete_suspects_by_code",
            "DELETE",
            "/suspects/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
