"""Malha de Distribuição do MRP — generated from MRPTransportingLanes_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPLaneException(BaseModel):
    product: str | None = Field(None, description="Código do produto", max_length=90)
    start_date: date | None = Field(None, alias="startDate", description="Data início")
    end_date: date | None = Field(None, alias="endDate", description="Data final")
    start_quantity: float | None = Field(None, alias="startQuantity", description="Quantidade Inicial")
    end_quantity: float | None = Field(None, alias="endQuantity", description="Quantidade Final")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class MRPTransportingLanes(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    start_warehouse_group: str | None = Field(
        None, alias="startWarehouseGroup", description="Grupo origem", max_length=15
    )
    branch_id_dest: str | None = Field(None, alias="branchIdDest", description="Filial destino", max_length=2)
    end_warehouse_group: str | None = Field(None, alias="endWarehouseGroup", description="Grupo destino", max_length=15)
    code: str | None = Field(None, description="Id Malha")
    list_of_mrp_lane_exception: list[MRPLaneException] | None = Field(
        None, alias="listOfMRPLaneException", description="Exceções da Malha de distribuição"
    )


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPTransportingLanes | None = Field(None, alias="detailedMessage")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class ListOfMRPTransportingLanes(BaseModel):
    items: list[MRPTransportingLanes] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class PagedMRPTransportingLanes(Paging, ListOfMRPTransportingLanes):
    pass


class MRPTransportingLanesMultiple(PagedMRPTransportingLanes, ListOfMessages):
    pass
