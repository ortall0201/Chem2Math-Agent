# Current Task

## Repo state

- What is already real:
  - GitHub-side pickup signaling works.
  - The local polling worker MVP now exists.
  - The repo already has:
    - PR workflow docs
    - task PR pattern
    - GitHub trigger protocol
    - GitHub pickup signal comment
    - local polling-worker MVP files
- What is partial:
  - The system can now detect pickup signals and materialize local task artifacts.
  - Running the worker is still more manual than it should be.
- What is missing or unstable:
  - there is no one-command launcher from the repo root
  - there is no default config resolution path for easy local use
  - there is still no actual Codex execution step

## Next approved unit of work

Implement a one-command runner for the local polling worker MVP so it can be launched easily from the repository root.

## Why this task now

- Why this is the highest-value next move:
  - It makes the existing local polling worker easy to run and observe.
- Why this should happen before other candidate tasks:
  - the polling worker now exists, but still requires more friction than necessary to test
  - this improves usability without jumping ahead to Codex execution

## Codex handoff

### Files to inspect

- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`
- `automation/polling_worker/poll_github_prs.py`

### Files to modify or create

- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`
- `automation/polling_worker/poll_github_prs.py`
- `run_polling_worker.py`

### Exact changes to make

- Create `run_polling_worker.py` at repo root.
- The launcher should:
  - use Python standard library only
  - by default look for `automation/polling_worker/config.local.json`
  - if that file does not exist, fall back to `automation/polling_worker/config.example.json`
  - invoke `automation/polling_worker/poll_github_prs.py`
  - exit with the child script's exit code
- Update `automation/polling_worker/poll_github_prs.py` only as needed to work cleanly with the root launcher.
- Keep the current artifact schema unchanged:
  - `pr_number`
  - `branch`
  - `head_sha`
  - `repo`
  - `task_contract_path`
  - `timestamp`
  - `marker_detected`
- Keep `output_dir` config-driven.
- Update `automation/polling_worker/README.md` so the primary usage becomes:
  - `python run_polling_worker.py`
- The README should also document:
  - local config override path: `automation/polling_worker/config.local.json`
  - fallback behavior to `config.example.json`
  - that this still does not execute Codex

### Constraints to preserve

- preserve scientific meaning
- do not broaden scope
- do not silently change assumptions
- no secrets
- no `n8n`
- no actual Codex execution yet
- no non-standard Python dependencies
- no GitHub write-back yet
- no new GitHub Actions
- no changes to `src/`
- keep it minimal and local-first
- keep artifact schema unchanged
- keep `output_dir` config-driven

### Success criteria

- the polling worker can be launched from repo root with one command
- config resolution works with local override then example fallback
- the existing artifact schema is preserved
- the bridge is easier to test without adding execution

### What not to change

- do not change unrelated files
- do not execute Codex yet
- do not post back to GitHub yet
- do not add daemon/service behavior yet
- do not add external services
- do not modify electrochemistry logic
- do not add new GitHub Actions
- do not perform broad workflow redesign

## Human approval check

This task is approved and ready to be mirrored into a PR or executed by Codex.

