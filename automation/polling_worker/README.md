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

1. Copy `config.example.json` to a local config file (for example `config.local.json`).
2. Run:

```bash
python automation/polling_worker/poll_github_prs.py --config automation/polling_worker/config.local.json
```

The script performs one polling pass and exits.
