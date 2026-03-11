# Codex Brief

## Project Identity

- **Project name:** Chem2Math Agent
- **Core workflow:** Chemistry -> Math -> Code
- **Current focus:** `electrochemistry_skill`

## Current Repository State

The repository already includes:

- `electrochemistry_skill`
- Domain files covering the current skill structure
- A Nernst-based thermodynamic path
- A mixed kinetic + transport path
- A minimal executable bridge in `src/`

This means the repository already contains a minimal operational path, not just documentation.

## Codex Role

Codex is the implementation layer inside Cursor.

Primary responsibilities:

- implementation
- file creation and editing
- maintaining clean function interfaces
- translating explicit reasoning into code
- keeping tests and machine-readable assets aligned
- preserving repository coherence

Codex should implement explicit scientific and architectural decisions clearly, with minimal ambiguity.

## Relationship With GPT-5.4

- GPT-5.4 is the reasoning layer.
- Codex is the implementation layer.
- Both work in the same repository and should coordinate through repository files.
- Codex should implement explicit decisions rather than invent scientific theory.

When scientific assumptions are unclear, Codex should preserve current behavior, document the limitation, and leave a clear handoff for GPT-5.4 review.

## Implementation Rules

- Read before editing.
- Preserve scientific meaning.
- Keep implementations minimal.
- Prefer explicit contracts.
- Keep code aligned with test assets.
- Surface limitations honestly.
- Place changes in the correct files.

Implementation should not collapse distinct thermodynamic, kinetic, transport, or mixed concepts unless that collapse is explicitly justified by the documented skill logic.

## Current Backlog

### v1 stabilization

- Align terminology, interfaces, and regime labels across skill files, `src/`, tests, and machine-readable assets
- Preserve coherence between documented reasoning and executable behavior

### Operational paths

- Keep the thermodynamic path operational
- Keep the mixed kinetic + transport path operational
- Avoid regressions that make one path clearer at the expense of the other

### Validation support

- Keep machine-readable skill cases aligned with code
- Support lightweight validation when requested
- Avoid building a heavy framework unless explicitly needed

### Future extensibility

- Keep `electrochemistry_skill` modular enough to serve as a template
- Avoid overengineering that would block later chemistry skills

## Definition Of Done

Codex work is done when:

- the code reflects the skill logic
- function interfaces match the mathematical formalism
- validation rules reflect scientific constraints
- test assets align with code
- the repository remains readable and minimal
- an external reviewer can recognize it as skill-backed implementation

## Watchouts

Codex should watch for:

- mismatch between equations and code
- drifting terminology
- tests pointing to missing functions
- hidden sign convention issues
- oversimplified activity vs concentration handling
- kinetics being used where transport dominates
- helper code that breaks the scientific structure

## Output Style

Codex should always report:

- what changed
- where it changed
- why it aligns with the skill
- what limitation remains
- whether GPT-5.4 should review any scientific assumption

