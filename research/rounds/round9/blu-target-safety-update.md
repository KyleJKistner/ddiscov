# BLU3797: target safety, perturbation identity, and the selectivity bridge

**Round 9 research continuation · 4 November 2026.** Baseline: recovered Round 8 commit **a7f10cd8b84bc2ffe6a4cf0160f29e9ab443dad3**, KyleJKistner/ddiscov, main. This is a public-source evidence update and decision analysis. No experimental work, procurement, or contact occurred. The completed Round 8 files remain intact.

## Decision

**Retain BLU3797 as a bounded human-muscle qualification priority. This workstream alone does not justify changing its Round 8 rank or 55/100 planning-effort allocation.** Two newly integrated primary papers sharpen the interpretation of safety evidence. They do not supply human BLU efficacy, an exposure-defined BLU liability, or a validated therapeutic window.

The concrete change is to make two interpretation rules explicit in the next decision record: a normal resting-cell assessment cannot waive an unresolved C2α selectivity question; and a phenotype caused by removal of C2β protein cannot automatically be assigned to inhibition of its catalytic activity. Existing force, exposure, energy-function, and material gates remain applicable. The ≤20% antitarget goal remains a prospective clean-interpretation criterion, without promotion to a demonstrated safe threshold.

| Newly integrated evidence | Bounded decision change |
|---|---|
| Posor et al., PNAS 2025: adult C2α inactivation and stress susceptibility, with accessible main text, original figures, and supplement. [BS09-S02–S03] | Preserve a separate C2α selectivity decision even after reassuring baseline function. An unqualified endothelial assay cannot clear the systemic question. |
| Manupati et al., Molecular Cancer Research 2025: C2β protein loss and kinase-defective add-back have different consequences in a tumor model. [BS09-S04] | Separate protein abundance/scaffold effects from catalytic inhibition when using genetic controls or interpreting mTORC1. This is a modality distinction, not evidence that BLU causes or prevents cancer. |

Neither paper tested BLU3797 or exact compound 47. Neither is an independent replication of BLU efficacy.

## 1. The exact endothelial paper and the remaining information ceiling

The relevant C2β paper is **Kobialka et al., “PI3K-C2β limits mTORC1 signaling and angiogenic growth,” Science Signaling, 28 November 2023, DOI 10.1126/scisignal.adg1913, PMID 38015911**. Round 8 dates it correctly. Its abstract reports vessel enlargement through increased endothelial cell size in kinase-inactive mice and normalization with rapamycin. Rapamycin inhibits mTORC1; it is not pharmacological C2β inhibition. [BS09-S01]

The distinct October 2026 Aki Science paper concerns combined C2α/C2β deletion and mitochondrial fusion. The two records must not be merged into a single β-selective drug-safety study. [BS09-S07; Round 8 model dossier]

The current retrieval ceiling for Kobialka is explicit:

- The publisher returned 403. The UCL accepted-manuscript link timed out through web retrieval; the repository's alternate public URL returned 403 through a normal download. MDC points back to UCL. Europe PMC reports no PMCID or available full text.
- Targeted exact-title, DOI, supplement, and preprint searches produced no accessible primary replacement. An unrelated vascular-malformation thesis was identified and excluded.
- **No new Kobialka figure denominator, age distribution, allele-specific time course, effect size, or pharmacological C2β exposure was recovered.** These fields remain null in the structured record. No values are borrowed from Posor, Alliouachene, Aki, or another cell type.

The signal already justified a developmental/vascular question in Round 8. Failed retrieval does not increase or decrease its biological effect. Another workstream devoted to the same inaccessible links has low expected information value until a new public document or dataset appears. The unresolved source access is documented without making an author response a prerequisite.

## 2. New C2α evidence: baseline tolerance does not settle stress susceptibility

Posor et al. converted adult mice to C2α inactivity using an inducible floxed allele plus a constitutive D1268A allele. The protein-retaining model left roughly 50–65% total protein; fibroblast activity was 2.7 ± 0.6% of WT. Tissue recombination varied and was largely absent in brain. This is genetic, near-complete, persistent inactivation, not reversible drug exposure. [BS09-S02]

### Primary denominator extraction

| Source | Actual unit and reported group size |
|---|---|
| Figure 3A, LPS survival | WT 7 mice; flox24–25/D1268A 5; vehicle groups 5/3. Inactive survival reaches zero by 72 hours; logrank p=0.0081. |
| Figure 3C, second allele | WT 23; flox3/+ 5; flox3/D1268A 17 mice. |
| Figure 4B, Tie2-Cre deletion | WT 6; flox3/flox3 13 mice. |
| Baseline histology | 25 tissues from 4 males plus 4 females per group. |

These figures were visually inspected. The LPS comparison used 0.5 mg/kg; the experimenter was blinded. These counts concern **C2α**, and cannot fill the missing denominator in the older C2β histology report. [BS09-S02]

### What the supplement adds

The one-year cohort began with 10 WT and 6 inactive mice; later chemistry/immune assessments used 7/6. S5's negative primary-lung-endothelial experiment used cultures from 3–8 WT and 4–12 mutant donor mice across conditions. The S5 graph and most of its legend identify flox3/D1268A, while the final denominator sentence prints flox24–25/D1268A; that internal label discrepancy is retained. S6's negative endothelial cleaved-caspase-3 assessment involved 3 WT and 4 mutant animals. Thousands of counted cells are nested observations, not thousands of independent animals. [BS09-S03]

**Reviewer inference:** the useful lesson is the mismatch between resting or isolated-system reassurance and the organismal challenge. The source does not identify a transferable human exposure threshold. Its failure to reproduce sensitization in the tested lung endothelial cultures also means that merely adding a conventional endothelial viability assay would not close the uncertainty. A negative result in an insensitive model carries little evidence about the hypothesized liability.

The original hypothesis remains testable in principle, but its assessment needs a system demonstrably sensitive to the relevant perturbation. No such human assay has been qualified by this review. Consequently, the next decision should record C2α activity and exposure coverage separately from general viability. If a beneficial BLU exposure also materially engages C2α, the result merits a molecule/selectivity investigation even when resting morphology appears normal. It does not establish clinical toxicity, and it does not automatically invalidate the C2β target.

The adult genetic design improves relevance to post-developmental intervention compared with a wholly embryonic knockout, but does not remove all translation gaps. One mutant allele existed before induction, residual protein differed from normal abundance, recombination was tissue-dependent, and recovery after inhibitor washout was not studied. Those differences prevent converting a mouse genotype into a BLU percentage-occupancy or duration limit.

## 3. New C2β evidence: protein removal and catalytic inhibition are different interventions

Manupati et al. found increased lung metastasis after deletion of C2β from HER2-positive mammary tumor cells. Re-expression of WT or the authors' kinase-defective construct reduced mTORC1 signaling, migration, and invasion; only WT restored the lipid-product signal. The KD construct contains **K1058A/S1077A/D1170A** as printed, not the mouse D1212A allele. [BS09-S04]

Figure 1 uses 5 mice/group for transplantation comparisons. Figure 4 reports n=4 for the lipid fluorescence readout and n=6 replicates for migration/invasion; those labels do not establish independent donor or animal counts. The main text describes WT/KD in-vivo add-back in Supplementary Figure S4, but that supplement was not successfully retrieved here, so its exact denominator remains unverified. Similar responses are not a formal equivalence demonstration. [BS09-S04]

**Reviewer inference:** this provides an empirical counterexample to the rule that every consequence of C2β depletion must follow from blocking its catalytic site. It strengthens the distinction already made in Round 8, rather than licensing a favorable safety assertion. A kinase inhibitor might preserve protein abundance while altering a protein interaction or localization; stable total protein alone therefore does not prove preserved scaffold function.

For BLU interpretation, the appropriate causal unit is the exact perturbation in the exact tissue. A delayed depletion control is informative about the target protein, but cannot stand alone as a catalytic-inhibitor safety surrogate. Conversely, kinase-defective add-back in a transformed tumor cell is not evidence that neuronal, endothelial, cardiac, or muscle responses will be kinase-independent. The endothelial catalytic-inactivation signal and the tumor scaffold result can both be true.

The practical record should keep total C2β abundance, engagement-compatible evidence, catalytic/functional pharmacodynamics, and the genetic intervention in separate fields. This reinforces the existing unheated protein control in the native-engagement plan. A decrease in total protein must not be mistaken for a drug-induced thermal shift. It also makes a global mTORC1 direction an unsuitable substitute for tissue-specific beneficial function or safety.

No cancer incidence rate, patient risk estimate, or chronic BLU safety conclusion is derived from these transplantation experiments. The new paper is a reason to interpret genetic evidence more precisely, without adding an unvalidated oncology program before the first informative muscle result.

## 4. Exact BLU / compound 47 / C2α / VPS34 bridge

The published molecule and assay identity remain indispensable. These are carried-forward primary measurements, rechecked against the article and original patent table; they are not new pharmacological results.

| Exact article / comparison | Present evidence | Unresolved bridge |
|---|---|---|
| BLU3797 → C2β | 28 nM biochemical IC50; 68.2 nM engineered NanoBRET IC50. [BS09-S05] | The Round 8 enzyme-description, reaction-condition, tracer, native-muscle, and measured-exposure qualifications remain. |
| BLU3797 → C2α | C2α is absent from the reported cellular selectivity table. [BS09-S05] | There is no matched native-cell C2α window to apply to the newly integrated stress evidence. |
| BLU3797 → VPS34 | Published NanoBRET IC50 14,366 nM; previously audited released response cells are all zero. [BS09-S05; Round 5 source audit] | Preserve both the publication and the unresolved source-data conflict. The C2α paper does not adjudicate VPS34. |
| Exact compound 47 → C2β | Patent C2β IC50 56 nM with Δ1–297/DPK1248–1250→KKT enzyme, 40 µM ATP. [BS09-S06] | Not directly rankable against BLU's different assay. Lysate binding does not establish cell entry. |
| Exact compound 47 → C2α / VPS34 | At 10 µM: 5% / −13% inhibition, each at the target's apparent ATP Km. Original Table 5, printed p.130, re-inspected. [BS09-S06] | Single-point cell-free measurements provide a favorable qualification prior, not a cellular or chronic safety margin. Retain the negative normalized value. |

**Reviewer inference:** the PNAS result increases the decision value of resolving BLU's missing C2α measurement. It does not prove that BLU inhibits C2α, and no numerical increase in risk can be assigned without the exposure bridge. Exact 47 remains the first comparator to qualify, because its different core and existing profile could help discriminate an exact-molecule liability from a β-associated effect. It is still not a fully qualified orthogonal probe. Its shared acetamidothiazole motif, possible residual off-targets, and missing native exposure must remain visible.

A comparison is useful only after both compounds have interpretable activity and exposure in the relevant context. A negative functional result from a compound that never reaches its target cannot rebut the target. Agreement at the same nominal concentration is also insufficient: it can compare different β modulation, different antitarget effects, or different free exposure.

The existing 20% C2α/VPS34 goal is not recalibrated from these sources. In particular, the 5% single-point C2α result for compound 47 cannot be turned into an exact IC50 or a wide safety margin by assuming a Hill slope, complete inhibition plateau, and comparable ATP. The same prohibition applies to inferring a new VPS34 constant from negative normalized inhibition or the BLU all-zero workbook cells.

## 5. Decision-record changes and allocation

| Decision field | Update now | Consequence |
|---|---|---|
| C2α uncertainty | Add an explicit unresolved stress-context flag until an exposure-linked selectivity assessment is interpretable. | Normal baseline viability, normal gross morphology, or a small kinome score cannot waive it. |
| Vascular-model readiness | Require evidence that an assay can detect the relevant perturbation before using its negative result as clearance. | An unqualified negative is inconclusive. This is an interpretation rule, not an instruction to execute a new assay. |
| Genetic-control identity | Record allele/construct, timing, tissue, protein abundance, and whether catalysis or protein expression was altered. | Adverse and favorable deletion phenotypes remain distinct from catalytic-inhibitor outcomes. |
| Native target assessment | Retain the existing total-protein/unheated control and separate it from thermal engagement evidence. | Protein depletion cannot masquerade as a binding readout. Stable abundance alone does not certify intact scaffolding. |
| Compound comparator | Retain exact 47 ahead of 91, contingent on its own exposure, activity, and selectivity. | No promotion to a replacement development article on the patent table alone. |
| Quantitative qualification thresholds | No numerical change from this workstream. | No novel safe occupancy, free concentration, human dose, or threefold chronic margin is claimed. |

**Allocation recommendation:** preserve the existing **55 planning-effort points** for the BLU decision unless a competing workstream changes the cross-portfolio opportunity cost. This is neither a spending authorization nor an allocation to conduct experiments. Within that effort, the new priority is an interpretable β-versus-α exposure/perturbation record. Do not expand effort merely to repeat inaccessible-source searches or produce another uncalibrated safety checklist.

The new papers do not yet supply the likelihood of useful human force rescue or the probability of a safe systemic product. In Bayesian terms, they alter which future observation would be informative: matched C2α modulation at a beneficial exposure is more valuable than another normal resting morphology result; a well-matched catalytic comparator is more informative than an unqualified depletion phenotype. Neither changes the existing absence of exact-BLU human functional proof.

The information ceiling remains the same at the decisive level: received article identity, native beneficial exposure, required β modulation, selectivity at that exposure, and a relevant functional safety window have not been measured in this research continuation. Further public-source work should reopen these questions only for a source that can change one of those fields. The portfolio can continue advancing comparative evidence while those fields remain explicit unknowns.

## Primary sources and provenance

- **BS09-S01 — Kobialka et al., 2023.** [PubMed PMID38015911](https://pubmed.ncbi.nlm.nih.gov/38015911/) · [DOI10.1126/scisignal.adg1913](https://doi.org/10.1126/scisignal.adg1913) · [UCL accepted-version record](https://discovery.ucl.ac.uk/id/eprint/10186576/) · [MDC record](https://edoc.mdc-berlin.de/id/eprint/23911/). Abstract and metadata available; full manuscript/supplement inaccessible in this bounded retrieval. Web references: turn6view0, turn6view1, turn8search0.
- **BS09-S02 — Posor et al., PNAS 2025.** [Publisher main text](https://www.pnas.org/doi/10.1073/pnas.2423358122) · [PMC12304892](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304892/) · [Europe PMC full XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12304892/fullTextXML). Main XML and figures3/4 downloaded and inspected. Web references: turn25view0, turn28view3, turn24search1. XML SHA256: a27770c1a2ebe6191336432cce263aa94691ed0153403f72194791de540609fc.
- **BS09-S03 — Posor supplementary appendix and figures.** [Publisher supplement](https://www.pnas.org/doi/suppl/10.1073/pnas.2423358122/suppl_file/pnas.2423358122.sapp.pdf) · [Official Europe PMC supplementary-file package](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12304892/supplementaryFiles). Publisher fetch failed; the official repository package succeeded. Supplement PDF SHA256: 3211f7720b0d8d5ad17bb484e0dcdb99fcc33489c717b0cc8e7163fe73c3745f. S5 original PDF page8 was rendered and visually checked; S2/S6 captions and extended methods were extracted.
- **BS09-S04 — Manupati et al., Molecular Cancer Research 2025.** [Primary accepted full text, PMC12353924](https://pmc.ncbi.nlm.nih.gov/articles/PMC12353924/) · [DOI10.1158/1541-7786.MCR-24-1045](https://doi.org/10.1158/1541-7786.MCR-24-1045). Main text and figure captions inspected through web retrieval; ordinary local PMC, Europe PMC XML, and supplemental S4 retrieval did not return the requested primary content. The locally archived web snapshot is an access record, not an original article PDF. Web references: turn32view0, turn35view0, turn49view0. No S4-specific numerical result is independently extracted.
- **BS09-S05 — Shearer et al., JCI Insight 2026.** [Main article](https://insight.jci.org/articles/view/198568) · [DOI10.1172/jci.insight.198568](https://doi.org/10.1172/jci.insight.198568). Main article reopened; source-data conflict and identity limits carried forward from the preserved Round 5/8 audits. Web references: turn44view1, turn33search2.
- **BS09-S06 — WO2025003330A1, 2 January 2025.** [Primary patent disclosure](https://patents.google.com/patent/WO2025003330A1/en). Original cached PDF Table5, physical page131/printed130, visually re-inspected. Original PDF units govern over erroneous OCR. Web references: turn44view0, turn45view0. This report makes no new patent-rights conclusion.
- **BS09-S07 — Aki et al., Science 2026.** [DOI10.1126/science.adx9628](https://doi.org/10.1126/science.adx9628) · [PMID42848893](https://pubmed.ncbi.nlm.nih.gov/42848893/). Kept as the separate combined-deletion lineage from Round 8; no newly recovered full-text result or denominator.

The accompanying JSON records evidence status, denominators, gate changes, source URLs, access failures, and hashes. Downloaded third-party source files are research intermediates, not part of the proposed repository publication. No access failure is represented as a biological negative.
