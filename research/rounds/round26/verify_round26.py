#!/usr/bin/env python3
"""Read-only artifact checks; these do not validate therapeutic or investment claims."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
ROUND = ROOT / "research/rounds/round26"
BASE = "2ac9dafe2c45aa7d1baf1499a440fde013cece28"
SELF = "research/rounds/round26/artifact-manifest.json"
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
    summary = read(ROUND / "round26-summary.json")
    ledger = read(ROUND / "candidate-ledger.json")
    sources = read(ROUND / "source-register.json")
    audit = read(ROUND / "novelty-audit.json")
    manifest = read(ROUND / "artifact-manifest.json")
    baseline_paths = set(git("ls-tree", "-r", "--name-only", BASE).decode().splitlines())
    round_paths = {str(p.relative_to(ROOT)) for p in ROUND.rglob("*") if p.is_file()}
    paths = set(git("ls-files").decode().splitlines()) | round_paths
    paths = {p for p in paths if (ROOT / p).is_file()}
    removed = sorted(p for p in baseline_paths if not (ROOT / p).is_file())
    modified = sorted(p for p in baseline_paths if p not in removed
                      and (ROOT / p).read_bytes() != git("show", BASE + ":" + p))
    check("all_424_baseline_files_preserved", len(baseline_paths) == 424 and not removed, removed)
    check("only_declared_existing_files_changed", set(modified) == ALLOWED_OLD, modified)
    check("all_new_files_scoped_to_round26",
          all(p.startswith("research/rounds/round26/") for p in paths - baseline_paths))
    check("no_symlinks", not any((ROOT / p).is_symlink() for p in paths))
    check("original_622_coverage_records_unchanged",
          len(current["coverage_records"]) == 622 and current["coverage_records"] == old["coverage_records"])
    old_rounds = [k for k in old if re.fullmatch(r"round\d+", k)]
    check("all_prior_round_objects_unchanged", all(current.get(k) == old[k] for k in old_rounds))
    check("prior_round_history_unchanged", current["round_history"] == old["round_history"])
    allowed_fields = {"schema_version", "as_of", "supersedes", "coverage_summary",
                      "current_marginal_dollar_decision", "publication", "round26"}
    changed_fields = {k for k in old.keys() | current.keys() if old.get(k) != current.get(k)}
    check("register_changes_declared", not changed_fields - allowed_fields, sorted(changed_fields))
    check("historical_coverage_summary_preserved",
          all(current["coverage_summary"].get(k) == v for k, v in old["coverage_summary"].items()))
    decision = current["current_marginal_dollar_decision"]
    check("current_selection_agrees_across_summary_and_register",
          decision == summary["selection"] == current["round26"]["selection"])
    check("no_spending_or_numeric_EV_asserted",
          decision["spending_authorized"] is False
          and decision["paid_development_promotions"] == 0
          and decision["estimated_return_per_dollar"] is None
          and decision["zero_or_wait_option_included"] is True)
    check("three_agents_all_focused_on_new_screening",
          len(summary["orchestration"]) == 3
          and all(x["scope_type"] == "new_candidate_screening" for x in summary["orchestration"])
          and summary["counts"]["existing_programs_reassessed"] == 0
          and summary["counts"]["lead_advancement_packages"] == 0)
    check("novelty_gap_retained", decision["novelty_exhaustive"] is False
          and bool(decision["missing_novelty_scope"]) and audit["exhaustive"] is False)
    check("candidate_ledger_preserved_in_register",
          ledger["records"] == current["round26"]["new_screen_records"])
    candidate_ids = [record_id(r) for r in ledger["records"]]
    check("candidate_ids_unique_and_counted",
          all(candidate_ids) and len(candidate_ids) == len(set(candidate_ids))
          == summary["counts"]["new_candidate_records"])
    lane_records = []
    for lane in ["human", "local", "functional"]:
        lane_records.extend(read(ROUND / (lane + "-candidate-ledger.json"))["records"])
    check("all_three_lane_ledgers_integrated_exactly", lane_records == ledger["records"])
    check("summary_matches_register_counts", summary["counts"] == current["round26"]["counts"])
    source_ids = [s["id"] for s in sources["sources"]]
    check("source_reference_ids_unique", len(source_ids) == len(set(source_ids)))
    check("source_counts_and_access_scopes_complete",
          len(source_ids) == sources["source_count"] == summary["counts"]["source_records"]
          and all(s.get("access_scope") and (s.get("url") or s.get("urls")
                  or s.get("query") or s.get("repository_paths")) for s in sources["sources"]))
    referenced_ids = set()
    for path in sorted(round_paths):
        if path.endswith((".json", ".md")):
            referenced_ids.update(re.findall(r"R26-[HFLI]\d{2}", (ROOT / path).read_text()))
    unresolved_ids = sorted(referenced_ids - set(source_ids))
    check("all_round26_source_references_resolve", not unresolved_ids, unresolved_ids)
    access = read(ROUND / "unpaywall-access-audit.json")
    access_dois = {r["doi"].lower() for r in access["records"]}
    check("unpaywall_all_lane_lookups_counted_with_access_scope",
          len(access["records"]) == access["lookup_records_in_this_consolidation"]
          == summary["counts"]["unpaywall_lookup_records_consolidated"] == 18
          and len(access_dois) == access["unique_normalized_dois"]
          == summary["counts"]["unpaywall_unique_dois"] == 16
          and {r["workstream"] for r in access["records"]} == {"human", "local", "functional", "integration"}
          and all(isinstance(r["is_oa"], bool) and isinstance(r["oa_locations"], list)
                  and "best_oa_location" in r and r.get("actual_content_access") for r in access["records"]))
    check("novelty_audit_covers_frozen_baseline_and_complete_reports",
          audit["baseline"]["file_count"] == 424
          and audit["baseline"]["read_errors"] == []
          and len(audit["external_reports"]) == 13
          and all(r["full_indexed_text_searched"] for r in audit["external_reports"]))
    audit_ids = {r["candidate_id"] for r in audit["candidate_checks"]}
    check("every_retained_candidate_has_root_novelty_check", set(candidate_ids) <= audit_ids)
    json_errors = []
    for path in sorted(round_paths):
        if path.endswith(".json"):
            try:
                read(ROOT / path)
            except Exception as exc:
                json_errors.append({"path": path, "error": str(exc)})
    check("all_round26_json_parses", not json_errors, json_errors)
    broken = []
    private_locations = []
    for path in sorted(ALLOWED_OLD | round_paths):
        if not path.endswith((".md", ".json")):
            continue
        content = (ROOT / path).read_text()
        if path.startswith("research/rounds/round26/") and re.search(
            r"api\.unpaywall\.org[^\s\"]*[?&]email=|oai-library://|libfile_[a-f0-9]{20,}", content):
            private_locations.append(path)
        if not path.endswith(".md"):
            continue
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^\n)]+)\)", content):
            target = target.strip().split(' "', 1)[0]
            if re.match(r"^[a-z]+:", target, re.I) or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if local and not ((ROOT / path).parent / local).resolve().exists():
                broken.append({"file": path, "target": target})
    check("local_markdown_links_resolve", not broken, broken)
    check("no_private_access_parameters_or_library_identifiers", not private_locations, private_locations)
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
          and manifest["baseline_file_count"] == 424
          and set(manifest["modified_files"]) == ALLOWED_OLD
          and not manifest["deleted_files"])
except Exception as exc:
    check("verifier_completed", False, str(exc))

result = {"schema_version": "ddiscov.round26.verification_output.v1",
          "base_commit": BASE, "checks": checks,
          "passed": bool(checks) and all(c["passed"] for c in checks),
          "scope": "Artifact consistency, historical preservation and publication hashes only."}
print(json.dumps(result, indent=2))
sys.exit(0 if result["passed"] else 1)
