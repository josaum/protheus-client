"""Proposta Comercial — generated from CommercialProposal_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class EntityType(StrEnum):
    field_1 = "1"
    field_2 = "2"


class RegisterSituation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ListofProductsInfo(BaseModel):
    item_internal_id: str | None = Field(
        None,
        alias="ItemInternalId",
        description="Código interno dos Item da proposta comercial no ERP",
        examples=["D MG 01 00000101101"],
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01"], max_length=8
    )
    item_id: str | None = Field(None, alias="ItemId", description="Código do item", examples=["01"], max_length=2)
    product_id: str | None = Field(
        None, alias="ProductId", description="Código do Produto", examples=["000000000000001"], max_length=15
    )
    product_description: str | None = Field(
        None, alias="ProductDescription", description="Descrição do Produto", examples=["PRODUTO 01"], max_length=30
    )
    unit_of_measurement: str | None = Field(
        None, alias="UnitOfMeasurement", description="Unidade de Medida", examples=["PA"], max_length=2
    )
    currency: str | None = Field(None, alias="Currency", description="Moeda", examples=["1"], max_length=1)
    payment_mode_id: str | None = Field(
        None, alias="PaymentModeId", description="Código da Condição de pagamento", examples=["001"], max_length=3
    )
    type_out: str | None = Field(
        None, alias="TypeOut", description="Tipo de Entrada/Saída (TES)", examples=["001"], max_length=3
    )
    quantity: float | None = Field(
        None, alias="Quantity", description="Quantidade", examples=[1], ge=0.0, le=99999999.99
    )
    unit_price: float | None = Field(
        None, alias="UnitPrice", description="Preço unitário", examples=[1], ge=0.0, le=99999999999.99
    )
    unit_price_list: float | None = Field(
        None,
        alias="UnitPriceList",
        description="Preço unitário da Tabela de preço",
        examples=[1],
        ge=0.0,
        le=99999999999.99,
    )
    total_value: float | None = Field(
        None, alias="TotalValue", description="Valor Total", examples=[1], ge=0.0, le=99999999999.99
    )
    item_discount_percentage: float | None = Field(
        None,
        alias="ItemDiscountPercentage",
        description="Percentual de Desconto do Item",
        examples=[1],
        ge=0.0,
        le=99.99,
    )
    item_discount_value: float | None = Field(
        None,
        alias="ItemDiscountValue",
        description="Valor do Desconto do Item",
        examples=[0.01],
        ge=0.0,
        le=99999999999.99,
    )


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListofProducts(BaseModel):
    items: list[ListofProductsInfo] | None = None


class CommercialProposalInfo(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1"], max_length=3
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="Código interno da Proposta comercial no ERP", examples=["D MG 01 000001"]
    )
    company_internal_id: str | None = Field(
        None,
        alias="CompanyInternalId",
        description="Código interno da Proposta comercial composto pelo código da empresa",
        examples=["T1D MG 01 000001"],
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01"], max_length=8
    )
    proposal_number: str | None = Field(
        None, alias="ProposalNumber", description="Número da Proposta", examples=["000001"], max_length=6
    )
    proposal_review: str | None = Field(
        None, alias="ProposalReview", description="Revisão da Proposta", examples=["01"], max_length=2
    )
    opportunity_id: str | None = Field(
        None, alias="OpportunityId", description="Código da Oportunidade de Venda", examples=["000001"], max_length=6
    )
    opportunity_review: str | None = Field(
        None, alias="OpportunityReview", description="Revisão da Oportunidade", examples=["01"], max_length=2
    )
    opportunity_description: str | None = Field(
        None,
        alias="OpportunityDescription",
        description="Descrição da Oportunidade",
        examples=["Venda de Software"],
        max_length=30,
    )
    entity_type: EntityType | None = Field(
        None, alias="EntityType", description="Entidade da Proposta: 1 - Cliente;2 - Prospect", examples=["1"]
    )
    entity_code: str | None = Field(
        None, alias="EntityCode", description="Código da entidade", examples=["000001"], max_length=6
    )
    entity_unit: str | None = Field(
        None, alias="EntityUnit", description="Loja da entidade", examples=["01"], max_length=2
    )
    entity_description: str | None = Field(
        None, alias="EntityDescription", description="Descrição da Entidade", examples=["Cliente Padrão"], max_length=40
    )
    seller_id: str | None = Field(
        None, alias="SellerId", description="Código do Vendedor", examples=["000000"], max_length=6
    )
    register_date: AwareDatetime | None = Field(
        None, alias="RegisterDate", description="Data de Emissão", examples=["1900-01-01T12:00:00Z"]
    )
    price_list_id: str | None = Field(
        None, alias="PriceListId", description="Código da Tabela de Preço", examples=["001"], max_length=3
    )
    discount_percentage: float | None = Field(
        None, alias="DiscountPercentage", description="Percentual de Desconto", examples=[10.95], ge=0.0, le=99.99
    )
    synchronize_proposal: str | None = Field(
        None, alias="SynchronizeProposal", description="Sincronizar Proposta", examples=["T"], max_length=1
    )
    register_situation: RegisterSituation | None = Field(
        None, alias="RegisterSituation", description="Status do registro: 1 - Inativo;2 - Ativo", examples=["2"]
    )
    listof_products: list[Any] | ListofProducts | None = Field(None, alias="ListofProducts")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedListofProducts(Paging, ListofProducts):
    pass


class CommercialProposal(BaseModel):
    items: list[CommercialProposalInfo] | None = None


class PagedCommercialProposal(Paging, CommercialProposal):
    pass
