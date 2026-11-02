'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');

const { version, Decoder, buildSpecIndex } = require('..');
const schemas = fs.readFileSync(
  path.join(__dirname, '..', '..', '..', 'src', 'protheus', 'spec', 'schemas', 'region_groups_v1.json'),
  'utf8',
);
let arrow = null;
try {
  arrow = require('apache-arrow');
} catch {
  /* optional: deeper IPC checks only when apache-arrow is installed */
}

const page = (n) =>
  Buffer.from(
    JSON.stringify({
      hasNext: n < 2,
      items: [
        { Code: `R${n}`, Description: 'Sul', ISSRate: 5.2 },
        { Code: `Q${n}`, Description: 'Norte', ISSRate: '5,2', TopGroup: 7 },
      ],
    }),
  );

test('version and constructor validation', () => {
  assert.match(version(), /^\d+\.\d+\.\d+$/);
  assert.throws(() => new Decoder('{not json', 'PagedRegionGroups'), /bundleJson/);
  assert.throws(() => new Decoder(schemas, 'Nope'), /unknown schema/);
  assert.equal(typeof buildSpecIndex, 'function');
});

test('archive builds accept explicit provenance without .git', () => {
  const repo = fs.mkdtempSync(path.join(os.tmpdir(), 'ttalk-archive-'));
  try {
    const apiDir = path.join(repo, 'jsonschema', 'apis');
    fs.mkdirSync(apiDir, { recursive: true });
    const minimal = {
      openapi: '3.0.1',
      info: { 'x-totvs': { productInformation: [{ product: 'Protheus' }] } },
      paths: {
        '/minimal': {
          get: {
            operationId: 'getMinimal',
            responses: {
              200: {
                description: 'OK',
                content: { 'application/json': { schema: { type: 'object', properties: { value: { type: 'string' } } } } },
              },
            },
          },
        },
      },
    };
    fs.writeFileSync(path.join(apiDir, 'minimal_v1_000.json'), JSON.stringify(minimal));
    const outDir = path.join(repo, 'out');
    const provenance = { repository: 'https://example.test/archive', commit: 'abc123', commitDate: '2026-01-02T03:04:05Z' };
    const summary = buildSpecIndex(repo, 'Protheus', outDir, provenance);
    assert.equal(summary.apis, 1);
    const index = JSON.parse(fs.readFileSync(path.join(outDir, 'spec-index.json'), 'utf8'));
    assert.deepEqual(index.provenance, { repository: provenance.repository, commit: provenance.commit, commit_date: provenance.commitDate });
  } finally {
    fs.rmSync(repo, { recursive: true, force: true });
  }
});

test('decode validates, demotes and keeps every row', () => {
  const dec = new Decoder(schemas, 'PagedRegionGroups');
  const { ipc, report } = dec.decode(page(1));
  assert.ok(Buffer.isBuffer(ipc) && ipc.length > 100);
  assert.equal(report.rows, 2);
  assert.equal(report.has_next, true);
  assert.equal(report.invalid_rows, 1);
  assert.equal(report.violation_count, 1);
  assert.ok(report.violations.some((v) => v.row === 1 && v.path === '/ISSRate' && /number/.test(v.message)));
  assert.deepEqual(report.demoted_fields, ['ISSRate']);
  assert.deepEqual(report.demotions, [
    { name: 'ISSRate', from: 'Float64', to: 'Utf8', reason: 'invalid_number' },
  ]);
  assert.equal(dec.fields().find((f) => f.name === 'ISSRate').type, 'Utf8');
  if (arrow) {
    const table = arrow.tableFromIPC(ipc);
    assert.equal(table.numRows, 2);
    assert.deepEqual(table.getChild('Code').toArray(), ['R1', 'Q1']);
    assert.deepEqual(table.getChild('ISSRate').toArray(), ['5.2', '5,2']);
  }
});

test('decodeAsync resolves on the thread pool and types stay stable', async () => {
  const dec = new Decoder(schemas, 'PagedRegionGroups', 'items', 10);
  const first = await dec.decodeAsync(page(1));
  const second = await dec.decodeAsync(page(2));
  assert.equal(first.report.has_next, true);
  assert.equal(second.report.has_next, false);
  assert.deepEqual(second.report.demoted_fields, ['ISSRate']);
  assert.equal(second.report.fields.find((f) => f.name === 'ISSRate').type, 'Utf8');
  if (arrow) {
    const t1 = arrow.tableFromIPC(first.ipc);
    const t2 = arrow.tableFromIPC(second.ipc);
    assert.equal(t1.schema.fields.find((f) => f.name === 'ISSRate').type.toString(), t2.schema.fields.find((f) => f.name === 'ISSRate').type.toString());
  }
});

test('empty page and violation cap', () => {
  const dec = new Decoder(schemas, 'PagedRegionGroups', 'items', 1);
  const empty = dec.decode(Buffer.from('{"hasNext":false,"items":[]}'));
  assert.equal(empty.report.rows, 0);
  const capped = dec.decode(Buffer.from(JSON.stringify({ items: [{ Code: 'TOOLONGCODE1' }, { Code: 'TOOLONGCODE2' }] })));
  assert.equal(capped.report.invalid_rows, 2);
  assert.equal(capped.report.violation_count, 2);
  assert.equal(capped.report.violations.length, 1);
  assert.equal(capped.report.violations_truncated, true);
});

test('resource limits have stable errors and malformed JSON remains a decode error', () => {
  const limited = new Decoder(schemas, 'PagedRegionGroups', 'items', 100, { maxRows: 1 });
  assert.throws(() => limited.decode(page(1)), /resource_limit_exceeded: rows limit exceeded/);
  assert.throws(() => limited.decode(Buffer.from('{"items":[}')), /decode_failed: invalid JSON/);
  const ipcLimited = new Decoder(schemas, 'PagedRegionGroups', 'items', 100, { maxIpcBytes: 16 });
  assert.throws(() => ipcLimited.decode(page(1)), /resource_limit_exceeded: ipc_bytes limit exceeded/);
});
