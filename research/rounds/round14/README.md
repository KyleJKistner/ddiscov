# Round 14 — controlled HS evidence and the HHD development claim

**4 November 2026. Completed bounded desk-research sprint for existing program R6-NL-01.** Base publication: [`45fd75459d5415697e733197bbf5d6a2b21a210c`](https://github.com/KyleJKistner/ddiscov/commit/45fd75459d5415697e733197bbf5d6a2b21a210c). Target branch: `main`.

## Outcome

**Retain ruxolitinib 1.5% cream/HHD at rank 3 and 10 planning points.** The sprint recovers complete official results and visible analysis-plan methods for NCT05635838, a randomized trial in hidradenitis suppurativa (HS). The primary lesion-count result is positive. Pain and itch superiority are unestablished, and previously unresolved endpoint counts, withdrawal and safety periods are now explicit. HS supplies no new Hailey–Hailey disease (HHD) effect estimate or exposure margin. [Evidence audit](rux-hs-trial-evidence.md) · [Claim decision](hhd-clinical-claim-amendment.md)

| Recovered field | Active / vehicle, unless otherwise specified |
|---|---|
| Controlled-period randomized / completed / not completed | 34/35; 24/32; 10/3 |
| Lesion endpoint displayed N | 24/32 |
| Pain and itch displayed N | 23/22 |
| Reported primary AN difference, 95% CI | −1.20, −2.21 to −0.18; P=.0215 |
| Pain difference, 95% CI | +0.19, −1.27 to +1.64; P=.7982 |
| Itch difference, 95% CI | +0.94, −0.52 to +2.40; P=.2031 |
| Controlled-period any TEAE / grade ≥3 TEAE counts | 13/34 versus 15/35; 0/34 versus 2/35 |
| Extension any TEAE / grade ≥3 TEAE counts | Continuing active 8/24 versus crossover 15/32; 0/24 versus 3/32; both groups active |

Source: [official trial results](https://clinicaltrials.gov/api/v2/studies/NCT05635838), with module and outcome locators in the [structured ledger](rux-hs-trial-evidence.json). Differences are active minus vehicle. Displayed endpoint Ns are not verified total longitudinal-model contributor Ns. Uncertain symptoms establish neither harm nor equivalence. Grade ≥3 severity and serious-event status differ.

## What changes in the program decision

Seven explicit claim decisions now distinguish visible disease improvement, painful disease/burden, benefit across assigned patients, relevant-care comparison, maintenance, safety and advancement. Existing Round 7 requirements for controlled evidence and useful patient benefit were already present. The new contribution is exact source reconciliation and a claim map informed by actual denominators and uncertainty, not a new clinical protocol.

The registry describes MMRM but labels its structured statistical method ANCOVA. Sponsor symptom/IHS4 changes differ from the registry LS means. The audit preserves those differences without inventing their explanation. The visible SAP supplies an all-randomized primary analysis plan and a weekly diary rule; neither proves implemented missingness robustness. The selected all-active extension does not estimate a contemporaneous vehicle-controlled maintenance effect. Pooled active safety includes crossover recipients and cannot be compared with vehicle as independent randomized arms. [Detailed decision and limits](hhd-clinical-claim-amendment.md)

No HHD response probability, threshold, sample size, duration or safety boundary is imported. The exact marketed-article proof, matched-vehicle or whole-product add-on alternatives, relevant background care, exposure assessment and optional-model limits remain. The 100-point allocation queue is identical to Round 13.

## Selection and stopping boundary

The user-closed BLU claim-mapping, zinc, SLC6A6 and HHD supplement lanes were excluded. Bounded leading-program triage found no actionable new primary delta in the reviewed DYN101/PIK3C2B or enasidenib routes. The HS question was selected because readable controlled exact-cream evidence could resolve a concrete patient-benefit interpretation for a leading clinical program. It was not an exhaustive new portfolio screen.

The full journal paper/supplement, complete implemented model populations, missing-data sensitivity analyses, exact baseline symptom distributions and measured HS plasma exposure remain unrecovered. No counts were back-solved from percentages; no analysis was fit or simulated. Close this retrieval pass until substantive primary results or a correction can change the claim or its interpretation. Other unresolved development questions remain available for later bounded sprints.

## Package

| File | Purpose |
|---|---|
| [rux-hs-trial-evidence.md](rux-hs-trial-evidence.md) | Readable trial, denominator, missingness and safety audit |
| [rux-hs-trial-evidence.json](rux-hs-trial-evidence.json) | 17 result records, six planned-analysis records, source locations and exact source-file hashes |
| [hhd-clinical-claim-amendment.md](hhd-clinical-claim-amendment.md) | Seven claim decisions and their HHD implications |
| [hhd-clinical-claim-amendment.json](hhd-clinical-claim-amendment.json) | Structured decisions, retained assumptions and source-specific quantities |
| [independent-trial-methods-review.json](independent-trial-methods-review.json) | Independent source/method review bound to the two evidence files by hashes |
| [independent-clinical-decision-review.json](independent-clinical-decision-review.json) | Independent decision challenge bound to the two decision files by hashes |
| [integration-review.md](integration-review.md) | Integration, preserved decisions and review resolution |
| [round14-root-deltas.json](round14-root-deltas.json) | Current-round scope, counts, updates and closed retrieval lanes |
| [local-verification.json](local-verification.json) | Deterministic preservation and content checks |
| [artifact-manifest.json](artifact-manifest.json) | Complete expected repository paths and content hashes |

This README completes the eleven-file package. The registry, sponsor release and article represent **one cohort of 69 people with HS**. Zero new HHD-treated people, screens, molecules or experimental results are counted. Two independent reviews cover four authored files. All 622 original coverage rows and all earlier round packages are retained.

Publication verification checks the expected `main` head, new commit parent/tree, complete committed paths and exact manifest content. The containing commit identifies this publication; the manifest binds other files by content hashes and is itself bound by its Git tree entry. No outreach, purchases, recruitment, experiments, simulations or material receipt occurred.
