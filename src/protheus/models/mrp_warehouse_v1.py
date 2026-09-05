"""Armazéns do MRP — generated from MRPWarehouse_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPWarehouseBase(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    code: str | None = Field(None, description="Id único do Armazém no MRP", max_length=200)
    warehouse: str | None = Field(None, description="Código do Armazém", max_length=2)
    type: str | None = Field(None, description="Tipo do armazém", max_length=1)
    use_mrp: str | None = Field(None, alias="useMrp", description="Usado no MRP", max_length=1)


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPWarehouseBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPWarehouse(BaseModel):
    items: list[MRPWarehouseBase] | None = None


class ListOfMessages(Paging):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPWarehouse(Paging, ListOfMRPWarehouse):
    pass


class MRPWarehouseMultiple(ListOfMRPWarehouse, ListOfMessages):
    pass
