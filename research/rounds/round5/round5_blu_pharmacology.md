# Round 5 — BLU3797 identity, pharmacology, exposure and comparator audit

**Evidence cut: 4 November 2026.** Research only. No outreach, procurement, experiments or remote repository writes. This extends the round-4 source audit; the integrated human-proof review covers efficacy-cohort reconstruction and human muscle-model qualification. The companion JSON preserves exact values, units, source-cell ranges, distinctions between measured and inferred findings, and a source registry.

## Decision

**Keep BLU3797 as a strong, defined tool for a staged PIK3C2B proof. The public evidence does not yet establish an exposure window for selective, sustained inhibition in human muscle, or qualify BLU3797 itself as a development candidate.** The new work sharpens that conclusion rather than treating missing measurements as failed measurements.

The most consequential additions are:

1. The finite published **PIK3C3 NanoBRET IC50 of 14,366 nM is not supported by the released dose-response cells**, which contain only zeros. This is an unresolved source-data reconciliation, not evidence of a newly discovered toxic off-target.
2. The biochemical **28 nM IC50 was measured with a reported final enzyme concentration of 60 nM**. Its proximity to half the enzyme concentration raises a tight-binding/ligand-depletion qualification. It is not a free Ki and may be near the assay's quantitative floor.
3. The released PK consists of **end-of-study or after-final-dose plasma measurements**, without recorded hours after dosing or a demonstrated unbound concentration. It cannot independently reconstruct a 24-hour trough, free-muscle exposure, half-life, oral bioavailability or brain separation.
4. A separate public **2025 inhibitor patent** supplies exact comparator structures and assays. **Compound 47 deserves priority over compound 91** for independent comparator qualification, because the underlying functional selectivity tables are materially different. Neither has publicly demonstrated XLMTM functional rescue in the material inspected.

These are concrete diligence improvements. They do not justify discarding the mouse activity or promoting the asset to S-tier.

## 1. Exact test article and material bridge

BLU3797 is the published **S stereoisomer of N-(5-(2-(1-cyclopropylethyl)-7-(cyclopropylmethoxy)-1-oxoisoindolin-5-yl)-4-methylthiazol-2-yl)acetamide**. The primary structure, named synthesis and nominal LCMS ion agree. The journal reports `[M+H]+ = 426` and a proton-NMR peak list. Probechem's listing independently identifies the same named structure, formula **C23H27N3O3S**, and molecular weight **425.55 g/mol**. The vendor supplies no CAS identifier on the inspected page. Its >98% HPLC claim is a catalog statement, not a demonstrated lot certificate or independent analytical release. [PH-S01, PH-S04]

The neutral structure is specified; the final isolated solid's counterion/solvate, absolute assay content, enantiomeric purity, residual-metal profile and stability are not established by the inspected public package. BLU2720's reported **93.5% purity belongs to BLU2720**, and must not be inherited by BLU3797. The latter's journal synthesis does not state a numerical final purity. [PH-S01]

### Public route: substantially defined, still requiring reconciliation

The journal gives two final transformations from **(S)-5-bromo-2-(1-cyclopropylethyl)-7-fluoroisoindolin-1-one**, replacing the fluorine substituent and installing the acetamidomethylthiazole-bearing aryl bond. The same named S intermediate is disclosed upstream in two unrelated PI3K patent programs: US20240226104A1 and CN119490502A. The Chinese disclosure identifies it as **A-1-1c**, with nominal LCMS 298, after three upstream stages. This is a credible public reconstruction route; it is stronger than an unspecified requirement to obtain proprietary material. It is not evidence that an independent batch has been made successfully. [PH-S01, PH-S05, PH-S06]

There is also a small but real material-accounting issue in the journal's final BLU3797 step. It reports **21.7 mg product from 0.114 mmol starting intermediate, at 38% yield**. Assuming the named neutral molecule, 425.55 g/mol, and no content correction, those numbers imply approximately **44.7%**. The discrepancy could reflect an omitted purity/form correction or a transcription issue. It does not identify the cause, and no corrected yield or salt is substituted here. The upstream US disclosure also contains quantity/stoichiometry inconsistencies already identified in round 4. These are reasons to reconcile a material specification, not proof that synthesis is impossible. [PH-S01, PH-S04, PH-S05]

**Material decision:** retain the exact S structure and analytical criteria as the unit of work. A catalog name, a route, an available starting material and permission to commercialize are separate questions. No supplier contact is required to establish that distinction.

## 2. Potency and selectivity: what the numbers mean

### Published pharmacology and its source support

All cellular concentrations below are the assay's nominal compound concentrations. The paper does not provide a measured free intracellular concentration. The NanoBRET Methods describe NanoLuc fusion expression, tracer displacement and manufacturer instructions, but do not identify the host cell line or give the in-house tracer's identity, concentration, affinity, serum conditions and equilibrium validation. Do not label this as native human-muscle target engagement. [PH-S01]

| Article | Assay / target | Published result | Released source support | Interpretation |
|---|---|---:|---|---|
| BLU3797 | Human PIK3C2B ADP-Glo | IC50 28 nM | `Fig 1B!A3:A12`, `F3:H12`; three value columns | Potent inhibition under the stated conditions; enzyme-concentration qualification below |
| BLU2720 | Human PIK3C2B ADP-Glo | IC50 1.0 µM | `Fig 1B!A3:A12`, `C3:D12`; two value columns | Weaker active analog, not an inactive control |
| BLU3797 | PIK3C2B NanoBRET | IC50 68.2 nM | `Table 1!A6:A15`, `B6:E15`; four value columns, duplicated in Fig 1C | Cellular engagement evidence; replicate independence is not specified |
| BLU3797 | PIK3CA NanoBRET | IC50 20,000 nM | `Table 1!A16:A25`, `F16:I25` | Value is at the maximum tested concentration; not a well-resolved finite constant |
| BLU3797 | PIK3C3 / VPS34 NanoBRET | IC50 14,366 nM | `Table 1!J16:K25` and `Fig 1C!J13:K22` are all zero | Finite published IC50 cannot be reconstructed from the released values |
| BLU3797 | PIK3CG NanoBRET | IC50 7,233 nM | `Table 1!AD6:AI15`, dose block `N6:N15` | Published value retained; right-side dose units are not labeled in the workbook |
| BLU3797 | PIK3CD NanoBRET | IC50 12,364 nM | `Table 1!W6:AB15`, dose block `N6:N15` | Same unit/fit qualification |
| BLU3797 | PIK3C2G NanoBRET | IC50 6,759 nM | `Table 1!P6:U15`, dose block `N6:N15` | Nearest listed numerical off-target, approximately 99 times the reported C2B IC50 |
| BLU3797 | KINOMEscan binding panel | S(10) = 0.015 at 3 µM | Figure 1E and Methods; no Fig 1E sheet or target-level table in released workbook | A single-concentration binding summary, not a functional safety window |

The value-column counts are **not assumed to be numbers of independent biological experiments**. Table 1's right-side raw dose block is retained without fitting or relabeling its unit. The original workbook remains unchanged. [PH-S02, PH-S03]

### New reconciliation issue: PIK3C3

The workbook has **twenty literal zero values** for BLU3797's PIK3C3 response across nominal concentrations from **20,000 to 0.076294 nM** in its explicitly labeled left-side dose block. The duplicate Fig 1C sheet agrees, and the plotted green curve is flat at zero. A finite IC50 of 14,366 nM cannot be estimated from those released measurements. Possible explanations include a table error, a different unreported assay dataset, or a source-file error. None is established. [PH-S02, PH-S03]

This does **not** establish that BLU3797 potently inhibits VPS34. Nor is it valid to replace 14,366 with a precise new value or an independently proven selectivity margin. The correct entry is **published 14,366 nM; source-data reconciliation unresolved**. An independent reviewer checked the same cells and figure.

For PIK3CA, the four values at 20 µM are 41.32195, 39.1307, 52.4 and 40.2% inhibition, with a descriptive mean of **43.263%**. The stated 20,000 nM is consequently at the test ceiling, with no clearly resolved upper plateau. Treating every 20,000 nM entry as a precisely measured affinity overstates the assay. [PH-S02, PH-S03]

### New qualification: 28 nM is close to the biochemical assay floor

The published final reaction contains **60 nM human PIK3C2B, 1 mM ATP and 150 nM diC8 phosphatidylinositol**, following a ten-minute compound/enzyme/ATP preincubation. The paper uses a four-parameter logistic fit and BGT-226 as the full-inhibition control. The lipid unit is reproduced exactly; no silent µM correction is made. The catalytic reaction duration and active-enzyme fraction are not specified in the inspected method. [PH-S01]

With a nominal enzyme concentration of 60 nM, an IC50 of 28 nM is near the **30 nM half-enzyme concentration**. Official assay guidance explains why ligand depletion/tight binding can make an IC50 near this regime depend on enzyme concentration. Active enzyme could differ from nominal protein, and the reported method could contain a unit error; neither is resolved here. This is a **qualification of quantitative interpretation**, not a finding of false inhibition. The true underlying affinity could be stronger than the apparent IC50. It matters especially for comparing potent analogs and for translating biochemical values to occupancy. No Ki is calculated. [PH-S07, PH-S08]

### What remains incomplete

The cellular panel still omits **PIK3C2A** and **class-I PIK3CB**. A small KINOMEscan S(10) does not substitute for those cellular comparisons. The binding panel was run at 3 µM and reports a thresholded score; a score alone cannot identify all weaker interactions or their functional relevance under sustained exposure. [PH-S01–03]

NanoBRET is useful precisely because cell permeability, ATP and local binding can change engagement relative to cell-free assays. Its quantitative interpretation also depends on tracer occupancy and assay conditions. The missing in-house tracer details prevent a direct, fully specified transfer of the published 68.2 nM value. A public **NanoLuc-PIK3C2B fusion vector, Addgene 238834**, provides a defined component but not a complete transferred assay. [PH-S09–11]

## 3. Exposure audit: a complete table of the released PK values

Figure 6A's image is explicitly titled **End of study PK**. Supplemental Figure 6B is titled **PK after last dose**. Both axes use **ng/mL plasma concentration**. Neither the source sheet nor the inspected Methods specifies the hours after dosing or whether the reported bioanalysis represents total or unbound drug. These should be described as **reported plasma concentrations, not demonstrated free concentrations**. Assuming ordinary total-plasma handling may be reasonable operationally, but it remains an assumption. [PH-S01–03]

| Actual article | Species / disease / matrix | Regimen as reported | Sampling information available | Raw values, ng/mL | n values | Mean / median / range, ng/mL | Source cells |
|---|---|---|---|---|---:|---|---|
| BLU3797 | Male mouse, Mtm1−/y, plasma | 25 mg/kg oral QD from P22 | End of 10-day study; hours after dose absent | 3520, 5430, 6450, 3370, 6030, 5340 | 6 | 5023.3 / 5385 / 3370–6450 | `Fig 6A!A3:A8` |
| BLU3797 | Same | 50 mg/kg oral QD from P22 | Same | 6370, 7720, 8320, 7980, 7090, 6380 | 6 | 7310 / 7405 / 6370–8320 | `Fig 6A!B3:B8` |
| BLU3797 | Same | 100 mg/kg oral QD from P22 | Same | 5590, 10300, 12400, 11000, 9000, 10900, 8990 | 7 | 9740 / 10300 / 5590–12400 | `Fig 6A!C3:C9` |
| BLU3797 | Same, P22-start group | 75 mg/kg BID in caption; dosing-history discrepancy inherited from round 4 | After final dose; hours after dose absent | 22600, 28400, 21000 | 3 | 24000 / 22600 / 21000–28400 | `Fig S6B!A3:A5` |
| BLU3797 | Same, P25-start group | 75 mg/kg BID | After final dose; hours after dose absent | 32700, 29200, 26900, 23400 | 4 | 28050 / 28050 / 23400–32700 | `Fig S6B!B3:B6` |

Counts are counts of released measurements. Individual animal IDs, matching across efficacy/PK endpoints and PK-specific biological denominators are not provided. No inferential comparison between the age groups is made. The previously identified P22 schedule mismatch—`Fig S6A!C2` says BID×5 and QD×3 while the caption says five days BID—remains unresolved and must stay attached to that group. [PH-S03, round 4 audit]

### What the exposure evidence supports

It supports **oral delivery producing measurable mouse plasma exposure** under an explicitly disclosed carboxymethylcellulose/Tween80 vehicle and dosing scheme. Together with dose-responsive in-vivo efficacy, it supports continuing the exact compound as a preclinical tool. It does not measure the fraction of an oral dose reaching systemic circulation; therefore “orally bioavailable” in the article must not be expanded into a numerical bioavailability claim. [PH-S01]

The paper states that once-daily dosing could furnish a 24-hour Ctrough at the target IC50, and that 75 mg/kg BID was chosen to achieve an IC90 trough. Those are **author-reported exposure interpretations**. The released PK values do not independently demonstrate either time course.

### The FBS correction does not close the free-exposure bridge

The figures overlay FBS-corrected NanoBRET IC50/IC90 dashed lines, graphically around **3,000 and 30,000 ng/mL**. These are approximate visual readings, not exact newly extracted constants. The source workbook does not contain numerical threshold values, serum-shift measurements or a correction formula. The inspected Methods do not disclose mouse-plasma protein binding, blood/plasma partitioning or muscle/brain unbound distribution. [PH-S01–03]

Consequently, this review does **not** infer a 1% unbound fraction from the plotted shift; does not convert nominal assay potency into a measured free-plasma threshold; and does not equate plasma concentration with intracellular muscle exposure. Nor does it derive half-life, clearance, AUC, Cmax, Kp, Kp,uu, a human dose, or an exposure-linked neural margin from these snapshots.

The measured plasma ranges are compatible with a useful mouse exposure profile. They are also compatible with several different binding/distribution/time-course scenarios. The public dataset does not distinguish those scenarios. That uncertainty is the remaining development question.

## 4. ADME and successor routes: unresolved parameters, not invented liabilities

No independently measured BLU3797 human/mouse hepatocyte or microsomal clearance, metabolite identification, CYP inhibition/induction, transporter effects, plasma stability, aqueous solubility, permeability/efflux, unbound plasma/muscle/brain fraction, or chronic exposure-linked safety package was located in the inspected primary materials and current exact-code searches. This is **absence of a located public measurement**, not proof the sponsor never measured it.

The structure contains an ether and other potential metabolic sites, but those features alone do not establish the major metabolite, clearance pathway, reactive-metabolite liability or brain penetration. A suspension vehicle does not prove poor human oral delivery. A high mouse mg/kg dose does not by itself establish an unacceptable human dose. Conversely, short-term survival of treated WT mice is not a chronic developmental, hepatic or neural safety margin.

There are three defensible routes, each with a distinct decision unit:

| Route | What it can presently claim | Deciding requirement |
|---|---|---|
| Exact BLU3797 | Defined structure; mouse pharmacology and functional activity; feasible public route to material | Reconciled analytical article, qualified engagement/selectivity, and useful human-muscle function linked to measured exposure and relevant-tissue distribution; equal culture concentrations alone do not establish a systemic window |
| A peripheral or muscle-favoring PIK3C2B successor | A rational product hypothesis informed by neural target risk | Measured muscle exposure/engagement with adequate brain separation; cannot inherit BLU efficacy or claim peripheral restriction from a drawing |
| Distinct-scaffold comparator or alternative target article | A way to test whether benefit survives a chemistry change | Exact-article cellular selectivity and target-dependent function before any development ranking |

The biology workstream's heterozygous-versus-homozygous kinase-dead findings argue against assuming that any modest PIK3C2B reduction will restore force. Its epilepsy evidence is a susceptibility signal from genetic perturbation and provocation models, not demonstrated BLU3797 toxicity or a numerical occupancy cutoff. The useful design problem is therefore **how much muscle inhibition is required and what exposure separation is achievable**, rather than assigning an arbitrary “safe” percent inhibition.

## 5. New public comparator series: WO2025003330A1

The **Forschungsverbund Berlin** disclosure, priority 30 June 2023 and published 2 January 2025, names Cirillo, Lo, Haucke and Nazaré. Its original 319-page PDF was inspected at the structure table, assay Methods, functional selectivity tables, claim drawings and kinobead figure. The text extraction repeatedly turns **µM into pM**; the PDF confirms **micromolar**, not picomolar, units. [PH-S12]

### Exact examples and assay boundaries

| Exact article | Public identity / result | What is independent and useful | What must not be imported |
|---|---|---|---|
| Compound47 | N-(5-(1-((2,3-dichlorophenyl)sulfonyl)-1,2,3,4-tetrahydroquinolin-6-yl)-4-methylthiazol-2-yl)acetamide; C2β IC50 56 nM, class-Iγ >10,000 nM | Different core from BLU; disclosed chemistry; functional Table 5 and HEK293-lysate kinobead profiling | No published XLMTM force rescue, unbound PK or same-compound live-cell pS6K result established here |
| Compound91 | N-(5-(1-((2,3-dihydrobenzo[b][1,4]dioxin-6-yl)sulfonyl)-1,2,3,4-tetrahydroquinolin-6-yl)-4-methylthiazol-2-yl)acetamide; C2β IC50 48 nM, class-Iγ >10,000 nM in Table 1 | Exact article and lysate profiling are public | Its Table 6 shows substantial functional inhibition of several other kinases at 10 µM; cannot be described as universally clean |
| DC-03-036, -040, -090, -096 | Four other numbered compounds, 1 µM overnight in HEK cells, followed by two hours of PKN1/2 inhibition | A disclosed sensitized pS6K cellular readout | Cellular evidence belongs to these four compounds; it is not live-cell evidence for 47 or 91 |

The biochemical assay uses engineered human **PI3KC2β Δ1–297, DPK1248–1250→KKT**, **10 ng/µL enzyme, 40 µM ATP and 200 µM phosphatidylinositol**. Reported ATP Km is 63.7 µM. These conditions differ substantially from BLU's 1 mM-ATP assay and enzyme preparation. The reported 56/48 nM values cannot be used to declare either compound more or less potent than BLU. Replicate counts for individual inhibitor IC50s and functional panel entries are not clearly specified; the triplicate statement applies to enzyme/ATP characterization. [PH-S12, printed pp124,133–134]

### Read the functional table before accepting “only target hit”

At **10 µM compound 47**, Table 5 reports C2α 5%, class-Iα/p85α 24%, class-Iβ/p85α 14%, VPS34 −13%, and class-Iγ 14% and22% in two listed rows. Negative assay-normalized percentages are retained. A C2γ row was not found in that table. This is a useful, incomplete profile. [PH-S12, printed pp129–131]

At **10 µM compound 91**, Table 6 reports **C2γ 77%, class-Iα/p85α 59%, class-Iγ 60%, VPS34 31%, CLK2 62%, PI4Kβ 53%, p38α 50% and Aurora B 48%**. Other low-inhibition entries include C2α 6% and class-Iβ/p85α 2%. These results do not eliminate 91 as a compound, but they prevent treating its selectivity as interchangeable with 47. Assay ATP concentrations vary by target, as recorded in the original table. [PH-S12, printed pp131–132]

The patent's assertion of no hit except C2β refers to **HEK293 lysate kinobead competition** with a hit criterion of apparent IC50<10 µM. That assay neither proves cell entry nor establishes absence of functional off-targets. Figure 5 actually marks C2γ as a biochemical-only target. Its figure is not separately labeled for each example, another reason not to assign all properties to every compound. [PH-S12, printed pp123,125,133; drawing 5/5]

**Comparator decision:** compound 47 is a defined public chemistry/assay candidate for qualification. It is not yet an independently validated orthogonal probe or a replacement development lead. It shares the acetamidothiazole motif with BLU, so “different core” is more accurate than “wholly unrelated chemistry.” Compound91 is secondary because its functional panel is less clean. Preserve the exact-number mapping.

### Other orthogonal tools

The earlier blanket caution about PITCOINs needs precision. **PITCOIN2** inhibits C2β at a reported 1.5 µM while also inhibiting C2α; it partially corrected surface active β1-integrin in MTM1-KO myoblasts in the 2022 PNAS study. A C2α-selective **PITCOIN3** comparison and genetic loss strengthen interpretation of that cell phenotype. PITCOIN2 alone remains unsuitable as a clean C2β-selective control, and the result is not muscle force. [PH-S13]

PI-701/PI-702 are legacy C2β-focused tools with limited class-II/kinome selectivity characterization. The 2023 medicinal-chemistry study explicitly identifies these coverage limits. They should not be elevated to clean orthogonal controls merely because an earlier paper calls them isoform-selective. Genetic catalytic perturbations and a newly qualified exact compound 47 would be more informative than swapping among incompletely profiled commercial names. [PH-S14]

## 6. Public ownership, claims and program status

| Disclosure / program | What was verified | Boundary |
|---|---|---|
| BLU3797 paper | Blueprint authors and funding; company described as a Sanofi subsidiary | Publication does not grant commercial rights or prove the program was abandoned |
| US20240226104A1 / WO2022226052A1 | University of Michigan applicant shown; matching upstream intermediate; compound/composition and nanoparticle claims | Route disclosure is not a BLU-specific clearance opinion; broad formula claims were not exhaustively charted |
| CN119490502A | Matching A-1-1c intermediate; named Chinese applicant; pending displayed | English text is machine translated; same intermediate is not proof of identical final-asset ownership |
| WO2025003330A1 | Actual Formula 1 use claim and broad chemical claim drawings inspected; exact47/91 examples | Claim scope is broader than the title's example scaffold. No definitive mapping of BLU into or outside the genus is asserted |
| EP4734987A1 / CN121816181A | 2026 national publications; both displayed as pending; Forschungsverbund Berlin applicant | PCT entry's “ceased” label does not establish a rights-free family. Official EPO register retrieval returned 403; displayed statuses remain aggregator observations |

The new patent shares relevant chemical motifs and explicitly claims class-II PI3K uses including myotubular myopathy for its defined compounds. It therefore belongs in the bounded landscape for a comparator or successor. This review neither finds infringement nor grants freedom to operate. Public reconstruction, medicinal-chemistry differentiation, patentability and commercial freedom must remain separate entries. [PH-S05–06, PH-S12, PH-S15–16]

Sanofi's official release confirms the Blueprint acquisition completed 18 July 2025. The inspected current Blueprint core-programs page lists avapritinib, elenestinib and BLU-808; absence of BLU3797 from that page does not prove termination or licensing availability. [PH-S17–18]

A direct ClinicalTrials.gov API query on 4 November 2026 for **BLU3797 OR BLU-3797** returned **zero studies**. Adding PIK3C2B returned one unrelated observational obstetric biomarker study, NCT07695467, not a PIK3C2B-inhibitor trial. These bounded searches did not locate a named clinical BLU program. They do not exclude an unpublished or differently coded program. [PH-S19–20]

## 7. What this changes in the screen

The strongest reason to continue is the combination of an exact public article, cellular engagement, mouse activity, genetic catalytic support and a now-broader independent comparator route. The strongest reason to avoid S-tier promotion is the unclosed bridge between **qualified useful human-muscle function and a measured selective exposure window**.

The next decision can be stated without making an email the scientific gate:

- **Continue exact BLU** if authenticated material and qualified engagement produce useful post-deficit human muscle function at concentrations separable from relevant injury.
- **Continue the target with a different article** if catalytic genetic perturbation and a properly qualified comparator support benefit while BLU fails on its own chemistry or distribution.
- **Reduce target priority** if verified target engagement fails to deliver function in a qualified disease model with a demonstrated post-deficit functional positive control, or measured relevant-tissue exposure shows no separation between useful muscle inhibition and injury. Prior genetic correction alone does not establish delayed modifiability. Equal-concentration culture overlap alone leaves the in-vivo distribution question unresolved. See the [integrated human proof](blu3797-human-proof.md).
- **Do not overinterpret an unqualified negative** when tracer transfer, article identity, intracellular exposure or model rescuability is unresolved.

The new source-data inconsistencies are neither erased nor counted as a failed therapeutic experiment. The report distinguishes an actual unfavorable measurement (compound 91's broader functional inhibition), an unresolved source reconciliation (BLU–PIK3C3 IC50), and a missing translational measurement (free muscle/brain exposure).

## Primary source registry

- **PH-S01:** [Shearer et al., JCI Insight 2026, doi 10.1172/jci.insight.198568](https://insight.jci.org/articles/view/198568). Methods, Table 1, Figures1/6, disclosure and dosing sections.
- **PH-S02:** [Publisher supporting data workbook](https://df6sxcketz7bb.cloudfront.net/manuscripts/198000/198568/jci.insight.198568.sdval.xlsx). Archived unchanged at `research/source-data/blu3797-source-values.xlsx`; SHA256 `61b73e018b4c294a7df77eb2dd1f6358035fc20d8073071d693ae5678cae0cb3`.
- **PH-S03:** [BLU supplement](https://insight.jci.org/articles/view/198568/sd/pdf/render/1), PDF p8, Supplemental Figure 6. Also [published Table 1](https://insight.jci.org/articles/view/198568/table/1) and [Figure 6](https://insight.jci.org/articles/view/198568/figure/6) visually checked.
- **PH-S04:** [Probechem BLU3797 PC-26519](https://www.probechem.com/products_BLU3797.html). Primary vendor listing; identity/purity/quote assertions retain vendor status.
- **PH-S05:** [US20240226104A1](https://patents.google.com/patent/US20240226104A1/en). Public patent text, matching intermediate synthesis, claims and displayed applicant.
- **PH-S06:** [CN119490502A](https://patents.google.com/patent/CN119490502A/en). Key intermediate A-1, steps1–3; translated text.
- **PH-S07:** [NCATS Assay Guidance Manual: Basics of Enzymatic Assays for HTS](https://www.ncbi.nlm.nih.gov/books/NBK92007/?report=printable). IC50 assay floor and curve interpretation.
- **PH-S08:** [Assay Guidance Manual: Mechanism of Action Assays for Enzymes](https://ncbi.nlm.nih.gov/sites/books/NBK92001/). Tight-binding/ligand-depletion interpretation.
- **PH-S09:** [Vasta et al., quantitative live-cell kinase profiling](https://pmc.ncbi.nlm.nih.gov/articles/PMC5814754/). Primary NanoBRET methodology.
- **PH-S10:** [Promega NanoBRET TE intracellular kinase assays](https://www.promega.com/products/cell-signaling/kinase-target-engagement/nanobret-te-intracellular-kinase-assay/?catNum=NF1200). Manufacturer documentation on tracer calibration.
- **PH-S11:** [Addgene 238834, NanoLuc-PIK3C2B](https://www.addgene.org/238834/). Primary construct catalog.
- **PH-S12:** [WO2025003330A1](https://patents.google.com/patent/WO2025003330A1/en), [original PDF](https://patentimages.storage.googleapis.com/0c/02/82/d70291e8e8f99d/WO2025003330A1.pdf). Table 1 printed pp78/89; Methodspp124–125 and133–134; Tables5–6 pp129–132; claims beginp293; drawing 5/5. PDF page index is printed page+1 for the numbered description/claim section.
- **PH-S13:** [Samsó et al., PNAS 2022, doi 10.1073/pnas.2202236119](https://pnas.org/doi/full/10.1073/pnas.2202236119). PITCOIN2/PITCOIN3 and MTM1 integrin phenotype.
- **PH-S14:** [Kücükdisli et al., J Med Chem 2023, doi 10.1021/acs.jmedchem.3c01319](https://pubs.acs.org/doi/abs/10.1021/acs.jmedchem.3c01319). Primary medicinal chemistry and explicit limits of older tools.
- **PH-S15:** [EP4734987A1](https://patents.google.com/patent/EP4734987A1/en). Displayed national-stage applicant/status; official register attempt was blocked.
- **PH-S16:** [CN121816181A](https://patents.google.com/patent/CN121816181A/en). Displayed national-stage applicant/status.
- **PH-S17:** [Sanofi acquisition completion,18 July 2025](https://www.sanofi.com/en/media-room/press-releases/2025/2025-07-18-05-00-00-3117709).
- **PH-S18:** [Blueprint current core programs](https://www.blueprintmedicines.com/pipeline/core-programs/).
- **PH-S19:** [ClinicalTrials.gov exact-code API query](https://clinicaltrials.gov/api/v2/studies?query.term=BLU3797+OR+BLU-3797&countTotal=true&format=json). Direct retrieval 4 November 2026: zero records.
- **PH-S20:** [ClinicalTrials.gov code/target API query](https://clinicaltrials.gov/api/v2/studies?query.term=BLU3797+OR+BLU-3797+OR+PIK3C2B&countTotal=true&format=json), and returned [NCT07695467](https://clinicaltrials.gov/study/NCT07695467). One unrelated observational biomarker record.
