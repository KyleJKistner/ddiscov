# Independent review: BLU qualification model, endpoints and safety

**Reviewer workstream:** Round8 human model/function. **Date:** 4 November 2026. Reviewed root work order `research/rounds/round8/blu3797-qualification-package.md`, snapshot SHA256 `ec055cfe62398a81c20d9b7f22596b5552ceff5be95ac11aa264cad1604eb70d`.

## Overall assessment

The core decision logic is sound for a bounded qualification investment. I found no model/biological reason to block the package. It correctly preserves tissue-level randomization, donor-level generality, batch reproducibility, the nonisogenic reference, the native-engagement limitation, and the difference between positive function evidence and a qualified negative reversal inference. It also avoids equating combined cardiac knockout with selective drug toxicity.

The fixed absolute useful-effect threshold `M=max(0.25*Gcal,delta_repeat)` is preferable to recalculating the threshold from treated-block reference values. My accompanying dossier/JSON has been aligned to this rule; contemporaneous gaps are descriptive diagnostics. The 24/96-tissue grids are resource proposals, not power or efficacy claims. A three-batch t interval will be very wide unless the effect is reproducible; that is a genuine limit of the chosen initial size, not evidence against the drug when uncertainty remains broad.

## Consequential clarifications recommended

1. **Define the day origin explicitly.** The manufacturer plots label culture days but do not publicly identify their exact relation to thaw, myogenic differentiation or casting. State that the proposed day20/day27 schedule is local days after the recorded casting origin, subject to blinded qualification. This prevents false exact-protocol replication. The main work order already permits adjustment before drug results.

2. **Keep specific force and fatigue denominators visible in the controlling order.** Add an explicit sentence that absolute force is primary, specific force uses a documented viable contractile cross-sectional-area estimate, and fatigue must include absolute impulse/late force alongside normalized retention. Record attachment, passive tension and geometry. The model dossier contains these rules; including one sentence in the operational order prevents an apparently better ratio or lower starting-force fatigue trace from becoming the success claim.

3. **Make second-background expansion conditional on the independent first-background result.** F2 currently groups independent confirmation and addition of a second background. A positive p.L463S confirmation can advance a narrow article/background claim without making creation of a second patient model an immediate condition. Broader-genotype claims do require the second-background result. The later quantitative table already says this correctly; align the F2 wording so it does not become an unnecessary first-investment gate.

4. **Allow a qualified energetic readout compatible with the actual 3D tissue.** ATP-linked respiration/reserve is biologically useful, but plate geometry, tissue mass and transport can prevent direct transfer of a 2D oxygen-consumption method. Require a qualified energetic-function assessment, with ATP-linked respiration/reserve preferred where technically valid and an orthogonal energy/stress readout otherwise. Destructive siblings are separate resources. Do not require an untransferred platform as a hidden gate to every useful initial force signal; do require resolution of an overlapping energetic liability before a larger systemic claim.

## Numerical gates: acceptable with their current boundaries

- The proposed ≥3/4 evaluable tissues per line/batch and positive gap direction in all3 qualification batches are process specifications. They are deliberately demanding for a tiny calibration block; a failed batch can justify the allowed bounded requalification. They cannot support rejection of C2β biology, and the work order correctly makes the downstream branch model-specific.
- `1.96×SD(paired repeat differences)` is a candidate repeatability limit for the qualified recording protocol, not a confidence interval for treatment effect. It should use genuinely repeated recordings at a controlled physiological state; differences across maturation days would mix biology with readout repeatability. The work order states the main distinction; the sample record should preserve the pairing and rest interval.
- A 20% repeated healthy-force or ATP-linked-respiration decrement is appropriately a **review/hold trigger**, not a safety cutoff. Smaller reproducible critical liabilities still matter. Repeatability/matrix interference/cell mass must be resolved before assigning mechanism.
- An upper bound below M establishes futility relative to a useful-effect target only in a sufficiently qualified setting. It does not establish zero pharmacological effect. Target-level downgrade appropriately requires more than one article or one patient line.
- Qualified native CETSA/PRM can support an engagement-response relationship without calibrating occupancy. The package correctly allows an interpretable positive function feasibility study while withholding a strong target-negative conclusion if engagement remains unresolved.

## Evidence boundaries retained

- Curi p.L463S is a standalone line. CB-SKM-6-WT is a proposed reference, not established as the marketing graph's control.
- Kora p.E48*/corrected and healthy/KO pairs do not establish mature-force rescue or provide the p.L463S isogenic control.
- The new Lionello2026 abstract reports force/calcium deficits, while CRISPR correction explicitly improves fiber size. Those endpoints must remain separate.
- Segawa thesis and Aki2026 paper share a research lineage. Single-isoform transformed-cell morphology and double cardiac deletion are different perturbations; no β-only catalytic dose window is recovered.
- Kobialka2023 adds developmental endothelial evidence against blanket “normal histology = no phenotype” reassurance, without establishing BLU toxicity. Its unresolved full-text denominator is stated.

No experiments or data-fitting were performed for this review. The review changes the interpretation and future work specification only.
