# Phase II candidate program

Ten coordinator teams investigate different routes to a promising drug-development candidate. Each owns an evidence scout and a translational/commercial challenger: **10 coordinators + 20 workers**, directed by an integrating lead. The question is which exact drug/use and obtainable economic interest deserves the next bounded commitment.

**First pass completed, 8 November 2026:** all ten coordinators and twenty workers ran in five waves. Their findings and unresolved next actions are recorded below. No agents continue running as a background service after the session.

**Planning envelope:** approximately $500,000. This is a constraint, not a spending target or an authorization. Maximum acceptable cumulative loss, minimum reserve, liquidity horizon and follow-on funding remain unresolved. The objective is a high probability of recovering invested cash with a return; no current first-pass analysis establishes that outcome.

## Read only what the task needs

1. [First-pass synthesis](synthesis.md) — results, prioritized information tasks and remaining limits.
2. [Phase II evidence standard](phase2-evidence-standard.md) — event definitions, historical anchors and nomination gates.
3. [Team registry](registry.json) — assignments, actual agent identities, completion states and next actions.
4. [Coordinator brief](TEAM-BRIEF.md) and [candidate template](candidate-template.md) — reusable instructions.

The [current opportunities](../../decisions/current-shortlist.md) remain the active decision source. The [selection policy](../../decisions/selection-policy.md) governs financial comparison. This focused review supplements the Round 26 evidence base; it does not silently refresh every historical source or replace the broad marginal-capital objective.

## Teams

| Coordinator | Distinct search route | Output |
|---|---|---|
| 01 | Genotype-matched existing drugs | [Genotype repurposing](teams/01-genotype-repurposing.md) |
| 02 | Local dermatology with human evidence | [Local dermatology](teams/02-local-dermatology.md) |
| 03 | Human genetics and target direction | [Genetic targets](teams/03-human-genetic-targets.md) |
| 04 | Clinically characterized discontinued assets | [Shelved clinical assets](teams/04-shelved-clinical-assets.md) |
| 05 | Rare neurometabolic function | [Neurometabolic](teams/05-rare-neurometabolic.md) |
| 06 | Ocular local delivery and repair | [Ocular](teams/06-ocular-local-delivery.md) |
| 07 | Neuromuscular translation | [Neuromuscular](teams/07-neuromuscular-translation.md) |
| 08 | Ex vivo organ preservation | [Organ preservation](teams/08-organ-preservation.md) |
| 09 | Precision CNS and controlled function | [Precision CNS](teams/09-precision-cns.md) |
| 10 | Early synthesis and bounded institutional options | [Synthesis/options](teams/10-synthesis-options.md) |

## Execution and continuation

The session permits seven active agents: the integrating lead, two coordinators and four workers. Run the ten teams in five waves, finishing each team's workers before releasing the coordinator. These are real session agents; the repository stores their research and continuation instructions. It is not a continuously running background service.

```sh
python3 scripts/phase2_program.py status
python3 scripts/phase2_program.py packet 03
python3 scripts/phase2_program.py check
```

`packet` prints the assignment for an agent-capable session; it does not launch one. For a new pass, record new actual agent identities and source cutoffs in a separate dated execution record, preserve this run's lineage, and update the current synthesis after reconciliation. Reuse finished workers only if their new assignment and resulting work are explicitly recorded. Never label an unlaunched assignment as completed.

Workers return compact evidence and challenge records to their coordinator. The coordinator owns its dossier; only the integrating lead edits the registry, synthesis and active decision pages. Dossiers include source-access limitations, exact denominators, contrary findings, a lead, an alternative and the next decision-changing artifact. A source-check failure remains a limitation rather than becoming a verified claim.

At integration, merge overlapping candidates and cohorts, retain scientific disagreement, and separate clinical promise from investability. Each next action requires a clear completion condition and a reason it could change the capital decision. A new review starts only when a named artifact, changed evidence or changed terms can alter that decision; repeated literature summaries do not by themselves justify another pass.

## Capital discipline

No laboratory order, clinical trial, purchase, license or outreach is authorized by this research setup. For proposed spending, use the opportunity template and establish attainable rights, all-in cash exposure to a genuine stopping point, continuation funding and retained-cash scenarios. Compare with acting on current evidence or preserving capital. Do not divide the budget equally among teams or assume the full budget can carry an asset through Phase II.

The potentially strongest approach is to buy access to already informative human evidence, a well-matched population and a decisive next milestone. Novel synthesis remains eligible when it produces more decision value per dollar under the same criteria. The number of agents does not improve a drug's biological odds; better source coverage and independent challenge can improve selection.
