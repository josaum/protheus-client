"""Relação de Benficiários - Global — generated from BeneficiariesDataContent_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class BenefitVendorSegmentCode(StrEnum):
    field_1 = "1"
    field_2 = "2"


class DegreeOfRelatedness(StrEnum):
    t = "T"
    c = "C"
    f = "F"
    e = "E"
    p = "P"
    o = "O"


class Gender(StrEnum):
    m = "M"
    f = "F"


class MaritalState(StrEnum):
    c = "C"
    d = "D"
    e = "E"
    i = "I"
    o = "O"
    p = "P"
    s = "S"
    v = "V"


class BornAlive(StrEnum):
    field_1 = "1"
    field_2 = "2"


class BeneficiariesDataContentItem(BaseModel):
    company_key: str | None = Field(
        None, alias="companyKey", description="Agrupamento de Empresa, Unidade de negócio e Filial"
    )
    branch: str | None = Field(None, description="Filial do Beneficiário")
    code: str | None = Field(None, description="Código do Beneficiário")
    id: str | None = Field(None, description="Chave única do Beneficiário")
    benefits_vendor_code: str | None = Field(
        None, alias="benefitsVendorCode", description="Identificador do Fornecedor de Benefícios"
    )
    benefit_vendor_internal_id: (
        str | None
    ) = Field(None, alias="benefitVendorInternalId", description="Identificador Interno do Fornecedor de Benefícios")
    benefit_vendor_segment_code: (
        BenefitVendorSegmentCode | None
    ) = (
        Field(None, alias="benefitVendorSegmentCode", description="Código do tipo de segmento do fornecedor do Benefício: 1 - Assistência Médica | 2 - Assistência Odontológica ")
    )
    benefit_code: str | None = Field(None, alias="benefitCode", description="Código do Benefício")
    benefit_internal_id: str | None = Field(
        None, alias="benefitInternalId", description="Identificador Interno do Benefício"
    )
    begin_date: AwareDatetime | None = Field(
        None, alias="beginDate", description="Início da vigência do Benefício ao beneficiário"
    )
    final_date: AwareDatetime | None = Field(
        None, alias="finalDate", description="Fim da vigência do Benefício ao beneficiário"
    )
    contract_number_code: str | None = Field(None, alias="contractNumberCode", description="Código do Contrato")
    contract_number_internal_id: (
        str | None
    ) = Field(None, alias="contractNumberInternalId", description="Identificador interno do Contrato")
    employee_code: str | None = Field(None, alias="employeeCode", description="Identificado do Funcionário")
    employee_internal_id: str | None = Field(
        None, alias="employeeInternalId", description="Identificado interno do Funcionário"
    )
    registry_type: str | None = Field(None, alias="registryType", description="Tipo do Registro do Beneficiário")
    degree_of_relatedness: DegreeOfRelatedness | None = Field(
        None,
        alias="degreeOfRelatedness",
        description="Grau de parentesco do dependente com o Titular: T - Titular, C - Conjuge, F - Filho, E - Enteado, P - Pai/Mae, O - Outros",
    )
    name: str | None = Field(None, description="Nome do beneficiário")
    benefit_cpf: str | None = Field(None, alias="benefitCPF", description="CPF do Beneficiário")
    mother_name: str | None = Field(None, alias="motherName", description="Nome da Mãe do beneficiário titular")
    gender: Gender | None = Field(None, description="Sexo do beneficiário: M - Masculino, F - Feminino")
    marital_state: MaritalState | None = Field(
        None,
        alias="maritalState",
        description="Estado Civil C - Casado | D - Desquitado | E - União Estável | I - Divorciado | O - Outros | P - Separado | S - Solteiro | V - Viúvo",
    )
    birth: str | None = Field(None, description="Data de aniversário do beneficiário")
    identity_number: str | None = Field(None, alias="identityNumber", description="Identidade da pessoa (RG)")
    identity_number_emitter_agency: (
        str | None
    ) = Field(None, alias="identityNumberEmitterAgency", description="Orgão emissor da identidade da pessoa (RG)")
    medical_assistance_card: str | None = Field(
        None, alias="medicalAssistanceCard", description="Numero do Cartão de Assistência Médica"
    )
    dental_assistance_card_code: (
        str | None
    ) = Field(None, alias="dentalAssistanceCardCode", description="Numero do Cartão de Assistência Odontológica")
    food_cards_code: str | None = Field(None, alias="foodCardsCode", description="Numero do Cartão para Alimentação")
    meal_cards_code: str | None = Field(None, alias="mealCardsCode", description="Numero do Cartão para Refeição")
    sus_card_code: str | None = Field(None, alias="SUSCardCode", description="Numero do Cartão do SUS")
    born_alive: BornAlive | None = Field(
        None,
        alias="bornAlive",
        description="Flag que determina se o beneficiário foi nascido vivo: 1 - Nascido Vivo , 0 - Não Nascido Vivo",
    )
    beneficiary_weight: str | None = Field(None, alias="beneficiaryWeight", description="Peso em (gr) do Beneficiário")
    beneficiary_tall: str | None = Field(None, alias="beneficiaryTall", description="Altura em (cm) do beneficiário")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedBeneficiariesDataContent(Paging):
    total: int | None = Field(None, examples=["1"])
    items: list[BeneficiariesDataContentItem] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
