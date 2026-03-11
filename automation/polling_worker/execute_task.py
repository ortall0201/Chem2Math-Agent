"""
Local executor bridge MVP.

Consumes one local task artifact JSON and invokes a configured local executor
command, passing the artifact path as an argument.

This script does not post back to GitHub and does not run as a daemon.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


REQUIRED_ARTIFACT_FIELDS = [
    "pr_number",
    "branch",
    "head_sha",
    "repo",
    "task_contract_path",
    "marker_detected",
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")
    return data


def validate_artifact(artifact: dict[str, Any]) -> None:
    missing = [k for k in REQUIRED_ARTIFACT_FIELDS if k not in artifact]
    if missing:
        raise ValueError(f"Artifact missing required fields: {', '.join(missing)}")
    if artifact.get("marker_detected") is not True:
        raise ValueError("Artifact marker_detected must be true")


def build_command(
    executor_command: str,
    artifact_path: Path,
    argument_mode: str,
) -> list[str]:
    if not executor_command.strip():
        raise ValueError("executor_command must be non-empty")

    if argument_mode not in ("append",):
        raise ValueError("artifact_path_argument_mode must be 'append' in MVP")

    cmd = executor_command.split()
    if argument_mode == "append":
        cmd.append(str(artifact_path))
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute one local task artifact with configured command.")
    parser.add_argument("--config", required=True, help="Path to polling worker config JSON.")
    parser.add_argument("--artifact", required=True, help="Path to local task artifact JSON.")
    args = parser.parse_args()

    config = load_json(Path(args.config))
    artifact_path = Path(args.artifact)
    artifact = load_json(artifact_path)
    validate_artifact(artifact)

    executor_command = str(config.get("executor_command", "")).strip()
    argument_mode = str(config.get("artifact_path_argument_mode", "append")).strip()
    command = build_command(executor_command, artifact_path, argument_mode)

    proc = subprocess.run(command, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
