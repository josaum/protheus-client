from __future__ import annotations

import httpx

from protheus import AsyncProtheusClient, ProtheusClient
from protheus.paging import Page, aiter_items, aiter_pages, iter_items, iter_pages

from conftest import Recorder


def _pages(request: httpx.Request) -> httpx.Response:
    page = int(request.url.params.get("page", "1"))
    return httpx.Response(200, json={"hasNext": page < 3, "items": [f"p{page}a", f"p{page}b"]})


def test_iter_pages_follows_has_next(recorder: Recorder) -> None:
    recorder.rule = _pages
    with ProtheusClient("http://x/rest", transport=httpx.MockTransport(recorder)) as client:
        pages = list(
            iter_pages(
                client.customer_vendor_v1.get_customer_vendor_by_entity_type, entity_type="customer", page_size=2
            )
        )
    assert [p.number for p in pages] == [1, 2, 3]
    assert [p.has_next for p in pages] == [True, True, False]
    assert all(r.url.params["pageSize"] == "2" for r in recorder.requests)
    assert [r.url.params["page"] for r in recorder.requests] == ["1", "2", "3"]


def test_iter_items_flattens_and_max_pages_caps(recorder: Recorder) -> None:
    recorder.rule = _pages
    with ProtheusClient("http://x/rest", transport=httpx.MockTransport(recorder)) as client:
        items = list(iter_items(client.user_v1.list_users, max_pages=2))
    assert items == ["p1a", "p1b", "p2a", "p2b"]


def test_page_from_bare_array_and_junk() -> None:
    assert Page.from_payload(1, [1, 2]).items == [1, 2]
    assert Page.from_payload(1, "nope").items == []
    assert not Page.from_payload(1, {"items": "x"}).has_next


async def test_async_paging(recorder: Recorder) -> None:
    recorder.rule = _pages
    async with AsyncProtheusClient("http://x/rest", transport=httpx.MockTransport(recorder)) as client:
        numbers = [p.number async for p in aiter_pages(client.user_v1.list_users)]
        items = [i async for i in aiter_items(client.user_v1.list_users, max_pages=1)]
    assert numbers == [1, 2, 3]
    assert items == ["p1a", "p1b"]
