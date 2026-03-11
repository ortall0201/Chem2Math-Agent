# Electrochemistry Skill v1 Status

## Scope of This Report
Repository consistency and execution readiness check as of 2026-03-11.

## What the Skill Can Do Now
- Classify electrochemistry problems into:
  - `thermodynamic-only`
  - `kinetic-only`
  - `transport-only`
  - `mixed`
- Map each regime to equation families and failure-mode checks.
- Provide worked derivations for:
  - Nernst equation
  - Tafel limits from Butler-Volmer
- Provide machine-readable test assets and hybrid validation specs.

## Scenarios Covered
- Thermodynamic equilibrium potential (Nernst/Gibbs relation).
- Kinetic current-overpotential relation (Butler-Volmer, Tafel limit context).
- Transport-limited current estimate (1D diffusion helper).
- Mixed activation + transport behavior (plateau case).

## Implemented in Code (`src/`)
- [nernst.py](/c:/Users/user/Desktop/Chem2Math-Agent/src/nernst.py)
  - `nernst_potential(E0, n, Q, T)`
- [electrochemistry_orchestrator.py](/c:/Users/user/Desktop/Chem2Math-Agent/src/electrochemistry_orchestrator.py)
  - `butler_volmer_current(j0, eta, n, T, alpha_a, alpha_c, ...)`
  - `diffusion_limited_current_density(n, D, c_bulk, delta, ...)`
  - `classify_regime(problem)`
  - `select_math_path(problem)`
  - `orchestrate_problem(problem)`

## Still Specification-Level
- No full parameter-estimation workflow (kinetic fitting, uncertainty handling).
- No mechanistic transport solver (only diffusion-limit helper).
- No automated YAML test runner script yet (design below, not implemented).
- No dataset parser for deriving classification flags from raw experimental files.

## Internal Consistency Audit (Result)
Aligned now:
- Regime labels match across skill files and `src/`.
- Function names match across `code_mapping.md`, `tests.md`, YAML assets, and code.
- `nernst_potential` signature normalized to `E0, n, Q, T` across docs and `src/`.
- Mixed test case in `tests.md` references its YAML source asset.
- README now states the skill/code execution layer explicitly.

Known minor inconsistency:
- Test IDs differ between `tests.md` shorthand (`ECHEM-T1`, `ECHEM-M1`) and YAML asset IDs (`ECHEM-THERMO-NERNST-001`, `ECHEM-MIXED-PLATEAU-001`). This is acceptable if `source_asset` is treated as canonical linkage.

## Known Limitations
- Rule-based selector requires precomputed boolean problem descriptors.
- Mixed current prediction uses a minimal cap logic, not a full coupled model.
- Activity-vs-concentration handling remains caller responsibility (no dedicated helper yet).

## Smallest Automated YAML Runner Design (Proposed)
- File location:
  - `src/skill_case_runner.py`
- Input format:
  - One YAML file per case in `skills/electrochemistry_skill/test_assets/`
  - Required keys: `id`, `expected.classification`, `expected.equation_family`, `code_validation.interfaces`
- Validation flow:
  1. Load YAML case.
  2. Build a minimal `problem` descriptor from case metadata (or predefined map).
  3. Call `classify_regime(problem)` and `select_math_path(problem)`.
  4. Compare returned classification/equation family to expected values.
  5. If executable parameters are available, call the listed interface function(s).
- Pass/fail criteria:
  - `PASS` if classification matches exactly and expected equation family entries are present.
  - `PASS` for code path if function call executes without validation errors for valid input.
  - `FAIL` otherwise, with explicit mismatch reason.
- Current callable functions:
  - `nernst_potential`
  - `butler_volmer_current`
  - `diffusion_limited_current_density`
  - `classify_regime`
  - `select_math_path`

## Version 2 Priorities
1. Implement YAML runner from this design.
2. Add transport+kinetic coupled prediction interface beyond capped heuristic.
3. Add helper for activity-aware `Q` construction with explicit approximation modes.
4. Add structured numeric benchmark fixtures and regression tests.
