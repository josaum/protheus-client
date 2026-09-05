"""Centro de Custo — generated from CostCenter_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CostCentersInfo(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1"], max_length=3
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "])
    company_internal_id: str | None = Field(
        None,
        alias="CompanyInternalId",
        description="InternalId da chave completa de empresa do produto",
        examples=["T1D MG 01 000000001"],
    )
    id: str | None = Field(
        None,
        alias="Id",
        description="Id, chave formada por Codigo da Coligada e Codigo do Centro de custo separados por '|'",
        examples=["1|01.7"],
    )
    code: str | None = Field(None, alias="Code", description="Código do Centro de Custo", examples=["000000001"])
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId de Integração", examples=["D MG 01 000000001"]
    )
    register_situation: str | None = Field(
        None, alias="RegisterSituation", description="Situação do Centro de Custo (Ativo ou Inativo)", examples=["2"]
    )
    name: str | None = Field(
        None, alias="Name", description="Descrição do Centro de Custo", examples=["Centro de Custo"], max_length=100
    )
    short_code: str | None = Field(None, alias="ShortCode", description="Código Reduzido", examples=["C001"])
    sped: str | None = Field(
        None, alias="SPED", description="Define se Centro de Custo será enviado para SPED", examples=[""]
    )
    allow_entry: str | None = Field(
        None, alias="AllowEntry", description="Define se Centro de Custo permite lançamento", examples=[""]
    )
    class_: str | None = Field(None, alias="Class", description="Classe", examples=["1"])
    top_code: str | None = Field(
        None, alias="TopCode", description="Código do Centro de Custo Superior", examples=["000000001"]
    )
    create_date: str | None = Field(
        None, alias="CreateDate", description="Data de inclusão do centro de custo", examples=[""]
    )
    accountable: str | None = Field(
        None, alias="Accountable", description="Código do responsável do centro de custo", examples=[""]
    )
    record_created_on: str | None = Field(
        None, alias="recordCreatedOn", description="Data de criação do registro na base de dados"
    )
    record_modified_on: str | None = Field(
        None, alias="recordModifiedOn", description="Data de modificação do registro na base de dados"
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


class CostCenters(BaseModel):
    items: list[CostCentersInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedCostCenters(Paging, CostCenters):
    pass
