"""Painel de Auditoria — generated from AuditPanel_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AuditPanelV1(ApiGroup):
    """Painel de Auditoria (/api/rh/v1)."""

    api_id = "audit_panel_v1"
    base_path = "/api/rh/v1"

    def list_painel_auditoria_period(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Periodos | Listagem

        GET /painel-auditoria/period; operationId=getAuditPeriods; Protheus >= 12.1.2310

        Retorna os períodos de apuração disponíveis no sistema.

        TOTVS note: Retorna os períodos disponíveis para filtro

        Response model: protheus.models.audit_panel_v1.AuditPeriodItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_period",
            "GET",
            "/painel-auditoria/period",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_big_numbers(self, *, month: str | None = None, year: str | None = None, company_id: str | None = None, period: str | None = None, branch_code: str | None = None, feedback: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Indicadores | Resumo

        GET /painel-auditoria/big-numbers; operationId=getBigNumbers; Protheus >= 12.1.2310

        Retorna os totais gerais de conformidades da tela principal.

        TOTVS note: Retorna os indicadores principais (Big Numbers) para o dashboard

        Response model: protheus.models.audit_panel_v1.AuditBigNumbersItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_big_numbers",
            "GET",
            "/painel-auditoria/big-numbers",
            path_params={},
            query={"month": month, "year": year, "companyId": company_id, "period": period, "branchCode": branch_code, "feedback": feedback},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_employees(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Funcionários | Listagem

        GET /painel-auditoria/employees; operationId=getEmployees; Protheus >= 12.1.2310

        Retorna a lista de colaboradores com suas informações básicas e situação atual.

        TOTVS note: Listagem de funcionários com conformidades.

        Response model: protheus.models.audit_panel_v1.AuditEmployeeItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_employees",
            "GET",
            "/painel-auditoria/employees",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_painel_auditoria_update_feedback(self, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Feedback | Atualização

        POST /painel-auditoria/update-feedback; operationId=UpdateFeedback; Protheus >= 12.1.2506

        Envia uma atualização de feedback para um registro de auditoria.

        TOTVS note: Permite atualizar o status de feedback da auditoria
        """
        return self._request(
            "audit_panel_v1.create_painel_auditoria_update_feedback",
            "POST",
            "/painel-auditoria/update-feedback",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_conformities(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, id: str | None = None, description: str | None = None, cpf_cnpj: str | None = None, feedback: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Conformidades | Listagem

        GET /painel-auditoria/conformities; operationId=getConformities; Protheus >= 12.1.2310

        Retorna a estrutura da tabela de conformidades utilizada na exibição das regras.

        TOTVS note: Lista de regras com conformidade

        Response model: protheus.models.audit_panel_v1.AuditConformityItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_conformities",
            "GET",
            "/painel-auditoria/conformities",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "id": id, "description": description, "cpf_cnpj": cpf_cnpj, "feedback": feedback, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_conformities_employees(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, feedback: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Conformidades de Funcionários | Listagem

        GET /painel-auditoria/conformities-employees; operationId=getConformitiesEmployees; Protheus >= 12.1.2310

        Retorna a lista de funcionários com conformidade, agrupando informações básicas para exibição na tabela de funcionarios da tela principal.

        TOTVS note: Lista os funcionários com conformidade

        Response model: protheus.models.audit_panel_v1.AuditConformityEmployeeItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_conformities_employees",
            "GET",
            "/painel-auditoria/conformities-employees",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "feedback": feedback, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_painel_auditoria_conformities_employees_details_by_employee_id(self, employee_id: str, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, feedback: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Detalhes de Conformidades do Funcionário | Listagem

        GET /painel-auditoria/conformities-employees-details/{employeeId}; operationId=getConformitiesEmployeeDetails; Protheus >= 12.1.2310

        Retorna a lista de todas as regras/conformidades vinculadas a um funcionário específico dentro do período selecionado.

        TOTVS note: Lista regras e conformidades de um funcionário

        Response model: protheus.models.audit_panel_v1.AuditConformityEmployeeDetailsItems
        """
        return self._request(
            "audit_panel_v1.get_painel_auditoria_conformities_employees_details_by_employee_id",
            "GET",
            "/painel-auditoria/conformities-employees-details/{employeeId}",
            path_params={"employeeId": employee_id},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "feedback": feedback},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_export_analitico(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, view_type: str | None = None, feedback: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exportação Analítica | Consulta

        GET /painel-auditoria/export-analitico; operationId=getExportAnalitico; Protheus >= 12.1.2310

        Retorna a lista unificada e consolidada (via Inner Join) contendo os dados cadastrais dos funcionários e os detalhes de suas respectivas conformidades para fins de exportação analítica.

        TOTVS note: Exportação dos dados de auditoria

        Response model: protheus.models.audit_panel_v1.AuditExportAnaliticoItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_export_analitico",
            "GET",
            "/painel-auditoria/export-analitico",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "viewType": view_type, "feedback": feedback},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_branches(self, *, company_id: str | None = None, page: int | None = None, page_size: int | None = None, filter: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Filiais | Listagem

        GET /painel-auditoria/branches; operationId=getBranches; Protheus >= 12.1.2310

        Retorna as filiais que o usuário logado tem permissão para visualizar, utilizado para o filtro de unidade de negócio do painel.

        TOTVS note: Retorna as filiais que o usuário logado tem permissão para visualizar.

        Response model: protheus.models.audit_panel_v1.AuditBranchItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_branches",
            "GET",
            "/painel-auditoria/branches",
            path_params={},
            query={"companyId": company_id, "page": page, "pageSize": page_size, "filter": filter},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_last_update(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Última Atualização | Consulta

        GET /painel-auditoria/last-update; operationId=getLastUpdate; Protheus >= 12.1.2310

        Informa a data e hora em que os dados da auditoria foram processados pela última vez no backend, para controle de obsolescência.

        TOTVS note: Verifica o timestamp da última execução do job de auditoria

        Response model: protheus.models.audit_panel_v1.AuditLastUpdate
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_last_update",
            "GET",
            "/painel-auditoria/last-update",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_painel_auditoria_history(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Histórico | Listagem

        GET /painel-auditoria/history; operationId=getHistory; Protheus >= 12.1.2310

        Retorna o histórico de execuções de auditorias passadas, permitindo a comparação de evolução de conformidade entre diferentes períodos.

        TOTVS note: Consulta tabelas históricas de resultados de auditoria

        Response model: protheus.models.audit_panel_v1.AuditHistoryItems
        """
        return self._request(
            "audit_panel_v1.list_painel_auditoria_history",
            "GET",
            "/painel-auditoria/history",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncAuditPanelV1(AsyncApiGroup):
    """Painel de Auditoria (/api/rh/v1)."""

    api_id = "audit_panel_v1"
    base_path = "/api/rh/v1"

    async def list_painel_auditoria_period(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Periodos | Listagem

        GET /painel-auditoria/period; operationId=getAuditPeriods; Protheus >= 12.1.2310

        Retorna os períodos de apuração disponíveis no sistema.

        TOTVS note: Retorna os períodos disponíveis para filtro

        Response model: protheus.models.audit_panel_v1.AuditPeriodItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_period",
            "GET",
            "/painel-auditoria/period",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_big_numbers(self, *, month: str | None = None, year: str | None = None, company_id: str | None = None, period: str | None = None, branch_code: str | None = None, feedback: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Indicadores | Resumo

        GET /painel-auditoria/big-numbers; operationId=getBigNumbers; Protheus >= 12.1.2310

        Retorna os totais gerais de conformidades da tela principal.

        TOTVS note: Retorna os indicadores principais (Big Numbers) para o dashboard

        Response model: protheus.models.audit_panel_v1.AuditBigNumbersItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_big_numbers",
            "GET",
            "/painel-auditoria/big-numbers",
            path_params={},
            query={"month": month, "year": year, "companyId": company_id, "period": period, "branchCode": branch_code, "feedback": feedback},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_employees(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Funcionários | Listagem

        GET /painel-auditoria/employees; operationId=getEmployees; Protheus >= 12.1.2310

        Retorna a lista de colaboradores com suas informações básicas e situação atual.

        TOTVS note: Listagem de funcionários com conformidades.

        Response model: protheus.models.audit_panel_v1.AuditEmployeeItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_employees",
            "GET",
            "/painel-auditoria/employees",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_painel_auditoria_update_feedback(self, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Feedback | Atualização

        POST /painel-auditoria/update-feedback; operationId=UpdateFeedback; Protheus >= 12.1.2506

        Envia uma atualização de feedback para um registro de auditoria.

        TOTVS note: Permite atualizar o status de feedback da auditoria
        """
        return await self._request(
            "audit_panel_v1.create_painel_auditoria_update_feedback",
            "POST",
            "/painel-auditoria/update-feedback",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_conformities(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, id: str | None = None, description: str | None = None, cpf_cnpj: str | None = None, feedback: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Conformidades | Listagem

        GET /painel-auditoria/conformities; operationId=getConformities; Protheus >= 12.1.2310

        Retorna a estrutura da tabela de conformidades utilizada na exibição das regras.

        TOTVS note: Lista de regras com conformidade

        Response model: protheus.models.audit_panel_v1.AuditConformityItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_conformities",
            "GET",
            "/painel-auditoria/conformities",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "id": id, "description": description, "cpf_cnpj": cpf_cnpj, "feedback": feedback, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_conformities_employees(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, feedback: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Conformidades de Funcionários | Listagem

        GET /painel-auditoria/conformities-employees; operationId=getConformitiesEmployees; Protheus >= 12.1.2310

        Retorna a lista de funcionários com conformidade, agrupando informações básicas para exibição na tabela de funcionarios da tela principal.

        TOTVS note: Lista os funcionários com conformidade

        Response model: protheus.models.audit_panel_v1.AuditConformityEmployeeItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_conformities_employees",
            "GET",
            "/painel-auditoria/conformities-employees",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "feedback": feedback, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_painel_auditoria_conformities_employees_details_by_employee_id(self, employee_id: str, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, feedback: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Detalhes de Conformidades do Funcionário | Listagem

        GET /painel-auditoria/conformities-employees-details/{employeeId}; operationId=getConformitiesEmployeeDetails; Protheus >= 12.1.2310

        Retorna a lista de todas as regras/conformidades vinculadas a um funcionário específico dentro do período selecionado.

        TOTVS note: Lista regras e conformidades de um funcionário

        Response model: protheus.models.audit_panel_v1.AuditConformityEmployeeDetailsItems
        """
        return await self._request(
            "audit_panel_v1.get_painel_auditoria_conformities_employees_details_by_employee_id",
            "GET",
            "/painel-auditoria/conformities-employees-details/{employeeId}",
            path_params={"employeeId": employee_id},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "feedback": feedback},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_export_analitico(self, *, month: str | None = None, year: str | None = None, period: str | None = None, company_id: str | None = None, branch_code: str | None = None, view_type: str | None = None, feedback: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exportação Analítica | Consulta

        GET /painel-auditoria/export-analitico; operationId=getExportAnalitico; Protheus >= 12.1.2310

        Retorna a lista unificada e consolidada (via Inner Join) contendo os dados cadastrais dos funcionários e os detalhes de suas respectivas conformidades para fins de exportação analítica.

        TOTVS note: Exportação dos dados de auditoria

        Response model: protheus.models.audit_panel_v1.AuditExportAnaliticoItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_export_analitico",
            "GET",
            "/painel-auditoria/export-analitico",
            path_params={},
            query={"month": month, "year": year, "period": period, "companyId": company_id, "branchCode": branch_code, "viewType": view_type, "feedback": feedback},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_branches(self, *, company_id: str | None = None, page: int | None = None, page_size: int | None = None, filter: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Filiais | Listagem

        GET /painel-auditoria/branches; operationId=getBranches; Protheus >= 12.1.2310

        Retorna as filiais que o usuário logado tem permissão para visualizar, utilizado para o filtro de unidade de negócio do painel.

        TOTVS note: Retorna as filiais que o usuário logado tem permissão para visualizar.

        Response model: protheus.models.audit_panel_v1.AuditBranchItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_branches",
            "GET",
            "/painel-auditoria/branches",
            path_params={},
            query={"companyId": company_id, "page": page, "pageSize": page_size, "filter": filter},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_last_update(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Última Atualização | Consulta

        GET /painel-auditoria/last-update; operationId=getLastUpdate; Protheus >= 12.1.2310

        Informa a data e hora em que os dados da auditoria foram processados pela última vez no backend, para controle de obsolescência.

        TOTVS note: Verifica o timestamp da última execução do job de auditoria

        Response model: protheus.models.audit_panel_v1.AuditLastUpdate
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_last_update",
            "GET",
            "/painel-auditoria/last-update",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_painel_auditoria_history(self, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Histórico | Listagem

        GET /painel-auditoria/history; operationId=getHistory; Protheus >= 12.1.2310

        Retorna o histórico de execuções de auditorias passadas, permitindo a comparação de evolução de conformidade entre diferentes períodos.

        TOTVS note: Consulta tabelas históricas de resultados de auditoria

        Response model: protheus.models.audit_panel_v1.AuditHistoryItems
        """
        return await self._request(
            "audit_panel_v1.list_painel_auditoria_history",
            "GET",
            "/painel-auditoria/history",
            path_params={},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
