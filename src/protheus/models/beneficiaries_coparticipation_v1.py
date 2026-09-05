"""Relação de Coparticipações dos Beneficiários e seus dependentes - Global — generated from BeneficiariesCoparticipation_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ServiceProviderContractType(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_9 = "9"


class ServiceType(StrEnum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    field_5 = "5"
    field_6 = "6"
    field_7 = "7"
    field_8 = "8"
    field_9 = "9"
    field_10 = "10"
    field_11 = "11"
    field_12 = "12"
    field_13 = "13"


class BeneficiariesCoparticipationItem(BaseModel):
    id: str | None = Field(
        None, alias="Id", description="Chave única que identifica os registros dos lançamentos de coparticipações."
    )
    company_key: str | None = Field(
        None, alias="CompanyKey", description="Empresa referente a coparticipação lançada no Datasul."
    )
    branch: str | None = Field(
        None, alias="Branch", description="Filial (Estabelecimento) referente a coparticipação lançada no Datasul."
    )
    employee_code: str | None = Field(
        None, alias="EmployeeCode", description="Matrícula do Beneficiário dentro do Produto TOTVS."
    )
    employee_name: str | None = Field(
        None, alias="EmployeeName", description="Nome do Beneficiário do Funcionário dentro do Produto TOTVS."
    )
    dependent_code: str | None = Field(
        None, alias="DependentCode", description="Matrícula do Dependente do Beneficiário dentro do Produto TOTVS."
    )
    dependent_name: str | None = Field(
        None, alias="DependentName", description="Nome do Dependente do Beneficiário dentro do Produto TOTVS."
    )
    degree_employee_dependency: (
        str | None
    ) = Field(None, alias="DegreeEmployeeDependency", description="Grau de dependência do Funcionário no Datasul.")
    occurrency_date: AwareDatetime | None = Field(
        None,
        alias="OccurrencyDate",
        description="Data de ocorrência do lançamento da coparticipação para o beneficiário.",
    )
    service_provider: str | None = Field(
        None, alias="ServiceProvider", description="Identificador do Prestador de Serviço"
    )
    service_provider_contract_type: (
        ServiceProviderContractType | None
    ) = (
        Field(None, alias="ServiceProviderContractType", description="Tipo de Contrato do Prestador de Serviço indicado no lançamento da Coparticipação do Beneficiário: 1 - Assistência Médica | 2 - Assistência Odontológica | 3 - VR | 4 - VA | 5 - VT | 9 - Outros")
    )
    service_provider_contract: (
        str | None
    ) = (
        Field(None, alias="ServiceProviderContract", description="Número do Contrato do Prestador de Serviço indicado no lançamento da Coparticipação do Beneficiário.")
    )
    coparticipation_value: int | None = Field(
        None,
        alias="CoparticipationValue",
        description="Valor referente ao lançamento da coparticipação do beneficiário no Produto TOTVS.",
    )
    year_month_reference: str | None = Field(
        None,
        alias="YearMonthReference",
        description="Ano e mês de referência do lançamento da coparticipação do beneficiário no Produto TOTVS.",
    )
    service_provider_id: str | None = Field(
        None,
        alias="ServiceProviderId",
        description="CNPJ do Prestador de Serviço referente ao lançamento da coparticipação do beneficiário no Produto TOTVS.",
    )
    service_provider_name: str | None = Field(
        None,
        alias="ServiceProviderName",
        description="Nome do Prestador de Serviço referente ao lançamento da coparticipação do beneficiário no Produto TOTVS.",
    )
    specialty_name: str | None = Field(
        None,
        alias="SpecialtyName",
        description="Nome da especialidade do Prestador de Serviço referente ao lançamento da coparticipação do beneficiário no Produto TOTVS.",
    )
    international_code_diseases: (
        str | None
    ) = (
        Field(None, alias="InternationalCodeDiseases", description="Código internacional de Doenças lançado da coparticipação do beneficiário no Produto TOTVS.")
    )
    service_type: ServiceType | None = Field(
        None,
        alias="ServiceType",
        description="Tipo de Atendimento informado pelo Prestador de Serviço no lançamento da Coparticipação do Beneficiário: 1 - Eletivo | 2 - PS | 3 - Exame | 4 - PAC | 5 - Material/Medicamento | 6 - Internação | 7 - Terapia | 8 - Taxa/Diária| 9 - Case | 10 - Reembolso | 11 - Remoção | 12 - Não Informado | 13 - Ambulatório",
    )
    amount_use: str | None = Field(
        None,
        alias="AmountUse",
        description="Quantidade de utilização de coparticipação por parte do beneficiário e seus dependentes dentro do Produto TOTVS.",
    )
    coparticipation_description: (
        str | None
    ) = (
        Field(None, alias="CoparticipationDescription", description="Descrição da Coparticipação referente ao lançamento no histórico do beneficiário no Produto TOTVS.")
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


class PagedBeneficiariesCoparticipation(Paging):
    total: int | None = Field(None, examples=["1"])
    items: list[BeneficiariesCoparticipationItem] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
