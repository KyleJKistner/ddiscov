#!/usr/bin/env python3
"""Read-only audit of the public BLU3797 supporting-data workbook.

No fitted efficacy model or significance test is performed. Numeric cells with
asterisks are retained and flagged. Counts describe reported entries, not an
inferred number of independent animals. Uses the Python standard library only.

Run from the repository root:
  python methods/blu3797_source_audit.py \
    --source research/source-data/blu3797-source-values.xlsx \
    --output research/rounds/round4/blu3797-source-audit.json
"""
import argparse
import hashlib
import json
import posixpath
import re
import statistics
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
URL = "https://df6sxcketz7bb.cloudfront.net/manuscripts/198000/198568/jci.insight.198568.sdval.xlsx"


def read_cells(path):
    """Preserve source cell contents; do not evaluate or rewrite the workbook."""
    with ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            shared = ["".join(s.itertext()) for s in root.findall("m:si", NS)]
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels}
        workbook = ET.fromstring(z.read("xl/workbook.xml"))
        sheets = {}
        for s in workbook.findall("m:sheets/m:sheet", NS):
            target = targets[s.attrib[f"{{{REL_NS}}}id"]]
            filename = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
            cells = {}
            for c in ET.fromstring(z.read(filename)).findall(".//m:sheetData/m:row/m:c", NS):
                v = c.find("m:v", NS)
                if c.attrib.get("t") == "inlineStr":
                    value = "".join(c.find("m:is", NS).itertext())
                elif v is None or v.text is None:
                    continue
                elif c.attrib.get("t") == "s":
                    value = shared[int(v.text)]
                elif c.attrib.get("t") in ("str", "e"):
                    value = v.text
                else:
                    value = float(v.text)
                    if value.is_integer():
                        value = int(value)
                cells[c.attrib["r"]] = value
            sheets[s.attrib["name"]] = cells
        return sheets


def col(n):
    result = ""
    while n:
        n, r = divmod(n - 1, 26)
        result = chr(65 + r) + result
    return result


def summary(sheets, sheet, row, first_col, last_col):
    selected = []
    for i in range(first_col, last_col + 1):
        address = f"{col(i)}{row}"
        value = sheets[sheet].get(address)
        if value is None:
            continue
        marked = isinstance(value, str) and value.endswith("*")
        if isinstance(value, (float, int)):
            number = float(value)
        elif marked and re.fullmatch(r"-?\d+(\.\d+)?\*", value):
            number = float(value[:-1])
        else:
            raise ValueError(f"Unexpected value at {sheet}!{address}: {value!r}")
        selected.append({"cell": address, "source_value": value, "numeric_value": number, "asterisk": marked})
    values = [x["numeric_value"] for x in selected]
    unmarked = [x["numeric_value"] for x in selected if not x["asterisk"]]
    return {
        "sheet": sheet,
        "range": f"{col(first_col)}{row}:{col(last_col)}{row}",
        "reported_entries": len(values),
        "mean_including_marked": statistics.mean(values) if values else None,
        "median_including_marked": statistics.median(values) if values else None,
        "range_including_marked": [min(values), max(values)] if values else None,
        "entries_at_60_second_ceiling": sum(v == 60 for v in values),
        "marked_entries": len(values) - len(unmarked),
        "mean_unmarked_sensitivity_only": statistics.mean(unmarked) if unmarked else None,
        "source_cells": selected,
    }


def audit(source):
    sheets = read_cells(source)
    daily = []
    groups = [("WT_vehicle", 2, 6), ("MTM1_vehicle", 9, 13), ("BLU3797_25_mg_kg", 16, 21), ("BLU3797_50_mg_kg", 22, 27), ("BLU3797_100_mg_kg", 28, 34)]
    for row in (3, 4, 5):
        for group, first, last in groups:
            x = summary(sheets, "Fig 6D", row, first, last)
            x.update(group=group, age_days=sheets["Fig 6D"][f"A{row}"])
            daily.append(x)
    withdrawal = []
    for group, first, last in [("start_P22", 2, 6), ("start_P25", 7, 11)]:
        for row in range(4, 13):
            x = summary(sheets, "Fig S6D", row, first, last)
            if x["reported_entries"]:
                x.update(group=group, age_days=sheets["Fig S6D"][f"A{row}"])
                withdrawal.append(x)
    tab = sheets["Table 1"]
    headers = {k: v for k, v in tab.items() if isinstance(v, str) and v.startswith("PIK3")}
    return {
        "as_of": "2026-11-04",
        "source_url": URL,
        "article_doi": "10.1172/jci.insight.198568",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "source_bytes": source.stat().st_size,
        "workbook_sheet_count": len(sheets),
        "method": "Descriptive extraction with source-cell provenance. No new p-values, cohort linkage, survival inference, or missing-value imputation.",
        "interpretation_limits": [
            "Counts are populated measurement entries. Animal IDs and linkage across panels are not supplied in these ranges.",
            "Asterisks appended to numeric strings are retained. No explanatory cell comments or asterisk key was found in the examined source. Unmarked-only means are sensitivity descriptions, not authorized exclusions.",
            "The 60-second ceiling makes a matching wire-hang result insufficient to establish equivalence of muscle force.",
            "Supplemental survival labels and caption differ on the P22 dosing course; the reported late-start benefit remains provisional for exact regimen transfer.",
            "Two baseline entries in each S6D group do not provide a paired baseline for all five later observations.",
            "The source workbook does not supply free muscle/brain exposure or replace functional target-window experiments.",
        ],
        "daily_wire_hang_seconds": daily,
        "withdrawal_wire_hang_seconds": withdrawal,
        "supplemental_survival_headers": {k: sheets["Fig S6A"][k] for k in ("C2", "D2")},
        "supplemental_survival_nonempty_event_entries": {
            "start_P22": sum(f"C{i}" in sheets["Fig S6A"] for i in range(3, 12)),
            "start_P25": sum(f"D{i}" in sheets["Fig S6A"] for i in range(3, 12)),
            "note": "Five and four populated event records cannot be linked to the separate functional cohorts without animal identifiers.",
        },
        "cellular_selectivity_headers": headers,
        "missing_cellular_selectivity_header_checks": {
            k: k not in set(headers.values()) for k in ("PIK3C2A", "PIK3CB")
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
    print(json.dumps({"source_sha256": result["source_sha256"], "sheets": result["workbook_sheet_count"], "daily_groups": len(result["daily_wire_hang_seconds"]), "withdrawal_groups": len(result["withdrawal_wire_hang_seconds"])}))


if __name__ == "__main__":
    main()
