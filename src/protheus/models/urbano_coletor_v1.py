"""Coletor — generated from UrbanoColetor_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, BaseModel, Field


class RequestItens(BaseModel):
    layout_coletor: dict[str, Any] | None = Field(None, alias="layoutColetor")
    cabecalho: dict[str, Any] | None = None
    servicos: list[Any] | None = None


class LayoutColetor(BaseModel):
    software_coletor: str = Field(
        ...,
        alias="softwareColetor",
        description="Descrição do software coletor",
        examples=["Software x"],
        max_length=15,
    )
    versao_coletor: str = Field(
        ..., alias="versaoColetor", description="Versão do coletor", examples=["2.0"], max_length=15
    )


class Cabecalho(BaseModel):
    empresa: str = Field(..., description="Código da empresa", examples=["02"], max_length=15)
    mat_motorista: str = Field(
        ..., alias="matMotorista", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    cartao_motorista: str = Field(
        ..., alias="cartaoMotorista", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    mat_cobrador: bool = Field(
        ..., alias="matCobrador", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    cartao_cobrador: bool = Field(
        ..., alias="cartaoCobrador", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    data_movimento: bool = Field(
        ..., alias="dataMovimento", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    filipeta: bool = Field(..., description="Permissão do Evento.", examples=["true"], max_length=15)


class Servicos(BaseModel):
    cod_servico: bool = Field(
        ..., alias="codServico", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    cod_veiculo: bool = Field(
        ..., alias="codVeiculo", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    prefixo_linha: bool = Field(
        ..., alias="prefixoLinha", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    codigo_linha: bool = Field(
        ..., alias="codigoLinha", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    turno: bool = Field(..., description="Permissão do Evento.", examples=["true"], max_length=15)
    data_inicio_viagem: bool = Field(
        ..., alias="dataInicioViagem", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    data_termino_viagem: bool = Field(
        ..., alias="dataTerminoViagem", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    hr_inicio: bool = Field(..., alias="hrInicio", description="Permissão do Evento.", examples=["true"], max_length=15)
    hr_fim: bool = Field(..., alias="hrFim", description="Permissão do Evento.", examples=["true"], max_length=15)
    roleta_inicio_validador: bool = Field(
        ..., alias="roletaInicioValidador", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    roleta_fim: bool = Field(
        ..., alias="roletaFim", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    tipo_pagamento: bool = Field(
        ..., alias="tipoPagamento", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    quantidade_passageiros: bool = Field(
        ..., alias="quantidadePassageiros", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    valor_unitario: bool = Field(
        ..., alias="valorUnitario", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    total_arrecadado: bool = Field(
        ..., alias="totalArrecadado", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    total_gratuidades: bool = Field(
        ..., alias="totalGratuidades", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    total_dinheiro: bool = Field(
        ..., alias="totalDinheiro", description="Permissão do Evento.", examples=["true"], max_length=15
    )
    diferenca: bool = Field(..., description="Permissão do Evento.", examples=["true"], max_length=15)


class RespostaColetor(BaseModel):
    status: str | None = Field(None, description="Status de retorno", examples=["success"], max_length=7)
    prestacao_contas: str | None = Field(
        None,
        alias="prestacaoContas",
        description="Código da prestação de contas incluida",
        examples=["000014"],
        max_length=6,
    )
    message: str | None = Field(
        None, description="Mensagem de sucesso", examples=["Prestação de contas incluída com sucesso"], max_length=30
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


class ResponseItens(BaseModel):
    items: list[RespostaColetor] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
