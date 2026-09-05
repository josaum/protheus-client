"""Manifest — generated from Manifest_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ManifestV1(ApiGroup):
    """Manifest (/api/gfe/v1)."""

    api_id = "manifest_v1"
    base_path = "/api/gfe/v1"

    def list_manifest(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os romaneios cadastrados.

        GET /Manifest; operationId=getManifest; Protheus >= 12.1.27

        Response model: protheus.models.manifest_v1.PagedManifest
        """
        return self._request(
            "manifest_v1.list_manifest",
            "GET",
            "/Manifest",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_manifest_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um romaneio.

        GET /Manifest/{Id}; operationId=getManifestID; Protheus >= 12.1.27

        Retorna o romaneio requerido

        Response model: protheus.models.manifest_v1.Manifest
        """
        return self._request(
            "manifest_v1.get_manifest_by_id",
            "GET",
            "/Manifest/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_manifest_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um romaneio.

        POST /Manifest/{Id}; operationId=postManifestID; Protheus >= 12.1.27

        Inclui o romaneio.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.manifest_v1.Manifest
        Request model: protheus.models.manifest_v1.Manifest
        """
        return self._request(
            "manifest_v1.create_manifest_by_id",
            "POST",
            "/Manifest/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def update_manifest_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um romaneio.

        PUT /Manifest/{Id}; operationId=putManifestID; Protheus >= 12.1.27

        Altera o romaneio informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.manifest_v1.Manifest
        Request model: protheus.models.manifest_v1.Manifest
        """
        return self._request(
            "manifest_v1.update_manifest_by_id",
            "PUT",
            "/Manifest/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncManifestV1(AsyncApiGroup):
    """Manifest (/api/gfe/v1)."""

    api_id = "manifest_v1"
    base_path = "/api/gfe/v1"

    async def list_manifest(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os romaneios cadastrados.

        GET /Manifest; operationId=getManifest; Protheus >= 12.1.27

        Response model: protheus.models.manifest_v1.PagedManifest
        """
        return await self._request(
            "manifest_v1.list_manifest",
            "GET",
            "/Manifest",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_manifest_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um romaneio.

        GET /Manifest/{Id}; operationId=getManifestID; Protheus >= 12.1.27

        Retorna o romaneio requerido

        Response model: protheus.models.manifest_v1.Manifest
        """
        return await self._request(
            "manifest_v1.get_manifest_by_id",
            "GET",
            "/Manifest/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_manifest_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um romaneio.

        POST /Manifest/{Id}; operationId=postManifestID; Protheus >= 12.1.27

        Inclui o romaneio.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.manifest_v1.Manifest
        Request model: protheus.models.manifest_v1.Manifest
        """
        return await self._request(
            "manifest_v1.create_manifest_by_id",
            "POST",
            "/Manifest/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def update_manifest_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um romaneio.

        PUT /Manifest/{Id}; operationId=putManifestID; Protheus >= 12.1.27

        Altera o romaneio informado.

        TOTVS note: Este verbo esta disponível com todos os parâmetros

        Response model: protheus.models.manifest_v1.Manifest
        Request model: protheus.models.manifest_v1.Manifest
        """
        return await self._request(
            "manifest_v1.update_manifest_by_id",
            "PUT",
            "/Manifest/{Id}",
            path_params={"Id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
