# Estimation method for the broad screen

**Review:** 9 November 2026 UTC / 8 November Pacific. **Decision stage:** broad screening and a provisional desk shortlist.

## What is being selected

Select a handful of drug-development opportunities for deeper desk diligence. A candidate can enter at synthesis, product qualification, preclinical development, an existing-drug indication or participation in an established program. The unit is an exact asset/use plus a plausible economic interest and a consequential next milestone.

At this stage, estimated terms are necessary. Each lane supplies low, central and high planning costs and time, a defined technical milestone, an analyst success range, a capture thesis, contrary evidence and reversal conditions. The estimates are judgments informed by the stated evidence, rather than quotes or measured candidate frequencies. Inquiries follow a narrowed shortlist.

## Keep the evidence and estimates legible

| Type | Treatment |
|---|---|
| Observed evidence | State the exact article, population, comparator, outcome and independent unit; link the primary source and access limitations. |
| Current program or rights fact | Date the official source. A public listing or announced license establishes its stated fact, not every field, territory or financial term. |
| Cost estimate | Define the deliverable and include an explicit entry/access allowance, product/material work, execution, analysis and contingency. State exclusions and later development separately. |
| Technical probability | Estimate the chance of the specified useful milestone conditional on the modeled access and competent execution. Producing data, a positive biomarker and a useful product/clinical result are separate events. |
| Economic probability | Use a clearly subjective conditional scenario for reaching net investor cash after a useful milestone. State the horizon and the access, rights, financing and distribution assumptions. |
| Genuine unknown | Show a range or alternative scenario where defensible. If no useful quantitative basis exists, record the uncertainty and give a qualitative preference or tie rather than pretending all candidates are indistinguishable. |

The numerical ranges are neither confidence intervals nor calibrated posterior distributions. Favorable combinations are possibilities, not forecasts. A central value is a working assumption for comparison. Cost and success may be correlated; the cautious and favorable cases deliberately combine coherent adverse or favorable assumptions instead of treating every input as independent.

## Compare useful milestones, not first invoices

A small qualification package can be valuable, but its price is not the price of clinical proof. In particular, the historical APR article/qualification and AAT process-qualification bands retain their original scopes. A newly estimated independent functional or controlled human package is larger because it answers a different question.

Each estimate states what a partner or subsequent developer could learn, what work remains, and whether the next milestone could be completed without an open-ended platform build. Clinical estimates for small academic signal or bridging packages do not imply a complete sponsor-run Phase II program, regulatory approval or commercial supply.

Historical HHS trial-cost data identify important scope and overhead drivers. NIH's staged translational program distinguishes qualification from later development and uses decision milestones. These are sanity checks on scope; neither source supplies a contemporary quote for a candidate. Source records and limits are in [method-sources.json](method-sources.json).

## Financial hurdle calculation

For a self-funded value-creation package with modeled all-in milestone cost **C**, probability **p** of a useful milestone, and conditional probability **q** of a paid handoff or investor distribution after that milestone, a deliberately simple screening model is:

`Expected net cash conditional on the modeled access/rights and execution = p × q × V − C`

Here **V** is net cash the investor receives on the paid branch, after downstream rights sharing, dilution, senior claims, required uses of transaction proceeds and transaction costs. Company valuation, total announced deal milestones and money retained for future work are not V. The model assigns zero recoverable cash to other branches and treats the full milestone cost as spent. Earlier stopping or recoverable value can be added in a subsequent dated decision tree.

The simple model assumes the investor has no mandatory or additional modeled contribution beyond C; later development must be funded by another party or the project stops. Zero recovery is conservative about salvage, but it does not cover unmodeled future cash outflows. If additional investor spending F occurs, include its probability-weighted cost in every branch where it is incurred, including later failure or no deal. The corresponding nominal hurdle becomes `(C + expected F) / (p × q)`. An uncapped diligence or financing obligation defeats the bounded-package assumption.

This model starts after the assumed entry arrangement is feasible; it does not estimate the chance of obtaining those rights or the unconditional return from today's screening decision. It also does not model a commissioned deliverable that earns payment for conforming completion even when the scientific result is negative. That structure would use acceptance, execution and collection branches rather than require a favorable efficacy result. No signed commissioned payment is assumed in this screen.

The break-even paid-branch cash is:

`V_break_even = C / (p × q)`

For example, an illustrative cost of $300,000, p = 50% and q = 30% requires $2 million of net investor cash on the paid branch to break even in this nominal model. That $2 million is a required outcome, not an estimated offer or asset value. The 15% product of p and q describes the modeled cash-event branch; it does not by itself establish principal recovery, which also depends on the size of V and all relevant obligations.

For cross-candidate sensitivity, the economic horizon is **five years as an analyst comparison assumption**, not a user-specified deadline. The calculation is nominal and undiscounted; delayed receipts would need a larger amount to earn an annualized return. Cautious cases combine high cost with low p and q; favorable cases combine low cost with high p and q. The purpose is to reveal the cash hurdle and where the preference changes. These calculations do not establish the probability of repaying the user's whole capital budget or the expected value of a portfolio.

## How the shortlist is chosen

The reproducible calculation also applies a common grid of net investor proceeds to each candidate: $0.5m, $1m, $3m and $10m on the paying branch. These are illustrative stress-test amounts, not asset-specific low/base/high values or offers. It computes `p*q*V-C` and that result divided by C. The grid makes the dependence on proceeds explicit without claiming unsupported comparable transaction prices. Subsequent desk work should estimate gross commercial value and the retained investor fraction separately.

Use the evidence and estimates together: useful-benefit credibility, cost and time to a consequential result, likely ability to retain value, the size and plausibility of the cash hurdle, remaining development burden, competing programs and the cost of being wrong. A large disease market does not establish an accessible paid outcome.

The shortlist is an integrating analyst judgment, not a vote among agents or an opaque weighted score. Preserve ties where differences are not robust, and name challengers that enter under different cost or capture assumptions. A new paper, an inexpensive ingredient, a familiar sponsor or advertised evaluation terms can improve one dimension without establishing overall superiority.

Apply the same assumptions to incumbents and challengers. APR and erlotinib are compared on a matched local product plus controlled useful-benefit milestone. Public counterparty specificity is recorded as an access fact; it does not substitute for the comparative evidence. The parallel [APR audit](https://github.com/KyleJKistner/ddiscov/blob/cc34bf24119f398b1061baca9c7d7a35cc897a1e/research/phase2-program/apr-ranking-audit.md) supplies the lineage of that correction.

## Next stage

Deepen the desk work on the small shortlist: challenge the clinical claim, refine the product and comparator, test cost and capture assumptions, and assess how much useful evidence is already forthcoming. Then make focused inquiries about the assumptions that still control the choice. A screening estimate is useful without authorizing an experiment, transaction or inquiry.
