# Research guide

Current priorities and evaluation rules live in [decisions](../decisions/README.md). The [shortlist reconciliation](strategy/2026-11-08-shortlist-reconciliation.md) integrates both research branches. The latest numbered review is [Round 28](rounds/round28/README.md), following the [49-package Round 27 screen](rounds/round27/README.md). The [commercial-route comparison](commercial-routes/README.md), [erlotinib dossier](phase2-program/erlotinib/README.md) and [35-candidate review](phase2-program/ranking-review/README.md) retain complementary evidence and dated conclusions.

## Find evidence

```sh
python3 scripts/repo.py search 'APR' --limit 8
rg -n 'APR-246' research/rounds/round25
```

`search` matches JSON string values and returns file locations and pointers. Use `show FILE /pointer` to retrieve a match. Shorten `/records/3/name` to `/records/3` for its enclosing record; large selections show available keys for a narrower lookup. Use `rg` for Markdown and CSV. Results are bounded so candidate work starts with focused context.

Search and format checks use Git's tracked and unignored files. Exported copies without Git skip common virtual-environment and cache directories. `status` reports the latest available evidence round linked from the current opportunities page.

| Location | Contents |
|---|---|
| [Shortlist reconciliation](strategy/2026-11-08-shortlist-reconciliation.md) | Unified research tiers, mandate, cost crosswalk and bounded next outputs. |
| [Round 28](rounds/round28/README.md) | Nifedipine/lidocaine clinical, regulatory and retained-cash review. |
| [Round 27](rounds/round27/README.md) | Broad 49-package screen; historical numerical ranks. |
| [Commercial routes](commercial-routes/README.md) | Dated comparison of earlier licensing, existing-sponsor contributions and human-anchored assets, with cost-provenance audit. |
| [Phase II candidate program](phase2-program/README.md) | Ten coordinator dossiers, twenty worker assignments, source-access limits, evidence gates and next information tasks. |
| [Marginal-capital strategy review](strategy/2026-11-08-marginal-capital.md) | Review of the commitment unit, broader sourcing and survivable financial exposure; separate from candidate evidence rounds. |
| [Round index](rounds/README.md) | One entry per research round, newest first. |
| [Screen index](screen-index.md) | Recent candidate ledgers and earlier screening catalogs. |
| [Cumulative register](portfolio-register.json) | Historical snapshot through Round 26: original coverage, source maps, earlier decisions and embedded round records. |
| [Original phase ledger](history/curated-ledger.md) | October 27–November 3 research history, organized by question. |
| [Reports](reports/README.md) | Earlier PDF reviews. |
| [Source data](source-data/README.md) | Original numeric data for reproducible audits. |

## Reading the cumulative register

The register retains its original structure for traceability. `coverage_records` contains 622 overlapping inventory records; `sources` maps source identifiers; `round3` through `round26` contain subsequent work. `current_marginal_dollar_decision` captures the last integrated decision at publication.

Earlier top-level fields such as `final_shortlist`, `policy`, `reading_rule` and `current_cross_portfolio_allocation` retain older instructions and rankings. Treat them as history. Use [current opportunities](../decisions/current-shortlist.md) and [selection policy](../decisions/selection-policy.md) for new work. Coverage counts describe records at different levels of aggregation; preserve their units when comparing them.

## Updating research

Store new evidence once, alongside its source identifiers and review date. Link a short decision summary from the current opportunities page. Add a round-index entry for a completed round. Historical dossiers and publication manifests retain the dates, claims and file hashes of their original review.
