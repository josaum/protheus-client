"""Tópico de Auditorias — generated from AuditTopic_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from datetime import date

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ItensTableTopicItem(BaseModel):
    topic: str | None = Field(None, description="Topico", max_length=10)
    rule_code: str | None = Field(None, alias="ruleCode", description="Código da Norma", max_length=10)
    description: str | None = Field(None, description="Descrição", max_length=50)
    notes: str | None = Field(None, description="Observações", max_length=50)


class ItensTableTopic(BaseModel):
    pass


class AuditTopicType(BaseModel):
    company_id: str | None = Field(None, alias="companyId", description="Empresa", max_length=3)
    branch_id: str | None = Field(None, alias="branchId", description="Filial", examples=["D MG 01"])
    check_list: str | None = Field(None, alias="checkList", description="Número do Check List", le=6)
    internal_id: str | None = Field(None, alias="internalId", description="InternalId do Questionário de Auditoria")
    revision: str | None = Field(None, description="Revisão do Topico", le=2)
    last_revision: date | None = Field(
        None, alias="lastRevision", description="Última Revisão", examples=["01-01-2019"], max_length=8
    )
    itens_table_topic: list[ItensTableTopicItem] | ItensTableTopic | None = Field(None, alias="itensTableTopic")


class ItensTableTopicInfoItem(BaseModel):
    topic: str | None = Field(None, description="Topico", max_length=10)
    rule_code: str | None = Field(None, alias="ruleCode", description="Código da Norma", max_length=10)
    description: str | None = Field(None, description="Descrição", max_length=50)
    notes: str | None = Field(None, description="Observações", max_length=50)


class ItensTableTopicInfo(RootModel[list[ItensTableTopicInfoItem]]):
    root: list[ItensTableTopicInfoItem]


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedTopic(Paging):
    items: list[AuditTopicType] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
