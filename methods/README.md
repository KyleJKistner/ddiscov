# Methods

Reproduce published-data audits and planning calculations with Python 3.9+. Run commands from the repository root. Outputs describe the cited studies and historical audit scope; use the [current shortlist](../decisions/current-shortlist.md) for portfolio decisions. Detailed results, attribution and limitations are in [historical method notes](reference.md).

## Run with files already in the repository

These commands use the Python standard library. Write generated JSON to a temporary directory while checking reproducibility:

```sh
mkdir -p /tmp/ddiscov-audits
python3 methods/wnt_context.py
python3 methods/blu3797_source_audit.py --source research/source-data/blu3797-source-values.xlsx --output /tmp/ddiscov-audits/blu-source.json
python3 methods/blu3797_cell_context_audit.py --source research/source-data/blu3797-source-values.xlsx --output /tmp/ddiscov-audits/blu-cells.json
python3 methods/blu3797_identity_audit.py --out /tmp/ddiscov-audits/blu-identity.json
python3 methods/rux_hhd_clinical_audit.py --input research/rounds/round7/rux_hhd_clinical.json --output /tmp/ddiscov-audits/rux-clinical.json
python3 methods/blu3797_qualification_decisions.py self-check
python3 methods/blu3797_qualification_decisions.py check research/rounds/round8/blu3797-decision-input-template.json
```

| Method | Output and interpretation |
| --- | --- |
| WNT context | Prints held-out prediction errors for two published panels and a sensitivity analysis. Small retrospective assembly comparison. |
| BLU source | JSON of workbook cells and descriptive summaries; compare with [Round 4 audit](../research/rounds/round4/blu3797-source-audit.json). |
| BLU cell context | JSON of additional cell/lipidomic panels; compare with [Round 5 audit](../research/rounds/round5/blu3797-cell-context-audit.json). |
| BLU identity | Formula-derived masses and source arithmetic; compare with [Round 8 audit](../research/rounds/round8/blu_identity_numeric_audit.json). |
| Ruxolitinib clinical | JSON checking case accounting and aggregate arithmetic; compare with [Round 7 audit](../research/rounds/round7/rux_hhd_clinical_audit.json). |
| Qualification `self-check` | Prints results of synthetic decision-logic checks. |
| Qualification `check` | Prints classification of the supplied decision record. The blank template returns `not_run_planning_only`; biological interpretation follows the [qualification package](../research/rounds/round8/blu3797-qualification-package.md). |

## Run with external inputs

Download the stated inputs to `/tmp/ddiscov-audits` first. Source URLs, versions and interpretation are recorded in the linked notes. The commands assume those exact filenames.

| Method | Required input and additional dependency |
| --- | --- |
| [Airway transport](reference.md#airway-particle-transport-across-donors) | Publisher workbook saved as `airway-transport.xlsx`; verifies the pinned checksum. Prints donor-held-out classification results. |
| [Enasidenib clinical](reference.md#round-7-clinical-and-exposure-audits) | Gold primary XML saved as `gold2024.xml`. Writes the one-child laboratory-series extraction. |
| [Ruxolitinib source](rux_hhd_source_audit.py) | Four files named in the script's `SOURCES` mapping; Poppler `pdftotext`. Writes PK tables and the historical Orange Book snapshot. |
| [Fluoxetine endpoints](reference.md#round-8-blu-identity-qualification-decisions-and-one-child-source-audit) | Primary XML saved as `fluoxetine-source.xml`. Writes seven published model summaries from one participant. |

```sh
python3 methods/airway_transport.py /tmp/ddiscov-audits/airway-transport.xlsx
python3 methods/enasidenib_clinical_audit.py --gold-xml /tmp/ddiscov-audits/gold2024.xml --output /tmp/ddiscov-audits/enasidenib.json
python3 methods/rux_hhd_source_audit.py --source-dir /tmp/ddiscov-audits --output /tmp/ddiscov-audits/rux-source.json
python3 methods/fluoxetine_endpoint_audit.py /tmp/ddiscov-audits/fluoxetine-source.xml /tmp/ddiscov-audits/fluoxetine.json
```

The ruxolitinib bundle pins an Orange Book archive with internal dates of 9 October 2026. A checksum mismatch identifies a different source version and needs review before reproducing that historical audit.

## Optional planning calculation

Install SciPy in your chosen Python environment, then run:

```sh
python3 methods/blu3797_qualification_decisions.py planning
```

This prints conditional t-interval widths using explicitly assumed variability. Assumptions and the saved output are in the [planning audit](../research/rounds/round8/qualification-planning-audit.json).
