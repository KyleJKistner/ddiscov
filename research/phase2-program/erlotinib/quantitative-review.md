# Independent quantitative review

Review completed 9 November 2026 UTC / 8 November Los Angeles by a separate reviewer from the design and economics authors. Scope: the [clinical model](design-model.py), [inputs](design-inputs.json), [results](design-results.csv), [clinical interpretation](clinical-design.md), [economic inputs](economics-inputs.json) and [economic interpretation](market-economics.md). This review checks implementation, arithmetic and interpretation; it does not validate the clinical assumptions, cost estimates or opportunity value.

**Finding: no numerical or implementation blocker found.** The model reproduces its 864 scenario rows. Independent analytic calculations agree with its core conditional operating characteristics. The economic totals and flexible-capital comparisons reconcile. No finding supplies a probability that topical erlotinib works, passes Phase II, or returns invested cash.

The integrated [dossier summary](README.md), [plot selection and labels](plot-design.py), and rendered [design figure](design-sensitivity.svg) were also reviewed. Their reported probabilities, cost differences and $2.888m closing-cash example agree with the underlying calculations; the figure correctly restricts its comparison to independent participants with no loss or attenuation. The summary preserves the distinction between a stringent precision criterion and Phase II success.

## Clinical calculations

The implementation correctly draws normally distributed mean contrasts and independent chi-squared variance estimates conditional on completed analysis units. Independent paired participants, independent two-person family means and equal-allocation parallel arms use the stated standard errors and degrees of freedom. The family calculation assumes equal family size and the specified correlation; it is not a general unequal-cluster analysis. Random complete loss is modeled explicitly, with whole-family loss in that sensitivity.

I independently used the noncentral-t distribution for positive confidence-bound events and numerical integration for the joint signal/point-estimate rule. For true benefit 2 points, SD 2.5, no loss or attenuation, and independent paired participants:

| Independent complete participants | Positive statistical signal | Signal and estimate ≥1.5 | Lower 95% CI >1.5 |
|---:|---:|---:|---:|
| 12 | 71.366% | 67.547% | 9.249% |
| 20 | 92.390% | 81.276% | 13.349% |

These analytic values differ slightly from the saved Monte Carlo percentages, as expected from simulation error. For example, the saved 12-person lower-bound result rounds to 9.1%, not the analytic 9.2%. At 100,000 replications, the largest binomial Monte Carlo standard error is approximately 0.158 percentage points. Shared random draws across effect/attenuation comparisons do not create independent evidence.

The independent calculation confirms that **199 complete independent paired participants** would be needed for 80% probability of a lower 95% confidence bound above 1.5 under this particular 2-point/SD 2.5 scenario. This is a stringent illustrative precision goal, not a standard Phase II success requirement or an enrollment recommendation. A positive smaller pilot may still be useful.

Exact binomial calculations also confirm the recruitment distinction: with independent 80% retention, the probability of at least 12 completers is **64.816% with 15 randomized, 94.873% with 18, 97.672% with 19 and 99.002% with 20**. Expected completion is not assured completion. Recruiting relatives does not automatically supply independent replication.

Interpretive boundaries that must survive summary:

- The 1.5-point worthwhile threshold, true effects, SDs, correlation and attrition are explicit assumptions, not estimated from the two related topical cases.
- Using the same numerical SD in paired and parallel rows is not an empirically matched comparison; those SDs describe different quantities.
- Normal contrasts and random complete loss omit bounded-score effects, informative withdrawal, uncertain baseline adjustment, product failure and failed recruitment.
- Lower CI >1.5 measures strong evidence above the illustrative threshold. Its approximately 9% frequency must not be relabeled drug-success probability.

## Economic calculations

The [standard-library verifier](verify-economics.py) independently recomputes saved arithmetic without changing inputs. It reconciles product modules, program components, contingencies, cumulative gates, visit costs, expected completion and binomial completion probabilities, additional-patient costs, capital capacity, revenue examples, recruitment yield, retained-cash break-even examples and follow-on totals. Cumulative gates increase within the corresponding total and are not added as extra costs.

Key reconciled values are the 15-randomized central pilot totals of **$462k with a qualifying transferred package** and **$624k with independent qualification**; the 19-person sensitivities are **$510k and $672k**. At hypothetical available capital of $750k, those 19-person cases leave **$240k and $78k**; at $1m they leave **$490k and $328k**. These are differences between capital and modeled cost, not profit or validated reserves. The user's $500k reference is explicitly not a hard cap.

The arithmetic cannot establish that an existing product/dossier can be transferred, that its evidence bridges to the proposed product, that prices are obtainable, or that a buyer will pay. Low/base/high scenarios are not confidence intervals. Major excluded safety or follow-on requirements can change costs materially. Cash-recovery examples correctly distinguish cash payable and retained participation from headline valuation or contingent milestones, but their probabilities and transaction amounts remain hypothetical.

## Reproduction

Run from the repository root:

```bash
python research/phase2-program/erlotinib/design-model.py --check
python research/phase2-program/erlotinib/verify-economics.py
```

Design reproduction was verified with NumPy 2.3.5 and SciPy 1.17.0. Exact CSV equality can depend on numerical-library versions. The financial verifier uses only the Python standard library. It checks money to half a cent and saved three-decimal completion probabilities to their rounding precision; it does not evaluate prose or source accuracy. Independent analytic cross-checks above were performed during review in addition to the model's own assertions.
