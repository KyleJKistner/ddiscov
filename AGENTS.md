# Agent guide

## Goal and starting context

Optimize the next dollar committed to drug development, across all development stages. Prefer credible success, affordable milestones and bounded downside. Read [current opportunities](decisions/current-shortlist.md) and [selection policy](decisions/selection-policy.md), then retrieve only the evidence needed for the task.

The active source of priority is `decisions/current-shortlist.md`; the active evaluation standard is `decisions/selection-policy.md`. Research records retain the conclusions and terminology of their review dates. The latest completed evidence review is Round 26, dated 8 November 2026.

## Retrieve focused context

```sh
python3 scripts/repo.py status
python3 scripts/repo.py search 'candidate name' --limit 8
```

`search` finds JSON string values. Pass its file and pointer to `show FILE /pointer` for that value; shorten `/records/3/name` to `/records/3` for the enclosing record. Large selections return their available keys so you can choose a smaller section. Use `rg -n 'term' research/rounds/round26` for prose and CSV searches. Browse [research](research/README.md) for source locations and [methods](methods/README.md) for executable analyses.

`research/portfolio-register.json` is a large cumulative snapshot through Round 26. Its older top-level shortlist, policy, allocation and reading instructions are historical. Query the relevant object for evidence or lineage; use `decisions/` to guide new work. Load older rounds, full catalogs and manifests when the task requires that detail.

## Make a useful change

- State the exact intervention/use and the decision the work can change.
- Preserve source identifiers, review dates, biological units, contrary evidence and material uncertainty.
- Distinguish observed evidence, calculations, estimates, proposed work and completed work.
- Verify time-sensitive claims when they affect a new decision. A document cleanup retains the evidence cutoff of its sources.
- Put detailed evidence in a focused research record. Summarize its decision impact in the current opportunities page and link it there.
- Update existing current summaries in place. Keep historical chronology in research records and Git history.
- Keep entry pages short and task-oriented; use links for candidate-specific methods, source disputes and historical accounting.

Use existing candidate identifiers where available. A new research round gets a dated README describing its question and findings, the necessary evidence files, and one row in the round index. Add structured data when it supports comparison or reproducibility.

## Validate and hand off

```sh
python3 scripts/repo.py check
python3 -m unittest discover -s tests
git diff --check
```

Run the relevant [method](methods/README.md) when changing an analysis. The `verify_round*.py` scripts and artifact manifests inside older rounds validate their original publication snapshots; run them at those commits when reproducing historical publication checks. Their original file hashes remain historical evidence.

Report what changed, the checks run and any unresolved limitation that affects use of the result. Keep operational details in the handoff or commit rather than adding them to every entry page.
