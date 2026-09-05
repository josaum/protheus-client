"""FreightAccountingBatches — generated from FreightAccountingBatches_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class FreightAccountingBatchesV1(ApiGroup):
    """FreightAccountingBatches (/api/gfe/v1)."""

    api_id = "freight_accounting_batches_v1"
    base_path = "/api/gfe/v1"

    def list_freight_accounting_batches(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os lotes de provisão cadastrados.

        GET /FreightAccountingBatches; operationId=getFreightAccountingBatch; Protheus >= 12.1.30

        Response model: protheus.models.freight_accounting_batches_v1.PagedFreightAccountingBatches
        """
        return self._request(
            "freight_accounting_batches_v1.list_freight_accounting_batches",
            "GET",
            "/FreightAccountingBatches",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_freight_accounting_batches_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um lote de provisão.

        GET /FreightAccountingBatches/{InternalId}; operationId=getFreightAccountingBatchesID; Protheus >= 12.1.30

        Retorna apenas um lote de provisão, requerido através da chave do registro (InternalId).

        Response model: protheus.models.freight_accounting_batches_v1.FreightAccountingBatchesType
        """
        return self._request(
            "freight_accounting_batches_v1.get_freight_accounting_batches_by_internal_id",
            "GET",
            "/FreightAccountingBatches/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_freight_accounting_batches_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a situação de um lote de provisão.

        PUT /FreightAccountingBatches/{InternalId}; operationId=UpdateFreightAccountingBatch; Protheus >= 12.1.30

        Altera a situação do lote de provisão informado através da chave (InternalId).

        TOTVS note: Este verbo esta disponí­vel com todos os parâmetros

        Response model: protheus.models.freight_accounting_batches_v1.FreightAccountingBatchesType
        Request model: protheus.models.freight_accounting_batches_v1.FreightAccountingBatchesType
        """
        return self._request(
            "freight_accounting_batches_v1.update_freight_accounting_batches_by_internal_id",
            "PUT",
            "/FreightAccountingBatches/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncFreightAccountingBatchesV1(AsyncApiGroup):
    """FreightAccountingBatches (/api/gfe/v1)."""

    api_id = "freight_accounting_batches_v1"
    base_path = "/api/gfe/v1"

    async def list_freight_accounting_batches(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos os lotes de provisão cadastrados.

        GET /FreightAccountingBatches; operationId=getFreightAccountingBatch; Protheus >= 12.1.30

        Response model: protheus.models.freight_accounting_batches_v1.PagedFreightAccountingBatches
        """
        return await self._request(
            "freight_accounting_batches_v1.list_freight_accounting_batches",
            "GET",
            "/FreightAccountingBatches",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_freight_accounting_batches_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um lote de provisão.

        GET /FreightAccountingBatches/{InternalId}; operationId=getFreightAccountingBatchesID; Protheus >= 12.1.30

        Retorna apenas um lote de provisão, requerido através da chave do registro (InternalId).

        Response model: protheus.models.freight_accounting_batches_v1.FreightAccountingBatchesType
        """
        return await self._request(
            "freight_accounting_batches_v1.get_freight_accounting_batches_by_internal_id",
            "GET",
            "/FreightAccountingBatches/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_freight_accounting_batches_by_internal_id(self, internal_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera a situação de um lote de provisão.

        PUT /FreightAccountingBatches/{InternalId}; operationId=UpdateFreightAccountingBatch; Protheus >= 12.1.30

        Altera a situação do lote de provisão informado através da chave (InternalId).

        TOTVS note: Este verbo esta disponí­vel com todos os parâmetros

        Response model: protheus.models.freight_accounting_batches_v1.FreightAccountingBatchesType
        Request model: protheus.models.freight_accounting_batches_v1.FreightAccountingBatchesType
        """
        return await self._request(
            "freight_accounting_batches_v1.update_freight_accounting_batches_by_internal_id",
            "PUT",
            "/FreightAccountingBatches/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
