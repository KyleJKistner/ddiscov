"""Extract published KCNC1 n-of-1 model intervals; does not refit patient data.

Input: lawful full-text JATS XML from Europe PMC.
This reports whether each published 95% credible interval contains zero.
It must not be interpreted as independent patient replication or a multiplicity
adjustment. No posterior probability is reconstructed from rounded intervals.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


def text(element):
    return " ".join("".join(element.itertext()).split())


def interval(cell):
    value = text(cell).replace("−", "-")
    numbers = re.findall(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)", value)
    if len(numbers) != 3:
        raise ValueError(f"Unexpected estimate/interval: {value}")
    estimate, low, high = map(float, numbers)
    if not low <= estimate <= high:
        raise ValueError(f"Estimate outside interval: {value}")
    return {"estimate": estimate, "lower_95_CrI": low, "upper_95_CrI": high,
            "contains_zero": low <= 0 <= high, "published_text": value}


parser = argparse.ArgumentParser()
parser.add_argument("xml", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
raw = args.xml.read_bytes()
root = ET.fromstring(raw)
table = root.find(".//table-wrap[@id='epi70253-tbl-0003']")
if table is None:
    raise ValueError("Expected published Table3 not present")
rows = []
for row in table.findall(".//tbody/tr"):
    cells = row.findall("td")
    if len(cells) == 4:
        rows.append({"outcome": text(cells[0]), "time": interval(cells[1]),
                     "intervention": interval(cells[2]), "time_by_intervention": interval(cells[3])})
if len(rows) != 7 or rows[0]["outcome"] != "EMQ total":
    raise ValueError(f"Unexpected outcome table shape: {len(rows)} rows")
result = {
    "source_doi": "10.1002/epi.70253", "source_pmcid": "PMC13360919",
    "source_xml_sha256": hashlib.sha256(raw).hexdigest(),
    "patient_n": 1, "variant": "KCNC1 c.1300G>C p.V434L",
    "analysis": "extraction of published model summary, no patient-data refit",
    "rows": rows,
    "intervention_intervals_containing_zero": sum(r["intervention"]["contains_zero"] for r in rows),
    "model_outcome_rows": len(rows),
    "multiplicity_adjusted": False,
    "posterior_probability_inferred": False,
    "primary_total_effect_divided_by_time_slope_weeks_descriptive_only": rows[0]["intervention"]["estimate"] / rows[0]["time"]["estimate"],
    "warning": "The descriptive level/slope ratio is not an acceleration estimate, validated MCID, independent patient count or precise delay recovered."
}
args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(f"Extracted {len(rows)} model outcomes from one participant; {result['intervention_intervals_containing_zero']} intervention intervals contain zero.")
