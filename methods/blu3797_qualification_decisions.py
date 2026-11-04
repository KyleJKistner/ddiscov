#!/usr/bin/env python3
"""BLU3797 proposed decision rules and deterministic precision sensitivity.

No biological data are supplied, generated, fitted or inferred by this utility.
`check` classifies an independently analyzed, documented result. `self-check`
uses synthetic decision inputs solely to verify branch logic. `planning` uses
assumed batch-level SD values; it is not a power calculation or experiment.
"""
import argparse
import copy
import json
import math
from pathlib import Path


TRISTATE_FIELDS = (
    "article_qualified", "model_qualified", "exposure_interpretable",
    "analysis_locked", "unacceptable_harm_confirmed",
    "direct_target_engagement_interpretable", "target_mechanism_supported",
    "adequate_target_perturbation", "delayed_functional_modifiability",
    "orthogonal_selective_failure_confirmed", "independent_background_failure",
    "independent_confirmation_data", "independent_background_benefit",
)
PROVENANCE_FIELDS = (
    "evidence_record", "lot_and_formulation", "genotype_and_reference_identity",
    "exposure_timecourse_record", "analysis_lock_record", "exclusions_and_missingness_record",
)
DENOMINATOR_FIELDS = (
    "disease_donors", "reference_donors", "independent_disease_backgrounds",
    "independent_batches", "randomized_tissues", "tissues_with_primary_endpoint",
    "treatment_related_tissue_failures",
)


def finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return float(value)


def classify(record):
    """Return a bounded scientific disposition, preserving unknown as unknown."""
    out = {
        "classification": None,
        "basis": "proposed round-8 operating rules; no automated scientific certification",
        "experiment_generated_by_utility": False,
        "target_rejection": False,
        "bounded_target_downgrade": False,
        "clinical_efficacy_established": False,
        "S_tier_promotion": False,
    }
    if record.get("observations_available") is not True:
        out.update(classification="not_run_planning_only",
                   reason="No observed biological result was supplied.")
        return out
    for key in TRISTATE_FIELDS:
        value = record.get(key)
        if value is not None and type(value) is not bool:
            raise ValueError(f"{key} must be true, false or null")
    stage = record.get("stage")
    if stage not in ("exploratory", "confirmation"):
        raise ValueError("stage must be exploratory or confirmation")
    if record.get("units") != "uN":
        raise ValueError("This specification requires absolute force units uN")
    effect = finite_number(record.get("effect_estimate"), "effect_estimate")
    low = finite_number(record.get("ci95_lower"), "ci95_lower")
    high = finite_number(record.get("ci95_upper"), "ci95_upper")
    minimum = finite_number(record.get("minimum_useful_effect"), "minimum_useful_effect")
    if minimum <= 0 or not low <= effect <= high:
        raise ValueError("Require M>0 and ci95_lower<=estimate<=ci95_upper")
    missing = [key for key in PROVENANCE_FIELDS
               if not isinstance(record.get(key), str) or not record[key].strip()]
    denoms = record.get("denominators")
    if not isinstance(denoms, dict):
        missing.append("denominators")
    else:
        for key in DENOMINATOR_FIELDS:
            value = denoms.get(key)
            if type(value) is not int or value < 0:
                missing.append(f"denominators.{key}")
        if not any(key.startswith("denominators.") for key in missing):
            if any(denoms[key] < 1 for key in ("disease_donors", "reference_donors",
                                              "independent_disease_backgrounds", "tissues_with_primary_endpoint")):
                missing.append("denominators.required_positive_counts")
            if denoms["independent_batches"] < 3:
                missing.append("denominators.at_least_3_batches_for_this_specification")
            if denoms["disease_donors"] < denoms["independent_disease_backgrounds"]:
                missing.append("denominators.independent_backgrounds_exceed_donor_backgrounds")
            if denoms["randomized_tissues"] < denoms["tissues_with_primary_endpoint"]:
                missing.append("denominators.endpoint_count_exceeds_randomized")
            if denoms["randomized_tissues"] < denoms["treatment_related_tissue_failures"]:
                missing.append("denominators.failure_count_exceeds_randomized")
            if ((record.get("independent_background_failure") is True
                 or record.get("independent_background_benefit") is True)
                    and denoms["independent_disease_backgrounds"] < 2):
                missing.append("denominators.second_background_not_documented")
    if missing:
        out.update(classification="incomplete_observation_provenance", unresolved_inputs=missing,
                   reported_harm_flag=record.get("unacceptable_harm_confirmed"),
                   reason="No gate advance or target downgrade without traceable article, model, exposure, analysis and denominators.")
        return out
    out["evidence_record"] = record["evidence_record"]
    out["quantitative_input"] = {"estimate_uN": effect, "ci95_uN": [low, high], "M_uN": minimum}
    contribution = record.get("incremental_product_contribution", "unknown")
    if contribution not in ("unknown", "provisional", "supported", "absent"):
        raise ValueError("Invalid incremental_product_contribution")
    out["asset_disposition"] = (
        "stop_standalone_asset_thesis" if contribution == "absent"
        else "requires_separate_product_and_rights_decision"
    )
    if record.get("unacceptable_harm_confirmed") is True:
        out.update(classification="hold_article_functional_liability",
                   reason="Confirmed unacceptable functional harm requires article/mechanism review.")
        return out
    failures = [k for k in ("article_qualified", "model_qualified", "exposure_interpretable")
                if record.get(k) is not True]
    if failures:
        out.update(classification="redirect_qualification", unresolved_inputs=failures,
                   reason="Unqualified or unknown inputs do not constitute target failure.")
        return out
    if record.get("analysis_locked") is not True:
        out.update(classification="inconclusive_analysis_not_locked",
                   reason="A post-hoc threshold/analysis cannot establish the planned gate.")
        return out
    if record.get("unacceptable_harm_confirmed") is None:
        out.update(classification="hold_safety_interpretation",
                   reason="Unknown observed functional liability is not a clean safety finding.")
        return out
    if high < minimum:
        required = ("direct_target_engagement_interpretable", "adequate_target_perturbation",
                    "delayed_functional_modifiability")
        missing = [k for k in required if record.get(k) is not True]
        if missing:
            out.update(classification="inconclusive_target_negative", unresolved_inputs=missing,
                       reason="The useful-effect bound is low, but exposure/engagement/modifiability cannot support target rejection.")
        elif (record.get("orthogonal_selective_failure_confirmed") is True
              and record.get("independent_background_failure") is True):
            out.update(classification="downgrade_target_under_tested_conditions",
                       bounded_target_downgrade=True,
                       scope="Only documented articles, genotypes/backgrounds, exposure, timing and qualified endpoints; not universal target rejection.",
                       reason="Qualified futility also survives orthogonal selective perturbation and an independent background; scope remains bounded.")
        else:
            out.update(classification="qualified_futility_in_tested_model",
                       reason="Stop the tested article/use conditions; broad target rejection is not supported.")
        return out
    if stage == "exploratory" and effect >= minimum and low > 0:
        out.update(classification="advance_independent_confirmation",
                   reason="Nominal exploratory function signal clears the predeclared useful-effect point target.",
                   mechanism_limit=(None if record.get("target_mechanism_supported") is True
                                    else "Function may advance; target attribution remains unresolved."))
        return out
    if stage == "confirmation" and low > minimum:
        if record.get("independent_confirmation_data") is not True:
            out.update(classification="inconclusive_nonindependent_confirmation",
                       reason="Selection data cannot also constitute independent confirmation.")
        elif record.get("target_mechanism_supported") is not True:
            out.update(classification="confirmed_function_mechanism_unresolved",
                       reason="Useful function is supported; target attribution still requires evidence.")
        else:
            out.update(classification=("advance_confirmed_multiple_backgrounds"
                                       if record.get("independent_background_benefit") is True
                                       else "advance_confirmed_tested_background"),
                       reason="Independent useful function clears M; scope is limited to supported background(s).")
        return out
    out.update(classification="inconclusive_useful_effect",
               reason="The interval does not establish the stage-specific useful-effect gate or qualified futility.")
    return out


def planning():
    """Conditional interval-width sensitivity, never source-derived variance."""
    from scipy.stats import t
    point, target, max_halfwidth = 0.40, 0.25, 0.15
    rows = []
    for sd in (0.10, 0.20, 0.30):
        n = next(n for n in range(3, 201) if t.ppf(.975, n - 1) * sd / math.sqrt(n) <= max_halfwidth)
        halfwidth = float(t.ppf(.975, n - 1) * sd / math.sqrt(n))
        rows.append({"assumed_SD_of_independent_batch_contrasts_in_gap_units": sd,
                     "minimum_batch_contrasts_for_conditional_width": n,
                     "conditional_halfwidth": halfwidth,
                     "hypothetical_interval_at_point_0_40": [point - halfwidth, point + halfwidth]})
    return {
        "classification": "deterministic planning sensitivity; no observed or simulated biological data",
        "published_human_BLU_force_variance_available": False,
        "assumed_normalized_point": point,
        "analyst_selected_useful_target": target,
        "interval": "two-sided 95% Student t interval across independent batch contrasts",
        "formula": "t(.975,n-1) * assumed_SD / sqrt(n)",
        "conditions": ["The table holds the assumed SD fixed; it is not an achieved or expected power calculation.",
                       "Batch contrasts are independent for batch reproducibility; they are not independent donors.",
                       "Gap is treated as a fixed calibration reference only for this sensitivity calculation.",
                       "This table cannot justify a patient sample size, a true effect, a success probability or a budget.",
                       "After blinded qualification, lock actual precision and maximum resources before treatment decoding."],
        "sensitivity": rows,
        "proposed_core_tissues": {"qualification": 3 * 2 * 4,
                                  "exploration": 3 * 2 * 4 * 4,
                                  "additional_destructive_or_comparator_tissues_included": False},
    }


def self_check():
    """Synthetic boundary cases test implementation, not drug performance."""
    base = dict(observations_available=True, stage="exploratory", units="uN",
                effect_estimate=40.0, ci95_lower=10.0, ci95_upper=70.0,
                minimum_useful_effect=25.0, evidence_record="SYNTHETIC_LOGIC_FIXTURE",
                incremental_product_contribution="unknown", article_qualified=True,
                model_qualified=True, exposure_interpretable=True, analysis_locked=True,
                unacceptable_harm_confirmed=False, direct_target_engagement_interpretable=True,
                target_mechanism_supported=True, adequate_target_perturbation=True,
                delayed_functional_modifiability=True, orthogonal_selective_failure_confirmed=False,
                independent_background_failure=False, independent_confirmation_data=False,
                independent_background_benefit=False,
                lot_and_formulation="SYNTHETIC_LOT_REFERENCE",
                genotype_and_reference_identity="SYNTHETIC_MODEL_REFERENCE",
                exposure_timecourse_record="SYNTHETIC_EXPOSURE_REFERENCE",
                analysis_lock_record="SYNTHETIC_LOCK_REFERENCE",
                exclusions_and_missingness_record="SYNTHETIC_MISSINGNESS_REFERENCE",
                denominators=dict(disease_donors=1, reference_donors=1,
                                  independent_disease_backgrounds=1, independent_batches=3,
                                  randomized_tissues=96, tissues_with_primary_endpoint=96,
                                  treatment_related_tissue_failures=0))
    cases = [
        ("blank_is_not_pass", {"observations_available": False}, "not_run_planning_only"),
        ("null_provenance_not_pass", dict(base, lot_and_formulation=None), "incomplete_observation_provenance"),
        ("boolean_evidence_not_pass", dict(base, evidence_record=True), "incomplete_observation_provenance"),
        ("blank_evidence_not_pass", dict(base, evidence_record="  "), "incomplete_observation_provenance"),
        ("null_denominators_not_pass", dict(base, denominators=None), "incomplete_observation_provenance"),
        ("exploratory_positive", base, "advance_independent_confirmation"),
        ("positive_without_80pct_gate", dict(base, adequate_target_perturbation=False), "advance_independent_confirmation"),
        ("positive_unresolved_mechanism", dict(base, target_mechanism_supported=None, direct_target_engagement_interpretable=None), "advance_independent_confirmation"),
        ("unqualified_lot", dict(base, article_qualified=None), "redirect_qualification"),
        ("harm_overrides_positive", dict(base, unacceptable_harm_confirmed=True), "hold_article_functional_liability"),
        ("unknown_harm_not_pass", dict(base, unacceptable_harm_confirmed=None), "hold_safety_interpretation"),
        ("imprecise_positive", dict(base, ci95_lower=-10), "inconclusive_useful_effect"),
        ("qualified_local_null", dict(base, effect_estimate=5, ci95_lower=-10, ci95_upper=20), "qualified_futility_in_tested_model"),
        ("null_missing_delayed_control", dict(base, effect_estimate=5, ci95_lower=-10, ci95_upper=20, delayed_functional_modifiability=None), "inconclusive_target_negative"),
        ("independent_target_failure", dict(base, effect_estimate=5, ci95_lower=-10, ci95_upper=20, orthogonal_selective_failure_confirmed=True, independent_background_failure=True, denominators=dict(base["denominators"], disease_donors=2, independent_disease_backgrounds=2)), "downgrade_target_under_tested_conditions"),
        ("claimed_second_background_missing", dict(base, independent_background_benefit=True), "incomplete_observation_provenance"),
        ("same_donor_genotype_not_second_background", dict(base, independent_background_benefit=True, denominators=dict(base["denominators"], independent_disease_backgrounds=2)), "incomplete_observation_provenance"),
        ("threshold_equality_not_confirmation", dict(base, stage="confirmation", ci95_lower=25, independent_confirmation_data=True), "inconclusive_useful_effect"),
        ("selected_data_not_confirmation", dict(base, stage="confirmation", ci95_lower=30), "inconclusive_nonindependent_confirmation"),
        ("independent_confirmed_one_background", dict(base, stage="confirmation", ci95_lower=30, independent_confirmation_data=True), "advance_confirmed_tested_background"),
    ]
    for name, record, expected in cases:
        actual = classify(copy.deepcopy(record))["classification"]
        if actual != expected:
            raise AssertionError(f"{name}: {actual} != {expected}")
    for bad in (dict(base, ci95_lower=float('nan')), dict(base, units="percent"),
                dict(base, minimum_useful_effect=0), dict(base, model_qualified="yes")):
        try:
            classify(bad)
        except ValueError:
            continue
        raise AssertionError("Malformed input was accepted")
    asset = classify(dict(base, incremental_product_contribution="absent"))
    assert asset["classification"] == "advance_independent_confirmation"
    assert asset["asset_disposition"] == "stop_standalone_asset_thesis"
    bounded = classify(dict(base, effect_estimate=5, ci95_lower=-10, ci95_upper=20,
                            orthogonal_selective_failure_confirmed=True, independent_background_failure=True,
                            denominators=dict(base["denominators"], disease_donors=2, independent_disease_backgrounds=2)))
    assert bounded["target_rejection"] is False and bounded["bounded_target_downgrade"] is True
    return {"classification": "synthetic decision-logic verification only",
            "branch_cases_passed": len(cases), "malformed_inputs_rejected": 4,
            "scientific_vs_asset_separation_passed": True,
            "bounded_downgrade_not_global_rejection_passed": True,
            "biological_results_generated": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "planning", "self-check"))
    parser.add_argument("input", nargs="?", type=Path)
    args = parser.parse_args()
    if args.command == "check":
        if args.input is None:
            parser.error("check requires a decision input JSON file")
        result = classify(json.loads(args.input.read_text()))
    elif args.command == "planning":
        result = planning()
    else:
        result = self_check()
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
