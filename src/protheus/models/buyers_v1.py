"""Compradores — generated from Buyers_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class OrderSc(StrEnum):
    field_1___sim = "1 = SIM"
    field_2___não = "2 = NÃO"


class BuyerInfo(BaseModel):
    company_internal_id: str | None = Field(
        None, alias="companyInternalId", description="InternalId da chave completa de empresa do produto."
    )
    branch_id: str | None = Field(None, alias="branchId", description="ID Filial.", examples=["M SP 01"], max_length=4)
    buyer_id: str | None = Field(None, alias="BuyerId", description="Código do Comprador.")
    name: str | None = Field(None, alias="Name", description="Nome do Comprador.")
    user_login: str | None = Field(None, alias="userLogin", description="ID do Login do usuário no Protheus.")
    company: str | None = Field(None, alias="Company", description="Estabelecimento Padrão.")
    cost_center: str | None = Field(None, alias="CostCenter", description="Centro de Custo.")
    is_corporative: bool | None = Field(None, alias="isCorporative", description="Corporativo.")
    purchasing_group: str | None = Field(None, alias="PurchasingGroup", description="Grupo de Compras do Comprador.")
    email: str | None = Field(None, alias="Email", description="E-mail do Comprador.")
    homepage: str | None = Field(None, alias="Homepage", description="Homepage do Comprador.")
    telephone: str | None = Field(None, alias="Telephone", description="Telefone do Comprador.")
    telephone_line: str | None = Field(None, alias="TelephoneLine", description="Ramal do Comprador.")
    fax: str | None = Field(None, alias="Fax", description="Fax do Comprador.")
    fax_line: str | None = Field(None, alias="FaxLine", description="Ramal do Fax do Comprador.")
    approve_group: str | None = Field(
        None, alias="approveGroup", description="Grupo de aprovação do Comprador no Protheus."
    )
    order_sc: OrderSc | None = Field(
        None,
        alias="orderSC",
        description="Campo para informar se o Comprador pode aprovar SC (Solicitação de Compra) ou não.",
    )
    purchase_group_contract: str | None = Field(
        None,
        alias="purchaseGroupContract",
        description="Grupo de Aprovação de Contratos que o Comprador pode ser vinculado.",
    )
    buyer_profile: str | None = Field(
        None, alias="buyerProfile", description="Perfil do Comprador usado no Portal de MarketPlace."
    )
    situation: str | None = Field(None, description="Situação do comprador", max_length=1)


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PostBuyer(BuyerInfo):
    pass


class PagedBuyers(Paging):
    items: list[BuyerInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
