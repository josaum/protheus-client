"""Reservas de Produto — generated from ItemReserve_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ReserveType(StrEnum):
    vd = "VD"
    cl = "CL"
    pd = "PD"
    lb = "LB"
    nf = "NF"


class ReserveItemType(BaseModel):
    item_code: str | None = Field(None, alias="ItemCode", description="Código do Produto", examples=["0001"])
    warehouse_code: str | None = Field(
        None, alias="WarehouseCode", description="Código do Local de Estoque(Armazem)", examples=["01"]
    )
    quantity: float | None = Field(None, alias="Quantity", description="Quantidade do Item", examples=["1"])
    reserve_expiration: str | None = Field(
        None, alias="ReserveExpiration", description="Data de Vencimento da Reserva", examples=["2018-11-10"]
    )
    issue_date_reserve: str | None = Field(
        None, alias="IssueDateReserve", description="Data de Emissão da Reserva", examples=["2018-11-10"]
    )
    lot_number: str | None = Field(
        None, alias="LotNumber", description="NÃºmero do lote usado no Controle de Reservas", examples=["A001"]
    )
    sub_lot_number: str | None = Field(
        None, alias="SubLotNumber", description="Código do Lote associado ao produto.", examples=["B002"]
    )
    series_item: str | None = Field(
        None,
        alias="SeriesItem",
        description="Número de Série do produto, caso o produto faça o controle.",
        examples=["02010"],
    )
    addressing_item: str | None = Field(
        None,
        alias="AddressingItem",
        description="Endereço do produto reservado, utilizado nos casos que o estoque do produto tem endereços.",
        examples=["0102"],
    )
    note_reserve_item: str | None = Field(
        None, alias="NoteReserveItem", description="Observacao da Reserva", examples=["reserva do lote amarelo"]
    )
    reserve_branch: str | None = Field(
        None, alias="ReserveBranch", description="Filial onde será realizada a reserva do item.", examples=["D MG 02"]
    )
    is_canceled: bool | None = Field(
        None,
        alias="IsCanceled",
        description="Indica se o Item deverá ser excluído, apenas em casos de updade.",
        examples=["F"],
    )


class ItemReserveType(BaseModel):
    company_id: bool | None = Field(None, alias="CompanyId", description="Empresa - Não possui campo físico na tabela")
    branch_id: str | None = Field(
        None,
        alias="BranchId",
        description="Será enviado o valor da variável cFilAnt indicando em qual Filial Será feita a Reserva",
        examples=["D MG 01"],
    )
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="O InternalID da Reserva é formado por C0_FILIAL|C0_DOCRES",
        examples=["D MG 01|100"],
    )
    reserve_number: str | None = Field(
        None, alias="ReserveNumber", description="Numero da Reserva no Protheus", examples=["0001"]
    )
    reserve_type: ReserveType | None = Field(
        None,
        alias="ReserveType",
        description="Tipo de Reserva / VD - Venda Direta / CL - Cliente / PD - Pedido de Venda / LB - Liberacao / NF - Nota Fiscal",
        examples=["LJ"],
    )
    document_reserve: str | None = Field(
        None, alias="DocumentReserve", description="Número do documento que originou a reserva.", examples=["100"]
    )
    requester: str | None = Field(
        None, alias="Requester", description="Nome do usuário solicitante da reserva.", examples=["gemco"]
    )
    request_branch: str | None = Field(
        None, alias="RequestBranch", description="Filial Responsável pela Solicitação de Reserva", examples=["D MG 01"]
    )
    reserve_item_type: list[list[Any] | ReserveItemType] | None = Field(None, alias="ReserveItemType")


class ItemReserveItems(BaseModel):
    item_code: str | None = Field(None, alias="ItemCode", description="Código do Produto", examples=["0001"])
    warehouse_code: str | None = Field(
        None, alias="WarehouseCode", description="Código do Local de Estoque(Armazem)", examples=["01"]
    )
    quantity: float | None = Field(None, alias="Quantity", description="Quantidade do Item", examples=["1"])
    reserve_expiration: str | None = Field(
        None, alias="ReserveExpiration", description="Data de Vencimento da Reserva", examples=["2018-11-10"]
    )
    issue_date_reserve: str | None = Field(
        None, alias="IssueDateReserve", description="Data de Emissão da Reserva", examples=["2018-11-10"]
    )
    lot_number: str | None = Field(
        None, alias="LotNumber", description="NÃºmero do lote usado no Controle de Reservas", examples=["A001"]
    )
    sub_lot_number: str | None = Field(
        None, alias="SubLotNumber", description="Código do Lote associado ao produto.", examples=["B002"]
    )
    series_item: str | None = Field(
        None,
        alias="SeriesItem",
        description="Número de Série do produto, caso o produto faça o controle.",
        examples=["02010"],
    )
    addressing_item: str | None = Field(
        None,
        alias="AddressingItem",
        description="Endereço do produto reservado, utilizado nos casos que o estoque do produto tem endereços.",
        examples=["0102"],
    )
    note_reserve_item: str | None = Field(
        None, alias="NoteReserveItem", description="Observacao da Reserva", examples=["reserva do lote amarelo"]
    )
    reserve_branch: str | None = Field(
        None, alias="ReserveBranch", description="Filial onde será realizada a reserva do item.", examples=["D MG 02"]
    )
    is_canceled: bool | None = Field(
        None,
        alias="IsCanceled",
        description="Indica se o Item deverá ser excluído, apenas em casos de updade.",
        examples=["F"],
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


class PagedItemReserves(Paging):
    items: list[ItemReserveType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
