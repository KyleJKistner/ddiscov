# Round 10 integration review

**Evidence cut: 4 November 2026. Baseline: `b21aaddd2270b6670a745c2197867316d46b5879`.** This document integrates the finalized dossiers and their independent reviews. It does not replace their source-level records or claim an already completed remote publication check.

## Portfolio decision and research accounting

Retain BLU3797, enasidenib, topical ruxolitinib, and lisdexamfetamine at ranks 1–4 and **55/15/10/6 planning-effort points**. The full 100-point allocation is unchanged. The two additional screens use the existing five-point discovery allocation; neither receives dedicated points or an S-tier designation.

The work consists of **two new exact intervention–use screens** and **five existing candidates reviewed**. Existing-candidate reviews cover BLU, enasidenib, ruxolitinib, SCARB2/miglustat, and ManNAc/GNE. Naltrexone is a comparator within the ruxolitinib workstream. Numbered patent comparators, unnamed conference leads, different salts, repeated case presentations, and analytic ledger rows do not become extra candidates.

The [alias audit](candidate-alias-audit.json) covers the entire 186-file baseline, including three PDFs and one XLSX, and the original 622 register rows. It adjudicates the workbook's isolated `Gnao1` measurement as a gene-only hit. Taurine was inventoried for other indications; the SLC6A6 exact use is additional. The count is therefore **two exact uses, zero new molecules**, with no ownership conclusion.

**ManNAc is explicitly linked to `historical-topics:T060`.** The original historical inventory and cumulative register already linked the AAN abstract, with fresh primary review marked false. The [controlled-result update](mannac-controlled-result.md) supplies a new current disposition after primary review; it does not claim a newly discovered candidate or newly published result.

## Outcomes and evidence boundaries

### BLU: retain qualification; exposure is still not a measured human window

The [exposure-feasibility dossier](blu-exposure-feasibility.md) independently recounts existing source measurements and adds exact comparator assay context. Five groups contain 26 numerical plasma entries, not a verified set of 26 independent animals linked to functional endpoints. Unknown postdose timing, analyte-method detail, unbound muscle exposure, and metabolite contribution remain unknown. The P22 workbook's BIDx5/QDx3 history is retained beside the caption-level twice-daily description.

The original patent drawing specifies GFP-C2β HEK cells, full medium, and a PKN1/2-sensitized pS6K readout for examples 36/40/90/96. The text legend confirms their mapping; this is a checked non-error, not a correction to earlier example identities. These results do not supply exact47 or exact91 live-cell access, native-muscle engagement, or occupancy. The 2024 abstract's three unnamed leads and 117-kinase panel excluding C2γ supply program context only. Omission is not demonstrated sparing.

These findings leave exact47 first in the comparator queue and BLU at 55 points. Missing exposure information neither proves inadequacy nor provides safety reassurance. The next useful evidence must identify an exact article and a decision-relevant exposure/function relationship.

### IDH: apply the current AGI-17011 override and stop an unsupported CNS ranking

The [43-row IDH ledger](idh-exposure-ledger.json) separates analyte, variant, assay, time, compartment, concentration basis, statistic, and denominator. **The current AGI-17011 interpretation supersedes categorical human absence.** EMA's clinical mass-balance sections identify M2/AGI-17011 as a minor human plasma metabolite, contradicting the same report's nonclinical wording. The 0.3% single-dose circulating-radioactivity exposure fraction cannot establish a chronic pediatric active burden or exclude one.

Preserve [Round 7's product JSON](../round7/enasidenib_product.json) and its historical `/pharmacology_interpretation/AGI17011` value. Carry the corrected interpretation into current decisions and the cumulative register with an explicit link to this round. The historical record documents what was previously concluded; the current override governs interpretation.

The ledger also retains metric-specific adult PK counts, mismatched assay incubation times, and missing AGI-69460 R140Q activity. The FDA tumor-ratio table and adjacent prose reverse dose assignments for one ratio; neither is silently repaired into a dose-response claim. Adult total tumor/plasma ratios, metabolite predose ratios, and binding arithmetic do not establish normal infant-brain free exposure. The public-data CNS-superiority comparison is closed as presently unidentifiable, while enasidenib's separate cardiac question and 15-point allocation remain affirmative.

### Clinical and discovery updates: preserve function without manufacturing response rates

| Evidence set | Current accounting | Limit on interpretation |
|---|---|---|
| [SCARB2/miglustat](scarb2-case-lineage-update.md) | Five retrieved treated people across four reports; Chaves adds one treated sister, not both described sisters. | Not a complete census or pooled success rate. Two unfavorable clinical trajectories share a family. New case genotype is unresolved; neither renal repair nor drug-caused death is established. |
| [Ruxolitinib/HHD comparator](hhd-active-care-comparator.md) | Four selected naltrexone cases across two reports. The 2025 presentation and 2026 report describe the same later case. | Do not pool with ruxolitinib or infer dose superiority. The nine-patient ruxolitinib preprint remains abstract-level and unpooled. |
| [ManNAc/GNE](mannac-controlled-result.md) | MAGiNE reports 54 treated: 37 ManNAc, 17 placebo. | Treated counts are not reconstructed endpoint-analysis counts. The investigator abstract reports no significant functional benefit, with no full effect interval or attrition table recovered. |
| [Taurine/SLC6A6](new-candidate-screen.md) | Three directly extracted treated people across two pedigrees; the cardiac pair are siblings. | The newer seven-affected-person cohort is not seven treated people. An unread two-brother abstract prevents a complete census. Residual transport, organ, and remaining tissue constrain transfer. |
| [Zinc acetate/GNAO1](new-candidate-screen.md) | 13 enrolled, 12 exposed, 11 completed; modified analysis set 12 includes the never-exposed refuser; external GMFM subset n=8. | Feasibility is not efficacy. The reference trajectories are cerebral palsy, not concurrent GNAO1 controls. Exact paired endpoint counts/imputation remain unresolved. |

The HHD comparison now asks what a specified cream adds over the relevant care pathway, including oral therapy, sweat control, infection treatment, rescue, and application burden. It does not require an oversized initial multi-arm trial or convert uncontrolled photographs into comparative efficacy.

The ManNAc negative result weighs against an undifferentiated muscle-strength proposition. Baseline imbalance and a nonsignificant per-protocol direction do not supply an unreported favorable adjusted effect. Nor does the abstract establish that every meaningful effect was excluded or every sialic-acid-pathway intervention failed.

The new zinc screen retains unchanged blinded movement severity and the earlier case's unchanged GMFM, residual weekly crises, hydromorphone cointervention, and gluconate-to-acetate sequence. The taurine screen retains mild baseline cardiomyopathy and absent demonstrated late-stage vision restoration. Both remain research reserves with asset holds. Existing clinical development, product identity, and a specific incremental contribution matter alongside a plausible mechanism.

## Independent challenge and the resolved provenance fix

Four independent JSON reviews bind their conclusions to exact file hashes:

| Review | Outcome and scope |
|---|---|
| [Clinical updates](independent-clinical-update-review.json) | Pass with explicit access limits. Covers ManNAc, SCARB2 and HHD identity, denominator, source-scope and inference handling; independently reopens Cao's primary case series without claiming a fresh audit of every source. |
| [IDH exposure](independent-idh-exposure-review.json) | Pass after a resolved provenance-only fix. The reviewer independently checked the disputed AGI-17011 passages and original FDA table/prose conflict. |
| [New screens](independent-new-candidate-review.json) | Pass without required fixes. Critical primary sections, pilot denominators, case formulation/cointervention, genotype/stage limits, baseline digest, and the gene-only workbook hit were checked. |
| [BLU exposure](independent-blu-exposure-review.json) | Pass without blocking fixes. Recounts workbook values, checks regimen ambiguity, original drawing/legend identity, engineered-cell limits, and the official conference abstract. |

The IDH review initially identified enasidenib-family missing-exposure rows that incorrectly reused an AGI-69460-specific TGA locator. The author replaced those with analyte-appropriate bounded-review locators and aligned all five missing-exposure rows. The reviewer verified that only those provenance strings changed; numeric values, unknowns, decision, and Markdown remained unchanged. **No requested fix remains.**

These are independent document/logic reviews, not independent clinical or experimental replication. Their recorded access ceilings remain part of the evidence package.

## Historical preservation and publication boundary

Round 10 adds current interpretations while preserving all prior round packages and the **622 original ordered coverage records**, original source mapping, generated concepts, and decision-history prefix. Current updates must not rewrite historical cohorts or inflate their original counts. In particular, Round 9's four-person retrieved SCARB2 set remains historically accurate even though the current set contains five.

The [Round 8 numerical specification](../round8/blu3797-qualification-spec.json) and [Round 9 manual qualification amendments](../round9/qualification-amendments.json) remain unchanged. Proposed numerical limits remain engineering choices, not newly validated clinical thresholds. The numerical utility does not automatically enforce manual source, model, or causal-interpretation requirements. This sprint adds no hidden systemic-safety gate before the already favored bounded first muscle proof.

[Local verification](local-verification.json) records completed strict parsing, internal links, source and review hashes, allocation, history consistency, and preservation checks against the baseline. The [artifact manifest](artifact-manifest.json) enumerates all expected repository files and content hashes under its stated self-reference rule. The separate publishing workflow verifies the containing commit, parent, branch/ref, complete tree and committed manifest by remote readback. This integration document records local content review and does not substitute for that remote verification.

Original third-party source files remain research intermediates unless already part of the historical repository. No outreach, purchases, recruitment, experiments, simulations, or material receipt occurred. The source review and integration work do not authorize those actions.
