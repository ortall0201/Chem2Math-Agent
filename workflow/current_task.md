# Current Task

## Repo state

- What is already real:
  - `electrochemistry_skill` is a structured domain skill with a real Chemistry -> Math -> Code path.
  - The repo has:
    - `src/nernst.py`
    - `src/electrochemistry_orchestrator.py`
    - structured skill files
    - PR workflow docs in `workflow/`
    - a PR template in `.github/`
- What is partial:
  - The repo supports a manual planner -> implementer -> reviewer workflow through repo files and PR structure.
  - There is still no automated PR pickup path for Codex.
- What is missing or unstable:
  - There is no GitHub Actions trigger for `codex-implement`.
  - There is no GitHub-side machine-readable signal for a local worker.
  - There is no polling worker scaffold yet.

## Next approved unit of work

Add the smallest GitHub-side automation scaffold so PRs can be marked as ready for Codex pickup in a machine-readable way.

## Why this task now

- Why this is the highest-value next move:
  - It creates the first real automation layer between GitHub PR state and future local Codex execution.
- Why this should happen before other candidate tasks:
  - The future polling worker needs a stable trigger contract to consume.
  - It keeps the system local-first and avoids external infrastructure.

## Codex handoff

### Files to inspect

- `workflow/pr_protocol.md`
- `workflow/gpt54_operating_mode.md`
- `workflow/codex_operating_mode.md`
- `.github/pull_request_template.md`

### Files to modify or create

- `.github/workflows/codex_trigger.yml`
- `workflow/github_trigger_protocol.md`

### Exact changes to make

- Create `.github/workflows/codex_trigger.yml`.
- The workflow should:
  - trigger on pull request events
  - run only when the PR has label `codex-implement`
  - read `workflow/current_task.md` if present
  - post a structured PR comment that acts as a machine-readable pickup signal
- The PR comment should include:
  - a stable marker such as `codex-task-ready: true`
  - PR number
  - head SHA
  - branch name
  - task contract path: `workflow/current_task.md`
  - a short note that this is a pickup signal only, not execution
- The workflow must not:
  - call external APIs
  - invoke Codex
  - use secrets
  - perform any webhook dispatch
- Create `workflow/github_trigger_protocol.md`.
- The protocol file should define:
  - trigger label: `codex-implement`
  - review label: `gpt54-review`
  - what the Action posts
  - what the future polling worker should read
  - how duplicate trigger comments should be handled
  - what this trigger does not do yet:
    - no execution
    - no Codex invocation
    - no polling worker implementation

### Constraints to preserve

- preserve scientific meaning
- do not broaden scope
- do not silently change assumptions
- no secrets
- no external bridge
- no `n8n`
- no worker implementation yet
- no changes to `src/`
- keep it minimal and local-first

### Success criteria

- the repo contains a GitHub Action that marks labeled PRs as ready for Codex pickup
- the repo contains a protocol file describing how future local polling should interpret that signal
- the Action is clearly signal-only and does not pretend to execute Codex
- no credentials or external dependencies are introduced

### What not to change

- do not change unrelated files
- do not implement the polling worker yet
- do not add webhook logic
- do not add external API integration
- do not modify electrochemistry logic
- do not perform broad workflow redesign

## Human approval check

This task is approved and ready to be mirrored into a PR or executed by Codex.

