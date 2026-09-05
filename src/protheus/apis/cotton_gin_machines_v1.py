"""CottonGinMachines — generated from CottonGinMachines_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CottonGinMachinesV1(ApiGroup):
    """CottonGinMachines (/api/agr/v1)."""

    api_id = "cotton_gin_machines_v1"
    base_path = "/api/agr/v1"

    def list_cotton_gin_machines(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os conjuntos de beneficiamento cadastrados.

        GET /CottonGinMachines; operationId=getCottonGinMachinesID; Protheus >= 12.1.23

        Retorna todos os conjuntos de beneficiamento de algodão cadastrados.

        Response model: protheus.models.cotton_gin_machines_v1.PagedCottonGinMachines
        """
        return self._request(
            "cotton_gin_machines_v1.list_cotton_gin_machines",
            "GET",
            "/CottonGinMachines",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_cotton_gin_machines(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Efetua o cadastro de um conjunto.

        POST /CottonGinMachines; operationId=postCottonGinMachineID; Protheus >= 12.1.23

        Efetua o cadastro de um conjunto de beneficiamento de algodão.

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return self._request(
            "cotton_gin_machines_v1.create_cotton_gin_machines",
            "POST",
            "/CottonGinMachines",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_cotton_gin_machines_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um conjunto.

        GET /CottonGinMachines/{InternalId}; operationId=getCottonGinMachineID; Protheus >= 12.1.23

        Retorna o conjunto de beneficiamento requerido.

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return self._request(
            "cotton_gin_machines_v1.get_cotton_gin_machines_by_internal_id",
            "GET",
            "/CottonGinMachines/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_cotton_gin_machines_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o conjunto.

        PUT /CottonGinMachines/{InternalId}; operationId=putCottonGinMachineID; Protheus >= 12.1.23

        Altera o conjunto de benficiamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        Request model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return self._request(
            "cotton_gin_machines_v1.update_cotton_gin_machines_by_internal_id",
            "PUT",
            "/CottonGinMachines/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_cotton_gin_machines_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui o conjunto.

        DELETE /CottonGinMachines/{InternalId}; operationId=deleteCottonGinMachineID; Protheus >= 12.1.23

        Exclui o conjunto de beneficiamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return self._request(
            "cotton_gin_machines_v1.delete_cotton_gin_machines_by_internal_id",
            "DELETE",
            "/CottonGinMachines/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncCottonGinMachinesV1(AsyncApiGroup):
    """CottonGinMachines (/api/agr/v1)."""

    api_id = "cotton_gin_machines_v1"
    base_path = "/api/agr/v1"

    async def list_cotton_gin_machines(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os conjuntos de beneficiamento cadastrados.

        GET /CottonGinMachines; operationId=getCottonGinMachinesID; Protheus >= 12.1.23

        Retorna todos os conjuntos de beneficiamento de algodão cadastrados.

        Response model: protheus.models.cotton_gin_machines_v1.PagedCottonGinMachines
        """
        return await self._request(
            "cotton_gin_machines_v1.list_cotton_gin_machines",
            "GET",
            "/CottonGinMachines",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_cotton_gin_machines(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Efetua o cadastro de um conjunto.

        POST /CottonGinMachines; operationId=postCottonGinMachineID; Protheus >= 12.1.23

        Efetua o cadastro de um conjunto de beneficiamento de algodão.

        TOTVS note: Este verbo esta disponível com todos os parametros

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return await self._request(
            "cotton_gin_machines_v1.create_cotton_gin_machines",
            "POST",
            "/CottonGinMachines",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_cotton_gin_machines_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um conjunto.

        GET /CottonGinMachines/{InternalId}; operationId=getCottonGinMachineID; Protheus >= 12.1.23

        Retorna o conjunto de beneficiamento requerido.

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return await self._request(
            "cotton_gin_machines_v1.get_cotton_gin_machines_by_internal_id",
            "GET",
            "/CottonGinMachines/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_cotton_gin_machines_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o conjunto.

        PUT /CottonGinMachines/{InternalId}; operationId=putCottonGinMachineID; Protheus >= 12.1.23

        Altera o conjunto de benficiamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        Request model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return await self._request(
            "cotton_gin_machines_v1.update_cotton_gin_machines_by_internal_id",
            "PUT",
            "/CottonGinMachines/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_cotton_gin_machines_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui o conjunto.

        DELETE /CottonGinMachines/{InternalId}; operationId=deleteCottonGinMachineID; Protheus >= 12.1.23

        Exclui o conjunto de beneficiamento informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.cotton_gin_machines_v1.CottonGinMachinesType
        """
        return await self._request(
            "cotton_gin_machines_v1.delete_cotton_gin_machines_by_internal_id",
            "DELETE",
            "/CottonGinMachines/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
