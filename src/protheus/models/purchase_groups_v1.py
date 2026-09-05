"""Grupo de Compras — generated from PurchaseGroups_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class QuoteAnalyzes(StrEnum):
    s = "S"
    n = "N"


class ListOfUserListItem(BaseModel):
    item_sequence: str | None = Field(
        None,
        alias="ItemSequence",
        description="Numero sequencial dos compradores que fazem parte do Grupo.",
        examples=["01"],
    )
    user_code: dict[str, Any] | None = Field(
        None, alias="userCode", description="Código do usuário.", examples=["000001"]
    )
    user_name: dict[str, Any] | None = Field(
        None, alias="userName", description="Nome do usuário no Protheus.", examples=["Colaborador Fulano da Silva."]
    )
    quote_analyzes: QuoteAnalyzes | None = Field(
        None,
        alias="quoteAnalyzes",
        description="Se o Comprador pode analisar a cotação (S=SIM, N=NAO).",
        examples=["S=SIM, N=NAO"],
    )


class ListOfUserList(BaseModel):
    pass


class PurchaseGroupsInfo(BaseModel):
    company_internal_id: str | None = Field(
        None, alias="companyInternalId", description="InternalId da chave completa de empresa do produto."
    )
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId do (purchaseGroups) no ERP",
        examples=["D MG 01 0000001900010101"],
    )
    branch_id: str | None = Field(None, alias="branchId", description="ID Filial", examples=["M SP 01"], max_length=8)
    code: str | None = Field(
        None, description="Código do Grupo de Compras.", examples=["000001, AP-001, SP0001."], max_length=6
    )
    list_of_user_list: list[ListOfUserListItem] | ListOfUserList | None = Field(
        None, alias="ListOfUserList", description="Cadastra os usuários que fazem parte do Grupo de Compras."
    )


class PurchaseGroupListBuyer(BaseModel):
    item_sequence: str | None = Field(
        None,
        alias="ItemSequence",
        description="Numero sequencial dos compradores que fazem parte do Grupo.",
        examples=["01"],
    )
    user_code: dict[str, Any] | None = Field(
        None, alias="userCode", description="Código do usuário.", examples=["000001"]
    )
    user_name: dict[str, Any] | None = Field(
        None, alias="userName", description="Nome do usuário no Protheus.", examples=["Colaborador Fulano da Silva."]
    )
    quote_analyzes: QuoteAnalyzes | None = Field(
        None,
        alias="quoteAnalyzes",
        description="Se o Comprador pode analisar a cotação (S=SIM, N=NAO).",
        examples=["S=SIM, N=NAO"],
    )


class PurchaseGroupListBuyers(RootModel[list[PurchaseGroupListBuyer]]):
    root: list[PurchaseGroupListBuyer] = Field(
        ..., description="Cadastra os usuários que fazem parte do Grupo de Compras."
    )


class Code(RootModel[int]):
    root: int = Field(..., description="Código do Usuário")


class Name(RootModel[str]):
    root: str = Field(..., description="Nome")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PurchasesGroups(BaseModel):
    items: list[PurchaseGroupsInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedPurchasesGroups(Paging, PurchasesGroups):
    pass
