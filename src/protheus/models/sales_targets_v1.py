"""Metas de Vendas — generated from SalesTargets_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class BlockedRecord(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ListOfSalesTarget(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId do item da metas de venda no ERP",
        examples="D MG 01 000000001/001",
    )
    sales_target_item: str | None = Field(
        None, alias="SalesTargetItem", description="Item da meta de venda.", examples=["001"], max_length=3
    )
    billing_date: str | None = Field(
        None,
        alias="BillingDate",
        description="Data de apuração da Meta de Venda.",
        examples=["11/11/2018"],
        max_length=8,
    )
    seller_code: str | None = Field(
        None, alias="SellerCode", description="Código do vendedor na meta de venda.", examples=["000001"], max_length=6
    )
    region_code: str | None = Field(
        None, alias="RegionCode", description="Código da região da Meta de Venda.", examples=["001"], max_length=3
    )
    category_code: str | None = Field(
        None, alias="CategoryCode", description="Código da categotia do produto.", examples=["000001"], max_length=6
    )
    product_type: str | None = Field(
        None, alias="ProductType", description="Código do tipo do produto.", examples=["PA"], max_length=2
    )
    product_group: str | None = Field(
        None, alias="ProductGroup", description="Código do grupo do produto.", examples=["0003"], max_length=4
    )
    quatity: float | None = Field(
        None,
        alias="Quatity",
        description="Quantidade a ser considerada para a metas de venda.",
        examples=["10.00"],
        ge=0.0,
        le=999999999999.99,
    )
    price: float | None = Field(
        None, alias="Price", description="Valor da Meta de Venda.", examples=["6000.00"], ge=0.0, le=99999999999999.98
    )
    currency: float | None = Field(
        None, alias="Currency", description="Código da moeda.", examples=["1"], ge=1.0, le=9.0
    )
    blocked_record: BlockedRecord | None = Field(
        None,
        alias="BlockedRecord",
        description="Informa se o registro está habilitado(ativo) para uso na aplicação.",
        examples=["2"],
    )


class ListOfSalesTargets(BaseModel):
    pass


class SalesTargetsInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa", max_length=3)
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da metas de venda no ERP", examples="D MG 01 000001"
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01"], max_length=8
    )
    company_internal_id: str | None = Field(None, alias="CompanyInternalId", description="Código da Empresa")
    code: str | None = Field(
        None, alias="Code", description="Código da metas de venda.", examples=["000000003"], max_length=6
    )
    sales_target_description: str | None = Field(
        None,
        alias="SalesTargetDescription",
        description="Descrição da metas de venda.",
        examples=["Meta de venda região norte"],
        max_length=40,
    )
    list_of_sales_targets: list[ListOfSalesTarget] | ListOfSalesTargets | None = Field(
        None, alias="ListOfSalesTargets", description="Descreve a lista de metas de vendas"
    )


class ListSalesTarget(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId do item da metas de venda no ERP",
        examples="D MG 01 000000001/001",
    )
    sales_target_item: str | None = Field(
        None, alias="SalesTargetItem", description="Item da meta de venda.", examples=["001"], max_length=3
    )
    billing_date: str | None = Field(
        None,
        alias="BillingDate",
        description="Data de apuração da Meta de Venda.",
        examples=["11/11/2018"],
        max_length=8,
    )
    seller_code: str | None = Field(
        None, alias="SellerCode", description="Código do vendedor na meta de venda.", examples=["000001"], max_length=6
    )
    region_code: str | None = Field(
        None, alias="RegionCode", description="Código da região da Meta de Venda.", examples=["001"], max_length=3
    )
    category_code: str | None = Field(
        None, alias="CategoryCode", description="Código da categotia do produto.", examples=["000001"], max_length=6
    )
    product_type: str | None = Field(
        None, alias="ProductType", description="Código do tipo do produto.", examples=["PA"], max_length=2
    )
    product_group: str | None = Field(
        None, alias="ProductGroup", description="Código do grupo do produto.", examples=["0003"], max_length=4
    )
    quatity: float | None = Field(
        None,
        alias="Quatity",
        description="Quantidade a ser considerada para a metas de venda.",
        examples=["10.00"],
        ge=0.0,
        le=999999999999.99,
    )
    price: float | None = Field(
        None, alias="Price", description="Valor da Meta de Venda.", examples=["6000.00"], ge=0.0, le=99999999999999.98
    )
    currency: float | None = Field(
        None, alias="Currency", description="Código da moeda.", examples=["1"], ge=1.0, le=9.0
    )
    blocked_record: BlockedRecord | None = Field(
        None,
        alias="BlockedRecord",
        description="Informa se o registro está habilitado(ativo) para uso na aplicação.",
        examples=["2"],
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


class ItensSalesTargets(BaseModel):
    items: list[list[ListSalesTarget]] | None = None


class SalesTargets(BaseModel):
    items: list[SalesTargetsInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedItensSalesTargets(Paging, ItensSalesTargets):
    pass


class PagedSalesTargets(Paging, SalesTargets):
    pass
