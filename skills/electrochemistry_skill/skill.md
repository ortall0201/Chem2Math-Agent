# electrochemistry_skill

## Purpose
Provide a domain skill for translating electrochemical concepts into formal mathematical structure that can be implemented in code with explicit assumptions, variable definitions, and validation rules.

This skill is designed for shared use by:
- a reasoning model (formal derivation and conceptual checks)
- Codex (implementation and validation in `src/`)

## Domain Scope
This version covers foundational electrochemistry needed for Chem2Math formalization:
- thermodynamic relations for electrochemical cells
- equilibrium potential modeling (Nernst)
- kinetic current-overpotential modeling baseline (Butler-Volmer, Tafel limit context)
- transport anchor relation (Fick's first law)
- explicit distinction between thermodynamic, kinetic, and transport regimes

## Problem Types Handled
- derive electrochemical equations from base thermodynamic relations
- classify whether a question is thermodynamic, kinetic, transport, or mixed
- map equations into code-ready function signatures and validations
- identify assumptions and failure modes before implementation

## Equation Coverage (v1)
- `Delta G = -n F E`
- `Delta G = Delta G^0 + R T ln(Q)`
- Nernst equation
- Butler-Volmer equation (standard form, interpretive scope)
- Tafel behavior as a limiting form
- Fick's first law as transport anchor

## Out of Scope (v1)
- full porous-electrode models
- concentrated-solution transport theory beyond basic activity discussion
- impedance and equivalent-circuit formalism
- full corrosion mixed-potential modeling workflows
- parameter estimation pipelines

## Role in Chem2Math System
This is the first domain skill in a modular architecture where each chemistry domain contributes:
- formal symbols and assumptions
- canonical derivations
- implementation mappings
- testable failure checks

Future skills should align to the same structure so all domains can be merged into a unified Chemistry-to-Mathematics framework.
