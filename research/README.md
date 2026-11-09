# Research guide

Current priorities and evaluation rules live in [decisions](../decisions/README.md). This directory supplies their evidence and history. The latest completed review is [Round 26](rounds/round26/README.md), dated 8 November 2026; [Round 25](rounds/round25/README.md) contains the latest consolidated incumbent reassessment and APR-246 advancement package.

## Find evidence

```sh
python3 scripts/repo.py search 'APR' --limit 8
rg -n 'APR-246' research/rounds/round25
```

`search` matches JSON string values and returns file locations and pointers. Use `show FILE /pointer` to retrieve a match. Shorten `/records/3/name` to `/records/3` for its enclosing record; large selections show available keys for a narrower lookup. Use `rg` for Markdown and CSV. Results are bounded so candidate work starts with focused context.

Search and format checks use Git's tracked and unignored files. Exported copies without Git skip common virtual-environment and cache directories. `status` reports the latest available evidence round linked from the current opportunities page.

| Location | Contents |
|---|---|
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
