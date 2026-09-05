"""Grupo de Região — generated from RegionGroups_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class RegionCategory(StrEnum):
    field_1 = "1"
    field_2 = "2"


class GroupCategory(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"


class RegionExemptTaxes(StrEnum):
    field_1 = "1"
    field_2 = "2"


class TmsPortal(StrEnum):
    field_1 = "1"
    field_2 = "2"


class StateType(BaseModel):
    state_id: str | None = Field(None, alias="stateId", description="Código do estado")
    state_internal_id: str | None = Field(None, alias="stateInternalId", description="InternalId do Estado no ERP")
    state_description: str | None = Field(None, alias="stateDescription", description="Nome do estado")


class CountryType(BaseModel):
    country_code: str | None = Field(None, alias="countryCode", description="Código do país")
    country_internal_id: str | None = Field(None, alias="countryInternalId", description="InternalId do país no ERP")
    country_description: str | None = Field(None, alias="countryDescription", description="Nome do país")


class CityType(BaseModel):
    city_code: str | None = Field(None, alias="cityCode", description="Código da cidade")
    city_internal_id: str | None = Field(None, alias="cityInternalId", description="InternalId da Cidade no ERP")
    city_description: str | None = Field(None, alias="cityDescription", description="Nome da cidade")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class RegionGroupsInfo(BaseModel):
    company_id: str | None = Field(
        None, alias="CompanyId", description="Código da empresa", examples=["T1"], max_length=3
    )
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01 "], max_length=12
    )
    company_internal_id: str | None = Field(None, alias="CompanyInternalId", description="Código da Empresa")
    code: str | None = Field(
        None, alias="Code", description="Código do Grupo de Região.", examples=["Q50308"], max_length=6
    )
    internal_id: str | None = Field(None, alias="InternalId", description="InternalId do Grupo de Região no ERP")
    description: str | None = Field(
        None, alias="Description", description="Descrição do Grupo de Região", examples=["Sao Paulo"], max_length=30
    )
    top_group: str | None = Field(None, alias="TopGroup", description="Código do Grupo Superior", examples=["SP"])
    state: StateType | None = Field(None, alias="State")
    destination_branch: str | None = Field(
        None, alias="DestinationBranch", description="Filial", examples=["M SP 01 "], max_length=12
    )
    associated_company_region_code: (
        str | None
    ) = Field(None, alias="AssociatedCompanyRegionCode", description="Código da Região Coligada", examples=["Q56453"])
    associated_company_region_description: (
        str | None
    ) = (
        Field(None, alias="AssociatedCompanyRegionDescription", description="Descrição do Grupo de Região Coligada", examples=["VARGEM GRANDE PAULISTA"], max_length=30)
    )
    region_category: RegionCategory | None = Field(
        None, alias="RegionCategory", description="Categoria da Região", examples=["1"]
    )
    base_tax_region: str | None = Field(
        None, alias="BaseTaxRegion", description="Código da Região Base para Taxa", examples=["Q50308"]
    )
    group_category: GroupCategory | None = Field(
        None, alias="GroupCategory", description="Categoria do Grupo", examples=["3"]
    )
    region_exempt_taxes: RegionExemptTaxes | None = Field(
        None, alias="RegionExemptTaxes", description="Região Isenta de Impostos", examples=["2"]
    )
    iss_rate: float | None = Field(None, alias="ISSRate", description="Aliquota do ISS", examples=["5,2"])
    country: CountryType | None = Field(None, alias="Country")
    city: CityType | None = Field(None, alias="City")
    tms_portal: TmsPortal | None = Field(None, alias="TMSPortal", description="Utiliza no portal TMS", examples=["2"])


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class RegionGroups(BaseModel):
    items: list[RegionGroupsInfo] | None = None


class PagedRegionGroups(Paging, RegionGroups):
    pass
