# Curation and provenance

This page describes the original curated edition, reviewed through 3 November 2026. Later work is indexed in the [research rounds](../research/rounds/README.md). The original archive holds the project registry, source snapshots, public study materials, working papers, analysis files and execution records. Each released section has a different unit of evidence.

| Section | Unit | How to interpret it |
|---|---|---|
| [Development comparisons](../decisions/reference-comparisons.md) | An intervention and a specific decision | A public invitation to collaborate identifies a counterparty. Material access, data rights and a development responsibility require separate evidence. |
| [Program atlas](../atlas/README.md) | A curated program family | A family can contain multiple constructs, doses, models and candidate studies. Evidence is attributed to the intervention actually tested. |
| [Research ledger](../research/history/curated-ledger.md) and [discovery crosswalk](../discovery/README.md) | A phase, topic or attributed screening record | One project can appear in several phases. The ledger incorporates later corrections to the source reviews. |
| [Formulations](../formulations/README.md) | A marketed brand or franchise | The same active ingredient can occur in multiple brands. Sales defined the search universe. Experimental comparisons address specific product properties. |
| [Methods](../methods/README.md) | An assembly, assay panel or donor | Multiple images, numeric readings and model predictions from one donor or construct remain linked to that unit. |

## Tracing a finding

For an external finding, follow the citation beside the result to the paper, supplement, registry, sponsor disclosure or institutional notice. The edition retains the source review's date. Scientific estimates keep their tested dose, model, timing or comparator where these distinctions change interpretation. A source can support several parts of a program with different levels of maturity.

For an internal interpretation, use the phase identifiers in the research ledger. The [archive anchor register](archive-anchors.json) identifies the source registry and reference dossier and gives a SHA-256 fingerprint for selected synthesis, correction and evidence records across all 31 phases. Archive paths are identifiers for holders of the source collection. Public readers can use the article and institutional links directly. The fingerprints identify document versions, independent of agreement with their conclusions.

To verify the 116 source fingerprints, run the following command from the public repository, supplying the directory that contains the original research registry.

```sh
python3 provenance/verify_archive.py "/path/to/original/research-archive"
```

The editorial review used a folder-wide inventory, checks of all 277 registered phase entry points, phase syntheses, correction records and close reading of selected primary studies and original analyses. It preserves contradictory and adverse findings beside the affected intervention. For example, the 40-day cardiac follow-up tested ISP, whereas the two-week scar result involved HJ-02. The earlier time point and the related drug answer different questions. The public edition contains original summaries, compact research indexes and reproducible code. Working correspondence, local configuration, execution logs, downloaded articles and research environments stay in the source archive.

## The component-repair precedent

The Mithril LAMA2 case motivated the program's emphasis on restoring a specific function with existing molecular components. Muscle deficient in laminin-α2 expresses compensatory laminin-411. Investigators built a bispecific antibody to connect laminin-α4 to the muscle-cell protein β-dystroglycan. The report attributes muscle exposure measurements to a **bivalent** tool molecule and a force and grip-strength signal in mice to a **tetravalent** tool molecule. The small, sequential, unblinded cohorts make a prospective comparison important. In the separate α-dystroglycanopathy program the proposed bridge uses laminin-211. Keeping those constructs and indications separate matters when using the case as a precedent. [Technical report, 26 October 2026](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf) · [Research account](https://www.anthropic.com/research/early-progress-drug-development)

## Maintaining the edition

When a new result arrives, record the exact material and model, comparison, endpoint, timing and biological unit. Update the relevant case and its source reference together. If the biology stays the same while access or a collaborator's needs change, date the access or contribution update separately. An analysis replay, a price estimate and a laboratory experiment each belong to a distinct record.
