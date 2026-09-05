"""Relacionamento de Contatos x Entidade — generated from ContactRelationship_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class ContactRelationshipV1(ApiGroup):
    """Relacionamento de Contatos x Entidade (/api/crm/v1)."""

    api_id = "contact_relationship_v1"
    base_path = "/api/crm/v1"

    def list_contactrelationship(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Relacionamentos de Contato

        GET /contactrelationship; operationId=getcontactrelationship; Protheus >= 12.1.21

        Retorna uma lista completa de Relacionamentos de Contato x Entidade

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.contact_relationship_v1.PagedContactRelationship
        """
        return self._request(
            "contact_relationship_v1.list_contactrelationship",
            "GET",
            "/contactrelationship",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_contactrelationship(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Relacionamento de Contato

        POST /contactrelationship; operationId=postcontactrelationship; Protheus >= 12.1.21

        Inclui uma Relacionamento de Contato conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.contact_relationship_v1.BusinessContentType
        Request model: protheus.models.contact_relationship_v1.BusinessContentType
        """
        return self._request(
            "contact_relationship_v1.create_contactrelationship",
            "POST",
            "/contactrelationship",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_contactrelationship_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Relacionamento de Contato pelo InternalId

        GET /contactrelationship/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna um Relacionamento de Contato x Entidade pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.contact_relationship_v1.BusinessContentType
        """
        return self._request(
            "contact_relationship_v1.get_contactrelationship_by_internal_id",
            "GET",
            "/contactrelationship/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_contactrelationship_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Relacionamento de Contato pelo InternalId

        PUT /contactrelationship/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Altera um Relacionamento de Contato x Entidade pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.contact_relationship_v1.BusinessContentType
        Request model: protheus.models.contact_relationship_v1.BusinessContentType
        """
        return self._request(
            "contact_relationship_v1.update_contactrelationship_by_internal_id",
            "PUT",
            "/contactrelationship/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_contactrelationship_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Relacionamento de Contato pelo InternalId

        DELETE /contactrelationship/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Relacionamento de Contato de Entidade pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return self._request(
            "contact_relationship_v1.delete_contactrelationship_by_internal_id",
            "DELETE",
            "/contactrelationship/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_contactrelationship_by_internal_id_listofcontact(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de items de Relacionamentos de Contato x Entidade

        GET /contactrelationship/{InternalId}/listofcontact; operationId=getlistofcontact; Protheus >= 12.1.21

        Retorna uma lista completa de items de todos Relacionamentos de Contato x Entidade

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize, Fields e InternalId

        Response model: protheus.models.contact_relationship_v1.PagedContactType
        """
        return self._request(
            "contact_relationship_v1.list_contactrelationship_by_internal_id_listofcontact",
            "GET",
            "/contactrelationship/{InternalId}/listofcontact",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_contactrelationship_by_internal_id_listofcontact(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Item no Relacionamento de Contato x Entidade especifico

        POST /contactrelationship/{InternalId}/listofcontact; operationId=postlistofcontact; Protheus >= 12.1.21

        Inclui um Item em um Relacionamento de Contato especifico conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.contact_relationship_v1.ContactType
        Request model: protheus.models.contact_relationship_v1.ContactType
        """
        return self._request(
            "contact_relationship_v1.create_contactrelationship_by_internal_id_listofcontact",
            "POST",
            "/contactrelationship/{InternalId}/listofcontact",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_contactrelationship_by_internal_id_listofcontact_by_contact_code(self, internal_id: str, contact_code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Item de um Relacionamento de Contato especifico

        GET /contactrelationship/{InternalId}/listofcontact/{ContactCode}; operationId=getContactCode; Protheus >= 12.1.21

        Retorna um Item Especifico pelo ContactCode de Relacionamento de Contato

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId, ContactCode e Fields

        Response model: protheus.models.contact_relationship_v1.ContactType
        """
        return self._request(
            "contact_relationship_v1.get_contactrelationship_by_internal_id_listofcontact_by_contact_code",
            "GET",
            "/contactrelationship/{InternalId}/listofcontact/{ContactCode}",
            path_params={"InternalId": internal_id, "ContactCode": contact_code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_contactrelationship_by_internal_id_listofcontact_by_contact_code(self, internal_id: str, contact_code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Item de um Relacionamento de Contato pelo especifico

        PUT /contactrelationship/{InternalId}/listofcontact/{ContactCode}; operationId=putContactCode; Protheus >= 12.1.21

        Altera um Item especifico pelo ContactCode de Relacionamento de Contato x Entidade

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e ContactCode

        Response model: protheus.models.contact_relationship_v1.ContactType
        Request model: protheus.models.contact_relationship_v1.ContactType
        """
        return self._request(
            "contact_relationship_v1.update_contactrelationship_by_internal_id_listofcontact_by_contact_code",
            "PUT",
            "/contactrelationship/{InternalId}/listofcontact/{ContactCode}",
            path_params={"InternalId": internal_id, "ContactCode": contact_code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_contactrelationship_by_internal_id_listofcontact_by_contact_code(self, internal_id: str, contact_code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Item de um Relacionamento de Contato pelo especifico

        DELETE /contactrelationship/{InternalId}/listofcontact/{ContactCode}; operationId=deleteContactCode; Protheus >= 12.1.21

        Exclui um Item especifico pelo ContactCode de Relacionamento de Contato x Entidade

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e ContactCode
        """
        return self._request(
            "contact_relationship_v1.delete_contactrelationship_by_internal_id_listofcontact_by_contact_code",
            "DELETE",
            "/contactrelationship/{InternalId}/listofcontact/{ContactCode}",
            path_params={"InternalId": internal_id, "ContactCode": contact_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncContactRelationshipV1(AsyncApiGroup):
    """Relacionamento de Contatos x Entidade (/api/crm/v1)."""

    api_id = "contact_relationship_v1"
    base_path = "/api/crm/v1"

    async def list_contactrelationship(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de Relacionamentos de Contato

        GET /contactrelationship; operationId=getcontactrelationship; Protheus >= 12.1.21

        Retorna uma lista completa de Relacionamentos de Contato x Entidade

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize e Fields

        Response model: protheus.models.contact_relationship_v1.PagedContactRelationship
        """
        return await self._request(
            "contact_relationship_v1.list_contactrelationship",
            "GET",
            "/contactrelationship",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_contactrelationship(self, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Relacionamento de Contato

        POST /contactrelationship; operationId=postcontactrelationship; Protheus >= 12.1.21

        Inclui uma Relacionamento de Contato conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e Fields

        Response model: protheus.models.contact_relationship_v1.BusinessContentType
        Request model: protheus.models.contact_relationship_v1.BusinessContentType
        """
        return await self._request(
            "contact_relationship_v1.create_contactrelationship",
            "POST",
            "/contactrelationship",
            path_params={},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_contactrelationship_by_internal_id(self, internal_id: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Relacionamento de Contato pelo InternalId

        GET /contactrelationship/{InternalId}; operationId=getInternalId; Protheus >= 12.1.21

        Retorna um Relacionamento de Contato x Entidade pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e Fields

        Response model: protheus.models.contact_relationship_v1.BusinessContentType
        """
        return await self._request(
            "contact_relationship_v1.get_contactrelationship_by_internal_id",
            "GET",
            "/contactrelationship/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_contactrelationship_by_internal_id(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Relacionamento de Contato pelo InternalId

        PUT /contactrelationship/{InternalId}; operationId=putInternalId; Protheus >= 12.1.21

        Altera um Relacionamento de Contato x Entidade pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.contact_relationship_v1.BusinessContentType
        Request model: protheus.models.contact_relationship_v1.BusinessContentType
        """
        return await self._request(
            "contact_relationship_v1.update_contactrelationship_by_internal_id",
            "PUT",
            "/contactrelationship/{InternalId}",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_contactrelationship_by_internal_id(self, internal_id: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Relacionamento de Contato pelo InternalId

        DELETE /contactrelationship/{InternalId}; operationId=deleteInternalId; Protheus >= 12.1.21

        Exclui um Relacionamento de Contato de Entidade pelo InternalId

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization e InternalId
        """
        return await self._request(
            "contact_relationship_v1.delete_contactrelationship_by_internal_id",
            "DELETE",
            "/contactrelationship/{InternalId}",
            path_params={"InternalId": internal_id},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_contactrelationship_by_internal_id_listofcontact(self, internal_id: str, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna uma lista de items de Relacionamentos de Contato x Entidade

        GET /contactrelationship/{InternalId}/listofcontact; operationId=getlistofcontact; Protheus >= 12.1.21

        Retorna uma lista completa de items de todos Relacionamentos de Contato x Entidade

        TOTVS note: Este verbo este disponível com os parâmetros Authorization, Order, Page, PageSize, Fields e InternalId

        Response model: protheus.models.contact_relationship_v1.PagedContactType
        """
        return await self._request(
            "contact_relationship_v1.list_contactrelationship_by_internal_id_listofcontact",
            "GET",
            "/contactrelationship/{InternalId}/listofcontact",
            path_params={"InternalId": internal_id},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_contactrelationship_by_internal_id_listofcontact(self, internal_id: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Item no Relacionamento de Contato x Entidade especifico

        POST /contactrelationship/{InternalId}/listofcontact; operationId=postlistofcontact; Protheus >= 12.1.21

        Inclui um Item em um Relacionamento de Contato especifico conforme dados enviados na requisição.

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields e InternalId

        Response model: protheus.models.contact_relationship_v1.ContactType
        Request model: protheus.models.contact_relationship_v1.ContactType
        """
        return await self._request(
            "contact_relationship_v1.create_contactrelationship_by_internal_id_listofcontact",
            "POST",
            "/contactrelationship/{InternalId}/listofcontact",
            path_params={"InternalId": internal_id},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_contactrelationship_by_internal_id_listofcontact_by_contact_code(self, internal_id: str, contact_code: str, *, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um Item de um Relacionamento de Contato especifico

        GET /contactrelationship/{InternalId}/listofcontact/{ContactCode}; operationId=getContactCode; Protheus >= 12.1.21

        Retorna um Item Especifico pelo ContactCode de Relacionamento de Contato

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId, ContactCode e Fields

        Response model: protheus.models.contact_relationship_v1.ContactType
        """
        return await self._request(
            "contact_relationship_v1.get_contactrelationship_by_internal_id_listofcontact_by_contact_code",
            "GET",
            "/contactrelationship/{InternalId}/listofcontact/{ContactCode}",
            path_params={"InternalId": internal_id, "ContactCode": contact_code},
            query={"fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_contactrelationship_by_internal_id_listofcontact_by_contact_code(self, internal_id: str, contact_code: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um Item de um Relacionamento de Contato pelo especifico

        PUT /contactrelationship/{InternalId}/listofcontact/{ContactCode}; operationId=putContactCode; Protheus >= 12.1.21

        Altera um Item especifico pelo ContactCode de Relacionamento de Contato x Entidade

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, Fields, InternalId e ContactCode

        Response model: protheus.models.contact_relationship_v1.ContactType
        Request model: protheus.models.contact_relationship_v1.ContactType
        """
        return await self._request(
            "contact_relationship_v1.update_contactrelationship_by_internal_id_listofcontact_by_contact_code",
            "PUT",
            "/contactrelationship/{InternalId}/listofcontact/{ContactCode}",
            path_params={"InternalId": internal_id, "ContactCode": contact_code},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_contactrelationship_by_internal_id_listofcontact_by_contact_code(self, internal_id: str, contact_code: str, *, extra_query: Mapping[str, Any] | None = None) -> None:
        """Exclui um Item de um Relacionamento de Contato pelo especifico

        DELETE /contactrelationship/{InternalId}/listofcontact/{ContactCode}; operationId=deleteContactCode; Protheus >= 12.1.21

        Exclui um Item especifico pelo ContactCode de Relacionamento de Contato x Entidade

        TOTVS note: Este verbo esta disponível com os parâmetros Authorization, InternalId e ContactCode
        """
        return await self._request(
            "contact_relationship_v1.delete_contactrelationship_by_internal_id_listofcontact_by_contact_code",
            "DELETE",
            "/contactrelationship/{InternalId}/listofcontact/{ContactCode}",
            path_params={"InternalId": internal_id, "ContactCode": contact_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
