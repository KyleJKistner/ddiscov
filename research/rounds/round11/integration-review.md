# Round 11 integration review

**Evidence cut: 4 November 2026. Baseline: `a66f2462541893b4dfb88b4f9aaa0d7863c204a8`.** This review integrates two existing-use audits and their source limits. It records content decisions, not a completed remote publication check.

## Decisions and accounting

Retain zinc acetate dihydrate/GNAO1 and taurine/SLC6A6 as conditional clinical-research reserves with independent asset holds. The 100-point allocation and leading 55/15/10/6 queue remain unchanged. There are **two existing uses reviewed, zero new screens, zero new molecules, and zero new unique people added to the treatment ledger**. The SLC6A6 target's actual additional unique-person count remains unknown. A previously unread Methods section, a new analysis-set interpretation, and a bibliographic match are not new participants or efficacy observations.

## Zinc: the analysis rule is recovered; endpoint counts are still open

The [zinc audit](zinc-endpoint-audit.md) resolves the main manuscript's missing-data approach: available observations contribute to descriptive analyses, while paired tests require both relevant visits. No formal missing-data method or imputation algorithm is reported in the inspected main text. This does not establish that missingness was random or inconsequential. The appendix and protocol were not recovered, so exact visit and paired counts for seven general secondary outcomes remain null.

Population membership now has a firmer interpretation. The FAS contains thirteen people and reports feasibility of 11/13. The mFAS excludes P3 and reports 10/12. P3 was exposed, withdrew after an unrelated serious adverse event, and had 80% reported adherence beforehand. P8 never received zinc but remains in the mFAS. The twelve-person safety set excludes P8 and includes P3. P3's membership in the FAS feasibility numerator follows from the published set definitions and numerator change; it is explicitly an inference. The eleven completers cannot be equated with the eleven feasibility successes. The other feasibility failure's identifier remains unresolved.

Neither twelve-person set supplies the effective N for every endpoint. The eight-person GMFM reference subset has a complete-pair definition and cerebral-palsy reference trajectories. It stays separate from the seven general endpoint rows and from the post-hoc propensity-matching analysis, whose achieved sample, matching details and balance remain unverified. Differences between available-case group means are not automatically mean within-person changes. No counts were inferred from plotted dots, variance or P values.

These findings improve interpretation without resolving causality. Exploratory functional signals and unchanged blinded movement severity remain controlling. The uncontrolled design and unresolved endpoint populations support the existing reserve and asset hold.

## SLC6A6: corroborated identity does not supply patient linkage

The [SLC6A6 audit](slc6a6-two-brother-audit.md) corroborates the 2023 title, cited authors, publication details and article URL through a later primary paper's reference list. The target abstract body was not recovered. Exact genotype, treatment article and chronology, functional outcomes, and report overlap therefore remain unknown.

The 2019 Preising p.A78E two-brother report is a possible linkage lead, not a verified identity assignment for the 2023 abstract. The original p.Gly399Val boy/girl pair and the later treated female exon-11-deletion proband retain their existing records. Count three directly extracted treated people across two pedigrees. No complete census, response rate, independent cardiac replication or new retinal rescue claim follows.

## Independent review and preservation

The [zinc review](independent-zinc-endpoint-review.json) and [SLC6A6 review](independent-slc6a6-review.json) bind their conclusions to the final dossier hashes. The SLC6A6 heading was clarified to keep report records separate until linkage is verified, avoiding an implied resolved number of lineages. That wording change does not alter data or decisions.

All earlier round packages, 622 original ordered coverage rows, source mapping and historical decision records remain preserved. Current findings are attached through the register and [root deltas](round11-root-deltas.json). The [local verification report](local-verification.json) records content checks; the [manifest](artifact-manifest.json) records expected paths and hashes. Remote commit, branch, tree and committed-manifest readback remains the separate publication verification.

Both retrieval attempts stop at their documented access ceilings. Reopen only for accessible primary documents supplying the specific unresolved fields. No outreach, purchases, recruitment, experiments, simulations or material receipt occurred.
