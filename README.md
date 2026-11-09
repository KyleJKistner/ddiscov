# ddiscov

Find drug-development opportunities that maximize the financial value retained from the next dollar invested, with a preference for credible success and survivable downside. Compare synthesis, formulation, preclinical work, repurposing, clinical development and participation in existing programs by the same standard: the next commitment, the economic interest obtainable, and the full path to retained value.

## Start here

1. [Current opportunities](decisions/current-shortlist.md) — packages to compare and the next useful information tasks.
2. [Selection policy](decisions/selection-policy.md) — how to compare commitments.
3. [Agent guide](AGENTS.md) — focused retrieval, checks and update conventions.
4. [Phase II candidate teams](research/phase2-program/README.md) — ten coordinators, twenty workers, independent challenge and candidate-specific next actions.

**Current reconciliation: 9 November 2026 UTC / 8 November Los Angeles.** The [unified shortlist](decisions/current-shortlist.md) governs the next research round: APR/erlotinib jointly lead; CBD3063 and the insulin/AAT/verteporfin gap checks form the next tier; nifedipine/lidocaine is a conditional reserve. The [reconciliation record](research/strategy/2026-11-08-shortlist-reconciliation.md) combines the broad screen, focused dossiers and commercial-route comparison. Research proceeds using explicit estimates. No reviewed opportunity establishes the desired high probability of recovering invested cash plus a return; capital deployment remains a separate decision.

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
