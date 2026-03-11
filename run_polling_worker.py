"""
One-command launcher for the local polling worker MVP.

Config resolution order:
1. automation/polling_worker/config.local.json
2. automation/polling_worker/config.example.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


def resolve_config(repo_root: Path) -> Path:
    local_cfg = repo_root / "automation" / "polling_worker" / "config.local.json"
    example_cfg = repo_root / "automation" / "polling_worker" / "config.example.json"
    return local_cfg if local_cfg.exists() else example_cfg


def read_interval_and_mode(config_path: Path) -> tuple[int, bool]:
    with config_path.open("r", encoding="utf-8") as f:
        cfg = json.load(f)
    interval = int(cfg.get("poll_interval_seconds", 30))
    continuous_mode = bool(cfg.get("continuous_mode", False))
    if interval <= 0:
        raise ValueError("poll_interval_seconds must be > 0")
    return interval, continuous_mode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local polling worker (one-shot or loop mode).")
    parser.add_argument("--loop", action="store_true", help="Run repeated polling passes until interrupted.")
    parser.add_argument(
        "--interval",
        type=int,
        default=None,
        help="Override polling interval in seconds for --loop mode.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    worker_script = repo_root / "automation" / "polling_worker" / "poll_github_prs.py"
    config_path = resolve_config(repo_root)
    config_interval, config_continuous_mode = read_interval_and_mode(config_path)

    loop_mode = args.loop or config_continuous_mode
    interval = args.interval if args.interval is not None else config_interval
    if interval <= 0:
        raise ValueError("--interval must be > 0")

    cmd = [sys.executable, str(worker_script), "--config", str(config_path.resolve())]

    if not loop_mode:
        proc = subprocess.run(cmd, check=False)
        return proc.returncode

    try:
        while True:
            proc = subprocess.run(cmd, check=False)
            if proc.returncode != 0:
                return proc.returncode
            time.sleep(interval)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
