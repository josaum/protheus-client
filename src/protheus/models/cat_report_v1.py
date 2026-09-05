"""Painel de Impressão da CAT — generated from CatReport_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class CatReportList(BaseModel):
    request_id: str | None = Field(
        None,
        alias="requestId",
        description="Identificador da Requisição de Processamento",
        examples=["885ebca6-d865-cea7-de62-e7812e946336"],
        max_length=36,
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


class ListStatus(BaseModel):
    finished: bool | None = Field(None, description="Finalizado", examples=["true"], max_length=10)
    percent: str | None = Field(None, description="Percentual", examples=["100%"], max_length=20)


class CatListValue(BaseModel):
    branch: str | None = Field(None, description="Código da filial", examples=["D MG 01 "], max_length=8)
    cat_number: str | None = Field(
        None, alias="catNumber", description="Número da CAT", examples=["1.2.0000000000145721641"], max_length=23
    )
    categ_code: str | None = Field(
        None, alias="categCode", description="Código da Categoria", examples=["101"], max_length=3
    )
    accident_date: str | None = Field(
        None, alias="accidentDate", description="Data do Acidente", examples=["19/07/22"], max_length=8
    )
    accident_time: str | None = Field(
        None, alias="accidentTime", description="Hora do Acidente", examples=["18:04"], max_length=5
    )
    accident_type: str | None = Field(
        None, alias="accidentType", description="Tipo do Acidente", examples=["Trajeto"], max_length=10
    )
    cat_type: str | None = Field(None, alias="catType", description="Tipo da CAT", examples=["Inicial"], max_length=25)
    event_type: str | None = Field(
        None, alias="eventType", description="Tipo do Evento", examples=["Inclusão"], max_length=10
    )
    death_date: str | None = Field(
        None, alias="deathDate", description="Data do Óbito", examples=["19/07/22"], max_length=8
    )
    origin_cat_number: str | None = Field(
        None,
        alias="originCatNumber",
        description="Número da CAT de Origem",
        examples=["1.2.0000000000145721641"],
        max_length=23,
    )
    cpf: str | None = Field(None, description="CPF", examples=["418.615.610-75"], max_length=14)
    name: str | None = Field(None, description="Nome", examples=["ALEXANDRE MARCOS FIGUEIREDO"], max_length=255)
    registration: str | None = Field(None, description="Matrícula", examples=["MATALEXANDRE001"], max_length=30)
    predecessor_type: str | None = Field(
        None, alias="predecessorType", description="Nome do Evento do Trabalhador", examples=["S2200"], max_length=5
    )
    initial_cat: str | None = Field(
        None, alias="initialCat", description="Iniciativa da CAT", examples=["Ordem judicial"], max_length=50
    )
    inscription_type: str | None = Field(
        None, alias="inscriptionType", description="Tipo de inscrição", examples=["CNPJ"], max_length=5
    )
    inscription_number: str | None = Field(
        None, alias="inscriptionNumber", description="Número de Inscrição", examples=["53113791000122"], max_length=14
    )
    social_reason: str | None = Field(
        None, alias="socialReason", description="Razão Social", examples=["TOTVS S.A."], max_length=255
    )
    cnae: str | None = Field(None, description="CNAE", examples=["1543101"], max_length=10)
    gender: str | None = Field(None, description="Gênero sexual", examples=["Feminino"], max_length=10)
    civil_status: str | None = Field(
        None, alias="civilStatus", description="Estado Civil", examples=["Solteiro"], max_length=10
    )
    birth_date: str | None = Field(
        None, alias="birthDate", description="Data de Nascimento", examples=["15/07/87"], max_length=10
    )
    cbo: str | None = Field(
        None,
        description="CBO (Classificação Brasileira de Ocupações)",
        examples=["2521-05 - Analista administrativo"],
        max_length=255,
    )
    area: str | None = Field(None, description="Áreas", examples=["Urbana"], max_length=10)
    work_hour: str | None = Field(
        None, alias="workHour", description="Após quantas horas de trabalho?", examples=["02:00"], max_length=5
    )
    removal: str | None = Field(None, description="Indica se houve afastamento", examples=["Sim"], max_length=3)
    place: str | None = Field(
        None, description="Local do acidente", examples=["Rua do estabelecimento X"], max_length=255
    )
    place_type: str | None = Field(
        None,
        alias="placeType",
        description="Especificação do local do acidente",
        examples=["Estab empreg. Brazil"],
        max_length=255,
    )
    country: str | None = Field(None, description="País", examples=["Brasil"], max_length=50)
    inscription_place: str | None = Field(
        None,
        alias="inscriptionPlace",
        description="CNPJ/CAEPF/ CNO do local do acidente",
        examples=["CNPJ"],
        max_length=5,
    )
    uf: str | None = Field(None, description="UF do local do acidente", examples=["SP"], max_length=2)
    county: str | None = Field(
        None, description="Munícipio do local do acidente", examples=["São Paulo"], max_length=30
    )
    affected_parts: str | None = Field(
        None,
        alias="affectedParts",
        description="Parte do corpo atingida",
        examples=["757030000 - Articulação do tornozelo"],
        max_length=255,
    )
    laterality: str | None = Field(None, description="Lateralidade", examples=["Não aplicável"], max_length=20)
    causer_agent: str | None = Field(
        None,
        alias="causerAgent",
        description="Agente causador",
        examples=["302010200 - Rua e estrada - superfície utilizada para sustentar pessoas"],
        max_length=255,
    )
    situation: str | None = Field(
        None,
        description="Situação geradora do acidente ou doença",
        examples=["200004300 - Impacto de pessoa contra objeto parado"],
        max_length=255,
    )
    police: str | None = Field(None, description="Indica de houve registro policial", examples=["Não"], max_length=3)
    death_sign: str | None = Field(
        None, alias="deathSign", description="Indica se houve morte", examples=["Não"], max_length=3
    )
    note: str | None = Field(
        None,
        description="Observações do acidente ou doença",
        examples=["Caiu de moto e troceu o tornozelo direito"],
        max_length=255,
    )
    service_date: str | None = Field(
        None, alias="serviceDate", description="Data de atendimento", examples=["08/08/22"], max_length=10
    )
    service_hour: str | None = Field(
        None, alias="serviceHour", description="Hora de atendimento", examples=["08:00"], max_length=5
    )
    hospitalization: str | None = Field(None, description="Indica se houve internação", examples=["Sim"], max_length=3)
    treatment_duration: str | None = Field(
        None,
        alias="treatmentDuration",
        description="Provável duração do tratamento (dias)",
        examples=["2"],
        max_length=5,
    )
    lesion: str | None = Field(None, description="Descrição e natureza da lesão", examples=["Luxação"], max_length=255)
    probable_diagnosis: str | None = Field(
        None,
        alias="probableDiagnosis",
        description="Diagnóstico provável",
        examples=["Entorse tornozelo direito"],
        max_length=255,
    )
    code_cid: str | None = Field(
        None,
        alias="codeCid",
        description="Código do CID( Classificação Internacional de Doenças )",
        examples=["A20"],
        max_length=10,
    )
    observation: str | None = Field(
        None, description="Observações do diagnóstico", examples=["Observação do atendimento médico"], max_length=255
    )
    doctor_information: str | None = Field(
        None,
        alias="doctorInformation",
        description="Informações do médico",
        examples=["ANTONIO SOARES, CRM 45657567357374 SP"],
        max_length=255,
    )
    last_day_worked: str | None = Field(
        None, alias="lastDayWorked", description="Último dia trabalhado", examples=["08/08/22"], max_length=10
    )
    there_was_removal: str | None = Field(
        None, alias="thereWasRemoval", description="Houve afastamento", examples=["Sim"], max_length=3
    )
    receiving_date: str | None = Field(
        None, alias="receivingDate", description="Data de recebimento", examples=["08/08/22"], max_length=10
    )
    key: str | None = Field(None, description="Nome do Evento do Trabalhador", examples=["000001"], max_length=6)


class CatReportItems(Paging):
    items: list[CatReportList] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class StatusItems(Paging):
    items: list[ListStatus] | None = None


class CatValuesItems(Paging):
    items: list[CatListValue] | None = None
