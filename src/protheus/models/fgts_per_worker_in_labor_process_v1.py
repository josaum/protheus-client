"""Evento Totalizador S-5503 — generated from FGTSPerWorkerInLaborProcess_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class FGTSPerWorkerInLaborProcessList(BaseModel):
    company_id: str = Field(
        ...,
        alias="companyId",
        description="Código da Empresa e Código da Filial",
        examples=["T1|D MG 01"],
        max_length=8,
    )
    period: str = Field(..., description="Período (Mês-Dia)", examples=["2023-08"], max_length=7)
    process_number: str = Field(
        ..., alias="processNumber", description="Número do Processo Trabalhista", examples=["00010434"], max_length=20
    )
    cpf: str = Field(..., description="CPF do Funcionário", examples=["82977978054"], max_length=11)
    name: str | None = Field(None, description="Nome do Funcionário", examples=["Alex André"], max_length=100)
    id: str = Field(..., description="Identificador Único do Evento S-5503", examples=["00010434"], max_length=8)
    receipt: str = Field(
        ..., description="Recibo de Protocolo e-Social", examples=["1.2.0000000000195474657"], max_length=8
    )


class InvalidRequest(BaseModel):
    code: float = Field(..., description="Código identificador do erro", examples=[400], max_length=3)
    message: str = Field(
        ...,
        description="Literal no idioma da requisição descrevendo o erro para o cliente",
        examples=["Empresa|Filial não informado no parâmetro 'companyId'."],
        max_length=100,
    )
    detailed_message: str | None = Field(
        None,
        alias="detailedMessage",
        description="Mensagem técnica e mais detalhada do erro",
        examples=[""],
        max_length=200,
    )


class InternalServerError(BaseModel):
    code: float = Field(..., description="Código identificador do erro", examples=[500], max_length=3)
    message: str = Field(
        ...,
        description="Literal no idioma da requisição descrevendo o erro para o cliente",
        examples=["O Servidor recebeu sua requisição, porém ocorreu um erro ao processar sua solicitação"],
        max_length=100,
    )
    detailed_message: str | None = Field(
        None,
        alias="detailedMessage",
        description="Mensagem técnica e mais detalhada do erro",
        examples=["Favor verificar arquivos de log do seu servidor"],
        max_length=200,
    )


class Id(RootModel[str]):
    root: str = Field(..., description="Identificador Único do Evento S-5503", examples=["00010434"], max_length=8)


class NotFound(BaseModel):
    code: float = Field(..., description="Código identificador do erro", examples=[404], max_length=3)
    message: str = Field(
        ...,
        description="Literal no idioma da requisição descrevendo o erro para o cliente",
        examples=["Não foram encontrados registros do evento S-5503 com os ID's informados"],
        max_length=100,
    )
    detailed_message: str | None = Field(
        None,
        alias="detailedMessage",
        description="Mensagem técnica e mais detalhada do erro",
        examples=["Favor verificar companyId e/ou ID's informados"],
        max_length=200,
    )


class FGTSPerWorkerInLaborProcessXMLList(BaseModel):
    id: str = Field(..., description="Identificador Único do Evento S-5503", examples=["00010434"], max_length=8)
    xml: str = Field(
        ...,
        description="XML (encode base64)",
        examples=["PGh0bWwgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiCiAgPGJvZHk+CiAgICA8cGFyc2VyZXJyb3Igc3R5bGU9ImRpc3BsYXk6IGJsb2NrOyB3aGl0ZS1zcGFjZTogcHJlOyBib3JkZXI6IDJweCBzb2xpZCAjYzc3OyBwYWRkaW5nOiAwIDFlbSAwIDFlbTsgbWFyZ2luOiAxZW07IGJhY2tncm91bmQtY29sb3I6ICNmZGQ7IGNvbG9yOiBibGFjayI+CiAgICAgIDxoMz5UaGlzIHBhZ2UgY29udGFpbnMgdGhlIGZvbGxvd2luZyBlcnJvcnM6PC9oMz4KICAgICAgPGRpdiBzdHlsZT0iZm9udC1mYW1pbHk6bW9ub3NwYWNlO2ZvbnQtc2l6ZToxMnB4Ij5lcnJvciBvbiBsaW5lIDIgYXQgY29sdW1uIDM6IGVycm9yIHBhcnNpbmcgYXR0cmlidXRlIG5hbWUKPC9kaXY+CiAgICAgIDxoMz5CZWxvdyBpcyBhIHJlbmRlcmluZyBvZiB0aGUgcGFnZSB1cCB0byB0aGUgZmlyc3QgZXJyb3IuPC9oMz4KICAgIDwvcGFyc2VyZXJyb3I+CiAgPC9ib2R5Pgo8L2h0bWw+"],
    )


class FGTSPerWorkerInLaborProcessWorkerRegistrationAndCategoryList(BaseModel):
    company_id: str = Field(
        ...,
        alias="companyId",
        description="Código da Empresa e Código da Filial",
        examples=["T1|D MG 01"],
        max_length=8,
    )
    id: str = Field(..., description="Identificador Único do Evento S-5503", examples=["00010434"], max_length=8)
    registration: str = Field(..., description="Matrícula do Funcionário", examples=["MAT_42227624078"], max_length=50)
    category: str = Field(..., description="Categoria do Funcionário", examples=["101"], max_length=3)
    origin_category: str = Field(
        ..., alias="originCategory", description="Categoria de Origem do Funcionário", examples=["101"], max_length=3
    )
    fgts_tot: float = Field(..., alias="fgtsTot", description="Total de FGTS", examples=["27000.15"], max_length=16)
    type_of_inscription: str = Field(
        ..., alias="typeOfInscription", description="Tipo de Inscrição do Funcionário", examples=["1"], max_length=1
    )
    registration_number: str = Field(
        ...,
        alias="registrationNumber",
        description="Número de Inscrição do Funcionário",
        examples=["53113791"],
        max_length=20,
    )


class FGTSPerWorkerInLaborProcessWorkerPaymentAndAmountsList(BaseModel):
    id: str = Field(..., description="Identificador Único do Evento S-5503", examples=["00010434"], max_length=8)
    reference_period: str = Field(
        ..., alias="referencePeriod", description="Período de Referência", examples=["2023-12"], max_length=7
    )
    category: str = Field(..., description="Categoria do Funcionário", examples=["101"], max_length=3)
    type_of_labor_process_value: float = Field(
        ...,
        alias="typeOfLaborProcessValue",
        description="Tipo do valor do Processo Trabalhista",
        examples=["71"],
        max_length=2,
    )
    rem_fgts_proc_trab: float = Field(
        ...,
        alias="remFGTSProcTrab",
        description="Valor histórico sobre base reconhecida",
        examples=["59000.99"],
        max_length=16,
    )
    rem_fgts_sefip: float = Field(
        ...,
        alias="remFGTSSefip",
        description="Valor base Sefip ainda não recolhida",
        examples=["845.00"],
        max_length=16,
    )
    dps_fgts_sefip: float = Field(
        ...,
        alias="dpsFGTSSefip",
        description="Valor de base já declarada na Segip",
        examples=["23500.45"],
        max_length=16,
    )
    rem_fgts_dec_ant: float = Field(
        ...,
        alias="remFGTSDecAnt",
        description="Valor de base declarado no eSocial e não recolhido",
        examples=["5015.19"],
        max_length=16,
    )
    dps_fgts_dec_ant: float = Field(
        ...,
        alias="dpsFGTSDecAnt",
        description="Valor Histórico sobre base já declarada no eSocial",
        examples=["23055.45"],
        max_length=16,
    )


class FGTSPerWorkerInLaborProcessItems(Paging):
    items: list[FGTSPerWorkerInLaborProcessList] | None = None


class RecordsToSelect(BaseModel):
    company_id: str = Field(
        ...,
        alias="companyId",
        description="Código da Empresa e Código da Filial",
        examples=["T1|D MG 01"],
        max_length=8,
    )
    id: list[Id] = Field(..., description="Relação de ID's de S-5503")


class FGTSPerWorkerInLaborProcessXMLItems(Paging, FGTSPerWorkerInLaborProcessXMLList):
    pass


class FGTSPerWorkerInLaborProcessWorkerRegistrationAndCategoryItems(Paging):
    items: list[FGTSPerWorkerInLaborProcessWorkerRegistrationAndCategoryList] | None = None


class FGTSPerWorkerInLaborProcessWorkerPaymentAndAmountsItems(Paging):
    items: list[FGTSPerWorkerInLaborProcessWorkerPaymentAndAmountsList] | None = None
