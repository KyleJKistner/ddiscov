# ddiscov

Find drug-development opportunities that maximize the financial value retained from the next dollar invested, with a preference for credible success and survivable downside. Compare synthesis, formulation, preclinical work, repurposing, clinical development and participation in existing programs by the same standard: the next commitment, the economic interest obtainable, and the full path to retained value.

## Start here

1. [Current opportunities](decisions/current-shortlist.md) — packages to compare and the next useful information tasks.
2. [Selection policy](decisions/selection-policy.md) — how to compare commitments.
3. [Agent guide](AGENTS.md) — focused retrieval, checks and update conventions.

**Candidate evidence reviewed through 9 November 2026 (Round 27).** The [broad estimated screen](research/rounds/round27/README.md) compares 49 development packages across 48 asset/use combinations and selects four for deeper desk work: nifedipine/lidocaine, APR-246, topical erlotinib and CBD3063. AAT process work, topical insulin and verteporfin remain immediate product challengers.

The current workflow is **broad screening → estimated comparison → a handful for deeper desk diligence → inquiries**. Use explicit ranges for uncertain cost, time, success and retained value. Missing quotes do not prevent a provisional comparison. The [opportunity template](decisions/opportunity-template.md) records the assumed interest, consequential milestone and reversal conditions; stronger diligence follows as a commitment becomes concrete.

The [earlier commercial comparison](research/commercial/2026-11-08-repayment-screen/README.md) preserves counterparty background for later diligence. Its inquiry order is superseded by Round 27.

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
