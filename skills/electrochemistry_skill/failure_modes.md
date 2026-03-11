# Failure Modes

## 1) Sign Errors in Electrochemical Relations
- Mistake: Using `Delta G = +nFE` or inconsistent sign when rearranging Nernst terms.
- Why wrong: Breaks thermodynamic direction interpretation.
- Detect: Check whether spontaneous direction (`Delta G < 0`) implies positive driving potential under the chosen convention.
- Correct: Lock reaction direction first, then apply one consistent sign convention through all steps.

## 2) Confusing `Delta G` and `Delta G^0`
- Mistake: Swapping standard and non-standard free energies.
- Why wrong: Loses composition dependence and invalidates Nernst derivation.
- Detect: If equation lacks `Q` correction but claims non-standard conditions, this error is likely.
- Correct: Keep `Delta G^0` only for standard reference; use `Delta G = Delta G^0 + RT ln(Q)` for actual conditions.

## 3) Misuse of Reaction Quotient `Q`
- Mistake: Wrong stoichiometric exponents or inverted products/reactants.
- Why wrong: Produces incorrect potential shift magnitude and direction.
- Detect: Rebuild `Q` directly from balanced reaction and compare exponents.
- Correct: Construct `Q` from reaction stoichiometry before any substitution.

## 4) Treating `Q` as Dimensional Without Comment
- Mistake: Using dimensional concentration products directly inside logarithms without normalization discussion.
- Why wrong: Log arguments should be dimensionless in strict thermodynamics.
- Detect: Unit analysis of `Q` gives non-unitless expression.
- Correct: Use activities or clearly state concentration-based approximation and normalization convention.

## 5) Using Concentration Where Activity Should Be Discussed
- Mistake: Presenting concentration-based Nernst expression as universally exact.
- Why wrong: Ignores non-ideality effects.
- Detect: No mention of activity coefficients in non-ideal systems.
- Correct: State approximation explicitly; include activity option in model/API.

## 6) `ln` vs `log10` Confusion
- Mistake: Switching logs without the `2.303` factor.
- Why wrong: Numerical scaling error in potential term.
- Detect: Compare implementation with known 298.15 K coefficient checks.
- Correct: Keep symbolic `ln` form internally or convert explicitly with `ln(x)=2.303 log10(x)`.

## 7) Wrong Electron Count `n`
- Mistake: Using stoichiometric coefficients not tied to transferred electrons.
- Why wrong: Directly rescales potential relation incorrectly.
- Detect: Balance half-reactions and verify electron cancellation in overall reaction.
- Correct: Use electron-transfer count from balanced overall redox equation.

## 8) Forgetting Temperature Dependence
- Mistake: Hardcoding room-temperature constants for all conditions.
- Why wrong: `RT/(nF)` changes with temperature.
- Detect: Code or derivation uses `0.05916/n` without checking `T=298.15 K`.
- Correct: Keep temperature as explicit input unless fixed by design with explicit constraint.

## 9) Using Butler-Volmer Beyond Its Reasonable Interpretive Scope
- Mistake: Applying BV as if it universally captures all observed polarization behavior.
- Why wrong: Transport, surface changes, or side reactions can dominate.
- Detect: Fit quality degrades systematically at high currents or different regimes.
- Correct: State BV regime assumptions and test transport/side-reaction alternatives.

## 10) Mixing Thermodynamic and Kinetic Logic
- Mistake: Using Nernst to predict current magnitude directly.
- Why wrong: Nernst gives equilibrium potential relation; kinetics gives current response.
- Detect: Outputs current from thermodynamic equation with no kinetic parameters.
- Correct: Use thermodynamics for equilibrium potential, then kinetics for rate/current.

## 11) Ignoring Transport Limitations
- Mistake: Interpreting all current-potential behavior as charge-transfer kinetics.
- Why wrong: Diffusion/migration/convection can cap current and change slopes.
- Detect: Presence of limiting-current behavior or concentration-dependent plateaus.
- Correct: Introduce transport model terms and classify regime as mixed or transport-limited.

## Validation Handoff
- This file should drive future automated checks.
- Codex should convert each failure mode into explicit validation rules in `src/` and test cases in the project test suite.
