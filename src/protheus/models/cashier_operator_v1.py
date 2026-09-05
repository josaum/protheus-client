"""Operador de Caixa — generated from CashierOperator_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CashierOperatorType(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa.")
    branch_id: str | None = Field(None, alias="BranchId", description="ID Filial")
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="InternalId da chave completa de empresa do produto"
    )
    cashier_code: str | None = Field(None, alias="CashierCode", description="Codigo do caixa\\operador", max_length=30)
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do caixa\\operador")
    name: str | None = Field(None, alias="Name", description="Nome do(a) operador(a) de Caixa", max_length=40)
    short_name: str | None = Field(
        None, alias="ShortName", description="Nome do(a) operador(a) de Caixa", max_length=20
    )
    withdrawal_limit: float | None = Field(
        None,
        alias="WithdrawalLimit",
        description="Valor limite para o caixa sangrar",
        ge=-9999999999.99,
        le=9999999999.99,
        multiple_of=0.01,
    )
    discount_total_percent: float | None = Field(
        None,
        alias="DiscountTotalPercent",
        description="Percentual permitido para o operador conceder desconto no total da venda",
        ge=-999.99,
        le=999.99,
        multiple_of=0.01,
    )
    discount_total_value: float | None = Field(
        None,
        alias="DiscountTotalValue",
        description="Valor permitido para o operador conceder desconto no tatal da venda",
        ge=-999.99,
        le=999.99,
        multiple_of=0.01,
    )
    discount_item_percent: float | None = Field(
        None,
        alias="DiscountItemPercent",
        description="Percentual permitido para o operador conceder desconto no item da venda",
        ge=-999.99,
        le=999.99,
        multiple_of=0.01,
    )
    discount_item_value: float | None = Field(
        None,
        alias="DiscountItemValue",
        description="Valor permitido para o operador conceder desconto no item da venda",
        ge=-999.99,
        le=999.99,
        multiple_of=0.01,
    )
    card_number: str | None = Field(
        None,
        alias="CardNumber",
        description="Numero do cartao do operador, utilizado para acesso do operador",
        max_length=5,
    )
    can_withdrawal: str | None = Field(
        None, alias="CanWithdrawal", description="Tem permissao para fazer sangria 1-SIM 2-NÃO 3-Solicita Superior"
    )
    can_cancel_item: str | None = Field(
        None, alias="CanCancelItem", description="Tem permissao para cancelar um item 1-SIM 2-NÃO 3-Solicita Superior"
    )
    can_cancel_sale: str | None = Field(
        None, alias="CanCancelSale", description="Tem permissao para cancelar a venda 1-SIM 2-NÃO 3-Solicita Superior"
    )
    can_edit_payment: str | None = Field(
        None,
        alias="CanEditPayment",
        description="Tem permissao para alterar pagamentos 1-SIM 2-NÃO 3-Solicita Superior",
    )
    can_open_drawer: str | None = Field(
        None, alias="CanOpenDrawer", description="Tem permissao para abrir gaveta 1-SIM 2-NÃO 3-Solicita Superior"
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


class PagedCashierOperators(Paging):
    items: list[CashierOperatorType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
