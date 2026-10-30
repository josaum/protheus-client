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

import asyncio
import json
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from dataclasses import dataclass, field
from functools import cache
from importlib import resources
from typing import Any

from protheus import spec
from protheus._base import ApiGroup, AsyncApiGroup, PreparedRequest

try:
    import ttalk_fast  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - exercised only without the wheel
    ttalk_fast = None

AVAILABLE = ttalk_fast is not None
DecodeError = getattr(ttalk_fast, "DecodeError", ValueError)
ResourceLimitError = getattr(ttalk_fast, "ResourceLimitError", DecodeError)


def _require() -> Any:
    if ttalk_fast is None:
        raise ImportError(
            "protheus.arrow needs the ttalk_fast extension: pip install ttalk-fast "
            "(or: maturin develop -m crates/ttalk-fast-py/Cargo.toml)"
        )
    return ttalk_fast


@cache
def components_json(api_id: str) -> str:
    """The bundled ``components.schemas`` document vendored for one API."""
    with resources.files("protheus.spec").joinpath("schemas", f"{api_id}.json").open("r", encoding="utf-8") as fh:
        return fh.read()


@dataclass(slots=True)
class DecodeLimits:
    """Resource budgets for one decoder; string lengths are UTF-8 source bytes."""

    max_input_bytes: int = 64 * 1024 * 1024
    max_rows: int = 1_000_000
    max_columns: int = 1_024
    max_nesting_depth: int = 64
    max_string_length: int = 16 * 1024 * 1024
    max_array_length: int = 1_000_000
    max_decode_time_ms: int = 30_000
    max_ipc_bytes: int = 64 * 1024 * 1024

    def to_dict(self) -> dict[str, int]:
        return {name: getattr(self, name) for name in self.__slots__}


@dataclass(slots=True)
class Violation:
    row: int
    path: str
    message: str


@dataclass(slots=True)
class DemotedField:
    name: str
    from_type: str
    to_type: str
    reason: str


@dataclass(slots=True)
class FieldInfo:
    name: str
    type: str


@dataclass(slots=True)
class DecodeReport(Mapping[str, Any]):
    """Typed report with mapping access retained for existing consumers."""

    rows: int
    invalid_rows: int
    violation_count: int
    violations: list[Violation]
    violations_truncated: bool
    demoted_fields: list[str]
    demotions: list[DemotedField]
    has_next: bool | None
    fields: list[FieldInfo]
    _data: dict[str, Any] = field(default_factory=dict, repr=False, compare=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DecodeReport:
        return cls(
            rows=data["rows"],
            invalid_rows=data["invalid_rows"],
            violation_count=data.get("violation_count", len(data["violations"])),
            violations=[Violation(**item) for item in data["violations"]],
            violations_truncated=data["violations_truncated"],
            demoted_fields=data["demoted_fields"],
            demotions=[
                DemotedField(item["name"], item["from"], item["to"], item["reason"])
                for item in data.get("demotions", [])
            ],
            has_next=data["has_next"],
            fields=[FieldInfo(**item) for item in data["fields"]],
            _data=data,
        )

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def to_dict(self) -> dict[str, Any]:
        """Return the JSON-compatible report representation."""
        return dict(self._data)


@dataclass(slots=True)
class ArrowPage:
    number: int
    ipc: bytes
    report: DecodeReport

    @property
    def rows(self) -> int:
        return self.report.rows

    @property
    def has_next(self) -> bool:
        return bool(self.report.has_next)

    def to_pyarrow(self) -> Any:
        import pyarrow.ipc  # optional dependency

        return pyarrow.ipc.open_stream(self.ipc).read_all()


class ArrowDecoder:
    """Decoder for one operation's 2xx response schema."""

    def __init__(
        self,
        operation_id: str,
        *,
        items_key: str = "items",
        max_violations: int = 100,
        limits: DecodeLimits | Mapping[str, int] | None = None,
    ) -> None:
        engine = _require()
        op = spec.get_operation(operation_id)
        schema = next((r["schema"] for s, r in op["responses"].items() if s.startswith("2") and r["schema"]), None)
        if schema is None:
            raise ValueError(f"{operation_id} declares no 2xx response schema")
        self.operation_id = operation_id
        self.schema_name = schema
        configured_limits = (
            limits.to_dict() if isinstance(limits, DecodeLimits) else dict(limits) if limits is not None else None
        )
        self._inner = engine.Decoder(
            components_json(op["api_id"]), schema, items_key, max_violations, configured_limits
        )

    def decode(self, body: bytes, number: int = 1) -> ArrowPage:
        ipc, report = self._inner.decode(body)
        return ArrowPage(number, ipc, DecodeReport.from_dict(json.loads(report)))

    async def adecode(self, body: bytes, number: int = 1) -> ArrowPage:
        """Decode without blocking the event loop on large pages."""
        return await asyncio.to_thread(self.decode, body, number)

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
    limits: DecodeLimits | Mapping[str, int] | None = None,
    **kwargs: Any,
) -> Iterator[ArrowPage]:
    """Page through ``raw_method(page=..., page_size=..., **kwargs)`` decoding each page to Arrow."""
    decoder = ArrowDecoder(
        operation_id, items_key=items_key, max_violations=max_violations, limits=limits
    )
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
    limits: DecodeLimits | Mapping[str, int] | None = None,
    **kwargs: Any,
) -> AsyncIterator[ArrowPage]:
    decoder = ArrowDecoder(
        operation_id, items_key=items_key, max_violations=max_violations, limits=limits
    )
    number, fetched = page, 0
    while True:
        current = await decoder.adecode(await raw_method(page=number, page_size=page_size, **kwargs), number)
        yield current
        fetched += 1
        if not current.has_next or (max_pages is not None and fetched >= max_pages):
            return
        number += 1
