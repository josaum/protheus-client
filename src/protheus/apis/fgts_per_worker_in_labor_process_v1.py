"""Evento Totalizador S-5503 — generated from FGTSPerWorkerInLaborProcess_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class FgtsPerWorkerInLaborProcessV1(ApiGroup):
    """Evento Totalizador S-5503 (/api/rh/esocial/v1)."""

    api_id = "fgts_per_worker_in_labor_process_v1"
    base_path = "/api/rh/esocial/v1"

    def list_fgts_per_worker_in_labor_process(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Registros S-5503 | Listagem

        GET /FGTSPerWorkerInLaborProcess; operationId=getFGTSPerWorkerInLaborProcess; Protheus >= xx.x.xx

        Carrega registros do evento S-5503, filtrados ou não, ordenados ou não.

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessItems
        """
        return self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process",
            "GET",
            "/FGTSPerWorkerInLaborProcess",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def delete_fgts_per_worker_in_labor_process(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> None:
        """Registros S-5503 | Exclusão

        DELETE /FGTSPerWorkerInLaborProcess; operationId=deleteFGTSPerWorkerInLaborProcess; Protheus >= xx.x.xx

        Exclui eventos S-5503 conforme coleção de ID's informados.

        TOTVS note: Este verbo está disponível com os parâmetros companyId e coleção de id's

        Request model: protheus.models.fgts_per_worker_in_labor_process_v1.RecordsToSelect
        """
        return self._request(
            "fgts_per_worker_in_labor_process_v1.delete_fgts_per_worker_in_labor_process",
            "DELETE",
            "/FGTSPerWorkerInLaborProcess",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def list_fgts_per_worker_in_labor_process_xml(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Registros S-5503 | XML

        GET /FGTSPerWorkerInLaborProcess/XML; operationId=postFGTSPerWorkerInLaborProcessXML; Protheus >= xx.x.xx

        Retorna XML's do evento S-5503 encodados em base64

        TOTVS note: Este verbo está disponível com os parâmetros companyId e coleção de id's

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessXMLItems
        Request model: protheus.models.fgts_per_worker_in_labor_process_v1.RecordsToSelect
        """
        return self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process_xml",
            "GET",
            "/FGTSPerWorkerInLaborProcess/XML",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def list_fgts_per_worker_in_labor_process_worker_registration_and_category(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Trabalhador do S-5503 | Informações Relativas a Matrícula e Categoria

        GET /FGTSPerWorkerInLaborProcess/Worker/RegistrationAndCategory; operationId=getFGTSPerWorkerInLaborProcess/Worker/RegistrationAndCategory; Protheus >= xx.x.xx

        Carrega informações relativas a Matrícula e Categoria de trabalhador específico do evento S-5503, ordenadas ou não.

        TOTVS note: Este verbo está disponível com os parâmetros companyId e id

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessWorkerRegistrationAndCategoryItems
        """
        return self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process_worker_registration_and_category",
            "GET",
            "/FGTSPerWorkerInLaborProcess/Worker/RegistrationAndCategory",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_fgts_per_worker_in_labor_process_worker_payment_and_amounts(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Trabalhador do S-5503 | Identificação do estabelecimento responsável pelo pagamento dos valores informados

        GET /FGTSPerWorkerInLaborProcess/Worker/PaymentAndAmounts; operationId=getFGTSPerWorkerInLaborProcess/Worker/PaymentAndAmounts; Protheus >= xx.x.xx

        Carrega informações relativas a Identificação do estabelecimento responsável pelo pagamento a trabalhador específico dos valores informados do evento S-5503, ordenadas ou não

        TOTVS note: Este verbo está disponível com os parâmetros companyId e id

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessWorkerPaymentAndAmountsItems
        """
        return self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process_worker_payment_and_amounts",
            "GET",
            "/FGTSPerWorkerInLaborProcess/Worker/PaymentAndAmounts",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncFgtsPerWorkerInLaborProcessV1(AsyncApiGroup):
    """Evento Totalizador S-5503 (/api/rh/esocial/v1)."""

    api_id = "fgts_per_worker_in_labor_process_v1"
    base_path = "/api/rh/esocial/v1"

    async def list_fgts_per_worker_in_labor_process(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Registros S-5503 | Listagem

        GET /FGTSPerWorkerInLaborProcess; operationId=getFGTSPerWorkerInLaborProcess; Protheus >= xx.x.xx

        Carrega registros do evento S-5503, filtrados ou não, ordenados ou não.

        TOTVS note: Este verbo está disponível com todos os parâmetros

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessItems
        """
        return await self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process",
            "GET",
            "/FGTSPerWorkerInLaborProcess",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def delete_fgts_per_worker_in_labor_process(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> None:
        """Registros S-5503 | Exclusão

        DELETE /FGTSPerWorkerInLaborProcess; operationId=deleteFGTSPerWorkerInLaborProcess; Protheus >= xx.x.xx

        Exclui eventos S-5503 conforme coleção de ID's informados.

        TOTVS note: Este verbo está disponível com os parâmetros companyId e coleção de id's

        Request model: protheus.models.fgts_per_worker_in_labor_process_v1.RecordsToSelect
        """
        return await self._request(
            "fgts_per_worker_in_labor_process_v1.delete_fgts_per_worker_in_labor_process",
            "DELETE",
            "/FGTSPerWorkerInLaborProcess",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def list_fgts_per_worker_in_labor_process_xml(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Registros S-5503 | XML

        GET /FGTSPerWorkerInLaborProcess/XML; operationId=postFGTSPerWorkerInLaborProcessXML; Protheus >= xx.x.xx

        Retorna XML's do evento S-5503 encodados em base64

        TOTVS note: Este verbo está disponível com os parâmetros companyId e coleção de id's

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessXMLItems
        Request model: protheus.models.fgts_per_worker_in_labor_process_v1.RecordsToSelect
        """
        return await self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process_xml",
            "GET",
            "/FGTSPerWorkerInLaborProcess/XML",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def list_fgts_per_worker_in_labor_process_worker_registration_and_category(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Trabalhador do S-5503 | Informações Relativas a Matrícula e Categoria

        GET /FGTSPerWorkerInLaborProcess/Worker/RegistrationAndCategory; operationId=getFGTSPerWorkerInLaborProcess/Worker/RegistrationAndCategory; Protheus >= xx.x.xx

        Carrega informações relativas a Matrícula e Categoria de trabalhador específico do evento S-5503, ordenadas ou não.

        TOTVS note: Este verbo está disponível com os parâmetros companyId e id

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessWorkerRegistrationAndCategoryItems
        """
        return await self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process_worker_registration_and_category",
            "GET",
            "/FGTSPerWorkerInLaborProcess/Worker/RegistrationAndCategory",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_fgts_per_worker_in_labor_process_worker_payment_and_amounts(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Trabalhador do S-5503 | Identificação do estabelecimento responsável pelo pagamento dos valores informados

        GET /FGTSPerWorkerInLaborProcess/Worker/PaymentAndAmounts; operationId=getFGTSPerWorkerInLaborProcess/Worker/PaymentAndAmounts; Protheus >= xx.x.xx

        Carrega informações relativas a Identificação do estabelecimento responsável pelo pagamento a trabalhador específico dos valores informados do evento S-5503, ordenadas ou não

        TOTVS note: Este verbo está disponível com os parâmetros companyId e id

        Response model: protheus.models.fgts_per_worker_in_labor_process_v1.FGTSPerWorkerInLaborProcessWorkerPaymentAndAmountsItems
        """
        return await self._request(
            "fgts_per_worker_in_labor_process_v1.list_fgts_per_worker_in_labor_process_worker_payment_and_amounts",
            "GET",
            "/FGTSPerWorkerInLaborProcess/Worker/PaymentAndAmounts",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
