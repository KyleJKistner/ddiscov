# Independent challenge: fluoxetine for KCNC1 gain of function

**Round8 | 4 November 2026. Decision: retain as a bounded clinical-proof reserve; no S-tier or proprietary-asset promotion.** The evidence is interesting enough to improve a genotype-specific research plan. It does not yet provide a reliable functional effect size, an exposure-to-channel bridge or a differentiated commercial product.

## 1. The strongest clinical observation remains uncertain

The 2026 primary study follows **one p.V434L/c.1300G>C child**, using fixed placebo–fluoxetine–placebo order with randomized/masked transition times. Powdered fluoxetine2.5 then5mg was mixed with cornstarch, encapsulated and sprinkled on yogurt. The primary caregiver EMQ estimate is **+6.61 points, 95%CrI−0.53 to14.78**; baseline change is +0.52/week and time×treatment−0.20 (−0.65 to0.22). Its clinically meaningful threshold is unvalidated. Purposeful-hand-movement secondary ratings narrowly exclude zero; other modeled endpoints do not. Increased EEG excitation, no clinical seizures, and possible six-week withdrawal irritability are distinct observations. [F01]

The attached source-table extractor verifies the seven published outcome rows and preserves every time, treatment and interaction interval. This is a **one-participant model-summary audit**, not seven independent efficacy tests or a patient-data reanalysis. No posterior probability is reconstructed from rounded intervals.

**Inference:** a credible interval crossing zero is neither proof of no effect nor a sufficiently precise success estimate. The level-effect estimate divided by the developmental slope is descriptively about12.7weeks; calling that proven developmental acceleration would conflate a level shift with a slope change. The interaction does not establish faster continued development. A new proof should predeclare the functional target and uncertainty rule and preserve observed skill acquisition separately from caregiver rating changes. Trial feasibility has value even when efficacy remains unresolved.

The completed public registry **NCT06341127** reports actual enrollment1 and no posted results module at the current retrieval. The published report is therefore the efficacy source; the registry is not a second cohort. Its masking classification and narrative differ in granularity: fixed sequence was known, while transitions were masked. [F02]

## 2. Genotype and mechanism cannot be pooled indiscriminately

The 2023 prior report concerns **p.V425M**, a different child and a phenotype including epilepsy. Transient CHO expression showed predominantly gain-of-function channel behavior; fluoxetine blocked both WT and mutant currents. It is uncontrolled clinical support, not a blinded replication of V434L developmental benefit. [F03]

**Inference:** preserve allele, functional classification, disease manifestation and endpoint as separate strata. A KCNC1 loss-of-function positive-modulator program is not a like-for-like comparator to a gain-of-function inhibitory hypothesis. The name of a channel-modulator class alone also does not establish its direction in a particular mutant: channel-state behavior can change the apparent drug action. Neither KCNC2 nor KCNT1 clinical observations should inflate the KCNC1 denominator.

## 3. Newly identified exact-V434L exposure gap

An investigator-generated **Metrion/KCNC1 Foundation/Perlara2024 poster** reports a fluoxetine **IC50 of12.3µM** in CHO-K1 V434L thallium-flux spiked-plate validation. It is a heterologous channel assay, not a patient-neuron concentration or clinical target-engagement measurement. The 6,718-compound library screen and its 46plate quality metrics are screening denominators, not patient outcomes. The source is a poster, with no independent clinical validation of its concentration estimate. [F04]

**Inference:** the proposed direct-channel explanation needs a quantitative bridge. It is insufficient to compare the oral dose, total plasma, total brain accumulation and an in-vitro nominal IC50 as though they were interchangeable. Both fluoxetine and active metabolite exposure, relevant free concentration and neuronal functional response matter. The retrieved clinical record does not provide that bridge. The EEG shift cannot substitute for selective Kv3.1 engagement, and its clinical direction requires separate judgment.

This does not prove the prescribed research dose could not work; an IC50 is not a required minimum clinical concentration, and partial modulation or another mechanism could matter. It prevents claiming that the clinical observation has already validated target engagement.

## 4. A more informative chemical comparator, with important liabilities

The 2026 primary **VU0521426/VU426** study (PMID42141755; DOI10.1152/ajpcell.00239.2026) reports state-dependent channel inactivation. Automated patch-clamp steady-state-current IC50 values are **WT4.228µM and V434L0.7885µM**, with three other GoF variants also tested. These are assay-dependent cell-current measurements. VU426 inhibits Kv1.1/Kv2.1/Kv3.2/Kv3.3 with overlapping potency; low concentrations can also shift activation in the hyperpolarizing direction. The authors frame it as a mechanistic probe and medicinal-chemistry starting point. [F05]

**Inference:** VU426 is a useful comparison for mechanism and state dependence, not an established clinical rival, an available exclusive asset or a superior drug. Its in-vitro potency should not be divided directly by the fluoxetine thallium-flux potency to advertise a clinical superiority ratio. The need for subtype selectivity, neuronal efficacy and exposure/tolerability remains. I recommend recording it inside the fluoxetine target/comparator assessment, without counting it as a seventh independently validated lead.

## 5. Incremental value and next bounded decision

The most credible near-term value is a genotype-qualified clinical evidence program that resolves useful function and mechanism under a reproducible formulation. Generic familiarity is an execution advantage, while it leaves a substantial value-capture question: a new developer needs evidence, delivery, formulation or another advantage that existing clinical use does not already supply. The present observations do not establish that advantage.

A later research tranche should have one declared primary functional outcome, a prespecified clinically useful target calibrated for this population, blinded assessment where feasible, explicit withdrawal/carryover handling and an exposure/mechanism substudy. Multiple weekly observations improve measurement of one child's trajectory; additional independently assessed participants and genotype strata are needed for generality. These are design requirements for a proposed future program, not instructions to treat, contact or recruit anyone now.

**Portfolio consequence:** retain this lead below the leading BLU qualification allocation. Its immediate evidence challenge is efficacy/interpretability and target exposure, not an assumption that an owner must answer an email. A chemistry program built around VU426 would be a separate, earlier-stage project and should not inherit the fluoxetine patient's observations.

## Sources and audit record

- **F01:** Jha et al., [An n-of-1 gene-directed drug repurposing trial for an ultrarare genetic condition](https://pmc.ncbi.nlm.nih.gov/articles/PMC13360919/), DOI10.1002/epi.70253, PMID41999155; primary full XML and Tables1–4 inspected. the [extractor](../../../methods/fluoxetine_endpoint_audit.py) and [saved audit](fluoxetine_endpoint_audit.json) extracts Table3 without reconstructing raw patient data.
- **F02:** [ClinicalTrials.gov NCT06341127](https://clinicaltrials.gov/study/NCT06341127), current public JSON supplied in the discovery workstream, version holder2026-11-04, `hasResults:false`. No contact made.
- **F03:** Ambrosino et al., [Epilepsia2023 DOI10.1111/epi.17656](https://onlinelibrary.wiley.com/doi/10.1111/epi.17656), [PMID37203213](https://pubmed.ncbi.nlm.nih.gov/37203213/); primary abstract/indexed methods reviewed. No invented patient PK or merged-cohort estimate.
- **F04:** Maidment et al., [Metrion2024 V434L primary poster](https://www.metrionbiosciences.com/wp-content/uploads/2024/06/KCNC1_SLAS-Europe-2024_poster_final.pdf); original PDF downloaded and text inspected. SHA256`64d9118219b6c27ef3882a3dbc528942627a743c194d20bcb866206b05615b13`. Figure5 places the fluoxetine estimate in the thallium-flux validation context. The repeated2024/2025 presentations are not independent biological replications.
- **F05:** [VU0521426 primary2026 paper](https://journals.physiology.org/doi/full/10.1152/ajpcell.00239.2026), [PMID42141755](https://pubmed.ncbi.nlm.nih.gov/42141755/), [PMC13270922](https://pmc.ncbi.nlm.nih.gov/articles/PMC13270922/). Primary indexed results/methods inspected; direct PMC had verification wall and EuropePMC XML returned500. No claims of raw-data reanalysis, PK or human response.

No purchased material, outreach, experiment, patient recommendation or new treatment action occurred.
