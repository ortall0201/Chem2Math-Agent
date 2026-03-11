# Code Mapping Guidance

## Purpose
Map electrochemical equations into robust, testable code while preserving domain assumptions.

## 1) Variable-to-Parameter Mapping
- Map every symbol to a named parameter with units in docstrings.
- Prefer explicit parameters over hidden constants for state-dependent terms.
- Example mapping for Nernst:
  - `E^0 -> E0` (volts)
  - `n -> n` (electron count, positive)
  - `Q -> Q` (dimensionless reaction quotient)
  - `T -> T` (kelvin)
  - constants: `R`, `F`

## 2) Required Input Validation
- `n > 0`
- `Q > 0` for logarithm validity
- `T > 0`
- type checks for numeric inputs
- clear errors for invalid domain values

This failure-mode mapping should become code rules:
- sign and convention checks
- log-base consistency
- temperature-awareness checks

## 3) Temperature Handling
- Keep `T` explicit in function signatures unless fixed by design.
- If a 298.15 K shortcut is provided, expose it as a separate convenience path with explicit labeling.

## 4) Assumptions Must Be Documented in Code
- State whether `Q` is activity-based or concentration-approximated.
- State valid regime (thermodynamic equilibrium relation for Nernst).
- State sign convention and reaction-direction assumptions.

## 5) Activities vs Concentrations in API Design
- Preferred: accept `Q` directly so caller owns thermodynamic construction.
- Optional v2: helper API to compute `Q` from composition should include:
  - explicit mode (`activity` or `concentration_approx`)
  - stoichiometric exponent handling
  - warning/metadata when approximation is used

## 6) Use of Math Functions
- Use natural logarithm implementation (`ln`) directly in core formula.
- If exposing base-10 form, convert explicitly with `2.303`.
- Do not mix log bases implicitly.

## 7) Basic Tests Required
- `Q = 1` returns `E = E0`
- changing `T` changes potential shift magnitude as expected
- invalid `Q <= 0` raises validation error
- `ln` form and converted `log10` form match numerically within tolerance
- wrong-sign regression tests (protect against accidental sign flips)

## 8) Separation of Logic vs Commentary
- Keep computational function pure and minimal.
- Place scientific context in docs or skill files, not inside core compute code path.

## Specific Interface Example
`nernst_potential(E0, n, Q, T)`

### Embedded Assumptions
- Thermodynamic equilibrium potential relation is appropriate.
- `Q` is already correctly formed and dimensionless.
- Constants `R` and `F` are standard.
- No kinetic or transport correction is included.

### Suggested Behavior
- Return value: potential `E` in volts.
- Raise clear errors for invalid domains (`Q <= 0`, `n <= 0`, `T <= 0`).

## Handoff
- This mapping defines the initial function contract for `src/nernst.py`.
- Codex should implement validation-first equation functions before adding higher-level wrappers.

## Additional v1 Interface Contracts

### 1) Butler-Volmer Current (Kinetic)
`butler_volmer_current(j0, eta, n, T, alpha_a, alpha_c, F=96485.33212, R=8.314462618)`

#### Return
- Net current density `j` in `A/m^2`.

#### Required Validation
- `j0 > 0`
- `T > 0`
- `n > 0`
- `0 < alpha_a <= 1`
- `0 < alpha_c <= 1`
- numeric type checks on all scalar inputs

#### Assumptions Embedded
- Charge-transfer kinetics represented by Butler-Volmer are valid in the modeled regime.
- `j0`, `alpha_a`, `alpha_c` are treated as known parameters for local conditions.
- `eta` sign convention is documented and consistent with caller usage.
- No transport correction is included in this function.

#### Failure-Mode Hooks
- Protect against hidden sign-convention flips (`eta` and current direction).
- Document that poor fit at high `|eta|` may indicate transport limitation, not only bad kinetic parameters.

### 2) 1D Diffusion-Limited Current Density Helper (Transport)
`diffusion_limited_current_density(n, D, c_bulk, delta, F=96485.33212)`

Suggested relation:
`j_lim = n * F * D * c_bulk / delta`

#### Return
- Magnitude of limiting current density `j_lim` in `A/m^2` under a 1D diffusion-layer approximation.

#### Required Validation
- `n > 0`
- `D > 0`
- `c_bulk >= 0`
- `delta > 0`
- numeric type checks

#### Assumptions Embedded
- Planar 1D transport approximation.
- Steady-state diffusion layer of thickness `delta`.
- Surface concentration approximates depletion limit for this estimate.
- Migration and convection are not explicitly modeled.

#### Failure-Mode Hooks
- Warn if caller treats this as universally valid outside diffusion-limited regime.
- Require explicit units in API docs (`D` in `m^2/s`, `c_bulk` in `mol/m^3`, `delta` in `m`).

## Minimal Implementation Sequence (v1)
1. Implement `nernst_potential(...)` with strict domain checks.
2. Implement `butler_volmer_current(...)` with explicit sign-convention documentation.
3. Implement `diffusion_limited_current_density(...)` as a transport sanity-bound helper.
4. Add tests that connect these via regime selection logic, not by silently mixing equations.
