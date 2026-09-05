#!/usr/bin/env bash
# Build the N-API artifact for crates/ttalk-fast-node and place it next to its
# index.js loader as ttalk_fast_node.node (+ a platform-suffixed copy), the same
# layout office-parsers-rs/build-node.sh produces for the *-node crates there.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

TARGET_DIR="${CARGO_TARGET_DIR:-$(cargo metadata --no-deps --format-version 1 | python3 -c 'import json,sys;print(json.load(sys.stdin)["target_directory"])')}"
case "$(uname -s)" in
  Darwin) EXT="dylib"; PREFIX="lib" ;;
  Linux)  EXT="so";    PREFIX="lib" ;;
  MINGW*|MSYS*|CYGWIN*) EXT="dll"; PREFIX="" ;;
  *) echo "unsupported OS: $(uname -s)" >&2; exit 1 ;;
esac
case "$(rustc -vV | awk '/^host:/ {print $2}')" in
  aarch64-apple-darwin)      PLATFORM="darwin-arm64" ;;
  x86_64-apple-darwin)       PLATFORM="darwin-x64" ;;
  x86_64-unknown-linux-gnu)  PLATFORM="linux-x64-gnu" ;;
  aarch64-unknown-linux-gnu) PLATFORM="linux-arm64-gnu" ;;
  x86_64-pc-windows-msvc)    PLATFORM="win32-x64-msvc" ;;
  aarch64-pc-windows-msvc)   PLATFORM="win32-arm64-msvc" ;;
  *)                         PLATFORM="$(rustc -vV | awk '/^host:/ {print $2}')" ;;
esac

cargo build --release -p ttalk-fast-node
SRC="$TARGET_DIR/release/${PREFIX}ttalk_fast_node.${EXT}"
[ -f "$SRC" ] || { echo "missing $SRC" >&2; exit 1; }
cp -f "$SRC" crates/ttalk-fast-node/ttalk_fast_node.node
cp -f "$SRC" "crates/ttalk-fast-node/ttalk_fast_node.${PLATFORM}.node"
echo "ok -> crates/ttalk-fast-node/ttalk_fast_node.node (+ .${PLATFORM}.node)"
