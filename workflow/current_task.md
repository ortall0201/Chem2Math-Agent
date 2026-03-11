# Current Task

## Repo state

- What is already real:
  - GitHub-side pickup signaling works.
  - The local polling worker MVP now exists.
  - The polling worker can now be launched from the repo root with one command.
  - The repo already has:
    - PR workflow docs
    - task PR pattern
    - GitHub trigger protocol
    - GitHub pickup signal comment
    - local polling-worker MVP files
- What is partial:
  - The system can now detect pickup signals and materialize local task artifacts.
  - It still does not turn those artifacts into local Codex execution.
- What is missing or unstable:
  - there is no local executor bridge from task artifact -> Codex run
  - there is no claim/process/report loop
  - there is no GitHub write-back after local execution

## Next approved unit of work

Implement the first local executor bridge so the polling-worker flow can consume a generated task artifact and invoke a local executor command for Codex.

## Why this task now

- Why this is the highest-value next move:
  - It is the first step from “detect task” to “start local execution.”
- Why this should happen before other candidate tasks:
  - GitHub-side trigger and local polling now both exist.
  - The next missing piece is actual local execution bridging.
  - This still stays bounded and local-first without jumping to full autonomous orchestration.

## Codex handoff

### Files to inspect

- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`
- `automation/polling_worker/poll_github_prs.py`
- `run_polling_worker.py`

### Files to modify or create

- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`
- `automation/polling_worker/poll_github_prs.py`
- `automation/polling_worker/execute_task.py`

### Exact changes to make

- Create `automation/polling_worker/execute_task.py`.
- The script should:
  - use Python standard library only
  - accept a path to one local task artifact JSON
  - load the artifact
  - validate required fields:
    - `pr_number`
    - `branch`
    - `head_sha`
    - `repo`
    - `task_contract_path`
    - `marker_detected`
  - read an executor command template from config
  - execute that command locally with the artifact path passed as an argument
  - return the child process exit code
- The script must not:
  - post back to GitHub
  - change labels
  - run as a daemon
  - embed credentials
- Extend `automation/polling_worker/config.example.json` with safe placeholder fields for local execution only, for example:
  - `executor_command`
  - `artifact_path_argument_mode`
- Keep all values as placeholders only.
- Update `automation/polling_worker/poll_github_prs.py` only as needed so it can optionally invoke `execute_task.py` after writing an artifact.
- Recommended minimal behavior:
  - add an optional config flag such as `invoke_executor_after_write`
  - example value should be `false`
  - if enabled, call `execute_task.py` for each newly written artifact
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
  - detection-only mode
  - optional local execution mode
  - still no GitHub write-back
  - still no continuous daemon
  - still no external services

### Constraints to preserve

- preserve scientific meaning
- do not broaden scope
- do not silently change assumptions
- no secrets
- no `n8n`
- no non-standard Python dependencies
- no GitHub write-back yet
- no daemon/service yet
- no external services
- no new GitHub Actions
- no changes to `src/`
- keep it minimal and local-first
- keep artifact schema unchanged
- keep `output_dir` config-driven

### Success criteria

- the polling-worker flow can consume a generated artifact and call a local executor command
- the existing artifact schema is preserved
- config additions remain credential-free
- the repo now has the first local execution bridge without adding full autonomous orchestration

### What not to change

- do not change unrelated files
- do not post back to GitHub yet
- do not add daemon/service behavior yet
- do not add external services
- do not modify electrochemistry logic
- do not add new GitHub Actions
- do not perform broad workflow redesign

## Human approval check

This task is approved and ready to be mirrored into a PR or executed by Codex.

