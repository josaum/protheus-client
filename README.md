# totvs-protheus

Typed Python client for the TOTVS Protheus REST APIs, generated from the official
TTALK OpenAPI specifications (`totvs/ttalk-standard-message`). No Mycelia
dependency; runtime needs only `httpx` and `pydantic>=2`, Python 3.12+.

```python
from protheus import ProtheusClient, OAuth2PasswordAuth
from protheus.paging import iter_items
from protheus.models.customer_vendor_v1 import PagedCustomerVendors

client = ProtheusClient(
    "http://erp.example.com:8080/rest",          # everything before /api/…
    auth=OAuth2PasswordAuth("admin", "secret"),  # or BasicAuth / BearerAuth
    accept_language="pt-BR",
)

page = client.customer_vendor_v1.get_customer_vendor_by_entity_type(
    "customer", fields="code,name,shortName", order=["-code"], page=1, page_size=50
)
typed = PagedCustomerVendors.model_validate(page)          # optional typed view

for cv in iter_items(client.customer_vendor_v1.get_customer_vendor_by_entity_type,
                     entity_type="customer", page_size=200):
    ...

client.sales_charge_v1.create_sales_charge(body={...})      # dict or pydantic model
```

`AsyncProtheusClient` has the same surface with `await` (and `paging.aiter_items`).

## What is generated, from what

| Artifact | Source | Notes |
|---|---|---|
| `protheus/spec/index.json` | `jsonschema/apis/*.json` `x-totvs` metadata | 122 APIs, 550 operations; provenance (`commit`, `commit_date`) pinned |
| `protheus/apis/<api>_v<n>.py` | operations available on Protheus | one class per API/version, sync + async, one method per operation |
| `protheus/models/<api>_v<n>.py` | response/request schemas (`jsonschema/schemas`) | pydantic v2, wire names kept as aliases |
| `tests/fixtures/responses.json` | the specs' own `example` values | one example per 2xx response |

Selection rule: an API is included when `info.x-totvs.productInformation`
lists Protheus; an operation is included unless it carries
`available: false` for Protheus. Operations without an operation-level flag
are kept and tagged `availability: "inherited"` (2 of 550, both in
`RetailSalesOrders`). Three Protheus-tagged APIs have no available operation
and are dropped (`Currency`, `ProductSupplierRelationship`, `RetailSales_v2`).

Method names derive from method + path so they never collide
(`operationId`s collide 91 times across specs). Positional arguments are the
path parameters in path order; query, header and standard TTALK parameters
(`fields`, `order`, `page`, `page_size`, `filter`, `expand`) are keyword-only;
`extra_query` passes anything the spec does not declare. Each docstring carries
the TOTVS minimal version and product note verbatim.

## Runtime behaviour

- **Auth.** `BasicAuth`, `BearerAuth`, or `OAuth2PasswordAuth` — password grant
  on `POST <base_url>/api/oauth2/v1/token` with credentials in the query
  string, cached token, refresh grant on expiry, one password re-grant on 401.
  The spec enum says `PASSWORD`/`REFRESH_TOKEN`; TOTVS documentation and
  servers use lowercase, which is what is sent. The auth object is not
  synchronised: concurrent first requests may fetch the token twice.
- **Errors.** Status >= 400 raises `ProtheusError` with the TTALK `ErrorModel`
  fields (`code`, `message`, `detailed_message`, `help_url`, `details`) or the
  raw body when the response is not an envelope. Network failures raise
  `ProtheusTransportError`. Both carry the operation id.
- **Responses** are returned as decoded JSON (`None` on 204). Models are opt-in
  on purpose: real Protheus data violates the spec's enums and lengths often
  enough that strict-by-default parsing would break production reads.
- **Paging.** `paging.iter_pages / iter_items` follow `hasNext`.

## What the specs got wrong (recorded, not hidden)

`tools/build.py` normalises what would otherwise break generation and writes
each fix into `index.json` under the API's `spec_quirks`: draft-03
`required: true` on properties (12 specs), numeric constraints written as
strings (`"999,999,999.99"`), parameters without `name`/`in`, one Latin-1
encoded schema, path parameters missing from `parameters[]`.

Separately, 165 of the 517 spec examples violate the schema they illustrate
(`entityType: "1-Company"` against enum `1..4`, `ISSRate: "5,2"`, date-times
without timezone, enum labels used where codes are declared, `maxLength` on
numbers). The generator validates every example against its model and stores
the verdict on the operation as `example_validation`; the test-suite pins it
both ways, so an upstream fix shows up as a failing test that says
"regenerate". Treat those constraints as unreliable when parsing live data.

## Regenerating

```sh
git clone https://github.com/totvs/ttalk-standard-message
pip install -e '.[dev]'
python tools/build.py ./ttalk-standard-message     # ~6 s, deterministic
TTALK_REPO=./ttalk-standard-message pytest         # 1052 passed, 165 xfailed
```

The determinism test regenerates and asserts `index.json` is byte-identical.

## Using the index without the client

`protheus.spec` exposes the vendored index (`provenance()`, `apis()`,
`iter_operations(side_effect=...)`, `get_operation(id)`) so a catalog, an MCP
tool list or documentation can be built from the same data the facade was.
