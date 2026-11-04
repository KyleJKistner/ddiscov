# Round 10 — two additional exact-use screens

**As of:** 4 November 2026. **Baseline:** `b21aaddd2270b6670a745c2197867316d46b5879`. This is a public-evidence and repository review. No outreach, purchases, experiments, simulations, material acquisition, or Git actions were performed for these screens.

## Decision

Retain both uses as **conditional clinical-research reserves**, with the independent asset theses on hold. Zinc/GNAO1 is the stronger next clinical-evidence question of this pair. Neither screen displaces a current leading priority, establishes an S-tier candidate, or justifies new dedicated allocation; initial diligence fits within the existing five-point discovery allocation. These are analyst judgments, not clinical recommendations.

| Exact use | Useful-function anchor | Main limiting evidence | Current decision |
|---|---|---|---|
| **R10-NL-01: oral taurine / SLC6A6 deficiency** | Cardiac function improved in two related p.Gly399Val patients; a younger sibling retained useful vision. | Mild baseline cardiac dysfunction; no independent cardiac replication; advanced retinal disease did not show restored vision; transport varies by genotype. | Narrow organ/genotype reserve; independent supplementation asset on hold. |
| **R10-NL-02: zinc acetate dihydrate / GNAO1-related disorder** | Prospective pilot measured exploratory motor and daily-function improvements. | No control; blinded movement severity unchanged; exposed and analysis denominators differ; existing academic development program. | First of this pair for a bounded clinical-evidence review; independent asset on hold. |

The source-backed observations behind this table are detailed below. The structured companion preserves exact entities, denominators, source IDs, unresolved fields, and advance/stop conditions.

## Counting and alias audit

The audit covered **all 186 baseline files**: 182 UTF-8 files, three PDFs with text extraction, and one XLSX through its XML text. It included every row of the **622-row cumulative register**. The audit JSON records the corpus digest, term-by-term hits, binary extraction methods, and adjudication.

Taurine already appears in MELAS and cold-platelet work, but SLC6A6 does not appear. GNAO1 has one gene-only hit: `Gnao1` in the BLU3797 source workbook, adjacent to `GNAO_MOUSE` and `ENSMUSG00000031748`. That measurement row does not describe a zinc/GNAO1 intervention use. Neither exact use was found in the candidate register. Count **two new exact-use screens and zero new molecules**.

An abbreviation-only search would also have missed the existing **N-acetylmannosamine/GNE** entry, `historical-topics:T060`. Its full-name alias was recovered and it was excluded from this screen’s new count. That update is handled separately by the parent sprint. Repository novelty is not a patent or global scientific-novelty conclusion.

## R10-NL-01 — oral taurine for SLC6A6 deficiency

### Evidence and biological units

The original report treated two siblings, aged 15 and 6, homozygous for **c.1196G>T, p.Gly399Val**. The tested cells retained approximately 15% transport capacity. Both had **mild** hypokinetic cardiomyopathy and a normal effort test. Fractional shortening increased from 24–27% to 32% after 24 months. This is fractional shortening, not LVEF. The younger sibling’s visual performance improved with stable central retinal anatomy; the older sibling had advanced macular disease without demonstrated visual recovery. The historical regimen was oral taurine, with Burgerstein tablets named in loading-test methods. No contemporaneous control or independent family replication was provided. [R10D-S01](https://pmc.ncbi.nlm.nih.gov/articles/PMC7068170/)

The newer cohort contained **seven affected and ten unaffected people in four families**, not seven treated patients. One explicitly described treated patient had an exon-11 deletion, advanced retinal disease, and essentially unchanged examination/full-field stimulus testing through approximately 17 months despite plasma taurine normalizing. The study also found complete or near-complete transport loss for p.Thr249Ile and p.Ala294Thr in tested cells. Its abstract prints p.Thr113Ter for a fourth family, whereas the sequence-linked main text gives **c.338G>A, p.Trp113Ter**; the discrepancy is preserved. [R10D-S02](https://pmc.ncbi.nlm.nih.gov/articles/PMC12679424/)

The directly extracted treatment ledger therefore contains **three people across two pedigrees**, with the cardiac signal coming from two siblings in one pedigree. A 2023 abstract describes taurine supplementation in two additional brothers, but its official page could not be read. Their genotype, outcome, and overlap with older reports remain unresolved; this is **not a complete global treated census**. Unaffected parents in the original loading test are not disease-outcome replicates. [R10D-S03](https://iovs.arvojournals.org/article.aspx?articleid=2787051)

### What the evidence changes

The cardiac observation is relevant because it follows an existing physiological deficit and measures organ function. Genetic causation, depleted taurine, residual transport, and temporal improvement form a coherent causal story. That raises interest above a generic nutrient hypothesis. It does not establish severe heart-failure recovery, independent replication, or general repair of irreversibly lost tissue.

The important development boundary is **genotype × organ × remaining tissue**. A mass-action explanation is plausible for residual transport, but cannot simply be assigned to a transport-null variant. Likewise, a result in surviving myocardium cannot establish retinal regeneration. Plasma normalization alone does not demonstrate adequate intracellular taurine in either organ. The newer patient’s stable advanced retina is compatible with several explanations, including natural history; it supplies no controlled prevention effect.

Comparator care is incompletely reconstructed. The original cardiac cointervention timeline was not fully recovered, and the two siblings share a genetic and environmental background. Independent useful-function evidence would therefore move the assessment more than additional repeats of the same biochemical rescue.

### Material, contribution, and decision boundary

The published tablets, exact constructs, and patient-cell assays are public leads. Their existence does not establish a currently qualified supply, a transferable model, or a validated clinical exposure plan. No materials were acquired and no assays were performed.

A useful contribution would be a genotype- and stage-specific account of where supplementation changes cardiac or retained visual function, with all treated cases and failures retained. A generic taurine product and an already published treatment idea do not establish a differentiated owned asset. This review did not establish exclusivity or complete a patent/FTO analysis.

**Advance:** independent meaningful organ function beyond plausible care and natural-history effects, in a clearly defined genotype and viable-tissue setting. Asset promotion additionally needs a specific incremental product or evidence contribution.

**Hold or redirect:** no useful function despite adequate exposure in the defined viable-tissue subgroup, or no differentiated contribution. Failure to restore late-stage vision should constrain that ocular claim; it should not be converted into evidence that the cardiac mechanism necessarily fails. First resolve the inaccessible two-brother report before representing a complete treatment census.

## R10-NL-02 — zinc acetate dihydrate for GNAO1-related disorder

### Exact article and denominator ledger

ZINCGNAO1 used **Wilzin zinc acetate dihydrate**, with doses expressed as **elemental zinc**. It was a six-month, single-centre, open-label safety/feasibility pilot. The published flowchart distinguishes the following units. [R10D-S04](https://pubmed.ncbi.nlm.nih.gov/42542632/)

| Unit | Count | Interpretation |
|---|---:|---|
| Screened | 16 | Screening population. |
| Enrolled / full analysis set | 13 | Eleven distinct variants. |
| Started / exposed safety set | 12 | One person refused before any dose. |
| Completed | 11 | One further withdrawal followed an unrelated serious adverse event. |
| Modified full analysis set | 12 | Caption excludes the SAE participant, thus retaining the never-exposed refuser. |
| Exploratory GMFM reference subset | 8 | Ages 2–18 with paired assessments; compared with published cerebral-palsy trajectories. |

Feasibility was 11/13, **84.6%**, not an efficacy-response rate. Exploratory mean GMFM-66 rose 33.1→37.8 and unblinded BFMDRS disability fell 25.5→23.5; nominal P values were .006 and .005. Movement severity, including a blinded BFMDRS movement assessment, did not improve. Exact endpoint paired denominators and imputation were not recovered. The n=8 reference comparison is not a concurrent GNAO1 control. [R10D-S04](https://pubmed.ncbi.nlm.nih.gov/42542632/)

### Earlier case and preclinical boundaries

The earlier p.Gly203Arg patient was **3.4 years old**, distinct from the pilot’s six-month-old p.Gly203Arg infant. Treatment began with zinc gluconate and changed to acetate dihydrate. At follow-up, crises fell from approximately twice daily to weekly, dystonia improved, and GMFM-66 remained unchanged. Hydromorphone was a new cointervention after acute illness in a palliative setting. The abstract’s cessation of *daily* crises does not mean elimination of all crises. The published PDF is preferred to an earlier indexed passage that used a different opioid name. [R10D-S05](https://access.archive-ouverte.unige.ch/access/metadata/b38fa5a4-bb7a-42b9-b110-2ad4a6ce8400/download)

That study profiled 16 variants in three biochemical response classes. Its zinc-sulfate mouse work found some improvements across mutant and wild-type genotypes while hyperactivity remained unchanged. This is not genotype-specific rescue by the exact clinical acetate article. Biochemical response categories remain a stratification hypothesis without demonstrated prediction of clinical benefit. [R10D-S05](https://pubmed.ncbi.nlm.nih.gov/39153472/)

### Why the pilot earns a reserve rather than promotion

Prospective assessment, a named article, explicit safety accounting, and useful-function outcomes improve the research proposition. The main uncertainty has moved from whether clinical assessment is practical toward whether a reproducible treatment effect exceeds maturation, practice, expectation, and background care.

The masked movement-severity null is a material counterweight to improvements in unmasked disability and caregiver outcomes. Multiple exploratory endpoints and nominal P values leave substantial room for chance. Cerebral-palsy trajectories may contextualize change, but cannot stand in for GNAO1 natural history or concurrent controls. Combining the earlier case and pilot into a responder fraction would obscure their different articles, settings, outcomes, and analysis populations.

Disease-specific symptomatic treatment, antiseizure care, rehabilitation, and prior DBS also remain relevant comparators or cointerventions. A development claim must establish added useful function with care documented; nothing here supports interrupting effective care. Treatment of an essential-element deficiency and mutant-protein correction should also be kept conceptually separate when interpreting response.

### Existing development, exposure, and contribution

Wilzin is a marketed **Wilson-disease** product whose current EMA-listed holder is **Recordati Rare Diseases**. Its intestinal copper-lowering action is intended in that indication; it cannot be assumed irrelevant to prolonged use in GNAO1. The official public record also identifies gastric irritation and enzyme elevations. The current detailed product-information PDF could not be retrieved, so this is not a complete label review. [R10D-S06](https://www.ema.europa.eu/en/medicines/human/EPAR/wilzin)

An academic clinical program already exists, involving Cologne and Geneva investigators and patient-organization funding. Its pilot discusses administration burdens and uncertainty about CNS exposure. [R10D-S04](https://pmc.ncbi.nlm.nih.gov/articles/PMC13427569/) Consequently, an independent asset needs a contribution beyond rediscovering zinc. Serum exposure is not proof of CNS target engagement, and elemental-zinc amounts must not be confused with salt mass.

The most valuable incremental contribution is a genotype-aware, controlled useful-function evidence package with transparent treatment exposure, completion, background care, and endpoint denominators. A formulation improvement could be relevant if it solves a documented administration burden; no new or invasive delivery program follows from these data. Current stock, manufacturing access, rights, and exclusivity were not established. No complete patent/FTO review was performed.

**Advance:** durable, clinically meaningful motor or daily-function benefit in a credible controlled comparison, acceptable sustained exposure, and a defined contribution beyond the active program.

**Hold or stop:** no meaningful controlled function despite adequate exposure, unacceptable sustained safety/administration burden, or no differentiation. Heterogeneous unresponsive variants should not be used to declare whole-target failure. Recovering paired endpoint counts and missing-data handling is the first bounded evidence task.

## Retrieval limits and reproducibility

The SLC6A6 primary texts and the earlier zinc published PDF were read. For the 2026 zinc pilot, the accessible evidence comprised its abstract, original figure captions, and indexed primary Table 1/methods/discussion extracts; the complete manuscript and supplement were not retrieved. The official registry yielded a JavaScript shell, so trial registration and design are attributed to the publication, not an independently audited registry history. The ARVO taurine abstract remains metadata-only.

The companion JSON contains seven stable source records, exact article and variant mappings, negative findings, historical-regimen labels, and explicit unresolved fields. The alias JSON contains the reproducible baseline digest and all match paths. These files support **two completed screens**, not a claim that every treated person, negative result, patent, current supply lot, or protocol detail has been recovered.
