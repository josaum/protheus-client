"""Classe de Valor — generated from ClassValue_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ClassValueV1(ApiGroup):
    """Classe de Valor (/api/ctb/v1)."""

    api_id = "class_value_v1"
    base_path = "/api/ctb/v1"

    def list_classvalue(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Cadastro de Classe de Valor

        GET /classvalue; operationId=getClassValue; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.class_value_v1.PagedItems
        """
        return self._request(
            "class_value_v1.list_classvalue",
            "GET",
            "/classvalue",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_classvalue(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Incluir uma Classe de Valor

        POST /classvalue; operationId=postClassValue; Protheus >= 12.1.21

        Incluir uma Classe de Valor conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.class_value_v1.PagedItems
        Request model: protheus.models.class_value_v1.BusinessContentType
        """
        return self._request(
            "class_value_v1.create_classvalue",
            "POST",
            "/classvalue",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_classvalue_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Classe de Valor específica de acordo com a chave de pesquisa

        GET /classvalue/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a Classe de Valor de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código da Classe de Valor

        Response model: protheus.models.class_value_v1.BusinessContentType
        """
        return self._request(
            "class_value_v1.get_classvalue_by_internal_id",
            "GET",
            "/classvalue/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_classvalue_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Classe de Valor

        PUT /classvalue/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a Classe de Valor conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.class_value_v1.BusinessContentType
        Request model: protheus.models.class_value_v1.BusinessContentType
        """
        return self._request(
            "class_value_v1.update_classvalue_by_internal_id",
            "PUT",
            "/classvalue/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_classvalue_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Classe de Valor

        DELETE /classvalue/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui uma Classe de Valor conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parametros Authorization e Fields
        """
        return self._request(
            "class_value_v1.delete_classvalue_by_internal_id",
            "DELETE",
            "/classvalue/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncClassValueV1(AsyncApiGroup):
    """Classe de Valor (/api/ctb/v1)."""

    api_id = "class_value_v1"
    base_path = "/api/ctb/v1"

    async def list_classvalue(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna Cadastro de Classe de Valor

        GET /classvalue; operationId=getClassValue; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.class_value_v1.PagedItems
        """
        return await self._request(
            "class_value_v1.list_classvalue",
            "GET",
            "/classvalue",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_classvalue(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Incluir uma Classe de Valor

        POST /classvalue; operationId=postClassValue; Protheus >= 12.1.21

        Incluir uma Classe de Valor conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponivel com os parametros Authorization e Fields

        Response model: protheus.models.class_value_v1.PagedItems
        Request model: protheus.models.class_value_v1.BusinessContentType
        """
        return await self._request(
            "class_value_v1.create_classvalue",
            "POST",
            "/classvalue",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_classvalue_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Classe de Valor específica de acordo com a chave de pesquisa

        GET /classvalue/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna a Classe de Valor de acordo com o ID de pesquisa

        TOTVS note: o InternalId é composto por filial + Código da Classe de Valor

        Response model: protheus.models.class_value_v1.BusinessContentType
        """
        return await self._request(
            "class_value_v1.get_classvalue_by_internal_id",
            "GET",
            "/classvalue/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_classvalue_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Classe de Valor

        PUT /classvalue/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza a Classe de Valor conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponivel com os parametros Authorization, InternalId e Fields

        Response model: protheus.models.class_value_v1.BusinessContentType
        Request model: protheus.models.class_value_v1.BusinessContentType
        """
        return await self._request(
            "class_value_v1.update_classvalue_by_internal_id",
            "PUT",
            "/classvalue/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_classvalue_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Classe de Valor

        DELETE /classvalue/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui uma Classe de Valor conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parametros Authorization e Fields
        """
        return await self._request(
            "class_value_v1.delete_classvalue_by_internal_id",
            "DELETE",
            "/classvalue/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
