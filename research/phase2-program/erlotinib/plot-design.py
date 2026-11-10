#!/usr/bin/env python3
"""Render selected conditional scenarios; never infer a drug-success probability."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

ROOT = Path(__file__).resolve().parent
with (ROOT / "design-results.csv").open(newline="") as source:
    rows = [r for r in csv.DictReader(source)
            if r["design"] == "paired_independent_people"
            and float(r["assumed_sd"]) == 2.5
            and float(r["true_active_benefit"]) == 2
            and float(r["attenuation_fraction"]) == 0
            and float(r["loss_probability"]) == 0]
rows.sort(key=lambda r: int(r["randomized_people"]))
assert [int(r["randomized_people"]) for r in rows] == [8, 12, 20, 30]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.fonttype": "none", "svg.hashsalt": "erlotinib-design-v1"})
fig, ax = plt.subplots(figsize=(10, 6.2))
fig.subplots_adjust(left=.10, right=.96, top=.78, bottom=.29)
series = [
    ("positive_signal_frequency", "Positive signal: lower 95% CI > 0", "#176d9c"),
    ("signal_and_point_threshold_frequency", "Signal + estimate at least 1.5 points", "#b77513"),
    ("lower_95ci_above_threshold_frequency", "Stronger precision: lower 95% CI > 1.5", "#704c91"),
]
x = [int(r["randomized_people"]) for r in rows]
for key, label, color in series:
    ax.plot(x, [float(r[key]) for r in rows], marker="o", lw=2.4,
            markersize=6, label=label, color=color)
ax.set_xticks(x)
ax.set_xlabel("Independent participants completing a paired-foot comparison")
ax.set_ylim(0, 1.05)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.set_ylabel("Frequency of result in the assumed scenario")
ax.grid(axis="y", alpha=.2)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper left", bbox_to_anchor=(0, -.22), frameon=False, fontsize=10)
fig.text(.10, .94, "A signal is easier to detect than a precisely large benefit",
         fontsize=16, weight="bold")
fig.text(.10, .875, "Assumed true benefit: 2 NRS points; paired SD: 2.5; no loss or attenuation.\n"
         "The 1.5-point threshold is illustrative. These are not drug-success probabilities.",
         fontsize=10.5)
fig.savefig(ROOT / "design-sensitivity.svg", metadata={"Date": None})
svg = ROOT / "design-sensitivity.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
fig.savefig("/tmp/erlotinib-design-preview.png", dpi=140)
print("Rendered design-sensitivity.svg from four recorded scenario rows.")
