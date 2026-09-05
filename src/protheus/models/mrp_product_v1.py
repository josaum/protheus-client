"""Produto do MRP — generated from MRPProduct_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPProduct(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    product: str | None = Field(None, description="Código do produto", max_length=90)
    warehouse: str | None = Field(None, description="Armazém", max_length=2)
    type: str | None = Field(None, description="Tipo produto", max_length=2)
    group: str | None = Field(None, description="Grupo do produto", max_length=4)
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
    decimal_type: str | None = Field(None, alias="decimalType", description="Tipo de decimal", max_length=1)
    traceability: str | None = Field(None, description="Rastreabilidade", max_length=1)
    enter_mrp: str | None = Field(None, alias="enterMRP", description="Considera no MRP", max_length=1)
    current_bill_of_material_revision: (
        str | None
    ) = Field(None, alias="currentBillOfMaterialRevision", description="Revisão atual do produto", max_length=3)
    maximum_stock: float | None = Field(None, alias="maximumStock", description="Estoque máximo")
    process_by_product: str | None = Field(
        None, alias="processByProduct", description="Processamento do subproduto", max_length=1
    )
    by_product_lot: float | None = Field(None, alias="byProductLot", description="Lote do subproduto")
    by_product_bill_of_materials: (
        str | None
    ) = (
        Field(None, alias="byProductBillOfMaterials", description="Estrutura a ser utilizada pelo subproduto", max_length=90)
    )
    appropriation: str | None = Field(None, description="Indicador de apropriação do produto", max_length=1)
    fixed_horizon: float | None = Field(None, alias="fixedHorizon", description="Horizonte fixo")
    fixed_horizon_type: str | None = Field(
        None, alias="fixedHorizonType", description="Tipo do horizonte fixo", max_length=1
    )
    number_decimals: str | None = Field(None, alias="numberDecimals", description="Número de decimais", max_length=1)
    level: str | None = Field(None, description="Nível", max_length=2)
    potency: str | None = Field(None, description="Potência", max_length=1)
    blocked: str | None = Field(None, description="Bloqueado", max_length=1)
    purchase_contract: str | None = Field(
        None, alias="purchaseContract", description="Autorização de entrega", max_length=1
    )
    default_routing: str | None = Field(None, alias="defaultRouting", description="Roteiro padrão", max_length=2)
    cost_center_for_costing: str | None = Field(
        None, alias="costCenterForCosting", description="Centro Custo", max_length=9
    )
    code: str | None = Field(None, description="Id Produto")


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPProduct | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPProduct(BaseModel):
    items: list[MRPProduct] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPProduct(Paging, ListOfMRPProduct):
    pass


class MRPProductMultiple(PagedMRPProduct, ListOfMessages):
    pass
