# Round 10 — IDH parent/metabolite exposure ledger

**Decision: retain enasidenib at 15 of 100 planning points and retain the separate cardiac question. CNS superiority of enasidenib or vorasidenib for IDH2-R140Q D2HGA2 is not identifiable from the reviewed public evidence.** The finite comparison is closed at that evidence ceiling. Neither an infant dose nor a treatment recommendation follows from this ledger.

Baseline: `b21aaddd2270b6670a745c2197867316d46b5879`. Review date: 4 November 2026. The accompanying JSON preserves analyte, species, age scope, variant/assay, compartment, concentration basis, time, statistic, denominator and source locator for 43 rows. Unknowns are explicit nulls. All work was public-document analysis; no outreach, purchase, experiment, simulation or Git action was performed by this workstream.

## 1. Correct the component ledger before comparing the drugs

### AGI-17011 cannot be categorically excluded from humans

Round 7's enasidenib dossier states that AGI-17011 was not detected in humans, following EMA's nonclinical wording on p18. The same assessment's clinical mass-balance section, pp33–34, identifies **M2 as AGI-17011** and reports **0.3% of circulating total-radioactivity exposure** after a single oral 100-mg radiolabeled dose. The clinical discussion on p46 again lists M2 (AGI-17011) among minor human plasma metabolites. The report therefore contains an internal inconsistency. Its clinical sections do not support the inherited blanket absence claim. [EEMA]

The current interpretation is: **AGI-17011 is reported as a minor human plasma metabolite, with biochemical R140Q activity; its steady-state, pediatric and normal-brain contribution remain unidentified.** Preserve the historical Round 7 files and attach this correction to the current decision record. The affected JSON field is `/pharmacology_interpretation/AGI17011`. A small single-dose radioactivity fraction establishes neither an important chronic active burden nor no chronic contribution. [EFDA, p27; EEMA, pp18,33–34,46]

### Exact variant and assay remain essential

| Analyte | Exact published context | Result | Denominator / time | Interpretation |
|---|---|---:|---|---|
| Enasidenib parent | Recombinant IDH2-R140Q, coupled NADPH enzyme assay | IC50 0.77 µM | 1 hour; n not given in table | Carried from R7; not matched to the metabolite's longer incubation |
| AGI-16903 | Same regulatory enzyme-assay summary, IDH2-R140Q | IC50 0.016 µM | 16 hours; n not given | Established active human metabolite; carried from R7 |
| AGI-17011 | Same regulatory enzyme-assay summary, IDH2-R140Q | IC50 0.205 µM | 16 hours; n not given | Human-detection interpretation corrected above |
| Vorasidenib parent | TF-1 overexpressing IDH2-R140Q | IC50 14 ± 1.1 nM | Mean ± SD, reported assay n=3 | Carried from R8/R9; nominal cellular concentration |
| Vorasidenib parent | U87MG overexpressing IDH2-R140Q | IC50 7.1 ± 3 nM | Mean ± SD, reported assay n=7 | Carried from R8/R9; not normal neuronal tissue |
| AGI-69460 | HT1080, IDH1-R132C | IC50 264.0 nM | PMDA reports n=1 | Same-study FDA parent comparator: 46.97 nM |
| AGI-69460 | TS603, IDH1-R132H | IC50 6.709 nM | PMDA reports n=1 | Same-study FDA parent comparator: 0.117 nM |
| AGI-69460 | Engineered HCT-116, IDH2-R172K | IC50 585 ± 338 nM | Mean ± SD; reported assay n=3 | Newly recovered exact variant; R172K cannot substitute for R140Q |
| AGI-69460 | **IDH2-R140Q** | **Not identified** | No exact result in reviewed sections | Missing evidence does not mean inactivity |

Sources: EFDA printed p27, Table 3; VFDA printed pp47–48, studies AG881-N-068/-069 and Table 2; PMDA printed p6 / physical p9, §3.1.2.1. PMDA describes LC-MS/MS measurement of cellular 2-HG. Its assay counts are not patient counts, and the review does not fully specify their independence unit. FDA's separate parent HT1080 value of 4.0 ± 0.3 nM in Table 2 comes from another study; it must not replace the matched 46.97-nM value merely because the cell-line name is the same.

The precise AGI-69460 values and counts are additions to the repository. AGI-16903 binding, its R140Q potency, enasidenib A3 functional antagonism and parent vorasidenib R140Q cellular activity were already known. This sprint does not count them as discoveries or new efficacy evidence.

## 2. Multiple-dose exposure is a different quantity from radioactivity fraction

### Enasidenib has measurable chronic parent and active-metabolite exposure

FDA Tables 76B and 77B summarize the **100-mg once-daily** group in AG221-C-001, an adult advanced-hematologic-malignancy study, with a 15 April 2016 data cutoff. Both original table images were checked. Each entry below is a **geometric mean**, with geometric CV in parentheses. The column cohort is 102, but the denominator changes by parameter. [EFDA, printed pp154,156 / physical pp155,157]

| Parameter | Parent enasidenib | AGI-16903 | Evaluable n for each analyte |
|---|---:|---:|---:|
| Multiple-dose Cmax | 13,255 ng/mL (46.3%) | 1,220 ng/mL (41.8%) | 102 |
| AUC0–10h | 106,661 ng·h/mL (47.7%) | 9,640 ng·h/mL (41.8%) | 90 |
| AUC0–10h accumulation ratio | 11.82 (65.1%) | 23.10 (96.0%) | 35 |
| Cmax accumulation ratio | 10.31 (59.7%) | 14.35 (56.7%) | 40 |

The accumulation rows include only participants with both single-dose **Day −3** data and a multiple-dose **steady-state-cycle** assessment. The summary does not establish one common sampling cycle for every participant or provide individual pairing identifiers. AUC0–10h must not become AUC0–24h. Separate Cmax summaries do not imply simultaneous peaks. The exact formulation lot is not resolved by these tables and is not assumed to be the pediatric sprinkle.

R7 already retained parent 98.5% and AGI-16903 96.6% human plasma protein binding. The following are transparent arithmetic demonstrations, not measured free exposure:

- Parent: 13,255 ng/mL × (1 − 98.5/100) = **198.825 ng/mL**, approximately 199 ng/mL.
- AGI-16903: 1,220 ng/mL × (1 − 96.6/100) = **41.48 ng/mL**, approximately 41.5 ng/mL.

Each combines an adult total-plasma summary with an in-vitro binding fraction. Neither is an infant, myocardial or brain concentration, and they must not be added as a synchronized active-moiety concentration. No PK model was fitted or simulated. The useful conclusion is that chronic metabolite accounting needs its own time and denominator. [ELBL, §12.3; EFDA, Tables 76B–77B]

### Vorasidenib's delayed metabolite needs the same discipline

| Observation | Value and population | Boundary |
|---|---|---|
| Parent label Cmax | Mean 133 ng/mL, CV 73%, highest approved 40-mg daily tablet regimen at steady state; summary n unstated | A parent peak cannot be treated as simultaneous with a Cycle 10 metabolite trough |
| AGI-69460 trough after one treatment cycle | Mean 61.72 ng/mL, AG881-C-004 | Aggregate glioma PK; parameter-specific n unstated |
| AGI-69460 predose Cycle 10 Day 1 | Mean 128 ng/mL, same pivotal trial | Sparse late predose sampling; not an AUC |
| Molar metabolite/parent predose ratio | 1.173 at Cycle 10 Day 1; FDA rounds to 1.17 | Carried from R9; not an AUC or potency-adjusted ratio |
| Human plasma unbound fraction | Parent 2.66 ± 0.18%; metabolite 13.0 ± 1.07% | The TGA passage does not label the dispersion type or establish infant binding |
| Metabolite radioactivity fraction | Approximately 9% in pooled plasma AUC0–72h and 44% in AUC96–336h after one dose | AG881-C-005, healthy subjects, 50-mg radiolabeled powder-in-capsule; interval-dependent fractions are not steady-state concentrations |

Sources: VLBL §12.3; VFDA printed pp105–106; TGA printed pp15–16. FDA describes intensive samples only predose, 0.5, 2 and 4 hours on Cycle 1 and Cycle 2 Day 1, with later predose sampling; the metabolite's PK profile was not adequately characterized. The R9 facts that AGI-69460 was excluded from the population PK model and that the dataset contained only one observed participant younger than 18 remain controlling. Those facts do not supply an infant bridge. [TGA, pp17–18]

TGA's discussion of metabolite contribution for **IDH1-R132H versus IDH1-R132C** is mutation-specific. It cannot be imported into R140Q D2HGA2. A more weakly bound metabolite with substantial trough exposure could matter, but a quantitative R140Q contribution requires its exact activity and relevant free-tissue exposure. Both remain unresolved.

## 3. Audit the compartment denominator, then close the unsupported CNS ranking

The FDA review's Table 21 reports parent vorasidenib tumor ratios in the perioperative AG120-881-C-001 study using **early F1 tablets**. Its adjacent prose reverses the dose assignments for the Cavg row. The original page was visually checked; this is a source conflict, not a text-extraction artifact. The table is transcribed below without silently repairing it. [VFDA, printed p105 / physical p106]

| Total-concentration ratio, as Table 21 is headed | 50 mg daily F1 | 10 mg daily F1 |
|---|---:|---:|
| Brain tumor / concurrent plasma | Mean 2.08; 90% CI 1.50–2.67; n=7 | Mean 2.30; 90% CI 1.74–2.85; n=7 |
| Brain tumor / plasma Cavg | Mean 1.69; 90% CI 1.35–2.03; n=9 | Mean 2.94; 90% CI 2.07–3.82; n=7 |

The prose instead assigns 1.69 to 10 mg and 2.94 to 50 mg. Neither dose-response interpretation is adopted. This does not erase evidence of parent drug reaching glioma tissue. It prevents an unjustified precise dose comparison. The label's tumor ratio of 1.6 and TGA's approximately 2.0 are not automatically contradictory because their exact summaries and denominator contexts differ.

All these values concern **total drug in tumor relative to plasma**. They do not identify unbound exposure in a child's normal brain. R7's enasidenib rat brain penetration of 10% and CSF penetration of 0.3% followed a single 50-mg/kg oral study; they are also unsuitable as matched human unbound partition coefficients. TGA explicitly notes that AGI-69460 brain penetration was not assessed in animals. [EFDA, pp41–42; TGA, p13]

The unresolved comparison is specific:

| Required bridge | Status after this sprint |
|---|---|
| Exact AGI-69460 IDH2-R140Q potency under interpretable assay conditions | Not identified in the reviewed FDA, TGA or PMDA sections |
| Matched free parent/metabolite plasma exposure in the relevant pediatric disease setting | Not identified |
| Normal-brain unbound partition for each active component at relevant age and time | Not identified |
| Demonstrated CNS functional benefit in D2HGA2 for vorasidenib | No new evidence recovered in this workstream |
| Quantitative comparison of joint on-target and off-target exposure | Not identifiable from these mismatched data |

**Close the public-data CNS-superiority question as presently unidentifiable.** This is a bounded evidence conclusion, not proof that a drug cannot enter normal brain or that undisclosed data do not exist. Reopen only for new exact-variant metabolite activity, matched normal-brain free exposure, or age-relevant human PK that could change the choice. Repeating adult tumor-ratio comparisons cannot fill these fields.

## Development consequence and stopping rule

No new independent D2HGA2 clinical outcome was added. The existing enasidenib cardiac observation remains disease-matched but confounded by concurrent care; it is not converted into neurological rescue. Consequently, the evidence neither warrants a promotion above the existing **15 planning points** nor displaces enasidenib with vorasidenib solely on tumor distribution.

The concrete contribution is an **exposure-qualified pediatric development record**: retain component identity, repeated-dose timing, exact administered article, concomitant treatment and organ-specific outcome interpretation. A product proposition still needs one demonstrable improvement in administration, exposure consistency, measurement burden or interpretable organ benefit over the existing pediatric article. The published sprinkle precedent remains in place; this literature exercise establishes neither a new formulation nor rights clearance. [R7 product dossier; R8 clinical challenge]

The bounded sprint recovered three useful evidence blocks: component identity/activity, time-resolved exposure, and compartment/denominator integrity. FDA's current large-PDF web failure was resolved with an already archived full official copy; EMA's enasidenib access failure likewise had a full archived copy. The inaccessible full vorasidenib EMA report was not treated as read. No access failure was counted as biological evidence. Further unfocused searching is stopped.

## Primary source key

- **EFDA:** [FDA enasidenib multidisciplinary review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2017/209606Orig1s000MultidisciplineR.pdf), reference 4131433; printed p27, pp41–42, Tables 76B/77B on pp154/156. Physical page is printed page + 1.
- **EEMA:** [EMA IDHIFA withdrawal assessment](https://www.ema.europa.eu/en/documents/withdrawal-report/withdrawal-assessment-report-idhifa_en.pdf), EMA/CHMP/13746/2020; printed/physical pp18,33–34,46.
- **VFDA:** [FDA vorasidenib multidisciplinary review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/218784Orig1s000MultidisciplineR.pdf), reference 5425021; printed pp47–48,95,105–106. Physical page is printed page + 1. Applicant-labeled sections do not necessarily represent FDA conclusions.
- **TGA:** [AusPAR Voranigo, finalized 21 May 2025](https://www.tga.gov.au/sites/default/files/2025-05/auspar-voranigo-250521.pdf), printed/physical pp13,15–18.
- **PMDA:** [Japanese Voranigo assessment, 2025](https://www.pmda.go.jp/drugs/2025/P20251023001/530457000_30700AMX00228_A100_1.pdf), §3.1.2.1 on printed p6 / physical p9. Cover deliberation date 29 August 2025; review date 7 August 2025.
- **ELBL:** [IDHIFA prescribing information](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=a5b4cdf0-3fa8-4c6c-80f6-8d8a00e3a5b6), §12.3, carried from R7.
- **VLBL:** [VORANIGO prescribing information](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=31405fee-55b7-4857-987e-2724ee76be84&type=display), §12.3, archived official label checked.

Full local-source SHA-256 values and source paths are recorded in the JSON. Original regulatory PDFs are not republished in the repository.
