# Protheus Client

Typed Python and Node clients for TOTVS Protheus REST APIs, with a fast Rust Arrow decoder and deterministic generation from the official TTALK specifications.

## Coverage

The generated client covers the complete available Protheus surface:

- **122 / 122 usable Protheus APIs**
- **550 / 550 available operations**
- **100.0% operation coverage**
- JSON request and response support across the available surface

The coverage audit regenerates from the official repository and fails CI if available operations are missing or generated files drift from the pinned source.

## Highlights

- Synchronous and asynchronous Python APIs.
- Node-API bindings with synchronous and asynchronous decoding.
- DOM-free JSON-to-Arrow conversion with nested structs and lists.
- Schema violation totals, row-level findings, and field-demotion provenance.
- Configurable input, structure, retained-memory, decode-time, and Arrow IPC output limits.
- Cross-platform wheels, Node packages, and CLI archives.
- CycloneDX SBOMs, source-commit manifests, and independently verified checksums.

## Install

Download the current release and platform-specific artifacts from [GitHub Releases](https://github.com/josaum/protheus-client/releases).

For the pure Python client:

```bash
python -m pip install https://github.com/josaum/protheus-client/releases/download/v0.1.2/totvs_protheus-0.1.2-py3-none-any.whl
```

For Arrow decoding, install `pyarrow` and the native `ttalk-fast` wheel matching your platform:

```bash
python -m pip install pyarrow
python -m pip install https://github.com/josaum/protheus-client/releases/download/v0.1.2/ttalk_fast-0.1.2-cp38-abi3-macosx_11_0_arm64.whl
```

Replace the wheel filename with the Linux x86_64, Linux arm64, or macOS Intel asset as needed.

Node packages and CLI archives are available for Linux x86_64/arm64 and macOS x86_64/arm64.

## Python usage

```python
from protheus import ProtheusClient

with ProtheusClient("http://erp.example.com:8080/rest") as client:
    result = client.customer_vendor_v1.get_customer_vendor_by_entity_type("customer")
    print(result)
```

Arrow decoding:

```python
from protheus import arrow

with ProtheusClient("http://erp.example.com:8080/rest") as client:
    group = arrow.raw(client.region_groups_v1)
    for page in arrow.iter_arrow_pages(group.list_regiongroups, "region_groups_v1.list_regiongroups"):
        print(page.report.rows, page.report.violation_count)
        table = page.to_pyarrow()
```

Async decoding uses `ArrowDecoder.adecode()` to keep large-page processing off the event-loop thread.

## Verify a release

The installation smoke script downloads all release assets, verifies `SHA256SUMS`, and tests Python, Node, and CLI installation on the detected platform:

```bash
./scripts/smoke_install.sh
```

Pass a different release version and platform as optional arguments.

## Development

Requirements include Rust/Cargo, Python 3.12+, Node, and `uv`.

```bash
cargo test --workspace --locked
npm test --prefix crates/ttalk-fast-node
uv run --no-project --with ruff ruff check src tests tools scripts
```

Regenerate the client from an official TTALK checkout:

```bash
python tools/build.py /path/to/ttalk-standard-message
python tools/coverage.py /path/to/ttalk-standard-message
```

The coverage command reports source and generated API counts, operation coverage, and unsupported content types. CI also runs deterministic regeneration, cross-platform tests, release builds, SBOM generation, and checksum verification.

## Documentation

- [Protheus client guide](docs/PROTHEUS-CLIENT.md)
- [Releases and installation assets](https://github.com/josaum/protheus-client/releases)
- [Community discussions](https://github.com/josaum/protheus-client/discussions)
