#!/usr/bin/env python3
"""Small, read-only navigation and consistency checks for the research repository."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REGISTER = "research/portfolio-register.json"
REQUIRED = (
    "README.md", "AGENTS.md", "decisions/current-shortlist.md",
    "decisions/selection-policy.md", REGISTER,
)
ACTIVE_DOCS = (
    "README.md", "AGENTS.md", "decisions/README.md",
    "decisions/current-shortlist.md", "decisions/selection-policy.md",
    "research/README.md", "research/screen-index.md", "research/rounds/README.md",
    "methods/README.md", "atlas/README.md", "discovery/README.md",
    "formulations/README.md", "provenance/README.md",
)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def short(text, limit=220):
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[:limit - 1] + "…"


def resolve_file(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Choose a file inside this repository.")
    if not path.is_file():
        raise ValueError(f"File does not exist: {name}")
    return path


def pointer_escape(value):
    return str(value).replace("~", "~0").replace("/", "~1")


def select_pointer(value, pointer):
    """Resolve an RFC 6901 JSON pointer, including escaped object keys."""
    if pointer == "":
        return value
    if not pointer.startswith("/"):
        raise ValueError("A JSON pointer starts with '/', or is empty for the whole file.")
    for token in pointer[1:].split("/"):
        if re.search(r"~(?![01])", token):
            raise ValueError(f"Invalid JSON pointer escape: {token}")
        key = token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict):
            if key not in value:
                raise ValueError(f"JSON pointer key not found: {key}")
            value = value[key]
        elif isinstance(value, list):
            if not re.fullmatch(r"0|[1-9][0-9]*", key) or int(key) >= len(value):
                raise ValueError(f"JSON pointer array index not found: {key}")
            value = value[int(key)]
        else:
            raise ValueError(f"JSON pointer continues beyond a scalar at: {key}")
    return value


def scalar_values(value, pointer=""):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from scalar_values(child, pointer + "/" + pointer_escape(key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from scalar_values(child, pointer + "/" + str(index))
    else:
        yield pointer, value


def search_order(path):
    name = path.as_posix()
    # Publication inventories repeat old filenames; search evidence before those inventories.
    if "manifest" in path.name or "verification" in path.name:
        return (3, 0, name)
    if name == REGISTER:
        return (2, 0, name)
    match = re.match(r"research/rounds/round(\d+)/", name)
    if match:
        priority = 0 if path.name == "candidate-ledger.json" else 1
        return (0, -int(match.group(1)), str(priority) + name)
    return (1, 0, name)


def search(root, term, limit=10):
    if not term.strip():
        raise ValueError("Use a nonempty search term.")
    if not 1 <= limit <= 100:
        raise ValueError("Search limit must be between 1 and 100.")
    paths = sorted((p.relative_to(root) for p in root.rglob("*.json")
                    if ".git" not in p.parts), key=search_order)
    matches = []
    errors = []
    needle = term.casefold()
    for relative in paths:
        try:
            value = read_json(root / relative)
        except (ValueError, OSError) as exc:
            errors.append({"file": relative.as_posix(), "error": str(exc)})
            continue
        for pointer, scalar in scalar_values(value):
            if isinstance(scalar, str) and needle in scalar.casefold():
                if len(matches) == limit:
                    return {"query": term, "matches": matches, "more_matches": True,
                            "errors": errors}
                matches.append({"file": relative.as_posix(), "pointer": pointer,
                                "excerpt": short(scalar)})
    return {"query": term, "matches": matches, "more_matches": False, "errors": errors}


def show(root, filename, pointer, max_chars=6000, full=False):
    value = select_pointer(read_json(resolve_file(root, filename)), pointer)
    rendered = json.dumps(value, ensure_ascii=False, indent=2)
    if len(rendered) > max_chars and not full:
        detail = {"file": filename, "pointer": pointer, "characters": len(rendered),
                  "message": "Choose a narrower pointer or use --full for this selection."}
        if isinstance(value, dict):
            detail["keys"] = list(value)[:50]
            detail["key_count"] = len(value)
        elif isinstance(value, list):
            detail["items"] = len(value)
        raise ValueError(json.dumps(detail, ensure_ascii=False))
    return value


def status(root):
    shortlist = (root / "decisions/current-shortlist.md").read_text(encoding="utf-8")
    rounds = sorted((int(p.name[5:]) for p in (root / "research/rounds").glob("round*")
                     if p.is_dir() and re.fullmatch(r"round\d+", p.name)), reverse=True)
    brief = [short(line.replace("**", "")) for line in shortlist.splitlines()
             if line.startswith("**Evidence cutoff:") or line.startswith("**Current capital")]
    return {
        "current_decisions": "decisions/current-shortlist.md",
        "selection_policy": "decisions/selection-policy.md",
        "agent_guide": "AGENTS.md",
        "current_notes": brief,
        "latest_evidence_round": rounds[0] if rounds else None,
        "latest_evidence_path": f"research/rounds/round{rounds[0]}/README.md" if rounds else None,
        "historical_register": REGISTER,
        "reading_order": "Read the current decisions and policy, then open evidence for the selected task.",
    }


def local_links(text):
    text = re.sub(r"```.*?```|~~~.*?~~~", "", text, flags=re.S)
    for target in re.findall(r"\[[^\]]*\]\(([^\n)]+)\)", text):
        target = target.strip()
        if target.startswith("<"):
            target = target[1:].split(">", 1)[0]
        else:
            target = re.split(r'\s+[\"\']', target, maxsplit=1)[0]
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith(("#", "//")):
            continue
        filename = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if filename:
            yield filename


def check(root):
    errors = []
    counts = {"json_files": 0, "csv_files": 0, "active_documents": 0, "local_links": 0}
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append({"file": name, "error": "Required entry point is missing."})
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        name = path.relative_to(root).as_posix()
        try:
            if path.suffix == ".json":
                counts["json_files"] += 1
                read_json(path)
            elif path.suffix == ".csv":
                counts["csv_files"] += 1
                with path.open(encoding="utf-8", newline="") as handle:
                    rows = csv.reader(handle, strict=True)
                    header = next(rows, None)
                    if not header:
                        raise ValueError("CSV header is missing.")
                    for number, row in enumerate(rows, 2):
                        if row and len(row) != len(header):
                            raise ValueError(f"CSV row {number} has {len(row)} fields; expected {len(header)}.")
        except (ValueError, OSError, csv.Error) as exc:
            errors.append({"file": name, "error": str(exc)})
    for name in ACTIVE_DOCS:
        path = root / name
        if not path.is_file():
            continue
        counts["active_documents"] += 1
        for target in local_links(path.read_text(encoding="utf-8")):
            counts["local_links"] += 1
            if not (path.parent / target).exists():
                errors.append({"file": name, "error": "Local link target is missing.", "target": target})
    return {"passed": not errors, "counts": counts, "errors": errors,
            "scope": "File formats and active-document links; evidence claims and archived publication hashes have separate reviews."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command")
    commands.add_parser("status", help="Show current entry points and latest evidence round.")
    query = commands.add_parser("search", help="Search JSON string values; latest evidence comes first.")
    query.add_argument("term")
    query.add_argument("--limit", type=int, default=10)
    selection = commands.add_parser("show", help="Read one JSON selection using an RFC 6901 pointer.")
    selection.add_argument("file")
    selection.add_argument("pointer", nargs="?", default="")
    selection.add_argument("--max-chars", type=int, default=6000)
    selection.add_argument("--full", action="store_true", help="Allow a large selection to be printed.")
    commands.add_parser("check", help="Check JSON, CSV, required entry points and active Markdown links.")
    args = parser.parse_args(argv)
    try:
        if args.command in (None, "status"):
            result = status(ROOT)
        elif args.command == "search":
            result = search(ROOT, args.term, args.limit)
        elif args.command == "show":
            if args.max_chars < 1:
                raise ValueError("--max-chars must be positive.")
            result = show(ROOT, args.file, args.pointer, args.max_chars, args.full)
        else:
            result = check(ROOT)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if args.command == "check" and not result["passed"] else 0
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
