#!/usr/bin/env python3
"""Audit primary topical-ruxolitinib PK tables and an official Orange Book snapshot.

Usage: python methods/rux_hhd_source_audit.py --source-dir /path/to/downloads --output audit.json
Inputs are specified in the round-7 product dossier. Python standard library plus
Poppler pdftotext are required. No new efficacy or safety hypothesis test is fit.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET
import zipfile


SOURCES = {
    "rux_phase23_pk.xml": {
        "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8200345/fullTextXML",
        "sha256": "a050647edaed5d226dd4022e65f06663b96f48654c264a66adf648f4de28b455",
        "table": "Tab1",
    },
    "rux_maxuse2022.xml": {
        "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9142470/fullTextXML",
        "sha256": "9f7710171c60326a86fdf63b5b88dcba53e6193dd1725214f47a003cbad94aa2",
        "table": "Tab3",
    },
    "rux_maxuse2022_supp.pdf": {
        "url": "https://static-content.springer.com/esm/art%3A10.1007%2Fs40257-022-00690-3/MediaObjects/40257_2022_690_MOESM1_ESM.pdf",
        "sha256": "b282921cef2d136cff06415d572e50b0515aa39f89b09d55e2b16364347e6b75",
        "table": "Supplementary Table S1, PDF page 2",
    },
    "orangebook_2026.zip": {
        "url": "https://www.fda.gov/media/76860/download?attachment=",
        "sha256": "c2088c7a36db1930a152b63db23e7a995c471bf4b18c960b1d28190580984e4d",
        "table": "products.txt, patent.txt and exclusivity.txt; NDA 215309 and 209606 only",
    },
}


def clean(element):
    return " ".join("".join(element.itertext()).split())


def table(path, identifier):
    root = ET.parse(path).getroot()
    t = root.find(f".//table-wrap[@id='{identifier}']")
    if t is None:
        raise ValueError(f"Missing table {identifier} in {path}")
    return {
        "label": clean(t.find("label")),
        "caption": clean(t.find("caption")),
        "rows": [[clean(c) for c in tr] for tr in t.findall(".//tr")],
        "footnotes": [clean(x) for x in t.findall("table-wrap-foot")],
        "interpretation": "Published aggregate rows; age/BSA strata overlap, repeated timepoints are not new participants.",
    }


def supplement(path):
    text = subprocess.run(["pdftotext", "-layout", str(path), "-"], check=True,
                          capture_output=True, text=True).stdout.replace("−", "-")
    pattern = re.compile(r"^\s*(\d+)/(M|F)\s+([\d.]+)\s+(\d+)\s+(\d+)\s+(-?\d+)\s+(\d+)\s+(-?\d+)\s*$", re.M)
    rows = []
    for m in pattern.finditer(text):
        age, sex, bsa, css, plt, dplt, hb, dhb = m.groups()
        r = dict(age_years=int(age), sex=sex, treated_BSA_percent=float(bsa), Css_nM=int(css),
                 platelet_day28_10e9_per_L=int(plt), platelet_change_10e9_per_L=int(dplt),
                 hemoglobin_day28_g_per_L=int(hb), hemoglobin_change_g_per_L=int(dhb))
        r["derived_platelet_baseline_10e9_per_L"] = int(plt) - int(dplt)
        r["derived_platelet_percent_change"] = round(100 * int(dplt) / (int(plt) - int(dplt)), 4)
        rows.append(r)
    if len(rows) != 5 or [r["Css_nM"] for r in rows] != [111, 122, 269, 711, 1870]:
        raise ValueError("Supplement extraction no longer matches the inspected five-row table")
    return {
        "source_table": "S1, five selected highest-Css participants within the 41-person maximum-use study",
        "rows": rows,
        "counting_rule": "Selected extremes, not an independent five-person study or an incidence estimate.",
        "interpretation": "The two highest Css values exceed the paper's 281 nM whole-blood TPO-pSTAT3 reference. That reference is not a universal safety cutoff or an HHD therapeutic window. The 90%-BSA participant's platelet fall is 56.75%, while the day-28 count remained within the reported normal range.",
    }


def orangebook(path):
    with zipfile.ZipFile(path) as z:
        selected = {}
        for filename in ["products.txt", "patent.txt", "exclusivity.txt"]:
            text = z.read(filename).decode("utf-8-sig")
            rows = list(csv.DictReader(io.StringIO(text), delimiter="~"))
            selected[filename] = [r for r in rows if r.get("Appl_No") in {"215309", "209606"}]
        dates = {i.filename: "-".join(map(str, i.date_time[:3])) for i in z.infolist()}
    counts = {}
    for nda in ["215309", "209606"]:
        pats = [r for r in selected["patent.txt"] if r["Appl_No"] == nda]
        nums = sorted({r["Patent_No"].replace("*PED", "") for r in pats})
        counts[nda] = {"patent_rows": len(pats), "distinct_base_patent_numbers": len(nums), "base_patent_numbers": nums}
    return {
        "retrieved": "2026-11-04", "zip_internal_dates": dates, "selected_rows": selected,
        "counts": counts,
        "interpretation": "Official listing snapshot with October 9 internal file dates. Repeated product/use-code and pediatric-extension rows are not new patents. Listed expiry is neither adjudicated validity, claim clearance, live status in every jurisdiction, nor a guaranteed generic launch date.",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source-dir", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    provenance = {}
    for name, meta in SOURCES.items():
        data = (a.source_dir / name).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest != meta["sha256"]:
            raise ValueError(f"Source checksum changed for {name}; inspect the changed source before using it")
        provenance[name] = {**meta, "bytes": len(data), "sha256_verified": True}
    phase23 = table(a.source_dir / "rux_phase23_pk.xml", "Tab1")
    maximum = table(a.source_dir / "rux_maxuse2022.xml", "Tab3")
    ob = orangebook(a.source_dir / "orangebook_2026.zip")
    result = {
        "as_of": "2026-11-04", "candidate": "R6-NL-01", "purpose": "Source-value and denominator audit, not a new efficacy analysis",
        "sources": provenance, "phase_II_III_PK_table": phase23, "maximum_use_PK_table": maximum,
        "maximum_use_selected_high_exposure_patients": supplement(a.source_dir / "rux_maxuse2022_supp.pdf"),
        "orange_book": ob,
        "key_denominators": {
            "phase_III_1_5_percent_BID_PK_n": 479,
            "phase_III_0_75_percent_BID_PK_n": 472,
            "phase_III_combined_PK_n": 951,
            "maximum_use_treated_n": 41,
            "maximum_use_day1_PK_n": 40,
            "maximum_use_Css_n": 40,
            "maximum_use_day28_PK_n": 38,
            "maximum_use_terminal_half_life_n": 9,
        },
        "claims_not_supported": [
            "A pharmacokinetic subset is the complete randomized efficacy denominator",
            "The adult-subset day-1 Cmax of 449 nM describes all 41 treated participants",
            "The mean Css of 104 nM captures the maximum-use high-exposure tail",
            "The 116-hour mean from nine participants defines HHD washout or a dosing rule",
            "Total plasma concentration divided by a whole-blood cellular assay IC50 establishes clinical safety",
            "AD exposure determines exposure through macerated HHD skin",
            "Thirty-nine Opzelura Orange Book rows represent thirty-nine distinct patents",
        ],
    }
    if ob["counts"]["215309"]["distinct_base_patent_numbers"] != 22:
        raise ValueError("Unexpected ruxolitinib patent count")
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"output": str(a.output), "phase_II_III_table_rows": len(phase23["rows"]),
                      "maximum_use_table_rows": len(maximum["rows"]), "supplement_rows": 5,
                      "orange_book_counts": ob["counts"]}, indent=2))


if __name__ == "__main__":
    main()
