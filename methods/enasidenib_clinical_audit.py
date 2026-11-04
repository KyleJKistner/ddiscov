#!/usr/bin/env python3
"""Audit published Gold et al. (2024) Table 1 without correcting its source data.

Input: the public primary full-text XML for PMC11078709, available from
https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11078709/fullTextXML

Example:
  python enasidenib_clinical_audit.py --gold-xml gold2024.xml --output audit.json

This parses one child's repeated measurements. It does not produce an efficacy
estimate, infer the true adverse-event date, or propose a treatment regimen.
Only the Python standard library is required.
"""

import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def clean(element):
    return " ".join("".join(element.itertext()).split())


def audit(source):
    raw = Path(source).read_bytes()
    root = ET.fromstring(raw)
    table = root.find(".//table-wrap[@id='jmd212421-tbl-0001']/table")
    if table is None:
        raise ValueError("Expected primary Table 1 was not found.")
    headings = [clean(x) for x in table.findall("./thead/tr/th")]
    expected = [
        "", "Diagnosis", "Enasidenib initiation", "Enasidenib treatment: 24 h",
        "Enasidenib treatment: 1 month", "Enasidenib treatment: 6 months",
        "Enasidenib treatment: 12 months", "Enasidenib treatment: 18 months",
        "Enasidenib treatment: 24 months", "Enasidenib treatment: 30 months",
        "Reference range",
    ]
    if headings != expected:
        raise ValueError(f"Unexpected column labels: {headings}")
    rows = {}
    for tr in table.findall("./tbody/tr"):
        cells = [clean(x) for x in tr.findall("td")]
        if len(cells) == 1:  # Section headings have colspan=11.
            continue
        if len(cells) != len(headings):
            raise ValueError(f"Column-count mismatch: {cells}")
        rows[cells[0]] = dict(zip(headings[1:], cells[1:]))
    timepoints = headings[1:-1]
    hg_key = next(k for k in rows if "Hydroxyglutaric acid" in k)
    hg, alt, ck = rows[hg_key], rows["Alanine aminotransferase"], rows["CK"]
    before = float(hg["Enasidenib initiation"])
    after = float(hg["Enasidenib treatment: 24 h"])
    return {
        "schema_version": "1.0",
        "evidence_cut": "2026-11-04",
        "source": {
            "doi": "10.1002/jmd2.12421", "pmcid": "PMC11078709",
            "url": "https://onlinelibrary.wiley.com/doi/full/10.1002/jmd2.12421",
            "xml_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11078709/fullTextXML",
            "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
            "table": "Table 1",
        },
        "method": "Parse primary JATS table using its explicit column labels; retain empty cells and source reference intervals. Recompute only stated arithmetic and reference-limit comparisons.",
        "units": {
            "independent_patients": 1, "analyte_series": len(rows),
            "timepoint_columns": len(timepoints),
            "populated_measurement_cells": sum(bool(r[t]) for r in rows.values() for t in timepoints),
            "note": "Measurements are repeated observations from one published child, not independent biological replications or a safety cohort denominator.",
        },
        "table_rows": rows,
        "arithmetic": {
            "reported_urine_2HGA": {
                "unit": "mg/g creatinine", "before": before, "after_24h": after,
                "computed_decrease_percent": 100 * (before - after) / before,
                "body_claim_percent": 84,
                "interpretation": "The table implies approximately 90.6%, not 84%. Preserve the source conflict; this calculation does not establish which biological value or timepoint is correct.",
            },
            "ALT_peak_fold_displayed_ULN": float(alt["Enasidenib treatment: 6 months"]) / 28,
            "ALT31_fold_displayed_ULN": 31 / 28,
            "CK334_fold_displayed_ULN": 334 / 198,
            "CK240_fold_displayed_ULN": 240 / 198,
        },
        "unresolved_source_conflicts": [
            {
                "topic": "Adverse-event timing",
                "table": "ALT 118 and CK 334 occur in the 6-month column; 18-month values are ALT 31 and CK 240.",
                "prose": "The case narrative says persistent elevation was noted 18 months after initiation and then describes dose-frequency reduction.",
                "consequence": "An exact event date or dose-reduction date cannot be reconstructed from this article without silently choosing one account.",
            },
            {
                "topic": "Normalization language",
                "table": "Displayed reference intervals: ALT 0–28 IU/L; CK 45–198 U/L. ALT 31 and CK 240 exceed these upper limits; CK 290 is also listed at 24 months.",
                "prose": "The authors describe post-reduction ALT 31 and CK 240 as normalization.",
                "consequence": "Use laboratory improvement with maintained biochemical suppression, not complete sustained laboratory normalization.",
            },
            {
                "topic": "Biochemical effect arithmetic",
                "table": "Urine 2-HGA 244 before and 23 mg/g creatinine at 24 hours.",
                "prose": "84% decrease within 24 hours.",
                "consequence": "Large prompt suppression is supported; the exact percentage is internally inconsistent.",
            },
            {
                "topic": "Utilization and developmental summaries",
                "table": "No independently linkable visit-level or raw neuropsychological dataset is supplied.",
                "prose": "The abstract uses a 2-year pre-treatment admission interval; body/discussion use 3 years, and prior ED counts differ (5 versus 3). Socialization age-equivalent wording differs (1→9 versus 2→10 months).",
                "consequence": "Retain direction of reported benefit; do not calculate an adjudicated utilization rate or select a single socialization change as corrected data.",
            },
        ],
        "limits": [
            "Author attribution of suspected drug-induced hepatitis is supported by dechallenge; this audit does not independently diagnose liver injury or assign causality.",
            "The reported urine organic-acid measurement is not pooled with separately quantified serum D-2HG or converted across units.",
            "There is no inferred optimal dosing schedule, pediatric PK model, confidence interval or new experimental result.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold-xml", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = audit(args.gold_xml)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "units": result["units"], "arithmetic": result["arithmetic"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
