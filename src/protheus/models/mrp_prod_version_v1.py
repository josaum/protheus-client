"""Versão da Produção MRP — generated from MrpProdVersion_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPProdVersionBase(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    code: str | None = Field(None, description="Código da versão da produção", max_length=200)
    product: str | None = Field(None, description="Código do Produto da versão da produção", max_length=90)
    start_date: date | None = Field(None, alias="startDate", description="Data Inicial")
    end_date: date | None = Field(None, alias="endDate", description="Data Final")
    start_quantity: float | None = Field(None, alias="startQuantity", description="Quantidade Inicial")
    end_quantity: float | None = Field(None, alias="endQuantity", description="Quantidade Final")
    revision: str | None = Field(None, description="Revisão da versão da produção", max_length=3)
    routing: str | None = Field(None, description="Roteiro produtivo da versão da produção", max_length=2)
    warehouse: str | None = Field(None, description="Armazém de consumo", max_length=10)


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPProdVersionBase | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPProdVersion(Paging):
    items: list[MRPProdVersionBase] | None = None


class ListOfMessages(Paging):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPProdVersion(ListOfMRPProdVersion, Paging):
    pass


class MRPProdVersionMultiple(ListOfMRPProdVersion, ListOfMessages):
    pass
