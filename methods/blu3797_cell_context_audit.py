#!/usr/bin/env python3
"""Descriptive, read-only audit of BLU3797 cell-assay and lipidomics context.

The source workbook contains representative imaging observations, not a complete
experiment-by-well hierarchy. This script does not fit dose-response curves,
recompute significance, treat fields as biological replicates, or infer force.

Run from the repository root:
  python methods/blu3797_cell_context_audit.py \
    --source research/source-data/blu3797-source-values.xlsx \
    --output research/rounds/round5/blu3797-cell-context-audit.json
"""
import argparse
import hashlib
import json
import re
import statistics
from pathlib import Path

from blu3797_source_audit import read_cells, URL


def column_summary(cells, sheet, column, first_row, last_row):
    records = []
    for row in range(first_row, last_row + 1):
        address = f"{column}{row}"
        value = cells.get(address)
        if value is None:
            continue
        marked = isinstance(value, str) and value.endswith("*")
        if isinstance(value, (float, int)):
            number = float(value)
        elif marked and re.fullmatch(r"-?\d+(\.\d+)?\*", value):
            number = float(value[:-1])
        else:
            raise ValueError(f"Unexpected value at {sheet}!{address}: {value!r}")
        records.append({"cell": address, "source_value": value,
                        "numeric_value": number, "asterisk": marked})
    numbers = [r["numeric_value"] for r in records]
    unmarked = [r["numeric_value"] for r in records if not r["asterisk"]]
    return {
        "range": f"{column}{first_row}:{column}{last_row}",
        "reported_entries": len(numbers),
        "mean_including_marked": statistics.mean(numbers) if numbers else None,
        "median_including_marked": statistics.median(numbers) if numbers else None,
        "range_including_marked": [min(numbers), max(numbers)] if numbers else None,
        "marked_entries": len(numbers) - len(unmarked),
        "mean_unmarked_sensitivity_only": statistics.mean(unmarked) if unmarked else None,
        "source_cells": records,
    }


def audit(source):
    sheets = read_cells(source)
    imaging = []
    for sheet in ("Fig 3B", "Fig 3C", "Fig 3D", "Fig 3E", "Fig 3F", "Fig 3G"):
        cells = sheets[sheet]
        groups = []
        for column in "ABCDEF":
            group = column_summary(cells, sheet, column, 3, 12)
            group["source_group_label"] = cells[f"{column}2"]
            group["nominal_concentration_nM"] = None if column == "A" else float(cells[f"{column}2"])
            groups.append(group)
        imaging.append({"sheet": sheet, "source_title": cells["A1"],
                        "model": "Selected MTM1-null C2C12 clone",
                        "groups": groups})
    depleted = []
    for sheet in ("FigS2B ", "FigS2C", "FigS2D"):
        cells = sheets[sheet]
        groups = []
        for column in "ABCDEFG":
            group = column_summary(cells, sheet, column, 4, 13)
            group["source_group_label"] = cells[f"{column}3"]
            group["nominal_concentration_nM"] = None if column in "AB" else float(cells[f"{column}3"])
            groups.append(group)
        depleted.append({"sheet": sheet, "source_title": cells["A1"],
                         "model": "PIK3C2B-depleted MTM1-null C2C12 cells; source caption, not healthy WT",
                         "groups": groups})
    pca = sheets["Fig 5E"]
    pca_records = [{"source_row": row, "label": pca[f"A{row}"],
                    "PC1": pca[f"B{row}"], "PC2": pca[f"C{row}"]}
                   for row in range(3, 19)]
    lipid = sheets["Fig 5F"]
    lipid_records = [{"source_row": row, "lipid_class": lipid[f"A{row}"],
                      "reported_KO_treatment_effect": lipid[f"B{row}"],
                      "reported_WT_treatment_effect": lipid[f"C{row}"],
                      "reported_KO_p_value": lipid[f"D{row}"],
                      "reported_WT_p_value": lipid[f"E{row}"],
                      "reported_KO_significance_flag": lipid[f"F{row}"],
                      "reported_WT_significance_flag": lipid[f"G{row}"]}
                     for row in range(3, 24)]
    return {
        "as_of": "2026-11-04",
        "source_url": URL,
        "article_url": "https://insight.jci.org/articles/view/198568",
        "article_doi": "10.1172/jci.insight.198568",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "source_bytes": source.stat().st_size,
        "workbook_sheet_count": len(sheets),
        "method": "Descriptive extraction with source cells. No fitted potency, new p-values, pooled biological n, or missing-value imputation.",
        "cell_imaging_context": {
            "selected_clones": "The article selected one MTM1-null clone after observing clone heterogeneity and impaired myogenesis even in nontargeting controls.",
            "timing": "Compound added after 72 hours of differentiation, then imaged after a further 48 hours. This is treatment during differentiation, not pretreatment from differentiation day zero and not established mature-force reversal.",
            "reported_repetition": "Figure3 calls B-E representative quantification from three independent experiments; B-G use five random nonoverlapping fields and report n=10. Complete experiment/well/field identifiers are absent from these source sheets.",
            "inference_unit": "Ten reported values per group cannot be relabeled ten independent cultures, donors or experiments.",
            "asterisks": "Numeric strings bearing an asterisk are retained. An unmarked-only mean is a descriptive sensitivity calculation, not an authorized exclusion.",
            "endpoint": "Fusion index, nuclei per MYH-positive structure and structure count are morphology. They do not measure twitch force, tetanic force, fatigue or respiratory performance.",
            "S2_context": "S2 is target-depleted MTM1-null cells. Its baseline is not a WT normalization denominator for Figure3.",
            "cross_panel_linkage": "Row positions alone do not establish matched images or experimental blocks across panels; no cross-panel product, paired test or shared baseline is computed.",
        },
        "main_imaging": imaging,
        "target_depleted_imaging": depleted,
        "lipidomic_context": {
            "model": "PIK3C3/VPS34-KO and PIK3C3-WT C2C12 cells, each with or without 1 micromolar PIK3C2B inhibitor",
            "context_consistency": "The PIK3C3 labels in Fig5E are consistent with the article caption, Results and Methods. They are not a labeling discrepancy.",
            "separate_from": "Figure5A-D proteomics/phosphoproteomics uses MTM1-null mouse muscle with versus without constitutive PIK3C2B kinase inactivation.",
            "reported_pca_group_entries": 4,
            "reported_lipid_classes": len(lipid_records),
            "reported_KO_nominal_significance_flags": sum(r["reported_KO_significance_flag"] == "S" for r in lipid_records),
            "reported_WT_nominal_significance_flags": sum(r["reported_WT_significance_flag"] == "S" for r in lipid_records),
            "multiplicity": "Figure5F reports significance at P<0.05 and this sheet contains p.value columns without adjusted q-value columns. No new multiplicity correction is asserted.",
            "interpretation": "This separate lipid-kinase perturbation experiment cannot be presented as direct lipidomic normalization of MTM1-null human muscle by BLU3797, nor as a validated functional-response biomarker.",
            "pca_records": pca_records,
            "lipid_class_records": lipid_records,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"source_sha256": result["source_sha256"],
                      "main_imaging_panels": len(result["main_imaging"]),
                      "target_depleted_panels": len(result["target_depleted_imaging"]),
                      "lipid_classes": result["lipidomic_context"]["reported_lipid_classes"]}))


if __name__ == "__main__":
    main()
