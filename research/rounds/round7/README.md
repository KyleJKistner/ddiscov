# Round 7 — enasidenib and ruxolitinib development dossiers

**Evidence cut: 4 November 2026. Baseline:** `a834a480d74b1ebefbaa3fc072db17f67c2aa3d6`. This sprint develops **two existing candidates**, with **zero new lead screens**. Four workstreams, including the integrating review, produced clinical and product dossiers, three reproducible audits, staged development plans and three independent challenges.

## Decision

**Both candidates now have the same diligence dimensions as BLU3797 and an affirmative, finite next-proof recommendation.** Their next steps follow their human evidence stage. Enasidenib warrants a defined pediatric article/exposure project linked to prospective organ function. Ruxolitinib warrants protocol/article/measurement qualification followed by a controlled comparison of useful HHD lesion control.

Neither is called an S-tier proprietary asset. The dossiers distinguish clinical benefit, readiness of the next proof and value capture. An existing franchise or off-label use does not erase scientific value; a scientific dataset does not automatically create a defensible drug company. No owner or author reply is a scientific-selection gate.

## What is now equivalent in diligence depth

| Dimension | Enasidenib / germline IDH2-R140Q D2HGA2 | Ruxolitinib 1.5% / HHD |
|---|---|---|
| Exact entity and intended use | Base/mesylate, tablet/sprinkle/minitablet, genotype and distinct infant versus established-organ claims | Active/concentration/route separated from brand/vehicle/lot; prospectively standardized marketed cream |
| Original evidence and lineage | Original supplement, full Gold/Roux reports, baseline cardiac severity and unresolved skin-case linkage | Five detailed exact-strength cases, combination/maintenance context, conference duplicate, separate 1% case and unpooled preprint |
| Quantitative/source challenge | 177 laboratory measurements from one child; timing, reference-range and arithmetic conflicts | Clinical denominator/demographic audit; two original PK tables, high-exposure supplement and official patent-row audit |
| Exposure and safety | Current adult PK, active metabolite, interactions, A3 activity, pediatric laboratory findings and CNS limits | AD PK subsets/extremes, label context, active/healed-skin exposure questions, no invented 281 nM safety cutoff |
| Material and model route | Defined assay materials, public formulation, biochemical versus cardiac-model distinction | Marketed clinical article, research salts, vehicle alternatives, authenticated model/assay scope |
| Competition and public claims | Existing clinical programs and granted pediatric formulation claims | Active KB111/guselkumab programs, Incyte franchise and selected current public patent/litigation facts |
| Development proof | Article/methods → exposure/PD/function feasibility → independent confirmation/product advantage | Article/control/measurement → controlled clinical value and PK → confirmation/product advantage |
| Independent challenge | Separate clinical reviewer checked primary clinical and selected product sources | Separate clinical and product reviewers checked cases, controls, PK, claims and protocol logic |

Equal review depth does not imply equal biological evidence, shared endpoints, identical risks or completion of the proposed experiments. BLU still needs its qualified human-force comparison. These two already have human treatment observations, so a new generic cell/animal rescue is an optional discriminating tool, not a universal gate.

## Enasidenib: a credible clinical-development question

One original child had severe established cardiomyopathy, with LVEF 20–25% at entry and 40–45% at eight months, followed by fluctuations. The other began with normal systolic function; Gold's independent child had milder abnormalities. These are different baseline strata. The five described outcome records are not a verified five-person response denominator, and the five-week-old 2026 item remains metadata-only. [Clinical dossier](enasidenib_clinical.md)

The formulation route is now concrete: actual pediatric sprinkle use and a granted public minitablet disclosure with 20 mg free-base equivalent per capsule. The historical clinical lot is not proven identical to that patent example. Current adult PK and interaction data make measured pediatric exposure important; a fixed adult dose or short interruption cannot supply an infant regimen or drug-free durability claim. [Product, exposure and staged proof](enasidenib_product.md)

The recommended first funded output specifies one pediatric administration article and a linked delivered-dose/exposure/chiral-metabolite/organ-function measurement plan. Prospective observations should preserve growth, baseline severity, concomitant treatment and tolerability. A more usable delivery or better exposure–benefit relationship is a possible product contribution; neither novelty nor rights clearance is presumed.

## Ruxolitinib: stronger human support, a necessary controlled comparison

Five distinguishable reports describe 1.5% cream use, with rapid reported symptom relief and/or useful maintenance. Some use combination induction, and none supplies a consecutive treated denominator. The nine-patient preprint's methods and clinical table remain unverified; its author data record is publicly embargoed. The existing detailed cases are sufficient to support the controlled question without waiting for that source. [Clinical dossier](rux_hhd_clinical.md)

A different HHD trial, DERM101, reported substantial control-arm improvement. Its small fixed analysis denominators and missing visit-level handling prevent a transferable placebo estimate, but the result demonstrates why another uncontrolled series is weak decisive evidence. The clinical review also corrects a later paper's anti–IL-8 mechanism citation. [Clinical arithmetic audit](rux_hhd_clinical_audit.json)

The marketed cream removes a synthesis prerequisite. AD studies supply an exposure anchor with a relevant high-exposure tail; HHD-specific tolerability cannot be read from a cohort mean or an assay IC50. A controlled patient-level trial with a specified primary benefit, consistent background care, masked outcome assessment and linked application/exposure records is the proposed next proof. A qualified matched vehicle is preferred where feasible; a transparent randomized whole-product add-on comparison is a concrete alternative. [Product dossier](rux_hhd_product.md) · [Development proof](rux_hhd_development_proof.md)

The company proposition remains less established than the clinical question. Existing public claims, an active franchise and independent HHD publications mean a positive pilot alone does not confer an exclusive drug asset. A new formulation should solve a measured limitation, not merely supply novelty language.

## Reports, data and independent reviews

- Enasidenib: [clinical narrative](enasidenib_clinical.md), [clinical records](enasidenib_clinical.json), [product/proof narrative](enasidenib_product.md), [product records](enasidenib_product.json), [laboratory audit](enasidenib_clinical_audit.json).
- Ruxolitinib: [clinical narrative](rux_hhd_clinical.md), [clinical records](rux_hhd_clinical.json), [clinical audit](rux_hhd_clinical_audit.json), [product narrative](rux_hhd_product.md), [product records](rux_hhd_product.json), [PK/patent audit](rux_hhd_source_audit.json), [development proof](rux_hhd_development_proof.md).
- Independent challenges: [enasidenib clinical/product](review_enas_by_rux_clinical.md), [rux clinical/proof](review_rux_by_enas_clinical.md), [rux product/exposure/rights](rux_hhd_product_review.md).
- [Final independent integration review](integration_review.md).
- [Integrated changes](round7_root_deltas.json), [current shortlist](../../../decisions/current-shortlist.md), [cumulative register](../../portfolio-register.json), [audit commands](../../../methods/reference.md#round-7-clinical-and-exposure-audits).

The reviews' precision changes were incorporated: historical lot identity stays unverified; tolerability claims stay within observed follow-up; cardiac measures account for growth; the proposed rux controlled window is harmonized to 8–12 weeks as a planning assumption; one useful primary dimension does not require superiority on every secondary outcome; responder-enriched maintenance, rescue and missingness retain explicit denominators; current label combination/application context is preserved.

## Verification and publication scope

The original 622 coverage records, generated proposals, rounds 3–6 structured objects, original core-candidate records and continuation files remain unchanged. Schema 7 adds the two developed clinical priorities to the current shortlist and removes their conflicting old reserve/new-priority placements, while snapshotting those prior dispositions in round 6 history. No new candidate or experimental result is manufactured by this reclassification.

Three audits were replayed, source hashes checked, internal Markdown links and JSON parsed, and publication verified against the intended Git tree and expected branch head. Full source papers remain verification intermediates; the repository preserves the research interpretation, extracted source values, provenance and reusable methods. No outreach, procurement, clinical intervention, wet-lab execution or financing is represented.
