"""Entities — generated from Entities_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Class(StrEnum):
    field_1___próprio = "1 - Próprio"
    field_2___cooperado = "2 - Cooperado"
    field_3___terceiro = "3 - Terceiro"


class DapIncentive(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class ActiveRegister(StrEnum):
    field_1___ativo = "1 - Ativo"
    field_2___inativo = "2 - Inativo"


class CustomsWarehouse(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class BankDatasType(BaseModel):
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    entity_code: str | None = Field(None, alias="EntityCode", description="Código da entidade", examples=["000001"])
    item: str | None = Field(None, alias="Item", description="Item dos dados bancários.", examples=["01"])
    bank_code: str | None = Field(None, alias="BankCode", description="Código do banco.", examples=["001"])
    agency_code: str | None = Field(None, alias="AgencyCode", description="Código da agência.", examples=["12345"])
    agency_verifying_digit: str | None = Field(
        None, alias="AgencyVerifyingDigit", description="Dígito verificador da agência.", examples=["12345"]
    )
    account_code: str | None = Field(None, alias="AccountCode", description="Número da conta.", examples=["0123456789"])
    account_verifying_digit: str | None = Field(
        None, alias="AccountVerifyingDigit", description="Dígito verificador da conta.", examples=["3"]
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


class BankDatas(BaseModel):
    items: list[BankDatasType] | None = None


class EntitiesType(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave da entidade.", examples=["99|000003|01"]
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    entity_code: str | None = Field(None, alias="EntityCode", description="Código da entidade.", examples=["000002"])
    entity_store_code: str | None = Field(
        None, alias="EntityStoreCode", description="Loja da entidade.", examples=["01"]
    )
    cnpj_entity: str | None = Field(
        None, alias="CNPJEntity", description="Cadastro do CNPJ da entidade", examples=["53113791002761"]
    )
    state_registration: str | None = Field(
        None, alias="StateRegistration", description="Inscrição estadual.", examples=["23210223"]
    )
    entity_name: str | None = Field(
        None, alias="EntityName", description="Nome da entidade.", examples=["FAZENDA RIO DE JANEIRO LTDA."]
    )
    entity_store_name: str | None = Field(
        None, alias="EntityStoreName", description="Nome da loja da entidade.", examples=["FAZENDA RIO DE JANEIRO"]
    )
    class_: Class | None = Field(None, alias="Class", description="Classe da entidade.", examples=["1"])
    dap_incentive: DapIncentive | None = Field(
        None, alias="DAPIncentive", description="Possui o incentivo DAP?", examples=["1"]
    )
    dap_expiration_date: Any | None = Field(
        None, alias="DAPExpirationDate", description="Data de vencimento do incentivo DAP.", examples=[20200101]
    )
    dap_register_number: str | None = Field(
        None, alias="DAPRegisterNumber", description="Número do registro de incentivo DAP.", examples=["0000000001"]
    )
    company_and_branch_code: str | None = Field(
        None, alias="CompanyAndBranchCode", description="Código da empresa e filial da entidade.", examples=["D RJ 01 "]
    )
    company_name: str | None = Field(
        None, alias="CompanyName", description="Nome da empresa correspondente.", examples=["Empresa Carioca"]
    )
    branch_name: str | None = Field(
        None, alias="BranchName", description="Nome da empresa correspondente.", examples=["Rio de Janeiro"]
    )
    active_register: ActiveRegister | None = Field(
        None, alias="ActiveRegister", description="Cadastro ativo?", examples=["1"]
    )
    supplier_code: str | None = Field(
        None, alias="SupplierCode", description="Código do fornecedor correspondente à entidade.", examples=["000003"]
    )
    supplier_store_code: str | None = Field(
        None,
        alias="SupplierStoreCode",
        description="Código da loja do fornecedor correspondente à entidade.",
        examples=["01"],
    )
    supplier_name: str | None = Field(
        None,
        alias="SupplierName",
        description="Nome do fornecedor correspondente à entidade.",
        examples=["Fazenda Rio de Janeiro LTDA."],
    )
    supplier_store_name: str | None = Field(
        None,
        alias="SupplierStoreName",
        description="Nome da loja do fornecedor correspondente à entidade.",
        examples=["Rio de Janeiro"],
    )
    customer_code: str | None = Field(
        None, alias="CustomerCode", description="Código do cliente correspondente à entidade.", examples=["000003"]
    )
    customer_store_code: str | None = Field(
        None,
        alias="CustomerStoreCode",
        description="Código da loja do cliente correspondente à entidade.",
        examples=["01"],
    )
    customer_name: str | None = Field(
        None,
        alias="CustomerName",
        description="Nome do cliente correspondente à entidade.",
        examples=["Fazenda Rio de Janeiro LTDA."],
    )
    customer_store_name: str | None = Field(
        None,
        alias="CustomerStoreName",
        description="Nome da loja do fornecedor correspondente à entidade.",
        examples=["Rio de Janeiro"],
    )
    customs_warehouse: CustomsWarehouse | None = Field(
        None, alias="CustomsWarehouse", description="Depósito alfandegário?", examples=["1"]
    )
    id_integration_pims: str | None = Field(
        None, alias="IDIntegrationPIMS", description="Código de integração com o PIMS.", examples=["0192749"]
    )
    bank_datas: BankDatas | None = Field(None, alias="BankDatas", description="Lista dos dados bancários da entidade.")


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedEntities(Paging):
    items: list[EntitiesType] | None = None
