"""Decode paged responses straight into Arrow with the ``ttalk_fast`` engine.

The Rust decoder validates every row against the operation's bundled response
schema and *reports* what does not fit instead of dropping it: a field whose
live values cannot be decoded as declared (``"5,2"`` in a number column) is
demoted to Utf8 for the rest of that decoder's life, so column types are
stable across pages once settled.

    from protheus.arrow import raw, iter_arrow_pages

    group = raw(client.customer_vendor_v1)            # same methods, bytes instead of JSON
    for page in iter_arrow_pages(group.get_customer_vendor_by_entity_type,
                                 "customer_vendor_v1.get_customer_vendor_by_entity_type",
                                 entity_type="customer", page_size=500):
        table = page.to_pyarrow()                     # or hand page.ipc to polars / duckdb
        print(page.report["invalid_rows"], page.report["demoted_fields"])

Requires the ``ttalk_fast`` extension (``pip install ttalk-fast`` or
``maturin develop -m crates/ttalk-fast-py/Cargo.toml``).
"""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from dataclasses import dataclass
from functools import lru_cache
from importlib import resources
from typing import Any

from protheus import spec
from protheus._base import ApiGroup, AsyncApiGroup, PreparedRequest

try:
    import ttalk_fast  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - exercised only without the wheel
    ttalk_fast = None

AVAILABLE = ttalk_fast is not None


def _require() -> Any:
    if ttalk_fast is None:
        raise ImportError(
            "protheus.arrow needs the ttalk_fast extension: pip install ttalk-fast "
            "(or: maturin develop -m crates/ttalk-fast-py/Cargo.toml)"
        )
    return ttalk_fast


@lru_cache(maxsize=None)
def components_json(api_id: str) -> str:
    """The bundled ``components.schemas`` document vendored for one API."""
    with resources.files("protheus.spec").joinpath("schemas", f"{api_id}.json").open("r", encoding="utf-8") as fh:
        return fh.read()


@dataclass(slots=True)
class ArrowPage:
    number: int
    ipc: bytes
    report: dict[str, Any]

    @property
    def rows(self) -> int:
        return int(self.report["rows"])

    @property
    def has_next(self) -> bool:
        return bool(self.report.get("has_next"))

    def to_pyarrow(self) -> Any:
        import pyarrow.ipc  # optional dependency

        return pyarrow.ipc.open_stream(self.ipc).read_all()


class ArrowDecoder:
    """Decoder for one operation's 2xx response schema."""

    def __init__(self, operation_id: str, *, items_key: str = "items", max_violations: int = 100) -> None:
        engine = _require()
        op = spec.get_operation(operation_id)
        schema = next((r["schema"] for s, r in op["responses"].items() if s.startswith("2") and r["schema"]), None)
        if schema is None:
            raise ValueError(f"{operation_id} declares no 2xx response schema")
        self.operation_id = operation_id
        self.schema_name = schema
        self._inner = engine.Decoder(components_json(op["api_id"]), schema, items_key, max_violations)

    def decode(self, body: bytes, number: int = 1) -> ArrowPage:
        ipc, report = self._inner.decode(body)
        return ArrowPage(number, ipc, json.loads(report))

    @property
    def fields(self) -> list[dict[str, str]]:
        return json.loads(self._inner.fields())


class _RawSender:
    def __init__(self, client: Any) -> None:
        self._client = client

    def send(self, prepared: PreparedRequest) -> bytes:
        return self._client.send_bytes(prepared)


class _AsyncRawSender:
    def __init__(self, client: Any) -> None:
        self._client = client

    async def send(self, prepared: PreparedRequest) -> bytes:
        return await self._client.send_bytes(prepared)


def raw(group: ApiGroup | AsyncApiGroup) -> Any:
    """The same API group, but its methods return the raw response bytes."""
    sender = _AsyncRawSender(group._client) if isinstance(group, AsyncApiGroup) else _RawSender(group._client)
    return type(group)(sender)  # type: ignore[arg-type]


def iter_arrow_pages(
    raw_method: Callable[..., bytes],
    operation_id: str,
    *,
    page: int = 1,
    page_size: int | None = None,
    max_pages: int | None = None,
    items_key: str = "items",
    max_violations: int = 100,
    **kwargs: Any,
) -> Iterator[ArrowPage]:
    """Page through ``raw_method(page=..., page_size=..., **kwargs)`` decoding each page to Arrow."""
    decoder = ArrowDecoder(operation_id, items_key=items_key, max_violations=max_violations)
    number, fetched = page, 0
    while True:
        current = decoder.decode(raw_method(page=number, page_size=page_size, **kwargs), number)
        yield current
        fetched += 1
        if not current.has_next or (max_pages is not None and fetched >= max_pages):
            return
        number += 1


async def aiter_arrow_pages(
    raw_method: Callable[..., Awaitable[bytes]],
    operation_id: str,
    *,
    page: int = 1,
    page_size: int | None = None,
    max_pages: int | None = None,
    items_key: str = "items",
    max_violations: int = 100,
    **kwargs: Any,
) -> AsyncIterator[ArrowPage]:
    decoder = ArrowDecoder(operation_id, items_key=items_key, max_violations=max_violations)
    number, fetched = page, 0
    while True:
        current = decoder.decode(await raw_method(page=number, page_size=page_size, **kwargs), number)
        yield current
        fetched += 1
        if not current.has_next or (max_pages is not None and fetched >= max_pages):
            return
        number += 1
