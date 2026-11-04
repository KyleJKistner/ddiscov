# Independent review — BLU3797 decision utility and JSON records

**Scope:** `ddiscov_round8/methods/blu3797_qualification_decisions.py`, the prospective qualification specification and blank decision-input template. Review performed against the controlling work-order narrative. Any numerical input used below is an explicitly synthetic branch-logic fixture; no biological data were generated or simulated.

## Initial verification

The supplied self-check passed **14 decision branches**, rejected **4 malformed numerical/type inputs**, and preserved the separation of scientific continuation from an absent standalone-product contribution. The blank template returned **`not_run_planning_only`**, with no target rejection, clinical-efficacy claim or S-tier promotion.

Numeric validation correctly rejects boolean values as numeric force, nonfinite values, nonpositive minimum useful effect, invalid interval ordering, incorrect units and invalid tristate flags. Threshold equality does not establish confirmation. A positive exploratory function result can advance with unresolved target attribution, while a target-negative conclusion requires engagement, adequate perturbation and delayed modifiability. These asymmetries match the scientific plan.

## Consequential issues identified and accepted for correction

### 1. Missing observation provenance could still yield an advance

Starting from the blank template, filling favorable numerical values and the qualification booleans allowed `advance_independent_confirmation` while all lot, genotype, exposure, analysis-lock, missingness and denominator fields remained null. Moreover, `evidence_record=true` and a whitespace-only string were accepted because the original code checked truthiness rather than a documented reference.

This was not a failure of the scientific threshold. It was a completeness failure in the record meant to support it. A human-supplied “qualified” boolean should not erase an explicitly unknown identity or denominator.

**Accepted resolution:** require nonempty string references for the evidence, lot/formulation, genotype/reference, exposure time course, analysis lock and exclusions/missingness records; require integer, nonnegative denominator values, with at least three independent batches and one disease/reference donor for the v1 work order. Incomplete or invalid provenance must produce `incomplete_observation_provenance`, never an advance. These are completeness checks; they cannot authenticate the contents of an external evidence record.

### 2. Generic `target_rejection=true` overstated a bounded downgrade

The branch named `downgrade_target_under_tested_conditions` correctly described its scope in prose but emitted `target_rejection=true`. A downstream reader could mistake that broad boolean for universal target rejection.

**Accepted resolution:** keep `target_rejection=false`, and emit `bounded_target_downgrade=true` with explicit tested-condition/background scope. An exact-article/local-model futility result remains distinct from this stronger, still bounded downgrade.

Initial synthetic reproductions are retained in `decision_utility_review_cases.json`. They document the pre-correction behavior and must not be mistaken for current implementation results or actual candidate outcomes.

## Other observations

- A positive result without calibrated native occupancy must retain its mechanism limitation. The current design does so; no80% efficacy minimum is imposed.
- Independent confirmation and an independently qualified background are separate concepts. Neither additional wells nor repeated images become additional donors through the utility.
- The v1 minimum of three batches is a prospective run-plan completeness requirement, not proof of adequate power or generality.
- `incremental_product_contribution=absent` can coexist with a scientific function signal. Its separate asset-stop field is intentional; the function classifier does not certify financing or authorize additional expenditure.
- The planning branch explicitly uses assumed standard deviations and conditional Student-t interval widths. It is not an observed effect, patient sample-size calculation, simulation of biology or success probability. That branch requires SciPy; `check` and `self-check` do not.
- The specification keeps the absolute useful-force threshold, lot and observed biological results unknown. Proposed98% purity/ee,20% research precision,80% high-engagement challenge and threefold exposure characterization are labeled prospective rather than attributed to published BLU results.

## Narrative JSON cleanup

The child-owned `blu_article_exposure.json` was corrected for joined words in descriptive fields: catalog/lot distinctions, constructs, source locations, unavailable measurements and statements not claimed are now readable, searchable prose. Stable identifiers, chemical formulas, URLs and machine enums were preserved. `w7_independent_challenge.json` was independently read and already contains readable narrative descriptions.

## Final patch verification

The provenance/scope patch was independently read and executed. Its self-check passes **19 branch cases**, rejects **4 malformed inputs**, verifies the independent science/asset dispositions and verifies that bounded target downgrade does not emit global target rejection. The blank template still returns `not_run_planning_only` with all promotion/rejection flags false. Requiring at least one primary endpoint together with endpoint count no greater than randomized count also closes the zero-tissue observed-pass case.

The review then identified one remaining denominator semantic issue: an initial synthetic second-background fixture counted two backgrounds but only one donor. Root accepted a final clarification that an independent background requires a distinct donor/genetic background. `disease_donors` will mean unique donor backgrounds contributing disease models, with `disease_donors >= independent_disease_backgrounds`; a healthy donor engineered to MTM1 loss may contribute another model background but is not thereby a second patient. The final verification below will confirm this additional check.


**Final result:** the donor/background consistency check is implemented, the second-background fixtures now use two donor backgrounds, and the template documents the distinction from affected-patient counts. The final self-check and blank-template check both pass. No consequential unresolved decision-logic issue remains in the reviewed scope. The utility remains a consistency checker of human-supplied evidence assessments, not an authenticator of experimental truth.

Reviewed final utility SHA-256: `e943c7818017f77db711d0c84cbe392389c8eaaad4cd2913091aa5b482615fc0`. No root repository file was edited by this reviewer.
