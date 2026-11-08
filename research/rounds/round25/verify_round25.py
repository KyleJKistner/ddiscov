#!/usr/bin/env python3
"""Read-only Round 25 publication checks, not biological or investment validation."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
ROUND = ROOT / "research/rounds/round25"
BASE = "994454ca215920e1dd3fd151df6d8081e0ee345c"
SELF = "research/rounds/round25/artifact-manifest.json"
ALLOWED_OLD = {
    "README.md", "decisions/current-shortlist.md", "research/portfolio-register.json",
    "research/rounds/README.md", "research/screen-index.md",
}
checks = []

def check(name, passed, detail=None):
    record = {"check": name, "passed": bool(passed)}
    if detail is not None:
        record["detail"] = detail
    checks.append(record)

def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])

def read(path):
    return json.loads(path.read_text())

def blob_hash(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def record_id(record):
    return record.get("id", record.get("candidate_id"))

try:
    old = json.loads(git("show", BASE + ":research/portfolio-register.json"))
    current = read(ROOT / "research/portfolio-register.json")
    summary = read(ROUND / "round25-summary.json")
    ledger = read(ROUND / "candidate-ledger.json")
    existing = read(ROUND / "existing-candidate-matrix.json")
    sources = read(ROUND / "source-register.json")
    manifest = read(ROUND / "artifact-manifest.json")
    baseline_paths = set(git("ls-tree", "-r", "--name-only", BASE).decode().splitlines())
    round_paths = {str(p.relative_to(ROOT)) for p in ROUND.rglob("*") if p.is_file()}
    paths = set(git("ls-files").decode().splitlines()) | round_paths
    paths = {p for p in paths if (ROOT / p).is_file()}
    removed = sorted(p for p in baseline_paths if not (ROOT / p).is_file())
    modified = sorted(p for p in baseline_paths if p not in removed
                      and (ROOT / p).read_bytes() != git("show", BASE + ":" + p))
    check("all_400_baseline_files_preserved", len(baseline_paths) == 400 and not removed, removed)
    check("only_declared_existing_files_changed", set(modified) == ALLOWED_OLD, modified)
    check("all_new_files_scoped_to_round25",
          all(p.startswith("research/rounds/round25/") for p in paths - baseline_paths))
    check("no_symlinks", not any((ROOT / p).is_symlink() for p in paths))
    check("original_622_coverage_records_unchanged",
          len(current["coverage_records"]) == 622 and current["coverage_records"] == old["coverage_records"])
    old_rounds = [k for k in old if re.fullmatch(r"round\d+", k)]
    check("all_prior_round_objects_unchanged", all(current.get(k) == old[k] for k in old_rounds))
    check("prior_round_history_unchanged", current["round_history"] == old["round_history"])
    allowed_fields = {"schema_version", "as_of", "supersedes", "coverage_summary",
                      "current_marginal_dollar_decision", "publication", "round25"}
    changed_fields = {k for k in old.keys() | current.keys() if old.get(k) != current.get(k)}
    check("register_changes_declared", not changed_fields - allowed_fields, sorted(changed_fields))
    check("historical_coverage_summary_preserved",
          all(current["coverage_summary"].get(k) == v for k, v in old["coverage_summary"].items()))
    decision = current["current_marginal_dollar_decision"]
    check("current_selection_agrees_across_summary_and_register",
          decision == summary["selection"] == current["round25"]["selection"])
    check("no_spending_or_numeric_EV_asserted",
          decision["spending_authorized"] is False
          and decision["paid_development_promotions"] == 0
          and decision["estimated_return_per_dollar"] is None
          and decision["zero_or_wait_option_included"] is True)
    check("novelty_gap_retained", decision["novelty_exhaustive"] is False
          and bool(decision["missing_novelty_scope"]))
    check("candidate_ledger_preserved_in_register",
          ledger["records"] == current["round25"]["new_screen_records"])
    candidate_ids = [record_id(r) for r in ledger["records"]]
    check("candidate_ids_unique_and_counted",
          all(candidate_ids) and len(candidate_ids) == len(set(candidate_ids))
          == summary["counts"]["new_candidate_records"])
    existing_ids = [record_id(r) for r in existing["records"]]
    check("existing_candidates_unique_and_counted",
          all(existing_ids) and len(existing_ids) == len(set(existing_ids))
          == summary["counts"]["existing_programs_reassessed"])
    check("summary_matches_register_counts", summary["counts"] == current["round25"]["counts"])
    source_ids = [s["id"] for s in sources["sources"]]
    check("source_reference_ids_unique", len(source_ids) == len(set(source_ids)))
    check("source_counts_and_access_scopes_complete",
          len(source_ids) == sources["source_count"] == summary["counts"]["source_records"]
          and all(s.get("access_scope") and (s.get("url") or s.get("urls")
                  or s.get("query") or s.get("repository_paths")) for s in sources["sources"]))
    referenced_ids = set()
    for path in sorted(round_paths):
        if path.endswith((".json", ".md")):
            referenced_ids.update(re.findall(r"R25-[AEIN]\d{2}", (ROOT / path).read_text()))
    unresolved_ids = sorted(referenced_ids - set(source_ids))
    check("all_round25_source_references_resolve", not unresolved_ids, unresolved_ids)
    check("new_and_existing_candidate_sets_do_not_overlap", not set(candidate_ids) & set(existing_ids))
    audit = read(ROUND / "external-screen-duplicate-audit.json")
    check("external_selected_alias_audit_covers_13_complete_reports",
          len(audit["reports"]) == 13
          and all(r["full_indexed_text_searched"] for r in audit["reports"])
          and audit["scope"]["novelty_exhaustive"] is False)
    json_errors = []
    for path in sorted(round_paths):
        if path.endswith(".json"):
            try:
                read(ROOT / path)
            except Exception as exc:
                json_errors.append({"path": path, "error": str(exc)})
    check("all_round25_json_parses", not json_errors, json_errors)
    broken = []
    for path in sorted(ALLOWED_OLD | round_paths):
        if not path.endswith(".md"):
            continue
        content = (ROOT / path).read_text()
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^\n)]+)\)", content):
            target = target.strip().split(' "', 1)[0]
            if re.match(r"^[a-z]+:", target, re.I) or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if local and not ((ROOT / path).parent / local).resolve().exists():
                broken.append({"file": path, "target": target})
    check("local_markdown_links_resolve", not broken, broken)
    manifest_paths = {entry["path"] for entry in manifest["files"]}
    check("manifest_has_complete_exact_path_set",
          manifest_paths == paths and len(manifest["files"]) == len(paths),
          {"missing": sorted(paths - manifest_paths), "extra": sorted(manifest_paths - paths)})
    mismatches = []
    for entry in manifest["files"]:
        path = entry["path"]
        if path == SELF:
            continue
        data = (ROOT / path).read_bytes()
        values = {"bytes": len(data), "git_blob_sha": blob_hash(data),
                  "sha256": hashlib.sha256(data).hexdigest(),
                  "mode": "100755" if (ROOT / path).stat().st_mode & 0o111 else "100644"}
        for key, value in values.items():
            if entry[key] != value:
                mismatches.append({"path": path, "field": key})
    check("manifest_content_hashes_and_modes_match", not mismatches, mismatches)
    check("manifest_base_and_counts_match",
          manifest["base_commit"] == BASE and manifest["file_count"] == len(paths)
          and manifest["baseline_file_count"] == 400
          and set(manifest["modified_files"]) == ALLOWED_OLD
          and not manifest["deleted_files"])
except Exception as exc:
    check("verifier_completed", False, str(exc))

result = {"schema_version": "ddiscov.round25.verification_output.v1",
          "base_commit": BASE, "checks": checks,
          "passed": bool(checks) and all(c["passed"] for c in checks),
          "scope": "Artifact consistency, historical preservation and publication hashes only."}
print(json.dumps(result, indent=2))
sys.exit(0 if result["passed"] else 1)
