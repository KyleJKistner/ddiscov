"""Behavior checks for bounded repository navigation and consistency validation."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("repo", Path(__file__).resolve().parents[1] / "scripts/repo.py")
repo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repo)


class NavigationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_json(self, name, value):
        return self.write(name, json.dumps(value))

    def test_pointer_preserves_escaped_keys_and_array_indexes(self):
        value = {"a/b": {"~key": [{"": "selected"}]}}
        self.assertEqual(repo.select_pointer(value, "/a~1b/~0key/0/"), "selected")
        self.assertEqual(repo.select_pointer(value, ""), value)
        for pointer in ("a", "/missing", "/a~2b", "/a~1b/~0key/-1", "/a~1b/~0key/00"):
            with self.subTest(pointer=pointer), self.assertRaises(ValueError):
                repo.select_pointer(value, pointer)

    def test_search_prioritizes_latest_evidence_and_bounds_results(self):
        self.write_json(repo.REGISTER, {"name": "BLU historical"})
        self.write_json("research/rounds/round2/record.json", {"name": "BLU old"})
        self.write_json("research/rounds/round26/candidate-ledger.json", {"records": [{"name": "BLU newest"}]})
        result = repo.search(self.root, "blu", limit=1)
        self.assertEqual(result["matches"][0]["excerpt"], "BLU newest")
        self.assertEqual(result["matches"][0]["pointer"], "/records/0/name")
        self.assertTrue(result["more_matches"])
        self.assertEqual(len(result["matches"]), 1)
        self.assertFalse(repo.search(self.root, "unmatched")["more_matches"])

    def test_search_reports_invalid_json_and_can_find_later_files(self):
        self.write("research/rounds/round26/broken.json", "{")
        self.write_json("record.json", {"name": "target"})
        result = repo.search(self.root, "target")
        self.assertEqual(len(result["errors"]), 1)
        self.assertEqual(result["matches"][0]["file"], "record.json")

    def test_show_requires_explicit_large_output_and_rejects_external_paths(self):
        self.write_json("large.json", {"small": "ok", "large": "x" * 1000})
        self.assertEqual(repo.show(self.root, "large.json", "/small", 100), "ok")
        with self.assertRaisesRegex(ValueError, "narrower pointer"):
            repo.show(self.root, "large.json", "", 100)
        self.assertEqual(len(repo.show(self.root, "large.json", "/large", 100, full=True)), 1000)
        with self.assertRaisesRegex(ValueError, "inside this repository"):
            repo.show(self.root, "../outside.json", "")

    def test_check_finds_broken_links_and_csv_width(self):
        for name in repo.REQUIRED:
            self.write(name, "{}" if name.endswith(".json") else "# Entry point\n")
        self.write("README.md", "[good](decisions/current-shortlist.md#section)\n[broken](missing.md)\n[external](https://example.com)\n```\n[example](ignored.md)\n```\n")
        self.write("bad.csv", 'id,name\n1,"two, fields"\n2\n')
        result = repo.check(self.root)
        self.assertFalse(result["passed"])
        self.assertEqual(len(result["errors"]), 2)
        self.write("missing.md", "# Found\n")
        self.write("bad.csv", 'id,name\n1,"two, fields"\n')
        self.assertTrue(repo.check(self.root)["passed"])

    def test_status_uses_numeric_round_order_and_current_document(self):
        self.write("research/rounds/round9/README.md", "")
        self.write("research/rounds/round26/README.md", "")
        self.write("decisions/current-shortlist.md", "# Opportunities\n\n**Evidence cutoff: 8 November 2026.** Current evidence.\n\n**Current capital position: uncommitted.**\n")
        result = repo.status(self.root)
        self.assertEqual(result["latest_evidence_round"], 26)
        self.assertIn("uncommitted", result["current_notes"][1])
        self.assertEqual(result["current_decisions"], "decisions/current-shortlist.md")


if __name__ == "__main__":
    unittest.main()
