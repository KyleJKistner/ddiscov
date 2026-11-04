# Public source data used in the review

## BLU3797 supporting values

`blu3797-source-values.xlsx` is an unchanged copy of the publisher's supporting-data workbook for:

Andrew Shearer, Melissa L. Brooks, Maxine M. Chen, Thiwanka Samarakoon, John Hsieh, Gramoz Kondakci, Emanuele Perola, Jason Brubaker, Kristina Fetalvero, Stefanie Schalm, and Joana Caetano-Lopes. **Pharmacological PIK3C2B inhibition rescues XLMTM phenotype in mouse models and identifies molecular markers of disease.** JCI Insight 2026;11(10):e198568. [DOI](https://doi.org/10.1172/jci.insight.198568).

- [Publisher download](https://df6sxcketz7bb.cloudfront.net/manuscripts/198000/198568/jci.insight.198568.sdval.xlsx)
- [Publisher source-data page](https://insight.jci.org/articles/view/198568/sd/3)
- License stated by the article: [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), ©2026 Shearer et al.
- Retrieved 4 November 2026. File size:824,614bytes.
- SHA-256:`61b73e018b4c294a7df77eb2dd1f6358035fc20d8073071d693ae5678cae0cb3`.

The workbook has not been edited. The repository's descriptive [audit](../rounds/round4/blu3797-audit.md) and [derived JSON](../rounds/round4/blu3797-source-audit.json) are separate analysis, not statements by the source authors. They can be regenerated with [the standard-library Python reader](../../methods/blu3797_source_audit.py).

## Later analyses and external source verification

The same unchanged BLU workbook supports the [round-5 cell-context extraction](../rounds/round5/blu3797-cell-context-audit.json) and [human-proof interpretation](../rounds/round5/blu3797-human-proof.md). A second parser matched 887 populated cells across eleven additional sheets; extraction agreement does not validate the biological experiment.

The [P2 audit](../rounds/round5/p2-off-target-audit.json) records the publisher supplement URL, archive size and SHA-256, all 87 assay values, and source-page/assay classes. The archive is an axon figure and off-target table, not animal-level efficacy data.

The [Darier comparator record](../rounds/round5/round5_ndc_comparator_update.json) records stable public CTIS document resolvers and hashes for the recovered English and Swedish reports. The English report independently matched 481,600 bytes and SHA-256 `8cc599c0f33308d66f03e337272238433ad85afee9ce860add2329d12fba996c`. These are final-submitted sponsor results retaining internal draft labels; no participant-level reanalysis or peer-reviewed status is inferred. Temporary signed download URLs are not stored.
