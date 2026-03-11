# Usage Examples

## Example 1: Derive Nernst from Thermodynamic Relations
Chemistry idea -> Mathematical formalism -> Code implication

- Chemistry idea: Potential changes with composition away from standard state.
- Mathematical formalism:
  - Start from `Delta G = -nFE`
  - Use `Delta G = Delta G^0 + RT ln(Q)`
  - Substitute `Delta G^0 = -nFE^0`
  - Rearrange to `E = E^0 - (RT/(nF)) ln(Q)`
- Code implication:
  - Implement `nernst_potential(E0, n, Q, T)`
  - Validate `Q > 0`, `n > 0`, `T > 0`
  - Keep natural log as primary form

## Example 2: Classify Thermodynamic vs Kinetic Question
Chemistry idea -> Mathematical formalism -> Code implication

- Chemistry idea: "Given composition, what is equilibrium potential?" vs "Given applied overpotential, what current flows?"
- Mathematical formalism:
  - Equilibrium potential question -> Nernst (thermodynamic)
  - Current response question -> Butler-Volmer (kinetic), possibly transport coupling
- Code implication:
  - Separate APIs:
    - `nernst_potential(...)` for equilibrium potential
    - `butler_volmer_current(...)` for kinetics
  - Do not return current from Nernst-only function

## Example 3: Turn Mathematical Result into Function Contract
Chemistry idea -> Mathematical formalism -> Code implication

- Chemistry idea: Need a reusable equation implementation for broader pipeline integration.
- Mathematical formalism:
  - Explicit symbol list with units and assumptions
  - Final canonical equation form and validity domain
- Code implication:
  - Function signature includes all state-dependent variables
  - Input validation mirrors mathematical domain
  - Docstring includes assumption block (activity handling, sign convention, regime limits)

## Operational Handoff Pattern
- Reasoning model should produce derivation + assumptions using `reasoning_protocol.md`.
- Codex should implement equation function and validation according to `code_mapping.md`.
- Tests should be selected from `tests.md` before integration into larger workflows.
