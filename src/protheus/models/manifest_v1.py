"""Manifest — generated from Manifest_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Situation(StrEnum):
    field_1___digitado = "1 - Digitado"
    field_2___emitido = "2 - Emitido"
    field_3___liberado = "3 - Liberado"
    field_4___encerrado = "4 - Encerrado"


class CalculationStatus(StrEnum):
    field_1___calculado_com_sucesso = "1 - Calculado com Sucesso"
    field_2___não_calculado = "2 - Não Calculado"
    field_3___tentativa_sem_sucesso = "3 - Tentativa sem Sucesso"
    field_4___necessita_recálculo = "4 - Necessita Recálculo"


class Source(StrEnum):
    field_1___1_usuário = "1 - 1=Usuário"
    field_2___erp = "2 - ERP"
    field_3___outros = "3 - Outros"
    field_4___sistema = "4 - Sistema"


class TollVoucher(StrEnum):
    field_1___não_se_aplica = "1 - Não se aplica"
    field_2___não_conferido = "2 - Não Conferido"
    field_3___conferido = "3 - Conferido"


class Manifest(BaseModel):
    internal_id: str | None = Field(
        None, alias="InternalId", description="Chave do romaneio.", examples=["01|00000001"]
    )
    branch_id: str | None = Field(None, alias="BranchId", description="Filial do Sistema", examples=["99"])
    manifest_number: str | None = Field(
        None, alias="ManifestNumber", description="Número do Romaneio.", examples=["00000001"]
    )
    oper_type: str | None = Field(None, alias="OperType", description="Tipo de Operação.", examples=["0000000001"])
    freight_clas: str | None = Field(None, alias="FreightClas", description="Classificação do Frete.", examples=["001"])
    carrier: str | None = Field(None, alias="Carrier", description="Código do Transportador.", examples=["000010"])
    driver: str | None = Field(None, alias="Driver", description="Código do Motorista.", examples=["000001"])
    driver2: str | None = Field(None, alias="Driver2", description="Código do Motorista 2.", examples=["000002"])
    vehicle_type: str | None = Field(None, alias="VehicleType", description="Tipo do Veículo.", examples=["000003"])
    front_licence_plate: str | None = Field(
        None, alias="FrontLicencePlate", description="Placa de Veículo Dianteiro.", examples=["MJX-0001"]
    )
    rear_licence_plate: str | None = Field(
        None, alias="RearLicencePlate", description="Placa de Veículo Traseiro.", examples=["MJX-0002"]
    )
    intermediate_lic_plate: str | None = Field(
        None, alias="IntermediateLicPlate", description="Placa de Veículo Meio.", examples=["MJX-0003"]
    )
    situation: Situation | None = Field(None, alias="Situation", description="Situação do Romaneio.", examples=["1"])
    manifest_creation_date: str | None = Field(
        None, alias="ManifestCreationDate", description="Data de Criação.", examples=["2019-10-10"]
    )
    creation_hour: str | None = Field(None, alias="CreationHour", description="Hora de Criação.", examples=["10:00"])
    calculation_status: CalculationStatus | None = Field(
        None, alias="CalculationStatus", description="Situação do Cálculo.", examples=["1"]
    )
    calculation_date: str | None = Field(
        None, alias="CalculationDate", description="Data do Cálculo.", examples=["2020-08-08"]
    )
    calculation_hour: str | None = Field(
        None, alias="CalculationHour", description="Hora do Cálculo.", examples=["11:11"]
    )
    user: str | None = Field(None, alias="User", description="Usuário de Criação do Romaneio.", examples=["admin"])
    source: Source | None = Field(None, alias="Source", description="Origem.", examples=["1"])
    outflow_inflow_dt: str | None = Field(
        None, alias="OutflowInflowDt", description="Data de Saída/Entrada.", examples=["2020-08-08"]
    )
    outflow_inflow_hr: str | None = Field(
        None, alias="OutflowInflowHr", description="Hora da Saída/Entrada.", examples=["11:11"]
    )
    route: str | None = Field(None, alias="Route", description="Percurso.", examples=["0001"])
    destiny_city: str | None = Field(None, alias="DestinyCity", description="Cidade Destino.", examples=["01000"])
    destin_postal_code: str | None = Field(
        None, alias="DestinPostalCode", description="CEP Destino.", examples=["89203-300"]
    )
    return_date: str | None = Field(None, alias="ReturnDate", description="Data Retorno.", examples=["2020-07-07"])
    return_time: str | None = Field(None, alias="ReturnTime", description="Hora Retorno.", examples=["09:00"])
    departure_odometer_readin: (
        str | None
    ) = Field(None, alias="DepartureOdometerReadin", description="Hodômetro Saída.", examples=["101500"])
    return_odometer_reading: str | None = Field(
        None, alias="ReturnOdometerReading", description="Hodômetro Retorno.", examples=["102709"]
    )
    tracing_code: str | None = Field(None, alias="TracingCode", description="Código Rastreamento.", examples=["102709"])
    toll_amount: str | None = Field(
        None, alias="TollAmount", description="Valor Pedágio.", examples=["48,00"], ge=0, le=99999.99
    )
    toll_voucher: TollVoucher | None = Field(None, alias="TollVoucher", description="Vale Pedágio.", examples=["1"])
    serial_number: str | None = Field(None, alias="SerialNumber", description="Número do Lacre.", examples=["00011"])
    trip_number: str | None = Field(None, alias="TripNumber", description="Viagem.", examples=["00000500"])


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class PagedManifest(Paging):
    items: list[Manifest] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
