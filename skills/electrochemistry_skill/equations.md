# Canonical Equations (v1)

## 1) Free Energy - Potential Relation
### Equation
`Delta G = -n F E`

### Variables
- `Delta G`: Gibbs free energy change (`J/mol`)
- `n`: moles of electrons transferred (dimensionless)
- `F`: Faraday constant (`C/mol`)
- `E`: cell potential (`V = J/C`)

### Assumptions
- Consistent reaction direction and sign convention are used.
- `n` matches the balanced overall electrochemical reaction.

### Domain of Use
- Thermodynamic conversion between free-energy change and electrical potential.

### Common Misuse
- Wrong sign from inconsistent reaction direction.
- Using incorrect electron count `n`.

---

## 2) Standard-State Correction
### Equation
`Delta G = Delta G^0 + R T ln(Q)`

### Variables
- `Delta G`: non-standard Gibbs free energy change
- `Delta G^0`: standard Gibbs free energy change
- `R`: gas constant (`J/(mol*K)`)
- `T`: absolute temperature (`K`)
- `Q`: reaction quotient (dimensionless, activity-based)

### Assumptions
- Same reaction stoichiometry is used in both `Delta G` and `Q`.
- `Q` is defined from activities; concentration-only form is approximate.

### Domain of Use
- Thermodynamic correction from standard to actual conditions.

### Common Misuse
- Treating `Q` as dimensional without normalization.
- Mixing activity-based derivation with concentration values without caveat.

---

## 3) Nernst Equation
### Equation
`E = E^0 - (R T / (n F)) ln(Q)`

Alternative base-10 form:
`E = E^0 - (2.303 R T / (n F)) log10(Q)`

### Variables
- `E`: cell/equilibrium potential at specified composition
- `E^0`: standard potential
- `R, T, n, F, Q`: as defined above

### Assumptions
- Equilibrium thermodynamic framework is appropriate.
- Activities (or clearly labeled concentration approximations) are used in `Q`.

### Domain of Use
- Predicting composition and temperature dependence of equilibrium potential.

### Common Misuse
- Confusing `ln` with `log10` without conversion factor `2.303`.
- Using `0.05916/n` outside `298.15 K`.

---

## 4) Butler-Volmer Equation
### Equation
`j = j0 * [exp((alpha_a n F eta)/(R T)) - exp(-(alpha_c n F eta)/(R T))]`

Symmetric simplified case often uses `alpha_a = alpha_c = alpha`.

### Variables
- `j`: net current density (`A/m^2`)
- `j0`: exchange current density (`A/m^2`)
- `eta`: overpotential (`V`)
- `alpha_a, alpha_c`: anodic/cathodic transfer coefficients
- `n, F, R, T`: as above

### Assumptions
- Charge-transfer controlled interface behavior in modeled regime.
- Parameters (`j0`, `alpha`) are valid for the local conditions.

### Domain of Use
- Electrode kinetics near and beyond equilibrium overpotential, with care.

### Common Misuse
- Applying without checking transport limitations.
- Ignoring stated sign convention for `eta`.

---

## 5) Tafel Behavior (Limiting Form Note)
### Equation (conceptual limit)
For sufficiently large `|eta|`, one exponential term dominates:
- anodic branch: `eta ~ (R T / (alpha_a n F)) ln(|j|/j0)`
- cathodic branch analogous with sign change.

### Assumptions
- One BV exponential dominates.
- Same kinetic regime and parameter validity as BV.

### Domain of Use
- Approximate linear relation in `eta` vs `log|j|` plots in selected ranges.

### Common Misuse
- Treating Tafel form as globally valid across all overpotentials.

---

## 6) Fick's First Law (Transport Anchor)
### Equation
`J_i = -D_i * grad(c_i)` (1D: `J_i = -D_i dc_i/dx`)

### Variables
- `J_i`: diffusive flux of species `i`
- `D_i`: diffusion coefficient
- `c_i`: concentration field

### Assumptions
- Diffusion-dominated local transport description.
- Coefficient and geometry assumptions are explicit.

### Domain of Use
- Transport-limitation reasoning and first-order concentration-gradient modeling.

### Common Misuse
- Ignoring migration/convection when they are non-negligible.

---

## v1 Scope Boundary
Advanced interfacial/impedance formalisms are out of scope in v1 and should be added in future skill versions with dedicated assumptions and validation tests.
