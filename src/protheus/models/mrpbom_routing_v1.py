"""Estrutura por Operação do MRP — generated from MRPBOMRouting_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPBOMRouting(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Produto pai", max_length=90)
    routing: str | None = Field(None, description="Roteiro", max_length=2)
    operation: str | None = Field(None, description="Operação", max_length=2)
    component: str | None = Field(None, description="Componente", max_length=90)
    sequence: str | None = Field(None, description="Sequencia do componente", max_length=10)
    code: str | None = Field(None, description="Id estrutura por operação")


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPBOMRouting | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPBOMRouting(BaseModel):
    items: list[MRPBOMRouting] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPBOMRouting(Paging, ListOfMRPBOMRouting):
    pass


class MRPBOMRoutingMultiple(PagedMRPBOMRouting, ListOfMessages):
    pass
