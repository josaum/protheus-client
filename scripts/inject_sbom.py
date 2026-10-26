#!/usr/bin/env python3
"""Embed one CycloneDX SBOM in each native ttalk-fast wheel and refresh RECORD."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import shutil
import tempfile
import zipfile
from pathlib import Path


def distribution(archive: zipfile.ZipFile) -> tuple[str, str]:
    metadata = next(name for name in archive.namelist() if name.endswith(".dist-info/METADATA"))
    info = metadata.split("/", 1)[0]
    for line in archive.read(metadata).decode("utf-8").splitlines():
        if line.startswith("Name: "):
            return line[6:].strip().lower().replace("_", "-"), info
    raise ValueError("wheel carries no distribution name")


def record_row(name: str, payload: bytes) -> list[str]:
    digest = base64.urlsafe_b64encode(hashlib.sha256(payload).digest()).rstrip(b"=").decode("ascii")
    return [name, f"sha256={digest}", str(len(payload))]


def inject(wheel: Path, sbom: Path) -> None:
    payload = sbom.read_bytes()
    document = json.loads(payload)
    if document.get("bomFormat") != "CycloneDX":
        raise ValueError(f"{sbom} is not a CycloneDX document")
    with zipfile.ZipFile(wheel) as archive:
        name, info = distribution(archive)
        if name != "ttalk-fast":
            return
        member = f"{info}/sboms/ttalk-fast-core.cyclonedx.json"
        entries = {item: archive.read(item) for item in archive.namelist() if "/sboms/" not in item}
    entries[member] = payload
    record = f"{info}/RECORD"
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    for item, blob in sorted(entries.items()):
        if item != record:
            writer.writerow(record_row(item, blob))
    writer.writerow([record, "", ""])
    entries[record] = output.getvalue().encode("utf-8")

    with tempfile.NamedTemporaryFile(dir=wheel.parent, suffix=".whl", delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
            for item, blob in sorted(entries.items()):
                metadata = zipfile.ZipInfo(item, date_time=(1980, 1, 1, 0, 0, 0))
                metadata.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(metadata, blob)
        shutil.move(str(temporary), wheel)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", default="artifacts", type=Path)
    parser.add_argument("--sbom", required=True, type=Path)
    args = parser.parse_args()
    count = 0
    for wheel in sorted(args.dist.glob("*.whl")):
        before = wheel.stat().st_size
        inject(wheel, args.sbom)
        with zipfile.ZipFile(wheel) as archive:
            name, _ = distribution(archive)
        if name == "ttalk-fast":
            count += 1
            print(f"embedded {args.sbom.name}: {wheel.name} ({before} -> {wheel.stat().st_size} bytes)")
    if count == 0:
        raise SystemExit("no native ttalk-fast wheels found")


if __name__ == "__main__":
    main()
