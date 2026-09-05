"""Centro de trabalho do MRP — generated from MRPWorkCenter_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class MRPWorkCenter(BaseModel):
    branch_id: str | None = Field(None, alias="branchId", description="Código da filial", max_length=2)
    workcenter: str | None = Field(None, description="Centro de Trabalho", max_length=6)
    warehouse: str | None = Field(None, description="Armazém", max_length=2)
    code: str | None = Field(None, description="Id Centro de trabalho")


class MessageBase(BaseModel):
    code: str | None = None
    message: str | None = None
    detailed_message: MRPWorkCenter | None = Field(None, alias="detailedMessage")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class ListOfMRPWorkCenter(BaseModel):
    items: list[MRPWorkCenter] | None = None


class ListOfMessages(BaseModel):
    field_messages: list[MessageBase] | None = Field(None, alias="_messages")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedMRPWorkCenter(Paging, ListOfMRPWorkCenter):
    pass


class MRPWorkCenterMultiple(PagedMRPWorkCenter, ListOfMessages):
    pass
