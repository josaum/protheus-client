"""Consulta os erros da integração TSI — generated from TSIIntegrationErrors_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListErrors(BaseModel):
    branch_code: str = Field(..., alias="branchCode", description="Codigo da Filial", examples=["D MG 01"])
    layout_error: str = Field(..., alias="layoutError", description="Layout do erro", examples=["C20 - Notas fiscais"])
    integration_date: Any = Field(
        ..., alias="integrationDate", description="Data da Integração", examples=["2022-05-25"]
    )
    integration_time: str = Field(..., alias="integrationTime", description="Hora de integração", examples=["15:50:45"])
    erpkey: str = Field(
        ...,
        description="Chave da Nota",
        examples=[" Nota Fiscal = 'S00013544' | Série = '102' | Cod. Participante = 'Inválido' | Data = '09/09/2021' "],
    )
    regkey: str = Field(..., description="Código do registro", examples=["PROD000000001"])
    error_message: str = Field(
        ...,
        alias="errorMessage",
        description="Mensagem de erro",
        examples=["Não foi encontrado o conteúdo 'CCT100101' informado no sistema de origem correspondente ao campo 'Id.Participante'( C20_CODPAR ) do TAF."],
    )


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class PagedItens(Paging):
    items: list[ListErrors] | None = None
