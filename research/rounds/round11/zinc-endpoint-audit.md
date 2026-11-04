# Round 11 — zinc pilot endpoint populations and missing-data audit

**Result: the published missing-data rule is recovered; the seven general secondary outcomes' exact visit and paired-analysis counts remain unresolved.** The full primary manuscript became readable in this sprint. It describes available-case analysis, with paired tests using participants observed at both relevant visits. It does not provide those outcome-specific counts in the accessible main text. The supplementary appendix and protocol remain inaccessible through the bounded public routes checked.

**Decision:** retain **R10-NL-02**, zinc acetate dihydrate/GNAO1-related disorder, as a conditional clinical-research reserve with the independent asset thesis on hold. No dedicated allocation or efficacy promotion follows. Baseline: `a66f2462541893b4dfb88b4f9aaa0d7863c204a8`; evidence review: 4 November 2026. This is an existing-use update. The [Round 10 screen](../round10/new-candidate-screen.md) remains unchanged, and the [structured audit](zinc-endpoint-audit.json) records every unresolved count as null.

## 1. What the primary Methods now establish

ZINCGNAO1 assessed participants at baseline, day 90 and day 180, with additional virtual safety/post-withdrawal visits. Its statistical section states that no formal missing-data method was applied: descriptive analyses used available observations, while each paired comparison required observations at both relevant times. There is no reported imputation algorithm in the inspected main text. This is not a statement that all enrolled or all modified-analysis participants supplied every measurement. [Z11-S1, Study design; Statistical analysis]

For changes, the authors describe paired t-tests or Wilcoxon signed-rank tests after an exploratory distribution check using Shapiro–Wilk and Q–Q plots. They also report post-hoc Wilcoxon sensitivity analyses. P values are two-sided, nominal and unadjusted for multiplicity. The main text reports no prespecified sensitivity analysis and no confirmatory outcome hierarchy. The exact test assignment and effective N for each comparison remain unverified because the relevant supplementary tables were not recovered. [Z11-S1, Statistical analysis; Results]

The manuscript calls primary and secondary analyses prespecified, with secondary outcomes exploratory. This audit attributes that statement to the publication; it does not claim an independent review of the protocol or original statistical analysis plan. The post-hoc cerebral-palsy comparisons and revision-added GNAO1 severity analysis are separately identified.

## 2. Equal set sizes conceal different people

| Population or endpoint | Published count | Membership or denominator rule |
|---|---:|---|
| Screened | 16 | Screening population |
| Full analysis set, FAS | 13 | All enrolled participants, P1–P13 |
| Safety analysis set | 12 | At least one zinc dose; excludes P8, includes P3 |
| Modified full analysis set, mFAS | 12 | Excludes P3 after an unrelated serious adverse event; retains P8 |
| Completed six-month trial | 11 | P3 and P8 discontinued |
| FAS feasibility | 11/13, 84.6% | Adherence criterion, not efficacy response; reported 95% CI 54.6–98.1% |
| mFAS feasibility | 10/12, 83.3% | Same endpoint after excluding P3; reported Clopper–Pearson 95% CI 51.6–97.9% |
| GMFM reference-trajectory subset | 8 | Ages 2–18 with complete baseline and six-month GMFM-66 measurements |

Sources: Z11-S1, Statistical analysis, Figure 1, Results and Figure 3; Z11-S2 independently carries the flowchart and figure captions.

**P3** received treatment, then withdrew following a serious adverse event the authors considered unrelated to treatment. The report describes adherence of 80% before that event. **P8** refused administration after swallowing and taste difficulties and never received a dose; the authors classified treatment as not feasible for her. Exact secondary-outcome visit availability for either person is not recoverable from the accessible main text. [Z11-S1, Results]

The FAS-to-mFAS change removes one feasible person as well as one participant. Given the stated exclusion of P3 alone, **P3's inclusion in the FAS feasibility numerator follows from the reported set definitions and counts**. This is a transparent inference, not a newly observed patient-level record. Likewise, the ten feasible people in the mFAS cannot equal all eleven completers. The other feasibility failure's study identifier remains unresolved. The repeated number eleven must not merge completion with adherence success.

The two twelve-person sets also answer different questions. P3 contributes to exposed safety accounting but is removed from the mFAS; P8 belongs to the mFAS but was never exposed. Neither set label establishes how many complete observations entered a particular secondary-outcome test.

## 3. Endpoint count ledger

The main text assigns secondary outcomes to the mFAS, but the available-case rule requires a second level of accounting. Each visit needs an observed N; each paired comparison needs the number with both measurements. The following counts remain **unknown**, rather than being filled with 12 or 11.

| Secondary outcome | Observed N at days 0 / 90 / 180 | Paired N, 0–90 / 0–180 | Reported main-text result retained |
|---|---|---|---|
| GMFM-66 | Unknown / unknown / unknown | Unknown / unknown | Mean (SD): 33.1 (12.8), 35.0 (13.8), 37.8 (12.8); nominal baseline-to-six-month P=.006 |
| COPM performance | Unknown / unknown / unknown | Unknown / unknown | Mean (SD) 2.6 (0.8) at baseline and 3.8 (1.3) at six months; nominal P=.003 |
| COPM satisfaction | Unknown / unknown / unknown | Unknown / unknown | Mean (SD) 2.7 (0.9) at baseline and 4.1 (1.7) at six months; nominal P=.002 |
| BFMDRS movement | Unknown / unknown / unknown | Unknown / unknown | Blinded ratings; means 57.8, 54.3 and 54.3; no clear change reported |
| BFMDRS disability | Unknown / unknown / unknown | Unknown / unknown | Unblinded ratings; means 25.5, 24.2 and 23.5; nominal baseline-to-six-month P=.005 |
| AIMS | Unknown / unknown / unknown | Unknown / unknown | No clear change reported; no unverified plot values extracted |
| CPCHILD | Unknown / unknown / unknown | Unknown / unknown | No clear change reported; no unverified plot values extracted |

Source: Z11-S1, Statistical analysis, Results and Figure 2. These are queried count slots, not a claim that every listed comparison was reported. The JSON separately records whether a result for a particular pair was identified.

The 33.1→37.8 GMFM summaries must not automatically become a **4.7-point mean within-person change**. With available-case summaries, that equality requires matching contributors, which the accessible record does not establish. No observations were imputed, reconstructed from plotted dots, or back-calculated from P values in this audit. The publication's own paired result remains a reported result whose exact contributing N could not be independently reconstructed.

The eight-person GMFM reference subset has an explicit complete-pair definition. That known count does not fill the seven general endpoint rows. The manuscript also describes a separate post-hoc propensity-score comparison against dyskinetic cerebral palsy. It identifies age, baseline GMFM-66, weight and height as matching variables and reports a contrast in mean changes; the achieved matched-group counts, matching ratio/caliper, and balance table are not verified without the appendix. The external disease population remains biologically non-equivalent to GNAO1. [Z11-S1, Statistical analysis; Results; Figure 3]

## 4. What changed, and what remains unchanged

Round 10 already retained the 13 enrolled/12 exposed/11 completed distinction, the eight-person cerebral-palsy reference subset, exploratory functional signals and unchanged blinded movement severity. This sprint resolves the **analysis rule**, identifies **P3/P8's different set memberships**, and adds the **10/12 mFAS feasibility result** and the published distinction between the two post-hoc cerebral-palsy comparisons.

Available-case reporting does not establish that missingness was random, balanced or harmless. Requiring complete pairs prevents a one-visit observation from entering that pair's change test, but does not address why a participant lacks an observation. Excluding an unrelated-event withdrawal may also change the population being described. None of these observations proves that the reported functional changes are false; they prevent greater precision or causal certainty than the recovered data warrant.

The strongest new conclusion is methodological: **the mFAS size is not the effective sample size for every endpoint**. The program still has prospective feasibility evidence and exploratory function signals, with an uncontrolled design, selected participants, uncertain endpoint-level denominators and an unchanged blinded movement result. The reserve and independent asset hold remain appropriate.

## 5. Retrieval ceiling and finite reopening condition

The full PMC primary manuscript was read. The linked **Supplementary Appendix (`mmc1.pdf`)** and **Protocol (`mmc3.pdf`)** returned download shells. Main-paper PDF and figure pages returned CAPTCHA. Publisher fulltext/CDN, EuropePMC XML, older PMC/metadata and institutional-copy routes did not yield a usable appendix. The official ClinicalTrials.gov page yielded a JavaScript shell and its API was inaccessible. Those failures do **not** establish that a registry has no results; `hasResults` remains null. The structured log distinguishes this workstream's attempts from root's complementary checks.

The article identifies Table S2 for sensitivity analyses, Table S3/Figure S1 for patient trajectories, and Supplementary Methods/Table S1 for the external comparison. These are the precise remaining public documents needed. Its data-sharing statement describes controlled future access to individual data and scripts and does not offer public individual-level data. No request was made. [Z11-S1, Results; Data sharing statement; Appendix A]

**Stop this retrieval pass here.** Reopen for an accessible linked appendix/protocol or a public correction/results release that supplies observed visit counts, complete-pair counts, missingness reasons or analysis-set definitions. Do not repeat failed routes or manufacture patient-level data to complete the table. No outreach, purchase, recruitment, experiment, simulation or Git action was performed by this workstream.

## Primary source key

- **Z11-S1:** Thiel et al. [Safety and feasibility of oral zinc for patients with GNAO1-related disorders (ZINCGNAO1)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13427569/). *eClinicalMedicine* 98 (2026), 104092. DOI [10.1016/j.eclinm.2026.104092](https://doi.org/10.1016/j.eclinm.2026.104092). Full primary HTML text read; Methods/Results locators and access ceilings are in the JSON. The article is marked CC BY.
- **Z11-S2:** [PubMed primary abstract and original figure captions, PMID 42542632](https://pubmed.ncbi.nlm.nih.gov/42542632/). Same report as Z11-S1, not an independent cohort.
- **Z11-S3:** [Linked Supplementary Appendix](https://pmc.ncbi.nlm.nih.gov/articles/instance/13427569/bin/mmc1.pdf). Identified but not read.
- **Z11-S4:** [Linked Protocol](https://pmc.ncbi.nlm.nih.gov/articles/instance/13427569/bin/mmc3.pdf). Identified but not read.
- **Z11-S5:** [Official study record NCT06412653](https://clinicaltrials.gov/study/NCT06412653). Content/history/results not independently recovered; registration identity is supported by the publication.
