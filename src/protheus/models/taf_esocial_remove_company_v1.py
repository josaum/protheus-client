"""TAF e-Social - Remover empregador da base de dados do RET — generated from TAFEsocialRemoveCompany_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class Return(BaseModel):
    status_message: str = Field(
        ...,
        alias="statusMessage",
        description="Mensagem de retorno do processo",
        examples=["Transmissão efetuada com sucesso. Verifique o retorno da transmissão através da opção 'Detalhamento', selecionando o evento S-1000. Se a situação do evento for 'Evento Rejeitado', consulte sua inconsistência. Se o código da inconsistência for '1012', execute a rotina 'Exclusão por Período Fiscal' para remover os dados da base do TAF."],
        max_length=9999,
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


class PagedItens(Paging):
    items: list[Return] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass
