# ddiscov

Find drug-development opportunities that maximize the value of the next dollar invested, with a preference for credible success and bounded financial downside. Evaluate synthesis, formulation, preclinical work, repurposing and clinical development on the same basis: the next useful milestone, its cost and the economic value the project can retain.

## Start here

1. [Current opportunities](decisions/current-shortlist.md) — active questions and next decisions.
2. [Selection policy](decisions/selection-policy.md) — how to compare commitments.
3. [Agent guide](AGENTS.md) — focused retrieval, checks and update conventions.

**Evidence reviewed through 8 November 2026 (Round 26).** The latest screen highlights topical erlotinib/KRT16, FD-2/ALS and levodopa/carbidopa/MCT8 as distinct information questions. Current scopes, prices and attainable interests are needed to turn those priorities into an investment comparison. See the current opportunities page for the full decision context.

## Find the relevant detail

| Task | Entry point |
|---|---|
| Find a candidate, source or previous decision | [Research guide](research/README.md) |
| Review a specific research round | [Round index](research/rounds/README.md) |
| Browse earlier biological and product ideas | [Program atlas](atlas/README.md), [formulations](formulations/README.md), [discovery crosswalk](discovery/README.md) |
| Reproduce a calculation | [Methods](methods/README.md) |
| Trace original source versions | [Provenance](provenance/README.md) |

The repository contains literature reviews, source reconciliation, retrospective analyses and proposed work. Each evidence record retains its review date. Current decisions live in `decisions/`; detailed research and the cumulative register provide supporting history.

## Local tools

Python 3.9+ is sufficient for repository navigation and checks:

```sh
python3 scripts/repo.py status
python3 scripts/repo.py search 'erlotinib' --limit 8
python3 scripts/repo.py check
python3 -m unittest discover -s tests
```

Individual scientific analyses have the prerequisites listed in [methods](methods/README.md).
