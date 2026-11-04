# Round 8 independent portfolio integration review

Reviewer: clinical/discovery workstream. Evidence cut: 4 November 2026. Baseline main: `f49a937206cbbf18e6c8f89f2dcb31eb704e9cd7`.

## Scope and initial verdict

Reviewed the integrated `ddiscov_round8/research/rounds/round8/portfolio-allocation.md`, Round 8 `README.md`, clinical challenge and six-record candidate Markdown/JSON files. Also checked the root README, local artifact links, numerical allocation, and the current register snapshot against Round 7. No shared file was modified by this reviewer.

**The portfolio dispositions, counting and symmetric commercial standard are coherent. One factual wording correction and several artifact-reference repairs were identified before publication.** The root README/current shortlist/register were still at Round 7 at the first inspection; the integrating agent had explicitly said those updates were in progress. They are not yet included in a final post-integration preservation verdict below.

The allocation table sums to 100: BLU 55, enasidenib 15, ruxolitinib 10, lisdexamfetamine 6, NDC/roflumilast 4, P2 2, selective thin-filament discovery 2, AAT 1, bounded discovery 5. This agrees with the clinical JSON after decomposing the five older-core points into NDC 2, P2 2 and AAT 1. The three leading decisions receive 80 points; the other ten challenger points are lisdexamfetamine 6, roflumilast 2 and selective thin-filament discovery 2. These are planning allocations, not financial forecasts, success probabilities or authorized spending.

## Findings requiring disposition

### 1. Correct the direction of survivor selection in the botulinum pilot

`portfolio-allocation.md`, under the ruxolitinib discussion, calls the pilot follow-up **“relapse-enriched.”** Relapsers were removed from efficacy follow-up. The correct description is **“survivor-enriched”** or **“responder-enriched.”** The clinical dossier correctly states this elsewhere, and the numerical denominator is correct: eleven relapses among twenty-six HHD participants, not an HHD rate using the mixed thirty-person cohort.

This is a factual wording correction, not a change in candidate rank or the recommendation to use a practical sweat-control benchmark.

### 2. Resolve publication-local artifact references without uploading full papers merely to satisfy a path

The integrated `new_candidates.md` still refers to `discovery_sources/alias_audit.json`; the staged repository artifact is `candidate-alias-audit.json`. Its JSON counterpart already points to the new artifact at a repository-relative path. Update the Markdown reference and make the path convention explicit or use a working relative Markdown link.

The `sources[*].local` values in the clinical and candidate JSONs point into `discovery_sources/` or `blu_model_sources/`, which are retrieval-workspace directories and are not present in the staged Round 8 directory. Primary URLs and access tiers are available. Rename these to clearly identified retrieval-workspace provenance, remove misleading local-path fields, or provide a compact source-access manifest with URLs and hashes. There is no need to republish copyrighted full articles to repair these references.

Additional plain-text references deserve normalization:

- `blu_article_exposure.md` names `blu_identity_numeric_audit.py`, while the published utility is `methods/blu3797_identity_audit.py`.
- `review_fluoxetine_kcnc1.md` refers jointly to `fluoxetine_endpoint_audit.py/.json`; these are published in different directories. The Round 8 README already links them correctly.
- The qualification article review mentions `round8_work/` scripts and a temporary check output as historical execution provenance. Those should remain explicitly historical, rather than appear to be runnable repository-local paths. Its integration command is correct.

At initial inspection the Round 8 README also linked three not-yet-staged files: `review_decision_utility.md`, `integration_review.md`, and `round8_root_deltas.json`. These are expected integration outputs; verify that each exists before publication. Their temporary absence is not evidence of missing scientific work.

### 3. Prefer an evidence statement to an assertion of exact biological absence

The NALL record says **“No aggregate improvement occurred”** on objective walk/peg measures. Prefer **“No aggregate improvement was demonstrated”** or **“No overall improvement was reported.”** The result is an absence of a demonstrated group change in the available analysis, not proof that the true effect is exactly zero. This is a nonblocking precision improvement; it does not alter the hold on an independent asset thesis.

## Claims checked and retained

- **Counting:** six reviewed records comprise four new exact intervention–use screens and two existing-use updates. The four include one BL-N05 concept expansion. W7/TNNT2-R94C and epalrestat/PMM2 were already in the original inventory; fluoxetine/CMS and NALL/NPC are different existing uses. The report makes no claim of six new molecules.
- **Clinical leaders:** enasidenib's cardiac, neurological and neonatal hypotheses remain distinct. Vorasidenib's R140Q activity is not promoted into normal infant CNS exposure, comparative clinical efficacy or a proven safer substitute. Ruxolitinib's symptomatic value does not require a genetic-repair claim, while a procedure-avoidance or maintenance claim has its own comparison and duration.
- **New candidates:** six selected lisdexamfetamine responders do not produce an all-treated response rate. Fluoxetine's primary credible interval crossing zero remains visible. VU426 is a mechanism comparator, not a seventh validated clinical lead. Roflumilast cream evidence remains Darier/ATP2A2-specific. W7's direct channel blockade challenges the exact systemic article rather than disproving selective thin-filament desensitization.
- **Negative update:** epalrestat is held on verified futility status with 42 actual participants. Official submission-tracking metadata is not a public result table. The files do not invent arm effects, safety findings, subgroup rescue or a delivery explanation.
- **Commercial symmetry:** the ordering explicitly reflects the next decision and the user's BLU emphasis. It does not claim superior BLU human evidence or easier rights. The same distinction between scientific value, a reproducible article, received resources, a differentiated product and commercialization rights is applied to BLU and known drugs. An independent clinical dataset can remain a research project when an exclusive asset thesis fails.
- **No new execution claims:** the documents distinguish proposed criteria, calculated planning quantities, extracted source data and actual biological observations. No acquired material, experiment, outreach, purchase or financing is claimed.

## Preservation and publication checks

At the initial inspection, the staged `portfolio-register.json` was structurally identical to the Round 7 baseline: 622 coverage records, with prior round objects unchanged. The integrating agent was still updating it. A post-update comparison must confirm that these 622 original records and all earlier round objects remain intact while Round 8 is added; then the controlling shortlist, root README and reading rule must consistently identify Round 8.

This review does not claim to verify a GitHub commit, branch head or final blob manifest. Those publication checks belong to the integrating agent after the authorized commit.

## Reviewed snapshots

Initial `portfolio-allocation.md` SHA-256: `730d02bc0f6641f5630709f2e45d50c4978b7a83d546250b11378efea833a521`.

Initial Round 8 `README.md` SHA-256: `8f3cf6b965435f5bba9c36cbb304ca223e490b51b21c78b4b4107ec6ab033100`.

The initial findings above are retained as the review trail. The completed post-integration check below controls the review disposition.

## Final post-integration verification

**Pass for scientific integration, counting, historical preservation and commercial symmetry.** The completed Round 8 current shortlist, root README, selection policy, portfolio allocation and schema-8 register are mutually consistent. No remaining scientific or decision-record correction is requested by this reviewer. The final publication manifest, GitHub commit and branch verification remain the publishing agent's responsibility.

### Historical preservation

The reviewer compared the parsed schema-8 register with the baseline main register and compared the complete baseline file tree with the staged tree:

| Check | Result |
|---|---|
| Original `coverage_records` | All 622 records remain structurally identical, including order and content. |
| Prior `round3`, `round4`, `round5`, `round6` and `round7` objects | Each is structurally identical to the baseline. |
| Original `generated_concepts` | Structurally unchanged. |
| Existing `round_history` entries | The original five-entry history is an unchanged prefix of the new six-entry history. |
| Added Round 7 history snapshot | `final_shortlist`, `secondary_priorities`, `retained_reserves`, `new_validation_priorities`, `local_qualification_comparison` and `current_corrections` each exactly match the prior current values. Its counts exactly match the original `round7.counts`. |
| Baseline files | 127 remain byte-identical; none are missing. Only the eight intended current/index documents changed. |
| Earlier round files | No historical Round 1–7 document changed. The enclosing rounds index was updated to include Round 8. |

The eight changed baseline documents are the root README, current shortlist, selection policy, research README, screen index, cumulative register, methods README and research-round index. The existing W7 and epalrestat rows remain historical records. Their new dispositions are applied explicitly through `current_dispositions_by_inventory_id` and the Round 8 update records, consistent with the revised reading rule.

### Current decisions and numerical controls

- The register's Round 8 screen arrays exactly match the six records in `new_candidates.json`: four new exact-use screens (`R8-NL-01` through `R8-NL-04`) and two existing-use updates (`R8-EX-01`, `R8-EX-02`). The four comprise three uses without a prior matching concept and one explicit PDE4 concept expansion. Comparator additions are not extra candidates.
- The three Round 8 leader records exactly match their corresponding current core records. The six-member continuing core retains NDC-9009, 8015-P2 and AAT/EVLP alongside BLU, enasidenib and ruxolitinib. The twenty-one retained reserves do not duplicate the clinical leaders as conflicting current decisions.
- The register's current allocation exactly matches `round8.allocation` and totals 100. Its 55/15/10 leader allocation, six lisdexamfetamine points, two selective thin-filament points, two roflumilast comparator points, five older-core points and five discovery points agree with the narrative portfolio table. W7's two points fund the selective-target discovery question, not systemic W7 development.
- The register reports zero S-tier promotions and each leading record retains `current_S_tier: false`. The reading rule identifies the Round 8 decisions as controlling and keeps participants, backgrounds, tissues, batches, repeated readings, proposed samples and synthetic code fixtures distinct.
- Product contribution and public-rights requirements apply explicitly to BLU as well as marketed, branded and generic leaders. The 55-point BLU emphasis is justified as a next-action allocation with a concrete qualification work order; it is not a claim of superior human evidence, easier rights or an already financeable exclusive asset.

### Corrections and artifact-reference closure

The factual botulinum wording is now **survivor-enriched**, the NALL wording now says no aggregate improvement **was demonstrated**, the alias audit is linked at `candidate-alias-audit.json`, and the identity audit points to the published `methods/blu3797_identity_audit.py` utility. Clinical and discovery source paths are explicitly labeled `retrieval_workspace_file_not_in_commit`; they no longer imply that downloaded full papers are committed artifacts. Primary source URLs and access-tier records remain available.

The Round 8 Markdown-link check found one expected publication-stage forward reference: `integration_review.md`. The integrating agent has explicitly retained that report and the final file manifest as the next publication tasks. `review_decision_utility.md` and `round8_root_deltas.json` are now present. This reviewer supplies the present report for inclusion as `review_portfolio_integration.md`.

One nonblocking shorthand remains in the fluoxetine review: `fluoxetine_endpoint_audit.py/.json`. The Round 8 README and methods README correctly resolve the script under `methods/` and its saved audit under `research/rounds/round8/`. Historical `round8_work/` paths in the qualification article review describe the earlier validation execution; the actual repository command is also provided. Neither issue changes the scientific decisions or prevents the published utilities from being located.

### Final inspected snapshot hashes

These SHA-256 values identify the inspected content before the publishing agent adds its integration report and publication manifest. They are not Git blob identifiers or a claim that the branch has already been updated.

| File | SHA-256 |
|---|---|
| Root `README.md` | `02acb05b1dc79564ba808af36320f89dc3d94652ae022da185e4e6637925bec1` |
| `decisions/current-shortlist.md` | `32cdd4e4e75caab34288de17ad6189dea0a120e58ebce78ba70c1b5be118ca2e` |
| `research/portfolio-register.json` | `56e84eb60b4f2ad230d43edf2ba5fd3ed30a133fd7899f1807087c285513d2a2` |
| `research/rounds/round8/portfolio-allocation.md` | `ff04d7d536e164599176b1c41d4b2ef62349a8d2935ad72266cf7a96d5abf28b` |

The scientific integration review is complete. No outreach, discussion, purchase, material acquisition, biological experiment or GitHub publication was performed by this reviewer.
