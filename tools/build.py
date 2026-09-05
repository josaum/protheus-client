"""Emit the Python surface of `totvs-protheus` from the ttalk-fast spec engine.

The spec work (loading, `$ref` bundling, normalisation, indexing, example
synthesis, JSON-Schema verdicts) lives in Rust (`crates/ttalk-fast-core`).
This script runs it, then does the Python-only part:

    src/protheus/apis/<api_id>.py      one facade class per API/version
    src/protheus/apis/__init__.py      lazy accessors mixed into the clients
    src/protheus/models/<api_id>.py    pydantic v2 models (datamodel-code-generator)
    src/protheus/spec/schemas/<id>.json bundled component schemas for the runtime decoder
    src/protheus/spec/index.json       the index, with model names verified against the
                                       generated modules and a pydantic verdict per example
    tests/fixtures/responses.json      one schema-derived example per 2xx response

Usage:
    python tools/build.py /path/to/ttalk-standard-message
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

PRODUCT = "Protheus"
STANDARD_QUERY = {
    "fields": "fields",
    "order": "order",
    "page": "page",
    "pageSize": "page_size",
    "filter": "filter",
    "expand": "expand",
}

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "protheus"
BUILD_DIR = ROOT / "build" / "ttalk"


# ------------------------------------------------------------- spec engine
def run_engine(repo: Path, out_dir: Path) -> dict[str, Any]:
    """Prefer the `ttalk_fast` wheel; fall back to the CLI binary or `cargo run`."""
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir(parents=True)
    try:
        import ttalk_fast  # type: ignore[import-not-found]

        return json.loads(ttalk_fast.build_spec_index(str(repo), PRODUCT, str(out_dir)))
    except ImportError:
        pass
    binary = shutil.which("ttalk-fast") or next(
        (
            str(p)
            for p in (ROOT / "target" / "release" / "ttalk-fast", ROOT / "target" / "debug" / "ttalk-fast")
            if p.exists()
        ),
        None,
    )
    cmd = [binary] if binary else ["cargo", "run", "-q", "--release", "-p", "ttalk-fast-cli", "--"]
    result = subprocess.run(
        [*cmd, "index", str(repo), "--product", PRODUCT, "--out", str(out_dir)],
        check=True,
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    return json.loads(result.stdout.strip().splitlines()[-1])


# ------------------------------------------------------------ code emission
HEADER = '"""{title} — generated from {spec_file} (ttalk {commit}). Do not edit by hand."""\n'


def _sig_and_call(op: dict[str, Any]) -> tuple[str, str]:
    args = ["self"]
    for p in op["path_params"]:
        args.append(f"{p['python']}: {p['type']}")
    args.append("*")
    call_path = "{" + ", ".join(f'"{p["name"]}": {p["python"]}' for p in op["path_params"]) + "}"
    if op["request_body"]:
        args.append("body: Body" if op["request_body"]["required"] else "body: Body | None = None")
    for p in op["query_params"] + op["header_params"]:
        args.append(f"{p['python']}: {p['type']} | None = None")
    for name in op["standard_params"]:
        py = STANDARD_QUERY[name]
        typ = "int" if name in ("page", "pageSize") else ("str | list[str]" if name == "order" else "str")
        args.append(f"{py}: {typ} | None = None")
    args.append("extra_query: Mapping[str, Any] | None = None")
    query_items = [f'"{p["name"]}": {p["python"]}' for p in op["query_params"]]
    query_items += [f'"{n}": {STANDARD_QUERY[n]}' for n in op["standard_params"]]
    header_items = [f'"{p["name"]}": {p["python"]}' for p in op["header_params"]]
    call = (
        f'self._request(\n            "{op["id"]}",\n            "{op["method"]}",\n            "{op["path"]}",\n'
        f"            path_params={call_path},\n"
        f"            query={{{', '.join(query_items)}}},\n"
        f"            headers={{{', '.join(header_items)}}},\n"
        f"            body={'body' if op['request_body'] else 'None'},\n"
        f"            extra_query=extra_query,\n        )"
    )
    return ", ".join(args), call


def _docstring(op: dict[str, Any]) -> str:
    lines = [op["summary"] or op["operation_id"] or op["name"]]
    meta = [f"{op['method']} {op['path']}"]
    if op["operation_id"]:
        meta.append(f"operationId={op['operation_id']}")
    if op["minimal_version"]:
        meta.append(f"Protheus >= {op['minimal_version']}")
    if op["availability"] == "inherited":
        meta.append("availability inherited from API level")
    if op["deprecated"]:
        meta.append("DEPRECATED")
    lines.append("")
    lines.append("; ".join(meta))
    if op["description"] and op["description"] != op["summary"]:
        lines += ["", op["description"]]
    if op["note"]:
        lines += ["", f"TOTVS note: {op['note']}"]
    api_id = op["id"].split(".")[0]
    models = [
        f"{label} model: protheus.models.{api_id}.{op[key]}"
        for label, key in (("Response", "response_model"), ("Request", "request_model"))
        if op[key]
    ]
    if models:
        lines += ["", *models]
    body = "\n".join(("        " + line.replace("\\", "\\\\").replace('"""', "'''")) if line else "" for line in lines)
    return f'"""{body.lstrip()}\n        """'


def emit_api_module(api: dict[str, Any], commit: str) -> str:
    out = [HEADER.format(title=api["title"], spec_file=api["spec_file"], commit=commit[:7])]
    out.append("from __future__ import annotations\n\nfrom collections.abc import Mapping\nfrom typing import Any\n\n")
    out.append("from protheus._base import ApiGroup, AsyncApiGroup, Body\n\n")
    for cls, base, prefix in (
        (api["class_name"], "ApiGroup", ""),
        ("Async" + api["class_name"], "AsyncApiGroup", "async "),
    ):
        out.append(f"\nclass {cls}({base}):\n")
        out.append(f'    """{api["title"]} ({api["base_path"]})."""\n\n')
        out.append(f'    api_id = "{api["id"]}"\n    base_path = "{api["base_path"]}"\n')
        for op in api["operations"]:
            sig, call = _sig_and_call(op)
            ret = "None" if not any(s.startswith("2") and r["schema"] for s, r in op["responses"].items()) else "Any"
            out.append(f"\n    {prefix}def {op['name']}({sig}) -> {ret}:\n")
            out.append(f"        {_docstring(op)}\n")
            out.append(f"        return {'await ' if prefix else ''}{call}\n")
    return "".join(out)


def emit_apis_init(apis: list[dict[str, Any]], commit: str) -> str:
    out = [f'"""Generated API accessors (ttalk {commit[:7]}). Do not edit by hand."""\n']
    out.append(
        "from __future__ import annotations\n\nfrom functools import cached_property\nfrom typing import TYPE_CHECKING\n\n"
    )
    out.append("if TYPE_CHECKING:\n")
    for api in apis:
        out.append(f"    from protheus.apis.{api['id']} import {api['class_name']}, Async{api['class_name']}\n")
    out.append("\n\nAPI_IDS: tuple[str, ...] = (\n")
    for api in apis:
        out.append(f'    "{api["id"]}",\n')
    out.append(")\n")
    for cls, prefix in (("SyncApis", ""), ("AsyncApis", "Async")):
        out.append(f"\n\nclass {cls}:\n")
        out.append(f'    """Lazy per-API accessors; mixed into the {"async" if prefix else "sync"} client."""\n')
        for api in apis:
            out.append(f"\n    @cached_property\n    def {api['id']}(self) -> {prefix}{api['class_name']}:\n")
            out.append(f'        """{api["title"]} ({api["base_path"]})."""\n')
            out.append(f"        from protheus.apis.{api['id']} import {prefix}{api['class_name']}\n\n")
            out.append(f"        return {prefix}{api['class_name']}(self)  # type: ignore[arg-type]\n")
    return "".join(out)


def emit_models(api: dict[str, Any], bundled: dict[str, Any], out_path: Path, commit: str) -> None:
    from datamodel_code_generator import DataModelType, InputFileType, generate
    from datamodel_code_generator.format import Formatter, PythonVersion

    generate(
        bundled,
        input_file_type=InputFileType.OpenAPI,
        output=out_path,
        output_model_type=DataModelType.PydanticV2BaseModel,
        target_python_version=PythonVersion.PY_312,
        snake_case_field=True,
        use_standard_collections=True,
        use_union_operator=True,
        field_constraints=True,
        collapse_root_models=True,
        disable_timestamp=True,
        use_double_quotes=True,
        custom_file_header=HEADER.format(title=api["title"], spec_file=api["spec_file"], commit=commit[:7]).rstrip(),
        formatters=[Formatter.BUILTIN],
    )


# ---------------------------------------------------------- verification
def schema_property_names(bundled: dict[str, Any], schema: Any, depth: int = 0) -> set[str] | None:
    """Wire-level property names of an object schema (following $ref/allOf); None if not an object."""
    if not isinstance(schema, dict) or depth > 8:
        return None
    ref = schema.get("$ref")
    if isinstance(ref, str):
        return schema_property_names(bundled, bundled["components"]["schemas"].get(ref.rsplit("/", 1)[-1]), depth + 1)
    names: set[str] = set()
    found = False
    if isinstance(schema.get("properties"), dict):
        names |= set(schema["properties"])
        found = True
    for part in schema.get("allOf") or []:
        sub = schema_property_names(bundled, part, depth + 1)
        if sub is not None:
            names |= sub
            found = True
    if schema.get("type") == "array":
        return None
    return names if found or schema.get("type") == "object" else None


def verify_model_names(apis: list[dict[str, Any]], bundles: dict[str, dict[str, Any]]) -> int:
    """Map each operation's request/response component to the generated class.

    datamodel-code-generator names inline nested objects after their property,
    which can steal a component's name (component ``Status`` -> class ``Status1``
    while an inline ``status`` property becomes ``Status``). So a candidate class
    only counts when its field aliases cover the component's properties; failing
    that we try ``Name<digit>`` siblings, then give up (``None``).
    """
    import importlib

    sys.path.insert(0, str(ROOT / "src"))
    missing = 0
    for api in apis:
        module = importlib.import_module(f"protheus.models.{api['id']}")
        bundled = bundles[api["id"]]
        classes = {n: getattr(module, n) for n in dir(module) if n[:1].isupper()}
        models = {n: c for n, c in classes.items() if hasattr(c, "model_fields")}

        def aliases(cls: Any) -> set[str]:
            return {f.alias or name for name, f in cls.model_fields.items()}

        for op in api["operations"]:
            for key, comp_key in (("request_model", "request"), ("response_model", "response")):
                if not op[key]:
                    continue
                component = (
                    (op["request_body"] or {}).get("schema")
                    if comp_key == "request"
                    else next(
                        (r["schema"] for s, r in op["responses"].items() if s.startswith("2") and r["schema"]), None
                    )
                )
                expected = schema_property_names(bundled, {"$ref": f"#/components/schemas/{component}"})
                wanted = op[key]
                fold = re.sub(r"[^0-9a-z]", "", wanted.lower())
                candidates = [n for n in models if re.fullmatch(rf"{re.escape(wanted)}\d*", n)]
                candidates += [
                    n
                    for n in models
                    if re.sub(r"[^0-9a-z]", "", n.lower()).rstrip("0123456789") == fold and n not in candidates
                ]
                chosen = None
                for name in candidates:
                    if expected is None or expected <= aliases(models[name]):
                        chosen = name
                        break
                if chosen is None:
                    missing += 1
                op[key] = chosen
    return missing


def validate_examples(apis: list[dict[str, Any]], fixtures: dict[str, Any]) -> int:
    """Pydantic verdict per example, stored next to the engine's JSON-Schema verdict."""
    import importlib

    from pydantic import ValidationError

    defects = 0
    for api in apis:
        module = importlib.import_module(f"protheus.models.{api['id']}")
        for op in api["operations"]:
            fixture = fixtures.get(op["id"])
            if fixture is None:
                op["example_validation"] = None
                continue
            if not op["response_model"]:
                continue  # keep the schema verdict only
            try:
                getattr(module, op["response_model"]).model_validate(fixture["body"])
                verdict = {"ok": True, "error": None}
            except ValidationError as exc:
                first = exc.errors()[0]
                loc = ".".join(str(x) for x in first["loc"])
                verdict = {"ok": False, "error": f"{first['type']} at {loc}: {first['msg']}"}
                defects += 1
            except TypeError as exc:
                # e.g. maxLength declared on a numeric property: the constraint itself is invalid
                verdict = {"ok": False, "error": f"invalid_constraint: {exc}"}
                defects += 1
            op["example_validation"]["model"] = verdict
    return defects


# -------------------------------------------------------------------- main
def main(repo_arg: str) -> int:
    repo = Path(repo_arg).resolve()
    summary = run_engine(repo, BUILD_DIR)
    spec = json.loads((BUILD_DIR / "spec-index.json").read_text(encoding="utf-8"))
    fixtures = json.loads((BUILD_DIR / "fixtures.json").read_text(encoding="utf-8"))
    commit = spec["provenance"]["commit"]
    apis: list[dict[str, Any]] = spec["apis"]
    bundles = {
        api["id"]: json.loads((BUILD_DIR / "bundles" / f"{api['id']}.json").read_text(encoding="utf-8")) for api in apis
    }

    for d in (SRC / "apis", SRC / "models", SRC / "spec" / "schemas"):
        d.mkdir(parents=True, exist_ok=True)
        for f in d.iterdir():
            if f.is_file() and f.name != "__init__.py":
                f.unlink()

    for api in apis:
        emit_models(api, bundles[api["id"]], SRC / "models" / f"{api['id']}.py", commit)
        schemas = {"components": {"schemas": bundles[api["id"]]["components"]["schemas"]}}
        (SRC / "spec" / "schemas" / f"{api['id']}.json").write_text(
            json.dumps(schemas, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
        )
    # accessors first: importing protheus.models pulls in protheus.apis via the package __init__
    (SRC / "apis" / "__init__.py").write_text(emit_apis_init(apis, commit), encoding="utf-8")
    (SRC / "models" / "__init__.py").write_text(
        '"""Generated pydantic models, one module per API (see protheus.spec for the index)."""\n', encoding="utf-8"
    )
    unverified = verify_model_names(apis, bundles)
    model_defects = validate_examples(apis, fixtures)
    for api in apis:
        (SRC / "apis" / f"{api['id']}.py").write_text(emit_api_module(api, commit), encoding="utf-8")

    index = {
        "provenance": {
            **spec["provenance"],
            "product": PRODUCT,
            "generator": "crates/ttalk-fast-core + tools/build.py",
        },
        "summary": {
            "apis": summary["apis"],
            "operations": summary["operations"],
            "apis_without_protheus_operations": summary["apis_without_product_operations"],
            "response_examples_violating_json_schema": summary["examples_violating_own_schema"],
            "response_examples_violating_pydantic_model": model_defects,
        },
        "apis": apis,
    }
    (SRC / "spec" / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=1, sort_keys=False) + "\n", encoding="utf-8"
    )
    (ROOT / "tests" / "fixtures" / "responses.json").write_text(
        json.dumps(fixtures, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8"
    )
    print(
        f"apis={summary['apis']} operations={summary['operations']} fixtures={len(fixtures)} "
        f"models_unverified={unverified} schema_defects={summary['examples_violating_own_schema']} "
        f"model_defects={model_defects} commit={commit[:7]}"
    )
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
