# Round 10 — BLU3797 exposure ceiling and exact-comparator feasibility

**Reviewed:** 4 November 2026. **Baseline:** `b21aaddd2270b6670a745c2197867316d46b5879` on `main`. This is public-document research and arithmetic on released measurements. No material was obtained, no person was contacted, and no experiment or simulation was conducted.

## Decision

**Retain BLU3797 at 55/100 planning points and continue the bounded human-muscle qualification project. Exact patent compound 47 remains the first comparator to qualify.** The inspected public documents do not identify the unbound muscle exposure, distribution, or metabolite contribution needed to turn the reported mouse plasma concentrations into a human therapeutic window. This does not show that exposure is inadequate; the relevant quantities remain unidentified.

The additive result is an exact-source clarification of the comparator's cellular evidence. The original patent's Figure 4B specifies **GFP-PI3KC2β HEK cells** in full medium. Its legend identifies examples **36, 40, 90 and 96**, matching the drawing's DC codes. The existing numerical identity mapping is therefore supported. These engineered, PKN1/2-sensitized pS6K results do not establish live-cell activity for examples 47 or 91, native-muscle engagement, or fractional occupancy. [B10-S2]

A newly retrieved 2024 conference abstract describes three unnamed C2β leads and a 117-kinase panel that excludes C2γ. It provides no article identities, numerical cellular potencies, exposure data or full panel results. It supports a comparator-discovery program, but it cannot fill an exact47, exact91 or BLU field. Its authors overlap the patent team, so it is not independent replication. [B10-S3]

## What is new, and what is carried forward

| Item | Round 10 status | Consequence |
|---|---|---|
| GFP-tagged C2β HEK context and full medium in patent Figure 4B | **New to the repository's extracted assay metadata**, verified in the original drawing | Adds a model-context limitation to the cellular evidence; no exact47 cell-access upgrade |
| Figure 4 legend names examples 36/40/90/96 | **Reverified**; resolves a provisional cross-mapping concern | Preserve the prior identity assignment; no correction to historical example numbers |
| Three unnamed leads; 117-kinase panel excluding C2γ; preliminary cellular claim in 2024 abstract | **New source**, at program level | No additional qualified comparator; no selectivity or PK transfer to a named article |
| Five mouse plasma groups and 26 numerical measurements | **Carried forward and independently re-counted** from the same JCI workbook | Source-location and denominator audit, not 26 new observations or an independent study |
| No located matched unbound tissue profiles, ADME package or quantified metabolites for exact BLU | **Carried forward; bounded source check** | Human exposure and systemic selectivity margins remain non-identifiable |
| Exact47 cleaner than exact91 in the published single-point panels | **Carried forward** | Keep 47 first; do not derive IC50 values from panel percentages |

## 1. Exact BLU exposure ledger

All five rows concern **male Mtm1−/y mice**, reported plasma BLU3797 concentration in **ng/mL**. The article describes terminal or after-final-dose collection. Elapsed hours after the last dose, longitudinal animal identifiers and a reconstructible plasma bioanalytical method are not supplied in these records. Treat these as **reported plasma concentrations, not demonstrated unbound measurements**. If a downstream document calls them “total,” that is an operational interpretation; the released method does not establish the bound/free analytical basis. [B10-S1]

| Regimen described by article/caption | Workbook locator | Released values, ng/mL | Measurement count | Mean; median; range, ng/mL |
|---|---|---|---:|---|
| 25 mg/kg oral once daily; P22 start; ten-day study | `Fig 6A!A3:A8` | 3520, 5430, 6450, 3370, 6030, 5340 | 6 | 5023.3; 5385; 3370–6450 |
| 50 mg/kg oral once daily; P22 start; ten-day study | `Fig 6A!B3:B8` | 6370, 7720, 8320, 7980, 7090, 6380 | 6 | 7310; 7405; 6370–8320 |
| 100 mg/kg oral once daily; P22 start; ten-day study | `Fig 6A!C3:C9` | 5590, 10300, 12400, 11000, 9000, 10900, 8990 | 7 | 9740; 10300; 5590–12400 |
| 75 mg/kg oral; P22-start cohort, caption describes twice daily | `Fig S6B!A3:A5` | 22600, 28400, 21000 | 3 | 24000; 22600; 21000–28400 |
| 75 mg/kg oral; P25-start cohort, caption describes twice daily | `Fig S6B!B3:B6` | 32700, 29200, 26900, 23400 | 4 | 28050; 28050; 23400–32700 |

**Denominator:** 19 Fig. 6A measurements plus 7 Fig. S6B measurements, across five groups. The workbook does not establish 26 unique animals linked to force, survival or other endpoints. No cross-endpoint pairing or inferred independence is added. Means and medians are simple summaries, not fitted PK parameters.

**Regimen discrepancy retained:** `Fig S6A!C2` labels the P22 cohort as five days twice daily followed by three days once daily; the figure caption's description is not a full resolution of that history. This matters when interpreting an after-final-dose snapshot as a trough. [B10-S1]

### Species, matrix and chemical-species boundaries

| Domain | What the inspected evidence identifies | What remains unidentified | Status |
|---|---|---|---|
| Mouse oral formulation | Fresh aqueous 0.5% w/v sodium carboxymethylcellulose plus 1% v/v Tween 80; oral administration | Formulation-specific solubility, absorption and absolute bioavailability | Carried forward; main Methods, pharmacological treatment |
| Mouse plasma | Five groups above; terminal blood collection is described | Hours post-dose, free fraction, validated total/free basis, assay recovery/selectivity and individual linkage | Carried forward; Fig. 6A, S6B and source workbook |
| Mouse skeletal muscle | Muscle tissues collected for functional/pathology assessments | Matched BLU muscle concentration, free fraction, intracellular availability or native occupancy | Not located in the bounded source set |
| Mouse brain, liver and heart | No exact-BLU concentration profile located | Unbound exposure and separation from any tissue-specific liability | Not located in the bounded source set |
| Human plasma or muscle | No exact-BLU human PK or native human-muscle exposure profile located | Translation of binding, uptake, clearance and exposure duration | Not located in the bounded source set |
| Parent/metabolites | The paper labels the measured drug BLU3797 | Identified metabolites, active metabolite potencies, parent/metabolite assay separation and contribution to efficacy | Not located; do not re-label the reported analyte as a metabolite |
| In vitro ADME | No exact-BLU permeability, transporter, microsomal/hepatocyte clearance or plasma-binding values located | Whether oral plasma persistence reflects absorption, binding, clearance or another process | Not located; no class- or scaffold-based substitution |

The article's 24-hour IC50/IC90 coverage statements and FBS-adjusted plot lines remain **author interpretations**. The public snapshots cannot independently establish those time-course claims. An FBS shift does not supply mouse plasma free fraction or human muscle intracellular concentration. The oral formulation likewise does not establish bioavailability. These distinctions were identified in earlier rounds and are preserved here. [B10-S1]

## 2. Keep four pharmacological quantities separate

| Quantity | Exact evidence anchor | Valid interpretation | Invalid transfer |
|---|---|---|---|
| BLU biochemical inhibition | Reported C2β IC50 28 nM; JCI assay at 1 mM ATP; prior construct/reagent and substrate-unit issues remain | Reported potency under that assay description | A native-muscle effective concentration or human dose |
| BLU engineered cellular engagement | Reported C2β NanoBRET 68.2 nM | A distinct engineered-assay result | Muscle occupancy, an unbound threshold, or a complete cellular C2α/VPS34 margin |
| Mouse plasma concentration | The five workbook groups above | Reported plasma observations under their regimens | A validated 24-hour trough, unbound muscle exposure, AUC, half-life or tissue partition coefficient |
| Native unbound target-site exposure | No measured profile located here | An explicitly missing translation input | A number derived by dividing total plasma by a biochemical IC50 |

No new exact-BLU C2α or VPS34 native-cell data were located. The previously recorded VPS34 publication/workbook discrepancy remains unresolved. This sprint does not silently substitute patent47's panel, a vendor claim or a different chemical series for BLU selectivity. [B10-S1; prior Round 5 and Round 8 audits]

## 3. Comparator feasibility: original-figure check

The original patent PDF was inspected, including drawings 1/5–4/5, with the text figure legend and assay descriptions. The patent uses human engineered C2β Δ1–297 with DPK1248–1250→KKT for its biochemical work; its 40 µM ATP conditions differ from the JCI assay. Exact47's reported 56 nM and exact91's 48 nM therefore do not establish greater or lesser potency than BLU's reported 28 nM. [B10-S2]

| Article | Exact source evidence retained | Denominator/context limit | Feasibility decision |
|---|---|---|---|
| **47** | Table 5 at 10 µM: C2α 5%, VPS34 −13%; no C2γ row identified there. HEK293-lysate kinobead profile is a different measurement. | Single-concentration percentages; replicate count not specified in the table. Negative normalized inhibition is retained as reported, not interpreted as activation or converted to zero. | First comparator for qualification. Public evidence still does not demonstrate its native-cell access, muscle activity or PK. |
| **91** | Table 6 at 10 µM: C2α 6%, C2γ 77%, VPS34 31%, class-Iα 59% and class-Iγ 60%, with additional protein-kinase signals. | Same single-point limitation; lysate profiling does not override the functional panel. | Secondary comparator. Its broader panel prevents borrowing 47's cleaner profile. |
| **36 / 40 / 90 / 96** | Figure 4 legend supplies example numbers; drawing labels DC-03-036/-040/-090/-096. Figure 4B specifies GFP-C2β HEK cells, full medium, nominal 1 µM overnight and subsequent two-hour PKN1/2 inhibition; endpoint pS6K. | Two blot sets are labelled first/second, but independent biological N is not unambiguously specified. No quantitative occupancy, intracellular free exposure or exact47 result. | Evidence that selected series members produced a sensitized cellular pathway response; no transfer to 47/91. |
| **Three unnamed 2024 leads** | Conference abstract reports nanomolar C2β activity and a 117-kinase panel excluding C2γ. | No structures or codes, detailed values, concentrations, replicate counts or PK in the abstract. C2γ is excluded from coverage, not demonstrated spared. | Discovery context only; do not create three qualified assets or merge them into numbered patent compounds. |

Figure 4's GFP tag is a **newly extracted model attribute**, not proof of the size or direction of an overexpression artifact. The patent figure also does not establish the host or construct of JCI's separate BLU NanoBRET experiment. Evidence stays with the assay in which it was generated.

## 4. Decision-changing missing inputs

These are finite information requirements, not instructions to perform experiments during this sprint.

| Missing input | Decision it would change | What does not substitute |
|---|---|---|
| Exact-BLU sample times, parent-selective analytical method and a matched total/unbound plasma profile | Whether the published systemic-coverage interpretation is independently supportable | End-of-study snapshot; approximate FBS-adjusted line |
| Measured muscle-accessible exposure with time-aligned native target modulation and useful human-muscle function | Whether BLU is an interpretable first-proof article and whether a negative result tests the target | Nominal medium concentration, cell-pellet total, or fusion-assay potency alone |
| Exact-BLU C2α/VPS34 activity under comparable cellular exposure conditions | Whether apparent benefit can be assigned to a sufficiently separated C2β intervention | Single-point patent47 inhibition or omitted NanoBRET rows |
| Identified circulating/tissue metabolites and their relevant activity, if present | Whether parent BLU explains exposure and effects | Parent scaffold expectations or another inhibitor's metabolism |
| Exact47 identity/content, accessible exposure and target-linked cellular activity | Whether it can provide an interpretable comparator to BLU | DC-coded other examples, HEK293 lysate binding or the unnamed conference leads |
| Matched distribution and tissue-specific functional evidence | Whether a useful systemic exposure window exists | Claims of brain exclusion, liver safety or a clinical margin without measurements |

**Portfolio consequence:** no score increase, no new validated compound and no target-wide rejection. Continue the existing first-proof project; retain its independent article, exposure and native-function qualifications. The next useful public-document trigger is an exact-article disclosure supplying one of these missing inputs. Repeating generic C2β or exhausted model searches would not resolve the identified exposure question.

## Sources, provenance and stopping rule

- **B10-S1 — BLU primary study and released workbook.** [Shearer et al., JCI Insight, DOI 10.1172/jci.insight.198568](https://insight.jci.org/articles/view/198568), Fig. 6A; Supplemental Fig. 6A–B; biochemical/NanoBRET and pharmacological-treatment Methods. [Source-value workbook](https://df6sxcketz7bb.cloudfront.net/manuscripts/198000/198568/jci.insight.198568.sdval.xlsx). Local audited file: `research/source-data/blu3797-source-values.xlsx`, SHA-256 `61b73e018b4c294a7df77eb2dd1f6358035fc20d8073071d693ae5678cae0cb3`. This is the same dataset as prior rounds.
- **B10-S2 — Exact comparator patent.** [WO2025003330A1](https://patents.google.com/patent/WO2025003330A1/en); [original PDF](https://patentimages.storage.googleapis.com/0c/02/82/d70291e8e8f99d/WO2025003330A1.pdf). Figure 4 legend; Example 4 cellular activity; Table 1 (47: printed p.78/physical p.79; 91: printed p.89/physical p.90); Tables 5–6 (printed pp.129–132/physical pp.130–133); Figure 4 drawing 4/5, **physical PDF p.313**. Original cached PDF SHA-256 `4862b6b3d24e135e200ef57c23276c68c9b38ee6f1fb0d8041150f60b316fe23`. Google Patents OCR sometimes renders µM as pM; the values here follow the original-PDF audit, not uncorrected OCR.
- **B10-S3 — New program-level primary abstract.** [New Trends in Chemistry Research 2024, abstract book](https://newtrends-timisoara.ro/2024/docs/Book-of-abstracts-NewChemRes2024.pdf), printed p.23 / physical PDF p.24, Cirillo et al., C2β-inhibitor discovery abstract. Text independently retrieved from the official conference-hosted PDF. No exact-article identity assignment is supplied by this abstract.

**Scope closed:** three primary document groups, with targeted identity/exposure lookups. The patent PDF exceeded the web reader's size limit; its previously cached original was inspected locally. One conference URL failed and its official `/2024/` path succeeded. No continuing access chase, no renewed Kobialka/L463S search and no inferred ADME dataset. Negative search results mean “not located in this bounded source set,” not proof that unpublished or other public data do not exist. Machine-readable values, missing fields and provenance are in `blu-exposure-feasibility.json`.
