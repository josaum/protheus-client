"""Candidato — generated from Candidates_v2_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Base64Str, BaseModel, Field


class CandidateSave(BaseModel):
    id: str | None = Field(None, description="Código do Candidato")
    company_id: str | None = Field(None, alias="companyId", description="Código da Empresa/Coligada", examples=["1"])
    role_id: str | None = Field(None, alias="roleId", description="Código do Cargo/Função", examples=["00001"])
    department_id: str | None = Field(
        None, alias="departmentId", description="Código do Departamento/Seção", examples=["01.01"]
    )
    branch_id: str | None = Field(None, alias="branchId", description="Código da Filial", examples=["01 ou D MG 01"])
    name: str | None = Field(None, description="Nome da Pessoa", examples=["João Pereira da Silva"])
    birth: Any | None = Field(None, description="Data de aniversário da Pessoa", examples=["1975-05-26 00:00:00"])
    home_state: str | None = Field(None, alias="homeState", description="Estado natal da pessoa", examples=["MG"])
    naturalness: str | None = Field(None, description="Naturalidade da Pessoa", examples=["Belo Horizonte"])
    nick_name: str | None = Field(None, alias="nickName", description="Apelido da Pessoa", examples=["Jão"])
    sex: str | None = Field(None, description="Sexo da pessoa", examples=["M"])
    nationality: str | None = Field(None, description="Nacionalidade da pessoa", examples=["10"])
    educational_level: str | None = Field(
        None, alias="educationalLevel", description="Grau de instrução da pessoa", examples=["9"]
    )
    street: str | None = Field(None, description="Rua do endereço da pessoa", examples=["Rua Mata Atlantica"])
    number: str | None = Field(None, description="Número da casa da pessoa", examples=["333"])
    district: str | None = Field(None, description="Bairro do endereço da pessoa", examples=["Planalto"])
    state: str | None = Field(None, description="Estado do endereço da pessoa", examples=["MG"])
    city: str | None = Field(None, description="Cidade do endereço da pessoa", examples=["Belo Horizonte"])
    cep: str | None = Field(None, description="Cep do endereço da pessoa", examples=["30100020"])
    country: str | None = Field(None, description="País do endereço da pessoa", examples=["Brasil"])
    professional_registration_number: (
        str | None
    ) = (
        Field(None, alias="professionalRegistrationNumber", description="Registro Profissional da pessoa", examples=["Reg-00098"])
    )
    cpf: str | None = Field(None, description="CPF da pessoa", examples=["51427362653"])
    image_id: int | None = Field(None, alias="imageId", description="Identificador da imagem da pessoa", examples=[844])
    phone_number1: str | None = Field(
        None, alias="phoneNumber1", description="Número de telefone 1 da pessoa", examples=["4613636"]
    )
    phone_number2: str | None = Field(
        None, alias="phoneNumber2", description="Número de telefone 2 da pessoa", examples=["4613636"]
    )
    identity_number: str | None = Field(
        None, alias="identityNumber", description="Identidade da pessoa", examples=["M 267392"]
    )
    identity_number_emitter_state: (
        str | None
    ) = (
        Field(None, alias="identityNumberEmitterState", description="Estado emissor da identidade da pessoa", examples=["MG"])
    )
    identity_number_emitter_agency: (
        str | None
    ) = (
        Field(None, alias="identityNumberEmitterAgency", description="Orgão emissor da identidade da pessoa", examples=["SSP"])
    )
    identity_number_emission_date: (
        Any | None
    ) = (
        Field(None, alias="identityNumberEmissionDate", description="Data de emissão da identidade da pessoa", examples=["1975-05-26 00:00:00"])
    )
    electoral_card: str | None = Field(
        None, alias="electoralCard", description="Titulo de eleitor da pessoa", examples=["123.334"]
    )
    electoral_ward: str | None = Field(
        None, alias="electoralWard", description="Zona eleitoral da pessoa", examples=["0012"]
    )
    electoral_section: str | None = Field(
        None, alias="electoralSection", description="Seção eleitoral da pessoa", examples=["0006"]
    )
    work_card: str | None = Field(
        None, alias="workCard", description="Carteira de trabalho da pessoa", examples=["015116"]
    )
    work_card_serial_number: str | None = Field(
        None,
        alias="workCardSerialNumber",
        description="Número de série da carteira de trabalho da pessoa",
        examples=["00001"],
    )
    work_card_emitter_state: str | None = Field(
        None,
        alias="workCardEmitterState",
        description="Estado emissor da carteira de trabalho da pessoa",
        examples=["MG"],
    )
    work_card_emission_date: Any | None = Field(
        None,
        alias="workCardEmissionDate",
        description="Data de emissão da carteira de trabalho da pessoa",
        examples=["1975-05-26 00:00:00"],
    )
    nit: bool | None = Field(None, description="Indicador de carteira tipo NIT da pessoa", examples=[0])
    drivers_license: str | None = Field(
        None, alias="driversLicense", description="Carteira de habilitação da pessoa", examples=["13.344.543"]
    )
    drivers_license_type: str | None = Field(
        None, alias="driversLicenseType", description="Tipo de carteira de habilitação da pessoa", examples=["A"]
    )
    drivers_license_expiration_date: (
        Any | None
    ) = (
        Field(None, alias="driversLicenseExpirationDate", description="Data de vencimento da carteira de habilitação da pessoa", examples=["1975-05-26 00:00:00"])
    )
    military_discharge_certificate: (
        str | None
    ) = (
        Field(None, alias="militaryDischargeCertificate", description="Certificado de reservista militar da pessoa", examples=["12856945678"])
    )
    military_grade: str | None = Field(
        None, alias="militaryGrade", description="Categoria militar da pessoa", examples=["CDI"]
    )
    brazil_consort: bool | None = Field(
        None, alias="brazilConsort", description="Indicador para caso a pessoa tenha um conjuge no Brasil", examples=[0]
    )
    naturalized: bool | None = Field(None, description="Indicador caso a pessoa seja naturalizada", examples=[0])
    brazilian_children: bool | None = Field(
        None, alias="brazilianChildren", description="Indicador caso a pessoa tenha filhos brasileiros", examples=[0]
    )
    brazilian_children_number: (
        int | None
    ) = (
        Field(None, alias="brazilianChildrenNumber", description="Números de filhos brasileiros da pessoa", examples=["2"])
    )
    email: str | None = Field(None, description="Email da pessoa", examples=["teste@totvs.com.br"])
    previous_training_investment: (
        Any | None
    ) = (
        Field(None, alias="previousTrainingInvestment", description="Valor de investimentos em treinamentos anteriores da pessoa", examples=["2300.00"])
    )
    shade_race: int | None = Field(None, alias="shadeRace", description="Raça ou Cor da pessoa", examples=["0"])
    disabled: bool | None = Field(None, description="Indicador para pessoa deficiente física", examples=[0])
    user_code: str | None = Field(
        None, alias="userCode", description="Código de usuário da pessoa", examples=["simone"]
    )
    phone_number3: str | None = Field(
        None, alias="phoneNumber3", description="Telefone 3 da pessoa", examples=["21229000"]
    )
    company: str | None = Field(None, description="Empresa da pessoa", examples=["RM SISTEMAS S.A"])
    occupation_code: str | None = Field(
        None, alias="occupationCode", description="Código de ocupação da pessoa", examples=["10"]
    )
    rehabilitated: bool | None = Field(None, description="Indicador de pessoa reabilitada", examples=[0])
    smoker: bool | None = Field(None, description="Indicador de pessoa fumante", examples=[0])
    adjusts_image_size: bool | None = Field(
        None, alias="adjustsImageSize", description="Indicador de ajuste do tamanho da foto da pessoa", examples=[0]
    )
    deaf_person: bool | None = Field(
        None, alias="deafPerson", description="Indicador de pessoa deficiente auditiva", examples=[0]
    )
    mute_person: bool | None = Field(
        None, alias="mutePerson", description="Indicador de pessoa deficiente de fala", examples=[0]
    )
    blind_person: bool | None = Field(
        None, alias="blindPerson", description="Indicador de pessoa deficiente visual", examples=[0]
    )
    mentally_impaired_person: bool | None = Field(
        None, alias="mentallyImpairedPerson", description="Indicador de pessoa com deficiencia mental", examples=[0]
    )
    curriculum_approval_date: Any | None = Field(
        None,
        alias="curriculumApprovalDate",
        description="Data de aprovação do currículo da pessoa",
        examples=["1975-05-26 00:00:00"],
    )
    student: bool | None = Field(None, description="Indicador de pessoa estudante", examples=[1])
    teacher: bool | None = Field(None, description="Indicador de pessoa professor", examples=[1])
    candidate: bool | None = Field(None, description="Indicador de pessoa candidato", examples=[1])
    biblios_user: bool | None = Field(
        None, alias="bibliosUser", description="Indicador de pessoa usuária da ferramenta Biblios", examples=[1]
    )
    employee: bool | None = Field(None, description="Indicador de pessoa funcionária", examples=[1])
    former_employee: bool | None = Field(
        None, alias="formerEmployee", description="Indicador de pessoa ex-funcionária", examples=[0]
    )
    intellectual_impaired_person: (
        bool | None
    ) = (
        Field(None, alias="intellectualImpairedPerson", description="Indicador de pessoa com deficiencia intelectual", examples=[0])
    )
    deceased: bool | None = Field(None, description="Indicador de pessoa falecida", examples=[0])
    age: int | None = Field(None, description="idade da pessoa", examples=[53])
    registry_date: Any | None = Field(
        None, alias="registryDate", description="Data de cadastramento", examples=["1975-05-26 00:00:00"]
    )
    wage_expectation: float | None = Field(
        None, alias="wageExpectation", description="Pretenção salarial", examples=["1111.32"]
    )
    area_of_interest_code1: int | None = Field(
        None, alias="areaOfInterestCode1", description="Código da área de interesse 1", examples=["15"]
    )
    area_of_interest_code2: int | None = Field(
        None, alias="areaOfInterestCode2", description="Código da área de interesse 2", examples=["15"]
    )
    wage_expectation_tradable: (
        int | None
    ) = Field(None, alias="wageExpectationTradable", description="Pretenção salaria negociável", examples=["1"])
    work_experience_time: int | None = Field(
        None, alias="workExperienceTime", description="Tempo de experiência profissional", examples=["15"]
    )
    work_experience_time_area1: (
        int | None
    ) = (
        Field(None, alias="workExperienceTimeArea1", description="Tempo de experiência profissional na área de interesse 1", examples=["15"])
    )
    work_experience_time_area2: (
        int | None
    ) = (
        Field(None, alias="workExperienceTimeArea2", description="Tempo de experiência profissional na área de interesse 2", examples=["15"])
    )
    contra_indicated: int | None = Field(None, alias="contraIndicated", description="É contraindicado?", examples=["1"])
    contraindication_reason: str | None = Field(
        None, alias="contraindicationReason", description="Razão da contraindicação"
    )
    available: int | None = Field(None, description="Que participar do processo seletivo?", examples=["1"])
    form_of_recruitment: str | None = Field(None, alias="formOfRecruitment", description="Forma de contratação")
    resume_skills_id: int | None = Field(
        None, alias="resumeSkillsId", description="ID do resumo da qualificação do candidato", examples=["15"]
    )
    hierarchy_level_code: int | None = Field(
        None, alias="hierarchyLevelCode", description="Código do nível hierárquico", examples=["15"]
    )
    professional_profile_description: (
        str | None
    ) = Field(None, alias="professionalProfileDescription", description="Descrição do perfil profissional")
    area_of_interest_description1: (
        str | None
    ) = Field(None, alias="areaOfInterestDescription1", description="Descrição da áre de interesse 1")
    area_of_interest_description2: (
        str | None
    ) = Field(None, alias="areaOfInterestDescription2", description="Descrição da áre de interesse 2")
    hierarchy_level_description: (
        str | None
    ) = Field(None, alias="hierarchyLevelDescription", description="Descrição do nível hierárquico")
    professional_skills_resume_description: (
        str | None
    ) = Field(None, alias="professionalSkillsResumeDescription", description="Descrição do resumo de qualificações")
    employee1: str | None = Field(None, description="Funcionário")
    personal_email: str | None = Field(None, alias="personalEmail", description="Email Pessoal")
    marital_state: str | None = Field(None, alias="maritalState", description="Estado Civil")
    complement: str | None = Field(None, description="Estado Civil")
    arrival_date: Any | None = Field(
        None, alias="arrivalDate", description="Data de Chegada ao Brasil", examples=["1975-05-26 00:00:00"]
    )
    letter_model19: str | None = Field(None, alias="letterModel19", description="Carta modelo 19")
    rne: str | None = Field(None, description="Registro Geral - RNE")
    immigration_decree: str | None = Field(None, alias="immigrationDecree", description="Decreto de Imigração")
    rne_expiration_date: Any | None = Field(
        None, alias="rneExpirationDate", description="Data de Venc. RNE", examples=["1975-05-26 00:00:00"]
    )
    work_card_expiration_date: (
        Any | None
    ) = (
        Field(None, alias="workCardExpirationDate", description="Data de Venc. Carteira Trabalho", examples=["1975-05-26 00:00:00"])
    )
    visa_type: str | None = Field(None, alias="visaType", description="Tipo de Visto")
    passport_number: str | None = Field(None, alias="passportNumber", description="Número do Passaporte")
    native_country: str | None = Field(None, alias="nativeCountry", description="País de origem")
    passport_expiration_date: Any | None = Field(
        None, alias="passportExpirationDate", description="Data Validade Passaporte", examples=["1975-05-26 00:00:00"]
    )
    accessibility_features_for_job_local: (
        str | None
    ) = (
        Field(None, alias="accessibilityFeaturesForJobLocal", description="Recursos p/ acessibilidade ao local de trabalho")
    )
    military_division: str | None = Field(None, alias="militaryDivision", description="CSM")
    military_certificate_emission_date: (
        Any | None
    ) = (
        Field(None, alias="militaryCertificateEmissionDate", description="Data Emissão C.Militar", examples=["1975-05-26 00:00:00"])
    )
    military_certificate_emitter_agency: (
        str | None
    ) = Field(None, alias="militaryCertificateEmitterAgency", description="Orgão de Expedição")
    military_region: str | None = Field(None, alias="militaryRegion", description="Região militar")
    military_situation: str | None = Field(None, alias="militarySituation", description="Situação Militar")
    electoral_card_emitter_state: (
        str | None
    ) = Field(None, alias="electoralCardEmitterState", description="Est. Emissor Tit. Eleitor")
    blood_type: str | None = Field(None, alias="bloodType", description="Tipo sanguíneo")
    image: Base64Str | None = Field(None, description="Imagem")
    neighborhood_type_code: int | None = Field(
        None, alias="neighborhoodTypeCode", description="Cód. Tipo Bairro", examples=["15"]
    )
    naturalness_code: str | None = Field(None, alias="naturalnessCode", description="Tipo sanguíneo")
    naturalisation_date: Any | None = Field(
        None, alias="naturalisationDate", description="Data de Naturalização", examples=["1975-05-26 00:00:00"]
    )
    drivers_license_emitter_agency: (
        str | None
    ) = Field(None, alias="driversLicenseEmitterAgency", description="Orgão Emissor CNH")
    rne_emitter_agency: str | None = Field(None, alias="rneEmitterAgency", description="Orgão e UF Emissor RNE")
    country_id: int | None = Field(None, alias="countryId", description="Id Pais", examples=["1"])
    decease_date: Any | None = Field(
        None, alias="deceaseDate", description="Data de falecimento", examples=["1975-05-26 00:00:00"]
    )
    death_certificate_number: str | None = Field(
        None, alias="deathCertificateNumber", description="Matrícula da Certidão de Óbito"
    )
    naturalisation_gatehouse: str | None = Field(
        None, alias="naturalisationGatehouse", description="Portaria de Naturalização"
    )
    brazil_condition_classification: (
        str | None
    ) = Field(None, alias="brazilConditionClassification", description="Portaria de Naturalização")
    drivers_license_first_emission_date: (
        Any | None
    ) = (
        Field(None, alias="driversLicenseFirstEmissionDate", description="Data Primeira CNH", examples=["1975-05-26 00:00:00"])
    )
    first_job_year: int | None = Field(
        None, alias="firstJobYear", description="Ano do Primeiro Emprego", examples=["15"]
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


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CandidateInfo(CandidateSave):
    code: int | None = Field(None, alias="Code", description="Código do Candidato", examples=["1"])
    row_state: int | None = Field(None, alias="RowState", description="Estado da row no Dataserver", examples=["1"])
    valid_row: int | None = Field(None, alias="ValidRow", description="Se o registro foi validado", examples=["1"])


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class CandidateGroups(Paging):
    items: CandidateInfo | None = None
