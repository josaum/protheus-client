"""Agendamento de Serviço — generated from JobScheduler_v1_100.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class JobSchedulerV1100(ApiGroup):
    """Agendamento de Serviço (/api/framework/v1)."""

    api_id = "job_scheduler_v1_100"
    base_path = "/api/framework/v1"

    def list_job_execution(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Informações sobre a execução dos processos

        GET /jobExecution; operationId=getJobExecution; Protheus >= 12.1.23

        Retorna todas as execuções de agendamentos

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.PagedExecutionJobscheduler
        """
        return self._request(
            "job_scheduler_v1_100.list_job_execution",
            "GET",
            "/jobExecution",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_job_execution_by_execution_id(self, execution_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Informações sobre a execução dos processos

        GET /jobExecution/{executionID}; operationId=getexecutionID; Protheus >= 12.1.23

        Retorna todos os agendamentos

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobExecutionType
        """
        return self._request(
            "job_scheduler_v1_100.get_job_execution_by_execution_id",
            "GET",
            "/jobExecution/{executionID}",
            path_params={"executionID": execution_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_job_scheduler(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Busca execuções de processos

        GET /jobScheduler; operationId=getJobschedulerID; Protheus >= 12.1.23

        Retorna todos os agendamentos

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.PagedJobscheduler
        """
        return self._request(
            "job_scheduler_v1_100.list_job_scheduler",
            "GET",
            "/jobScheduler",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_job_scheduler(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Cria agendamento de processo

        POST /jobScheduler; operationId=postJobschedulerID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        Request model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return self._request(
            "job_scheduler_v1_100.create_job_scheduler",
            "POST",
            "/jobScheduler",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_job_scheduler_by_job_schedule_id(self, job_schedule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos Jobscheduler

        GET /jobScheduler/{jobScheduleID}; operationId=getJobschedulerIDs; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return self._request(
            "job_scheduler_v1_100.get_job_scheduler_by_job_schedule_id",
            "GET",
            "/jobScheduler/{jobScheduleID}",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_job_scheduler_by_job_schedule_id(self, job_schedule_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui  Jobscheduler

        PUT /jobScheduler/{jobScheduleID}; operationId=postJobschedulerIDs; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        Request model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return self._request(
            "job_scheduler_v1_100.update_job_scheduler_by_job_schedule_id",
            "PUT",
            "/jobScheduler/{jobScheduleID}",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_job_scheduler_by_job_schedule_id(self, job_schedule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui  Jobscheduler

        DELETE /jobScheduler/{jobScheduleID}; operationId=deleteJobschedulerID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return self._request(
            "job_scheduler_v1_100.delete_job_scheduler_by_job_schedule_id",
            "DELETE",
            "/jobScheduler/{jobScheduleID}",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_job_scheduler_by_job_schedule_id_trigger(self, job_schedule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Dispara a execução um agendamento de processo

        POST /jobScheduler/{jobScheduleID}/trigger; operationId=postJobschedulerIDtrigger; Protheus >= 12.1.23

        TOTVS note: disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return self._request(
            "job_scheduler_v1_100.create_job_scheduler_by_job_schedule_id_trigger",
            "POST",
            "/jobScheduler/{jobScheduleID}/trigger",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncJobSchedulerV1100(AsyncApiGroup):
    """Agendamento de Serviço (/api/framework/v1)."""

    api_id = "job_scheduler_v1_100"
    base_path = "/api/framework/v1"

    async def list_job_execution(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Informações sobre a execução dos processos

        GET /jobExecution; operationId=getJobExecution; Protheus >= 12.1.23

        Retorna todas as execuções de agendamentos

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.PagedExecutionJobscheduler
        """
        return await self._request(
            "job_scheduler_v1_100.list_job_execution",
            "GET",
            "/jobExecution",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_job_execution_by_execution_id(self, execution_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Informações sobre a execução dos processos

        GET /jobExecution/{executionID}; operationId=getexecutionID; Protheus >= 12.1.23

        Retorna todos os agendamentos

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobExecutionType
        """
        return await self._request(
            "job_scheduler_v1_100.get_job_execution_by_execution_id",
            "GET",
            "/jobExecution/{executionID}",
            path_params={"executionID": execution_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_job_scheduler(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Busca execuções de processos

        GET /jobScheduler; operationId=getJobschedulerID; Protheus >= 12.1.23

        Retorna todos os agendamentos

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.PagedJobscheduler
        """
        return await self._request(
            "job_scheduler_v1_100.list_job_scheduler",
            "GET",
            "/jobScheduler",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_job_scheduler(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Cria agendamento de processo

        POST /jobScheduler; operationId=postJobschedulerID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        Request model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return await self._request(
            "job_scheduler_v1_100.create_job_scheduler",
            "POST",
            "/jobScheduler",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_job_scheduler_by_job_schedule_id(self, job_schedule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todos Jobscheduler

        GET /jobScheduler/{jobScheduleID}; operationId=getJobschedulerIDs; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return await self._request(
            "job_scheduler_v1_100.get_job_scheduler_by_job_schedule_id",
            "GET",
            "/jobScheduler/{jobScheduleID}",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_job_scheduler_by_job_schedule_id(self, job_schedule_id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui  Jobscheduler

        PUT /jobScheduler/{jobScheduleID}; operationId=postJobschedulerIDs; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        Request model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return await self._request(
            "job_scheduler_v1_100.update_job_scheduler_by_job_schedule_id",
            "PUT",
            "/jobScheduler/{jobScheduleID}",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_job_scheduler_by_job_schedule_id(self, job_schedule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui  Jobscheduler

        DELETE /jobScheduler/{jobScheduleID}; operationId=deleteJobschedulerID; Protheus >= 12.1.23

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return await self._request(
            "job_scheduler_v1_100.delete_job_scheduler_by_job_schedule_id",
            "DELETE",
            "/jobScheduler/{jobScheduleID}",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_job_scheduler_by_job_schedule_id_trigger(self, job_schedule_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Dispara a execução um agendamento de processo

        POST /jobScheduler/{jobScheduleID}/trigger; operationId=postJobschedulerIDtrigger; Protheus >= 12.1.23

        TOTVS note: disponivel com todos os parametros

        Response model: protheus.models.job_scheduler_v1_100.JobSchedulerType
        """
        return await self._request(
            "job_scheduler_v1_100.create_job_scheduler_by_job_schedule_id_trigger",
            "POST",
            "/jobScheduler/{jobScheduleID}/trigger",
            path_params={"jobScheduleID": job_schedule_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
