"""Typed Python client for the TOTVS Protheus REST APIs (TTALK standard)."""

from protheus.auth import BasicAuth, BearerAuth, OAuth2PasswordAuth
from protheus.client import AsyncProtheusClient, ProtheusClient
from protheus.errors import ProtheusError, ProtheusTransportError
from protheus.paging import Page

__all__ = [
    "AsyncProtheusClient",
    "BasicAuth",
    "BearerAuth",
    "OAuth2PasswordAuth",
    "Page",
    "ProtheusClient",
    "ProtheusError",
    "ProtheusTransportError",
]
