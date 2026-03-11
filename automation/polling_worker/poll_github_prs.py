"""
Local polling worker MVP.

Single-run script:
- reads open PRs via gh CLI
- checks trigger label and pickup marker comment
- writes local JSON artifacts for execution-ready tasks

This script does not execute Codex.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def run_gh_json(args: list[str]) -> Any:
    cmd = ["gh"] + args
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"gh command failed: {' '.join(cmd)}\n{proc.stderr.strip()}")
    stdout = proc.stdout.strip()
    if not stdout:
        return None
    return json.loads(stdout)


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        cfg = json.load(f)

    required = [
        "github_repo",
        "poll_interval_seconds",
        "trigger_label",
        "pickup_signal_marker",
        "task_contract_path",
        "output_dir",
    ]
    missing = [k for k in required if k not in cfg]
    if missing:
        raise ValueError(f"Missing config keys: {', '.join(missing)}")
    return cfg


def parse_signal_comment(body: str) -> dict[str, Any]:
    def pick(key: str) -> str | None:
        m = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", body)
        return m.group(1).strip() if m else None

    return {
        "pr_number": pick("pr_number"),
        "head_sha": pick("head_sha"),
        "branch": pick("branch"),
        "task_contract_path": pick("task_contract_path"),
    }


def write_artifact(output_dir: Path, payload: dict[str, Any]) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"pr_{payload['pr_number']}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Local GitHub PR polling worker MVP (single run).")
    parser.add_argument("--config", required=True, help="Path to JSON config file.")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    repo = cfg["github_repo"]
    trigger_label = cfg["trigger_label"]
    marker = cfg["pickup_signal_marker"]
    default_task_contract = cfg["task_contract_path"]
    output_dir = Path(cfg["output_dir"])
    invoke_executor_after_write = bool(cfg.get("invoke_executor_after_write", False))

    prs = run_gh_json(
        [
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "open",
            "--json",
            "number,headRefName,headRefOid,labels",
            "--limit",
            "100",
        ]
    )
    if not prs:
        return 0

    for pr in prs:
        labels = [lbl.get("name", "") for lbl in pr.get("labels", [])]
        if trigger_label not in labels:
            continue

        number = pr["number"]
        comments = run_gh_json(["api", f"repos/{repo}/issues/{number}/comments"]) or []

        matching = [
            c for c in comments if isinstance(c.get("body"), str) and marker in c.get("body", "")
        ]
        if not matching:
            continue

        latest = matching[-1]
        parsed = parse_signal_comment(latest["body"])

        payload = {
            "pr_number": int(parsed["pr_number"]) if parsed["pr_number"] else int(number),
            "branch": parsed["branch"] or pr["headRefName"],
            "head_sha": parsed["head_sha"] or pr["headRefOid"],
            "repo": repo,
            "task_contract_path": parsed["task_contract_path"] or default_task_contract,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "marker_detected": True,
        }

        path = write_artifact(output_dir, payload)
        print(f"Wrote {path}")

        if invoke_executor_after_write:
            executor_script = Path(__file__).resolve().parent / "execute_task.py"
            cmd = [
                sys.executable,
                str(executor_script),
                "--config",
                str(Path(args.config).resolve()),
                "--artifact",
                str(path.resolve()),
            ]
            proc = subprocess.run(cmd, check=False)
            if proc.returncode != 0:
                return proc.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
