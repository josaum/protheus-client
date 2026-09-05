"""Campanhas — generated from Campaigns_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Type(StrEnum):
    field_1 = "1"
    field_2 = "2"


class Attendance(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class CampaignEvolutionStatus(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"


class ListOfCampaign(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId do item da Campanha no ERP",
        examples="D MG 01 00000101/01/19900101",
    )
    event_code: str | None = Field(
        None, alias="EventCode", description="Código do Evento.", examples=["000001"], max_length=6
    )
    script_code: str | None = Field(
        None, alias="ScriptCode", description="Código do Script.", examples=["000001"], max_length=6
    )
    product_code: str | None = Field(
        None, alias="ProductCode", description="Código do Produto.", examples=["000001"], max_length=6
    )
    midia_code: str | None = Field(
        None, alias="MidiaCode", description="Código da mídia.", examples=["000001"], max_length=6
    )


class ListOfCampaigns(BaseModel):
    pass


class CampaignsInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa", max_length=3)
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da campanha no ERP", examples="D MG 01 000001"
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01"], max_length=8
    )
    company_internal_id: str | None = Field(None, alias="CompanyInternalId", description="Código da Empresa")
    code: str | None = Field(None, alias="Code", description="Código da campanha.", examples=["000001"], max_length=6)
    type: Type | None = Field(
        None, alias="Type", description="Tipo de atendimento.(1-Receptivo, 2-Ativo)", examples=["1"]
    )
    campaing_description: str | None = Field(
        None,
        alias="CampaingDescription",
        description="Descrição da campanha.",
        examples=["Campanha de nova versão do produto"],
        max_length=40,
    )
    init_date: str | None = Field(
        None,
        alias="InitDate",
        description="Data em que a campanha foi iniciada.",
        examples=["10/10/2018"],
        max_length=8,
    )
    end_date: str | None = Field(
        None,
        alias="EndDate",
        description="Data em que a campanha foi fechada ou concluída",
        examples=["11/10/2018"],
        max_length=8,
    )
    objective: str | None = Field(
        None,
        alias="Objective",
        description="Objetivo da campanha.",
        examples=["O objetivo desta campanha é demonstrar o serviço de API´s"],
        max_length=254,
    )
    attendance: Attendance | None = Field(
        None,
        alias="Attendance",
        description="Tipo de atendimento.(1-Telemarketing, 2-Televendas, 3-Telecobranca, 4-Todos, 5-Marketing)",
        examples=["5"],
    )
    expected_porcentage: float | None = Field(
        None,
        alias="ExpectedPorcentage",
        description="Percentual  de resposta esperada para a campanha.",
        examples=["60"],
        ge=0.0,
        le=100.0,
    )
    blocked_record: str | None = Field(
        None,
        alias="BlockedRecord",
        description="Campanha bloqueada para uso (1-bloqueado 2-ativo).",
        examples=["2"],
        max_length=1,
    )
    campaign_evolution_status: (
        CampaignEvolutionStatus | None
    ) = (
        Field(None, alias="Campaign_Evolution_Status", description="Status da evolução da campanha (1-Pronta para ser lançada, 2-Lançada, 3-Concluída, 4-Cancelada, 5-Suspensa)", examples=["1"])
    )
    campaing_type: str | None = Field(
        None, alias="CampaingType", description="Tipo da campanha.", examples=["000001"], max_length=6
    )
    list_of_campaigns: list[ListOfCampaign] | ListOfCampaigns | None = Field(
        None, alias="ListOfCampaigns", description="Descreve a lista de campanhas"
    )


class ListCampaign(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="InternalId do item da Campanha no ERP",
        examples="D MG 01 00000101/01/19900101",
    )
    event_code: str | None = Field(
        None, alias="EventCode", description="Código do Evento.", examples=["000001"], max_length=6
    )
    script_code: str | None = Field(
        None, alias="ScriptCode", description="Código do Script.", examples=["000001"], max_length=6
    )
    product_code: str | None = Field(
        None, alias="ProductCode", description="Código do Produto.", examples=["000001"], max_length=6
    )
    midia_code: str | None = Field(
        None, alias="MidiaCode", description="Código da mídia.", examples=["000001"], max_length=6
    )


class ListCampaigns(RootModel[list[ListCampaign]]):
    root: list[ListCampaign] = Field(..., description="Descreve a lista de campanhas")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Campaigns(BaseModel):
    items: list[CampaignsInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedCampaigns(Paging, Campaigns):
    pass
