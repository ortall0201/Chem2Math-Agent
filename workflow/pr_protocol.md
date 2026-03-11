# PR Collaboration Protocol

## Purpose

This file defines the minimal GitHub pull request workflow for collaboration between GPT-5.4 and Codex in `Chem2Math Agent`.

The goal is to make the shared workflow durable, reviewable, and repository-centered.

Core philosophy:

Chemistry -> Math -> Code

## Roles

### GPT-5.4

GPT-5.4 is the reasoning, planning, validation, and review layer.

GPT-5.4 should:

- inspect current repo state
- identify the next bounded task
- define scientific and architectural constraints
- write the implementation contract
- review the resulting PR for alignment and maturity

### Codex

Codex is the bounded implementation layer.

Codex should:

- implement the approved bounded task
- preserve scientific meaning
- keep changes minimal and explicit
- report what changed and what remains unresolved

## Why Use PRs

Pull requests provide:

- a durable task boundary
- a review surface for reasoning and implementation alignment
- visible change history
- a clear planner -> implementer -> reviewer loop

PRs are the coordination layer. The repository remains the shared memory.

## Standard Workflow

### 1. Define the task

GPT-5.4 defines one bounded task using the task template in `workflow/task_template.md`.

This task should state:

- repo state
- the next approved unit of work
- why it matters now
- exact implementation scope
- validation or success criteria

### 2. Open or mirror the task in GitHub

The bounded task should appear in one of these forms:

- GitHub issue
- PR description
- repository task file copied from the template

The important requirement is that the contract is explicit and stable.

### 3. Codex implements

Codex reads the approved task contract and performs only that task.

Codex should not:

- broaden scope
- silently change assumptions
- treat the PR as permission for unrelated cleanup

### 4. Codex opens or updates the PR

The PR should clearly state:

- what changed
- which files changed
- what limitation remains
- what GPT-5.4 should review

Use `.github/pull_request_template.md` as the default structure.

### 5. GPT-5.4 reviews

GPT-5.4 reviews the PR for:

- scientific correctness
- chemistry / math / code separation
- consistency with existing skill files
- agreement with the bounded task
- visible limitations

### 6. Decide the next bounded task

After review:

- merge if the task is complete and aligned
- request revision if there is mismatch
- define the next bounded task only after the current one is resolved

## Task Sizing Rules

Each PR should aim for one focused unit of work.

Prefer:

- one alignment fix
- one validation step
- one small implementation contract

Avoid:

- bundling multiple backlog items
- mixing stabilization with expansion
- changing docs, code, and validation architecture all at once unless necessary

## Current Priority Order

For `electrochemistry_skill` v1, prefer:

1. alignment
2. stabilization
3. minimal executable validation
4. careful strengthening
5. future expansion

## Review Gates

Before merging a PR, check:

### Internal consistency gate

- labels match across files
- interfaces match docs and code
- no obvious naming drift

### Scientific rigor gate

- assumptions remain explicit
- equations preserve meaning
- sign/log conventions remain correct

### Repository truth gate

- PR does not overclaim completion
- limitations remain visible
- scope boundaries stay honest

## Current Repo Truth

This repository can currently claim:

- a real `electrochemistry_skill`
- a thermodynamic Nernst path
- a minimal mixed kinetic + transport path
- reusable skill logic and code mapping

This repository cannot yet claim:

- full end-to-end stabilization
- fully operational machine-readable validation
- a full mechanistic mixed electrochemistry solver

