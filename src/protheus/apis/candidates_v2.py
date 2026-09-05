"""Candidato — generated from Candidates_v2_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class CandidatesV2(ApiGroup):
    """Candidato (/api/rh/v2)."""

    api_id = "candidates_v2"
    base_path = "/api/rh/v2"

    def get_candidates_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna dados de tabela do Candidato especificado

        GET /candidates/{id}; operationId=getCandidatesId; Protheus >= 12.1.25

        Retorna dados de tabela da Candidato especificada

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateInfo
        """
        return self._request(
            "candidates_v2.get_candidates_by_id",
            "GET",
            "/candidates/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_candidates_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um registro existente de tabela de Candidatos

        PUT /candidates/{id}; operationId=putCandidatesId; Protheus >= 12.1.25

        Atualiza um registro existente de tabela de Candidatos. Caso não seja informado alguma propriedade para ser atualizada, está será considerada nula.

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateInfo
        Request model: protheus.models.candidates_v2.CandidateSave
        """
        return self._request(
            "candidates_v2.update_candidates_by_id",
            "PUT",
            "/candidates/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_candidates_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui Candidato

        DELETE /candidates/{id}; operationId=DeleteCandidatesId; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponivel com todos parametros
        """
        return self._request(
            "candidates_v2.delete_candidates_by_id",
            "DELETE",
            "/candidates/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_candidates(self, *, persons_ids: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as Candidatos

        GET /candidates; operationId=getCandidates; Protheus >= 12.1.25

        Retorna todos as Candidatos

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateGroups
        """
        return self._request(
            "candidates_v2.list_candidates",
            "GET",
            "/candidates",
            path_params={},
            query={"personsIds": persons_ids, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_candidates(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um novo registro na tabela de Candidatos

        POST /candidates; operationId=postCandidates; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateInfo
        Request model: protheus.models.candidates_v2.CandidateSave
        """
        return self._request(
            "candidates_v2.create_candidates",
            "POST",
            "/candidates",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

class AsyncCandidatesV2(AsyncApiGroup):
    """Candidato (/api/rh/v2)."""

    api_id = "candidates_v2"
    base_path = "/api/rh/v2"

    async def get_candidates_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna dados de tabela do Candidato especificado

        GET /candidates/{id}; operationId=getCandidatesId; Protheus >= 12.1.25

        Retorna dados de tabela da Candidato especificada

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateInfo
        """
        return await self._request(
            "candidates_v2.get_candidates_by_id",
            "GET",
            "/candidates/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_candidates_by_id(self, id: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza um registro existente de tabela de Candidatos

        PUT /candidates/{id}; operationId=putCandidatesId; Protheus >= 12.1.25

        Atualiza um registro existente de tabela de Candidatos. Caso não seja informado alguma propriedade para ser atualizada, está será considerada nula.

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateInfo
        Request model: protheus.models.candidates_v2.CandidateSave
        """
        return await self._request(
            "candidates_v2.update_candidates_by_id",
            "PUT",
            "/candidates/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_candidates_by_id(self, id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui Candidato

        DELETE /candidates/{id}; operationId=DeleteCandidatesId; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponivel com todos parametros
        """
        return await self._request(
            "candidates_v2.delete_candidates_by_id",
            "DELETE",
            "/candidates/{id}",
            path_params={"id": id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_candidates(self, *, persons_ids: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna todas as Candidatos

        GET /candidates; operationId=getCandidates; Protheus >= 12.1.25

        Retorna todos as Candidatos

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateGroups
        """
        return await self._request(
            "candidates_v2.list_candidates",
            "GET",
            "/candidates",
            path_params={},
            query={"personsIds": persons_ids, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_candidates(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um novo registro na tabela de Candidatos

        POST /candidates; operationId=postCandidates; Protheus >= 12.1.25

        TOTVS note: Este verbo esta disponivel com todos parametros

        Response model: protheus.models.candidates_v2.CandidateInfo
        Request model: protheus.models.candidates_v2.CandidateSave
        """
        return await self._request(
            "candidates_v2.create_candidates",
            "POST",
            "/candidates",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )
