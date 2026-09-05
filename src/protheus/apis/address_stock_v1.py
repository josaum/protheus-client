"""Endereços — generated from AddressStock_v1_000.json (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from protheus._base import ApiGroup, AsyncApiGroup, Body


class AddressStockV1(ApiGroup):
    """Endereços (/api/entradas/v1)."""

    api_id = "address_stock_v1"
    base_path = "/api/entradas/v1"

    def list_address_stocks(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Endereços

        GET /AddressStocks; operationId=getAddressStock; Protheus >= 12.1.21

        Retorna lista completa de Grupo de Produto

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.PagedAddressStock
        """
        return self._request(
            "address_stock_v1.list_address_stocks",
            "GET",
            "/AddressStocks",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def create_address_stocks(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Endereço

        POST /AddressStocks; operationId=postAddressStock; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        Request model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return self._request(
            "address_stock_v1.create_address_stocks",
            "POST",
            "/AddressStocks",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def get_address_stocks_by_warehouse_code(self, warehouse_code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os Endereços de um Local de Estoque específico

        GET /AddressStocks/{WarehouseCode}; operationId=getWarehouseCode; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return self._request(
            "address_stock_v1.get_address_stocks_by_warehouse_code",
            "GET",
            "/AddressStocks/{WarehouseCode}",
            path_params={"WarehouseCode": warehouse_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def get_address_stocks_by_warehouse_code_and_location_code(self, warehouse_code: str, location_code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os Endereços de um Local de Estoque específico

        GET /AddressStocks/{WarehouseCode}/{LocationCode}; operationId=getLocationCode; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return self._request(
            "address_stock_v1.get_address_stocks_by_warehouse_code_and_location_code",
            "GET",
            "/AddressStocks/{WarehouseCode}/{LocationCode}",
            path_params={"WarehouseCode": warehouse_code, "LocationCode": location_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    def update_address_stocks_by_warehouse_code_and_location_code(self, warehouse_code: str, location_code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza cadastro de Endereço conforme dados enviados na requisição

        PUT /AddressStocks/{WarehouseCode}/{LocationCode}; operationId=putLocationCode; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        Request model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return self._request(
            "address_stock_v1.update_address_stocks_by_warehouse_code_and_location_code",
            "PUT",
            "/AddressStocks/{WarehouseCode}/{LocationCode}",
            path_params={"WarehouseCode": warehouse_code, "LocationCode": location_code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    def delete_address_stocks_by_warehouse_code_and_location_code(self, warehouse_code: str, location_code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui Local de Estoque cadastrado conforme dados enviados na requisição

        DELETE /AddressStocks/{WarehouseCode}/{LocationCode}; operationId=deleteLocationCode

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return self._request(
            "address_stock_v1.delete_address_stocks_by_warehouse_code_and_location_code",
            "DELETE",
            "/AddressStocks/{WarehouseCode}/{LocationCode}",
            path_params={"WarehouseCode": warehouse_code, "LocationCode": location_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

class AsyncAddressStockV1(AsyncApiGroup):
    """Endereços (/api/entradas/v1)."""

    api_id = "address_stock_v1"
    base_path = "/api/entradas/v1"

    async def list_address_stocks(self, *, order: str | list[str] | None = None, page: int | None = None, page_size: int | None = None, fields: str | None = None, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna lista de Endereços

        GET /AddressStocks; operationId=getAddressStock; Protheus >= 12.1.21

        Retorna lista completa de Grupo de Produto

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.PagedAddressStock
        """
        return await self._request(
            "address_stock_v1.list_address_stocks",
            "GET",
            "/AddressStocks",
            path_params={},
            query={"order": order, "page": page, "pageSize": page_size, "fields": fields},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def create_address_stocks(self, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Inclui um Endereço

        POST /AddressStocks; operationId=postAddressStock; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        Request model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return await self._request(
            "address_stock_v1.create_address_stocks",
            "POST",
            "/AddressStocks",
            path_params={},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def get_address_stocks_by_warehouse_code(self, warehouse_code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os Endereços de um Local de Estoque específico

        GET /AddressStocks/{WarehouseCode}; operationId=getWarehouseCode; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return await self._request(
            "address_stock_v1.get_address_stocks_by_warehouse_code",
            "GET",
            "/AddressStocks/{WarehouseCode}",
            path_params={"WarehouseCode": warehouse_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def get_address_stocks_by_warehouse_code_and_location_code(self, warehouse_code: str, location_code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Retorna os Endereços de um Local de Estoque específico

        GET /AddressStocks/{WarehouseCode}/{LocationCode}; operationId=getLocationCode; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return await self._request(
            "address_stock_v1.get_address_stocks_by_warehouse_code_and_location_code",
            "GET",
            "/AddressStocks/{WarehouseCode}/{LocationCode}",
            path_params={"WarehouseCode": warehouse_code, "LocationCode": location_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )

    async def update_address_stocks_by_warehouse_code_and_location_code(self, warehouse_code: str, location_code: str, *, body: Body, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Atualiza cadastro de Endereço conforme dados enviados na requisição

        PUT /AddressStocks/{WarehouseCode}/{LocationCode}; operationId=putLocationCode; Protheus >= 12.1.21

        TOTVS note: Este verbo esta disponivel com todos os parametros

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        Request model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return await self._request(
            "address_stock_v1.update_address_stocks_by_warehouse_code_and_location_code",
            "PUT",
            "/AddressStocks/{WarehouseCode}/{LocationCode}",
            path_params={"WarehouseCode": warehouse_code, "LocationCode": location_code},
            query={},
            headers={},
            body=body,
            extra_query=extra_query,
        )

    async def delete_address_stocks_by_warehouse_code_and_location_code(self, warehouse_code: str, location_code: str, *, extra_query: Mapping[str, Any] | None = None) -> Any:
        """Exclui Local de Estoque cadastrado conforme dados enviados na requisição

        DELETE /AddressStocks/{WarehouseCode}/{LocationCode}; operationId=deleteLocationCode

        Response model: protheus.models.address_stock_v1.AddressStockInfo
        """
        return await self._request(
            "address_stock_v1.delete_address_stocks_by_warehouse_code_and_location_code",
            "DELETE",
            "/AddressStocks/{WarehouseCode}/{LocationCode}",
            path_params={"WarehouseCode": warehouse_code, "LocationCode": location_code},
            query={},
            headers={},
            body=None,
            extra_query=extra_query,
        )
