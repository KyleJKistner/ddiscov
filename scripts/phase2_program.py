#!/usr/bin/env python3
"""Inspect and validate the recorded Phase II research teams; does not launch agents."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path("research/phase2-program/registry.json")
STATES = {"pending", "running", "completed", "blocked"}


def validate(data, root):
    errors = []
    teams = data.get("teams", [])
    runtime = data.get("runtime", {})
    if len(teams) < 10:
        errors.append("At least ten coordinator teams are required.")
    ids, tasks, dossiers = set(), set(), set()
    waves = {}
    for team in teams:
        label = str(team.get("id", "missing"))
        if label in ids:
            errors.append(f"Duplicate team ID: {label}")
        ids.add(label)
        task = team.get("coordinator_task")
        if not task or task in tasks:
            errors.append(f"Missing or duplicate coordinator task: {label}")
        tasks.add(task)
        state = team.get("state")
        if state not in STATES:
            errors.append(f"Invalid team state: {label}")
        workers = team.get("workers", [])
        if len(workers) != 2 or {w.get("role") for w in workers} != {"evidence", "challenge"}:
            errors.append(f"Team {label} needs distinct evidence and challenge workers.")
        for worker in workers:
            worker_task = worker.get("task")
            if worker.get("state") not in STATES:
                errors.append(f"Invalid worker state: {label}")
            if worker_task and worker_task in tasks:
                errors.append(f"Duplicate worker task: {worker_task}")
            if worker_task:
                tasks.add(worker_task)
            if worker.get("state") == "completed" and not worker_task:
                errors.append(f"Completed worker has no actual task identity: {label}")
        dossier = team.get("dossier", "")
        path = (root / dossier).resolve()
        valid_path = bool(dossier) and path.is_relative_to(root.resolve())
        if not valid_path or dossier in dossiers:
            errors.append(f"Missing, unsafe or duplicate dossier path: {label}")
        dossiers.add(dossier)
        if state == "completed":
            if not valid_path or not path.is_file() or not path.read_text(encoding="utf-8").strip():
                errors.append(f"Completed team lacks a nonempty dossier: {label}")
            if len(workers) != 2 or any(w.get("state") != "completed" for w in workers):
                errors.append(f"Completed team has incomplete workers: {label}")
            if not team.get("next_action"):
                errors.append(f"Completed team lacks a next action: {label}")
        wave = team.get("wave")
        if not isinstance(wave, int) or isinstance(wave, bool) or wave < 1:
            errors.append(f"Invalid wave: {label}")
        else:
            waves[wave] = waves.get(wave, 0) + 1 + len(workers)
    capacity = runtime.get("max_active_agents", 0)
    root_slots = runtime.get("root_slots", 1)
    for wave, count in waves.items():
        if root_slots + count > capacity:
            errors.append(f"Wave {wave} exceeds active-agent capacity.")
    if data.get("status") == "first_pass_completed" and any(t.get("state") != "completed" for t in teams):
        errors.append("Program claims completion with incomplete teams.")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    sub.add_parser("status")
    packet = sub.add_parser("packet")
    packet.add_argument("team_id", help="Two-digit coordinator ID, e.g. 03")
    args = parser.parse_args()
    try:
        data = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
        errors = validate(data, ROOT)
        if args.command == "check":
            print(json.dumps({"passed": not errors, "teams": len(data["teams"]), "errors": errors}, indent=2))
            return bool(errors)
        if errors:
            raise ValueError("; ".join(errors))
        if args.command == "status":
            print(f"{data['status']}; recorded session work, no background service")
            for team in data["teams"]:
                print(f"{team['id']} | wave {team['wave']} | {team['state']} | {team['name']}")
        else:
            team = next((t for t in data["teams"] if t["id"] == args.team_id), None)
            if team is None:
                raise ValueError(f"Unknown team: {args.team_id}")
            print(json.dumps({"assignment": team, "read_first": ["AGENTS.md", "decisions/current-shortlist.md", "decisions/selection-policy.md", "research/phase2-program/TEAM-BRIEF.md", "research/phase2-program/phase2-evidence-standard.md"], "execution": "Resume manually in an agent-capable session; this command prints instructions only."}, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
