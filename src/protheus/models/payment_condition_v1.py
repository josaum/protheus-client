"""Condição de Pagamento — generated from PaymentCondition_v1_00.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class WeekDayFixed(Enum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_6 = "6"
    field_7 = "7"


class DaysCondition(Enum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_6 = "6"


class DueType(BaseModel):
    plot_number: int | None = Field(None, alias="PlotNumber", description="Número sequencial da parcela.", examples=[1])
    base_date: str | None = Field(
        None,
        alias="BaseDate",
        description="Data Base ocorre pela entrada ou emissão do documento.",
        examples=["E"],
        max_length=1,
    )
    due_day: int | None = Field(
        None,
        alias="DueDay",
        description="Quantidade de dias para o vencimento da parcela.",
        examples=[1],
        ge=0,
        le=9999,
    )
    percentage: float | None = Field(
        None,
        alias="Percentage",
        description="Indica se o valor da parcela deverá ser um percentual do total.",
        examples=[999.99],
        ge=-999.99,
        le=999.99,
    )
    down_payment_percentage: float | None = Field(
        None,
        alias="DownPaymentPercentage",
        description="Percentual para baixa de adiantamento.",
        examples=[50],
        ge=0.0,
        le=999.99,
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


class Plots(BaseModel):
    due: list[DueType] | None = Field(None, alias="Due")


class PaymentConditionInfo(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1 "], max_length=3
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12
    )
    company_internal_id: str | None = Field(
        None, alias="CompanyInternalId", description="Código da Empresa", examples=["T1D MG 01 001"]
    )
    code: str | None = Field(
        None, alias="Code", description="Código da Condição de Pagamento.", examples=["001"], max_length=3
    )
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId da Condição de pagamento no ERP")
    description: str | None = Field(
        None, alias="Description", description="Descrição da Condição de Pagamento", examples=["A VISTA"], max_length=50
    )
    mean_time: int | None = Field(None, alias="MeanTime", description="Número Médio de Dias", examples=[1], ge=0, le=99)
    days_first_due: int | None = Field(
        None,
        alias="DaysFirstDue",
        description="Quantidade de dias para o vencimento da primeira parcela (0 a 99)",
        examples=[1],
        ge=0,
        le=99,
    )
    quantity_plots: int | None = Field(
        None, alias="QuantityPlots", description="Quantidade de parcelas (1 a 99).", examples=[1], ge=1, le=99
    )
    range_plots: int | None = Field(
        None,
        alias="RangePlots",
        description="Intervalo entre cada parcela, em dias (0 a 999).",
        examples=[1],
        ge=0,
        le=999,
    )
    week_day_fixed: WeekDayFixed | None = Field(
        None,
        alias="WeekDayFixed",
        description="Define um dia da semana fixo para o vencimento das parcelas. 1 - Domingo 2 - Segunda 3 - Terça 4 - Quarta 5 - Quinta 6 - Sexta 7 - Sábado.",
        examples=[1],
    )
    day_month_fixed: int | None = Field(
        None,
        alias="DayMonthFixed",
        description="Define um dia do mês fixo para o vencimento das parcelas (1 a 31).",
        examples=[1],
        ge=1,
        le=31,
    )
    days_condition: DaysCondition | None = Field(
        None,
        alias="DaysCondition",
        description="Define como será a contagem dos dias do intervalo de cada parcela. 1 - Data do Dia 2 - Fora o Dia 3 - Fora Semana 4 - Fora Quinzena 5 - Fora mês 6 - Fora Dezena.",
        examples=[1],
    )
    financial_discount_days: int | None = Field(
        None,
        alias="FinancialDiscountDays",
        description="Quantidade de dias para o desconto financeiro (1 a 99).",
        examples=[1],
        ge=1,
        le=99,
    )
    percentage_discount_days: float | None = Field(
        None,
        alias="PercentageDiscountDays",
        description="Percentual do desconto financeiro para a Condição",
        examples=[1],
        ge=-99.99,
        le=99.99,
    )
    percentage_increase: Any | None = Field(
        None,
        alias="PercentageIncrease",
        description="Percentual do acréscimo financeiro para a Condição.",
        examples=[1],
        ge=-999.99,
        le=999.99,
    )
    days_count_way: int | None = Field(
        None, alias="DaysCountWay", description="Forma de contagem dos dias de vencimento.", examples=[1]
    )
    payment_situation: int | None = Field(
        None, alias="PaymentSituation", description="Situação de Pagamento.", examples=[2]
    )
    start_counting: Any | None = Field(
        None, alias="StartCounting", description="Início da contagem dos dias das parcelas.", examples=["N"]
    )
    plots: Plots | None = Field(
        None,
        alias="Plots",
        description="Define as parcelas da Condição de pagamento quando o intervalo não for regular ou o valor das parcelas não for dividido de forma igual.",
    )


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PaymentConditions(BaseModel):
    items: list[PaymentConditionInfo] | None = None


class PagedPaymentCondition(Paging, PaymentConditions):
    pass
