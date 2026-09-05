"""Painel de Auditoria — generated from AuditPanel_v1_000.json (ttalk ca5e26a). Do not edit by hand."""

from __future__ import annotations

from pydantic import AwareDatetime, BaseModel, Field


class Item(BaseModel):
    period: list[str] | None = Field(None, examples=[["Todos", "1", "2"]])


class AuditPeriodItems(BaseModel):
    items: list[Item] | None = None


class InvalidRequest(BaseModel):
    code: float = Field(..., examples=[400])
    message: str = Field(..., examples=["Registro não encontrado"])
    detailed_message: str | None = Field(None, alias="detailedMessage", examples=[""])
    type: str = Field(..., examples=["error"])


class InternalServerError(BaseModel):
    code: float = Field(..., examples=[500])
    message: str = Field(..., examples=["Erro Interno do Servidor"])
    detailed_message: str | None = Field(
        None, alias="detailedMessage", examples=["Favor verificar arquivos de log do seu servidor"]
    )


class Item1(BaseModel):
    general_situations: float | None = Field(None, alias="general-situations", examples=[1345])
    resolved_situations: float | None = Field(None, alias="resolved-situations", examples=[345])


class AuditBigNumbersItems(BaseModel):
    items: list[Item1] | None = None


class Paging(BaseModel):
    has_next: bool | None = Field(None, alias="hasNext", examples=[False])


class AuditEmployeeList(BaseModel):
    id: str = Field(..., examples=["000001"])
    name: str = Field(..., examples=["Maria Silva"])
    branch_code: str | None = Field(None, alias="branchCode", examples=["01"])
    employee_id: str = Field(..., alias="employeeId", examples=["102030"])
    rubric_code: str | None = Field(None, alias="rubricCode", examples=["001"])
    rubric_desc: str | None = Field(None, alias="rubricDesc", examples=["Salário Mensalista"])
    cpf: str = Field(..., examples=["123.456.789-00"])
    cnpj: str | None = Field(None, examples=["00.111.222/0001-33"])
    situations: bool | None = Field(None, examples=[True])


class AuditConformityList(BaseModel):
    id: str = Field(..., examples=["000001"])
    descricao: str = Field(..., examples=["Pagamento de Salário Duplicado"])
    quantidade: float = Field(..., examples=[100])
    detail: str | None = Field(None, examples=["true"])


class AuditConformityEmployeeList(BaseModel):
    cpf: str | None = Field(None, examples=["123.456.789-00"])
    name: str | None = Field(None, examples=["Maria Silva"])
    employee_id: str | None = Field(None, alias="employeeId", examples=["102030"])
    branch_code: str | None = Field(None, alias="branchCode", examples=["01"])
    cnpj: str | None = Field(None, examples=["68.004.307/0001-02"])
    quantity: float | None = Field(None, examples=[4])


class AuditConformityEmployeeDetailsList(BaseModel):
    id: str | None = Field(None, examples=["1001"])
    descricao: str | None = Field(None, examples=["Hora Extra acima do permitido"])
    rubric_code: str | None = Field(None, alias="rubricCode", examples=["001"])
    rubric_desc: str | None = Field(None, alias="rubricDesc", examples=["Hora Extra 50%"])
    exception_description: str | None = Field(
        None, alias="exceptionDescription", examples=["Excedeu o limite diário de 2h"]
    )
    feedback: str | None = Field(None, examples=["0"])
    period: str | None = Field(None, examples=["2"])


class AuditExportAnaliticoList(BaseModel):
    filial: str | None = Field(None, examples=["1"])
    matricula: str | None = Field(None, examples=["00004"])
    nome: str | None = Field(None, examples=["ADALBERTO DE JESUS LIMA"])
    cpf: str | None = Field(None, examples=["455.886.006-49"])
    cnpj: str | None = Field(None, examples=["21.867.387/0001-58"])
    id_regra: str | None = Field(None, alias="idRegra", examples=["001"])
    descricao_regra: str | None = Field(None, alias="descricaoRegra", examples=["Evento duplicado"])
    cod_rubrica: str | None = Field(None, alias="codRubrica", examples=["0005"])
    desc_rubrica: str | None = Field(None, alias="descRubrica", examples=["SALARIO FAMILIA"])
    excecao: str | None = Field(None, examples=["Transação duplicada (2 ocorrências)"])
    feedback: str | None = Field(None, examples=["Sem Feedback"])


class AuditBranchList(BaseModel):
    branch_code: str | None = Field(None, alias="branchCode", examples=["01"])
    branch_name: str | None = Field(None, alias="branchName", examples=["Matriz"])
    branch_cnpj: str | None = Field(None, alias="branchCNPJ", examples=["53113791000122"])


class AuditLastUpdate(BaseModel):
    last_update: str | None = Field(None, alias="last-update", examples=["2025-10-30 17:43:24"])


class AuditHistoryList(BaseModel):
    branch_code: str | None = Field(None, alias="branchCode", examples=["01"])
    company_id: float | None = Field(None, alias="companyId", examples=[1])
    id: str | None = Field(None, examples=["000001"])
    description: str | None = Field(None, examples=["Pagamento de Horas Extras"])
    employee_id: str | None = Field(None, alias="employeeId", examples=["XPTO0001"])
    name_employee: str | None = Field(None, alias="nameEmployee", examples=["MARCOS"])
    date_included: AwareDatetime | None = Field(None, alias="dateIncluded", examples=["2025-11-12T11:00:01Z"])
    resolved: float | None = Field(None, examples=[0])
    type_history: float | None = Field(None, alias="typeHistory", examples=[0])


class AuditEmployeeItems(Paging):
    items: list[AuditEmployeeList] | None = None


class AuditConformityItems(Paging):
    items: list[AuditConformityList] | None = None


class AuditConformityEmployeeItems(Paging):
    items: list[AuditConformityEmployeeList] | None = None


class AuditConformityEmployeeDetailsItems(Paging):
    items: list[AuditConformityEmployeeDetailsList] | None = None


class AuditExportAnaliticoItems(Paging):
    items: list[AuditExportAnaliticoList] | None = None


class AuditBranchItems(Paging):
    items: list[AuditBranchList] | None = None


class AuditHistoryItems(Paging):
    items: list[AuditHistoryList] | None = None
