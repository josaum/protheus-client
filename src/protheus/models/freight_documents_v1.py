"""FreightDocuments — generated from FreightDocuments_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class TypeofDocument(StrEnum):
    field_1___normal = "1 - Normal"
    field_2___complementar_valor = "2 - Complementar Valor"
    field_3___complementar_imposto = "3 - Complementar Imposto"
    field_4___reentrega = "4 - Reentrega"
    field_5___devolução = "5 - Devolução"
    field_6___redespacho = "6 - Redespacho"
    field_7___serviço = "7 - Serviço"


class FreightToll(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class IcmsBaseToll(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class PisCofinsBaseToll(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class TaxType(StrEnum):
    field_1___icms = "1 - ICMS"
    field_2___iss = "2 - ISS"
    field_3___nenhum = "3 - Nenhum"


class TaxationType(StrEnum):
    field_1___tributado = "1 - Tributado"
    field_2___isento_não_tributado = "2 - Isento/Não tributado"
    field_3___subs_tributária = "3 - Subs Tributária"
    field_4___diferido = "4 - Diferido"
    field_5___reduzido = "5 - Reduzido"
    field_6___outros = "6 - Outros"
    field_7___presumido = "7 - Presumido"


class TaxCredit(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class GenerateCredit(StrEnum):
    field_1___sim = "1 - Sim"
    field_2___não = "2 - Não"


class NaturSped(StrEnum):
    field_0___venda_c__ônus = "0 - Venda c/ ônus"
    field_1___vendas_s__ônus = "1 - Vendas s/ ônus"
    field_2___compra_c__crédito = "2 - Compra c/ crédito"
    field_3___compra_s__crédito = "3 - Compra s/ crédito"
    field_4___trans_prod_acabado = "4 - Trans Prod Acabado"
    field_5___transf_prod_elaboração = "5 - Transf Prod Elaboração"
    field_9___outras = "9 - Outras"


class Purpose(StrEnum):
    field_0___venda_c__ônus = "0 - Venda c/ ônus"
    field_1___vendas_s__ônus = "1 - Vendas s/ ônus"
    field_2___compra_c__crédito = "2 - Compra c/ crédito"
    field_3___compra_s__crédito = "3 - Compra s/ crédito"
    field_4___trans_prod_acabado = "4 - Trans Prod Acabado"
    field_5___transf_prod_elaboração = "5 - Transf Prod Elaboração"
    field_9___outras = "9 - Outras"


class Status(StrEnum):
    field_1___não_enviado = "1 - Não Enviado"
    field_2___pendente = "2 - Pendente"
    field_3___rejeitado = "3 - Rejeitado"
    field_4___atualizado = "4 - Atualizado"
    field_5___pendente_desatualização = "5 - Pendente Desatualização"
    field_6___não_se_aplica = "6 - Não se aplica"


class Transaction(StrEnum):
    field_310___despesa = "310 - Despesa"
    field_311___icms = "311 - ICMS"
    field_312___pis = "312 - PIS"
    field_313___cofins = "313 - COFINS"


class AccountingMovements(BaseModel):
    transaction: Transaction | None = Field(None, alias="Transaction", description="Transação ", examples=["310"])
    number: str | None = Field(None, alias="Number", description="Numero do Documento", examples=["0000000000000014"])
    debit_account: str | None = Field(None, alias="DebitAccount", description="Conta débito.", examples=["9999999"])
    cost_center: str | None = Field(None, alias="CostCenter", description="Centro Custo débito.", examples=["9999999"])
    business_unit: str | None = Field(None, alias="BusinessUnit", description="Unidade de negócio.", examples=["001"])
    value: str | None = Field(
        None, alias="Value", description="Valor de movimento.", examples=["30,00"], ge=0, le=999999999.99
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


class AccountingMovementsModel(BaseModel):
    items: list[AccountingMovements] | None = None


class FreightDocumentsType(BaseModel):
    internal_id: str | None = Field(
        None,
        alias="InternalId",
        description="Chave do documento de frete.",
        examples=["99 |CTRC |77785         |UN   |0300901         |20180930"],
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    document_specie: str | None = Field(
        None, alias="DocumentSpecie", description="Espécie do Documento.", examples=["CTRC"]
    )
    issuer_code: str | None = Field(None, alias="IssuerCode", description="Emissor do Documento.", examples=["77785"])
    document_serie: str | None = Field(None, alias="DocumentSerie", description="Série do Documento.", examples=["001"])
    document_number: str | None = Field(
        None, alias="DocumentNumber", description="Número do Documento.", examples=["9999999"]
    )
    issue_date: str | None = Field(None, alias="IssueDate", description="Data de Emissão.", examples=["20191010"])
    typeof_document: TypeofDocument | None = Field(
        None, alias="TypeofDocument", description="Tipo do Documento.", examples=["1"]
    )
    input_date: str | None = Field(None, alias="InputDate", description="Data de Entrada.", examples=["20191010"])
    tax_op_code: str | None = Field(None, alias="TaxOpCode", description="CFOP.", examples=["1232"])
    input_user: str | None = Field(None, alias="InputUser", description="Usuário de Entrada.", examples=["admin"])
    document_value: str | None = Field(
        None, alias="DocumentValue", description="Valor do Documento.", examples=["48,00"], ge=0, le=999999999.99
    )
    toll_value: str | None = Field(
        None, alias="TollValue", description="Valor do Pedágio.", examples=["42,00"], ge=0, le=999999.99
    )
    freight_toll: FreightToll | None = Field(
        None, alias="FreightToll", description="Pedágio no Valor do Frete.", examples=[1]
    )
    icms_base_toll: IcmsBaseToll | None = Field(
        None, alias="ICMSBaseToll", description="Pedágio na Base de ICMS.", examples=[1]
    )
    pis_cofins_base_toll: PisCofinsBaseToll | None = Field(
        None, alias="PisCofinsBaseToll", description="Pedágio na Base PIS/COFINS.", examples=[1]
    )
    tax_type: TaxType | None = Field(None, alias="TaxType", description="Tipo Imposto.", examples=[1])
    taxation_type: TaxationType | None = Field(
        None, alias="TaxationType", description="Tipo de Tributação.", examples=[1]
    )
    tax_calculation_base: str | None = Field(
        None,
        alias="TaxCalculationBase",
        description="Base de Cálculo Imposto.",
        examples=["48,00"],
        ge=0,
        le=999999999.99,
    )
    tax_rate: str | None = Field(
        None, alias="TaxRate", description="Alíquota Imposto.", examples=["12,00"], ge=0, le=100
    )
    tax_value: str | None = Field(
        None, alias="TaxValue", description="Valor do imposto.", examples=["20,00"], ge=0, le=999999.99
    )
    withheld_tax_value: str | None = Field(
        None, alias="WithheldTaxValue", description="Valor Imposto Retido.", examples=["20,00"], ge=0, le=999999.99
    )
    withheld_tax_rate: str | None = Field(
        None, alias="WithheldTaxRate", description="Percentual Imposto Retido.", examples=["20,00"], ge=0, le=100
    )
    note: str | None = Field(None, alias="Note", description="Observacoes", examples=["Teste"])
    tax_credit: TaxCredit | None = Field(None, alias="TaxCredit", description="Permite Crédito de ICMS", examples=["1"])
    electronic_access_key: str | None = Field(
        None,
        alias="ElectronicAccessKey",
        description="Chave do Ct-e",
        examples=["35170705248891000181570010000011831339972127"],
        ge=1,
        le=44,
    )
    integration_date: str | None = Field(
        None, alias="IntegrationDate", description="Data Integração Fiscal", examples=["20191010"]
    )
    cofins_base_value: str | None = Field(
        None, alias="CofinsBaseValue", description="Valor Base Cofins", examples=["20,00"], ge=1, le=999999999.99
    )
    cofins_value: str | None = Field(
        None, alias="CofinsValue", description="Valor Cofins", examples=["20,00"], ge=1, le=999999999.99
    )
    pis_base_value: str | None = Field(
        None, alias="PisBaseValue", description="Valor Base PIS", examples=["20,00"], ge=1, le=999999999.99
    )
    pis_value: str | None = Field(
        None, alias="PisValue", description="Valor PIS", examples=["20,00"], ge=1, le=999999999.99
    )
    generate_credit: GenerateCredit | None = Field(
        None, alias="GenerateCredit", description="Gera crédito PIS/COFINS", examples=["1"]
    )
    natur_sped: NaturSped | None = Field(None, alias="NaturSped", description="Natur SPED", examples=["1"])
    purpose: Purpose | None = Field(None, alias="Purpose", description="Tipo do CT-e", examples=["1"])
    tax_rejection_reason: str | None = Field(
        None, alias="TaxRejectionReason", description="Motivo de Rejeição Fiscal", examples=["Teste"]
    )
    service_type: str | None = Field(None, alias="ServiceType", description="Código Tipo Serviço", examples=["Teste"])
    city_origin: str | None = Field(
        None, alias="cityOrigin", description="Código da cidade de Origem.", examples=["0000001"]
    )
    uf_origin: str | None = Field(
        None, alias="UFOrigin", description="Codigo do Estado (UF) de Origem.", examples=["SC"]
    )
    city_origin_name: str | None = Field(
        None, alias="cityOriginName", description="Nome da Cidade de Origem.", examples=["JOINVILLE"]
    )
    city_destination: str | None = Field(
        None, alias="cityDestination", description="Código da cidade de destino.", examples=["0000001"]
    )
    city_destination_name: str | None = Field(
        None, alias="cityDestinationName", description="Nome da Cidade de destino.", examples=["JOINVILLE"]
    )
    uf_destination: str | None = Field(
        None, alias="UFDestination", description="Nome da Cidade de destino.", examples=["JOINVILLE"]
    )
    status: Status | None = Field(None, alias="Status", description="Situação Fiscal", examples=["1"])
    accounting_movements: AccountingMovementsModel | None = Field(
        None, alias="AccountingMovements", description="Movimentos Contábeis."
    )


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedFreightDocuments(Paging):
    items: list[FreightDocumentsType] | None = None
