"""Atividade do Vendedor — generated from SellerActivity_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class Status(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_6 = "6"
    field_7 = "7"
    field_8 = "8"
    field_9 = "9"


class Priority(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class CompletionPercentage(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class RegisterSituation(StrEnum):
    field_1 = "1"
    field_2 = "2"


class SellerActivityInfo(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1"], max_length=3
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12
    )
    code: str | None = Field(None, alias="Code", description="Código da Atividade", examples=["000001"])
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da Atividade do Vendedor no ERP", examples=["D MG 01 000001"]
    )
    type: Type | None = Field(
        None,
        alias="Type",
        description="Define o tipo de atividade cadastrada. 1 - Tarefa, 2 - Compromisso e 3 - Email.",
        examples=["1"],
    )
    status: Status | None = Field(
        None,
        alias="Status",
        description="Define o status da atividade cadastrada. 1 - Não Iniciado, 2 - Em Andamento , 3 - Concluída, 4 - Aguardando outros, 5 - Adiada, 6 - Pendente, 7 - Enviado, 8 - Lido e 9 - Cancelada",
        examples=["1"],
    )
    participant: str | None = Field(
        None, alias="Participant", description="E-Mail do Participante", examples=["contato@teste.com"]
    )
    local_activity: str | None = Field(
        None, alias="LocalActivity", description="Local da Atividade", examples=["SALA 01"]
    )
    subject: str | None = Field(None, alias="Subject", description="Assunto da atividade", examples=["Reunião diaria"])
    register_date: AwareDatetime | None = Field(
        None, alias="RegisterDate", description="Data de cadastro da atividade", examples=["1900-01-01T12:00:00Z"]
    )
    description: str | None = Field(
        None, alias="Description", description="Descrição da Atividade", examples=["Reunião de alinhamento diario"]
    )
    owner: str | None = Field(None, alias="Owner", description="Código do proprietario", examples=["000001"])
    priority: Priority | None = Field(
        None,
        alias="Priority",
        description="Define o tipo de atividade cadastrada. 1 - Alta, 2 - Normal e 3 - Baixa.",
        examples=["1"],
    )
    start_date: AwareDatetime | None = Field(
        None, alias="StartDate", description="Data Inicio", examples=["1900-01-01T12:00:00Z"]
    )
    start_time: str | None = Field(None, alias="StartTime", description="Hora Inicio", examples=["12:00"])
    end_date: AwareDatetime | None = Field(
        None, alias="EndDate", description="Data Fim", examples=["1900-01-01T12:00:00Z"]
    )
    end_time: str | None = Field(None, alias="EndTime", description="Hora Fim", examples=["13:00"])
    duration: str | None = Field(None, alias="Duration", examples=[999.99], ge=-999.99, le=999.99)
    entity_id: str | None = Field(None, alias="EntityId", description="Alias da Entidade", examples=["SA1"])
    entity_key: str | None = Field(None, alias="EntityKey", description="Codigo da Entidade", examples=["00000101"])
    remind_date: AwareDatetime | None = Field(
        None, alias="RemindDate", description="Data do Lembrete", examples=["1900-01-01T12:00:00Z"]
    )
    remind_time: str | None = Field(None, alias="RemindTime", description="Hora do Lembrete", examples=["11:50"])
    completion_percentage: CompletionPercentage | None = Field(
        None,
        alias="CompletionPercentage",
        description="Define o status da atividade cadastrada. 1 - 0%, 2 - 25%, 3 - 50%, 4 - 75% e 5 - 100%",
        examples=["1"],
    )
    conclusion_date: AwareDatetime | None = Field(
        None, alias="ConclusionDate", description="Data de conclusão", examples=["1900-01-01T12:00:00Z"]
    )
    register_situation: RegisterSituation | None = Field(
        None, alias="RegisterSituation", description="Registro bloqueado. 1 - Invativo e 2 - Ativo", examples=["2"]
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


class SellerActivity(BaseModel):
    items: list[SellerActivityInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedSellerActivity(Paging, SellerActivity):
    pass
