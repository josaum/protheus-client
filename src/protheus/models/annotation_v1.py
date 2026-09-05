"""Apontamento de Visita — generated from Annotation_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListOfAnnotationCostItem(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId do item da Anotação no ERP",
        examples="D MG 01 000001190001010101",
    )
    item_sequence: str | None = Field(
        None, alias="ItemSequence", description="Numero sequencial do item do Apontamento", examples=["01"]
    )
    product_id: str | None = Field(
        None, alias="ProductId", description="Código do Produto", examples=["000000000000001"]
    )
    quantity: float | None = Field(
        None, alias="Quantity", description="Quantidade", examples=[1], ge=0.01, le=999999.99
    )
    unit_value: float | None = Field(
        None, alias="UnitValue", description="Valor Unitario do item", examples=[149.99], ge=0.01, le=999999999.99
    )
    total_value: float | None = Field(
        None, alias="TotalValue", description="Valor Total do item", examples=[149.99], ge=0.01, le=999999999.99
    )


class ListOfAnnotationCost(BaseModel):
    pass


class AnnotationInfo(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1"], max_length=3
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12
    )
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="Código da Empresa", examples=["T1D MG 01 0000001900010101"]
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da Anotação no ERP", examples=["D MG 01 0000001900010101"]
    )
    seller_id: str | None = Field(None, alias="SellerId", description="Codigo do Vendedor", examples=["000001"])
    register_date: AwareDatetime | None = Field(
        None, alias="RegisterDate", description="Data do Apontamento", examples=["1900-01-01T12:00:00Z"]
    )
    sequence: str | None = Field(None, alias="Sequence", description="Sequência do Contato", examples=["01"])
    customer_id: str | None = Field(None, alias="CustomerId", description="Código do Cliente", examples=["000001"])
    customer_unit: str | None = Field(None, alias="CustomerUnit", description="Loja do Cliente", examples=["01"])
    event_id: str | None = Field(None, alias="EventId", description="Codigo do Evento", examples=["000001"])
    opportunity_id: str | None = Field(
        None, alias="OpportunityID", description="Numero da Oportunidade", examples=["000001"]
    )
    prospect_id: str | None = Field(None, alias="ProspectId", description="Código do Prospect", examples=["000001"])
    prospect_unit: str | None = Field(None, alias="ProspectUnit", description="Loja do Prospect", examples=["01"])
    list_of_annotation_cost: list[ListOfAnnotationCostItem] | ListOfAnnotationCost | None = Field(
        None, alias="ListOfAnnotationCost", description="Descreve os Custos dos apontamentos"
    )


class AnnotationCostItem(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId do item da Anotação no ERP",
        examples="D MG 01 000001190001010101",
    )
    item_sequence: str | None = Field(
        None, alias="ItemSequence", description="Numero sequencial do item do Apontamento", examples=["01"]
    )
    product_id: str | None = Field(
        None, alias="ProductId", description="Código do Produto", examples=["000000000000001"]
    )
    quantity: float | None = Field(
        None, alias="Quantity", description="Quantidade", examples=[1], ge=0.01, le=999999.99
    )
    unit_value: float | None = Field(
        None, alias="UnitValue", description="Valor Unitario do item", examples=[149.99], ge=0.01, le=999999999.99
    )
    total_value: float | None = Field(
        None, alias="TotalValue", description="Valor Total do item", examples=[149.99], ge=0.01, le=999999999.99
    )


class AnnotationCost(RootModel[list[AnnotationCostItem]]):
    root: list[AnnotationCostItem] = Field(..., description="Descreve os Custos dos apontamentos")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Annotations(BaseModel):
    items: list[AnnotationInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedAnnotation(Paging, Annotations):
    pass
