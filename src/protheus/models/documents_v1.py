"""Documentos — generated from Documents_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class ListOfKnowledgeItem(BaseModel):
    file_name: str | None = Field(
        None,
        alias="FileName",
        description="Nome do documento na base de conhecimento.",
        examples=["ACE32.DLL"],
        max_length=200,
    )
    file_description: str | None = Field(
        None,
        alias="FileDescription",
        description="Descrição do documento na base de conhecimento.",
        examples=["ACE32"],
        max_length=60,
    )
    file_size_bytes: int | None = Field(
        None, alias="FileSizeBytes", description="Tamanho do documento na base de conecimento.", ge=0, le=999999999999
    )


class ListOfKnowledge(BaseModel):
    pass


class ListOfKeyWord(BaseModel):
    file_search: str | None = Field(
        None,
        alias="FileSearch",
        description="Palavra chave do documento na base de conecimento.",
        examples=["ACE"],
        max_length=20,
    )


class ListOfKeyWords(BaseModel):
    pass


class DocumentInfo(BaseModel):
    company_id: str | None = Field(None, alias="CompanyId", description="Código da empresa", max_length=3)
    branch_id: str | None = Field(
        None, alias="BranchId", description="Código da Filial", examples=["D MG 01"], max_length=12
    )
    company_internal_id: str | None = Field(
        None,
        alias="CompanyInternalId",
        description="Código da Empresa",
        examples=["D MG 01 0000000001SA1D MG 01 000001"],
    )
    internal_id: str | None = Field(
        None, alias="InternalId", description="InternalId da anotação no ERP", examples=["D MG 01 000001"]
    )
    code: str | None = Field(
        None,
        alias="Code",
        description="Código do documento da base de conhecimento.",
        examples=["0000000001"],
        max_length=10,
    )
    entity: str | None = Field(
        None,
        alias="Entity",
        description="Alias da entidade do documento na base de conhecimento.",
        examples=["SA1"],
        max_length=3,
    )
    branch_entity: str | None = Field(
        None, alias="BranchEntity", description="Código da Filial da entidade", examples=["D MG 02"], max_length=12
    )
    entity_code: str | None = Field(
        None,
        alias="EntityCode",
        description="Código da entidade do documento na base de conhecimento.",
        examples=["000001"],
        max_length=70,
    )
    list_of_knowledge: list[ListOfKnowledgeItem] | ListOfKnowledge | None = Field(
        None, alias="ListOfKnowledge", description="Descreve o documento na base de conhecimento"
    )
    list_of_key_words: list[ListOfKeyWord] | ListOfKeyWords | None = Field(
        None, alias="ListOfKeyWords", description="Palavra chave do documento na base de conhecimento."
    )


class ListKnowledgeItem(BaseModel):
    file_name: str | None = Field(
        None,
        alias="FileName",
        description="Nome do documento na base de conhecimento.",
        examples=["ACE32.DLL"],
        max_length=200,
    )
    file_description: str | None = Field(
        None,
        alias="FileDescription",
        description="Descrição do documento na base de conhecimento.",
        examples=["ACE32"],
        max_length=60,
    )
    file_size_bytes: int | None = Field(
        None, alias="FileSizeBytes", description="Tamanho do documento na base de conecimento.", ge=0, le=999999999999
    )


class ListKnowledge(RootModel[list[ListKnowledgeItem]]):
    root: list[ListKnowledgeItem] = Field(..., description="Descreve o documento na base de conhecimento")


class ListKeyWord(BaseModel):
    file_search: str | None = Field(
        None,
        alias="FileSearch",
        description="Palavra chave do documento na base de conecimento.",
        examples=["ACE"],
        max_length=20,
    )


class ListKeyWords(RootModel[list[ListKeyWord]]):
    root: list[ListKeyWord] = Field(..., description="Palavra chave do documento na base de conhecimento.")


class ErrorModelBase(BaseModel):
    code: str = Field(..., description="Código identificador do erro.")
    message: str = Field(..., description="Literal no idioma da requisição descrevendo o erro para o usuário.")
    detailed_message: str = Field(
        ..., alias="detailedMessage", description="Mensagem técnica e mais detalhada do erro."
    )
    help_url: AnyUrl | None = Field(None, alias="helpUrl", description="URI para documentação do erro.")


class ErrorDetail(BaseModel):
    details: list[ErrorModelBase] | None = None


class Documents(BaseModel):
    items: list[DocumentInfo] | None = None


class ErrorModel(ErrorModelBase, ErrorDetail):
    pass


class PagedDocument(Paging, Documents):
    pass
