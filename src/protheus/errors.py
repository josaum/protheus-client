"""Error types. Upstream errors follow the TTALK ``ErrorModel`` envelope."""

from __future__ import annotations

from typing import Any

import httpx


class ProtheusError(Exception):
    """An HTTP error response from Protheus (status >= 400).

    Fields mirror the TTALK ``ErrorModel``: ``code``, ``message``,
    ``detailedMessage``, ``helpUrl`` and ``details[]``. When the body is not a
    TTALK envelope (proxies, HTML error pages), ``code``/``message`` fall back
    to the HTTP status and reason and the raw body is kept in ``body``.
    """

    def __init__(
        self,
        *,
        status_code: int,
        code: str,
        message: str,
        detailed_message: str | None = None,
        help_url: str | None = None,
        details: list[dict[str, Any]] | None = None,
        body: Any = None,
        operation: str | None = None,
        request: httpx.Request | None = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message
        self.detailed_message = detailed_message
        self.help_url = help_url
        self.details = details or []
        self.body = body
        self.operation = operation
        self.request = request
        where = f" [{operation}]" if operation else ""
        super().__init__(f"HTTP {status_code}{where} {code}: {message}")

    @classmethod
    def from_response(cls, response: httpx.Response, operation: str | None = None) -> ProtheusError:
        body: Any
        try:
            body = response.json()
        except ValueError:
            body = response.text
        if isinstance(body, dict) and ("message" in body or "code" in body):
            return cls(
                status_code=response.status_code,
                code=str(body.get("code") or response.status_code),
                message=str(body.get("message") or response.reason_phrase),
                detailed_message=body.get("detailedMessage"),
                help_url=body.get("helpUrl"),
                details=[d for d in body.get("details") or [] if isinstance(d, dict)],
                body=body,
                operation=operation,
                request=response.request,
            )
        return cls(
            status_code=response.status_code,
            code=str(response.status_code),
            message=response.reason_phrase or "HTTP error",
            body=body,
            operation=operation,
            request=response.request,
        )

    @property
    def is_auth_error(self) -> bool:
        return self.status_code in (401, 403)

    @property
    def is_not_found(self) -> bool:
        return self.status_code == 404


class ProtheusTransportError(Exception):
    """The request never produced an HTTP response (DNS, TLS, timeout, refused)."""

    def __init__(self, cause: httpx.RequestError, operation: str | None = None) -> None:
        self.cause = cause
        self.operation = operation
        where = f" [{operation}]" if operation else ""
        super().__init__(f"{type(cause).__name__}{where}: {cause}")
