#!/usr/bin/env python3
"""Small, read-only navigation and consistency checks for the research repository."""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
import re
import subprocess
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
    "decisions/opportunity-template.md",
    "research/README.md", "research/screen-index.md", "research/rounds/README.md",
    "methods/README.md", "atlas/README.md", "discovery/README.md",
    "formulations/README.md", "provenance/README.md",
)
LOCAL_DIRS = {".git", ".hg", ".svn", ".venv", "venv", "__pycache__", ".pytest_cache", "node_modules"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def project_files(root):
    """Use Git's tracked/unignored files, or skip local tooling in an exported tree."""
    root = root.resolve()
    names = None
    if (root / ".git").exists():
        try:
            result = subprocess.run(
                ["git", "-C", str(root), "ls-files", "--cached", "--others",
                 "--exclude-standard", "-z"],
                check=True, capture_output=True, text=True,
            )
            names = {Path(name) for name in result.stdout.split("\0") if name}
        except (OSError, subprocess.CalledProcessError):
            pass
    if names is None:
        names = set()
        for directory, subdirs, files in os.walk(root, followlinks=False):
            subdirs[:] = [name for name in subdirs if name not in LOCAL_DIRS
                         and not (Path(directory) / name).is_symlink()]
            names.update((Path(directory) / name).relative_to(root) for name in files)
    for name in sorted(names):
        path = root / name
        if path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root):
            yield name


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
    paths = sorted((p for p in project_files(root) if p.suffix == ".json"), key=search_order)
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
    # The current decision page identifies relevant evidence; draft folders do not.
    rounds = set()
    for target in local_links(shortlist):
        match = re.match(r"\.\./research/rounds/round(\d+)/", target)
        if match:
            number = int(match.group(1))
            try:
                resolve_file(root, f"research/rounds/round{number}/README.md")
                resolve_file(root, "decisions/" + target)
            except ValueError:
                continue
            rounds.add(number)
    latest = max(rounds, default=None)
    brief = [short(line.replace("**", "")) for line in shortlist.splitlines()
             if line.startswith("**Evidence cutoff:") or line.startswith("**Current capital")]
    return {
        "current_decisions": "decisions/current-shortlist.md",
        "selection_policy": "decisions/selection-policy.md",
        "agent_guide": "AGENTS.md",
        "current_notes": brief,
        "latest_evidence_round": latest,
        "latest_evidence_path": f"research/rounds/round{latest}/README.md" if latest is not None else None,
        "evidence_round_basis": "Latest round linked from the current decisions with an available README.",
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
    active_docs = set(ACTIVE_DOCS)
    counts = {"json_files": 0, "csv_files": 0, "active_documents": 0, "local_links": 0}
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append({"file": name, "error": "Required entry point is missing."})
    for relative in project_files(root):
        path = root / relative
        name = relative.as_posix()
        if name.startswith(("research/phase2-program/", "research/commercial-routes/")) and path.suffix == ".md":
            active_docs.add(name)
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
    for name in sorted(active_docs):
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
    commands.add_parser("status", help="Show current entry points and latest referenced evidence round.")
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
