"""Coletor — generated from UrbanoColetor_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class UrbanoColetorV1(ApiGroup):
    """Coletor (/api/coletorurbano/coletor)."""

    api_id = "urbano_coletor_v1"
    base_path = "/api/coletorurbano/coletor"

    def create_coletor_urbano(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui informações do coletor na prestação de contas

        POST /ColetorUrbano; operationId=PostPrestacao; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.urbano_coletor_v1.ResponseItens
        Request model: protheus.models.urbano_coletor_v1.RequestItens
        """
        return self._request(
            "urbano_coletor_v1.create_coletor_urbano",
            "POST",
            "/ColetorUrbano",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncUrbanoColetorV1(AsyncApiGroup):
    """Coletor (/api/coletorurbano/coletor)."""

    api_id = "urbano_coletor_v1"
    base_path = "/api/coletorurbano/coletor"

    async def create_coletor_urbano(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui informações do coletor na prestação de contas

        POST /ColetorUrbano; operationId=PostPrestacao; Protheus >= 12.1.23

        TOTVS note: Este verbo está disponível com os parâmetros companyId, page e pageSize

        Response model: protheus.models.urbano_coletor_v1.ResponseItens
        Request model: protheus.models.urbano_coletor_v1.RequestItens
        """
        return await self._request(
            "urbano_coletor_v1.create_coletor_urbano",
            "POST",
            "/ColetorUrbano",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
