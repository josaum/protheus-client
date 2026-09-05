"""Políticas de Estoque por Grupo de Armazém do MRP — generated from MRPWareHouseInventoryPolicies_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPWareHouseInventoryPolicies(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Código do produto", max_length=90)
    warehouse_group: str | None = Field(None, alias="warehouseGroup", description="Grupo de Armazém", max_length=15)
    packing_quantity: float | None = Field(None, alias="packingQuantity", description="Quantidade por embalagem")
    order_point: float | None = Field(None, alias="orderPoint", description="Ponto de pedido")
    safety_stock: float | None = Field(None, alias="safetyStock", description="Estoque de segurança")
    delivery_lead_time: float | None = Field(None, alias="deliveryLeadTime", description="Prazo de entrega")
    type_delivery_lead_time: str | None = Field(
        None, alias="typeDeliveryLeadTime", description="Tipo do prazo de entrega", max_length=1
    )
    economic_lot_size: float | None = Field(None, alias="economicLotSize", description="Lote econômico")
    minimum_lot_size: float | None = Field(None, alias="minimumLotSize", description="Lote mínimo")
    tolerance: float | None = Field(None, description="Tolerância")
    maximum_stock: float | None = Field(None, alias="maximumStock", description="Estoque máximo")
    fixed_horizon: float | None = Field(None, alias="fixedHorizon", description="Horizonte fixo")
    fixed_horizon_type: str | None = Field(
        None, alias="fixedHorizonType", description="Tipo do horizonte fixo", max_length=1
    )
    code: str | None = Field(None, description="Id Produto")


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPWareHouseInventoryPolicies | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPWareHouseInventoryPolicies(BaseModel):
    items: list[MRPWareHouseInventoryPolicies] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPWareHouseInventoryPolicies(Paging, ListOfMRPWareHouseInventoryPolicies):
    pass


class MRPWareHouseInventoryPoliciesMultiple(PagedMRPWareHouseInventoryPolicies, ListOfMessages):
    pass
