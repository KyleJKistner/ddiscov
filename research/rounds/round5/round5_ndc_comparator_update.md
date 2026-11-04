# Round 5: NDC-9009 / Darier comparator update

**As of 4 November 2026. Existing-candidate update only: R3-NL-01 (NDC-9009) and R3-NL-02 (dantrolene). Zero new leads; no S-tier promotion.**

## Decision

**The actual public dantrolene trial results have been recovered.** They establish a limited positive clinical signal among completers, with substantial nonresponse attrition. Dantrolene therefore becomes an adult clinical benchmark for the NDC program, while remaining an unproven treatment for durable barrier restoration. NDC stays on conditional local qualification priority; the new evidence raises the comparative bar without establishing either drug's superiority.

The earlier statement that the dantrolene result tables remained unread is superseded. The official CTIS public document endpoint returned the submitted PDF. [S1–S4]

## 1. Exact source and status

CTIS **2024-519201-36-00**, previously EudraCT **2020-004281-19**, lists result notification **SUM-151495**. Its official JSON marks the submission as final and submitted on **10 September 2026**. The downloaded English PDF is version 2.0 dated 8 September 2026, internally labelled a draft incorporating sponsor review, and contains a digital signature dated 10 September. The Swedish lay summary also retains a draft label and reviewer instructions. These are **public sponsor-submitted results**, not a verified peer-reviewed clinical-trial article. The lay summary identifies the scientific article only as a manuscript. [S1–S4]

The official endpoint resolves to a temporary public S3 download URL; the stable resolver and document UUID are recorded below. The English PDF is 481,600 bytes, SHA256 `8cc599c0f33308d66f03e337272238433ad85afee9ce860add2329d12fba996c`. The Swedish PDF is 229,483 bytes, SHA256 `cefebff04a12a826e24682b7e462810778bf5fd4254233806d72d1cff38274d6`. English outcome and safety tables were also visually checked on PDF pages 8–9 and 11–12. [S2–S3]

## 2. What was actually tested

| Item | Verified result-document information |
|---|---|
| Product and route | Oral dantrolene sodium, Dantrium hard capsules; CTIS product is 25 mg capsules. This was not a topical trial. |
| Regimen | Target 100 mg/day, reached by a four-week titration from 25 mg once daily to 50 mg twice daily; six months of treatment. Achieved plasma or epidermal exposure was not reported. |
| Design | Single center, open label, nonrandomized, one arm; comparison with each participant's baseline, no concurrent active or placebo group. |
| Actual denominator | 19 screened; 3 screen failures; **16 started**. Ages 23–74; 10 women and 6 men. Planned enrollment of 20 was not reached. |
| Completion and analysis | **10 completed and supplied the primary paired analysis**; 2 stopped after month 1 and 4 after month 3. Discontinuers were not subsequently assessed. This is an available-case analysis, not intention-to-treat. |
| Nonresponse | The summary says the manuscript flow diagram assigns insufficient response to all six discontinuations; surrounding prose says “most commonly.” Preserve that discrepancy. Six of sixteen is 37.5% attrition; ten completers are not ten verified responders. |
| Prior and concomitant therapy | 12 previously used acitretin and 1 isotretinoin; these 13 underwent three-month washout. Short topical steroid courses, emollients and treatment of intercurrent infections were permitted. |
| Dates | First participant enrolled 15 September 2023; CTIS transition 7 November 2024; last visit/global end 10 September 2025. The CTIS transition date is not the first enrollment date. |

Sources: official CTIS record and submitted English/Swedish summaries. [S1–S3]

The old EudraCT page describes planned enrollment of 14 and an EASI primary outcome, whereas the transitioned record and submitted analysis identify PGA as primary and 20 planned participants. Those old fields must not be substituted for the conducted analysis. The submitted summary identifies protocol version 1.6, dated 5 June 2023, and describes a change from the earlier randomized/blinded proposal before first enrollment. The underlying manuscript, full statistical analysis plan and participant-level data were not recovered. [S1–S2,S5]

## 3. Clinical signal and limits

The reported paired comparisons use the **10 participants with both baseline and six-month data**. Positive differences below indicate improvement. The table reproduces the reported estimates, not an independent reanalysis. [S2]

| Endpoint | Reported paired result | Interpretation |
|---|---|---|
| PGA, primary | Median score 3 to 2; Hodges–Lehmann difference 1.5, 95% CI 1.0–1.5; p = .02 | A clinical severity signal in completers; no controlled causal estimate. The reported one-point clinical threshold was not validated specifically for Darier disease. |
| DLQI | Median score 10.5 to 3.5; paired estimate 4.8, 95% CI 1.5–14.5; p = .01 | Patient-reported quality-of-life signal; exploratory secondary analysis. |
| EASI | Paired estimate 3.6, 95% CI −2.4–18.4; p = .13 | Imprecise; no statistically demonstrated effect on this complementary severity measure. |
| Affected body surface area | Paired estimate 4.0 percentage points, 95% CI −0.5–24.0; p = .10 | Imprecise; no statistically demonstrated extent reduction. |

Mood and treatment-satisfaction comparisons were also nonsignificant. The visit means use changing denominators—16 at baseline, 14 at month 3, 10 at month 6—and should not be interpreted as longitudinal results for all 16. No post hoc responder rate can be reconstructed from these aggregate data. [S2]

Three issues materially lower the evidential weight:

1. **Selective completion.** The six people who stopped for inadequate benefit are absent from the paired efficacy estimate. The direction of this selection favors apparent efficacy. The available summary cannot repair that bias.
2. **Retinoid withdrawal and return.** Disease worsened between screening and the post-washout baseline. At the nine-month visit, six of ten assessed participants had restarted retinoids. Further improvement at that visit is not evidence that dantrolene repaired skin durably after withdrawal. A short drug half-life alone cannot exclude lasting biological effects, but co-treatment and lack of a control make such a claim unidentifiable here.
3. **Outcome mismatch with the restoration thesis.** Clinical lesion ratings and quality of life matter, but this report contains no treatment result for TEWL, permeability, mechanical strength or another direct barrier-function measure. Biopsies were collected, yet the summary explicitly says their exploratory histological/molecular results are unreported. [S2–S3]

This is neither a definitive clinical failure nor a robust efficacy confirmation. It modestly supports pharmacological tractability of adult Darier disease while giving a concrete reason to demand better function, retention and comparative value from an NDC development program.

## 4. Safety: report the observed denominator and missing information

All **16 exposed participants** form the safety population. The summary reports **17 events**, comprising 3 serious and 14 nonserious events. These are occurrence counts, not 17 affected people; the number of unique patients with repeated infections is not supplied. [S2]

| Reported event | Number of events | Timing / interpretation |
|---|---:|---|
| Bacterial skin infection | 9 | One serious event occurred during washout, before dantrolene. Eight were nonserious; infections continued during treatment. Nine events divided by 16 must not be presented as a verified 56.3% patient incidence. |
| Upper respiratory infection | 2 | Nonserious; unique-patient count not stated. |
| Pneumonia | 1 | Serious; explicitly predose during washout. |
| Elective gynecological surgery | 1 | Serious by hospitalization, investigator-assessed unrelated. Do not duplicate it with the alternative term used in the safety record. |
| Laryngitis, amenorrhoea, sinusitis, hiatal hernia | 1 each | Nonserious. |

No deaths, suspected unexpected serious adverse reactions, or adverse-event discontinuations were reported. The summary reports no clinically significant laboratory abnormality and no hepatotoxicity; it supplies no numeric ALT/AST trajectory or exposure-response analysis. Baseline liver disease/abnormal chemistry and several relevant comorbidities or interacting drugs were excluded. [S2–S3]

**Absence of recorded muscle toxicity is not a strong negative finding.** Mild expected adverse effects such as tiredness were deliberately excluded from recording. Creatine kinase and other muscle enzymes were not in the laboratory panel, and no quantified muscle-function assessment is supplied. This leaves tolerability incompletely characterized even though no treatment-related serious event was assigned.

The uploaded summaries contain a causality inconsistency: their narrative speculates that dantrolene could contribute to pneumonia, while the event table places the only pneumonia before the first dose. Preserve the explicit timing; do not attribute that predose event to study-drug exposure. The documents' instruction to flag an issue to the sponsor is source text, not an instruction for this research project. No message was sent. [S2–S3]

## 5. Has a better direct adult barrier comparator appeared since the NDC paper?

The NDC paper appeared online in early August 2026. This bounded search found **no verified controlled adult-patient pharmacological barrier-restoration result** that resolves its mature-function gate. That is a statement about the recovered evidence, not proof that no such result exists. [S6]

| Evidence | Date and denominator | What it changes |
|---|---|---|
| Dantrolene clinical result upload | September 2026; 16 exposed, 10 paired completers | New adult clinical evidence, as above. No active comparison or direct barrier readout. |
| Dantrolene mitochondrial/MCU paper | Online 8 October 2026; full experimental denominators not recovered | Primary abstract describes patient cells and other models, improved mitochondrial measures and adhesion. It is not the clinical-trial report, and does not establish adult treatment benefit or topical delivery. [S7] |
| Glodjajic et al., Th2/Th17 inflammation in Darier/Hailey–Hailey | Online 9 October 2026 | Publisher's listing reports clinical improvement and partial normalization of barrier **markers** after targeting inflammation. Full text/PDF was not retrievable in this bounded pass; exact drugs, denominators, treatment comparison and any direct barrier assay remain unverified. Do not promote marker normalization into barrier function. [S8] |
| Andersen et al., adult biologic case series | Online 23 June 2026, before NDC; 6 patients, including 2 given ustekinumab | Ustekinumab showed better disease control than the other patients' biologic courses, with concomitant/intensified therapy. The two received 45 mg at weeks 0/4 then every 12 weeks; one had early infectious readmission. This is observational heterogeneity, not a randomized comparative or direct barrier result. [S9] |
| Burle et al., negative/mixed anti-inflammatory series | 22 April 2026, before NDC; 8 adults | One modest responder, two stable, three worsened; two stopped early for adverse events, including hospitalized herpes on upadacitinib. An IL-17-high patient did not respond. These negative outcomes counter selection of favorable cytokine/JAK case reports. [S10] |
| Upadacitinib plus acitretin case | 4 August 2026, immediately before NDC; 1 adult | 15 mg/day upadacitinib plus 20 mg/day acitretin improved symptoms/lesions and DLQI, followed by retinoid discontinuation. No concurrent control or direct barrier measure; combination contribution unresolved. [S11] |

The June/April/August reports are comparator context newly checked in this pass, not discoveries after NDC and not additional candidate counts. Disease symptoms, molecular barrier markers and mechanical/permeability function remain distinct evidence tiers. A keratinocyte-only model may not validly test immune-directed biologics; do not interpret their failure in such a model as a clinical comparison.

## 6. Resulting go/stop rule for NDC

**Go only to qualification of an exact local product and a mature functional model.** Dantrolene should now be included as a mechanistically distinct benchmark wherever matched exposure and model biology make the comparison interpretable. A practical retinoid/current-care comparator should be evaluated in a model that can capture its effect. NDC must still establish identity, dissolved/free concentration, viable epidermal delivery, delayed rescue of a stable adult-relevant adhesion/permeability deficit and a tolerable local/systemic exposure margin.

**Stop advancement beyond qualification** if NDC improves only differentiation timing/markers, cannot reach a functional concentration without injury, or provides no meaningful advantage over an obtainable comparator. Its proposed advantage could be a better local therapeutic margin or superior durable barrier rescue; neither follows from the oral dantrolene results. Dantrolene's human signal gives no measured topical formulation, epidermal PK, safety margin, or NDC efficacy by analogy.

The process improvement is concrete: resolve public result documents before ranking a comparator by trial status, track nonresponders through the analysis denominator, and separate clinical lesion improvement from barrier restoration. The current source gap was solvable through ordinary public records.

## Sources and retrieval record

- **S1 — Official CTIS record:** https://euclinicaltrials.eu/ctis-public/view/2024-519201-36-00 ; structured public record: https://euclinicaltrials.eu/ctis-public-api/retrieve/2024-519201-36-00 . Retrieved without authentication using ordinary HTTPS. Metadata includes the exact document UUIDs and final-submission flags.
- **S2 — English sponsor result PDF, v2.0, 8 September 2026:** https://euclinicaltrials.eu/ctis-public-api/documents/2024-519201-36-00/0c63f05c-80f0-4f3a-a9ec-58c143fb1a40/download . This resolver returns a temporary URL.
- **S3 — Swedish lay summary PDF, v2.0, 8 September 2026:** https://euclinicaltrials.eu/ctis-public-api/documents/2024-519201-36-00/762ac81a-b09d-49ad-95f7-db0895f88eed/download .
- **S4 — Public frontend documenting ordinary API route:** https://euclinicaltrials.eu/ctis-public/main-XRBOMS6O.js ; view module https://euclinicaltrials.eu/ctis-public/chunk-NI4HHJ4V.js ; connector https://euclinicaltrials.eu/ctis-public/chunk-TT6KNQDE.js . `getDocument` uses `/ctis-public-api/documents/{trial}/{uuid}/download`. No endpoint enumeration, credentials, sign-in, or access-control bypass was used.
- **S5 — Older official EudraCT record:** https://www.clinicaltrialsregister.eu/ctr-search/trial/2020-004281-19/SE . Its results section is empty because the trial transitioned; use S1–S3 for actual outcomes.
- **S6 — NDC/Darier paper:** DOI 10.1126/sciadv.aee1599; https://pubmed.ncbi.nlm.nih.gov/42555718/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC13440392/ . Prior-round full analysis is retained; this pass confirmed publication timing, not a new extraction of its experiments.
- **S7 — Dantrolene mitochondrial study:** DOI 10.1016/j.jid.2026.08.031; https://pubmed.ncbi.nlm.nih.gov/42849607/ ; https://www.sciencedirect.com/science/article/pii/S0022202X26037681 . Abstract only in this pass.
- **S8 — October Th2/Th17 paper:** DOI 10.1002/jvc2.70463; https://onlinelibrary.wiley.com/doi/10.1002/jvc2.70463 ; primary publisher listing https://onlinelibrary.wiley.com/toc/27686566/0/0 . Ordinary PDF request returned HTTP 403; no repeated bypass attempts. Exact treatment/method details remain unresolved.
- **S9 — Adult biologic series:** DOI 10.1093/skinhd/vzag072; https://academic.oup.com/skinhd/article/6/4/593/8713716 ; https://pubmed.ncbi.nlm.nih.gov/42539885/ . Public indexed primary article text and abstract reviewed; no controlled efficacy claim.
- **S10 — Negative adult series:** DOI 10.2340/actadv.v106.adv-2026-0322; https://medicaljournalssweden.se/actadv/article/download/46003/53637?inline=1 . Full primary HTML reviewed.
- **S11 — Upadacitinib/acitretin case:** DOI 10.2340/actadv.v106.adv-2026-0662; https://pmc.ncbi.nlm.nih.gov/articles/PMC13434539/ ; https://pubmed.ncbi.nlm.nih.gov/42549604/ . Primary indexed case text reviewed; no controlled functional endpoint.

No outreach, procurement, laboratory work, browser session or remote repository mutation was performed. This report and accompanying JSON are for integration into the existing-candidate record.
