'use strict';
// Loader: prefer the platform-specific artifact, fall back to the generic one
// (both are written by ../../build-node.sh next to this file).
const { platform, arch } = process;
const candidates = [
  `./ttalk_fast_node.${platform}-${arch}${platform === 'linux' ? '-gnu' : platform === 'win32' ? '-msvc' : ''}.node`,
  './ttalk_fast_node.node',
];
let native = null;
let lastError = null;
for (const candidate of candidates) {
  try {
    native = require(candidate);
    break;
  } catch (error) {
    lastError = error;
  }
}
if (!native) {
  throw new Error(`ttalk-fast-node: native module not built for ${platform}-${arch}; run build-node.sh (${lastError && lastError.message})`);
}

module.exports = {
  version: native.version,
  buildSpecIndex: native.buildSpecIndex,
  Decoder: native.Decoder,
};
