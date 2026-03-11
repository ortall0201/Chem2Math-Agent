"""
One-command launcher for the local polling worker MVP.

Config resolution order:
1. automation/polling_worker/config.local.json
2. automation/polling_worker/config.example.json
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def resolve_config(repo_root: Path) -> Path:
    local_cfg = repo_root / "automation" / "polling_worker" / "config.local.json"
    example_cfg = repo_root / "automation" / "polling_worker" / "config.example.json"
    return local_cfg if local_cfg.exists() else example_cfg


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    worker_script = repo_root / "automation" / "polling_worker" / "poll_github_prs.py"
    config_path = resolve_config(repo_root)

    cmd = [sys.executable, str(worker_script), "--config", str(config_path)]
    proc = subprocess.run(cmd, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
