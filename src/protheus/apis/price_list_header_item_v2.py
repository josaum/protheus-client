"""Tabela de Preços — generated from PriceListHeaderItem_v2_005.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class PriceListHeaderItemV2(ApiGroup):
    """Tabela de Preços (/api/supply/v2)."""

    api_id = "price_list_header_item_v2"
    base_path = "/api/supply/v2"

    def list_price_list_header_items(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Tabelas de Preço

        GET /PriceListHeaderItems; operationId=getpriceListHeaderItem; Protheus >= 12.1.21

        Retorna lista de Tabela de Preço

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return self._request(
            "price_list_header_item_v2.list_price_list_header_items",
            "GET",
            "/PriceListHeaderItems",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_price_list_header_items(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Tabela de Preço

        POST /PriceListHeaderItems; operationId=postpriceListHeaderItem; Protheus >= 12.1.25

        Inclui uma tabela de preço conforme dados enviados na requisição.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        Request model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return self._request(
            "price_list_header_item_v2.create_price_list_header_items",
            "POST",
            "/PriceListHeaderItems",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_price_list_header_items_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a tabela de preço e todos os seus itens de acordo com o seu código

        GET /PriceListHeaderItems/{code}; operationId=getpriceListCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e code.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return self._request(
            "price_list_header_item_v2.get_price_list_header_items_by_code",
            "GET",
            "/PriceListHeaderItems/{code}",
            path_params={"code": code},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_price_list_header_items_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Cabeçalho da tabela de preço

        PUT /PriceListHeaderItems/{code}; operationId=putpriceListCode; Protheus >= 12.1.25

        Atualiza o cadastro da tabela de preço conforme dados enviados na requisição

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        Request model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return self._request(
            "price_list_header_item_v2.update_price_list_header_items_by_code",
            "PUT",
            "/PriceListHeaderItems/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_price_list_header_items_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui uma tabela de preço

        DELETE /PriceListHeaderItems/{code}; operationId=deletepriceListCode; Protheus >= 12.1.25

        Exclui a tabela de preço conforme dados enviados na requisição.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return self._request(
            "price_list_header_item_v2.delete_price_list_header_items_by_code",
            "DELETE",
            "/PriceListHeaderItems/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def list_price_list_header_items_by_code_itens_table_price(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os itens da tabela de preço de acordo com o seu código

        GET /PriceListHeaderItems/{code}/itensTablePrice/; operationId=getpriceListItems; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e code.

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        """
        return self._request(
            "price_list_header_item_v2.list_price_list_header_items_by_code_itens_table_price",
            "GET",
            "/PriceListHeaderItems/{code}/itensTablePrice/",
            path_params={"code": code},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_price_list_header_items_by_code_itens_table_price(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item na Tabela de Preço

        POST /PriceListHeaderItems/{code}/itensTablePrice/; operationId=postpriceListItems; Protheus >= 12.1.25

        Inclui um novo item na tabela de preço conforme dados enviados.

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        Request model: protheus.models.price_list_header_item_v2.ItensTablePrices
        """
        return self._request(
            "price_list_header_item_v2.create_price_list_header_items_by_code_itens_table_price",
            "POST",
            "/PriceListHeaderItems/{code}/itensTablePrice/",
            path_params={"code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_price_list_header_items_by_code_itens_table_price_by_item_list(self, code: str, item_list: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um item específico de preço de acordo com o seu código

        GET /PriceListHeaderItems/{code}/itensTablePrice/{itemList}; operationId=getpriceListItemList; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e code.

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        """
        return self._request(
            "price_list_header_item_v2.get_price_list_header_items_by_code_itens_table_price_by_item_list",
            "GET",
            "/PriceListHeaderItems/{code}/itensTablePrice/{itemList}",
            path_params={"code": code, "itemList": item_list},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_price_list_header_items_by_code_itens_table_price_by_item_list(self, code: str, item_list: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um item da tabela de preço

        PUT /PriceListHeaderItems/{code}/itensTablePrice/{itemList}; operationId=putpriceListItemList; Protheus >= 12.1.25

        Atualiza um item da tabela de preço conforme dados enviados na requisição

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        Request model: protheus.models.price_list_header_item_v2.ItensTablePrices
        """
        return self._request(
            "price_list_header_item_v2.update_price_list_header_items_by_code_itens_table_price_by_item_list",
            "PUT",
            "/PriceListHeaderItems/{code}/itensTablePrice/{itemList}",
            path_params={"code": code, "itemList": item_list},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_price_list_header_items_by_code_itens_table_price_by_item_list(self, code: str, item_list: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um item da tabela de preço

        DELETE /PriceListHeaderItems/{code}/itensTablePrice/{itemList}; operationId=deletepriceListItemList; Protheus >= 12.1.25

        Exclui um item da tabela de preço conforme dados enviados na requisição.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return self._request(
            "price_list_header_item_v2.delete_price_list_header_items_by_code_itens_table_price_by_item_list",
            "DELETE",
            "/PriceListHeaderItems/{code}/itensTablePrice/{itemList}",
            path_params={"code": code, "itemList": item_list},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncPriceListHeaderItemV2(AsyncApiGroup):
    """Tabela de Preços (/api/supply/v2)."""

    api_id = "price_list_header_item_v2"
    base_path = "/api/supply/v2"

    async def list_price_list_header_items(self, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Tabelas de Preço

        GET /PriceListHeaderItems; operationId=getpriceListHeaderItem; Protheus >= 12.1.21

        Retorna lista de Tabela de Preço

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return await self._request(
            "price_list_header_item_v2.list_price_list_header_items",
            "GET",
            "/PriceListHeaderItems",
            path_params={},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_price_list_header_items(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui uma Tabela de Preço

        POST /PriceListHeaderItems; operationId=postpriceListHeaderItem; Protheus >= 12.1.25

        Inclui uma tabela de preço conforme dados enviados na requisição.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        Request model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return await self._request(
            "price_list_header_item_v2.create_price_list_header_items",
            "POST",
            "/PriceListHeaderItems",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_price_list_header_items_by_code(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna a tabela de preço e todos os seus itens de acordo com o seu código

        GET /PriceListHeaderItems/{code}; operationId=getpriceListCode; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e code.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return await self._request(
            "price_list_header_item_v2.get_price_list_header_items_by_code",
            "GET",
            "/PriceListHeaderItems/{code}",
            path_params={"code": code},
            query={"order": order, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_price_list_header_items_by_code(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera o Cabeçalho da tabela de preço

        PUT /PriceListHeaderItems/{code}; operationId=putpriceListCode; Protheus >= 12.1.25

        Atualiza o cadastro da tabela de preço conforme dados enviados na requisição

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        Request model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return await self._request(
            "price_list_header_item_v2.update_price_list_header_items_by_code",
            "PUT",
            "/PriceListHeaderItems/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_price_list_header_items_by_code(self, code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui uma tabela de preço

        DELETE /PriceListHeaderItems/{code}; operationId=deletepriceListCode; Protheus >= 12.1.25

        Exclui a tabela de preço conforme dados enviados na requisição.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return await self._request(
            "price_list_header_item_v2.delete_price_list_header_items_by_code",
            "DELETE",
            "/PriceListHeaderItems/{code}",
            path_params={"code": code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def list_price_list_header_items_by_code_itens_table_price(self, code: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os itens da tabela de preço de acordo com o seu código

        GET /PriceListHeaderItems/{code}/itensTablePrice/; operationId=getpriceListItems; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e code.

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        """
        return await self._request(
            "price_list_header_item_v2.list_price_list_header_items_by_code_itens_table_price",
            "GET",
            "/PriceListHeaderItems/{code}/itensTablePrice/",
            path_params={"code": code},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_price_list_header_items_by_code_itens_table_price(self, code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um item na Tabela de Preço

        POST /PriceListHeaderItems/{code}/itensTablePrice/; operationId=postpriceListItems; Protheus >= 12.1.25

        Inclui um novo item na tabela de preço conforme dados enviados.

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        Request model: protheus.models.price_list_header_item_v2.ItensTablePrices
        """
        return await self._request(
            "price_list_header_item_v2.create_price_list_header_items_by_code_itens_table_price",
            "POST",
            "/PriceListHeaderItems/{code}/itensTablePrice/",
            path_params={"code": code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_price_list_header_items_by_code_itens_table_price_by_item_list(self, code: str, item_list: str, *, order: str | list[str] | None = None, fields: str | None = None, page: int | None = None, page_size: int | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna um item específico de preço de acordo com o seu código

        GET /PriceListHeaderItems/{code}/itensTablePrice/{itemList}; operationId=getpriceListItemList; Protheus >= 12.1.21

        TOTVS note: Este verbo está disponível com os parâmetros Authorization e code.

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        """
        return await self._request(
            "price_list_header_item_v2.get_price_list_header_items_by_code_itens_table_price_by_item_list",
            "GET",
            "/PriceListHeaderItems/{code}/itensTablePrice/{itemList}",
            path_params={"code": code, "itemList": item_list},
            query={"order": order, "fields": fields, "page": page, "pageSize": page_size},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_price_list_header_items_by_code_itens_table_price_by_item_list(self, code: str, item_list: str, *, body: Body, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Altera um item da tabela de preço

        PUT /PriceListHeaderItems/{code}/itensTablePrice/{itemList}; operationId=putpriceListItemList; Protheus >= 12.1.25

        Atualiza um item da tabela de preço conforme dados enviados na requisição

        Response model: protheus.models.price_list_header_item_v2.PagedItensTablePrice
        Request model: protheus.models.price_list_header_item_v2.ItensTablePrices
        """
        return await self._request(
            "price_list_header_item_v2.update_price_list_header_items_by_code_itens_table_price_by_item_list",
            "PUT",
            "/PriceListHeaderItems/{code}/itensTablePrice/{itemList}",
            path_params={"code": code, "itemList": item_list},
            query={"fields": fields},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_price_list_header_items_by_code_itens_table_price_by_item_list(self, code: str, item_list: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui um item da tabela de preço

        DELETE /PriceListHeaderItems/{code}/itensTablePrice/{itemList}; operationId=deletepriceListItemList; Protheus >= 12.1.25

        Exclui um item da tabela de preço conforme dados enviados na requisição.

        Response model: protheus.models.price_list_header_item_v2.PagedPriceListHeaderItems
        """
        return await self._request(
            "price_list_header_item_v2.delete_price_list_header_items_by_code_itens_table_price_by_item_list",
            "DELETE",
            "/PriceListHeaderItems/{code}/itensTablePrice/{itemList}",
            path_params={"code": code, "itemList": item_list},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
