'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

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

test('decode validates, demotes and keeps every row', () => {
  const dec = new Decoder(schemas, 'PagedRegionGroups');
  const { ipc, report } = dec.decode(page(1));
  assert.ok(Buffer.isBuffer(ipc) && ipc.length > 100);
  assert.equal(report.rows, 2);
  assert.equal(report.has_next, true);
  assert.equal(report.invalid_rows, 1);
  assert.ok(report.violations.some((v) => v.row === 1 && v.path === '/ISSRate' && /number/.test(v.message)));
  assert.deepEqual(report.demoted_fields, ['ISSRate']);
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
  assert.equal(capped.report.violations.length, 1);
  assert.equal(capped.report.violations_truncated, true);
});
