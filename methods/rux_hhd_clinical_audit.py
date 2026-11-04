#!/usr/bin/env python3
"""Reproduce denominator/demographic checks from the audited primary-source ledger.

This checks arithmetic and ledger consistency, not clinical efficacy. No network or
third-party packages are used. Optional input/output paths support relocation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def group_summary(rows: list[dict]) -> dict:
    return {
        "sample_rows": len(rows),
        "mean_age": sum(x["age"] for x in rows) / len(rows),
        "min_age": min(x["age"] for x in rows),
        "max_age": max(x["age"] for x in rows),
        "female_count": sum(x["sex"] == "F" for x in rows),
        "female_percent": 100 * sum(x["sex"] == "F" for x in rows) / len(rows),
    }


def audit(data: dict, input_hash: str) -> dict:
    cases = data["cases"]
    ids = [x["case_id"] for x in cases]
    assert len(ids) == len(set(ids)) == 5
    assert all(x["ruxolitinib_concentration_percent"] == 1.5 for x in cases)
    assert all(not x["individual_genotype_verified"] for x in cases)
    assert data["decision"]["formal_pooled_response_rate"] is None
    assert data["ceccacci_preprint"]["reported_treated_n_in_abstract"] == 9
    assert not data["ceccacci_preprint"]["clinical_participant_table_recovered"]
    assert not data["related_nonexact_case"]["exact_1_5_percent_evidence"]

    trial = data["derm101_control_audit"]
    assert sum(trial["randomized"].values()) == 33
    assert trial["randomized"]["HHD_active"] + trial["randomized"]["HHD_placebo"] == 16
    assert trial["completed"]["HHD_active"] == 9
    assert trial["completed"]["HHD_placebo"] == 6
    assert trial["week_specific_observed_denominators"] is None
    assert trial["missing_data_imputation_rule"] is None
    response_counts = []
    for row in trial["HHD_response_percentages"]:
        out = {
            "visit": row["visit"],
            "threshold_grade_improvement": row["threshold_grade_improvement"],
        }
        for arm in ("active", "placebo"):
            n = trial["reported_efficacy_denominators"][f"HHD_{arm}"]
            matches = [k for k in range(n + 1) if abs(100 * k / n - row[arm]) <= 0.051]
            assert len(matches) == 1, (row, arm, matches)
            out[arm] = {
                "arithmetic_implied_responders": matches[0],
                "reported_population_denominator": n,
                "reported_percent": row[arm],
            }
        response_counts.append(out)

    biopsy = data["gaumond_biopsy_audit"]
    rows = biopsy["rows_from_table_1"]
    summaries = {g: group_summary([x for x in rows if x["group"] == g]) for g in ("HHD", "AD", "normal")}
    summaries["all_groups"] = group_summary(rows)
    assert {g: summaries[g]["sample_rows"] for g in ("HHD", "AD", "normal")} == biopsy["reported_group_n"]
    text = biopsy["text_labels_as_HHD"]
    pooled = summaries["all_groups"]
    assert round(pooled["mean_age"], 1) == text["mean_age"]
    assert pooled["min_age"] == text["min_age"]
    assert pooled["max_age"] == text["max_age"]
    assert round(pooled["female_percent"], 1) == text["female_percent"]
    assert round(summaries["HHD"]["mean_age"], 1) != text["mean_age"]

    return {
        "as_of": data["as_of"],
        "input_sha256": input_hash,
        "status": "arithmetic and internal ledger checks passed",
        "case_ledger": {
            "exact_strength_peer_reviewed_case_reports": len(cases),
            "individual_genotypes_verified": 0,
            "duplicate_conference_case_not_added": "Mendez EADV abstract 3470",
            "nonexact_strength_combination_case_not_added": "Levin 2024, 1% plus naltrexone",
            "nine_patient_preprint_not_pooled": True,
            "population_response_rate_estimable": False,
        },
        "derm101": {
            "randomized_total": sum(trial["randomized"].values()),
            "randomized_HHD": 16,
            "completed_HHD": 15,
            "response_counts": response_counts,
            "interpretation": "Counts are arithmetic reconstructions from rounded published percentages and fixed reported populations, not recovered individual records or proof of observed week-specific denominators.",
            "missing_data_rule_recovered": False,
        },
        "gaumond": {
            "table_1_recomputed": summaries,
            "published_HHD_demographic_text_matches": "Pooled 17-sample set, not seven HHD rows",
            "independent_donor_count_adjudicated": False,
            "sections_or_cells_counted_as_patients": False,
        },
        "clinical_efficacy_reanalysis": "Not performed: no controlled ruxolitinib HHD individual-level dataset was available.",
    }


def main() -> None:
    base = Path(__file__).resolve().parents[1] / "research" / "rounds" / "round7"
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=base / "rux_hhd_clinical.json")
    parser.add_argument("--output", type=Path, default=base / "rux_hhd_clinical_audit.json")
    args = parser.parse_args()
    raw = args.input.read_bytes()
    result = audit(json.loads(raw), hashlib.sha256(raw).hexdigest())
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "output": str(args.output), "reports": 5, "HHD_trial_randomized": 16, "HHD_biopsy_mean_age": result["gaumond"]["table_1_recomputed"]["HHD"]["mean_age"]}))


if __name__ == "__main__":
    main()
