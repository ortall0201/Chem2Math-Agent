# Electrochemistry-to-Math Reasoning Protocol

Use this protocol whenever translating an electrochemical statement into formal mathematics and then into implementable logic.

## 1) Identify the Electrochemical Regime or Concept
- Determine whether the question is about equilibrium potential, reaction direction, current response, or transport constraints.
- Record the target quantity (for example `E`, `j`, `eta`, flux).

## 2) Classify Problem Type
- Classify as one:
  - thermodynamic
  - kinetic
  - transport
  - mixed
- If mixed, split into sub-problems before combining equations.

### Operational Decision Rules (Model Selection)
- `R1 Thermodynamic-only`: Use when target is equilibrium potential, reaction spontaneity, or composition-dependent voltage at zero net current.
  - Typical outputs: `E_eq`, `Delta G`, `Delta G^0`.
  - Use: `Delta G = -nFE`, `Delta G = Delta G^0 + RT ln(Q)`, Nernst.
  - Reject if the task asks for current magnitude under finite overpotential.
- `R2 Kinetic-only`: Use when target is current-overpotential relation and problem states charge-transfer control (or gives kinetic parameters like `j0`, `alpha`).
  - Typical outputs: `j(eta)` or fitted kinetic parameters.
  - Use: Butler-Volmer or Tafel-limit approximation (with validity caveat).
  - Reject if concentration polarization or limiting current is explicitly present.
- `R3 Transport-only`: Use when target is flux, limiting current, diffusion-layer behavior, or concentration profile constraints with no need for interfacial kinetic parameterization.
  - Typical outputs: `J_i`, `j_lim`, concentration-gradient effects.
  - Use: Fick-based transport anchors and stated transport assumptions.
  - Reject if interfacial activation parameters are required for the asked output.
- `R4 Mixed`: Use when observations include both interfacial and transport signatures (for example: activation region at low `|eta|`, limiting plateau at high `|eta|`).
  - Typical workflow: compute/fit kinetic relation in activation region, add transport bound or coupling relation for high-current region.
  - Require explicit interface between submodels and a statement of coupling assumptions.

## 3) Define Variables and Symbols
- List every symbol with:
  - physical meaning
  - units
  - expected domain (for example `Q > 0`, `T > 0`, `n` positive integer in chemistry context)
- Ensure sign conventions are declared (`eta`, reaction direction, anodic/cathodic current sign).

## 4) State Assumptions Explicitly
- Record ideality assumptions (activity vs concentration).
- Record state assumptions (isothermal, isobaric, steady-state, equilibrium or not).
- Record model scope limits (for example BV kinetic regime, diffusion-neglect assumptions).

## 5) Choose Governing Equation(s)
- Select canonical equation(s) from `equations.md`.
- Justify why each selected equation matches the classified regime.
- Reject equations that belong to a different regime unless building a mixed model intentionally.
- For mixed models, state sequence explicitly:
  - example: `E_eq` from Nernst -> `eta = E_applied - E_eq` -> `j` from Butler-Volmer -> compare against/limit by transport relation.

## 6) Derive or Transform Step by Step
- Show each algebraic transition on its own line.
- Explain sign handling and substitutions (especially standard-state substitutions).
- Keep symbolic form until the end; substitute numerical constants last.

## 7) Check Dimensional Consistency
- Verify each term has compatible units.
- Verify arguments to `ln` or `log10` are dimensionless.

## 8) Identify Approximation Level
- Label result as:
  - exact within model
  - approximation (and of what type)
- Examples: activity-to-concentration approximation, Tafel-limit approximation.

## 9) List Common Failure Points
- Before finalizing, compare derivation against `failure_modes.md`.
- Mark any relevant risk items explicitly.

## 10) Express Final Mathematical Result Clearly
- Provide final equation in canonical form.
- Include variable definitions and sign convention reminder adjacent to the result.

## 11) Map Result into Code
- Define function signature and parameter semantics.
- Add input constraints and validation rules.
- Separate equation computation from narrative commentary in implementation.

## 12) Define Validation Needed
- Specify checks:
  - symbolic/algebraic sanity checks
  - numerical spot checks
  - edge-case checks (`Q -> 1`, invalid `Q`, temperature variation)
  - convention checks (sign, log base)

## Shared-Memory Handoff Rules
- Reasoning model should produce derivation artifacts using this protocol.
- Codex should implement only after assumptions and validation checks are explicitly listed.
- Each finalized derivation should define a future function interface in `src/`.
