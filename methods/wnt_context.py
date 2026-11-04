"""Reproduce two construct-held-out WNT comparisons with the Python standard library."""
import csv
import math
from pathlib import Path
from statistics import mean, pstdev

DEPENDENCIES = {"3D": {"FZD1", "FZD2", "FZD7"}, "3C": {"FZD5"}}


def ridge_prediction(training, target_overlap):
    """One standardized predictor, an unpenalized intercept, and unit ridge penalty."""
    overlaps, outcomes = zip(*training)
    center, scale = mean(overlaps), pstdev(overlaps)
    intercept = mean(outcomes)
    if scale == 0:
        return intercept
    z = [(value - center) / scale for value in overlaps]
    slope = sum(a * (b - intercept) for a, b in zip(z, outcomes)) / (sum(a * a for a in z) + 1)
    return intercept + slope * (target_overlap - center) / scale


def evaluate(rows, panel, column):
    samples = {}
    for row in rows:
        profile = row["frizzled_binding_profile"].split()
        if row["panel"] != panel or not profile:  # Controls describe the assay baseline.
            continue
        name = row["source_arm"]
        if name in samples:
            raise ValueError(f"More than one condition per assembly in panel {panel}: {name}")
        overlap = int(bool(DEPENDENCIES[panel].intersection(profile)))
        response = float(row[column])
        samples[name] = (overlap, math.log2(response) if panel == "3D" else response)
    residuals = {"mean": [], "context": []}
    for name, (overlap, observed) in samples.items():
        training = [value for other, value in samples.items() if other != name]
        residuals["mean"].append(mean(outcome for _, outcome in training) - observed)
        residuals["context"].append(ridge_prediction(training, overlap) - observed)
    return {model: math.sqrt(mean(r * r for r in errors)) for model, errors in residuals.items()}


if __name__ == "__main__":
    with Path(__file__).with_name("wnt-panel-means.csv").open(newline="") as handle:
        data = list(csv.DictReader(handle))
    print("Panel  Summary                   Training mean RMSE   Receptor context RMSE")
    for panel, column in (("3D", "arithmetic_mean"), ("3D", "mean_without_source_flag"),
                          ("3C", "arithmetic_mean")):
        result = evaluate(data, panel, column)
        print(f"{panel:6} {column:25} {result['mean']:18.4f} {result['context']:22.4f}")
