"""Check the decision safeguards of the provisional screening calculation."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest

REVIEW = Path(__file__).resolve().parents[1] / "research/phase2-program/ranking-review"
SPEC = importlib.util.spec_from_file_location("candidate_ranking", REVIEW / "calculate.py")
ranking = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ranking)


class RankingTests(unittest.TestCase):
    def setUp(self):
        self.model = json.loads((REVIEW / "screening-model.json").read_text())

    def test_ties_and_monotonicity(self):
        first = copy.deepcopy(self.model["candidates"][0])
        second = copy.deepcopy(first)
        second["key"] = "same_evidence"
        weights = self.model["weights_percent"]["balanced"]
        self.assertEqual(set(ranking.ranks([first, second], weights).values()), {1})
        second["scores"]["K"][1] += 1
        result = ranking.ranks([first, second], weights)
        self.assertEqual(result[second["key"]], 1)
        self.assertEqual(result[first["key"]], 2)

    def test_strong_scores_cannot_cancel_a_hold(self):
        row = copy.deepcopy(self.model["candidates"][0])
        row["scores"] = {axis: [4, 4, 4] for axis in "HTKV"}
        for status in ranking.STATUSES - {"compare"}:
            row["status"] = status
            self.assertFalse(ranking.eligible(row))
        row["status"] = "compare"
        row["scores"]["K"] = [0, 1, 4]
        self.assertFalse(ranking.eligible(row))
        row["scores"]["K"][1] = 2
        self.assertTrue(ranking.eligible(row))

    def test_bad_ranges_and_duplicate_assets_rejected(self):
        invalid = copy.deepcopy(self.model)
        invalid["candidates"][0]["scores"]["H"] = [3, 2, 4]
        with self.assertRaises(ValueError):
            ranking.validate(invalid)
        invalid = copy.deepcopy(self.model)
        invalid["candidates"][1]["key"] = invalid["candidates"][0]["key"]
        with self.assertRaises(ValueError):
            ranking.validate(invalid)

    def test_saved_outputs_match_reviewed_inputs(self):
        ranking.validate(self.model)
        for filename, expected in ranking.outputs(self.model).items():
            self.assertEqual((REVIEW / filename).read_text(), expected)


if __name__ == "__main__":
    unittest.main()
