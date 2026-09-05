"""Roteiro Produtivo do MRP — generated from MRPRouting_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPOperationList(BaseModel):
    operation: str | None = Field(None, description="Operação", max_length=2)
    workcenter: str | None = Field(None, description="Centro de trabalho", max_length=6)


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class MRPRouting(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Produto", max_length=90)
    routing: str | None = Field(None, description="Roteiro", max_length=2)
    code: str | None = Field(None, description="Id Roteiro")
    list_of_mrp_routing: list[MRPOperationList] | None = Field(
        None, alias="ListOfMRPRouting", description="Operações do roteiro"
    )


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPRouting | None = Field(None, alias="detailedMessage")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class ListOfMRPRouting(BaseModel):
    items: list[MRPRouting] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class PagedMRPRouting(Paging, ListOfMRPRouting):
    pass


class MRPRoutingMultiple(PagedMRPRouting, ListOfMessages):
    pass
