"""Helpers for TTALK paged collections (``{"hasNext": bool, "items": [...]}``)."""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Page:
    number: int
    items: list[Any]
    has_next: bool
    raw: Any = field(repr=False)

    @classmethod
    def from_payload(cls, number: int, payload: Any, items_key: str = "items") -> Page:
        if isinstance(payload, dict):
            items = payload.get(items_key)
            return cls(number, list(items) if isinstance(items, list) else [], bool(payload.get("hasNext")), payload)
        if isinstance(payload, list):  # a few endpoints return a bare array
            return cls(number, payload, False, payload)
        return cls(number, [], False, payload)


def iter_pages(
    fn: Callable[..., Any],
    *,
    page: int = 1,
    page_size: int | None = None,
    items_key: str = "items",
    max_pages: int | None = None,
    **kwargs: Any,
) -> Iterator[Page]:
    """Call ``fn(page=..., page_size=..., **kwargs)`` until ``hasNext`` is false."""
    number = page
    fetched = 0
    while True:
        payload = fn(page=number, page_size=page_size, **kwargs)
        current = Page.from_payload(number, payload, items_key)
        yield current
        fetched += 1
        if not current.has_next or (max_pages is not None and fetched >= max_pages):
            return
        number += 1


def iter_items(fn: Callable[..., Any], **kwargs: Any) -> Iterator[Any]:
    for current in iter_pages(fn, **kwargs):
        yield from current.items


async def aiter_pages(
    fn: Callable[..., Awaitable[Any]],
    *,
    page: int = 1,
    page_size: int | None = None,
    items_key: str = "items",
    max_pages: int | None = None,
    **kwargs: Any,
) -> AsyncIterator[Page]:
    number = page
    fetched = 0
    while True:
        payload = await fn(page=number, page_size=page_size, **kwargs)
        current = Page.from_payload(number, payload, items_key)
        yield current
        fetched += 1
        if not current.has_next or (max_pages is not None and fetched >= max_pages):
            return
        number += 1


async def aiter_items(fn: Callable[..., Awaitable[Any]], **kwargs: Any) -> AsyncIterator[Any]:
    async for current in aiter_pages(fn, **kwargs):
        for item in current.items:
            yield item
