"""Prospects — generated from Prospects_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ProspectsV1(ApiGroup):
    """Prospects (/api/crm/v1)."""

    api_id = "prospects_v1"
    base_path = "/api/crm/v1"

    def list_prospects(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Prospects

        GET /prospects; operationId=getprospects; Protheus >= 12.1.21

        Retorna lista completa de prospects

        Response model: protheus.models.prospects_v1.PagedProspects
        """
        return self._request(
            "prospects_v1.list_prospects",
            "GET",
            "/prospects",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_prospects(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um prospect

        POST /prospects; operationId=postCode; Protheus >= 12.1.21

        Inclui um prospect conforme dados enviados na requisição.

        Response model: protheus.models.prospects_v1.ProspectInfo
        Request model: protheus.models.prospects_v1.ProspectInfo
        """
        return self._request(
            "prospects_v1.create_prospects",
            "POST",
            "/prospects",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_prospects_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna prospect pelo seu Código

        GET /prospects/{Code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Code.

        Response model: protheus.models.prospects_v1.ProspectInfo
        """
        return self._request(
            "prospects_v1.get_prospects_by_code",
            "GET",
            "/prospects/{Code}",
            path_params={"Code": code},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_prospects_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Prospect

        PUT /prospects/{Code}; operationId=putCode; Protheus >= 12.1.21

        Atualiza cadastro de prospect conforme dados enviados na requisição

        Response model: protheus.models.prospects_v1.ProspectInfo
        Request model: protheus.models.prospects_v1.ProspectInfo
        """
        return self._request(
            "prospects_v1.update_prospects_by_code",
            "PUT",
            "/prospects/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_prospects_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um prospect

        DELETE /prospects/{Code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui cadastro de Prospect conforme dados enviados na requisição.

        Response model: protheus.models.prospects_v1.PagedProspects
        """
        return self._request(
            "prospects_v1.delete_prospects_by_code",
            "DELETE",
            "/prospects/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncProspectsV1(AsyncApiGroup):
    """Prospects (/api/crm/v1)."""

    api_id = "prospects_v1"
    base_path = "/api/crm/v1"

    async def list_prospects(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Prospects

        GET /prospects; operationId=getprospects; Protheus >= 12.1.21

        Retorna lista completa de prospects

        Response model: protheus.models.prospects_v1.PagedProspects
        """
        return await self._request(
            "prospects_v1.list_prospects",
            "GET",
            "/prospects",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_prospects(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um prospect

        POST /prospects; operationId=postCode; Protheus >= 12.1.21

        Inclui um prospect conforme dados enviados na requisição.

        Response model: protheus.models.prospects_v1.ProspectInfo
        Request model: protheus.models.prospects_v1.ProspectInfo
        """
        return await self._request(
            "prospects_v1.create_prospects",
            "POST",
            "/prospects",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_prospects_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna prospect pelo seu Código

        GET /prospects/{Code}; operationId=getCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e Code.

        Response model: protheus.models.prospects_v1.ProspectInfo
        """
        return await self._request(
            "prospects_v1.get_prospects_by_code",
            "GET",
            "/prospects/{Code}",
            path_params={"Code": code},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_prospects_by_code(self, code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Prospect

        PUT /prospects/{Code}; operationId=putCode; Protheus >= 12.1.21

        Atualiza cadastro de prospect conforme dados enviados na requisição

        Response model: protheus.models.prospects_v1.ProspectInfo
        Request model: protheus.models.prospects_v1.ProspectInfo
        """
        return await self._request(
            "prospects_v1.update_prospects_by_code",
            "PUT",
            "/prospects/{Code}",
            path_params={"Code": code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_prospects_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um prospect

        DELETE /prospects/{Code}; operationId=deleteCode; Protheus >= 12.1.21

        Exclui cadastro de Prospect conforme dados enviados na requisição.

        Response model: protheus.models.prospects_v1.PagedProspects
        """
        return await self._request(
            "prospects_v1.delete_prospects_by_code",
            "DELETE",
            "/prospects/{Code}",
            path_params={"Code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
