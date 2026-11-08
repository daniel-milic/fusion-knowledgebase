"""
get_scenario.py

Read-only. Retrieves one scenario and the task definitions its tasks use, so a
scenario can be checked or edited without querying the database by hand.

Usage:
    python get_scenario.py <sid> [--out-dir DIR]

    <sid>  the scenario's _id as hex text

Environment:
    CONNECTION_STRING  MongoDB / Cosmos DB connection string (required)
    DATABASE_NAME      database name (optional, default: qaas)

Writes to --out-dir (default: current folder):
    <sid>.json   the scenarios collection document
    tdids.json   {tdid: task_def document} for every tdid used by the scenario's tasks

Warnings go to stderr for tasks without a tdid and for tdids that are not in task_def.
"""

import argparse
import os
import sys
from pathlib import Path

from bson import ObjectId, json_util
from pymongo import MongoClient

DEFAULT_DATABASE = "qaas"


def get_scenario(db, sid: str) -> dict | None:
    """Return the scenario document for a hex sid, or None if it is not found."""
    return db["scenarios"].find_one({"_id": ObjectId(sid)})


def get_task_defs(db, scenario: dict) -> tuple[dict, list[str]]:
    """Return ({tdid: task_def document}, [tdids not found]) for a scenario's tasks."""
    tdids: list[str] = []
    for task in scenario.get("tasks", []):
        tdid = task.get("tdid")
        if not tdid:
            print(f"WARNING: task {task.get('tid')} has no tdid", file=sys.stderr)
        elif tdid not in tdids:
            tdids.append(tdid)

    valid = [t for t in tdids if ObjectId.is_valid(t)]
    for tdid in tdids:
        if tdid not in valid:
            print(f"WARNING: tdid {tdid} is not a valid id", file=sys.stderr)

    found = {
        str(doc["_id"]): doc
        for doc in db["task_def"].find({"_id": {"$in": [ObjectId(t) for t in valid]}})
    }
    # Keep the scenario's task order
    ordered = {t: found[t] for t in valid if t in found}
    missing = [t for t in tdids if t not in ordered]
    return ordered, missing


def write_json(path: Path, data) -> None:
    path.write_text(json_util.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Retrieve a scenario and its task definitions.")
    parser.add_argument("sid", help="scenario _id as hex text")
    parser.add_argument("--out-dir", default=".", help="folder for the output files (default: current folder)")
    args = parser.parse_args()

    connection = os.environ.get("CONNECTION_STRING")
    if not connection:
        print("ERROR: set the CONNECTION_STRING environment variable", file=sys.stderr)
        return 1
    if not ObjectId.is_valid(args.sid):
        print(f"ERROR: {args.sid} is not a valid sid", file=sys.stderr)
        return 1

    client = MongoClient(connection)
    try:
        db = client[os.environ.get("DATABASE_NAME", DEFAULT_DATABASE)]

        scenario = get_scenario(db, args.sid)
        if scenario is None:
            print(f"ERROR: no scenario with sid {args.sid}", file=sys.stderr)
            return 1

        task_defs, missing = get_task_defs(db, scenario)
    finally:
        client.close()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    scenario_file = out_dir / f"{args.sid}.json"
    tdids_file = out_dir / "tdids.json"
    write_json(scenario_file, scenario)
    write_json(tdids_file, task_defs)

    print(f"Scenario {scenario.get('reference', '')}: {len(scenario.get('tasks', []))} tasks -> {scenario_file}")
    print(f"Task definitions: {len(task_defs)} found -> {tdids_file}")
    for tdid in missing:
        print(f"WARNING: tdid {tdid} not found in task_def", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
