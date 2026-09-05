"""Token — generated from Token_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Scope(StrEnum):
    default = "default"


class TokenType(StrEnum):
    bearer = "Bearer"


class BusinessContentType(BaseModel):
    access_token: str | None = Field(None, description="Token para acesso a aplicação")
    refresh_token: str | None = Field(
        None, description="Refresh Token para requisição de um novo token para caso de expiração."
    )
    scope: Scope | None = Field(None, description="Escopo do token")
    token_type: TokenType | None = Field(None, description="Tipo do token")
    expires_in: int | None = Field(None, description="Tempo de expiração do token em segundos")


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
