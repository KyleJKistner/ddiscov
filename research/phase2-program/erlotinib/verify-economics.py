"""Reconcile saved planning arithmetic; does not validate costs or investment value."""

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def verify(data):
    checks = 0

    def equal(label, actual, expected, tolerance=0.005):
        nonlocal checks
        if isinstance(actual, list):
            if not isinstance(expected, list) or len(actual) != len(expected):
                raise ValueError(f"{label}: different dimensions")
            for i, (a, b) in enumerate(zip(actual, expected)):
                equal(f"{label}[{i}]", a, b, tolerance)
            return
        if not math.isclose(actual, expected, rel_tol=1e-12, abs_tol=tolerance):
            raise ValueError(f"{label}: calculated {actual}, saved {expected}")
        checks += 1

    def vector_sum(rows):
        rows = list(rows)
        if any(len(row) != len(data["scenario_order"]) for row in rows):
            raise ValueError("Cost vectors must match scenario_order")
        return [sum(values) for values in zip(*rows)]

    def including_contingency(values):
        return [value * (1 + rate) for value, rate in zip(values, data["contingency_fraction"])]

    base = data["scenario_order"].index("base")
    common = vector_sum(data["common_costs"].values())
    equal("Independent CMC modules", vector_sum(data["independent_cmc_modules"].values()),
          data["product_costs"]["independent_qualification"])
    for route, product in data["product_costs"].items():
        subtotal = [a + b for a, b in zip(common, product)]
        total = including_contingency(subtotal)
        saved = data["totals"][route]
        equal(f"{route} subtotal", subtotal, saved["subtotal"])
        equal(f"{route} contingency", [t - s for t, s in zip(total, subtotal)], saved["contingency"])
        equal(f"{route} total", total, saved["all_in"])
        equal(f"{route} reference difference", data["capital_reference"] - total[base],
              saved["difference_from_500k_reference_after_base"])
        previous = [0] * len(total)
        for name in ("G0", "G1", "G2"):
            gate = data["gates"][name]
            if name == "G2":
                calculated = total
            else:
                allocations = list(gate["common_allocations"].values()) + [gate["product_allocations"][route]]
                calculated = including_contingency(vector_sum(allocations))
            equal(f"{route} {name}", calculated, gate["all_in"][route])
            if any(not (a <= b <= c) for a, b, c in zip(previous, calculated, total)):
                raise ValueError(f"{route} {name}: cumulative gates must increase within total")
            previous = calculated

    site = data["base_site_cost_build"]
    site_total = sum(site[k] for k in ("setup_closeout", "travel", "remote_contacts", "local_logistics"))
    site_total += site["person_visits"] * site["cost_per_visit"]
    equal("Base site costs", site_total, data["common_costs"]["sites_visits_contacts_travel"][base])
    clinical = data["clinical_assumptions"]
    randomized = clinical["randomized_low_base_high"][base]
    retention = 1 - clinical["attrition_assumed"]
    target = clinical["independent_completers_target"]
    equal("Expected completers", randomized * retention, clinical["base_expected_completers"])
    equal("Base visits", randomized * clinical["base_visits_per_patient"], site["person_visits"])
    for n, key in ((randomized, "base_probability_at_least_12"), (19, "nineteen_probability_at_least_12")):
        probability = sum(math.comb(n, k) * retention**k * (1 - retention)**(n - k)
                          for k in range(target, n + 1))
        equal(f"Completion probability n={n}", probability, clinical[key], tolerance=0.0005)

    enrollment = data["enrollment_sensitivity"]
    equal("Incremental patient cost", sum(enrollment["variable_base_cost_allocations"].values()) /
          enrollment["base_randomized"], enrollment["incremental_per_patient_before_contingency"])
    for n, routes in enrollment["totals"].items():
        increment = (int(n) - enrollment["base_randomized"]) * enrollment["incremental_per_patient_before_contingency"]
        increment *= 1 + enrollment["contingency"]
        for route, saved in routes.items():
            equal(f"{route} enrollment {n}", data["totals"][route]["all_in"][base] + increment, saved)
    capacity = data["capital_capacity_sensitivity"]
    for amount in capacity["reference_levels"]:
        for route, cost in enrollment["totals"][str(capacity["pilot_randomized"])].items():
            equal(f"{route} capacity {amount}", amount - cost,
                  capacity["unallocated_after_pilot"][str(amount)][route])

    market = data["market_sensitivity"]
    equal("Revenue grid", [[n * price for price in market["annual_net_price"]]
                           for n in market["served_patients"]], market["annual_revenue_grid"])
    equal("Operating cash example", market["example_revenue"] * market["example_margin"] -
          market["example_fixed_cost"], market["example_operating_cash_before_tax_and_development"])
    recruiting = data["recruitment_sensitivity"]
    calculated_yield = math.prod(recruiting[k] for k in ("eligibility", "site_accessibility", "consent"))
    equal("Recruitment yield", calculated_yield, recruiting["yield"], tolerance=1e-12)
    equal("Reachable population", recruiting["target_randomized"] / calculated_yield, recruiting["reachable_needed"])
    equal("Alternative reachable population", recruiting["target_randomized"] / recruiting["alternative_yield"],
          recruiting["alternative_reachable_needed"])

    cash = data["cash_recovery"]
    equal("Principal recovery", [(cash["C"] + cash["Q"]) / f for f in cash["participation_f"]],
          cash["principal_recovery_P"])
    equal("Illustrative return", [(cash["C"] * (1 + cash["illustrative_return_fraction"]) + cash["Q"]) / f
                                  for f in cash["participation_f"]], cash["return_target_P"])
    equal("Successful-branch break-even cash", [cash["C"] / q for q in cash["assumed_probability_axes"]],
          cash["net_success_cash_principal_break_even"])
    follow_on = data["follow_on_sensitivity"]
    subtotal = vector_sum(follow_on[k] for k in ("expanded_trial", "product_stability_scale",
                                                "additional_nonclinical", "regulatory_data_ip_operations"))
    equal("Follow-on total", [x * (1 + follow_on["contingency_fraction"]) for x in subtotal], follow_on["all_in"])
    return checks


if __name__ == "__main__":
    inputs = json.loads((ROOT / "economics-inputs.json").read_text())
    count = verify(inputs)
    print(f"Checked {count} saved economic calculations; planning assumptions and investment value remain unvalidated")
