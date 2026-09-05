"""Relação de Funcionários - Global — generated from EmployeeDataContent_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class EmployeeDataContentItem(BaseModel):
    company_key: str | None = Field(
        None, alias="companyKey", description="Agrupamento de Empresa, Unidade de negócio e Filial"
    )
    branch: str | None = Field(None, description="Filial do Funcionario")
    code: str | None = Field(None, description="Matricula do Funcionario")
    id: str | None = Field(None, description="id do funcionário")
    name: str | None = Field(None, description="Nome do Funcionario")
    full_name: str | None = Field(None, alias="fullName", description="Nome Completo do Funcionário")
    badge_number: str | None = Field(None, alias="badgeNumber", description="Número do Crachá")
    department_code: str | None = Field(None, alias="departmentCode", description="Codigo do departamento")
    department_internal_id: str | None = Field(
        None, alias="departmentInternalId", description="InternalId do Departamento"
    )
    department_description: str | None = Field(
        None, alias="departmentDescription", description="Descrição do Departamento"
    )
    hiring_date: AwareDatetime | None = Field(None, alias="hiringDate", description="Data de Admissão")
    demission_date: AwareDatetime | None = Field(None, alias="demissionDate", description="Data de Demissão")
    birth_date: AwareDatetime | None = Field(None, alias="birthDate", description="Data de aniversário")
    gender: str | None = Field(None, description="Sexo")
    street: str | None = Field(None, description="Rua do funcionário")
    street_number: str | None = Field(None, alias="streetNumber", description="Número do endereço")
    complement: str | None = Field(None, description="Complemento do endereço")
    neighborhood: str | None = Field(None, description="Bairro do Funcionário")
    home_state: str | None = Field(None, alias="homeState", description="Estado do Funcionário")
    natural_city: str | None = Field(None, alias="naturalCity", description="Naturalidade")
    employee_situation: str | None = Field(
        None, alias="employeeSituation", description="Situação do Funcionário na Folha"
    )
    work_center_code: str | None = Field(None, alias="workCenterCode", description="Centro de Trabalho")
    city: str | None = Field(None, description="Cidade do Funcionário")
    zip_code: str | None = Field(None, alias="zipCode", description="Número do Cep")
    area_code: str | None = Field(None, alias="areaCode", description="Código de Área(DDD)")
    telephone: str | None = Field(None, description="Telefone")
    area_code_mobile: str | None = Field(None, alias="areaCodeMobile", description="Código de Área(DDD)")
    mobile_number: str | None = Field(None, alias="mobileNumber", description="Número do Telefone Celular")
    social_integ_prog_code: str | None = Field(
        None, alias="socialIntegProgCode", description="Numero do PIS do Funcionário"
    )
    work_card_number: str | None = Field(
        None, alias="workCardNumber", description="Carteira de Trabalho do Funcionário"
    )
    work_card_serie: str | None = Field(
        None, alias="workCardSerie", description="Serie da Carteira de Trabalho Profissional"
    )
    work_card_state_issuing: str | None = Field(
        None, alias="workCardStateIssuing", description="Unidade da federação emitente da carteira de trabalho"
    )
    cost_center_code: str | None = Field(None, alias="costCenterCode", description="Código do Centro de Custo")
    cost_center_internal_id: str | None = Field(
        None, alias="costCenterInternalId", description="InternalId do Centro de Custo"
    )
    cost_center_description: str | None = Field(
        None, alias="costCenterDescription", description="Descrição do Centro de Custo"
    )
    employee_position_code: str | None = Field(
        None, alias="employeePositionCode", description="Código do Cargo do Funcionário"
    )
    employee_position_code_internal_id: (
        str | None
    ) = Field(None, alias="employeePositionCodeInternalId", description="InternalId do Cargo do Funcionário")
    employee_position_description: (
        str | None
    ) = Field(None, alias="employeePositionDescription", description="Descrição do Cargo do Funcionário")
    salary_category: str | None = Field(
        None,
        alias="salaryCategory",
        description="Categoria Salarial. Rever estas categorias quando  for utilizar com o RM. Produto Datasul também possui outras categorias (Semana, Quinzenal e Diarista)",
    )
    work_shift_code: str | None = Field(None, alias="workShiftCode", description="Turno de Trabalho")
    work_shift_internal_id: str | None = Field(
        None, alias="workShiftInternalId", description="InternalId do Turno de Trabalho"
    )
    workshift_description: str | None = Field(
        None, alias="workshiftDescription", description="Descrição do Turno de Trabalho"
    )
    work_shift_sequence: str | None = Field(
        None, alias="workShiftSequence", description="Sequência de Turno do funcionário"
    )
    initial_shift_sequence_date: (
        AwareDatetime | None
    ) = Field(None, alias="initialShiftSequenceDate", description="Data Inicial da Sequencia do Turno")
    role_code: str | None = Field(None, alias="roleCode", description="Código da Função do Funcionário")
    role_internal_id: str | None = Field(
        None, alias="roleInternalId", description="InternalId do Código da Função do Funcionário"
    )
    role_description: str | None = Field(
        None, alias="roleDescription", description="Descrição da Função do Funcionário"
    )
    role_level: int | None = Field(None, alias="roleLevel", description="Código Nivel Função")
    business_unit: str | None = Field(None, alias="businessUnit", description="Unidade de Negócio")
    clock_in_card: str | None = Field(None, alias="clockInCard", description="Número do cartão ponto do funcionário")
    labor_type: str | None = Field(None, alias="laborType", description="Tipo de Mão de obra")
    union_code: str | None = Field(None, alias="unionCode", description="Código do Sindicato")
    work_group_code: str | None = Field(None, alias="workGroupCode", description="Turma  de Trabalho")
    employee_class_code: int | None = Field(
        None, alias="employeeClassCode", description="Código da classe de funcionários para ponto eletrônico"
    )
    locality: str | None = Field(None, description="Localidade")
    allocation_plan_code: str | None = Field(None, alias="allocationPlanCode", description="Código do Plano Lotacional")
    country_locality_code: str | None = Field(None, alias="countryLocalityCode", description="Pais Localidade")
    work_shift_change_date: AwareDatetime | None = Field(
        None, alias="workShiftChangeDate", description="Deverá ser enviado qdo ocorrer alteraçao de lotaçao de turno"
    )
    time_table_code: int | None = Field(None, alias="timeTableCode", description="Código da jornada")
    carrier_code: int | None = Field(None, alias="carrierCode", description="Codigo do Transportador Rural")
    rural_group_code: str | None = Field(None, alias="ruralGroupCode", description="Codigo Turma Rural")
    contract_end: AwareDatetime | None = Field(
        None, alias="contractEnd", description="Data de término do contrato trabalho/experiência"
    )
    employee_cpf: str | None = Field(None, alias="employeeCpf", description="CPF")
    section_code: str | None = Field(None, alias="sectionCode", description="Código da Seção")
    section_description: str | None = Field(None, alias="sectionDescription", description="Descrição da Seção")
    esocial_category_code: str | None = Field(
        None, alias="esocialCategoryCode", description="Código da Categoria eSocial"
    )
    esocial_category_description: (
        str | None
    ) = Field(None, alias="esocialCategoryDescription", description="Descrição da Categoria eSocial")
    employee_type: str | None = Field(None, alias="employeeType", description="Tipo de Funcionário")
    private_citizen: str | None = Field(None, alias="privateCitizen", description="Número da Pessoa Física")
    registration_digit: str | None = Field(
        None, alias="registrationDigit", description="Dígito Verificador do Funcionário"
    )
    transference_admission_date: (
        AwareDatetime | None
    ) = Field(None, alias="transferenceAdmissionDate", description="Data de Transferência")
    date_of_salary_change: AwareDatetime | None = Field(
        None, alias="dateOfSalaryChange", description="Data de alteração salarial"
    )
    email: str | None = Field(None, description="Email do funcionário")
    monthly_working_hours: int | None = Field(
        None, alias="monthlyWorkingHours", description="Jornada de trabalho mensal (número de horas)"
    )
    wage_table_internal_id: str | None = Field(
        None, alias="wageTableInternalId", description="Tabela de Faixa do Funcionario"
    )
    type_of_salary_change: str | None = Field(
        None, alias="typeOfSalaryChange", description="Tipo da Alteração Salarial"
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


class PagedEmployeeDataContent(Paging):
    total: int | None = Field(None, examples=["1"])
    employees: list[EmployeeDataContentItem] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
