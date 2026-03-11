# Current Task

## Repo state

- What is already real:
  - GitHub-side pickup signaling works.
  - The local polling worker MVP now exists.
  - The polling worker can now be launched from the repo root with one command.
  - The local executor bridge now exists.
  - The polling loop can now run repeatedly without manual relaunch.
  - The repo already has:
    - PR workflow docs
    - task PR pattern
    - GitHub trigger protocol
    - GitHub pickup signal comment
    - local polling-worker MVP files
- What is partial:
  - The system can now detect pickup signals, materialize local task artifacts, and invoke a configured local executor command in repeated polling mode.
  - It still risks re-processing the same PR/head SHA unless duplicate protection is added.
- What is missing or unstable:
  - there is no processed-state tracking for repeated execution
  - there is no duplicate-safe `(pr_number, head_sha)` handling
  - the worker may re-invoke the executor for the same PR signal on later passes
  - there is still no GitHub write-back after local execution

## Next approved unit of work

Implement duplicate-safe automatic execution in repeated polling mode so the same PR/head SHA is not re-run on every poll.

## Why this task now

- Why this is the highest-value next move:
  - It makes repeated local execution safe enough to use in practice.
- Why this should happen before other candidate tasks:
  - GitHub trigger, repeated polling, and local executor bridge already exist.
  - Without duplicate protection, repeated mode can keep re-invoking Codex for the same PR.
  - This is the smallest bounded step toward practical automatic pickup.

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
- `automation/polling_worker/state.example.json`

### Exact changes to make

- Update `automation/polling_worker/poll_github_prs.py` so repeated mode can avoid re-processing already handled PR/head SHA pairs.
- Add local processed-state handling using a simple JSON state file.
- The deduplication key should be:
  - `pr_number`
  - `head_sha`
- Only invoke the executor automatically when a `(pr_number, head_sha)` pair is new.
- If the same pair has already been processed, skip execution on later polling passes.
- Extend `automation/polling_worker/config.example.json` with safe placeholder fields such as:
  - `state_path`
  - `skip_already_processed`
- Example values should remain safe placeholders or local paths only.
- Create `automation/polling_worker/state.example.json` as a tiny example schema file or documented placeholder state shape.
- Keep state local and transient in practice; do not treat runtime state as PR material.
- Update `automation/polling_worker/README.md` to explain:
  - how processed-state tracking works
  - that duplicate execution is prevented per `(pr_number, head_sha)`
  - that new commits on the same PR should still be eligible because `head_sha` changes
- Keep the current artifact schema unchanged:
  - `pr_number`
  - `branch`
  - `head_sha`
  - `repo`
  - `task_contract_path`
  - `timestamp`
  - `marker_detected`
- Keep `output_dir` config-driven.
- Do not add GitHub write-back yet.
- Do not add daemon/service installation yet.

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
- keep processed state local and out of PR scope by default

### Success criteria

- repeated mode can invoke the executor for new PR/head SHA pairs
- repeated mode does not re-invoke the executor for already processed pairs
- pushing a new commit to the same PR can still trigger execution because `head_sha` changes
- the existing artifact schema is preserved
- config additions remain credential-free
- the repo gains duplicate-safe automatic repeated local pickup without adding full autonomous orchestration

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

