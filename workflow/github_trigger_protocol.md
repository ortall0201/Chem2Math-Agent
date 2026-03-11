# GitHub Trigger Protocol

## Purpose

Define the minimal GitHub-side trigger contract for marking PRs as ready for Codex pickup.

This protocol is signal-only. It does not execute Codex.

## Labels

- Trigger label: `codex-implement`
- Review label: `gpt54-review`

## Trigger Action Behavior

When a pull request has label `codex-implement`, the GitHub Action:

1. checks whether `workflow/current_task.md` exists in the PR head
2. posts a machine-readable PR comment signal
3. updates the existing signal comment instead of creating duplicates

## Machine-Readable PR Signal

The Action comment contains a stable marker and metadata:

- `codex-task-ready: true`
- `pr_number`
- `head_sha`
- `branch`
- `task_contract_path: workflow/current_task.md`
- note: pickup signal only, not execution

## Future Polling Worker Contract

A future local polling worker should read PR comments and consume the signal with:

- marker: `codex-task-ready: true`
- latest `head_sha`
- contract path `workflow/current_task.md`

The worker should ignore older stale signals if a newer signal exists for the same PR.

## Duplicate Signal Handling

- Duplicate trigger comments should not accumulate.
- The Action should update the existing signal comment identified by marker metadata.

## Out of Scope (Current Version)

This trigger does not provide:

- execution
- Codex invocation
- polling worker implementation
- external bridge integration
