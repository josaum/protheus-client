"""Bounded ordinary JSON decoding without a native parser dependency."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class JsonLimits:
    """Conservative budgets applied before constructing Python JSON objects."""

    max_input_bytes: int = 64 * 1024 * 1024
    max_tokens: int = 1_000_000
    max_retained_bytes: int = 64 * 1024 * 1024


class JsonResourceError(ValueError):
    """A JSON response exceeded a configured pre-materialization budget."""

    code = "resource_limit_exceeded"

    def __init__(self, resource: str, observed: int, limit: int) -> None:
        self.resource = resource
        self.observed = observed
        self.limit = limit
        super().__init__(f"{self.code}: {resource} limit exceeded ({observed} > {limit})")


def _check(resource: str, observed: int, limit: int) -> None:
    if observed > limit:
        raise JsonResourceError(resource, observed, limit)


def _preflight(text: str, input_bytes: int, limits: JsonLimits) -> None:
    _check("input_bytes", input_bytes, limits.max_input_bytes)
    tokens = 0
    index = 0
    length = len(text)
    while index < length:
        char = text[index]
        if char in " \t\r\n,:":
            index += 1
            continue
        if char in "]}":
            index += 1
            continue
        tokens += 1
        _check("tokens", tokens, limits.max_tokens)
        if char == '"':
            index += 1
            escaped = False
            while index < length:
                char = text[index]
                index += 1
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    break
            continue
        index += 1
        while index < length and text[index] not in ' \t\r\n,:[]{}"':
            index += 1
    # A deliberately conservative upper-bound proxy, checked before json.loads
    # allocates its dict/list/scalar tree. It is a budget, not an RSS estimate.
    retained_bytes = input_bytes + tokens * 64
    _check("retained_bytes", retained_bytes, limits.max_retained_bytes)


def decode_json(content: bytes, limits: JsonLimits) -> Any:
    """Decode UTF-8 JSON after enforcing aggregate input and output budgets."""

    text = content.decode("utf-8")
    _preflight(text, len(content), limits)
    return json.loads(text)
