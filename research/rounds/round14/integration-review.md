# Round 14 integration review

**4 November 2026. Base: `45fd75459d5415697e733197bbf5d6a2b21a210c`; target: `main`.**

## Integrated decision

The [evidence audit](rux-hs-trial-evidence.md) and [claim amendment](hhd-clinical-claim-amendment.md) update one existing leader, R6-NL-01. Rank 3 and 10 planning points remain. A different-disease randomized trial can improve the quality of the HHD decision without establishing HHD efficacy: the recovered primary lesion-count result, uncertain symptoms, differential withdrawal, endpoint-specific availability and phase-specific safety define what the evidence can support.

The new results are recovered published observations, not newly generated data. The registry, release and journal abstract are one HS cohort. The original five selected exact-strength HHD reports and unpooled nine-patient preprint scope remain unchanged. No new molecule, screen, HHD-treated person or S-tier promotion is counted.

## Source and review reconciliation

The initial public summaries did not resolve actual endpoint counts. An ordinary download of the official ClinicalTrials.gov JSON resolved those fields, participant flow, uncertainty and safety periods. The final files replace the preliminary unknown-count draft with directly reported values. Raw JSON and the official SAP were checked against exact bytes and SHA256; selected visible SAP pages were rendered and viewed. The PDF contains redactions, which were not recovered.

The [independent methods review](independent-trial-methods-review.json) checks the evidence files against the registry and SAP. The [independent decision review](independent-clinical-decision-review.json) challenges transfer into HHD. Both reviews bind their final reviewed inputs by bytes and SHA256. Remaining evidentiary limits are recorded, not marked resolved by a review pass:

- Endpoint display Ns do not establish complete longitudinal-model contributors. The registry's MMRM narrative and ANCOVA field remain unreconciled.
- Sponsor symptom/IHS4 quantities and registry LS estimates are distinct. No unsupported raw-versus-adjusted explanation is assigned.
- The registry defines AN change in baseline-affected anatomical areas; the SAP's pre-existing-AN wording does not independently verify exactly how this secondary analysis was implemented.
- Diary score construction and a planned ITT model do not demonstrate robustness to informative missingness. Exact baseline symptom distributions and detailed missingness/sensitivity results remain unrecovered.
- Grade ≥3 and seriousness are different. Controlled, extension and pooled crossover safety populations cannot be collapsed. Treatment-emergent status alone does not establish causality.
- The selected all-active extension supplies no contemporaneous vehicle contrast; an early-versus-delayed strategy analysis would require a distinct estimand and adequate follow-up.
- The full journal paper and supplement were not read. The positive primary result is retained alongside these limitations; uncertainty is not converted into proof of no effect.

## Preserved policy and records

The Round 7 clinical-proof direction, Round 10 comparator alternatives, Round 13 optional model/comparator decision and all other programs remain unchanged. No HS threshold, duration, sample size, power calculation or exposure margin is imported. The BLU claim-mapping, zinc, SLC6A6 and HHD supplement searches remain closed.

The cumulative register advances to schema 14.0, appends an exact snapshot of Round 13 current decisions and retains the original curated snapshot identifier. Original ordered coverage, source records, generated concepts, Round 3–13 objects and the prior history prefix remain identical. All 189 earlier round-package files are retained byte for byte. Only six current index/register files are modified, and eleven Round 14 files are added.

## Verification and publication

[Local verification](local-verification.json) checks the baseline hashes, original 622 ordered coverage rows, historical objects and snapshots, the unchanged 100-point allocation queue, exact source/result values, four review input hashes, strict JSON and relative links. The [manifest](artifact-manifest.json) lists every expected repository file and hashes all other content; its own Git blob binds the manifest without a recursive self-hash.

The publishing workflow checks the actual remote `main` head immediately before the non-forced expected-head update, then freshly reads the branch, commit, full tree and committed manifest. Publication is complete only after those readbacks agree. No local checkout status is asserted. No outreach, purchases, recruitment, experiments, simulations or material receipt occurred.
