/** Crate / binding version string. */
export declare function version(): string;

export interface BuildSummary {
  apis: number;
  operations: number;
  apisWithoutProductOperations?: number;
  apis_without_product_operations: number;
  examples_violating_own_schema: number;
}

/**
 * Run the spec engine over a TTALK checkout and write `spec-index.json`,
 * `fixtures.json` and `bundles/<api_id>.json` into `outDir` (default `ttalk-build`).
 */
export declare function buildSpecIndex(repo: string, product?: string, outDir?: string): BuildSummary;

export interface Violation {
  row: number;
  /** JSON pointer inside the row, e.g. `/address/city` or `/contacts/1/email`. */
  path: string;
  message: string;
}

export interface DemotedField {
  name: string;
  from: string;
  to: string;
  reason: string;
}

export interface DecodeReport {
  rows: number;
  invalid_rows: number;
  /** Total violations, including entries omitted by maxViolations. */
  violation_count: number;
  violations: Violation[];
  violations_truncated: boolean;
  /** Fields demoted to Utf8 so far (dotted paths), cumulative for the decoder. */
  demoted_fields: string[];
  /** Cumulative type-change provenance. */
  demotions: DemotedField[];
  has_next: boolean | null;
  fields: Array<{ name: string; type: string }>;
}

export interface DecoderLimits {
  maxInputBytes?: number;
  maxRows?: number;
  maxColumns?: number;
  maxNestingDepth?: number;
  maxStringLength?: number;
  maxArrayLength?: number;
  maxDecodeTimeMs?: number;
  maxIpcBytes?: number;
}

export interface DecodedPage {
  /** Arrow IPC stream; read with `tableFromIPC` from `apache-arrow`. */
  ipc: Buffer;
  report: DecodeReport;
}

/**
 * Decoder for one operation's 2xx response schema. Rows are validated against
 * the bundled JSON Schema and reported, never dropped; a primitive field whose
 * live values cannot be decoded as declared is demoted to Utf8 for the rest of
 * the decoder's life so column types stay stable across pages.
 */
export declare class Decoder {
  /**
   * @param bundleJson the bundled OpenAPI document (or `{"components":{"schemas":…}}`) as a JSON string
   * @param schemaName the response component name, e.g. `PagedCustomerVendors`
   * @param itemsKey   collection property holding the rows (default `items`)
   * @param maxViolations cap on reported violations per page (default 100)
   * @param limits optional structural and decode-time resource budgets
   */
  constructor(bundleJson: string, schemaName: string, itemsKey?: string, maxViolations?: number, limits?: DecoderLimits);
  /** Decode one page synchronously. */
  decode(body: Buffer): DecodedPage;
  /** Decode one page on the libuv thread pool. */
  decodeAsync(body: Buffer): Promise<DecodedPage>;
  /** Current Arrow schema (after any demotions). */
  fields(): Array<{ name: string; type: string }>;
}
