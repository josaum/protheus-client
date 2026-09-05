"""Generate the Protheus client surface from the TOTVS TTALK OpenAPI specs.

Input : a checkout of https://github.com/totvs/ttalk-standard-message
Output: src/protheus/spec/index.json      operation index + provenance
        src/protheus/apis/<api_id>.py     one facade class per API/version
        src/protheus/apis/__init__.py     lazy accessors mixed into the clients
        src/protheus/models/<api_id>.py   pydantic v2 models (datamodel-code-generator)
        tests/fixtures/responses.json     one schema-derived example per 2xx response

Only operations available on Protheus are emitted: the API must list Protheus in
``info.x-totvs.productInformation`` and the operation must not carry
``available: false`` for Protheus. Operations with no operation-level flag are
kept and tagged ``availability = "inherited"``.

Usage:
    python tools/build.py /path/to/ttalk-standard-message
"""

from __future__ import annotations

import json
import keyword
import re
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any

RAW_PREFIX = "https://raw.githubusercontent.com/totvs/ttalk-standard-message/master/"
PRODUCT = "Protheus"
HTTP_METHODS = ("get", "post", "put", "patch", "delete")
STANDARD_QUERY = {
    "fields": "fields",
    "order": "order",
    "page": "page",
    "pageSize": "page_size",
    "filter": "filter",
    "expand": "expand",
}
CLIENT_MANAGED_HEADERS = {"authorization", "accept-language"}

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "protheus"


# --------------------------------------------------------------------------- io
def load_json(path: Path) -> Any:
    raw = path.read_bytes()
    try:
        return json.loads(raw.decode("utf-8-sig"))
    except UnicodeDecodeError:
        # One TTALK schema (StopReport) is Latin-1 encoded.
        return json.loads(raw.decode("latin-1"))


def git_provenance(repo: Path) -> dict[str, str]:
    def git(*args: str) -> str:
        return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()

    return {
        "repository": "https://github.com/totvs/ttalk-standard-message",
        "commit": git("rev-parse", "HEAD"),
        "commit_date": git("log", "-1", "--format=%cI"),
    }


# ------------------------------------------------------------------ naming utils
def snake(name: str) -> str:
    s = re.sub(r"[^0-9A-Za-z]+", "_", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = re.sub(r"_+", "_", s).strip("_").lower()
    if not s:
        s = "x"
    if s[0].isdigit():
        s = "n_" + s
    if keyword.iskeyword(s):
        s += "_"
    return s


def pascal(name: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in snake(name).split("_"))


def api_stem_and_version(filename: str) -> tuple[str, str, str]:
    """'CustomerVendor_v1_000.json' -> ('CustomerVendor', '1', '1_000')."""
    m = re.match(r"^(.*?)_v(\d+)(?:_(\d+))?\.json$", filename)
    if not m:
        raise ValueError(f"unexpected spec filename: {filename}")
    stem, major, minor = m.group(1), m.group(2), m.group(3) or "0"
    return stem, major, f"{major}_{minor}"


# ------------------------------------------------------------------- bundling
class Bundler:
    """Rewrite one TTALK spec into a self-contained OpenAPI 3 document.

    External ``$ref``s (absolute GitHub URLs and cross-file relative paths) are
    copied into ``components/schemas`` / ``components/parameters`` under stable,
    readable names. Draft-03 style ``required: true`` on properties is folded
    into the parent's ``required`` list (12 Protheus specs still use it).
    """

    def __init__(self, repo: Path, spec_path: Path) -> None:
        self.repo = repo
        self.spec_path = spec_path
        self.docs: dict[Path, Any] = {}
        self.names: dict[tuple[Path, str], str] = {}
        self.quirks: list[str] = []
        self.spec = self._doc(spec_path)
        comps = self.spec.setdefault("components", {})
        comps.setdefault("schemas", {})
        comps.setdefault("parameters", {})

    def _doc(self, path: Path) -> Any:
        if path not in self.docs:
            self.docs[path] = load_json(path)
        return self.docs[path]

    def _target_file(self, current: Path, ref: str) -> Path:
        target = ref.partition("#")[0]
        if not target:
            return current
        if target.startswith(RAW_PREFIX):
            return self.repo / target[len(RAW_PREFIX) :]
        if target.startswith("http"):
            raise ValueError(f"unsupported external ref {ref} in {current}")
        return (current.parent / target).resolve()

    @staticmethod
    def _deref(doc: Any, fragment: str) -> Any:
        node = doc
        for part in fragment.lstrip("#/").split("/"):
            if part:
                node = node[part.replace("~1", "/").replace("~0", "~")]
        return node

    def _component_name(self, file: Path, fragment: str, section: str) -> str:
        key = (file, fragment)
        if key in self.names:
            return self.names[key]
        last = re.sub(r"[^A-Za-z0-9_]", "_", fragment.rstrip("/").split("/")[-1])
        stem = re.sub(r"_\d+_\d+$", "", file.stem)  # CustomerVendor_2_008 -> CustomerVendor
        bucket = self.spec["components"][section]
        candidates = [last, f"{stem}_{last}", f"{file.stem}_{last}"]
        for cand in candidates:
            if cand not in bucket:
                self.names[key] = cand
                bucket[cand] = None  # reserve
                return cand
        n = 2
        while f"{file.stem}_{last}_{n}" in bucket:
            n += 1
        name = f"{file.stem}_{last}_{n}"
        self.names[key] = name
        bucket[name] = None
        return name

    def _rewrite(self, node: Any, current: Path) -> Any:
        if isinstance(node, list):
            return [self._rewrite(v, current) for v in node]
        if not isinstance(node, dict):
            return node
        ref = node.get("$ref")
        if isinstance(ref, str):
            file = self._target_file(current, ref)
            fragment = ref.partition("#")[2]
            if file == self.spec_path and fragment.startswith("/components/"):
                return node
            section = "parameters" if fragment.startswith("/parameters/") else "schemas"
            key = (file, fragment)
            if key not in self.names:
                name = self._component_name(file, fragment, section)
                target = self._deref(self._doc(file), fragment)
                self.spec["components"][section][name] = self._rewrite(json.loads(json.dumps(target)), file)
            else:
                name = self.names[key]
            out = {k: v for k, v in node.items() if k != "$ref"}
            out["$ref"] = f"#/components/{section}/{name}"
            return out
        return {k: self._rewrite(v, current) for k, v in node.items()}

    @staticmethod
    def _fold_draft3_required(node: Any) -> None:
        """Move draft-03 ``required: <bool>`` from property schemas to the parent list."""
        if isinstance(node, list):
            for v in node:
                Bundler._fold_draft3_required(v)
            return
        if not isinstance(node, dict):
            return
        props = node.get("properties")
        if isinstance(props, dict):
            req = list(node["required"]) if isinstance(node.get("required"), list) else []
            for pname, pschema in props.items():
                if isinstance(pschema, dict) and isinstance(pschema.get("required"), bool):
                    if pschema.pop("required") and pname not in req:
                        req.append(pname)
            if req:
                node["required"] = req
        if isinstance(node.get("required"), bool):
            del node["required"]
        for k, v in node.items():
            if k not in ("example", "examples", "default", "enum", "x-totvs"):
                Bundler._fold_draft3_required(v)

    _NUMERIC_KEYS = ("maximum", "minimum", "exclusiveMaximum", "exclusiveMinimum", "multipleOf")
    _INT_KEYS = ("maxLength", "minLength", "maxItems", "minItems", "maxProperties", "minProperties")

    def _sanitize(self, node: Any, where: str = "") -> None:
        """Coerce numeric constraints written as strings ('999,999,999.99', '50')."""
        if isinstance(node, list):
            for i, v in enumerate(node):
                self._sanitize(v, f"{where}[{i}]")
            return
        if not isinstance(node, dict):
            return
        for key in (*self._NUMERIC_KEYS, *self._INT_KEYS):
            val = node.get(key)
            if isinstance(val, str):
                try:
                    num = float(val.replace(",", "")) if key in self._NUMERIC_KEYS else int(float(val.replace(",", "")))
                    node[key] = num
                    self.quirks.append(f"{where}.{key}: string constraint {val!r} coerced to {num}")
                except ValueError:
                    del node[key]
                    self.quirks.append(f"{where}.{key}: unparsable constraint {val!r} dropped")
        for k, v in node.items():
            if k not in ("example", "examples", "default", "enum", "x-totvs"):
                self._sanitize(v, f"{where}.{k}" if where else k)

    def bundle(self) -> dict[str, Any]:
        spec = self.spec
        # Local components declared by the spec itself may hold external refs too.
        own = {s: list(spec["components"][s]) for s in ("parameters", "schemas")}
        spec["paths"] = self._rewrite(spec["paths"], self.spec_path)
        for section, names in own.items():
            for name in names:
                spec["components"][section][name] = self._rewrite(spec["components"][section][name], self.spec_path)
        for section in ("parameters", "schemas"):
            unresolved = [n for n, v in spec["components"][section].items() if v is None]
            if unresolved:
                raise RuntimeError(f"{self.spec_path.name}: unresolved {section} {unresolved}")
        self._fold_draft3_required(spec["components"]["schemas"])
        for param in spec["components"]["parameters"].values():
            if isinstance(param, dict) and "schema" in param:
                self._fold_draft3_required(param["schema"])
        self._sanitize(spec["components"]["schemas"], "schemas")
        self._sanitize(spec["components"]["parameters"], "parameters")
        return spec


# --------------------------------------------------------------- indexing ops
def protheus_op_availability(op: dict[str, Any]) -> tuple[str, dict[str, Any]] | None:
    infos = ((op.get("x-totvs") or {}).get("productInformation")) or []
    for info in infos:
        if isinstance(info, dict) and info.get("product") == PRODUCT:
            if info.get("available") is False:
                return None
            return "declared", info
    return "inherited", {}


def resolve_param(spec: dict[str, Any], p: dict[str, Any], quirks: list[str] | None = None) -> dict[str, Any]:
    key = None
    if "$ref" in p:
        key = p["$ref"].rsplit("/", 1)[-1]
        p = spec["components"]["parameters"][key]
    if not p.get("name") or not p.get("in"):
        fixed = {**p, "name": p.get("name") or key or "param", "in": p.get("in") or "query"}
        if quirks is not None:
            quirks.append(f"parameter '{fixed['name']}' lacks name/in; assumed query parameter")
        return fixed
    return p


def schema_ref_name(schema: Any) -> str | None:
    if isinstance(schema, dict) and isinstance(schema.get("$ref"), str):
        return schema["$ref"].rsplit("/", 1)[-1]
    return None


def method_name(method: str, path: str) -> str:
    parts = [p for p in path.strip("/").split("/") if p]
    words: list[str] = []
    trailing_param = False
    for part in parts:
        if part.startswith("{"):
            words.append(("and_" if trailing_param else "by_") + snake(part.strip("{}")))
            trailing_param = True
        else:
            words.append(snake(part))
            trailing_param = False
    verb = {
        "get": "get" if trailing_param else "list",
        "post": "create",
        "put": "update",
        "patch": "patch",
        "delete": "delete",
    }[method]
    return "_".join([verb, *words])


def python_type(schema: dict[str, Any] | None) -> str:
    if not schema:
        return "str"
    t = schema.get("type")
    if isinstance(t, list):
        t = next((x for x in t if x != "null"), "string")
    return {
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "list[str]",
        "object": "dict[str, Any]",
    }.get(t, "str")


def assign_api_ids(filenames: list[str]) -> dict[str, str]:
    """filename -> api_id. Same stem+major twice (JobScheduler v1_001/v1_100) keeps the full version."""
    groups: dict[str, list[str]] = {}
    for fn in filenames:
        stem, major, _ = api_stem_and_version(fn)
        groups.setdefault(f"{snake(stem)}_v{major}", []).append(fn)
    ids: dict[str, str] = {}
    for short, members in groups.items():
        for fn in members:
            ids[fn] = (
                short if len(members) == 1 else f"{snake(api_stem_and_version(fn)[0])}_v{api_stem_and_version(fn)[2]}"
            )
    return ids


def _unique_arg_names(op: dict[str, Any]) -> None:
    reserved = {"self", "body", "extra_query", *STANDARD_QUERY.values()}
    for group in ("path_params", "query_params", "header_params"):
        for p in op[group]:
            name = p["python"]
            while name in reserved:
                name += {"path_params": "_path", "query_params": "_q", "header_params": "_h"}[group]
            p["python"] = name
            reserved.add(name)


def index_api(filename: str, api_id: str, spec: dict[str, Any]) -> dict[str, Any] | None:
    info = spec["info"]
    xt = info.get("x-totvs") or {}
    product_infos = [p for p in (xt.get("productInformation") or []) if isinstance(p, dict)]
    prod = next((p for p in product_infos if p.get("product") == PRODUCT), None)
    if prod is None:
        return None
    stem = api_stem_and_version(filename)[0]

    server_url = spec["servers"][0]["url"]
    base_path = "/" + server_url.split("/api/", 1)[1] if "/api/" in server_url else server_url
    base_path = "/api/" + base_path.lstrip("/")

    operations: list[dict[str, Any]] = []
    seen_methods: set[str] = set()
    quirks: list[str] = []
    for path, item in spec["paths"].items():
        path_level_params = [resolve_param(spec, p, quirks) for p in item.get("parameters", [])]
        for method in HTTP_METHODS:
            op = item.get(method)
            if not op:
                continue
            avail = protheus_op_availability(op)
            if avail is None:
                continue
            availability, pinfo = avail
            params = path_level_params + [resolve_param(spec, p, quirks) for p in op.get("parameters", [])]
            path_params, query_params, header_params, standard = [], [], [], []
            for p in params:
                loc, name = p.get("in"), p.get("name")
                entry = {
                    "name": name,
                    "python": snake(name),
                    "required": bool(p.get("required")),
                    "type": python_type(p.get("schema")),
                    "description": (p.get("description") or "").strip(),
                }
                if loc == "path":
                    entry["required"] = True
                    entry["type"] = "str"  # a path segment is a string whatever the schema says
                    path_params.append(entry)
                elif loc == "query":
                    if name in STANDARD_QUERY:
                        standard.append(name)
                    else:
                        query_params.append(entry)
                elif loc == "header":
                    if name.lower() not in CLIENT_MANAGED_HEADERS:
                        header_params.append(entry)
            # path params declared in the template but missing from parameters[]
            for tmpl in re.findall(r"{([^}]+)}", path):
                if all(pp["name"] != tmpl for pp in path_params):
                    quirks.append(f"{method.upper()} {path}: path parameter '{tmpl}' not declared; added")
                    path_params.append(
                        {"name": tmpl, "python": snake(tmpl), "required": True, "type": "str", "description": ""}
                    )
            # positional arguments follow the path template, not the spec's declaration order
            order_in_path = {name: i for i, name in enumerate(re.findall(r"{([^}]+)}", path))}
            path_params.sort(key=lambda pp: order_in_path.get(pp["name"], len(order_in_path)))
            body = None
            rb = op.get("requestBody")
            if rb:
                content = rb.get("content") or {}
                ctype = "application/json" if "application/json" in content else next(iter(content), None)
                body = {
                    "required": bool(rb.get("required", True)),
                    "content_type": ctype,
                    "schema": schema_ref_name((content.get(ctype) or {}).get("schema")) if ctype else None,
                }
            responses = OrderedDict()
            for status, resp in (op.get("responses") or {}).items():
                content = (resp or {}).get("content") or {}
                js = content.get("application/json") or {}
                responses[str(status)] = {
                    "description": (resp or {}).get("description", ""),
                    "schema": schema_ref_name(js.get("schema")),
                }
            name = method_name(method, path)
            while name in seen_methods:
                name += "_"
            seen_methods.add(name)
            ok_schema = next((r["schema"] for s, r in responses.items() if s.startswith("2") and r["schema"]), None)
            operations.append(
                {
                    "id": f"{api_id}.{name}",
                    "name": name,
                    "operation_id": op.get("operationId"),
                    "method": method.upper(),
                    "path": path,
                    "summary": (op.get("summary") or "").strip(),
                    "description": (op.get("description") or "").strip(),
                    "deprecated": bool(op.get("deprecated")),
                    "side_effect": method != "get",
                    "availability": availability,
                    "minimal_version": pinfo.get("minimalVersion") or None,
                    "note": (pinfo.get("note") or "").strip() or None,
                    "path_params": path_params,
                    "query_params": query_params,
                    "header_params": header_params,
                    "standard_params": standard,
                    "request_body": body,
                    "responses": responses,
                    "request_model": model_class(body["schema"]) if body and body.get("schema") else None,
                    "response_model": model_class(ok_schema) if ok_schema else None,
                }
            )
            _unique_arg_names(operations[-1])
    if not operations:
        return None
    return {
        "id": api_id,
        "class_name": pascal(api_id),
        "spec_file": filename,
        "title": (info.get("title") or stem).strip(),
        "description": (info.get("description") or "").strip(),
        "version": info.get("version"),
        "segment": ((xt.get("messageDocumentation") or {}).get("segment") or "").strip() or None,
        "base_path": base_path,
        "product_info": {
            "contact": prod.get("contact") or None,
            "description": (prod.get("description") or "").strip() or None,
            "adapter": prod.get("adapter") or None,
        },
        "spec_quirks": sorted(set(quirks)),
        "operations": operations,
    }


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


def model_class(component: str) -> str:
    """Mirror datamodel-code-generator's class naming: split on non-alphanumerics,
    capitalise each part's first letter, keep the rest (acronyms survive)."""
    parts = [p for p in re.split(r"[^0-9A-Za-z]+", component) if p]
    name = "".join(p[:1].upper() + p[1:] for p in parts) or "Model"
    return ("Model" + name) if name[0].isdigit() else name


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


# ---------------------------------------------------------------- fixtures
def example_from_schema(schema: Any, bundled: dict[str, Any], depth: int = 0, seen: tuple[str, ...] = ()) -> Any:
    if not isinstance(schema, dict) or depth > 48:
        return None
    ref = schema_ref_name(schema)
    if ref:
        if ref in seen:
            return None
        return example_from_schema(bundled["components"]["schemas"].get(ref), bundled, depth + 1, (*seen, ref))
    if "example" in schema:
        return schema["example"]
    if isinstance(schema.get("examples"), list) and schema["examples"]:
        return schema["examples"][0]
    if "allOf" in schema:
        merged: dict[str, Any] = {}
        for part in schema["allOf"]:
            val = example_from_schema(part, bundled, depth + 1, seen)
            if isinstance(val, dict):
                merged.update(val)
        return merged
    for key in ("oneOf", "anyOf"):
        if key in schema and schema[key]:
            return example_from_schema(schema[key][0], bundled, depth + 1, seen)
    if isinstance(schema.get("enum"), list) and schema["enum"]:
        return schema["enum"][0]
    t = schema.get("type")
    if isinstance(t, list):
        t = next((x for x in t if x != "null"), None)
    if t == "object" or "properties" in schema:
        return {
            k: example_from_schema(v, bundled, depth + 1, seen) for k, v in (schema.get("properties") or {}).items()
        }
    if t == "array":
        item = example_from_schema(schema.get("items"), bundled, depth + 1, seen)
        return [] if item is None else [item]
    if t in ("integer", "number"):
        value: float = 1
        lo, hi = schema.get("minimum"), schema.get("maximum")
        if isinstance(lo, (int, float)) and value < lo:
            value = lo
        if isinstance(hi, (int, float)) and value > hi:
            value = hi
        return int(value) if t == "integer" else float(value)
    if t == "boolean":
        return False
    if t == "string":
        fmt = schema.get("format")
        text = {
            "date-time": "2026-01-01T00:00:00Z",
            "date": "2026-01-01",
            "uri": "https://example.invalid/",
            "email": "user@example.invalid",
        }.get(fmt, "string")
        max_len, min_len = schema.get("maxLength"), schema.get("minLength")
        if isinstance(max_len, int) and len(text) > max_len:
            text = "x" * max_len
        if isinstance(min_len, int) and len(text) < min_len:
            text = text + "x" * (min_len - len(text))
        return text
    return None


# -------------------------------------------------------------------- main
def main(repo_arg: str) -> int:
    repo = Path(repo_arg).resolve()
    apis_dir = repo / "jsonschema" / "apis"
    prov = git_provenance(repo)
    commit = prov["commit"]

    for d in (SRC / "apis", SRC / "models"):
        for f in d.glob("*.py"):
            if f.name != "__init__.py":
                f.unlink()

    protheus_specs: list[Path] = []
    for spec_path in sorted(apis_dir.glob("*.json")):
        raw = load_json(spec_path)
        products = [p.get("product") for p in (raw.get("info", {}).get("x-totvs", {}).get("productInformation") or [])]
        if PRODUCT in products:
            protheus_specs.append(spec_path)
    api_ids = assign_api_ids([p.name for p in protheus_specs])

    apis: list[dict[str, Any]] = []
    bundles: dict[str, dict[str, Any]] = {}
    fixtures: dict[str, Any] = {}
    skipped_unavailable = 0
    for spec_path in protheus_specs:
        bundler = Bundler(repo, spec_path)
        bundled = bundler.bundle()
        api = index_api(spec_path.name, api_ids[spec_path.name], bundled)
        if api is None:
            skipped_unavailable += 1
            continue
        api["spec_quirks"] = sorted(set(api["spec_quirks"]) | set(bundler.quirks))
        apis.append(api)
        bundles[api["id"]] = bundled
        emit_models(api, bundled, SRC / "models" / f"{api['id']}.py", commit)
        for op in api["operations"]:
            for status, resp in op["responses"].items():
                if status.startswith("2") and resp["schema"]:
                    fixtures[op["id"]] = {
                        "status": int(status),
                        "body": example_from_schema({"$ref": f"#/components/schemas/{resp['schema']}"}, bundled),
                    }
                    break

    apis.sort(key=lambda a: a["id"])
    # accessors first: importing protheus.models pulls in protheus.apis via the package __init__
    (SRC / "apis" / "__init__.py").write_text(emit_apis_init(apis, commit), encoding="utf-8")
    unverified = verify_model_names(apis, bundles)
    example_defects = validate_examples(apis, fixtures)
    for api in apis:
        (SRC / "apis" / f"{api['id']}.py").write_text(emit_api_module(api, commit), encoding="utf-8")
    (SRC / "models" / "__init__.py").write_text(
        '"""Generated pydantic models, one module per API (see protheus.spec for the index)."""\n', encoding="utf-8"
    )
    index = {
        "provenance": {**prov, "product": PRODUCT, "generator": "tools/build.py"},
        "summary": {
            "apis": len(apis),
            "operations": sum(len(a["operations"]) for a in apis),
            "apis_without_protheus_operations": skipped_unavailable,
            "response_examples_violating_own_schema": example_defects,
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
        f"apis={len(apis)} operations={index['summary']['operations']} fixtures={len(fixtures)} "
        f"models_unverified={unverified} example_defects={example_defects} commit={commit[:7]}"
    )
    return 0


def validate_examples(apis: list[dict[str, Any]], fixtures: dict[str, Any]) -> int:
    """Validate each spec-derived response example against its generated model.

    A failure here is an upstream defect (the example contradicts the schema it
    illustrates) and is recorded on the operation as ``example_validation`` so
    consumers know which response contracts are unreliable.
    """
    import importlib

    from pydantic import ValidationError

    defects = 0
    for api in apis:
        module = importlib.import_module(f"protheus.models.{api['id']}")
        for op in api["operations"]:
            fixture = fixtures.get(op["id"])
            if not op["response_model"] or fixture is None:
                op["example_validation"] = None
                continue
            try:
                getattr(module, op["response_model"]).model_validate(fixture["body"])
                op["example_validation"] = {"ok": True, "error": None}
            except ValidationError as exc:
                first = exc.errors()[0]
                loc = ".".join(str(x) for x in first["loc"])
                op["example_validation"] = {"ok": False, "error": f"{first['type']} at {loc}: {first['msg']}"}
                defects += 1
            except TypeError as exc:
                # e.g. maxLength declared on a numeric property: the constraint itself is invalid
                op["example_validation"] = {"ok": False, "error": f"invalid_constraint: {exc}"}
                defects += 1
    return defects


def schema_property_names(bundled: dict[str, Any], schema: Any, depth: int = 0) -> set[str] | None:
    """Wire-level property names of an object schema (following $ref/allOf); None if not an object."""
    if not isinstance(schema, dict) or depth > 8:
        return None
    ref = schema_ref_name(schema)
    if ref:
        return schema_property_names(bundled, bundled["components"]["schemas"].get(ref), depth + 1)
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
