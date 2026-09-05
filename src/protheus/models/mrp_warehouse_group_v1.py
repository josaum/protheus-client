"""Grupo de Armazém do MRP — generated from MRPWarehouseGroup_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPWarehouseList(BaseModel):
    warehouse: str | None = Field(None, description="Armazém", max_length=2)
    warehouse_default: str | None = Field(None, alias="warehouseDefault", description="Armazém default", max_length=1)
    code: str | None = Field(None, description="Id Grupo armazém")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class MRPWarehouseGroup(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    warehouse_group: str | None = Field(None, alias="warehouseGroup", description="Grupo de armazém", max_length=15)
    type_group: str | None = Field(None, alias="typeGroup", description="Tipo do grupo de armazém", max_length=1)
    list_of_mrp_warehouse: list[MRPWarehouseList] | None = Field(
        None, alias="listOfMRPWarehouse", description="Armazéns do grupo"
    )


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPWarehouseGroup | None = Field(None, alias="detailedMessage")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class ListOfMRPWarehouseGroup(BaseModel):
    items: list[MRPWarehouseGroup] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class PagedMRPWarehouseGroup(Paging, ListOfMRPWarehouseGroup):
    pass


class MRPWarehouseGroupMultiple(PagedMRPWarehouseGroup, ListOfMessages):
    pass
