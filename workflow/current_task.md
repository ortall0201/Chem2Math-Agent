# Current Task

## Repo state

- What is already real:
  - GitHub-side pickup signaling works.
  - The local polling worker MVP now exists.
  - The polling worker can now be launched from the repo root with one command.
  - The local executor bridge now exists.
  - The repo already has:
    - PR workflow docs
    - task PR pattern
    - GitHub trigger protocol
    - GitHub pickup signal comment
    - local polling-worker MVP files
- What is partial:
  - The system can now detect pickup signals, materialize local task artifacts, and invoke a configured local executor command.
  - The polling flow still requires a manual one-shot launch.
- What is missing or unstable:
  - there is no continuous or repeated polling mode
  - future PRs are not picked up automatically unless the user reruns the command
  - there is still no GitHub write-back after local execution

## Next approved unit of work

Implement a continuous/repeated local polling mode so future PRs can be picked up automatically without manual relaunch.

## Why this task now

- Why this is the highest-value next move:
  - It removes the remaining manual relaunch step in the local pickup loop.
- Why this should happen before other candidate tasks:
  - GitHub trigger, local polling, one-command launch, and local executor bridge already exist.
  - The next missing piece is repeated pickup over time.
  - This still stays local-first and avoids daemon/service overbuild.

## Codex handoff

### Files to inspect

- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`
- `automation/polling_worker/poll_github_prs.py`
- `automation/polling_worker/execute_task.py`
- `run_polling_worker.py`

### Files to modify or create

- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`
- `automation/polling_worker/poll_github_prs.py`
- `run_polling_worker.py`

### Exact changes to make

- Update `run_polling_worker.py` so it can optionally run continuously or repeatedly instead of one-shot only.
- Preferred minimal interface:
  - keep existing one-shot behavior by default
  - add an explicit loop mode such as `--loop`
  - optional `--interval` override is acceptable if it falls back to config
- Update `automation/polling_worker/config.example.json` with a safe placeholder field such as:
  - `continuous_mode`
- `continuous_mode` example value should be `false`
- Update `automation/polling_worker/poll_github_prs.py` only as needed to support repeated invocation cleanly.
- Repeated mode should:
  - sleep between passes using configured interval
  - reuse existing polling + artifact + optional executor behavior
  - stop cleanly on keyboard interrupt
- Do not convert this into a background service or OS-specific daemon.
- Keep the current artifact schema unchanged:
  - `pr_number`
  - `branch`
  - `head_sha`
  - `repo`
  - `task_contract_path`
  - `timestamp`
  - `marker_detected`
- Keep `output_dir` config-driven.
- Update `automation/polling_worker/README.md` to document:
  - one-shot mode
  - repeated/continuous local polling mode
  - optional local execution mode
  - still no GitHub write-back
  - still no daemon/service installation
  - still no external services

### Constraints to preserve

- preserve scientific meaning
- do not broaden scope
- do not silently change assumptions
- no secrets
- no `n8n`
- no non-standard Python dependencies
- no GitHub write-back yet
- no daemon/service installation
- no external services
- no new GitHub Actions
- no changes to `src/`
- keep it minimal and local-first
- keep artifact schema unchanged
- keep `output_dir` config-driven

### Success criteria

- the polling worker can be run once or in repeated mode from the repo root
- repeated mode picks up future PR signals without manually relaunching each time
- the existing artifact schema is preserved
- config additions remain credential-free
- the repo gains automatic repeated local pickup without adding full autonomous orchestration

### What not to change

- do not change unrelated files
- do not post back to GitHub yet
- do not add daemon/service installation
- do not add external services
- do not modify electrochemistry logic
- do not add new GitHub Actions
- do not perform broad workflow redesign

## Human approval check

This task is approved and ready to be mirrored into a PR or executed by Codex.

