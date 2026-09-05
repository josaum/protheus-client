"""Folha de pagamento para linha de produtos totvs - Global — generated from PayrollControl_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class PayrollControlItem(BaseModel):
    company_key: str | None = Field(
        None, alias="companyKey", description="Agrupamento de Empresa, Unidade de negócio e Filial"
    )
    branch: str | None = Field(None, description="Filial do Funcionario")
    id: str | None = Field(None, description="Chave unica para localização do registro")
    code: str | None = Field(None, description="Matricula do Funcionario")
    internal_id_code: str | None = Field(None, alias="internalIdCode", description="InternalId do funcionário")
    moviment_date: AwareDatetime | None = Field(None, alias="movimentDate", description="Data da Movimentação")
    original_record: str | None = Field(None, alias="originalRecord", description="Registro Original")
    provider_code: str | None = Field(None, alias="providerCode", description="Codigo do provedor")
    provider_type: str | None = Field(None, alias="providerType", description="Tipo do provedor")
    contract_code: str | None = Field(None, alias="contractCode", description="Codigo do Contrato")
    product_code: str | None = Field(None, alias="productCode", description="Código do produto")
    payroll_identifier: str | None = Field(
        None, alias="payrollIdentifier", description="Identificador do cálculo da folha de pagamento"
    )
    payment_amount: int | None = Field(None, alias="paymentAmount", description="Valor do pagamento")
    payment_date: AwareDatetime | None = Field(None, alias="paymentDate", description="Data de pagamento")
    payment_period: str | None = Field(None, alias="paymentPeriod", description="Competencia de pagamento")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedPayrollControl(Paging):
    total: int | None = Field(None, examples=["1"])
    payments: list[PayrollControlItem] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
