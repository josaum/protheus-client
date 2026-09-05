from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx
import pytest

from protheus import AsyncProtheusClient, ProtheusClient

FIXTURES = Path(__file__).parent / "fixtures"
BASE_URL = "http://erp.test:8080/rest"


@pytest.fixture(scope="session")
def responses() -> dict[str, Any]:
    return json.loads((FIXTURES / "responses.json").read_text(encoding="utf-8"))


@dataclass
class Recorder:
    """MockTransport handler that records requests and answers from a queue or a rule."""

    rule: Callable[[httpx.Request], httpx.Response] | None = None
    queue: list[httpx.Response] = field(default_factory=list)
    requests: list[httpx.Request] = field(default_factory=list)
    headers: list[dict[str, str]] = field(default_factory=list)  # snapshot: auth flows mutate the request

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        self.headers.append(dict(request.headers))
        if self.queue:
            return self.queue.pop(0)
        if self.rule:
            return self.rule(request)
        return httpx.Response(200, json={"hasNext": False, "items": []})

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]


@pytest.fixture
def recorder() -> Recorder:
    return Recorder()


@pytest.fixture
def client(recorder: Recorder) -> ProtheusClient:
    with ProtheusClient(BASE_URL, transport=httpx.MockTransport(recorder)) as c:
        yield c


@pytest.fixture
async def aclient(recorder: Recorder) -> AsyncProtheusClient:
    async with AsyncProtheusClient(BASE_URL, transport=httpx.MockTransport(recorder)) as c:
        yield c
