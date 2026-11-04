# Exact 8015-P2: what the released off-target panel measures

**Review date: 4 November 2026.** This is a source interpretation update to an existing candidate, with no new candidate or experiment counted.

## Decision

Keep the preliminary profiling evidence, but replace the unqualified phrase “59% MAO-A inhibition” with **59% MAO-A radioligand binding displacement at 10 µM**. The panel does not establish a uniform greater-than-10,000-fold selectivity ratio or a clinical safety margin.

The original [publisher supplement](https://www.mdpi.com/article/10.3390/ijms27167376/s1) was retrieved through its ordinary public download route. It contains an axon-size figure and a three-page off-target table. It contains no animal-level efficacy dataset. The [derived audit](p2-off-target-audit.json) preserves 87 numeric assay entries, assay sections, page locations, archive identity and the boundaries of the calculation.

## Findings

The table uses one nominal 10 µM concentration. Of 87 assay rows, 75 are classified as binding assays and 12 as enzyme/cell assays. Only the MAO-A row exceeds 50%. These are assay rows, not necessarily distinct proteins: several entries concern different binding sites or isoforms. A second reviewer independently confirmed the counts and the critical assay identities.

| Source entry | Reported percentage | What was measured | Interpretation boundary |
|---|---:|---|---|
| MAO-A | 59 | Antagonist-radioligand binding, clorgyline reference | A binding interaction worth characterizing; no catalytic rate or concentration-response curve is supplied. |
| MAO-B | −5 | Recombinant enzyme assay | A different isoform and assay. It cannot supply the missing MAO-A functional result. |
| hERG | −14 | Dofetilide binding | Does not demonstrate absence of functional potassium-current inhibition. |
| 5-HT2B | 42 | Agonist-radioligand binding | The ligand's label does not establish that P2 is an agonist. |

Negative normalized percentages are retained. They do not establish protective activity or target activation.

The supplement compares 10 µM with an approximately 0.8 nM fusion EC50; the main article elsewhere reports approximately 0.6 nM. Dividing the former numbers yields 12,500, an arithmetic ratio of nominal concentrations from different assays. It supplies no off-target affinity estimate, free-concentration comparison or functional tissue margin. The thresholded panel remains useful early evidence, but a large numerical ratio does not close those missing measurements. [Primary paper](https://www.mdpi.com/1422-0067/27/16/7376), DOI 10.3390/ijms27167376, and its Supplemental Table S1.

## How this changes the proof

An independent P2 program should relate the concentration that restores useful nerve-muscle function to functional counterassays at the exposures those tissues actually receive. Characterize a binding signal if it approaches the achieved exposure; do not infer a clinical adverse effect from a single screening point. Conversely, a negative binding point cannot stand in for an electrical-function assay.

The current human-function gate remains: authenticate the exact stereochemical article, qualify a disease-dependent functional deficit and delayed modifiability, and measure useful recovery with genotype and exposure retained. The panel cannot rescue a negative functional result or substitute for a qualified model. It also supplies no reason, by itself, to discard the animal efficacy signal.

## Provenance and retrieval correction

The earlier PMC download attempt returned challenge HTML. The publisher route subsequently returned the actual ZIP, 390,445 bytes, SHA-256 `5fb7c6c29196145afde0b42900d0a9a302fc6e87454a1b0838f2bbe276047b85`. Both retrieval facts are retained; a blocked mirror is not absence of public evidence. The recovered material still does not permit reanalysis of animal-level efficacy.

The current register and this note clarify the historical assay wording. The earlier round-3 memo remains a dated review, with the correction linked from the current assessment. No new biological experiment or new selectivity curve was generated.
