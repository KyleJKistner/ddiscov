# Independent challenge: PLCζ fertility rescue and FeM-1269 iron transport

> **Historical review snapshot.** Later findings and rankings are reconciled in the [current shortlist](../../../decisions/current-shortlist.md) and [round 4 review](../round4/README.md). Statements about activity or access describe this review period.

Reviewed 4 November 2026. This is an independent challenge of candidates promoted by another research branch. No outreach, purchases, human experimentation, or remote repository changes were performed. Proposed studies and budgets are planning judgments, not completed experiments or supplier quotes.

## Decision

**PLCζ remains an A-tier, potentially high-value proof project. I would fund sequence-defined reagent qualification and an active-comparator rescue experiment; I would not yet describe it as an S-tier differentiated clinical product.** The biological lesion is unusually direct, the delivery route already reaches the relevant compartment, and an experimentally useful product can be built from public information. Its largest remaining question is whether a reproducible, stable reagent improves development sufficiently over existing assisted activation to justify a new clinical product. The strongest clinical paper does not answer that comparative question.

**FeM-1269 is A− as a mechanistic translational research prospect, with a particularly good human-cell experiment available.** It has an unusually coherent physical-function replacement hypothesis and a more developed animal pharmacology package than a typical screening hit. Its anemia efficacy model is less clean than the abstract implies. Existing patent/license disclosures also make it a substantially less obvious unencumbered asset than a catalog listing might suggest. Neither issue prevents a sensible research proof.

| Candidate | Existing repository record | Publicly actionable next step | Why it is not yet S-tier |
|---|---|---|---|
| PLCζ | `screen-index:PLCZ_FUNCTIONAL_REAGENT_COMPARISON:537` | Manufacture a fully specified research construct; establish reproducible oscillation potency and embryo development against ionophore | Exact clinical construct not disclosed adequately; comparator and clinical endpoint limitations |
| FeM-1269 | `screen-index:transport-02-fem1269:510` | Authenticate the optically positive compound and test macrophage-to-erythroid iron transfer in human donor systems | No exact-compound human functional rescue demonstrated here; mixed anemia model; existing rights need weighting |

## 1. PLCζ: what survives the challenge

The opportunity is to replace the deficient sperm activation signal at ICSI with a measured amount of functional enzyme. This is a stronger starting hypothesis than nonspecific stimulation of downstream pathways. A reagent with predictable potency, good handling stability, and a clear selection rule for activation deficiency would be a concrete product even before anyone claims broad superiority in IVF.

### Clinical evidence ledger

The 2026 case series included 135 couples, with treatment allocated by sperm PLCζ staining rather than randomized across the same population. Previous cycles were historical controls, generally within 12 months; the collection spans 25 years. Twenty couples received rhPLCζ alone. Reported outcomes combine ongoing pregnancies and deliveries. [P1]

| Group | Couples | Historical / intervention cycles | Historical / intervention 2PN fertilization | Intervention ongoing-or-delivered / transfer cycles |
|---|---:|---:|---:|---:|
| Ionophore | 77 | 85 / 133 | 137/790 / 622/1,185 | 21/39 |
| rhPLCζ | 20 | 40 / 32 | 60/327 / 116/280 | 5/17 |
| Dual | 38 | 48 / 50 | 118/489 / 355/485 | 19/31 |
| All | 135 | 173 / 215 | 315/1,606 / 1,093/1,950 | 45/87 |

Raw counts transcribed from Tables 1–6 of [P1]; calculations and interpretation below are this review. The zero-fertilization columns are nested subgroups and must not be added to their full-cohort columns.

The effect on two-pronuclear fertilization is a credible signal deserving replication. It should update the prior probability that replacement can work in selected human gametes. It does not establish how much of the observed improvement was caused by rhPLCζ, which patients benefit over ionophore, or whether the dual regimen is synergistic.

### Denominator audit

Several reported percentages do not reconcile with the printed counts:

| Location | Printed inputs | Independent calculation | Consequence |
|---|---|---|---|
| Dual ongoing/delivery | 19 events, 31 transfer cycles, printed 63.3% | 19/31 = **61.3%**; 63.3% would imply a denominator of 30 | The headline clinical percentage has an unresolved denominator |
| Ionophore ongoing/delivery | 21 events, 39 transfer cycles, printed 54.8% | 21/39 = **53.8%** | A second discrepancy lowers confidence in numerical reporting |
| Testicular-sperm activation | 41 events, 133 injected oocytes, printed 28.5% | 41/133 = **30.8%** | Another table percentage does not reconcile |
| Aggregate pregnancy loss | 4 events, printed 4.6% | 4/87 transfers = 4.6%; 4/49 implantations = 8.2% | The apparent denominator changes from the subgroup loss calculations; this cannot be sold as a clean miscarriage comparison |
| rhPLCζ ongoing/delivery | 5 events, 17 transfers, 32 intervention cycles | 29.4% per transfer; **15.6% per intervention cycle** | Per-transfer success is conditional on reaching transfer |
| All ongoing/delivery | 45 events, 87 transfers, 215 intervention cycles | 51.7% per transfer; **20.9% per intervention cycle** | A much larger conditionality effect than the small arithmetic errors |

These discrepancies do not erase the fertilization counts. They do mean the pregnancy claims need less weight than a headline reading gives them. The last two calculations are alternative denominators, not new estimates of live birth: the source does not separate completed deliveries sufficiently for that claim.

### Independence and confounding

The independent clinical unit is the couple, with cycles and oocytes nested within it. Treating each oocyte as an independent patient would make precision look better than it is. Repeated cycles also carry shared female, male, laboratory, and operator effects. A repeated-measures model or paired couple-level analysis is required to quantify treatment uncertainty properly; the described chi-square/Fisher comparisons do not resolve this hierarchy.

Selection on an unusually poor prior fertilization result creates regression-to-the-mean risk. Changes in stimulation, egg cohort, sperm preparation, or operator can also produce a difference between cycles. The within-12-month comparison helps, but does not make the design randomized.

Most importantly, treatment assignment tracks the proposed cause of failure. A higher fertilization fraction in the dual group cannot demonstrate superiority over rhPLCζ or ionophore in an exchangeable population. Neither can it establish synergy, which requires an interaction comparison within a common experimental design.

Sperm staining is an enrichment tool, not a functional diagnosis by itself. Normal abundance need not imply catalytic competence, correct localization, or release. An abnormality in a protein assay can also coexist with oocyte defects. The proposed diagnostic product should therefore include a function-linked selection criterion, rather than simply reproduce a staining threshold.

## 2. The exact PLCζ article is not yet an authenticated reproducible construct

The clinical paper identifies a custom GenScript 64.5-kDa preparation from bacterial expression, nickel affinity and size exclusion, but does not provide a sequence accession, full fusion sequence, tag-cleavage state, lot certificate, or quantitative activity release specification. Its supplement is a consent form. Mouse validation measured pronuclear activation, not direct calcium oscillation physiology. The ionophore method also switches between 50 µM and 50 mM. [P1, P2]

The claimed approximately 3.6 million injected molecules is arithmetically consistent with 0.4 pL of a 0.97 mg/mL, 64.5-kDa preparation. That is not the weakness. A consistent nominal mass calculation cannot establish molecular identity or effective catalytic dose.

There are three different entities that must remain separate:

| Entity | What is public | What must not be inferred |
|---|---|---|
| GenScript clinical material | Supplier and partial production description in [P1] | That any catalog PLCZ1 reagent is identical |
| 2024 MBP-PLCζ research construct | pETMM41-based MBP fusion, mouse calcium oscillations, frozen enzyme stability | That this fusion was used in the 2026 patients, or that its safety transfers to another construct |
| Canonical PLCZ1 and catalog shorter isoform | UniProt Q86YW0 canonical protein has 608 amino acids; Cusabio advertises aa1–415, full isoform 2 with N-His-SUMO, at 64.5 kDa | That matching 64.5-kDa labels authenticate the clinical preparation |

Sources: [P3–P5]. The Cusabio match is a reason to demand sequence specificity, not evidence of an error by the clinical authors. A shorter natural isoform, a fusion, and a canonical protein can behave differently even when sold under the same target name. Supplier claims of purity are not a potency assay.

The 2024 MBP construct retains enzyme activity after 90 days at −80°C, but performs worse after storage at −20°C or 4°C. Its chicken embryo assay is a preliminary toxicity observation, not mammalian post-ICSI offspring validation. [P3] These results make the reagent engineering problem plausible and testable. They do not give the clinical preparation a shelf-life claim.

The 50 µM/50 mM inconsistency is 1,000-fold and must be recorded as unresolved. A proposed study should use an independently justified comparator protocol with explicit concentration units and measured handling, not silently choose whichever value is convenient from this paper.

### A viable product definition

**Proposed product:** a sequence-defined, potency-qualified, stable recombinant PLCζ reagent for confirmed activation deficiency at ICSI, with a functional companion assay or a validated selection rule.

**Proposed research construct:** full-length canonical human PLCZ1, Q86YW0 residues 1–608, produced with a removable solubility tag; compare the retained-tag and tag-cleaved preparations during development. The intended delivered species would be chosen only after demonstrating preserved activity and stability. This is a new, explicit development design, not a claim to have reproduced the clinical protein. The published MBP reagent is a useful positive benchmark.

The defensible differentiation could be reproducible calcium oscillations and improved development at a controlled dose, superior stability/handling, or rescue in a subgroup inadequately served by ionophore. “Physiological” by itself is not a commercial endpoint. Protein replacement can also create nonphysiological timing or excessive activity, so the concentration-response window matters as much as maximal activation.

The availability conclusion is therefore **buildable research reagent**, not unavailable until an owner replies. Public sequence and standard recombinant production make an independent prototype possible. Routine analytical and functional qualification should establish whether it deserves more investment.

## 3. The positive PLCζ experiment to fund

### First milestone: make the signal reproducible

Use three genuinely independent production lots, not three aliquots of one batch. Establish sequence and intact-mass identity, aggregate fraction, residual host contaminants, endotoxin, and enzyme activity. The primary potency assay should include calcium oscillation kinetics in an activation-deficient ICSI model, with normal fertilization providing a physiological reference.

Compare vehicle, a defined ionophore protocol, the published MBP benchmark, and the proposed formulation. Include a matched inactive protein or appropriately characterized inactive control to distinguish catalytic rescue from injection or formulation effects. Test clinically practical thawing, bench residence, and freeze–thaw conditions; activity after storage is more relevant than protein concentration alone.

Use approximately 24–30 independent donor females across multiple experimental days for an initial mouse comparison, distributing sibling oocytes across conditions. Analysis should retain donor and batch clustering. Oocytes increase measurement precision within donors; they do not create hundreds of independent biological replicates. An internal pilot should set variance and effect-size assumptions before a confirmatory sample size is fixed.

Readouts should proceed from calcium dynamics to normal 2PN formation, then blastocyst development and embryo quality. Activation alone is an inadequate success criterion. A later mouse transfer arm should assess offspring, with recipient dam/litter as another statistical level. It should be considered a separate safety-development milestone, not silently folded into a cheap activation assay.

**Go criterion, proposed:** reproducible rescue across lots and donors, an acceptable dose window, and a material developmental advantage over ionophore or a reproducible rescue of a defined ionophore-resistant subgroup. **Kill criterion:** similar activation but no developmental advantage, unstable potency, abnormal calcium dynamics, or a narrow toxicity window. Noninferior embryo development plus substantially better reagent control might support a research-tool business, but is a different investment thesis.

### Second milestone: a human functional bridge

Use appropriately consented research material from a functionally characterized activation-deficient population, with sperm genotype/phenotype and prior ICSI failure documented. Randomize sibling oocytes where feasible and prespecify the minimum number of evaluable donor couples, not a target number of eggs alone. An initial 20–30-couple feasibility study would estimate variance and selection performance; it should not be called a powered live-birth trial.

The initial research endpoint is normal fertilization and development with the actual proposed product against the active comparator. A future interventional trial would need the qualified clinical product and relevant approvals, a prospectively randomized design, live birth per started cycle, complete transfer accounting, and child follow-up. Existing human use is relevant supporting evidence, but it does not exempt a new construct from its own product and clinical development.

**Planning allowance:** roughly $100,000–180,000 for the sequence/lot/analytics and mouse functional milestone, followed by approximately $120,000–300,000 for a human research bridge. These are broad project budgets assuming access to an established embryology laboratory, approximately three protein lots, paid analytical services, multiple donor batches, and specialist imaging/ICSI time. They exclude a clinical live-birth trial, formal regulatory manufacturing, long-term offspring follow-up, and any license payment. Human sample access and recruitment, rather than protein mass, are likely the dominant uncertainties.

### Rights and clinical-development interpretation

Google Patents lists US20080175827A1 as abandoned, with a 2011 failure-to-respond event. [P6] That supports a narrow historical observation, not global freedom to operate. Later method, formulation, diagnostic, manufacturing, or jurisdiction-specific rights remain possible. The correct next action for this research decision is a focused public claim landscape attached to the exact proposed product, not an owner email as a prerequisite to understanding its scientific value.

## 4. FeM-1269: functional replacement, with an important model boundary

FeM-1269 is the optically positive tropolone derivative designated (+)-6, designed to reduce the aggregation problem of hinokitiol–iron complexes. The paper reports iron transport in deficient cell systems and six-day post-induction anemia treatment in mice. However, the final model combines turpentine inflammation, dietary iron restriction, and bleeding; the inflammatory/hepcidin response wanes over follow-up. The work includes exploratory 90-day mouse tolerance, shorter rat testing, and pharmacokinetics. High-dose rat stomach lesions and altered splenic iron are disclosed. [F1]

This is **post-induction treatment**, not merely prophylaxis. But it is not a clean demonstration that FeM restores erythropoiesis during sustained chronic inflammatory iron sequestration. A mixed model may amplify a benefit by combining iron scarcity, blood-loss recovery, and resolution of inflammation. That is a reason to choose a sharper next experiment, not to discard a coherent mechanism.

The model also illustrates why hemoglobin and serum iron should be kept separate. A compound can move iron across a membrane yet fail to deliver it into useful heme, or move it into harmful redox-active pools. Conversely, a modest change in circulating iron can be sufficient if the marrow is otherwise competent. The development question is destination and function, not iron movement alone.

The 2022 hinokitiol paper provides relevant human patient-macrophage evidence and a transferrin-dependent route to erythroid maturation. [F2] That is mechanism-class support; it is not direct validation of FeM-1269 in human cells. The exact compound must earn its own translational bridge.

### Obtainability and identity

Probechem lists PC-22243, CAS 2640543-21-9, with small packs labeled in stock, including 10 mg at $528. A public batch certificate exists for PC-2224301 and claims >98% purity. Its text names the tetrahydrofuran-substituted tropolone without an explicit enantiomeric-purity value. [F3, F4] This is better evidence of a testable source than “available on request,” but it is not confirmation of current inventory, biological potency, or clinical quality.

The exact intended article is the paper’s (+)-6 compound, with the stated chemical form and analytical characterization. Confirm chirality, salt/free-compound form, purity, and iron-transport behavior on receipt. A non-stereospecific structure label should not be treated as proof of a matched enantiomer. This is routine compound authentication, not a reason to wait for an inventor.

The public primary report also identifies patent families licensed to Cajal Neuroscience and former Ambys tropolone patents owned by Cajal. [F1] Thus “catalog available” and “commercially unencumbered” are demonstrably different questions here. This materially reduces the attractiveness of pretending FeM is a free standalone asset, while preserving its value as a research benchmark and potential development thesis.

### Strongest next proof: human macrophage-to-erythroid iron transfer

The proposed experiment asks whether the **same iron atoms** leave a sequestering human macrophage, load onto transferrin, and enter functional hemoglobin in human erythroid precursors under continued iron-restricting conditions.

Use paired donor-level experiments from approximately 8–12 independent macrophage donors, with disease-derived cells where feasible and a controlled persistent-hepcidin model in healthy cells. Use at least 4 independent erythroid donor backgrounds; report both donor sources and avoid counting every donor cross-pair as fully independent. Assay repeats should support precision within each biological donor.

Pulse-load macrophage iron with a traceable isotope before inducing the transport defect. Compare authenticated FeM-1269, hinokitiol, vehicle, and an iron-delivery positive control. A chelation comparator helps distinguish redistribution from simple removal. Include conditions that separate transferrin-mediated transfer from nonspecific uptake, and maintain the inflammatory/hepcidin environment during the functional test.

The decisive endpoint is isotope incorporation into erythroid heme/hemoglobin together with maturation and viability. Measure macrophage retention, transferrin-bound iron, non-transferrin-bound/labile iron, reactive oxygen species, lipid oxidation, mitochondrial effects, and copper/zinc redistribution. Examine aggregation in biologically relevant medium rather than relying only on a buffer-based colloid result.

A useful **proposed go threshold** would be consistent restoration of a material fraction of the iron-restricted hemoglobinization deficit across donors, without a corresponding rise in redox injury or impaired maturation. The numerical threshold should be locked after assay validation, before blinded testing. Kill if iron efflux occurs without heme delivery, if only nonphysiological exposure works, or if the effective range overlaps metal toxicity/aggregation.

Mouse total serum concentrations should not be equated with human unbound exposure. The human-cell study should measure medium and intracellular concentrations and protein binding, then relate the effective exposure to the published animal exposure range. The first follow-on animal study should demonstrate treatment of established anemia with continuing inflammatory restriction and use an appropriate active comparator, rather than repeat the same optimized model.

**Planning allowance:** $70,000–160,000 for a donor-based functional study, isotope/metal analytics, compound authentication, and exposure measurements, assuming an established erythroid culture platform. A subsequent focused animal/exposure proof could add approximately $60,000–140,000. These are cost assumptions, not quotes. Material cost is small compared with donor biology and validated metal/hemoglobin measurements.

## 5. Process corrections illustrated by these cases

1. **Identify the actual article before ranking a target.** PLCZ1 can mean different isoforms, fusion tags, and activity states. FeM can mean an enantiomer or a catalog name with unstated chirality.
2. **Separate biological plausibility, comparative benefit, and product readiness.** Human use does not automatically validate a new reagent, and a good chemical transport assay does not automatically imply clinical erythropoiesis.
3. **Count independent units.** Couples, donor females, cell donors, animals, production lots, and experimental days answer different questions. Oocyte counts and repeated wells cannot substitute for those units.
4. **Audit denominators before repeating headline percentages.** Per-transfer, per-started-cycle, and live-birth outcomes are different. A readily calculated fraction is not necessarily the clinically relevant one.
5. **Use shortcomings to design the next valuable proof.** The point is not to accumulate reasons to hold every candidate. PLCζ needs reproducible identity and active-comparator development; FeM needs human iron destination and heme function under persistent restriction.
6. **Keep rights uncertainty weighted and specific.** An abandoned application is not global clearance; an available research vial is not a license. Neither fact requires outreach before completing a scientific shortlist.

## Primary source register

### PLCζ

- **[P1]** Xie et al., *Assisted oocyte activation re-envisioned: a more physiological approach*, 16 June 2026. Main article and Tables 1–6: https://link.springer.com/article/10.1007/s10815-026-03921-2 . PDF: https://link.springer.com/content/pdf/10.1007/s10815-026-03921-2.pdf .
- **[P2]** Supplement to [P1], seven-page informed-consent document, inspected completely; no construct sequence or release certificate: https://static-content.springer.com/esm/art:10.1007%2Fs10815-026-03921-2/MediaObjects/10815_2026_3921_MOESM1_ESM.pdf .
- **[P3]** Saleh et al., *Development of Recombinant PLC-Zeta Protein as a Therapeutic Intervention for the Clinical Treatment of Oocyte Activation Failure*, Biomedicines 2024;12:1183. https://doi.org/10.3390/biomedicines12061183 . Author-deposited PDF: https://orca.cardiff.ac.uk/id/eprint/169637/1/biomedicines-12-01183.pdf .
- **[P4]** UniProt canonical human PLCZ1, Q86YW0: https://www.uniprot.org/uniprotkb/Q86YW0/entry . The indexed UniProt location entry explicitly reports 608 amino acids: https://www.uniprot.org/locations/SL-0007 .
- **[P5]** Cusabio CSB-EP768240HU, manufacturer description of aa1–415/full isoform 2/N-His-SUMO/64.5-kDa research protein: https://www.cusabio.com/Recombinant-Protein/Recombinant-Human-1-phosphatidylinositol-45-bisphosphate-phosphodiesterase-zeta-1PLCZ1partial-1030901.html . An additional supplier explicitly states untested activity: https://www.targetmol.com/recombinant-protein/plcz1_protein_human_recombinant_his_sumo .
- **[P6]** Published application and indexed legal events, not a complete legal opinion: https://patents.google.com/patent/US20080175827A1/en .
- **Additional clinical registry link:** https://clinicaltrials.gov/study/NCT01944332 . Official page was reachable but its dynamic record text was not exposed by this retrieval tool. No current recruitment or regulatory status is asserted from that page.

### FeM-1269

- **[F1]** Blake et al., *Minimizing higher-order aggregation maximizes iron mobilization by small molecules*, Nature Chemical Biology 2024;20:1282–1293. https://www.nature.com/articles/s41589-024-01596-3 . Author manuscript: https://pmc.ncbi.nlm.nih.gov/articles/PMC11831690/ . Detailed methods and model optimization were retrieved through indexed primary text. Publisher extended data and competing interests were also inspected. Supplementary PDF, 26.6 MB, too large for this web parser and not independently fully reviewed: https://static-content.springer.com/esm/art:10.1038%2Fs41589-024-01596-3/MediaObjects/41589_2024_1596_MOESM1_ESM.pdf . Do not claim a complete supplementary chemistry or toxicology audit.
- **[F2]** Ekaputri et al., *A small molecule redistributes iron in ferroportin-deficient mice and patient-derived primary macrophages*, PNAS 2022;119:e2121400119. https://pmc.ncbi.nlm.nih.gov/articles/PMC9245668/ . https://pubmed.ncbi.nlm.nih.gov/35737834/ . This is hinokitiol evidence, not FeM evidence.
- **[F3]** Probechem PC-22243 listing: https://www.probechem.com/products_FeM-1269.html .
- **[F4]** Public supplier certificate and data sheet: https://www.probechem.com/userfiles/Products/PDF/PC-22243/PC-2224301/PC-2224301_COA.pdf ; https://www.probechem.com/userfiles/Products/PDF/PC-22243/PC-2224301/PC-2224301_DataSheet.pdf .

### Review boundaries

PLCζ main paper, clinical tables, methods, supplement, the distinct 2024 construct, manufacturer identity examples, and one old patent family were challenged. FeM main/extended primary text, detailed model methods, public supplier certificate, and its hinokitiol human-mechanism antecedent were checked. Neither assessment is a comprehensive patent clearance, completed supplier qualification, or formal regulatory determination. Those are future concrete work packages; they are not reasons to stop this scientific assessment or ask an owner to supply the investment thesis.
