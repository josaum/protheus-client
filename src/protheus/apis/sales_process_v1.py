"""Processo de Venda — generated from SalesProcess_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class SalesProcessV1(ApiGroup):
    """Processo de Venda (/api/crm/v1)."""

    api_id = "sales_process_v1"
    base_path = "/api/crm/v1"

    def list_sales_process(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Processos de Venda

        GET /SalesProcess; operationId=getSalesProcess; Protheus >= 12.1.21

        Retorna lista completa de Processos de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.sales_process_v1.PagedSalesProcess
        """
        return self._request(
            "sales_process_v1.list_sales_process",
            "GET",
            "/SalesProcess",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_sales_process(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Processo de Venda

        POST /SalesProcess; operationId=postSalesProcess; Protheus >= 12.1.21

        Inclui um Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.sales_process_v1.SalesProcessInfo
        Request model: protheus.models.sales_process_v1.SalesProcessInfo
        """
        return self._request(
            "sales_process_v1.create_sales_process",
            "POST",
            "/SalesProcess",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_sales_process_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Processo de Venda pelo seu Código

        GET /SalesProcess/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.sales_process_v1.SalesProcessInfo
        """
        return self._request(
            "sales_process_v1.get_sales_process_by_internal_id",
            "GET",
            "/SalesProcess/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_sales_process_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Processo de Venda

        PUT /SalesProcess/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza cadastro de Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, InternalId e Fields

        Response model: protheus.models.sales_process_v1.SalesProcessInfo
        Request model: protheus.models.sales_process_v1.SalesProcessInfo
        """
        return self._request(
            "sales_process_v1.update_sales_process_by_internal_id",
            "PUT",
            "/SalesProcess/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_sales_process_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Processo de Venda

        DELETE /SalesProcess/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui cadastro de Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return self._request(
            "sales_process_v1.delete_sales_process_by_internal_id",
            "DELETE",
            "/SalesProcess/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_sales_process_by_internal_id_list_of_stages(self, internal_id: str, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Estágios

        GET /SalesProcess/{InternalId}/ListOfStages; operationId=getListOfStages; Protheus >= 12.1.21

        Retorna lista completa de Estágios do Processo de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.sales_process_v1.PagedStages
        """
        return self._request(
            "sales_process_v1.list_sales_process_by_internal_id_list_of_stages",
            "GET",
            "/SalesProcess/{InternalId}/ListOfStages",
            path_params={"InternalId": internal_id},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_sales_process_by_internal_id_list_of_stages(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Estágio no Processo de Venda

        POST /SalesProcess/{InternalId}/ListOfStages; operationId=postListOfStages; Protheus >= 12.1.21

        Inclui um Estágio no Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo não é utilizado.

        Response model: protheus.models.sales_process_v1.StagesInfo
        Request model: protheus.models.sales_process_v1.StagesInfo
        """
        return self._request(
            "sales_process_v1.create_sales_process_by_internal_id_list_of_stages",
            "POST",
            "/SalesProcess/{InternalId}/ListOfStages",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_sales_process_by_internal_id_list_of_stages_by_stage_id(self, internal_id: str, stage_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Estágio do Processo de Venda pelo seu Código

        GET /SalesProcess/{InternalId}/ListOfStages/{StageId}; operationId=getStage; Protheus >= 12.1.21

        Retorna o Estágio do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.sales_process_v1.StagesInfo
        """
        return self._request(
            "sales_process_v1.get_sales_process_by_internal_id_list_of_stages_by_stage_id",
            "GET",
            "/SalesProcess/{InternalId}/ListOfStages/{StageId}",
            path_params={"InternalId": internal_id, "StageId": stage_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_sales_process_by_internal_id_list_of_stages_by_stage_id(self, internal_id: str, stage_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Estágio do Processo de Venda

        PUT /SalesProcess/{InternalId}/ListOfStages/{StageId}; operationId=putStage; Protheus >= 12.1.21

        Atualiza a cadastro de um Estágio do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo não é utilizado.

        Response model: protheus.models.sales_process_v1.StagesInfo
        Request model: protheus.models.sales_process_v1.StagesInfo
        """
        return self._request(
            "sales_process_v1.update_sales_process_by_internal_id_list_of_stages_by_stage_id",
            "PUT",
            "/SalesProcess/{InternalId}/ListOfStages/{StageId}",
            path_params={"InternalId": internal_id, "StageId": stage_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_sales_process_by_internal_id_list_of_stages_by_stage_id(self, internal_id: str, stage_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Estágio

        DELETE /SalesProcess/{InternalId}/ListOfStages/{StageId}; operationId=deleteStage; Protheus >= 12.1.21

        Exclui cadastro de Estágio do Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo não é utilizado.
        """
        return self._request(
            "sales_process_v1.delete_sales_process_by_internal_id_list_of_stages_by_stage_id",
            "DELETE",
            "/SalesProcess/{InternalId}/ListOfStages/{StageId}",
            path_params={"InternalId": internal_id, "StageId": stage_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_sales_process_by_internal_id_list_of_rules(self, internal_id: str, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Regras

        GET /SalesProcess/{InternalId}/ListOfRules; operationId=getListOfRules; Protheus >= 12.1.21

        Retorna lista completa de Regras do Processo de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.sales_process_v1.PagedRules
        """
        return self._request(
            "sales_process_v1.list_sales_process_by_internal_id_list_of_rules",
            "GET",
            "/SalesProcess/{InternalId}/ListOfRules",
            path_params={"InternalId": internal_id},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_sales_process_by_internal_id_list_of_rules(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Regra no Processo de Venda

        POST /SalesProcess/{InternalId}/ListOfRules; operationId=postListOfRules; Protheus >= 12.1.21

        Inclui uma Regra no Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.sales_process_v1.RulesInfo
        Request model: protheus.models.sales_process_v1.RulesInfo
        """
        return self._request(
            "sales_process_v1.create_sales_process_by_internal_id_list_of_rules",
            "POST",
            "/SalesProcess/{InternalId}/ListOfRules",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_sales_process_by_internal_id_list_of_rules_by_rule_id(self, internal_id: str, rule_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Regra do Processo de Venda pelo seu Código

        GET /SalesProcess/{InternalId}/ListOfRules/{RuleId}; operationId=getRule; Protheus >= 12.1.21

        Retorna a Regra do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.sales_process_v1.RulesInfo
        """
        return self._request(
            "sales_process_v1.get_sales_process_by_internal_id_list_of_rules_by_rule_id",
            "GET",
            "/SalesProcess/{InternalId}/ListOfRules/{RuleId}",
            path_params={"InternalId": internal_id, "RuleId": rule_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_sales_process_by_internal_id_list_of_rules_by_rule_id(self, internal_id: str, rule_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Regra do Processo de Venda

        PUT /SalesProcess/{InternalId}/ListOfRules/{RuleId}; operationId=putRule; Protheus >= 12.1.21

        Atualiza a cadastro de uma Regra do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, InternalId e Fields

        Response model: protheus.models.sales_process_v1.RulesInfo
        Request model: protheus.models.sales_process_v1.RulesInfo
        """
        return self._request(
            "sales_process_v1.update_sales_process_by_internal_id_list_of_rules_by_rule_id",
            "PUT",
            "/SalesProcess/{InternalId}/ListOfRules/{RuleId}",
            path_params={"InternalId": internal_id, "RuleId": rule_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_sales_process_by_internal_id_list_of_rules_by_rule_id(self, internal_id: str, rule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Regra

        DELETE /SalesProcess/{InternalId}/ListOfRules/{RuleId}; operationId=deleteRule; Protheus >= 12.1.21

        Exclui cadastro da Regra do Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return self._request(
            "sales_process_v1.delete_sales_process_by_internal_id_list_of_rules_by_rule_id",
            "DELETE",
            "/SalesProcess/{InternalId}/ListOfRules/{RuleId}",
            path_params={"InternalId": internal_id, "RuleId": rule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncSalesProcessV1(AsyncApiGroup):
    """Processo de Venda (/api/crm/v1)."""

    api_id = "sales_process_v1"
    base_path = "/api/crm/v1"

    async def list_sales_process(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Processos de Venda

        GET /SalesProcess; operationId=getSalesProcess; Protheus >= 12.1.21

        Retorna lista completa de Processos de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.sales_process_v1.PagedSalesProcess
        """
        return await self._request(
            "sales_process_v1.list_sales_process",
            "GET",
            "/SalesProcess",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_sales_process(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Processo de Venda

        POST /SalesProcess; operationId=postSalesProcess; Protheus >= 12.1.21

        Inclui um Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.sales_process_v1.SalesProcessInfo
        Request model: protheus.models.sales_process_v1.SalesProcessInfo
        """
        return await self._request(
            "sales_process_v1.create_sales_process",
            "POST",
            "/SalesProcess",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_sales_process_by_internal_id(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Processo de Venda pelo seu Código

        GET /SalesProcess/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna o Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.sales_process_v1.SalesProcessInfo
        """
        return await self._request(
            "sales_process_v1.get_sales_process_by_internal_id",
            "GET",
            "/SalesProcess/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_sales_process_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Processo de Venda

        PUT /SalesProcess/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Atualiza cadastro de Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, InternalId e Fields

        Response model: protheus.models.sales_process_v1.SalesProcessInfo
        Request model: protheus.models.sales_process_v1.SalesProcessInfo
        """
        return await self._request(
            "sales_process_v1.update_sales_process_by_internal_id",
            "PUT",
            "/SalesProcess/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_sales_process_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Processo de Venda

        DELETE /SalesProcess/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui cadastro de Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return await self._request(
            "sales_process_v1.delete_sales_process_by_internal_id",
            "DELETE",
            "/SalesProcess/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_sales_process_by_internal_id_list_of_stages(self, internal_id: str, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Estágios

        GET /SalesProcess/{InternalId}/ListOfStages; operationId=getListOfStages; Protheus >= 12.1.21

        Retorna lista completa de Estágios do Processo de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.sales_process_v1.PagedStages
        """
        return await self._request(
            "sales_process_v1.list_sales_process_by_internal_id_list_of_stages",
            "GET",
            "/SalesProcess/{InternalId}/ListOfStages",
            path_params={"InternalId": internal_id},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_sales_process_by_internal_id_list_of_stages(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Estágio no Processo de Venda

        POST /SalesProcess/{InternalId}/ListOfStages; operationId=postListOfStages; Protheus >= 12.1.21

        Inclui um Estágio no Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo não é utilizado.

        Response model: protheus.models.sales_process_v1.StagesInfo
        Request model: protheus.models.sales_process_v1.StagesInfo
        """
        return await self._request(
            "sales_process_v1.create_sales_process_by_internal_id_list_of_stages",
            "POST",
            "/SalesProcess/{InternalId}/ListOfStages",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_sales_process_by_internal_id_list_of_stages_by_stage_id(self, internal_id: str, stage_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Estágio do Processo de Venda pelo seu Código

        GET /SalesProcess/{InternalId}/ListOfStages/{StageId}; operationId=getStage; Protheus >= 12.1.21

        Retorna o Estágio do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.sales_process_v1.StagesInfo
        """
        return await self._request(
            "sales_process_v1.get_sales_process_by_internal_id_list_of_stages_by_stage_id",
            "GET",
            "/SalesProcess/{InternalId}/ListOfStages/{StageId}",
            path_params={"InternalId": internal_id, "StageId": stage_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_sales_process_by_internal_id_list_of_stages_by_stage_id(self, internal_id: str, stage_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Estágio do Processo de Venda

        PUT /SalesProcess/{InternalId}/ListOfStages/{StageId}; operationId=putStage; Protheus >= 12.1.21

        Atualiza a cadastro de um Estágio do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo não é utilizado.

        Response model: protheus.models.sales_process_v1.StagesInfo
        Request model: protheus.models.sales_process_v1.StagesInfo
        """
        return await self._request(
            "sales_process_v1.update_sales_process_by_internal_id_list_of_stages_by_stage_id",
            "PUT",
            "/SalesProcess/{InternalId}/ListOfStages/{StageId}",
            path_params={"InternalId": internal_id, "StageId": stage_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_sales_process_by_internal_id_list_of_stages_by_stage_id(self, internal_id: str, stage_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Estágio

        DELETE /SalesProcess/{InternalId}/ListOfStages/{StageId}; operationId=deleteStage; Protheus >= 12.1.21

        Exclui cadastro de Estágio do Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo não é utilizado.
        """
        return await self._request(
            "sales_process_v1.delete_sales_process_by_internal_id_list_of_stages_by_stage_id",
            "DELETE",
            "/SalesProcess/{InternalId}/ListOfStages/{StageId}",
            path_params={"InternalId": internal_id, "StageId": stage_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_sales_process_by_internal_id_list_of_rules(self, internal_id: str, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Regras

        GET /SalesProcess/{InternalId}/ListOfRules; operationId=getListOfRules; Protheus >= 12.1.21

        Retorna lista completa de Regras do Processo de Venda

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.sales_process_v1.PagedRules
        """
        return await self._request(
            "sales_process_v1.list_sales_process_by_internal_id_list_of_rules",
            "GET",
            "/SalesProcess/{InternalId}/ListOfRules",
            path_params={"InternalId": internal_id},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_sales_process_by_internal_id_list_of_rules(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Regra no Processo de Venda

        POST /SalesProcess/{InternalId}/ListOfRules; operationId=postListOfRules; Protheus >= 12.1.21

        Inclui uma Regra no Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.sales_process_v1.RulesInfo
        Request model: protheus.models.sales_process_v1.RulesInfo
        """
        return await self._request(
            "sales_process_v1.create_sales_process_by_internal_id_list_of_rules",
            "POST",
            "/SalesProcess/{InternalId}/ListOfRules",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_sales_process_by_internal_id_list_of_rules_by_rule_id(self, internal_id: str, rule_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma Regra do Processo de Venda pelo seu Código

        GET /SalesProcess/{InternalId}/ListOfRules/{RuleId}; operationId=getRule; Protheus >= 12.1.21

        Retorna a Regra do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e InternalId.

        Response model: protheus.models.sales_process_v1.RulesInfo
        """
        return await self._request(
            "sales_process_v1.get_sales_process_by_internal_id_list_of_rules_by_rule_id",
            "GET",
            "/SalesProcess/{InternalId}/ListOfRules/{RuleId}",
            path_params={"InternalId": internal_id, "RuleId": rule_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_sales_process_by_internal_id_list_of_rules_by_rule_id(self, internal_id: str, rule_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera uma Regra do Processo de Venda

        PUT /SalesProcess/{InternalId}/ListOfRules/{RuleId}; operationId=putRule; Protheus >= 12.1.21

        Atualiza a cadastro de uma Regra do Processo de Venda conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, InternalId e Fields

        Response model: protheus.models.sales_process_v1.RulesInfo
        Request model: protheus.models.sales_process_v1.RulesInfo
        """
        return await self._request(
            "sales_process_v1.update_sales_process_by_internal_id_list_of_rules_by_rule_id",
            "PUT",
            "/SalesProcess/{InternalId}/ListOfRules/{RuleId}",
            path_params={"InternalId": internal_id, "RuleId": rule_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_sales_process_by_internal_id_list_of_rules_by_rule_id(self, internal_id: str, rule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui uma Regra

        DELETE /SalesProcess/{InternalId}/ListOfRules/{RuleId}; operationId=deleteRule; Protheus >= 12.1.21

        Exclui cadastro da Regra do Processo de Venda conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return await self._request(
            "sales_process_v1.delete_sales_process_by_internal_id_list_of_rules_by_rule_id",
            "DELETE",
            "/SalesProcess/{InternalId}/ListOfRules/{RuleId}",
            path_params={"InternalId": internal_id, "RuleId": rule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
