# BLU3797: source-data and material reconstruction audit

Evidence cut: 4 November 2026. This is a new read-only audit of public source data and chemistry disclosures. It does not report a synthesized compound, a replicated experiment or a legal clearance.

## Decision change

Retain the PIK3C2B/MTM1 program as a leading independent human-function proof. Improve the assessment of public chemical reconstructibility: two patent disclosures describe the exact upstream stereodefined intermediate used in the BLU3797 paper. Reduce confidence in transferring the small late-start dosing comparison literally: the source workbook and supplement do not give a fully reconciled regimen and animal-level record.

The result supports a material/model qualification tranche followed by a human force and tissue-exposure experiment. It does not justify treating the published wire-hang ceiling as normal muscle force or treating the small late-start comparison as an equivalence study.

## 1. The upstream chemistry gap is narrower

The journal describes the final steps from **(S)-5-bromo-2-(1-cyclopropylethyl)-7-fluoroisoindolin-1-one**, named Intermediate 3. Two separate public disclosures now supply routes to that same named stereodefined intermediate:

| Public disclosure | What is actually disclosed | What follows |
|---|---|---|
| [US20240226104A1](https://patents.google.com/patent/US20240226104A1/en), intermediate preparation, steps 1–2 | S-configured fluorobenzamide followed by formation of the matching fluoroisoindolinone | A public upstream route can be joined to the journal's final transformations. Some reported mass/mole entries are internally inconsistent; the text requires chemical reconciliation. |
| [CN119490502A](https://patents.google.com/patent/CN119490502A/en), key intermediate A-1, steps 1–3 | An alternative route ending at A-1-1c with the matching chemical name, S configuration and reported LC-MS | A second publicly disclosed route strengthens reconstruction plausibility. The English machine translation and analytical details still need checking against the original document before experimental use. |
| [Shearer et al., JCI Insight 2026](https://insight.jci.org/articles/view/198568), Methods and Supplemental Figure S7 | Final BLU3797 transformations, molecular identity and analytical observations | These sources together give a plausible public route map. They do not constitute an independently reproduced end-to-end synthesis or demonstrate a currently deliverable lot. |

The two patents concern other PI3K programs. Matching an intermediate does not establish a claim on BLU3797, freedom to operate, a commercial license or additional efficacy evidence. They are used here as chemical disclosures only. A supplier's [PC-26519 listing](https://www.probechem.com/products_BLU3797.html) adds a potential procurement route but remains quote-based. The decisive material evidence is an authenticated lot with the expected stereochemistry, purity and functional potency.

## 2. The underlying workbook can now be inspected

The publisher's [supporting-values workbook](https://df6sxcketz7bb.cloudfront.net/manuscripts/198000/198568/jci.insight.198568.sdval.xlsx) was downloaded from its ordinary public URL and read without modification. It contains **60 worksheets** and 824,614 bytes. SHA-256: `61b73e018b4c294a7df77eb2dd1f6358035fc20d8073071d693ae5678cae0cb3`.

A standard-library reader extracts selected cells and descriptive summaries. An independent openpyxl read agreed on all **815 populated cells** checked across Table 1, Fig 6D, Fig S6A and Fig S6D. This verifies the extraction, not the underlying experiments. Source-cell provenance is retained in the audit JSON. No new p-values or survival analysis were calculated.

### Daily-dose function is visibly exposure dependent and ceiling limited

| Age | Group | Reported wire-hang entries | Mean, seconds | Entries at 60-second ceiling |
|---|---|---:|---:|---:|
| P25 | WT vehicle | 5 | 60.0 | 5 |
| P25 | MTM1 vehicle | 5 | 8.08 | 0 |
| P25 | BLU3797 25 mg/kg | 6 | 27.31 | 1 |
| P25 | BLU3797 50 mg/kg | 6 | 37.68 | 1 |
| P25 | BLU3797 100 mg/kg | 7 | 60.0 | 7 |
| P29 | BLU3797 25 mg/kg | 6 | 11.50 | 0 |
| P29 | BLU3797 50 mg/kg | 6 | 28.08 | 0 |
| P29 | BLU3797 100 mg/kg | 7 | 57.99 | 6 |

Source: workbook **Fig 6D**, rows 4–5. These are descriptive summaries of reported measurements. The P29 vehicle disease group has no measurements in this sheet; missing values are not assigned zero. Matching WT at the 60-second ceiling cannot establish normal specific force, fatigue resistance, or equivalence to WT.

### The late-start comparison needs a narrower interpretation

The [supplement's Figure S6 caption](https://insight.jci.org/articles/view/198568/sd/pdf/render/1) describes twice-daily 75 mg/kg dosing for five days in both start groups. The workbook's **Fig S6A!C2** labels the P22 arm **BIDx5 and QDx3**, whereas D2 labels P25 **BIDx5**. This unresolved discrepancy concerns the regimen used in the survival comparison. Neither source establishes which description should control a replication.

In **Fig S6D**, each start group has only two populated baseline measurements, both 15.9 and 6.4 seconds. Five later measurements appear for each group: P22-start animals at P27 average 59.84 seconds, and P25-start animals at P30 average 53.46 seconds. Later counts decrease. The survival sheet contains five populated P22 event entries and four P25 entries; there are no animal identifiers linking these to the functional observations. Separate cohorts or terminal sampling could explain differences. The public sheet does not settle that question.

The reasonable conclusion is that the reported late-start response is encouraging and that function declines after withdrawal. A fully paired effect estimate, clean equal-regimen comparison or durable disease reversal cannot be reconstructed from these ranges. Identical baseline entries and incomplete linkage are documentation limitations, not evidence of misconduct.

Several values are stored as numbers followed by an asterisk. The reviewed workbook contains no explanatory cell comments; an asterisk key was not found in the examined source. The audit preserves marked values and reports an unmarked-only sensitivity summary where relevant. It does not assume a valid exclusion rule.

### More raw data do not fill the tissue-window gap

Table 1 has cellular assay headers for PIK3C2B, PIK3CA, PIK3C3, PIK3C2G, PIK3CD and PIK3CG. It does not add PIK3C2A or class-I PIK3CB dose-response columns. The right-side concentration block is labeled only 'Concentration', requiring care with units. No new selectivity curve is fitted from that ambiguously labeled block.

Plasma concentration entries do not establish unbound muscle exposure, unbound brain partitioning or chronic neural and hepatobiliary safety. These remain early program variables. The separately identified TAM4MTM trial halt strengthens the reason to test liver function in the relevant disease context; it does not demonstrate BLU3797 hepatotoxicity.

## 3. Revised decisive proof

First authenticate the article and establish a reproducible MTM1-dependent force deficit in a mature human muscle model. Then ask whether treatment begun after the deficit restores force and fatigue at measured exposure, with orthogonal target engagement and useful separation from neural and hepatobiliary dysfunction. A biochemical potency result or a larger myotube is insufficient to advance.

The public route map makes this work more concrete. The source audit makes the experiment more demanding about cohort identity, baseline function, dosing records and attrition. Both changes improve the next decision without requiring an author reply.

## Reproducible artifacts

Within the published repository, see `methods/blu3797_source_audit.py`, `research/source-data/blu3797-source-values.xlsx`, and `research/rounds/round4/blu3797-source-audit.json`. The publisher workbook is unchanged; the JSON and this memo are new analysis. Attribution and license information accompany the archived workbook.
