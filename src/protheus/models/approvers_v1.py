"""Aprovadores — generated from Approvers_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class UserCode(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")


class UserName(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")


class HigherApprover(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")


class TypeLimitApprove(StrEnum):
    d = "D"
    s = "S"
    m = "M"


class UserLogin(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")


class ConversionDatePendingValue(StrEnum):
    field_1 = "1"
    field_2 = "2"


class LotationDestiny(StrEnum):
    field_1 = "1"
    field_2 = "2"


class ApproversInfo(BaseModel):
    company_internal_id: str | None = Field(
        None, alias="companyInternalId", description="InternalId da chave completa de empresa do produto."
    )
    branch_id: str | None = Field(None, alias="branchId", description="ID Filial", examples=["M SP 01"], max_length=8)
    code: str | None = Field(
        None, description="Código do Aprovador.", examples=["000001, AP-001, SP0001."], max_length=6
    )
    user_code: UserCode | None = Field(None, alias="userCode", description="Código do usuário.", examples=["000001"])
    user_name: UserName | None = Field(
        None, alias="userName", description="Nome do usuário no Protheus.", examples=["Colaborador Fulano da Silva."]
    )
    higher_approver: HigherApprover | None = Field(
        None, alias="higherApprover", description="Armazena o ID do usuário no Protheus.", examples=["000001, THF-01."]
    )
    approve_value_limit_min: float | None = Field(
        None,
        alias="approveValueLimitMin",
        description="Valor Minimo do Limite de Aprovação do Aprovador.",
        examples=["0.00"],
        max_length=14,
    )
    approve_value_limit_max: float | None = Field(
        None,
        alias="approveValueLimitMax",
        description="Valor Máximo do Limite de Aprovação do Aprovador.",
        examples=["0.00"],
        max_length=14,
    )
    currency_approve: float | None = Field(
        None,
        alias="currencyApprove",
        description="Identifica qual Tipo de Moeda (US$, R$, €) o Aprovador ira trabalhar no sistema.",
        examples=["1,2,3,4 ou 5."],
        max_length=5,
    )
    approve_limit_approver: float | None = Field(
        None, alias="approveLimitApprover", description="Limite do Aprovador", examples=["0.00"], max_length=14
    )
    type_limit_approve: TypeLimitApprove | None = Field(
        None,
        alias="typeLimitApprove",
        description="Tipo de limite que sera atribuido D-Diario/S-Semanal/M-Mensal. O Padrão é D-Diario.",
        examples=["D - Diario, S - Semanal, M - Mensal."],
    )
    limited_order: float | None = Field(None, alias="limitedOrder", description="", examples=[""], max_length=13)
    user_login: UserLogin | None = Field(
        None,
        alias="userLogin",
        description="Armazena login do usuário no Protheus.",
        examples=["aprovadora, aprovadorb"],
    )
    company: str | None = Field(
        None,
        alias="Company",
        description="Estabelecimento que o Aprovador está relacionado.",
        examples=[""],
        max_length=5,
    )
    lotation: str | None = Field(
        None, description="Código da lotação pertencente ao usuário.", examples=[""], max_length=20
    )
    view_pending_value: bool | None = Field(
        None, alias="viewPendingValue", description="Visualiza Valor da Pendência na Moeda do Aprovador?"
    )
    conversion_date_pending_value: (
        ConversionDatePendingValue | None
    ) = (
        Field(None, alias="conversionDatePendingValue", description="Data que deve ser utilizada para converter o valor da pendência para a moeda do Aprovador: 1 = Data Aprovação; 2 = Data da Geração da Pendência")
    )
    lotation_destiny: LotationDestiny | None = Field(
        None,
        alias="lotationDestiny",
        description="Valor a ser utilizado na geração da pendência para aprovações do tipo hierarquia e/ou faixa: 1 = Lotação; 2 = Centro de Custo",
        examples=[""],
    )
    master_approver: bool | None = Field(
        None,
        alias="masterApprover",
        description="Determina que o aprovador não tenha restrições de limite ou lotação quando for aprovar uma determinada pendência",
    )
    send_email: bool | None = Field(
        None, alias="sendEmail", description="Determina o envio ou não de e-mail's.", examples=[""]
    )
    receive_email: bool | None = Field(
        None, alias="receiveEmail", description="Determina o recebimento ou não de e-mail's."
    )
    receive_html_email: bool | None = Field(
        None, alias="receiveHTMLEmail", description="Determina o recebimento ou não de e-mail's no formato HTML."
    )
    automatic_approval: bool | None = Field(
        None,
        alias="automaticApproval",
        description="Determina que o documento digitado pelo próprio aprovador, desde que dentro do seu limite de aprovação, seja aprovado automaticamente.",
        examples=[""],
    )
    email: str | None = Field(None, description="Endereço de e-mail do Aprovador.", examples=[""], max_length=80)


class GovernmentalInformationType(BaseModel):
    id: list[str] | None = Field(None, alias="Id", description="Identificação.")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Approve(BaseModel):
    items: list[ApproversInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedApprove(Paging, Approve):
    pass
