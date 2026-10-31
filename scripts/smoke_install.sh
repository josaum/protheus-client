#!/usr/bin/env bash
# Download a published release, verify every artifact, and smoke-test installation.
set -euo pipefail

VERSION="${1:-0.1.1}"
PLATFORM="${2:-auto}"
REPOSITORY="${REPOSITORY:-josaum/protheus-client}"

if [[ "$PLATFORM" == auto ]]; then
  case "$(uname -s)-$(uname -m)" in
    Darwin-arm64) PLATFORM="darwin-arm64" ;;
    Darwin-x86_64) PLATFORM="darwin-x64" ;;
    Linux-x86_64) PLATFORM="linux-x64-gnu" ;;
    Linux-aarch64 | Linux-arm64) PLATFORM="linux-arm64-gnu" ;;
    *) echo "unsupported platform: $(uname -s)-$(uname -m)" >&2; exit 2 ;;
  esac
fi

case "$PLATFORM" in
  darwin-arm64) WHEEL_PLATFORM="macosx_11_0_arm64" ;;
  darwin-x64) WHEEL_PLATFORM="macosx_10_12_x86_64" ;;
  linux-x64-gnu) WHEEL_PLATFORM="manylinux2014_x86_64.manylinux_2_17_x86_64" ;;
  linux-arm64-gnu) WHEEL_PLATFORM="manylinux2014_aarch64.manylinux_2_17_aarch64" ;;
  *) echo "unsupported platform: $PLATFORM" >&2; exit 2 ;;
esac

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
cd "$WORK"
gh release download "v$VERSION" --repo "$REPOSITORY" --dir artifacts
cd artifacts
if command -v sha256sum >/dev/null; then
  sha256sum -c SHA256SUMS
else
  shasum -a 256 -c SHA256SUMS
fi

cat > bundle.json <<'JSON'
{"components":{"schemas":{"Row":{"type":"object","properties":{"rate":{"type":"number"}}},"Page":{"type":"object","properties":{"items":{"type":"array","items":{"$ref":"#/components/schemas/Row"}}}}}}}
JSON
printf '%s\n' '{"items":[{"rate":"5,2"}]}' > page.json

if command -v python3 >/dev/null; then
  python3 -m venv "$WORK/python"
  "$WORK/python/bin/python" -m pip install --quiet \
    "totvs_protheus-$VERSION-py3-none-any.whl" \
    "ttalk_fast-$VERSION-cp38-abi3-$WHEEL_PLATFORM.whl"
  "$WORK/python/bin/python" - <<'PY'
import json
import ttalk_fast
from protheus import JsonLimits, ProtheusClient

bundle = open('bundle.json').read()
decoder = ttalk_fast.Decoder(bundle, 'Page')
ipc, report = decoder.decode(open('page.json', 'rb').read())
report = json.loads(report)
assert ipc and report['rows'] == 1 and report['demoted_fields'] == ['rate']
assert JsonLimits(max_tokens=10) and ProtheusClient
print('Python installation: OK')
PY
fi

if command -v node >/dev/null && command -v npm >/dev/null; then
  mkdir node && cd node
  npm init -y >/dev/null
  npm install --silent "../ttalk-fast-node-$VERSION-$PLATFORM.tgz"
  node - <<'JS'
const { Decoder } = require('ttalk-fast-node');
const fs = require('node:fs');
const decoder = new Decoder(fs.readFileSync('../bundle.json', 'utf8'), 'Page');
const { ipc, report } = decoder.decode(fs.readFileSync('../page.json'));
if (!ipc.length || report.rows !== 1 || report.demoted_fields[0] !== 'rate') {
  throw new Error(JSON.stringify(report));
}
console.log('Node installation: OK');
JS
  cd ..
fi

mkdir cli
tar -xzf "ttalk-fast-cli-$VERSION-$PLATFORM.tar.gz" -C cli
./cli/ttalk-fast decode bundle.json Page page.json >/dev/null
echo "CLI installation: OK"
echo "Release v$VERSION ($PLATFORM): all available installation checks passed"
