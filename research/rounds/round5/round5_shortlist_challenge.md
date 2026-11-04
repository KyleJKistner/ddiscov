# Round 5: independent challengers and local-repair reassessment

Assessment date: **4 November 2026**. This is a research-screening decision record, not an assertion that any intervention is ready for patients or investment.

## Decision

**No new S-tier candidate emerged.** Two new exact uses deserve constrained reserves: pantethine/PPCS cardiomyopathy, because it joins human disease and cardiac-function evidence, and topical gentamicin/nonsense JEB, because it has direct human wound and functional protein evidence. Both have specific, experimentally answerable obstacles. Neither advances on the assumption that a paper title, catalog entry or willing owner makes it developable.

RM4404 remains an independent-validation priority outside the core. APR-246/AEC remains a serious local challenger. Their next decisions are more precise after reviewing chemical identity, timing of functional rescue, comparators and actual patent language.

The screen covers **seven new intervention/use pairs, six new molecular families, one new use of an existing molecule, and two existing-candidate updates**. Gentamicin was already present for SERPINB7/Nagashima disease; the LAMA3/LAMB3-JEB use is new. RM4404 and APR-246 are updates, not two further discoveries. Comparators and related mechanistic papers are not counted as leads.

Deduplication used the published schema-4 inventory at `research/portfolio-register.json`, SHA-256 `0351ff29994bef1a14b63db0c9e990ef53ec00bc506e8d15354f0711b6a0bb65`. Its historical baseline commit is distinct from the round-4 publication commit, `3dd9bf879d0555f60e27de649a9eb4620832ffec`.

## New screens

| ID | Exact intervention/use | Most decision-relevant evidence | Decision |
|---|---|---|---|
| R5-C01 | Pantethine for PPCS-deficiency dilated cardiomyopathy | Two patient cardiac backgrounds; partial functional rescue/stabilization; reagent labeled pantethine but catalog identifies pantetheine | Conditional reserve; identity and exposure before further promotion |
| R5-C02 | Topical 0.5% gentamicin sulfate in petrolatum for susceptible LAMA3/LAMB3 nonsense JEB | Three treated children, nine wounds; cell adhesion/protein function and later wound closure | Human functional reserve; comparator, safety and differentiated product needed |
| R5-C03 | Low-dose oral efavirenz for juvenile/adult NPC1 cognitive dysfunction | Sixteen-person uncontrolled pilot; “100% response” is permissive non-deterioration, not universal improvement | Hold for controlled functional benefit on current care |
| R5-C04 | Artesunate for homozygous LAMB3 R635X severe JEB | One mixed-route, confounded clinical course; no convincing early healing or topical response | Stop current product thesis; retain negative result |
| R5-C05 | RCM-1 for established EoE epithelial barrier loss | Functional resistance measured in an immortalized line during IL-13 co-treatment; delayed mouse pathology arm | Hold for post-deficit patient-model function and exposure |
| R5-C06 | Perampanel for restored daily function in established Lafora disease | Dramatic first case tempered by a ten-person series without significant disability/cognition improvement | Stop restoration thesis; seizure benefit is a separate use |
| R5-C07 | Diacerein 1% / AC-203 for generalized EBS | Two randomized studies missed primary efficacy outcomes; latest 81-person result released October 2026 | Stop neglected-asset pursuit; active sponsor and negative efficacy evidence |

### R5-C01 — Pantethine/PPCS: the strongest new challenger needs chemical reconciliation

The 2025 study combines treated clinical cases with two patient-derived cardiac backgrounds. Its cardiac patches received 500 micromolar reagent on days 7–21; force decline stabilized without a significant force increase, and force-frequency behavior remained abnormal. Other cardiomyocyte measures improved partially. Four treated patients described in this paper include follow-up of earlier cases; standard cardiac interventions complicate clinical attribution. Patch counts are 15/13 untreated/treated for one patient and 9/8 for the other, with eight control patches across two lines. These are **two patient backgrounds**, not dozens of independently treated patients. [P1](https://iris.unibs.it/retrieve/73dc3bf9-28fd-45b1-bcd0-5305f9fa5050/43856_2025_Article_1017.pdf)

The article calls its reagent pantethine and cites **Sigma 16702**. The manufacturer identifies 16702 as **(R)-pantetheine**, a monomeric thiol, rather than pantethine, its disulfide. This does not prove the historical vial was wrong; it makes chemical species, concentration basis and the bridge from cell experiment to oral product unresolved. Redox interconversion does not automatically justify identical molar or exposure assumptions. [P2](https://www.sigmaaldrich.com/US/en/product/sigma/16702)

A historical study in four children with cystinosis found rapid oral pantethine conversion without detectable intact parent in plasma by its assay. Different disease and historical analytical limits prevent a categorical “no exposure” conclusion. They do make an unqualified 100–500 micromolar parent-drug bath a poor substitute for a human exposure argument. The deciding issue is which circulating/metabolized species reaches diseased myocardium and reproduces the phenotype. [P3](https://pmc.ncbi.nlm.nih.gov/articles/PMC424158/)

The public models also require precision. HMGUi003-A is marked not readily obtainable. MRIi028-A is listed for research with commercial/for-profit restrictions. A new, commercially permitted parental iPSC background engineered with PPCS variants is a plausible independent route, but requires disease-model qualification and does not override the patient line's restrictions. [P4](https://hpscreg.eu/cell-line/HMGUi003-A) [P5](https://hpscreg.eu/cell-line/MRIi028-A)

**Deciding proof:** authenticate the relevant chemical species, establish a plausible exposure range, and demonstrate improved force/fatigue after a qualified, predictable deficit in independent PPCS backgrounds. Include genetic correction, precursor/metabolite controls and arrhythmia monitoring. If the result only slows decline, stop the full-reversal claim and assess a separate useful-preservation hypothesis. Infeasible exposure or an unresolved active chemical identity stops advancement of the exact product until resolved. The case could support a small disease-focused qualification effort; an addressable patient population and differentiated commercial product have not been established.

An additional infant report, DOI 10.1002/ehf2.15283, is under root's independent clinical/overlap review. It is deliberately not counted here as a separate independent patient or ignored as nonexistent. [P7](https://academic.oup.com/eschf/article/12/4/3195/8488057)

### R5-C02 — Topical gentamicin/JEB: direct function, incomplete product thesis

The topical primary study used **0.5% gentamicin sulfate in white petrolatum** for two weeks on selected wounds of three children with susceptible LAMA3/LAMB3 nonsense variants. Its patient keratinocytes showed functional laminin-332; wound closure and protein findings persisted to later assessments. Nine wounds are nested within three patients. These open-label comparisons support biological activity but cannot fully separate readthrough from wound care or antibacterial effects. [G1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7210719/)

A separate five-child intravenous series provides additional human evidence, but it is a different exposure/product and possible participant overlap has not been excluded. It must not become “eight independent topical responders.” Short-course absence of observed renal, auditory or antibody toxicity does not establish repeated treatment over large skin areas. [G2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8892363/)

**Deciding proof:** durable adhesion/barrier improvement compared with matched vehicle, optimized care and an antimicrobial-active control lacking the desired readthrough mechanism; measure systemic exposure. Public engineered readthrough models provide an initial independent route. [G3](https://pmc.ncbi.nlm.nih.gov/articles/PMC6048497/) A standardized pulse regimen or formulation must add measurable safety or efficacy beyond known gentamicin use to become a compelling new development asset.

### R5-C03 — Efavirenz/NPC: audit the response definition and the 2026 comparator

Sixteen participants completed a 52-week open-label, miglustat-background pilot. Its 100% response criterion meant avoiding threshold-defined deterioration in at least two of three cognitive domains. Continuous cognitive results were mixed; ataxia/disability were stable. Response-derived favorable and unfavorable clusters are not independently validated predictors. This is a meaningful human signal, but it is weaker than universal cognitive restoration. [E1](https://sms.carm.es/ricsmur/bitstream/handle/123456789/25242/10.1016j.neurot.2025.e00706.pdf?sequence=1)

Current US care includes levacetylleucine and arimoclomol with miglustat; the paper's historical framing of miglustat as the sole registered treatment cannot determine the current comparator. A randomized levacetylleucine study provides a functional benchmark that the efavirenz narrative must address. [E2](https://www.fda.gov/news-events/press-announcements/fda-approves-new-drug-treat-niemann-pick-disease-type-c) [E3](https://www.fda.gov/news-events/press-announcements/fda-approves-first-treatment-niemann-pick-disease-type-c) [E4](https://pubmed.ncbi.nlm.nih.gov/38294974/)

**Deciding proof:** controlled add-on improvement in a prespecified cognition, swallowing or daily-function outcome, with measured exposure. A small target-engagement experiment in another disorder does not establish NPC efficacy; high-exposure ataxia in HIV treatment is a reason to measure exposure, not proof that low-dose NPC treatment is harmful. [E5](https://pmc.ncbi.nlm.nih.gov/articles/PMC9797897/) [E6](https://pmc.ncbi.nlm.nih.gov/articles/PMC5532735/)

### R5-C04 — Artesunate/JEB: preserve the negative case

The one-child report used sequential systemic and topical routes. Early healing was absent, skin laminin changes were marginal, and topical treatment did not improve the flanks. Later buttock improvement coincided with amnion transplantation. The child died; this alone does not establish drug toxicity. The cell figure's p=0.053 also warrants more restraint than the abstract's positive wording. [A1](https://zenodo.org/records/17812353)

The present product does not compete with the gentamicin evidence. Reopening requires a defined new exposure/formulation proposition and independent functional benefit; changing route repeatedly or emphasizing a confounded late wound does not resolve the result.

### R5-C05 — RCM-1/EoE: functional assay, wrong timing for restoration

The key electrical-resistance experiment used **EPC2-hTERT**, an immortalized human epithelial line, with IL-13 and RCM-1 administered together. Culture observations are not independent EoE patients. Patient tissue/organoids support the biology, and the mouse work includes treatment after disease establishment, but neither converts the human co-treatment resistance assay into demonstrated reversal of established patient barrier failure. [R1](https://pmc.ncbi.nlm.nih.gov/articles/PMC13151461/)

Public RCM-1 identity is available through the manufacturer. [R2](https://www.selleckchem.com/msds/MSDS_S6898.pdf) The next proof should start only after stable barrier loss in independent patient-derived cultures, measure permeability and regenerative capacity, and compare an active pathway treatment at feasible local exposure. A compound that only suppresses insult induction or inhibits healthy repair should stop.

### R5-C06 — Perampanel/Lafora: do not let one striking case dominate the series

The original case described regained walking and communication. The later ten-person open-label series found some seizure/myoclonus benefit but no significant disability or cognition improvement; three discontinued for ineffectiveness or adverse effects. This does not deny symptomatic value. It does lower the probability of a broadly restorative product consistent with this portfolio's objective. [L1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5691360/) [L2](https://pmc.ncbi.nlm.nih.gov/articles/PMC4307869/)

Reopening requires independent daily-function recovery beyond seizure suppression and a differentiated development proposition. A known clinical molecule does not solve the efficacy-fit problem.

### R5-C07 — Diacerein/EBS: a new primary-result check changes the screen

The earlier 54-person randomized study failed to establish its primary and key secondary benefit over vehicle. [D1](https://pubmed.ncbi.nlm.nih.gov/37276163/) A fresh check found that the sponsor released the **81-participant EBShield result on 18 October 2026**: primary IGA p=0.426; BSA, EBDASI and QOLEB were also not significant. Pain and itching favored treatment. The open-label extension does not substitute for the randomized result. [D2](https://www.twibiotech.com/en/news/content/twi_biotechnology_announces_primary_endpoint_results_from_phase_2_3_trial_of_ac_203_in_epidermolysis_bullosa_simplex?category=Press)

The sponsor's 30 October update continues development and describes subgroup analyses and regulatory plans. These are active external development, not an abandoned asset. Subgroup signals may generate a future hypothesis; they do not establish a prespecified restorative effect. [D3](https://www.twibiotech.com/en/news/content/twi_biotechnology_announces_ac_203_clinical_trial_results_and_future_regulatory_strategy_at_investor_conference)

## Existing candidate updates

### R5-C-U01 / R4-L01 — RM4404

**New chemical correction:** the paper's Sigma/Calbiochem 317700 is currently described as **WAY-262611 hydrochloride**; Cayman 17704 is the **free base**. The same active moiety is not an automatically equivalent micellar drug product. Salt, concentration basis, final solvent, loading and released/free drug should be specified analytically before replication. [RM2](https://www.merckmillipore.com/INTL/en/product/Dkk-1-Inhibitor-WAY-262611-HCl-Calbiochem,EMD_BIO-317700) [RM3](https://www.caymanchem.com/product/17704/way-262611)

The original WAY-262611 discovery uses functional Wnt/TCF signaling in a DKK1 context. The reviewed evidence did not establish a binding constant or corneal cell-specific target occupancy. Therefore, a chemical repair phenotype alone should not be labeled exclusive Schwann-cell DKK1 causality. [RM4](https://pubmed.ncbi.nlm.nih.gov/19856966/)

The institution publicly lists a 2025 US provisional titled **Compositions and Methods for Corneal Nerve Regeneration via DKK1 Inhibition**, and describes a patent-pending topical formulation. The search did not locate the application number or claims. The exact rights boundary and licensing availability remain unknown; an owner response is not required to do the independent scientific proof. [RM5](https://facultydirectory.uchc.edu/profile?profileId=Bargagna-Mohan-Paola) [RM6](https://today.uconn.edu/2026/06/targeting-schwann-cells-a-new-approach-to-repairing-corneal-injury/)

Cenegermin is a meaningful comparator. Its labeled randomized studies demonstrated epithelial healing; mean sensitivity changes were not clinically significant. An early-stage open-label study reports sensory improvement, so the claim must not become “existing therapy cannot restore sensation.” Population and endpoint matching matter. [RM7](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=89e4bfec-d710-40ed-8885-5d13ba46b1cd) [RM8](https://pmc.ncbi.nlm.nih.gov/articles/PMC10787719/)

The prior round's denominators and corrections remain: some analyses use paired-eye observations; randomization and blinded secondary imaging review were reported; the primary sensory assessor's masking is unclear; calendar time after dosing is not measured washout; significance against healthy tissue does not establish drug-versus-vehicle superiority. [RM1](https://onlinelibrary.wiley.com/doi/full/10.1002/jnr.70142)

**Go:** independently replicate delayed sensation with characterized formulation, matched solvent, animal-level analysis, masked sensory assessment, appropriate active comparator, optical/epithelial integrity and pain discrimination. **Stop:** solvent/salt correction erases the effect, the signal is sensitization rather than useful sensation, or benefit relies on healthy-reference normalization.

### R5-C-U02 / R4-L02 — APR-246/AEC

The original evidence still comprises two children and their associated cellular work. The cell experiment began before calcium-induced differentiation; key cornification markers remained unrescued. Clinical coverage therefore cannot be equated with mature barrier restoration. Biopsies came from nonerosive arm sites that healed normally, sharpening the need for an actual lesion-context model. The reported 0.6mg/g cream plus literal 5mg active/day implies 8.33g cream/day if interpreted literally: a dose-transfer ambiguity that requires specification, not a presumed proven error. [APR1](https://www.nature.com/articles/s41419-020-2223-8)

The exact molecule is **PRIMA-1MET/APR-246**, catalog3710, rather than PRIMA-1. A public reagent route is identifiable. [APR2](https://www.rndsystems.com/products/prima-1met_3710) Its thiol/redox pharmacology creates a concrete mechanism/exposure question; cancer-cell glutathione or oxidoreductase effects cannot directly establish skin toxicity or exclusive mutant-p63 restoration. [APR3](https://pubmed.ncbi.nlm.nih.gov/26086967/) [APR4](https://pmc.ncbi.nlm.nih.gov/articles/PMC6107631/)

**Actual US claim nuance:** claim1 of US12521392B2 requires AEC, PRIMA-1MET and ectodermal dysplasia affecting at least one cornea. Dependent skin/cream claims retain the corneal-disease predicate. That does not mean administration must only be to the cornea, and does not clear skin treatment of AEC patients who have corneal involvement. Nor does it justify describing all skin uses as categorically blocked. The European published application proposes broader claims; published scope is not confirmed granted scope. [APR5](https://patents.google.com/patent/US12521392B2/en) [APR6](https://patents.google.com/patent/EP3823622A1/en)

A later three-line JEB paper reports partial adhesion rescue, with overlapping investigators. It adds phenotype context but is not independent AEC clinical replication and is not an eighth new lead here. [APR7](https://www.sciencedirect.com/science/article/pii/S0022202X23025861)

**Go:** defined topical exposure restores permeability and mechanical resilience after established deficit, persists after withdrawal and spares healthy repair. **Stop:** surface coverage without mature resilience, only differentiation pretreatment activity, or an inadequate redox/safety window.

## How this changes the next work allocation

1. Complete BLU3797's existing independent challenge before promoting a replacement on less complete evidence.
2. Keep RM4404's formulation/sensory proof and APR-246's mature-barrier proof alive as explicit local-function alternatives.
3. Use a tightly bounded identity/exposure/model qualification for pantethine/PPCS before more clinical optimism.
4. Develop topical gentamicin/JEB only around a demonstrably better product or validated response strategy.
5. Retain the three clear negative/poor-fit screens, especially the newly disclosed diacerein randomized miss, to prevent rediscovery by positive abstracts.
6. Treat efavirenz and RCM-1 as evidence gaps with concrete tests, rather than asking owners whether something is “available.”

The companion JSON contains exact evidence units, remaining uncertainties, go/stop criteria and the complete source index. No outreach, procurement, experiments or remote writes were performed by this challenger agent.


## Integrated follow-up

The [independent clinical/function challenge](ppcs-clinical-function-challenge.md) verifies a separate infant PPCS case, retains spontaneous recovery and concurrent-care confounding in the larger series, and distinguishes useful preservation from reversal. The [chemistry and exposure challenge](round5_pantethine_chemistry_challenge.md) further evaluates the actual species and exposure bridge. These refinements govern interpretation of R5-C01.
