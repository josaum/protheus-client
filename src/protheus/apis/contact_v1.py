"""Contatos — generated from Contact_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ContactV1(ApiGroup):
    """Contatos (/api/crm/contact/v1)."""

    api_id = "contact_v1"
    base_path = "/api/crm/contact/v1"

    def list_contacts(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Contatos

        GET /contacts; operationId=getcontact; Protheus >= 12.1.21

        Retorna lista completa de Contatos

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.contact_v1.PagedContacts
        """
        return self._request(
            "contact_v1.list_contacts",
            "GET",
            "/contacts",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_contacts(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Contato

        POST /contacts; operationId=postContact; Protheus >= 12.1.21

        Inclui um Contato conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.contact_v1.PagedContacts
        Request model: protheus.models.contact_v1.ContactInfo
        """
        return self._request(
            "contact_v1.create_contacts",
            "POST",
            "/contacts",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_contacts_by_contact_id(self, contact_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Contato pelo seu Código

        GET /contacts/{contactId}; operationId=getcontactId; Protheus >= 12.1.21

        Retorna o contato conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e ContactId.

        Response model: protheus.models.contact_v1.ContactInfo
        """
        return self._request(
            "contact_v1.get_contacts_by_contact_id",
            "GET",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_contacts_by_contact_id(self, contact_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Contato

        PUT /contacts/{contactId}; operationId=putcontactId; Protheus >= 12.1.21

        Atualiza cadastro do Contato conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, Fieldse e ContactId

        Response model: protheus.models.contact_v1.ContactInfo
        Request model: protheus.models.contact_v1.ContactInfo
        """
        return self._request(
            "contact_v1.update_contacts_by_contact_id",
            "PUT",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_contacts_by_contact_id(self, contact_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Contato

        DELETE /contacts/{contactId}; operationId=deletecontactId; Protheus >= 12.1.21

        Exclui cadastro do Contato conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e ContactId

        Response model: protheus.models.contact_v1.PagedContacts
        """
        return self._request(
            "contact_v1.delete_contacts_by_contact_id",
            "DELETE",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncContactV1(AsyncApiGroup):
    """Contatos (/api/crm/contact/v1)."""

    api_id = "contact_v1"
    base_path = "/api/crm/contact/v1"

    async def list_contacts(self, *, fields: str | None = None, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Contatos

        GET /contacts; operationId=getcontact; Protheus >= 12.1.21

        Retorna lista completa de Contatos

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields, Order, Page, PageSize

        Response model: protheus.models.contact_v1.PagedContacts
        """
        return await self._request(
            "contact_v1.list_contacts",
            "GET",
            "/contacts",
            path_params={},
            query={"fields": fields, "order": order, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_contacts(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Contato

        POST /contacts; operationId=postContact; Protheus >= 12.1.21

        Inclui um Contato conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com o parametro Authorization

        Response model: protheus.models.contact_v1.PagedContacts
        Request model: protheus.models.contact_v1.ContactInfo
        """
        return await self._request(
            "contact_v1.create_contacts",
            "POST",
            "/contacts",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_contacts_by_contact_id(self, contact_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna o Contato pelo seu Código

        GET /contacts/{contactId}; operationId=getcontactId; Protheus >= 12.1.21

        Retorna o contato conforme dados enviados na requisição

        TOTVS note: Este verbo está disponível com os parâmetros Authorization, Fields e ContactId.

        Response model: protheus.models.contact_v1.ContactInfo
        """
        return await self._request(
            "contact_v1.get_contacts_by_contact_id",
            "GET",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_contacts_by_contact_id(self, contact_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Contato

        PUT /contacts/{contactId}; operationId=putcontactId; Protheus >= 12.1.21

        Atualiza cadastro do Contato conforme dados enviados na requisição

        TOTVS note: Este verbo esta disponível com os parâmetros authorization, Fieldse e ContactId

        Response model: protheus.models.contact_v1.ContactInfo
        Request model: protheus.models.contact_v1.ContactInfo
        """
        return await self._request(
            "contact_v1.update_contacts_by_contact_id",
            "PUT",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_contacts_by_contact_id(self, contact_id: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um Contato

        DELETE /contacts/{contactId}; operationId=deletecontactId; Protheus >= 12.1.21

        Exclui cadastro do Contato conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e ContactId

        Response model: protheus.models.contact_v1.PagedContacts
        """
        return await self._request(
            "contact_v1.delete_contacts_by_contact_id",
            "DELETE",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
