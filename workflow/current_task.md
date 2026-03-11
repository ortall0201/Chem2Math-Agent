# Current Task

## Repo state

- What is already real:
  - `electrochemistry_skill` is now better aligned after PR #1.
  - The repo has:
    - structured skill files
    - executable electrochemistry code in `src/`
    - PR workflow docs in `workflow/`
    - a PR template in `.github/`
    - GitHub-side pickup signaling:
      - `.github/workflows/codex_trigger.yml`
      - `workflow/github_trigger_protocol.md`
- What is partial:
  - GitHub can now mark a PR as ready for Codex pickup.
  - There is still no local worker that consumes that signal.
- What is missing or unstable:
  - There is no polling-worker protocol.
  - There is no local scaffold directory.
  - There is no safe example config.
  - There is no execution loop between GitHub signal and local Codex invocation.

## Next approved unit of work

Add the minimal local polling-worker protocol and scaffold that will later consume the GitHub pickup signal created by `codex_trigger.yml`.

## Why this task now

- Why this is the highest-value next move:
  - It adds the missing local consumer side after the GitHub trigger scaffold.
- Why this should happen before other candidate tasks:
  - It builds directly on the GitHub pickup signal already on `main`.
  - It keeps the system local-first and avoids `n8n`, webhooks, and external bridges.

## Codex handoff

### Files to inspect

- `workflow/pr_protocol.md`
- `.github/workflows/codex_trigger.yml`
- `workflow/github_trigger_protocol.md`
- `.github/pull_request_template.md`

### Files to modify or create

- `workflow/polling_worker_protocol.md`
- `automation/polling_worker/README.md`
- `automation/polling_worker/config.example.json`

### Exact changes to make

- Create `workflow/polling_worker_protocol.md`.
- The protocol file should define:
  - trigger source:
    - open PRs with label `codex-implement`
    - and/or the GitHub pickup comment signal created by `.github/workflows/codex_trigger.yml`
  - next review label: `gpt54-review`
  - where the worker reads task instructions from:
    - PR body
    - `workflow/current_task.md`
  - how the worker claims a PR to avoid duplicate processing
  - what the worker should emit after processing:
    - PR comment
    - label update
    - optional local log
  - failure behavior
  - retry behavior
  - stale-signal handling using `head_sha`
- Create `automation/polling_worker/README.md`.
- The README should describe the intended local worker loop:
  - poll GitHub
  - detect `codex-implement`
  - read the GitHub-side pickup signal comment
  - read the bounded task from PR body or `workflow/current_task.md`
  - invoke local executor later
  - post result
  - relabel for review
- The README must clearly state:
  - this is a scaffold only
  - this does not yet execute Codex
  - this does not yet implement GitHub API polling code
- Create `automation/polling_worker/config.example.json`.
- The config example should include safe placeholder fields such as:
  - `github_repo`
  - `poll_interval_seconds`
  - `trigger_label`
  - `review_label`
  - `task_contract_path`
  - `pickup_signal_marker`
  - `log_path`
- The config example must not include:
  - real tokens
  - usernames
  - machine-specific paths
  - personal values

### Constraints to preserve

- preserve scientific meaning
- do not broaden scope
- do not silently change assumptions
- no secrets
- no `n8n`
- no actual polling implementation yet
- no actual Codex execution yet
- no new GitHub Actions
- no webhook logic
- no changes to `src/`
- keep it minimal and local-first

### Success criteria

- the repo contains a polling-worker protocol that matches the current GitHub trigger comment format
- the repo contains a safe local scaffold directory for future implementation
- the config example is credential-free
- no credentials or external dependencies are introduced

### What not to change

- do not change unrelated files
- do not implement actual worker code yet
- do not add webhook logic
- do not add external API integration
- do not modify electrochemistry logic
- do not add new GitHub Actions
- do not perform broad workflow redesign

## Human approval check

This task is approved and ready to be mirrored into a PR or executed by Codex.

