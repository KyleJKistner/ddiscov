"""Read the published CiliaTracks workbook and evaluate the donor-held-out speed baseline."""
import argparse
from collections import defaultdict
import hashlib
from math import inf
from pathlib import Path
from statistics import mean, median
from xml.etree import ElementTree
from zipfile import ZipFile

# Pin the publisher workbook, including shared-string and worksheet coordinates.
WORKBOOK_SHA256 = "87cc230efbe8e9658e4a0bc7c7c99c30974e90d5301b07ad8f6b2fa790f6f62c"


def read_recordings(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != WORKBOOK_SHA256:
        raise ValueError("Expected Hadas et al. Supplementary Data workbook (see README).")
    with ZipFile(path) as book:
        strings = ["".join(node.itertext()) for node in ElementTree.fromstring(book.read("xl/sharedStrings.xml"))]
        sheet = ElementTree.fromstring(book.read("xl/worksheets/sheet9.xml"))
    recordings = defaultdict(list)
    donor_labels = {}
    for row in sheet.findall(".//{*}row"):
        cells = {}
        for cell in row.findall("{*}c"):
            value = cell.findtext("{*}v")
            if value is not None:
                col = cell.attrib["r"].rstrip("0123456789")
                cells[col] = strings[int(value)] if cell.get("t") == "s" else value
        if cells.get("M") in {"0", "1"}:
            donor, label = cells["O"], int(cells["M"])
            if donor_labels.setdefault(donor, label) != label:
                raise ValueError("Different condition labels inside one donor.")
            recordings[donor].append(float(cells["H"]))
    return recordings, donor_labels


def fit_cutoff(training):
    levels = sorted({speed for speed, _ in training})
    candidates = [-inf, *((a + b) / 2 for a, b in zip(levels, levels[1:])), inf]

    def balanced_accuracy(cutoff):
        return mean(mean((speed < cutoff) == group for speed, label in training if label == group)
                    for group in (0, 1))

    # Candidates are ordered, so a tie selects the smallest cutoff.
    return max(candidates, key=balanced_accuracy)


def evaluate(path):
    recordings, labels = read_recordings(path)
    speeds = {donor: median(values) for donor, values in recordings.items()}
    calls = defaultdict(list)
    for held_out in speeds:
        training = [(speed, labels[donor]) for donor, speed in speeds.items() if donor != held_out]
        predicted_pcd = speeds[held_out] < fit_cutoff(training)
        calls[labels[held_out]].append(predicted_pcd == labels[held_out])
    print(f"{sum(map(len, recordings.values()))} recordings, {len(speeds)} donors")
    for label, name in ((1, "PCD"), (0, "Control")):
        print(f"{name}: {sum(calls[label])}/{len(calls[label])} classified correctly")
    print(f"Donor-level balanced accuracy: {mean(mean(group) for group in calls.values()):.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path, help="42003_2026_11149_MOESM6_ESM.xlsx")
    evaluate(parser.parse_args().workbook)
