# Independent challenge of the proposed BLU3797 human-function proof

**Reviewed 4 November 2026:** [BLU3797 human proof](blu3797-human-proof.md). This is a focused scientific review of decision logic. No experiments or external actions were performed.

The proof already handles the major source problems correctly: p.L463S and p.E48* are distinct models; mouse differentiation is not human force; fields are not independent donors; PIK3C3 lipidomics is not MTM1 lipidomics; relative fatigue can hide a low starting force; and trajectory-aware baseline adjustment is preferable to requiring a perfectly flat culture. I found four remaining decision points worth tightening. None warrants abandoning the proposed staged proof.

## 1. A corrected line proves disease dependence; it may not prove reversibility after onset

Stage A's MTM1-dependence control is necessary. A line corrected **before differentiation**, however, may prevent a structural defect without showing that the already-deficient tissue can recover. The same logical limit applies to a healthy-parent/constitutive-MTM1-KO pair. The 2025 endogenous C375S and 2012 local protein-delivery results illustrate why developmental context and intervention timing can change the phenotype. [2025 primary](https://insight.jci.org/articles/view/189286); [2012 primary](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1002965).

**Material risk:** a negative post-deficit BLU result plus a healthy corrected line could be misclassified as target failure when the particular mature assay has become structurally irreversible, or when the selected assay does not preserve the repair capacity that the hypothesis requires.

**Suggested change:** distinguish two controls explicitly:

- Prior genetic correction establishes that MTM1 causes the assay deficit.
- A validated intervention applied **after the same deficit** establishes that the measured output is modifiable on the observation timescale. Temporally controlled MTM1 restoration is strongest; a validated disease-relevant functional rescue can also demonstrate modifiability, with its interpretation stated.

The proposed delayed PIK3C2B perturbation then tests the target itself. If that perturbation achieves verified, appropriate catalytic suppression and still fails in a demonstrably modifiable assay, the mature target thesis is challenged. If only BLU fails, demote the molecule. If no delayed positive intervention works, label the rescue question unresolved in that assay. Do not require creation of an entirely new model before a practical pilot can begin, but make the decision branch explicit.

## 2. “A useful effect” needs a confidence-based advance and futility rule

The document correctly says to lock a minimum useful effect before unblinding and avoids inventing a clinical minimum. It should specify how uncertainty around the result is used. A point estimate above a threshold with a confidence interval spanning trivial effects is materially different from evidence that the useful threshold is exceeded.

Define, prospectively, an assay-repeatability floor **Δnoise** and a distinct minimum useful effect **Δuseful**. The latter is a product-development choice informed by the genetically rescuable gap, the active comparator and the proposed functional benefit; statistical precision alone cannot determine it. The gap should not be recalculated opportunistically from a favorable measurement day.

**Suggested decision rule:** advance only when the lower confidence bound for the prespecified functional estimand exceeds the larger threshold. A confidence interval entirely below Δuseful supports futility. An interval crossing it is inconclusive and should not be described as either proof or biological failure. The interval should preserve donor/batch dependence; large numbers of repeated stimulations cannot supply missing biological information.

This does not require an arbitrary percentage today. It requires that the qualification pilot fix a reviewable threshold and a bounded confirmatory design before drug outcomes are revealed. Report raw absolute force even when a normalized gap fraction is used to communicate the effect.

## 3. Equal free concentration across culture systems is a useful hazard comparison, not the in-vivo window

The exposure section is substantially correct, but a same-concentration muscle/neuron comparison can be overinterpreted in either direction. A neuron effect below the muscle-effective concentration need not doom a compound that has very low free brain penetration. Conversely, absence of toxicity at the nominal medium concentration does not establish safety if a tissue accumulates parent drug or an active metabolite. The human-variant/mouse neural evidence is a reason to resolve this uncertainty; it is not evidence of BLU clinical toxicity. [Primary neural study](https://academic.oup.com/brain/article/145/7/2313/6628565).

**Suggested change:** define the first comparison as an **intrinsic tissue-sensitivity screen**. Close the systemic window only when measured or suitably bounded unbound tissue distributions connect the muscle-effective exposure to the exposure in vulnerable tissues. For example, the relevant relationships are free muscle versus free plasma and free brain versus free plasma, not an assumed identical concentration everywhere. Distinguish parent and any functionally relevant metabolites.

A concerning in-vitro overlap with unknown tissue distribution should hold the molecule at an unresolved window. A measured overlap at the exposures required in the vulnerable tissue supports a stop. The liver may require particular attention because low brain exposure does not itself address liver exposure or MTM1-dependent canalicular susceptibility. This adjustment prevents both premature rejection and false reassurance.

## 4. “Post-deficit” and “mature” should remain separate labels

The revised baseline section rightly allows predictable maturation. Keep that flexibility. A treatment can act after an observable deficit while the tissue is still undergoing substantial myogenesis; this can yield real functional benefit without establishing reversal in chronically mature muscle. The published BLU cell experiment's delayed addition during differentiation is precisely this distinction. [BLU primary](https://insight.jci.org/articles/view/198568).

**Suggested change:** name the first endpoint “post-deficit human muscle-function benefit” and separately specify what will qualify the tissue as sufficiently mature for a mature-rescue claim. Use converging structural and physiological criteria and a prespecified observation window; an absolutely flat force curve is not necessary. Replace the table's unqualified “adult-stage target reduction” wording with “target reduction after the qualified tissue deficit,” unless an adult-like state has actually been demonstrated.

A trajectory-adjusted improvement during ongoing maturation may support a valuable pediatric developmental-compensation hypothesis. It should not be discarded merely for occurring during maturation, nor promoted as proof of adult chronic reversal. A second later-state comparison determines the broader claim.

## One target-specific interpretation to retain

PIK3C2B perturbation affects active integrin trafficking and focal adhesion in the primary cellular literature. [Primary integrin study](https://doi.org/10.1073/pnas.2202236119). In an engineered three-dimensional force system, improved force transmission/attachment can therefore contribute to a larger measured force. This may be useful biology, but it need not mean intrinsic excitation–contraction coupling has normalized.

The proof's calcium handling, tissue dimensions and viable contractile content already help. When qualifying the platform, also preserve passive tension/geometry or another platform-appropriate check that separates changed coupling from an increase in active mechanical output. Interpret a transmission benefit on its own merits rather than calling it automatically an artifact or automatically an intrinsic muscle rescue. This is a mechanistic interpretation safeguard, not another broad safety panel.

## Recommendation and disposition

Keep the proposed proof, with the four decision clarifications above. The useful minimum is an authenticated article, an interpretable disease-dependent functional deficit, a post-deficit modifiability control, a predeclared useful-effect threshold with uncertainty rules, and a measured exposure argument. Add experiments only when they resolve one of those distinctions. The present literature does not supply the missing outcome and does not justify S-tier promotion.

**Integration disposition:** All four clarifications and the force-transmission safeguard were incorporated into the linked proof before publication. This review is retained to make the changes and their reasoning visible.
