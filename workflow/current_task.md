# Current Task

## Repo state

- What is already real:
  - GitHub-side pickup signaling works.
  - PRs labeled `codex-implement` can now receive a machine-readable pickup comment.
  - The repo already has:
    - PR workflow docs
    - task PR pattern
    - GitHub trigger protocol
    - electrochemistry skill + executable code
- What is partial:
  - The system can now mark PRs as ready for pickup.
  - It still cannot execute Codex automatically.
- What is missing or unstable:
  - there is no local polling worker implementation
  - there is no claim/process/report loop
  - there is no local executor bridge from GitHub signal -> Codex run

## Next approved unit of work

Implement the first real local polling worker MVP that reads GitHub PR pickup signals and writes a local execution-ready task file.

## Why this task now

- Why this is the highest-value next move:
  - It adds the first local consumer after the GitHub trigger scaffold.
- Why this should happen before other candidate tasks:
  - the signal already exists and is testable
  - without a local worker, the trigger stops at a PR comment
  - this is the smallest step that moves from “signal exists” toward “Codex can actually be invoked”

## Codex handoff

### Files to inspect

- `workflow/pr_protocol.md`
- `.github/workflows/codex_trigger.yml`
- `workflow/github_trigger_protocol.md`
- `workflow/current_task.md`

### Files to modify or create

- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`
- `automation/polling_worker/poll_github_prs.py`

### Exact changes to make

- Create `automation/polling_worker/README.md`.
- The README should explain that this is the first local polling worker MVP.
- The README should describe the loop:
  - poll GitHub
  - look for label `codex-implement`
  - inspect PR comments
  - detect marker `codex-task-ready: true`
  - extract:
    - PR number
    - head SHA
    - branch
    - task contract path
  - write a local task artifact
- The README must clearly state:
  - this MVP does not execute Codex yet
  - it only detects and materializes execution-ready tasks locally
- Create `automation/polling_worker/config.example.json`.
- The config example should include safe placeholder fields such as:
  - `github_repo`
  - `poll_interval_seconds`
  - `trigger_label`
  - `pickup_signal_marker`
  - `task_contract_path`
  - `output_dir`
- The config example must not include:
  - real tokens
  - usernames
  - machine-specific paths
  - personal values
- Create `automation/polling_worker/poll_github_prs.py`.
- The script should:
  - use Python standard library only
  - be clearly marked as MVP
  - read config from a JSON file path
  - shell out to `gh` for GitHub data access
  - read open PRs
  - inspect comments
  - detect PRs with:
    - label `codex-implement`
    - comment marker `codex-task-ready: true`
  - write a local JSON artifact to:
    - `automation/polling_worker/out/pr_<number>.json`
- The output artifact should contain:
  - PR number
  - branch
  - head SHA
  - repo
  - task contract path
  - timestamp
  - `marker_detected: true`
- Single-run polling only.
- Do not implement daemon/service behavior yet.

### Constraints to preserve

- preserve scientific meaning
- do not broaden scope
- do not silently change assumptions
- no secrets
- no `n8n`
- no actual Codex execution yet
- no posting back to GitHub yet
- no non-standard Python dependencies
- no new GitHub Actions
- no changes to `src/`
- keep it minimal and local-first
- use `gh` instead of embedded GitHub tokens in repo code

### Success criteria

- a local script can read GitHub PR state through `gh`
- it can detect the PR pickup signal already produced by the GitHub Action
- it can write a structured local task artifact for later execution
- the repo now has the first real bridge from GitHub signal -> local machine state

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

