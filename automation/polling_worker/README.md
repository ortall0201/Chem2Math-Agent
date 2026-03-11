# Local Polling Worker (MVP)

This directory contains the first local polling worker MVP.

It is a signal consumer only. It does not execute Codex.

## MVP Loop (single run)

1. Poll GitHub PRs via `gh`.
2. Filter PRs with label `codex-implement`.
3. Inspect PR comments.
4. Detect marker `codex-task-ready: true`.
5. Extract:
   - PR number
   - head SHA
   - branch
   - task contract path
6. Write a local task artifact.

## Output

For each detected PR signal, the worker writes:

- `automation/polling_worker/out/pr_<number>.json`

Each artifact contains structured metadata for later execution steps.

## What This MVP Does Not Do

- does not execute Codex
- does not post back to GitHub
- does not run as a daemon/service
- does not include an external bridge

## Usage

Primary usage:

```bash
python run_polling_worker.py
```

Config resolution:

1. `automation/polling_worker/config.local.json` (local override)
2. fallback to `automation/polling_worker/config.example.json`

Advanced direct usage:

```bash
python automation/polling_worker/poll_github_prs.py --config automation/polling_worker/config.local.json
```

The worker performs one polling pass and exits.

This still does not execute Codex.
