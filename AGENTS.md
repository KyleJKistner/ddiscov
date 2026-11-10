# Agent guide

## Goal and starting context

Optimize financial value retained from the next dollar committed to drug development, across all stages and attainable transaction structures. Prefer credible success and protect the ability to continue after losses. Read [current opportunities](decisions/current-shortlist.md) and [selection policy](decisions/selection-policy.md), then retrieve only the evidence needed for the task.

The active source of priority is `decisions/current-shortlist.md`; the active evaluation standard is `decisions/selection-policy.md`. The [shortlist reconciliation](research/strategy/2026-11-08-shortlist-reconciliation.md) combines PR #4 and PR #6, including their prerequisite reviews. Round 28 is the latest numbered review. Priorities are tied APR/erlotinib leads, an unordered CBD3063 plus insulin/AAT/verteporfin challenger tier, and conditional reserves. Existing-article access and a useful commercial gap precede a new study proposal. Preserve broad sourcing, cash-recovery discipline, flexible capital and 100% initial founder equity with separate upstream obligations and later dilution. Historical model filters, ranks and pilot costs retain their original scopes. Personal financial limits stay in the private mandate. Screen and deepen using explicit estimates; inquiries and commitments are later decisions. Read the focused evidence needed for the task.

## Retrieve focused context

```sh
python3 scripts/repo.py status
python3 scripts/repo.py search 'candidate name' --limit 8
```

`search` finds JSON string values. Pass its file and pointer to `show FILE /pointer` for that value; shorten `/records/3/name` to `/records/3` for the enclosing record. Large selections return their available keys so you can choose a smaller section. Use `rg -n 'term' research/rounds/round26` for prose and CSV searches. Browse [research](research/README.md) for source locations and [methods](methods/README.md) for executable analyses.

`research/portfolio-register.json` is a large cumulative snapshot through Round 26. Its older top-level shortlist, policy, allocation and reading instructions are historical. Query the relevant object for evidence or lineage; use `decisions/` to guide new work. Load older rounds, full catalogs and manifests when the task requires that detail.

## Make a useful change

- State the exact intervention/use and the decision the work can change.
- Compare an asset/use **plus obtainable economic interest plus bounded next commitment**. Use the [opportunity template](decisions/opportunity-template.md) when preparing a serious proposal; label missing prices, terms and capital limits explicitly.
- Source established and novel assets, existing-drug indications, product/process improvements and participation in existing programs across disease areas. Match evidence and endpoints to the actual benefit and next stage.
- Preserve source identifiers, review dates, biological units, contrary evidence and material uncertainty.
- Distinguish observed evidence, calculations, estimates, proposed work and completed work.
- Verify time-sensitive claims when they affect a new decision. A document cleanup retains the evidence cutoff of its sources.
- Put detailed evidence in a focused research record. Summarize its decision impact in the current opportunities page and link it there.
- Update existing current summaries in place. Keep historical chronology in research records and Git history.
- Reconsider an economic package when its scope, price, rights, funding or payment route changes; retain the scientific findings at their original evidence dates. Reading order and historical candidate rank supply context, while comparable commitments determine allocation.
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
