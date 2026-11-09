"""Illustrative trial-design sensitivity, with explicit non-patient-derived inputs."""

import argparse
import csv
import io
import json
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent


def validate(config):
    assert config["replicates_per_base_scenario"] >= 10000
    assert all(n >= 6 and n % 2 == 0 for n in config["randomized_people"])
    assert all(sd > 0 for sd in config["assumed_sd_grid"])
    assert all(0 <= p < 1 for p in config["loss_probability"])
    assert all(0 <= x < 1 for x in config["contrast_attenuation_fraction"])
    assert 0 <= config["within_family_contrast_correlation"] < 1
    assert config["family_size"] == 2
    assert config["two_sided_confidence_level"] == 0.95
    assert config["illustrative_worthwhile_difference_nrs_points"] > 0
    assert config["assumed_true_active_benefit_nrs_points"] == sorted(config["assumed_true_active_benefit_nrs_points"])


def distribution(config, rng, design, n, sd, loss):
    size = config["replicates_per_base_scenario"]
    if design == "parallel_equal_allocation":
        active = rng.binomial(n // 2, 1 - loss, size=size)
        control = rng.binomial(n // 2, 1 - loss, size=size)
        valid = (active >= 3) & (control >= 3)
        df = np.maximum(active + control - 2, 1)
        truth_se = sd * np.sqrt(1 / np.maximum(active, 1) + 1 / np.maximum(control, 1))
        complete_people = active + control
        independent_units = complete_people
    else:
        cluster = design == "paired_two_per_family"
        if design not in ("paired_independent_people", "paired_two_per_family"):
            raise ValueError(design)
        units = n // 2 if cluster else n
        observed = rng.binomial(units, 1 - loss, size=size)
        valid = observed >= 3
        df = np.maximum(observed - 1, 1)
        unit_sd = sd
        if cluster:
            rho = config["within_family_contrast_correlation"]
            unit_sd *= np.sqrt(rho + (1 - rho) / 2)
        truth_se = unit_sd / np.sqrt(np.maximum(observed, 1))
        complete_people = observed * (2 if cluster else 1)
        independent_units = observed
    noise = truth_se * rng.standard_normal(size)
    estimated_se = truth_se * np.sqrt(rng.chisquare(df) / df)
    critical = stats.t.ppf(0.975, df)
    width = critical * estimated_se
    return noise, width, valid, complete_people, independent_units


def generate(config):
    validate(config)
    rng = np.random.default_rng(config["seed"])
    threshold = config["illustrative_worthwhile_difference_nrs_points"]
    output = []
    for design in config["designs"]:
        for n in config["randomized_people"]:
            for sd in config["assumed_sd_grid"]:
                for loss in config["loss_probability"]:
                    noise, width, valid, complete, units = distribution(config, rng, design, n, sd, loss)
                    for attenuation in config["contrast_attenuation_fraction"]:
                        previous_signal = previous_go = -1
                        for true_effect in config["assumed_true_active_benefit_nrs_points"]:
                            observed_effect = true_effect * (1 - attenuation)
                            estimate = observed_effect + noise
                            lower, upper = estimate - width, estimate + width
                            signal = valid & (lower > 0)
                            point_worthwhile = valid & (estimate >= threshold)
                            go = signal & point_worthwhile
                            excludes_threshold = valid & (lower > threshold)
                            futility = valid & (upper < threshold)
                            inconclusive = valid & ~go & ~futility
                            # These checks enforce distinct events and avoid multiplying pseudo-replicates.
                            assert not np.any(go & futility)
                            assert np.all(~excludes_threshold | go)
                            assert signal.mean() + 1e-12 >= previous_signal
                            assert go.mean() + 1e-12 >= previous_go
                            previous_signal, previous_go = signal.mean(), go.mean()
                            total = go.mean() + futility.mean() + inconclusive.mean() + (~valid).mean()
                            assert abs(total - 1) < 1e-12
                            # Positive-direction significance at null is 2.5%, not a 5% positive effect rate.
                            if true_effect == 0:
                                assert signal.mean() <= 0.03
                            if loss == 0 and design == "paired_independent_people":
                                exact = stats.nct.sf(stats.t.ppf(0.975, n - 1), n - 1, observed_effect * np.sqrt(n) / sd)
                                assert abs(signal.mean() - exact) < 0.006
                            output.append({
                                "design": design, "randomized_people": n, "assumed_sd": sd,
                                "true_active_benefit": true_effect, "attenuation_fraction": attenuation,
                                "effective_contrast": observed_effect, "loss_probability": loss,
                                "worthwhile_threshold": threshold,
                                "replicates": config["replicates_per_base_scenario"],
                                "mean_complete_people": complete.mean(), "mean_analysis_units": units.mean(),
                                "positive_signal_frequency": signal.mean(),
                                "point_estimate_at_least_threshold_frequency": point_worthwhile.mean(),
                                "signal_and_point_threshold_frequency": go.mean(),
                                "lower_95ci_above_threshold_frequency": excludes_threshold.mean(),
                                "upper_95ci_below_threshold_frequency": futility.mean(),
                                "inconclusive_frequency": inconclusive.mean(),
                                "no_interpretable_result_frequency": (~valid).mean(),
                                "mean_95ci_halfwidth_valid": width[valid].mean(),
                            })
    return output


def as_csv(rows):
    text = io.StringIO()
    writer = csv.DictWriter(text, fieldnames=rows[0].keys(), lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({k: format(v, ".6f") if isinstance(v, (float, np.floating)) else v for k, v in row.items()})
    return text.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Recompute with validation and compare saved CSV")
    args = parser.parse_args()
    config = json.loads((ROOT / "design-inputs.json").read_text())
    rows = generate(config)
    output = as_csv(rows)
    path = ROOT / "design-results.csv"
    if args.check:
        if not path.exists() or path.read_text() != output:
            raise SystemExit("Design CSV does not match current assumptions/code")
    else:
        path.write_text(output)
    print(f"{'Checked' if args.check else 'Generated'} {len(rows)} conditional design scenarios; no clinical data fitted")


if __name__ == "__main__":
    main()
