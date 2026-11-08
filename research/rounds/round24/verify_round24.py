#!/usr/bin/env python3
"""Read-only verification of the Round 24 publication and preservation claims.

Run from any directory in a checkout containing the pinned baseline commit.
No network calls, experiments, scientific models, or financial simulations occur.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
ROUND = ROOT / 'research/rounds/round24'
BASE = '1cf49c3bcd61b23b55b6ce7df02e73e5d4be233d'
SELF_MANIFEST = 'research/rounds/round24/artifact-manifest.json'
ALLOWED_OLD = {'README.md', 'decisions/current-shortlist.md',
               'research/portfolio-register.json', 'research/rounds/README.md',
               'research/screen-index.md'}
checks = []

def check(name, passed, detail=None):
    item = {'check': name, 'passed': bool(passed)}
    if detail is not None:
        item['detail'] = detail
    checks.append(item)

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def blob_hash(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def load(path):
    return json.loads(path.read_text())

try:
    baseline = json.loads(git('show', BASE + ':research/portfolio-register.json'))
    register = load(ROOT / 'research/portfolio-register.json')
    ledger = load(ROUND / 'candidate-ledger.json')
    existing = load(ROUND / 'existing-candidate-matrix.json')
    sources = load(ROUND / 'source-register.json')
    manifest = load(ROUND / 'artifact-manifest.json')
    decision = register['current_marginal_dollar_decision']
    baseline_paths = set(git('ls-tree', '-r', '--name-only', BASE).decode().splitlines())
    tracked_paths = set(git('ls-files').decode().splitlines())
    local_round_paths = {str(p.relative_to(ROOT)) for p in ROUND.rglob('*') if p.is_file()}
    current_paths = tracked_paths | local_round_paths
    current_paths = {p for p in current_paths if (ROOT / p).is_file()}
    modified_old = []
    removed = []
    for path in sorted(baseline_paths):
        if not (ROOT / path).is_file():
            removed.append(path)
        elif (ROOT / path).read_bytes() != git('show', BASE + ':' + path):
            modified_old.append(path)
    check('all_baseline_paths_preserved', not removed, removed)
    check('only_intended_existing_files_changed', set(modified_old) == ALLOWED_OLD, modified_old)
    check('new_files_scoped_to_round24', all(p.startswith('research/rounds/round24/') for p in current_paths - baseline_paths))
    check('no_symlinks', not any((ROOT / p).is_symlink() for p in current_paths))
    check('original_622_coverage_rows_unchanged', len(register['coverage_records']) == 622 and register['coverage_records'] == baseline['coverage_records'])
    old_round_keys = [k for k in baseline if re.fullmatch(r'round\d+', k)]
    check('all_prior_round_objects_unchanged', all(register.get(k) == baseline[k] for k in old_round_keys))
    check('prior_round_history_unchanged', register['round_history'] == baseline['round_history'])
    allowed_fields = {'schema_version', 'as_of', 'supersedes', 'coverage_summary', 'current_marginal_dollar_decision', 'publication', 'round24'}
    changed_fields = {k for k in baseline.keys() | register.keys() if baseline.get(k) != register.get(k)}
    check('register_changes_are_declared', not (changed_fields - allowed_fields), sorted(changed_fields))
    check('coverage_summary_history_preserved', all(register['coverage_summary'].get(k) == v for k, v in baseline['coverage_summary'].items()))
    check('inherited_conditional_queue_preserved', decision['inherited_conditional_development_prefix'] == baseline['current_marginal_dollar_decision']['inherited_conditional_development_prefix'])
    check('no_paid_development_or_numerical_ev_promotion', decision['spending_authorized'] is False and decision['paid_development_promotions'] == 0 and decision['estimated_return_per_dollar'] is None)
    check('cash_and_incomplete_novelty_retained', decision['zero_or_wait_option_included'] is True and decision['novelty_exhaustive'] is False)
    check('candidate_ledger_matches_register', ledger['records'] == register['round24']['new_screen_records'])
    ids = [r['id'] for r in ledger['records']]
    check('new_candidate_ids_unique_and_counted', len(ids) == len(set(ids)) == ledger['counts']['screened_records'])
    check('all_new_records_unfunded', all(r['funding_authorized'] is False and r['paid_development_promotion'] is False and r['estimated_return_per_dollar'] is None for r in ledger['records']))
    check('new_screen_information_order_matches_register', ledger['additional_screen_information_order'] == decision['additional_screen_information_queue'])
    check('existing_candidate_records_preserved_as_existing', len(existing['records']) == len({r['candidate_id'] for r in existing['records']}) and len(existing['records']) == 12)
    source_ids = [s['id'] for s in sources['sources']]
    source_set = set(source_ids)
    check('source_ids_unique', len(source_ids) == len(source_set))
    check('source_count_and_access_scopes_complete', sources['source_count'] == len(source_ids) and all(s.get('access_scope') for s in sources['sources']))
    unresolved = {}
    for path in sorted(local_round_paths):
        if Path(path).suffix not in {'.md', '.json'} or path == SELF_MANIFEST:
            continue
        text = (ROOT / path).read_text()
        missing = sorted(set(re.findall(r'\b([CENT]\d{2})\b', text)) - source_set)
        if missing:
            unresolved[path] = missing
    check('source_references_resolve', not unresolved, unresolved)
    broken = []
    for path in sorted(ALLOWED_OLD | local_round_paths):
        if not path.endswith('.md'):
            continue
        text = (ROOT / path).read_text()
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^\n)]+)\)', text):
            target = target.strip().split(' "', 1)[0]
            if re.match(r'^[a-z]+:', target, re.I) or target.startswith('#'):
                continue
            file_part = target.split('#', 1)[0]
            if file_part and not ((ROOT / path).parent / file_part).resolve().exists():
                broken.append({'file': path, 'target': target})
    check('local_markdown_links_resolve', not broken, broken)
    manifest_paths = {f['path'] for f in manifest['files']}
    check('manifest_has_complete_exact_path_set', manifest_paths == current_paths and len(manifest['files']) == len(current_paths), {'missing': sorted(current_paths - manifest_paths), 'extra': sorted(manifest_paths - current_paths)})
    mismatches = []
    for item in manifest['files']:
        path = item['path']
        if path == SELF_MANIFEST:
            continue
        data = (ROOT / path).read_bytes()
        actual = {'bytes': len(data), 'git_blob_sha': blob_hash(data), 'sha256': hashlib.sha256(data).hexdigest(), 'mode': '100755' if (ROOT / path).stat().st_mode & 0o111 else '100644'}
        for field, value in actual.items():
            if item[field] != value:
                mismatches.append({'path': path, 'field': field})
    check('manifest_content_hashes_and_modes_match', not mismatches, mismatches)
    check('manifest_base_and_counts_match', manifest['base_commit'] == BASE and manifest['file_count'] == len(current_paths) and set(manifest['modified_files']) == ALLOWED_OLD and not manifest['deleted_files'])
except Exception as exc:
    check('verifier_completed', False, str(exc))

result = {'schema_version': 'ddiscov.round24.verifier_output.v1', 'base_commit': BASE, 'checks': checks, 'passed': bool(checks) and all(c['passed'] for c in checks)}
print(json.dumps(result, indent=2))
sys.exit(0 if result['passed'] else 1)
