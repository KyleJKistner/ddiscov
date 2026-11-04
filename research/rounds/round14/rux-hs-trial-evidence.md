# Ruxolitinib cream in HS: controlled-trial evidence audit

**Round 14 · 4 November 2026 · existing HHD program R6-NL-01.** Trial NCT05635838 / INCB 18424-221. Base publication: `45fd75459d5415697e733197bbf5d6a2b21a210c`. The [structured ledger](rux-hs-trial-evidence.json) records endpoint values, population labels, source access and analysis-plan locators.

## Decision-relevant result

**The same-strength cream has controlled lesion-count evidence in HS, without demonstrated pain or itch superiority.** Newly recovered official results resolve exact displayed endpoint denominators, uncertainty and participant flow. They strengthen the reason to measure the intended patient-important benefit independently. They provide no new HHD efficacy or HHD exposure boundary.

The study randomized 69 adults with Hurley I/II HS. Its week-16 results distinguish a lesion-count effect from uncertain symptom effects. All differences below are active minus vehicle; negative change means improvement. The registry calls these least-squares means. [C1, outcome indices 0, 3, 4, 6]

| Week-16 outcome | Active / vehicle LS mean change | Displayed N, active / vehicle | Reported difference, 95% CI | P |
|---|---:|---:|---:|---:|
| AN count, primary | −3.61 / −2.42 | 24 / 32 | −1.20 [−2.21, −0.18] | .0215 |
| Skin Pain NRS | −1.90 / −2.09 | 23 / 22 | +0.19 [−1.27, +1.64] | .7982 |
| Itch NRS | −1.45 / −2.39 | 23 / 22 | +0.94 [−0.52, +2.40] | .2031 |
| IHS4 | −3.58 / −2.76 | 24 / 32 | −0.82 [−2.20, +0.56] | .2387 |

The primary difference is the reported −1.20, not subtraction of rounded group means. Symptom point estimates favor vehicle, but their intervals include benefit and disadvantage. They establish neither treatment-caused worsening nor equivalence. The study does not demonstrate pain or itch superiority; it also does not rule out a useful benefit. No clinically important HHD threshold is imported from these intervals.

The March 2024 sponsor release reports different symptom changes: pain −1.85/−2.61 and itch −1.42/−2.75, without identifying their exact estimator; IHS4 is labelled mean change −4.46/−2.66. These figures remain separate from the registry's adjusted results. The sponsor's low-baseline-symptom explanation is not resolved: exact baseline pain, itch and BSA distributions are absent from the recovered results. [R1; C1]

## Denominators, participant flow and missing data

The official registry displays N=24/32 for AN change, AN50/75/90/100, HiSCR, IHS4 and AN change within baseline-affected areas; pain and itch each display N=23/22. It describes efficacy analysis as ITT restricted to available observations. **These displayed endpoint Ns do not establish how many participants or visits contributed to the longitudinal models.** No all-randomized responder denominator or missing-equals-nonresponse analysis is verified. [C1, outcome indices 0–6]

AN50/75/90/100 percentages are 79.2/56.3, 54.2/25.0, 20.8/12.5 and 20.8/12.5. HiSCR is 79.2/50.0. Their explicit registry denominators are 24/32; response numerators are not supplied and are not reconstructed. The sponsor labels the AN percentages on-treatment; its HiSCR sentence does not carry that label. Registry population information is sourced independently, not borrowed from adjacent wording. [C1; R1]

| Participant flow | Active-origin group | Vehicle-origin group |
|---|---:|---:|
| Controlled-period starters | 34 | 35 |
| Controlled-period completed / not completed | 24 / 10 | 32 / 3 |
| Open-label extension starters | 24 | 32 |
| Extension completed / not completed | 21 / 3 | 24 / 8 |

Controlled-period noncompletion reasons were adverse event 2/0; lost to follow-up 5/1; physician decision 0/1; protocol violation 1/0; participant withdrawal 1/0; presence of disease tunnel 1/0; and developed draining fistula 0/1. These totals are directly reported. They do not identify which missing diary scores arose from which reason. Baseline demographics were also uneven: White/Caucasian 19/34 versus 12/35, Black/African-American 11/34 versus 18/35, and Hispanic/Latino 7/34 versus 1/35. Those differences are descriptive and do not establish a causal explanation for the treatment estimate. [C1, participant flow and baseline modules]

Attrition was therefore greater in the active arm, while symptom endpoint availability followed a different pattern from lesion availability. Available-data reporting plus a planned ITT definition does not demonstrate robustness to informative missingness. Exact daily missingness, full model-contributing counts, implemented imputation and missing-not-at-random sensitivity results remain unrecovered.

## What the official analysis plan establishes

The original SAP is dated **12 September 2023**, based on the **19 August 2022 protocol**. It has 42 PDF pages including its cover; printed page plus one gives physical page. Registry document metadata records upload on 4 October 2024. A dated document and later upload do not establish finalization before database lock or prospective public posting. [A1; C1 document metadata]

| Planned feature | Source location, printed pages | Interpretation boundary |
|---|---|---|
| ITT includes all randomized; safety includes participants who applied treatment | §§5.2–5.3, pp14–15 | Definition and empirical endpoint availability are separate |
| Primary AN analysis uses MMRM with treatment, baseline AN stratum, visit and treatment-by-visit terms; unstructured covariance | §7.3.1/Table 3, p24 | Plan intends inclusion despite missing week-16 observations or discontinuation; full contributing counts remain unknown |
| Two-sided primary alpha .10; approximately 60 planned without a formal power calculation | §§3.2–3.3, pp10–11 | Exploratory planning; P=.0215 also falls below .05 |
| Visit-level pain/itch uses seven preceding diary days; at least four missing days make the visit score missing | §§7.2.4.1–2, pp20–21 | Score construction does not supply a complete missing-outcome strategy |
| Secondary continuous outcomes may use analogous MMRM; categorical summaries include counts and percentages | §§7.4.1–2, pp25–26 | Public visible text does not establish a categorical imputation or sensitivity algorithm |

**The registry's continuous-outcome descriptions name MMRM, but its statistical-method fields say ANCOVA.** Its analysis comments include treatment, AN stratum, visit and treatment-by-visit terms. The audit preserves this mismatch rather than silently choosing a method. Registry-reported estimates can be transcribed without claiming independent reconstruction or complete SAP compliance. [C1, outcome indices 0, 2, 3, 4, 6]

Rendered printed SAP pages 24–26 were independently inspected. Black redaction blocks are visible on pages 24 and 26; contents remain unknown and no recovery was attempted. No explicit MAR/MNAR assumption, endpoint-specific imputation algorithm or missing-outcome sensitivity result was recovered from visible material. A model's name does not establish those details. [A1]

## Safety, extension and applicability

Controlled-period safety, through week 16 plus 30 days, reports any TEAE in **13/34 active versus 15/35 vehicle** and grade ≥3 TEAEs in **0/34 versus 2/35**. The sponsor gives corresponding any-TEAE percentages 38.2%/42.9% and TEAE-related discontinuations 2/0. Those discontinuations do not equal total trial noncompletion. [C1, outcomes 7–8; R1]

The extension adds **16 weeks, through week 32**, with all entrants receiving active cream and entry conditional on completion/safety; the SAP also specifies compliance. The indexed journal abstract describes as-needed use. Extension TEAEs occurred in 8/24 active-origin and 15/32 vehicle-origin entrants; grade ≥3 TEAEs were 0/24 and 3/32, through week 32 plus 30 days. Both groups then receive active treatment, so these are not continued randomized active-versus-vehicle contrasts. [A1 pp10–12; C1, outcomes 9–10; J1]

The separate registry adverse-event module pools active exposure from original active recipients and crossover recipients: serious events affected **2/66** active-exposed participants, compared with **1/35** during vehicle exposure. Crossover participants can appear in both exposure groups, and exposure windows differ. This is not a randomized safety comparison and does not contradict the sponsor's earlier controlled-period statement of no serious TEAE in the active arm. Neither small dataset excludes rare risk or establishes safety on HHD erosions. [C1, adverse-event module; R1]

Eligibility includes adults, Hurley I/II HS, 3–10 ANs, no draining tunnels and pain **or** itch NRS ≥1. Indexed primary Methods additionally report affected BSA ≤20%; these are eligibility limits, not observed baseline distributions. The registry baseline tables provide demographics, not exact symptom or BSA distributions. No measured HS plasma PK was recovered. [C1; J2]

## Implication for the leading HHD program

Retain the controlled clinical-proof direction. Keep erosion/lesion outcomes, pain, rescue and treatment burden independently interpretable, with a baseline range capable of evaluating the intended claim. Lesion improvement alone cannot establish pain benefit. The new attrition and endpoint-availability evidence also makes missing-data interpretation material to a persuasive symptom claim. These are audit inferences, not an HHD efficacy prediction, an instruction to require superiority on every secondary outcome, or an HHD effect-size/sample-size calculation. The existing HHD proof specification remains the controlling portfolio plan. [B1]

## Source scope and closeout

- **C1:** [Official ClinicalTrials.gov record API](https://clinicaltrials.gov/api/v2/studies/NCT05635838). Exact downloaded JSON read, including all 11 posted outcome objects, participant flow, baseline characteristics and adverse-event modules. Results first and last posted 1 November 2024. The earlier retrieval-tool failure was resolved by an ordinary download. Exact bytes/hash are in the structured ledger.
- **A1:** [Official SAP](https://cdn.clinicaltrials.gov/large-docs/38/NCT05635838/SAP_001.pdf). Visible text and three key rendered pages inspected; planned methods. Exact PDF hash is in the ledger.
- **R1:** [Incyte release, 10 March 2024](https://investor.incyte.com/news-releases/news-release-details/incyte-announces-new-data-phase-2-study-evaluating-ruxolitinib). Primary sponsor reporting of the same trial.
- **J1:** [Indexed journal abstract, PMID 41248765](https://pubmed.ncbi.nlm.nih.gov/41248765/). Indexed primary passages; direct PubMed rendering incomplete.
- **J2:** [Primary publisher article](https://www.sciencedirect.com/science/article/pii/S0190962225032359). Indexed Methods passage; direct full article returned 403. No full-paper or supplement audit claimed.
- **P1:** [Official protocol](https://cdn.clinicaltrials.gov/large-docs/38/NCT05635838/Prot_000.pdf). Link and document metadata verified; full protocol not independently read.
- **B1:** Preserved [Round 7 HHD development proof](../round7/rux_hhd_development_proof.md).

One trial is represented across the registry, release and journal report; these are not independent replications. Close this bounded pass with the remaining missing-data, baseline, full-manuscript and PK gaps explicit. No poster, Mendeley supplement or individual-participant dataset was read. The closed BLU claim-mapping, zinc, SLC6A6 and HHD model-supplement searches were not reopened. No outreach, purchases, recruitment, experiments, simulations or material receipt occurred.
