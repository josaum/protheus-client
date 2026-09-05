"""Total de Nota de Entrada — generated from TotalInputDocument_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class TotalInputDocument(BaseModel):
    quantity: float | None = Field(
        None, alias="Quantity", description="quantidade de notas de entrada com sucesso ", ge=-9999.99, le=9999.99
    )
    amount: float | None = Field(None, alias="Amount", description="valor total de notas de entrada com sucesso ")
    from_date: Any | None = Field(None, alias="FromDate", description="Data inicio de emissão")
    to_date: Any | None = Field(None, alias="ToDate", description="Data até de emissão")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
