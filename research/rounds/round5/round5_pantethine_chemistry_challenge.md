# Round 5 — Pantethine / pantetheine identity and exposure challenge

**Research date:** 2026-11-04. **Scope:** public chemistry, assay identity, metabolism and exposure; complementary to the clinical/functional PPCS review. No outreach, procurement, experiments or remote writes.

## Decision

**Keep the PPCS rescue hypothesis under active review, but do not regard oral pantethine as an exposure-qualified development article.** The published reagent name and catalog number conflict; the culture conditions can alter sulfur speciation; and no source reviewed establishes the concentration of an intact PPCS-bypassing precursor reaching human myocardium after the reported oral treatment. These are specific, decision-relevant uncertainties. They do not demonstrate that the biological results are false or that oral treatment cannot work.

The strongest correction to a negative interpretation is equally important: historical plasma nondetection was an indirect, relatively insensitive measurement in another disease. A newly published 2026 primary study reports relative pantethine signals by LC-MS in human serum and mouse plasma. Those observations can coexist. Neither supplies the missing quantitative oral-to-cardiomyocyte bridge.

## 1. Lock the identities before combining evidence

| Material | Public identity | What it establishes |
|---|---|---|
| Sigma 16702 | (R)-Pantetheine, reduced monomer, PanSH; CAS 496-65-1; C11H22N2O4S; MW 278.37; ≥95% HPLC | Current manufacturer identity. It does not prove the content of the historical experimental vial. [S1] |
| Sigma/Supelco P2125 | D-Pantethine, disulfide dimer, PanSSPan; CAS 16816-67-4; C22H42N4O8S2; MW 554.72 | A chemically distinct catalog product; one molecule contains two pantetheine moieties. [S2] |
| Zhang 2025 cell reagent | Named “pantethine” with catalog 16702 | Unresolved name–catalog inconsistency. Do not silently relabel the experiments or infer mis-supply. [S3, Methods p4] |
| Wedman 2025 reagent table | Explicitly lists 16702 as PanSH and P2125 as PanSSPan | Independent contemporary primary corroboration of the distinction. [S4, printed p12 / PDF p13] |
| 4′-Phosphopantetheine | PPanSH, the phosphorylated downstream precursor | A separate chemical article, not a synonym for either entry above. [S4, Fig1; S7] |

Chemical bookkeeping alone gives a potential twofold ambiguity in *moiety* equivalents. Under a fully specified pure-compound assumption, 100 μM PanSH contains 100 μM pantetheine moieties, while 100 μM PanSSPan contains 200 μM. The corresponding nominal mass concentrations are 27.837 and 55.472 mg/L, calculated from the manufacturer molecular weights. **These calculations are not corrections to the paper:** stock preparation, molecular weight used for dilution, batch identity and subsequent redox composition are not established. Nor are they plasma or intracellular concentrations. [S1–S2; arithmetic]

A valid evidence ledger therefore needs separate fields for **bottle identity**, **nominal added dose**, **species present over time**, and **intracellular CoA response**. A biological response can remain real while the exact active extracellular species is unresolved.

## 2. Exposure observations that must remain distinct

| Source / setting | Administered or added material | Dose, matrix and time | What was actually measured; limitation |
|---|---|---|---|
| Zhang 2025, patient-derived 2D cardiomyocytes | Name/catalog conflict above | 100 μM, five days; EB2 with 2% heat-inactivated FBS and 0.1 mM β-mercaptoethanol; medium exchanged every other day | Functional readouts; no concentration-time profile of PanSH, PanSSPan or PPanSH. [S3, p3] |
| Zhang 2025, 3D cardiac patches | Same paper's nominal “pantethine” | 500 μM, days 7–21; EB2 recipe includes 0.1 mM β-mercaptoethanol | Contractile/arrhythmic readouts, not redox-resolved exposure. [S3, p3, Fig3] |
| Zhang 2025, oral PPCS treatment | Commercial pantethine from several named manufacturers | Approximately 10–17 mg/kg/day in described regimens; formulations vary | No paired active-species plasma/heart PK reported. Clinical causality is reviewed separately. [S3, p2] |
| Wittwer 1985, four cystinotic children | Oral aqueous D-pantethine | 70–1,000 mg/kg/day; repeated-dose plasma sampling principally 1 and 5 hours after a dose | Indirect plasma assay; 32 samples without detected panteth(e)ine. Detection boundary 5–10% of concurrent pantothenate, not a fixed LC-MS LLOQ. [S5, pp1666–1669] |
| Cao 2026, inflammatory mouse model | Sigma P2125 | 50 mg/kg intraperitoneally daily; day6 collection, precise postdose plasma time not specified in cited caption | Relative plasma pantethine LC-MS signal increased; not absolute molar concentration or oral PK. [S6, FigS3M] |
| Cao 2026, human serum | Endogenous, observational | Healthy donors n17; psoriasis patients n12 | Relative LC-MS comparison, not a post-oral-dose exposure series. [S6, FigS5S] |

All culture concentrations above are **nominal extracellular additions**. No unbound fraction, intracellular precursor concentration, target-organ partition or exposure coverage calculation is justified. The 3D result is stabilization of force, as addressed in the parent efficacy audit; chemical uncertainty should not be used to exaggerate or erase that result.

β-Mercaptoethanol supplies a thiol-containing experimental environment. Reduction, oxidation and mixed-disulfide exchange are plausible; their extent cannot be calculated from the ingredient list. Heat-inactivated dilute serum also differs from intact circulating plasma. Thus the right conclusion is *unmeasured speciation and metabolic stability in the efficacy matrix*, not that the supplement necessarily remained monomeric or necessarily became a particular mixed disulfide. There is no public basis for applying a simple factor-of-two correction or treating the nominal 100/500 μM values as required human plasma troughs.

## 3. Reconcile the apparently conflicting blood evidence

Wittwer's assay measured the increment in radioimmunoassayed pantothenate after pantetheinase treatment with 5 mM DTT. It therefore did not separately quantify reduced monomer and disulfide. The authors also detected urinary pantethine after enrichment: 0.57±0.32% of excreted pantothenate, n23, and explicitly allowed transient circulation. The four children had renal impairment, with creatinine clearances 17–67 mL/min/1.73 m². [S5, pp1666–1669]

Cao used LC-MS and reports relative abundance. The published extraction method uses cold organic solvent and overnight extraction; the inspected main methods do not disclose a redox-preserving quench, validated species transitions, calibration range, recovery or LLOQ. The study also uses 50 μM β-mercaptoethanol in dendritic-cell media. These omissions prevent reconstruction of an absolute redox-species balance; they do not by themselves invalidate the reported relative comparisons. [S6, Methods]

The comparison has four separate mismatches:

1. **Route:** the 2026 intervention is intraperitoneal; the 1985 intervention is oral. Bypassing intestinal handling can change what reaches plasma.
2. **Population:** cystinosis with renal disease, inflammatory mice and observational adult human serum are different settings. Neither is an oral exposure study in PPCS deficiency.
3. **Analytical question:** an enzyme-coupled difference assay and a relative LC-MS signal have different sensitivity, selectivity and normalization. A nondetect in the former does not imply that the latter cannot find a signal.
4. **Species/time:** neither study provides the needed paired oral concentration-time curves for PanSH, PanSSPan, PPanSH and relevant mixed disulfides in the PPCS setting.

Accordingly, preserve **substantial hydrolysis as a real exposure liability** and **some intact or salvage-competent exposure as an open possibility**. Do not recast the 28-hour elimination half-life of pantothenate reported in 1985 as the half-life of pantethine or of the desired bypass precursor. [S5]

## 4. What the new transport work changes

The JBC article is **2025**, DOI 10.1016/j.jbc.2025.110503, not 2026. In yeast, PanSH and PPanSH can form glutathione mixed disulfides and enter through Opt1. Its experiments use 27 μM precursor with 67 μM GSH; preoxidation, reducing-agent controls and OPT1 genetics support a chemically specific mechanism. The discussion says Opt1 has no apparent ortholog outside yeast and explicitly leaves analogous mammalian uptake untested. [S4, Figs1–3; Discussion; reagent table]

This raises the credibility of *redox-dependent alternative uptake*, while leaving the human transport and exposure questions open. It is not a license to treat yeast rescue as proof that oral pantethine reaches a child's heart. Conversely, it makes a blanket inference that polarity or absent parent plasma signal rules out all bypass delivery too strong.

An additional primary mechanism is microbiome processing. Yu 2022 traced precursor use in flies: pantethine rescue of a PANK-null developmental block depended on the microbiome, whereas supplied PPanSH could rescue without it; pantothenate plus cysteamine did not substitute. That establishes a nonhuman route by which an administered molecule can act through a different salvage precursor. It does not establish its size, consistency or necessity in human PPCS disease. [S9]

From pathway structure, pantothenate generated by complete hydrolysis still encounters the PPCS step. Therefore increased vitamin B5 exposure cannot, by itself, be counted as demonstrated PPCS bypass. Residual-enzyme substrate effects or other biological effects remain hypotheses; they require their own evidence rather than being merged with the intact salvage pathway.

## 5. Alternative articles remain separate

Srinivasan 2015 demonstrated extracellular CoA processing to PPanSH, serum stability of that downstream precursor, and restoration of CoA-related cellular phenotypes. This supports a salvage strategy, with experiments spanning several model systems; it is not oral pantethine PK in humans. [S7]

Jeong 2019 compared orally delivered equimolar pantetheine, pantothenate, CoA and PPanSH in Pank2-knockout mice over 14 days. PPanSH at 5 μg/g was the active comparator for a brain gene-expression endpoint; the other three did not normalize that marker. The authors inferred brain delivery from pharmacodynamic rescue rather than presenting a full concentration-time tissue PK bridge. Their disease, endpoint and compound differ from PPCS cardiomyopathy. [S8, Fig6; treatment protocols]

These studies justify tracking PPanSH as a distinct route and checking whether the existing PPCS data support it. They do not justify upgrading pantethine by borrowing PPanSH's stability or replacing the strongest existing cardiac result with a different molecule. The current question is which exact deliverable can reproduce the relevant rescue under clinically plausible exposure—not which related metabolite has the most attractive name.

## 6. Portfolio action and remaining public questions

**Classification:** material-identity discrepancy confirmed; historical vial identity unresolved; culture-to-human exposure bridge unresolved; oral efficacy not refuted by this chemistry audit. This is insufficient for an S-tier, execution-ready label. Retain the candidate as a biologically supported rescue lead while scoring the delivery article independently.

The public evidence needed for an upgrade is concrete:

- A versioned identity chain connecting the actual cell reagent, stock concentration convention and clinically administered formulation.
- Redox-resolved or otherwise validated active-precursor exposure data sufficient to connect oral dosing with the cardiac effect. A vitamin B5 concentration alone is inadequate for the bypass claim.
- Evidence separating direct precursor delivery, microbial conversion and non-bypass mechanisms where those distinctions change product selection.

These are **evidence requirements**, not an instruction to contact anyone or begin experiments. The reviewed public records narrow the uncertainty considerably, but none supplies the complete bridge. Failure to find a public bridge is not proof that no such data exist; it is a reason to keep the qualification status explicit.

## Sources

- **S1.** Sigma 16702, current manufacturer identity: https://www.sigmaaldrich.com/US/en/product/sigma/16702
- **S2.** Sigma/Supelco P2125, current manufacturer identity: https://www.sigmaaldrich.com/US/en/product/sial/p2125
- **S3.** Zhang et al., *Communications Medicine* 2025, DOI 10.1038/s43856-025-01017-z. Institutional full article: https://iris.unibs.it/retrieve/73dc3bf9-28fd-45b1-bcd0-5305f9fa5050/43856_2025_Article_1017.pdf
- **S4.** Wedman et al., *JBC* 2025;301(9):110503, DOI 10.1016/j.jbc.2025.110503. https://pmc.ncbi.nlm.nih.gov/articles/PMC12406275/ ; original PDF https://research-portal.uu.nl/ws/portalfiles/portal/271138401/PIIS0021925825023531.pdf
- **S5.** Wittwer et al., *JCI* 1985;76:1665–1672, DOI 10.1172/JCI112152. https://jci.org/articles/view/112152 . Original scanned pages independently inspected: https://jci.org/articles/view/112152/scanned-page/1666 ; https://jci.org/articles/view/112152/scanned-page/1667 ; https://jci.org/articles/view/112152/scanned-page/1669
- **S6.** Cao et al., *JEM*, published October 27, 2026;223(11):e20252558, DOI 10.1084/jem.20252558. https://rupress.org/jem/article/223/11/e20252558/283127/Vanin-pantethine-metabolic-axis-shapes-dendritic . Findings used: FigsS3M/S5S and cell-culture / LC-MS methods, not the clinical efficacy claim.
- **S7.** Srinivasan et al., *Nature Chemical Biology* 2015;11:784–792, DOI 10.1038/nchembio.1906. https://pubmed.ncbi.nlm.nih.gov/26322826/ ; institutional PDF https://eriba.umcg.nl/wp-content/uploads/2017/02/Nollen-2015-10-11-Nat-Chem-Biol..pdf
- **S8.** Jeong et al., *EMBO Molecular Medicine* 2019;11:e10489, DOI 10.15252/emmm.201910489. https://pmc.ncbi.nlm.nih.gov/articles/PMC6895607/
- **S9.** Yu et al., *Molecular Cell* 2022;82:2650–2665.e12, DOI 10.1016/j.molcel.2022.05.006. https://pubmed.ncbi.nlm.nih.gov/35662397/ ; publisher-hosted full PDF https://www.cell.com/article/S1097276522004403/pdf
