# Public model routes for 8015-P2 and NDC9009

> **Historical review snapshot.** Later findings and rankings are reconciled in the [current shortlist](../../../decisions/current-shortlist.md) and [round 4 review](../round4/README.md). Statements about activity or access describe this review period.

**Evidence cut: 4 November 2026.** Bounded public-source search; no outreach, signup, ordering or experimental work. This supplement does not add new drug candidates. It separates three questions: whether a material is publicly defined, whether a physical lot is presently available, and whether the resulting model has qualified useful function.

## Decision

**8015-P2 has a concrete public multi-allele patient-cell repository route. NDC9009 has a publicly specified engineered-model route, but no ready disease-qualified catalog assay was verified.** For both, model qualification remains the first experimental gate. Neither should be presented as waiting for an investigator's opinion about whether the biology is worth pursuing.

## 8015-P2 / CMT2A

NYSCF's public CMTA panel identifies these patient iPSC lines and marks fibroblasts as available for each. [MR01–02]

| Exact line ID | Catalog MFN2 variant | Donor information | What it provides |
|---|---|---|---|
| AG0002-01-MR | H361Y | Male; age unspecified | Patient iPSC/fibroblast starting material |
| AG0008-01-MR | c.2219G>C; protein label printed with a typo as “Tryp740Ser” | Female,39 | Patient iPSC/fibroblast starting material; verify HGVS by sequencing |
| AG0015-01-MR | R364W | Female; age unspecified | Patient iPSC/fibroblast starting material |

These are distinct listed mutation backgrounds, independent of the original P2 investigators' T105M patient culture. They are **not** demonstrated P2-responsive neurons or a ready motor-neuron/muscle functional assay. The examined panel contains isogenic control rows for other genes; those cannot be treated as MFN2 controls.

**Availability limitation:** NYSCF's current page says its search function is being updated and availability is handled by request. The PDFs identify the materials, but their upload paths and printed version dates differ; the current page also links an older2017 panel. Present inventory, lead time and recipient terms were not established. No exactT105M patient catalog entry was found in this bounded search. [MR01–03]

### Proposed usable route

The initial experimental specification can name two or more of these backgrounds and require allele/line authentication, mature neuronal/NMJ deficits, and genetic correction/restoration controls. Choose fibroblast direct conversion or iPSC differentiation as an explicit model-design decision. Neither route inherits the original study's phenotype or donor age simply from the disease label.

If exactT105M anchoring is needed, engineering that variant into an independently available parent is a separate model-development task. It should be scored as an isogenic engineered model, not another patient or a claim that the original investigator's cells are available. A negative drug result is interpretable only once the deficit and positive-control rescuability are established.

## NDC9009 / Darier disease

### A patient-cell listing exists, but it is not the immediate solution

ATCC **Lei Cap, CRL-1098**, is a female62-year-old skin fibroblast line labeled Darier-White disease with an extensive family history. The public page does not identify its ATP2A2 variant. It is a **Mission Collection Item**. [MR04]

ATCC states that Mission Collection items are outside standard inventory and require an inventory check and potentially a special production run. Its general policy gives approximately six months and a minimum$5,000 per vial for most such items; this is not a quote or delivery promise for Lei Cap. [MR05]

Do not describe this as immediately procurable patient keratinocytes. Even if recovered, it would require mutation confirmation, reprogramming/differentiation and disease-model qualification. Keep it as a defined patient-material reserve rather than the dependency for the first functional experiment.

### The published engineered model is specific enough to rebuild

JCI Insight170739 uses **N/TERT-2G** keratinocytes and ATP2A2 exon1 editing to create heterozygous frameshift and null clones. The paper specifies guide identities and PX458/Addgene48138, and documents adhesion/calcium phenotypes and organotypic abnormalities. It reports three independent experiments for the adhesion comparison; those are not three patient donors. The genetic organotypic model did not reproduce full acantholysis. [MR06]

The original parent was a gift. Cellosaurus identifies N/TERT-2 as N/TERT-2G and points to a BWH collection list, which indeed lists the line. This is a public material identity and institutional collection route, not verified present stock. No standard catalog entry for the exact mutant clones was found. [MR08–09]

One concrete eligibility limitation matters: **Addgene48138 is listed for academics/nonprofits only and is not available to industry.** Do not silently promise it to an unspecified commercial recipient. [MR07]

### An independent rebuilding branch

An alternative parent can be specified now: **ATCC Ker-CT, CRL-4048**, a cataloged immortalized human keratinocyte line with organotypic-culture precedent. Alternatively, primary adult **HEKa C0055C** or neonatal **HEKn C0015C** are cataloged by Thermo Fisher. These are different parents and carry no Darier mutation. [MR10–11]

Applying the published ATP2A2 perturbation concept to one of these parents would be **new model engineering and qualification**, not a verified reproduction of the JCI model. A commercial Cas9-protein/synthetic-guide workflow provides a separately specified editor route if PX458 eligibility does not fit; it does not confer rights to the original plasmid or eliminate validation. [MR12]

For the proposed residual-SERCA2 activation hypothesis, the primary efficacy model should retain a functioning allele. Use a null clone as a mechanistic boundary control. First establish a stable, rescuable mechanical adhesion/barrier deficit in the heterozygous model, then test NDC9009 after that deficit is present. Avoid letting easier procurement turn an unqualified engineered line or a chemically poisoned pump into the decisive disease assay.

## Consequence for the shortlist

The CMT result makes the proposed P2 human study more concrete but leaves stock and functional qualification open. The Darier result is mixed: there is a real patient-cell catalog entry, yet its production status and missing genotype make it a poor immediate dependency. The stronger short-term proposition is a defined engineered human-epidermis model with a funded qualification gate.

These findings should replace a binary “available/unavailable” label with explicit statuses. They support making scientific selection now while preserving the limits of what public evidence establishes. They do not justify claiming that the proposed experiments can begin tomorrow or that a supplier listing validates efficacy.

## Sources

- **MR01** — [NYSCF CMTA iPSC/fibroblast panel](https://www.nyscf.org/wp-content/uploads/2025/05/Available-iPSCs_CMTA_051525.pdf). primary repository catalog.

- **MR02** — [NYSCF February-path catalog](https://nyscf.org/wp-content/uploads/2025/02/Available-iPSCs_CMTA_020425.pdf). primary repository catalog.

- **MR03** — [Current NYSCF repository page](https://www.nyscf.org/resources/stem-cell-search/). primary repository page.

- **MR04** — [Lei Cap Darier patient fibroblast](https://www.atcc.org/products/crl-1098). primary catalog.

- **MR05** — [ATCC Mission Collection availability policy](https://www.atcc.org/forms/mission-collection-items). primary supplier policy.

- **MR06** — [Zaver et al. SERCA2 organotypic epidermis model](https://insight.jci.org/articles/view/170739/). primary article.

- **MR07** — [PX458 Addgene48138](https://www.addgene.org/48138/). primary catalog.

- **MR08** — [BWH Cell Culture Core collection list](https://dermatology.bwh.harvard.edu/docs/Cell-Culture-Core-Cell-Lines.pdf). primary institutional collection list.

- **MR09** — [Cellosaurus N/TERT-2 identity](https://www.cellosaurus.org/CVCL_UZ62). curated identity registry.

- **MR10** — [ATCC Ker-CT CRL4048](https://www.atcc.org/products/cells_and_microorganisms/htert_immortalized_cell_lines/foreskin_keratinocytes/crl-4048). primary catalog.

- **MR11** — [Primary adult/neonatal human keratinocyte catalog](https://www.thermofisher.com/us/en/home/life-science/cell-culture/primary-cell-culture/keratinocyte-culture.html). primary catalog.

- **MR12** — [Commercial Cas9 protein reagent route](https://www.thermofisher.com/order/catalog/product/A36499). primary catalog.
