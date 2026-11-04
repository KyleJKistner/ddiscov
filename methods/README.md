# Measuring function across constructs, donors, and assays

The analyses below show how the choice of experimental unit changes what a result can answer. They use Python 3.9+ and its standard library; the round-7 ruxolitinib PDF extraction also requires Poppler pdftotext, as specified below. The numerical results are project reanalyses of published experiments. Each source supplies the measurements.

## WNT receptor context

Tao and colleagues built antibodies with two binding arms for Frizzled receptors and two for LRP6. In one design the two Frizzled arms both target FZD5. That antibody induced a mean 2.01-fold reporter signal in HEK cells. In a different assay, the same antibody restored normalized seven-day proliferation of HPAF-II pancreatic cancer cells to 0.835 during WNT secretion blockade, versus 0.100 with the blocker alone. This contrast motivates recording functional activity separately for each construct, cell type, and endpoint. [Tao et al., Figures 3C and 3D](https://elifesciences.org/articles/46134#fig3)

The reconstruction uses an earlier genetic perturbation study implicating FZD1, FZD2, and FZD7 in HEK293T cells and an earlier study identifying FZD5 dependence in HPAF-II cells. A binary feature records whether the assembly binds any receptor in the corresponding set. The feature uses empirical binding specificity. We chose the rule with the qualitative outcomes already known. The HEK reporter caption names HEK293, whereas the general methods name HEK293T. Exact cell-line equivalence across the two studies remains uncertain. [HEK receptor perturbation](https://pmc.ncbi.nlm.nih.gov/articles/PMC5636703/) · [Pancreatic tumor receptor dependence](https://pubmed.ncbi.nlm.nih.gov/27869803/)

Run from the repository root.

```sh
python3 methods/wnt_context.py
```

The script fits each panel separately. It holds out one assembly, standardizes the overlap feature on the training assemblies, and fits ridge regression with penalty 1 and an unpenalized intercept. The comparison predicts the training-set mean. Each held-out assembly contributes one equally weighted error. The four or five assemblies per panel allow a reconstruction of this study's response pattern. Generalization to a new assembly family would require additional families and a prospective test.

| Published panel | Assemblies | Response used in fit | Mean-only RMSE | Receptor-context RMSE |
| --- | ---: | --- | ---: | ---: |
| HEK reporter, 3D | 5 | log₂ of mean fold induction | 3.4022 | 1.0528 |
| HEK reporter, 3D, sensitivity | 5 | same, omitting one author-flagged reading | 3.3329 | 0.9532 |
| HPAF-II proliferation, 3C | 4 | normalized proliferation fraction | 0.4583 | 0.1525 |

**Data and attribution.** The [panel means](wnt-panel-means.csv) summarize 12 published panel/arm combinations, including controls. The 3D assembly means each use five reported values of unspecified biological independence. The 3C means use three independent experiments at 100 nM. The 3D dose was unspecified. The primary pan-Frizzled mean of 190.028 includes the starred value. Removing it gives 160.577. Empty binding profiles identify control arms excluded from fitting. The CSV adapts Tao et al. (2019) by aggregating source values and attaching binding specificities. It is distributed under the source's CC BY 4.0 license. [3C source data](https://cdn.elifesciences.org/articles/46134/elife-46134-fig3-data3-v1.txt) · [3D source data](https://cdn.elifesciences.org/articles/46134/elife-46134-fig3-data4-v1.txt) · [License](https://creativecommons.org/licenses/by/4.0/)

The broader WNT inventory mapped 23 assembly identities. Seven had complete published sequences, including the five in the 3D comparison. Across six panels, 451 raw functional values yielded 102 condition summaries, including controls and auxiliary dose curves. A separate reproduction of the full archived baseline suite matched 327 held-out predictions and 108 error metrics. Those counts describe repeated fits and sensitivity analyses of a small published collection. The command above reproduces the two receptor-context comparisons and the flagged-value sensitivity.

## Airway particle transport across donors

Hadas and colleagues measured movement of particles on ciliated airway cultures. Their workbook contains 602 recordings from 14 primary ciliary dyskinesia (PCD) donors and 10 controls. A donor can contribute dozens of recordings. Splitting those recordings individually could put the same donor on both sides of a comparison. [Hadas et al.](https://www.nature.com/articles/s42003-026-11149-0)

Download the publisher's workbook and run the analysis from the repository root.

```sh
curl -fL -o airway-transport.xlsx 'https://media.springernature.com/full/springer-static/esm/art%3A10.1038%2Fs42003-026-11149-0/MediaObjects/42003_2026_11149_MOESM6_ESM.xlsx'
python3 methods/airway_transport.py airway-transport.xlsx
```

The script verifies the workbook checksum, takes each donor's median straight-line particle speed, then holds out that donor. It fits the threshold on the other 23 donors to maximize balanced accuracy, counting lower speed as PCD and taking the lowest threshold when tied. It prints only aggregate results. The analysis classified **13 of 14 PCD donors and 9 of 10 controls** correctly. The mean of those two class-specific rates was 0.9143. This baseline measures separation between untreated donor groups. Evaluating ODAD1 replacement requires transport measurements in treated, genotype-matched tissue. [Publisher workbook, Supplementary Data 1](https://media.springernature.com/full/springer-static/esm/art%3A10.1038%2Fs42003-026-11149-0/MediaObjects/42003_2026_11149_MOESM6_ESM.xlsx)

## Other quantitative comparisons

| Comparison | Observed result | What a subsequent experiment could establish |
| --- | --- | --- |
| YC-001 and mutant rhodopsin trafficking | In 27 variants shared between studies, six of the 16 with a significant increase in a 30 µM reporter assay also had a significant increase in 40 µM cell imaging. The other ten were unstarred in imaging. Of the eleven without a significant positive reporter call, one increased in imaging, eight were unstarred and two decreased. An unstarred measurement carries uncertainty about the effect. | Both P23H and P23L improved in the reporter. Only P23H increased significantly in imaging. The pair could test whether those assay readouts transfer to rod function. [Reporter study](https://doi.org/10.1126/sciadv.aef3518) · [Imaging study, Fig. 1A](https://doi.org/10.1172/jci.insight.153717) |
| MAP3K15 compound ranking | The 645 PKIS2 compound rows resolved to 640 parent compounds and 369 scaffolds. Ten exceeded or equaled 80% competition-binding inhibition. In five scaffold-separated folds, a fingerprint-based tree model yielded pooled RMSE of 16.33 versus 17.38 percentage points for a training-mean baseline. Its pooled top 32 contained two positives. The folds contained 2, 2, 0, 1 and 5 positives and used different fitted models. | A fresh compound panel and catalytic counterassays could test retrieval and selectivity at the actual experimental budget. The source assay measured binding competition at a single concentration. [Drewry et al., dataset S4](https://doi.org/10.1371/journal.pone.0181585.s004) |
| Choosing an informative experiment | In an internal simulation, adaptive selection gained about four percentage points over a tuned fixed design when the assumed mechanisms generated the observations. With a simulated, omitted mechanism that gave the same signal in the designated check, 59.24% of runs made a confident wrong call that passed the check. | Identify a measurement that separates the competing mechanisms, estimate noise in the target assay, and compare fixed and adaptive designs at equal cost. These percentages describe simulated trials. |

## BLU3797 source-data audit

The round-4 audit reads the publisher's unchanged supporting workbook, preserves cell addresses and marked values, and calculates descriptive summaries. It does not fit new efficacy statistics, impute missing measurements or link unidentified animals across panels. An independent openpyxl extraction agreed on all 815 populated cells checked in four selected sheets.

Run from the repository root:

```bash
python methods/blu3797_source_audit.py --source research/source-data/blu3797-source-values.xlsx --output research/rounds/round4/blu3797-source-audit.json
```

Read the [interpretation and limitations](../research/rounds/round4/blu3797-audit.md), [derived data](../research/rounds/round4/blu3797-source-audit.json), and [source attribution/license](../research/source-data/README.md). An assay ceiling, a regimen-header discrepancy and incomplete panel linkage limit inference. Extraction agreement verifies the reader, not the underlying experiments.

## BLU3797 cell and lipidomic context

Round 5 extends the unchanged workbook audit to Figure 3, Supplemental Figure 2 and Figure 5E–F. Independent openpyxl extraction matched 887 populated cells across eleven sheets. These do not overlap the four sheets checked in round 4.

```bash
python methods/blu3797_cell_context_audit.py --source research/source-data/blu3797-source-values.xlsx --output research/rounds/round5/blu3797-cell-context-audit.json
```

The script preserves asterisk-marked values, cell addresses and group labels. Means are descriptive; technical fields do not become independent cultures, and no cross-panel pairing or new significance test is manufactured. Figure 5E–F deliberately uses VPS34/PIK3C3-knockout cells; its labels agree with the article. Read the [human-proof interpretation](../research/rounds/round5/blu3797-human-proof.md) and [derived audit](../research/rounds/round5/blu3797-cell-context-audit.json).

The separate [P2 panel extraction](../research/rounds/round5/p2-off-target-audit.json) preserves 87 single-concentration assay entries with source pages and assay classes. Its [interpretation](../research/rounds/round5/p2-off-target-audit.md) distinguishes binding displacement from catalytic inhibition and electrical function. It does not generate new selectivity curves or an animal efficacy analysis.


## Round 7 clinical and exposure audits

Three scripts preserve source units and reproducible arithmetic. They do not estimate a new controlled clinical efficacy effect or a population safety rate.

**Enasidenib:** download the [Gold primary XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11078709/fullTextXML), then run:

```bash
python methods/enasidenib_clinical_audit.py --gold-xml /path/to/gold2024.xml --output /path/to/enasidenib-audit.json
```

The script extracts 177 populated cells across 23 laboratory series from one child and preserves reference intervals, timestamps and source conflicts. [Derived audit](../research/rounds/round7/enasidenib_clinical_audit.json) · [Interpretation](../research/rounds/round7/enasidenib_clinical.md)

**Ruxolitinib clinical ledger:** the committed structured dossier contains the transcribed primary values and their source/access records. Run from the repository root:

```bash
python methods/rux_hhd_clinical_audit.py --input research/rounds/round7/rux_hhd_clinical.json --output /path/to/rux-clinical-audit.json
```

This checks case/duplicate accounting, reconstructs DERM101 response numerators from reported percentages/denominators, and recomputes the 17-row biopsy-demographic table. It does not recover individual trial records or resolve undisclosed missingness. [Audit](../research/rounds/round7/rux_hhd_clinical_audit.json)

**Ruxolitinib exposure and official patent snapshot:** obtain the four exact source files named in the script's `SOURCES` mapping: two EuropePMC XMLs, the Springer maximum-use supplement and the official FDA Orange Book ZIP. Preserve their downloaded filenames. The script uses the Python standard library and Poppler `pdftotext`:

```bash
python methods/rux_hhd_source_audit.py --source-dir /path/to/source-files --output /path/to/rux-source-audit.json
```

It verifies source-byte hashes, extracts primary PK tables, preserves the five selected high-exposure participants from the original 41-person study, and separates patent rows from distinct patent numbers. The official ZIP is a mutable endpoint; this review's internal file dates are 9 October 2026. A later checksum mismatch requires source review rather than automatic substitution. The [committed audit](../research/rounds/round7/rux_hhd_source_audit.json) preserves all selected table values and official product/patent/exclusivity rows, even if a later source version changes. [Interpretation](../research/rounds/round7/rux_hhd_product.md)
