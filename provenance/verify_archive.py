"""Verify the edition's source anchors against a copy of the original research archive."""

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="directory containing the original project-state.json")
    archive = parser.parse_args().archive.resolve()
    manifest = json.loads(Path(__file__).with_name("archive-anchors.json").read_text())
    anchors = list(manifest["registry_and_reference"])
    for phase in manifest["phases"]:
        anchors.extend(phase["anchors"])

    differences = []
    for anchor in anchors:
        name = anchor["archive_path"]
        path = (archive / name).resolve()
        if archive not in path.parents or not path.is_file():
            differences.append(f"Missing archive file: {name}")
        elif sha256(path) != anchor["sha256"]:
            differences.append(f"Different archive version: {name}")

    if differences:
        print("\n".join(differences))
        raise SystemExit(1)
    print(f"Verified {len(anchors)} source fingerprints across {len(manifest['phases'])} phases.")


if __name__ == "__main__":
    main()
