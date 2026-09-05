"""Segmentos de Mercado — generated from MarketSegment_v2_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MarketSegments1(BaseModel):
    pass


class Childs(BaseModel):
    child_market_segment_id: str | None = Field(None, alias="childMarketSegmentId", description="ID do segmento filho")
    child_market_segmant_description: (
        str | None
    ) = Field(None, alias="childMarketSegmantDescription", description="Descrição do segmento filho")


class MarketSegmentsInfo(BaseModel):
    market_segment_id: str | None = Field(
        None, alias="marketSegmentID", description="Código do Segmento", examples=["000001"]
    )
    branch_id: str | None = Field(None, alias="branchId", description="Filial", examples=["D MG 01"])
    company_id: str | None = Field(None, alias="companyId", description="Empresa")
    market_segment_description: (
        str | None
    ) = Field(None, alias="marketSegmentDescription", description="Descrição do Segmento", examples=["Services"])
    main_market_segment: bool | None = Field(
        None, alias="mainMarketSegment", description="Indica se é um segmento principal", examples=[True]
    )
    parent_market_segment: str | None = Field(
        None, alias="parentMarketSegment", description="Segmento pai/superior", examples=["000002"]
    )
    parent_market_segment_description: (
        str | None
    ) = (
        Field(None, alias="parentMarketSegmentDescription", description="Descrição do Segmento pai/superior", examples=["AGROPECUARIA"])
    )
    childs: Childs | None = Field(None, description="Lista de Segmentos filhos")
    is_active: bool | None = Field(
        None, alias="IsActive", description="Indica se o Segmento está ativo.", examples=[True]
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


class MarketSegments(RootModel[list[list[MarketSegmentsInfo]] | MarketSegments1]):
    root: list[list[MarketSegmentsInfo]] | MarketSegments1


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMarketSegments(Paging):
    pass
