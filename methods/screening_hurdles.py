#!/usr/bin/env python3
"""Reproduce nominal cash hurdles and an illustrative paid-branch cash grid."""

import argparse
import hashlib
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "research/rounds/round27/candidate-ledger.json"
LABELS = ("low", "base", "high")
DEFAULT_GRID = (500000, 1000000, 3000000, 10000000)
DECOMPOSITION_TOLERANCE = Decimal("0.000001")


def number(value, label, probability=False):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise ValueError(f"{label}: expected a number")
    result = Decimal(str(value))
    if not result.is_finite() or result < 0:
        raise ValueError(f"{label}: must be finite and nonnegative")
    if probability and not 0 < result <= 1:
        raise ValueError(f"{label}: probability must satisfy 0 < p <= 1")
    return result


def scenario_range(candidate, key, probability=False):
    value = candidate.get(key)
    if not isinstance(value, dict) or any(k not in value for k in LABELS):
        raise ValueError(f"{candidate['id']}.{key}: low/base/high are required")
    result = {k: number(value[k], f"{candidate['id']}.{key}.{k}", probability)
              for k in LABELS}
    if not result["low"] <= result["base"] <= result["high"]:
        raise ValueError(f"{candidate['id']}.{key}: ranges must be ordered")
    return result


def dollars(value):
    return int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def fraction(value):
    return float(value.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


def numeric_range(value):
    return {k: int(v) if v == v.to_integral_value() else float(v)
            for k, v in value.items()}


def cash_amount(value):
    try:
        return Decimal(value)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError("cash amounts must be numbers") from error


def calculate(ledger, cash_grid=DEFAULT_GRID):
    candidates = ledger.get("candidates") if isinstance(ledger, dict) else None
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("candidates must be a nonempty list")
    grid = [number(v, "cash_grid") for v in cash_grid]
    if not grid or len(set(grid)) != len(grid):
        raise ValueError("cash_grid must contain distinct nonnegative amounts")
    rows, seen = [], set()
    with localcontext() as context:
        context.prec = 50
        for candidate in candidates:
            cid = candidate.get("id") if isinstance(candidate, dict) else None
            if not isinstance(cid, str) or not cid.strip() or cid in seen:
                raise ValueError(f"candidate ID must be nonblank and unique: {cid!r}")
            seen.add(cid)
            sources, details = candidate.get("source_ids"), candidate.get("details_file")
            if (not isinstance(sources, list) or not sources
                    or any(not isinstance(s, str) or not s.strip() for s in sources)
                    or len(set(sources)) != len(sources)
                    or not isinstance(details, str) or not details.strip()):
                raise ValueError(f"{cid}: source_ids and details_file must identify sources")
            cost = scenario_range(candidate, "all_in_cost_usd")
            p = scenario_range(candidate, "p_useful_milestone", probability=True)
            q = scenario_range(candidate, "q_investor_cash_given_milestone", probability=True)
            decomposition = ("q_company_cash_given_milestone", "p_distribution_given_company_cash")
            present = [key in candidate for key in decomposition]
            extra = {}
            if any(present):
                if not all(present):
                    raise ValueError(f"{cid}: both cash decomposition ranges are required")
                company, distribution = [scenario_range(candidate, key, True) for key in decomposition]
                for label in LABELS:
                    if abs(q[label] - company[label] * distribution[label]) > DECOMPOSITION_TOLERANCE:
                        raise ValueError(f"{cid}.{label}: investor q must equal company q times distribution p")
                extra = dict(zip(decomposition, map(numeric_range, (company, distribution))))
            joint = p["base"] * q["base"]
            rows.append({
                "id": cid,
                "all_in_cost_usd": numeric_range(cost),
                "p_useful_milestone": numeric_range(p),
                "q_investor_cash_given_milestone": numeric_range(q),
                **extra,
                "required_net_cash_on_paying_branch_usd": {
                    "cautious": dollars(cost["high"] / (p["low"] * q["low"])),
                    "base": dollars(cost["base"] / joint),
                    "favorable": dollars(cost["low"] / (p["high"] * q["high"])),
                },
                "base_joint_cash_event": fraction(joint),
                "base_hurdle_increase_for_extra_100000_cost_usd": dollars(Decimal(100000) / joint),
                "illustrative_paid_branch_cash_grid": [{
                    "net_investor_cash_on_paying_branch_usd": dollars(value),
                    "base_expected_net_usd": dollars(joint * value - cost["base"]),
                    "base_expected_net_per_invested_dollar": (
                        fraction((joint * value - cost["base"]) / cost["base"])
                        if cost["base"] else None),
                } for value in grid],
                "source_ids": sources,
                "details_file": details,
            })
    return {
        "schema_version": "1.0",
        "horizon_years": 5,
        "formula": "required paying-branch net investor cash = C / (p * q_investor)",
        "grid_formula": "expected net = p * q_investor * V - C; per invested dollar = expected net / C",
        "assumptions": [
            "Five years is an analyst comparison assumption, not a supplied investor deadline.",
            "Input ranges are subjective scenarios, not statistical confidence intervals; corner cases are not forecasts.",
            "q is conditional on a useful milestone and modeled access, and requires actual net investor cash by the horizon.",
            "p*q is a joint useful-result and cash-event scenario, not the probability of recovering principal or earning a return.",
            "C is the full all-in bounded commitment; zero receipts on other branches and no additional mandatory or voluntary investor outlays beyond C are assumed.",
            "Any later investor obligations, including no-deal costs, require explicit branch modeling; early stops may reduce expected spending but receive no credit here.",
            "Paying-branch cash is net of investor share, dilution, royalties, senior claims, costs, taxes and retained development funds; company financing and valuation are not investor cash.",
            "No time discounting, interim receipts or downside recovery is modeled; preserving unspent cash is not investment success.",
            "The identical cash grid is deliberately illustrative stress testing, not estimated sale prices, asset values, offers or likely receipts.",
            "Amounts are rounded to whole USD and ratios to four decimal places; arithmetic precision is not evidence precision. A zero base cost gives an undefined per-dollar ratio.",
            "Source-reference schema is checked; source contents and commercial/legal validity are not verified by this calculator.",
        ],
        "candidate_count": len(rows),
        "candidates": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, help="write JSON to this file instead of stdout")
    parser.add_argument("--cash-grid", nargs="+", type=cash_amount, default=DEFAULT_GRID,
                        metavar="USD", help="illustrative net investor cash amounts on the paying branch")
    args = parser.parse_args()
    try:
        raw = args.input.read_bytes()
        result = calculate(json.loads(raw, parse_float=Decimal), args.cash_grid)
        try:
            result["input_file"] = str(args.input.resolve().relative_to(ROOT))
        except ValueError:
            result["input_file"] = args.input.name
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        rendered = json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, ValueError, InvalidOperation, OverflowError) as error:
        parser.exit(2, f"screening_hurdles: {error}\n")


if __name__ == "__main__":
    main()
