# Round 5 — BLU3797 target biology, reversibility and therapeutic-window audit

**Evidence cut: 4 November 2026. Scope: public-source scientific diligence.** This extends the round-4 BLU3797 audit; it does not report new experiments, obtained materials, outreach or freedom to operate. The exact-compound pharmacology and human-model procurement reviews are separate workstreams. Evidence identifiers correspond to `round5_blu_biology.json`.

## Decision

**Retain BLU3797 as a priority for a tightly bounded development proof. Do not promote it to S-tier.** The PIK3C2B target hypothesis is stronger than the available case for this particular molecule. Several different interventions support a reversible component of MTM1-deficient muscle disease. None establishes an adequate exposure window for exact BLU3797 in mature human muscle, brain and MTM1-deficient liver together.

The most useful change from round 4 is a sharper separation of three questions:

1. **Can the target compensate for MTM1 loss?** Substantial mouse evidence supports this.
2. **Can exact BLU3797 restore useful function after a deficit is established?** Encouraging animal evidence; human force and exposure-linked replication remain open.
3. **Can it do so with tolerable effects in other tissues?** Unresolved. A CNS susceptibility signal and disease-specific hepatobiliary vulnerability make this a central development question.

The source record now supports a specific experiment thesis, rather than a broad assertion that the compound is ready for development. No numerical probability of clinical success is justified by these studies.

### Material changes from round 4

- **Newly integrated catalytic-loss model:** the 2025 endogenous MTM1-C375S knock-in study helps reconcile earlier phosphatase-dead rescue experiments. Catalytic loss can produce substantial disease despite retained protein; noncatalytic functions can still modify severity. [B05]
- **More precise temporal evidence:** the 2016 inducible genetic rescue is post-onset but juvenile; an independent acute isolated-fiber experiment supports a rapidly reversible physiological component without establishing C2β-specific or exact-BLU efficacy. [B01, B06]
- **A stronger comparator:** AZD8055 has within-MTM1 mouse specific-force evidence, including a clearly labelled five-week-start arm. Its methods, cohort labels and known human hepatic liability prevent an automatic ranking upgrade. [B09, B17, B18]
- **New disease-context safety evidence:** the 2026 diet-sensitized mouse liver study and October 2026 large-animal retrospective make the limitations of healthy-animal safety reassurance more concrete. Neither demonstrates BLU toxicity. [B14, B15]
- **A dated competitive benchmark:** the primary VALOR registry describes an active ASP2957 program. This is an investigational alternative with restrictive eligibility, not a proven competitor outcome. [B20, B21]

## 1. Causal evidence matrix

“Direct” below means the reported experiment tests the stated link. It does not imply clinical validation. Related publications and overlapping investigators are not counted as independent replications merely because they have different DOIs.

| Evidence unit | Intervention, setting and observation | What this establishes | Boundary that matters |
|---|---|---|---|
| **B01 — 2016 genetic rescue** | Muscle-specific Pik3c2b deletion prevents the Mtm1-null phenotype. A separate tamoxifen-inducible Cre experiment begins at P21 or P30. The P30 survival group has seven animals; four contribute the P100 grip comparison. | PIK3C2B reduction can compensate after symptoms appear. | The temporal Cre design should not be called muscle-restricted. P30 is juvenile, not years of established human disease. The P28 deficit comparison comes from an earlier figure, not a demonstrated paired baseline for every rescued animal. TAM-treated Mtm1 controls were included. [B01] |
| **B02 — 2023 kinase-dead alleles** | Protein-retaining Pik3c2b-D1212A homozygosity rescues Mtm1-null muscle force. Heterozygosity improves survival/hanging but does not rescue TA/GAS atrophy or TA force. | Catalytic inhibition, without deleting the whole PIK3C2B protein, is a credible therapeutic mechanism. | Partial phenotypic improvement is not interchangeable with force recovery. Allele dosage cannot be converted into a pharmacological occupancy percentage. BIN1-CNM was not rescued. [B02] |
| **B03 — exact BLU3797** | Published mouse survival/motor benefit is dose-dependent; treatment withdrawal and delayed-start experiments add pharmacological evidence. | The molecule has an in-vivo efficacy signal beyond a biochemical assay. | Retain round-4 concerns about ceiling-limited hanging, small delayed-start cohorts and source-workbook provenance. Genetic TA-force results must not be relabelled as exact-BLU force evidence. [B03; round-4 audit] |
| **B04 — phosphatase-dead protein delivery** | Local AAV expression of MTM1-C375S in young Mtm1-null muscle improves specific force and several structural abnormalities without normalizing total PI3P. | Some disease consequences can be improved while bulk lipid concentration remains abnormal. | Local protein delivery is not endogenous replacement throughout life. It does not establish that catalytic function is dispensable or that a bulk PI3P assay predicts all functional benefit. [B04] |
| **B05 — endogenous catalytic loss** | Male C375S knock-in mice retain MTM1 protein but have elevated muscle PI3P, progressive weakness and median survival of 12 weeks. Absolute TA force is markedly reduced; the specific-force comparison is variable and nonsignificant. | A catalytic defect alone is sufficient for substantial disease in this model. | Comparisons of severity with historical null strains are not a matched head-to-head experiment. Protein abundance/localization does not prove preservation of every scaffold interaction. No BLU rescue of this genotype was shown. [B05] |
| **B06 — acute fiber physiology** | Broad PI3K inhibition improves sarcoplasmic-reticulum calcium release after one hour in isolated Mtm1-deficient fibers; reduced CaV1.1 current remains. | At least part of the physiological deficit can respond without prolonged myogenesis or structural replacement. | The inhibitors are not C2β-specific; fiber counts are not donor counts. Calcium release is an intermediate endpoint, not human force or respiratory recovery. [B06] |
| **B07/B08 — trafficking mechanisms** | Genetic C2β loss and pharmacology support restoration of active surface integrin; separate work links C2β depletion to EEA1-associated PI3P and Rab4 recycling. PITCOIN2/PITCOIN3 comparisons help distinguish C2β involvement from C2α-only inhibition. | A trafficking mechanism connects the phosphoinositide imbalance to cell behavior. | These are cell-level effects. PITCOIN2 has mixed isoform pharmacology. Endosomal rescue does not establish a mature human contractile effect. [B07, B08] |
| **B09 — lysosomal mechanism / comparator** | Lysosomal lipid and Rag–mTOR experiments implicate a second compartment. AZD8055 improves survival and TA specific force; Extended Data 10 identifies a five-week-start force arm, n=6/group. | mTOR-linked physiology supplies an orthogonal within-disease functional comparator. | No randomization or blinding; dead mice excluded from endpoint analyses. Main-figure cohort labels and treatment-duration wording require caution. No BLU superiority follows from cross-study results. [B09] |
| **B22 — human isogenic cells** | Healthy/MTM1-knockout and patient/corrected iPSC pairs show abnormal lysosomal distribution and mTOR signaling. | The pathway has human cellular relevance. | This paper is principally a myogenesis study. The abstract's rapamycin differentiation rescue is in mouse myoblast models. It is not an exact-BLU mature-human-force result. Detailed line/genotype and access qualification are handled by the human-model workstream. [B22] |

### How the phosphatase-dead results fit together

The strongest supported interpretation is **multiple, interacting MTM1 functions**, not a choice between “lipid biology is causal” and “lipid biology is irrelevant.” B04 shows that a non-native intervention can improve selected consequences without correcting the bulk lipid measurement. B05 shows that retaining endogenous protein without its catalytic function does not prevent disease. The latter paper proposes substrate binding and intervention timing as possible explanations for the earlier rescue; these remain explanations, not experimentally settled facts. [B04, B05]

For development, this means a compound should be judged by target engagement **and** useful output. Normalized total PI3P alone is insufficient. Failure to normalize every MTM1-associated marker is also insufficient to reject a compound that restores useful function safely. Both mistakes would distort this screen.

## 2. Timing, genotype and sex boundaries

### Prevention, rescue and chronic maintenance are distinct claims

The cumulative evidence contains more than prevention. Inducible genetics, acute fiber physiology and delayed pharmacology all justify testing established dysfunction. It still leaves an important gap between juvenile mouse rescue and reversal of a stable deficit in mature human tissue. [B01, B03, B06]

A mature-function assay must document a deficit before drug exposure and characterize the untreated trajectory over the same interval. Perfectly flat force is unnecessary: a predictable maturation trajectory can be handled with contemporaneous controls and baseline-adjusted longitudinal analysis. Improved differentiation, cell number or survival still require separate interpretation. Absolute force, force normalized to viable contractile tissue, fatigue and relaxation answer different questions and should be retained separately. A calcium transient is a useful mechanistic companion but does not substitute for mechanical output.

The mTOR work also warns against assuming a single direction of benefit at every developmental stage. Treatment at differentiation day five improved the studied cellular phenotype, whereas treatment at day two did not. That observation is not evidence that all late treatment fails. [B09]

### Genotype breadth remains a hypothesis

The strong genetic rescue is concentrated in Mtm1-null male mice. A patient missense label does not by itself identify retained protein, retained enzyme activity or a distinct disease mechanism. The first human panel should therefore classify actual MTM1 abundance/activity and include a null-like and a protein-retaining pathogenic background where feasible. C375S is an engineered mechanistic model, not an established clinical responder population. [B01, B02, B05]

Failure in one well-qualified genotype should narrow the intended population before it is generalized to the target. Conversely, a response in one donor or one corrected pair cannot establish coverage of all MTM1 variants. A cataloged p.L463S line is a model route, not evidence that this variant responds to BLU.

Female carriers cannot be treated as uniformly unaffected. A primary deeply phenotyped cohort included severe, moderate, mild and nonmanifesting carriers; X-inactivation did not fully explain variation. [B19] The current male animal package therefore establishes neither efficacy nor lack of efficacy in symptomatic females. Any later female model should verify allelic expression and stability of its disease phenotype; sex and genotype should be recorded independently.

### Compensation is a testable alternative explanation

Germline genetic perturbation allows adaptation. The protein-retaining kinase-dead study still provides valuable evidence because it narrows the mechanism, but a lifelong allele and a reversible inhibitor need not have identical consequences. Importantly, rescued double-mutant muscle can retain elevated DNM2, while PI3P and mTOR readouts change. DNM2 normalization should therefore not be made a mandatory surrogate of PIK3C2B success. [B02]

Use temporal target modulation and a chemically distinct intervention to ask whether functional benefit follows contemporary C2β engagement. A result confined to development or requiring an unmeasured compensatory state would weaken the chronic small-molecule thesis without disproving all target biology.

## 3. Tissue-specific liability matrix

| Tissue / evidence status | Public observation | Implication for exact BLU3797 |
|---|---|---|
| **Brain: target-related susceptibility signal** | Human heterozygous PIK3C2B variants and mouse KO/HET or G1501fs*1 models support impaired PI(3,4)P2 signaling, mTOR activation and hyperexcitability. Human penetrance is incomplete; mouse behavioral seizures were provoked. [B10] | Establish free brain exposure relative to a neuronal functional adverse-effect range. Do not equate lifelong deletion with adult reversible drug exposure, or call BLU neurotoxic from these data. A peripherally restricted article would be attractive if muscle exposure is preserved. |
| **Liver: disease-context vulnerability** | Mtm1-deficient zebrafish lose canalicular architecture/transport; liver-specific MTM1 restoration and dynamin inhibition partly improve it. [B13] | Effective muscle exposure must preserve canalicular function in an MTM1-deficient liver context. Healthy-cell viability or an isolated ALT observation does not qualify this gate. No PIK3C2B-mediated liver rescue is established by B13. |
| **Liver: new model evidence** | In 2026 mouse work, diet sensitization reveals cholestatic abnormalities; liver-specific deletion supports a liver-autonomous component. AAV8 increases injury in this setting; LNP-MTM1 prevents selected pathology. [B14] | Include a biologically justified challenge condition when qualifying the safety model. This evidence concerns an AAV/environment/disease interaction; it does not identify a BLU adverse effect. |
| **Systemic catalytic loss: reassuring but bounded** | Healthy D1212A mice have enhanced insulin sensitivity and protection from diet-associated steatosis. [B11] | Retain this favorable evidence. It cannot establish safety in MTM1-deficient canalicular disease or exclude neural effects that were not the principal study question. Monitor metabolic physiology as a separate response. |
| **Immune cells: secondary mechanism alert** | PIK3C2B silencing in human CD4 cells impairs KCa3.1/Ca2+ signaling associated with activation. [B12] | A functional immune check becomes relevant if systemic free exposure overlaps sustained C2β inhibition. This is a cellular hazard hypothesis, not demonstrated clinical immunosuppression by BLU. |

There is a particularly important direction-of-effect problem: reducing excess PI3P in diseased muscle and reducing PI(3,4)P2 in healthy neurons can have different consequences for mTOR. [B02, B10] A single blood pS6 measurement cannot establish that the intended muscle compartment is corrected and all other tissues are safe. This is a reason to measure tissue exposure and function, not a reason to assume that systemic development is impossible.

The October 29, 2026 large-animal report documents generally reassuring AAV8 studies in infant monkeys and XLMTM dogs despite subsequent fatal human cholestatic events. [B15] Its relevance is the **failure of a particular preclinical safety prediction**. Applying its toxicity directly to BLU would be as unjustified as using its animal reassurance to clear BLU.

## 4. Competing mechanisms and current programs

| Comparator | What it contributes | What it does not establish |
|---|---|---|
| **MTM1 correction** | Isogenic genetic correction is the most useful assay-rescue control because it tests whether the disease deficit is modifiable in the chosen system. [B22] | It does not identify a druggable exposure window or prove that every downstream surrogate is necessary. |
| **DNM2 reduction** | A different MTM1-compensating mechanism; existing portfolio work preserves exact mouse-article distinctions. The human DYN101 experience demonstrates that target rationale can coexist with inadequate article tolerability. [B16; prior rounds] | The hepatic/hematological tolerability problem cannot be assigned exclusively to DNM2 biology or generalized to every modality from this trial alone. |
| **AZD8055 / mTOR inhibition** | A concrete within-disease pharmacological force comparator. Use its published functional arm to set a higher standard than morphology alone. [B09] | It is a dual mTORC1/2 inhibitor, not a selective mTORC1 experiment. In the 49-treated adult oncology trial, investigator-related ALT/AST increases were each reported in 22%, and transaminase rises were dose-limiting. This is not an obvious chronic pediatric repurposing winner. [B17, B18] |
| **PIKfyve, Rag/LAMTOR and lysosomal trafficking modulation** | Mechanistic probes can distinguish which compartment mediates rescue. [B09, B22] | Partial cellular correction is insufficient for a new development lead. The published PIKfyve/C2β combination did not show additive benefit; a combination pitch is not supported by pathway proximity alone. [B09] |
| **ASP2957 / VALOR** | The primary registry, retrieved 2026-11-04, lists recruiting phase 1/2, estimated enrollment nine, actual start 2025-12-15, update posted 2026-09-03. Enrollment is male, ≤36 months and heavily ventilator dependent; previous cholestatic disease is excluded. [B20, B21] | No posted results were present in the retrieved record. Eligibility exclusions are not evidence that BLU is safe or effective in excluded patients. A possible older-patient or liver-vulnerable niche must be proved. |

### Comparator methods audit

B09 was inspected as a full publisher PDF, including figures, Extended Data 10 and methods. It reports nonrandomized, unblinded experiments, no a-priori power calculation, and omission from endpoint analyses of mice dying before treatment completion. This creates survivor-selection and observer risks. The methods/Figure 7B specify a 20-day regimen; Figure 7H's caption says 30 days. Main Figure 7 also mixes 2W/5W labels across blots and legends. Therefore use the clearly labelled Extended Data 10 late-start force arm, avoid a precise early-versus-late effect-size claim, and require replication before ranking the comparator above BLU. [B09]

A bounded search of the key article identifiers with correction/erratum/retraction terms found no formal corrective notice that resolves these questions. The Brain article's routine “corrected and typeset” history is not evidence of a later scientific corrigendum. Absence from this search is not a guarantee that no notice exists.

## 5. Falsifiable target-product hypothesis

> An authenticated, selective, reversible PIK3C2B inhibitor can improve sustained contractile output after a reproducible deficit develops in human MTM1-deficient muscle, across more than one relevant genetic background, at free exposures that preserve neuronal network and hepatobiliary transport function. The initial product hypothesis is symptomatic disease compensation during treatment; permanent correction, all-genotype coverage and hepatic rescue are not prerequisites or current claims.

This hypothesis belongs to the target class. BLU3797 earns continuation only by meeting the article-specific portion of it. The following are proposed decision rules, not completed results or clinical dose recommendations.

| Gate | Advance condition | Stop or redirect condition |
|---|---|---|
| **A. Qualify the disease model** | A reproducible pre-treatment functional deficit, interpretable vehicle trajectory, and genetic disease dependence; adequate dynamic range and independent differentiation batches. Demonstrate post-deficit modifiability separately from prevention by a corrected line. | No interpretable or modifiable functional deficit: reject the assay for this rescue question. Do not reject the target from this failure. |
| **B. Demonstrate post-deficit article benefit** | Exact BLU improves predeclared sustained force and fatigue/relaxation measures in at least two patient genetic backgrounds. The lower confidence bound must exceed both the assay-repeatability floor and a predeclared minimum useful effect anchored to the corrected gap/comparator; cells/fields are not independent donors. | Benefit restricted to cell count, fusion, biomarker shifts or treatment during differentiation: stop the mature-function development claim. A qualified negative functional result is meaningful; imprecision is an inconclusive result. |
| **C. Establish target attribution** | Direct engagement, appropriate compartmental lipid response and convergent functional benefit from temporal C2β perturbation or a validated orthogonal article. | BLU benefit persists without relevant C2β engagement, or requires known off-target exposure: redirect the article/mechanism. Do not preserve a C2β label by assumption. |
| **D. Resolve an exposure window** | Measure unbound exposure in the actual muscle system and relevant safety systems. Benefit and absence of adverse function must overlap across exposure uncertainty, incorporating measured tissue distribution rather than assuming equal tissue concentrations. | In-vitro liability at muscle-equivalent free exposure keeps the window open pending distribution evidence. Stop systemic BLU when the required measured exposure in the vulnerable tissue overlaps adverse function without usable separation. Consider another article or tissue restriction only if it changes that window. |
| **E. Establish persistence and reversibility** | Functional gain remains during sustained exposure without deteriorating tissue function; washout/rechallenge distinguishes compensation from assay carryover. | Early gain followed by declining output or unresolved toxicity: stop the current schedule/article thesis. Withdrawal loss alone is compatible with a maintenance therapy and is not a failure. |
| **F. Demonstrate practical differentiation** | A same-model comparison supports a useful advantage in function, durability, tolerability or feasible delivery relative to an appropriate comparator. | A weaker outcome than an accessible comparator with no compensating practical advantage: deprioritize the asset even if its biology is interesting. |

The immediate value-producing package is **A–D**, with comparator and exposure work designed in from the start. A theoretical tenfold selectivity ratio, a supplier listing, a second review article or another positive pathway marker cannot close these gates.

## 6. Evidence status and remaining uncertainty

**Supported:** mouse target causality, a kinase-dependent mechanism, and the existence of post-onset/reversible disease components. **Supported but bounded:** exact-BLU animal efficacy and human cellular pathway relevance. **Open:** exact-BLU mature human force, cross-genotype breadth, free tissue exposure and a chronic therapeutic window. **Not established:** S-tier status, clinical efficacy, universal genotype/sex coverage, or correction of MTM1-associated liver disease.

This research materially improves the choice of what would falsify the lead. It does not turn an unavailable experiment into completed evidence. The decision should move when those distinctions change, rather than when another paper repeats the same pathway rationale.

## Primary sources and audit trail

- **B01:** Sabha et al., 2016, *JCI*, DOI [10.1172/JCI86841](https://www.jci.org/articles/view/86841). Full text, Figure 4 and Cre methods inspected.
- **B02:** Massana-Muñoz et al., 2023, *JCI Insight*, DOI [10.1172/jci.insight.151933](https://insight.jci.org/articles/view/151933). Full text and figure captions inspected.
- **B03:** 2026 exact-BLU paper, DOI [10.1172/jci.insight.198568](https://insight.jci.org/articles/view/198568). Interpreted with the repository's round-4 source audit.
- **B04:** Amoasii et al., 2012, *PLoS Genetics*, DOI [10.1371/journal.pgen.1002965](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1002965). Full text, force and lipid results inspected.
- **B05:** Moschovaki-Filippidou et al., 2025, *JCI Insight*, DOI [10.1172/jci.insight.189286](https://insight.jci.org/articles/view/189286), PMID 41086017. Full text and methods inspected.
- **B06:** Kutchukian et al., 2016, *PNAS*, DOI [10.1073/pnas.1604099113](https://pubmed.ncbi.nlm.nih.gov/27911767/). Indexed primary text/figure captions inspected; full PMC open encountered a bot check. Animal-age and donor-denominator details were not independently resolved here.
- **B07:** 2022 integrin study, DOI [10.1073/pnas.2202236119](https://doi.org/10.1073/pnas.2202236119), [PMC9549396](https://pmc.ncbi.nlm.nih.gov/articles/PMC9549396/). Primary text and pharmacology-team cross-check.
- **B08:** 2025 recycling study, DOI [10.1016/j.jlr.2025.100756](https://pubmed.ncbi.nlm.nih.gov/39952567/). Primary indexed text; already present in round 4.
- **B09:** Picot et al., 2026, *Nature Metabolism*, DOI [10.1038/s42255-026-01484-1](https://www.nature.com/articles/s42255-026-01484-1), [publisher PDF](https://www.nature.com/articles/s42255-026-01484-1.pdf), PMID 41851531. Full PDF, methods, Figure 7 and Extended Data 10 visually inspected. PDF SHA256 `befe1fdb818d9c7c280e3d58aeba158f5ab121f7ef3ebbf522f98011e6c0775e`.
- **B10:** Gozzelino et al., 2022, *Brain*, DOI [10.1093/brain/awac082](https://academic.oup.com/brain/article/145/7/2313/6628565), [institutional PDF](https://air.unimi.it/retrieve/c4f0e35b-fdbd-4f0e-8d8f-d2f23722ddf9/Defective%20lipid%20signalling%20caused%20by%20mutations%20in%20PIK3C2B.1.pdf). Full indexed PDF inspected.
- **B11:** Alliouachene et al., 2015, *Cell Reports*, DOI [10.1016/j.celrep.2015.10.052](https://pubmed.ncbi.nlm.nih.gov/26655903/), [institutional PDF](https://www.babraham.ac.uk/sites/default/files/media/files/26655903.pdf).
- **B12:** Srivastava et al., 2009, *Molecular Biology of the Cell*, DOI [10.1091/mbc.e09-05-0390](https://pubmed.ncbi.nlm.nih.gov/19587117/). Primary abstract.
- **B13:** Karolczak et al., 2023, *JCI*, DOI [10.1172/JCI166275](https://www.jci.org/articles/view/166275). Full results and rescue limits inspected.
- **B14:** Pannia et al., 2026-02-18, *Science Translational Medicine*, DOI [10.1126/scitranslmed.adr1483](https://pubmed.ncbi.nlm.nih.gov/41706871/). Primary abstract; publisher full text was inaccessible in this review.
- **B15:** Chen et al., 2026-10-29, *Molecular Therapy*, DOI [10.1016/j.ymthe.2026.10.027](https://pubmed.ncbi.nlm.nih.gov/42958795/). Primary abstract; no full-methods animal-denominator claim.
- **B16:** Colombo et al., 2025, unite-CNM hepatic report, DOI [10.1177/22143602251329215](https://journals.sagepub.com/doi/10.1177/22143602251329215). Full text and study-termination description inspected.
- **B17:** AZD8055 phase I, 2012, *British Journal of Cancer*, DOI [10.1038/bjc.2012.368](https://www.nature.com/articles/bjc2012368). Full safety/PK results inspected; this is historical adult oncology evidence.
- **B18:** Chresta et al., 2010, AZD8055 pharmacology, [PMID 20028854](https://pubmed.ncbi.nlm.nih.gov/20028854/). Primary abstract confirms dual-complex pharmacology.
- **B19:** 2019 carrier deep-phenotyping study, DOI [10.1212/WNL.0000000000008316](https://doi.org/10.1212/WNL.0000000000008316), [PMC6815204](https://pmc.ncbi.nlm.nih.gov/articles/PMC6815204/). Indexed primary text.
- **B20:** [ClinicalTrials.gov NCT07052929](https://clinicaltrials.gov/study/NCT07052929), [primary API record](https://clinicaltrials.gov/api/v2/studies/NCT07052929). Retrieved 2026-11-04; last posted update 2026-09-03. JSON SHA256 `02dd5c49a7e3725e0bf98f6cdb2172fb4d4878844b3a677c7815b6a2a12ed5f1`.
- **B21:** Astellas [VALOR community information](https://myotubulartrust.org/wp-content/uploads/Astellas_XLMTM-Community-Information-VALOR-clinical-trial-overview_FINAL.pdf). Sponsor-authored primary document; host is Myotubular Trust.
- **B22:** Kora et al., online 2025 / issue 2026, *Brain*, DOI [10.1093/brain/awaf278](https://pubmed.ncbi.nlm.nih.gov/40729434/). Primary abstract; full human-model interpretation cross-referenced to the root workstream.

Local source copies/screenshots are research intermediates; citations link to the original public sources. No third-party full text is proposed for republication in the repository.
