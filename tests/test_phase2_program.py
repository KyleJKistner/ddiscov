"""Checks that recorded team completion and capacity cannot silently disagree."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("phase2_program", Path(__file__).resolve().parents[1] / "scripts/phase2_program.py")
program = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(program)


class ProgramTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.data = {"status": "in_progress", "runtime": {"max_active_agents": 7, "root_slots": 1}, "teams": []}
        for i in range(10):
            self.data["teams"].append({"id": f"{i+1:02}", "coordinator_task": f"/root/c{i}", "state": "pending", "wave": i // 2 + 1, "dossier": f"team{i}.md", "workers": [{"role": role, "task": None, "state": "pending"} for role in ("evidence", "challenge")]})

    def test_wave_budget_and_minimum_team_count(self):
        self.assertEqual(program.validate(self.data, self.root), [])
        self.data["teams"][2]["wave"] = 1
        self.assertTrue(any("capacity" in e for e in program.validate(self.data, self.root)))
        self.data["teams"].pop()
        self.assertTrue(any("ten" in e for e in program.validate(self.data, self.root)))

    def test_completion_requires_workers_dossier_and_next_action(self):
        team = self.data["teams"][0]
        team["state"] = "completed"
        self.assertEqual(len(program.validate(self.data, self.root)), 3)
        (self.root / team["dossier"]).write_text("Reviewed evidence", encoding="utf-8")
        team["next_action"] = "Resolve the product bridge"
        for worker in team["workers"]:
            worker.update(state="completed", task=team["coordinator_task"] + "/" + worker["role"])
        self.assertEqual(program.validate(self.data, self.root), [])
        self.data["status"] = "first_pass_completed"
        self.assertTrue(any("incomplete teams" in e for e in program.validate(self.data, self.root)))

    def test_reused_agents_and_external_dossiers_are_rejected(self):
        data = copy.deepcopy(self.data)
        data["teams"][0]["workers"][0]["task"] = data["teams"][1]["coordinator_task"]
        data["teams"][0]["dossier"] = "../outside.md"
        errors = program.validate(data, self.root)
        self.assertTrue(any("duplicate coordinator" in e for e in errors))
        self.assertTrue(any("unsafe" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
