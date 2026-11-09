#!/usr/bin/env python3
"""Reproduce Round 28's conditional cream/territory cash-flow scenarios.

No probabilities, transaction valuations or treatment recommendations are inferred.
See the input conventions and commercial evidence for scope and limitations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "research/rounds/round28/commercial-inputs.json"


def calculate(inputs, route, case_name, fill_multiplier=1.0, years=5, erosion=0.0):
    a = dict(inputs["case_assumptions"][case_name])
    a.update(route.get("scenario_development_overrides", {}).get(case_name, {}))
    region = "us" if route["id"].startswith("us_") else "small"
    structure = route["structure"]
    ramp = list(a["ramp_" + region])
    launch = next((i + 1 for i, rate in enumerate(ramp) if rate > 0), None)
    if years > len(ramp):
        if launch is None:
            return None  # No invented launch date for an unlaunched branch.
        ramp += ([0.60] if ramp[-1] == 0.25 else [1.0])
        ramp += [1.0] * (years - len(ramp))
    overrides = route.get("scenario_cost_overrides", {}).get(case_name, {})
    initial = inputs["initial_package_cost_usd"]
    cases = route["modeled_catchment"] * a["incidence"]
    eligible = cases * a["eligible"]
    filled = eligible * a["filled"] * fill_multiplier
    captured = filled * a["capture_" + region]
    courses = captured * a["courses"]
    packs = courses * a["packs"]
    steady_sales = packs * a["net_" + region]
    flows = []
    start_year = int(inputs["as_of"][:4])
    for index, factor in enumerate(ramp[:years]):
        year = index + 1
        price_factor = (1 - erosion) ** max(0, year - 5)
        sales = steady_sales * factor * price_factor
        admin = 0 if year == 1 else overrides.get("annual_admin_after_year1", a["admin"])
        supply = variable = fixed = development = fee = 0.0
        if structure == "royalty":
            receipts = sales * a["downstream_royalty"]
            upstream = sales * a["upstream_royalty"]
            setup = inputs["royalty_vehicle_launch_setup_usd"][region] if year == launch else 0
        else:
            receipts = sales
            supply = sales * a["supply_" + region]
            variable = sales * a["variable_" + region]
            upstream = sales * a["license_us"] if region == "us" else 0
            if launch is not None and year >= launch:
                fixed = overrides.get("annual_operator_fixed_from_launch", a["fixed_" + region])
            setup = overrides.get("launch_setup", a["launch_" + region]) if year == launch else 0
            if region == "us" and index < len(a["us_development"]):
                development = a["us_development"][index]
                fee = a["us_application_fee_by_year"][index]
        operating = receipts - upstream - supply - variable - fixed - admin - setup - development - fee
        tax_reserve = max(0.0, operating) * inputs["positive_cash_tax_withholding_reserve_fraction"]
        after_reserve = operating - tax_reserve
        initial_cash = initial if year == 1 else 0
        flows.append({
            "year": year, "period_end": f"{start_year + year}{inputs['as_of'][4:]}",
            "launch_ramp": factor, "price_factor": price_factor,
            "product_packs": packs * factor,
            "commercializer_net_product_sales_usd": sales,
            "gross_vehicle_receipts_usd": receipts,
            "upstream_pass_through_or_license_usd": upstream,
            "product_supply_cost_usd": supply,
            "variable_commercial_cost_usd": variable,
            "direct_fixed_commercial_cost_usd": fixed,
            "vehicle_admin_usd": admin,
            "one_off_launch_setup_usd": setup,
            "additional_us_development_usd": development,
            "us_application_fee_usd": fee,
            "tax_withholding_planning_reserve_usd": tax_reserve,
            "initial_package_usd": initial_cash,
            "new_investor_contribution_usd": initial_cash + max(0.0, -after_reserve),
            "investor_distribution_usd": max(0.0, after_reserve),
        })
    contributed = sum(f["new_investor_contribution_usd"] for f in flows)
    distributed = sum(f["investor_distribution_usd"] for f in flows)
    later_calls = contributed - initial
    rate = inputs["illustrative_annual_discount_rate"]
    present_future_cash = sum(
        (f["investor_distribution_usd"] - f["new_investor_contribution_usd"] + f["initial_package_usd"])
        / (1 + rate) ** f["year"] for f in flows
    )
    nominal_ceiling = distributed - later_calls
    return {
        "route_id": route["id"], "case": case_name, "horizon_years": years,
        "filled_purchase_multiplier": fill_multiplier, "post_year5_price_erosion": erosion,
        "investor_vehicle_ownership": route["investor_vehicle_ownership"],
        "annual_diagnosed_cases": cases, "annual_eligible_cases": eligible,
        "annual_filled_cases": filled, "annual_captured_patients": captured,
        "annual_captured_courses": courses, "steady_state_packs": packs,
        "steady_state_net_product_sales_usd": steady_sales, "launch_year": launch,
        "cashflows": flows,
        "total_contributions_usd": contributed, "total_distributions_usd": distributed,
        "net_cash_usd": distributed - contributed,
        "cash_multiple": distributed / contributed if contributed else None,
        "future_contributions_after_initial_usd": later_calls,
        "maximum_initial_package_for_nominal_recoup_usd": nominal_ceiling,
        "maximum_entry_fee_after_illustrative_non_entry_work_usd": nominal_ceiling - inputs["illustrative_non_entry_initial_work_usd"],
        "entry_cost_sensitivities": [
            {"non_entry_initial_work_usd": work,
             "maximum_entry_fee_nominal_usd": nominal_ceiling - work,
             "maximum_entry_fee_at_discount_rate_usd": present_future_cash - work}
            for work in inputs["non_entry_initial_work_sensitivity_usd"]
        ],
        "illustrative_annual_discount_rate": rate,
        "maximum_initial_package_at_discount_rate_usd": present_future_cash,
        "net_present_value_usd": present_future_cash - initial,
        "recoups_all_modeled_contributions": distributed >= contributed,
    }


def run(path):
    raw = path.read_bytes()
    inputs = json.loads(raw)
    main, stress, longer = [], [], []
    for route in inputs["routes"]:
        for case in inputs["case_assumptions"]:
            main.append(calculate(inputs, route, case, years=inputs["primary_horizon_years"]))
            stress.append(calculate(inputs, route, case, fill_multiplier=0.5, years=inputs["primary_horizon_years"]))
            for erosion in inputs["post_year5_annual_price_erosion_cases"]:
                result = calculate(inputs, route, case, years=inputs["long_horizon_years"], erosion=erosion)
                if result is not None:
                    longer.append(result)
    without_waiver = json.loads(json.dumps(inputs))
    direct_us = next(r for r in inputs["routes"] if r["id"] == "us_direct")
    without_waiver["case_assumptions"]["upside"]["us_application_fee_by_year"][3] = direct_us["development_scope"]["application_fee_current_rate_proxy_usd"]
    return {
        "as_of": inputs["as_of"], "currency": inputs["currency"],
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "interpretation": "Conditional analyst cash scenarios, not valuations, offers, forecasts or recovery probabilities. Negative ceilings mean the branch cannot support a nonnegative initial package under these assumptions.",
        "main_scenarios": main, "half_fill_scenarios": stress,
        "ten_year_continuation_scenarios": longer,
        "us_direct_favorable_without_fee_waiver": calculate(without_waiver, direct_us, "upside"),
        "long_horizon_limit": "Only branches launched by year 5 are extended; no new launch date is assumed for the US downside. Rights duration and the ability to continue are assumed, not established.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = json.dumps(run(args.input), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
