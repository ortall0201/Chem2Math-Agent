# Foundational Principles

## 1) Gibbs Free Energy and Electrical Work
- Electrochemical cell work is linked to free energy by `Delta G = -nFE`.
- Sign meaning:
  - `Delta G < 0` corresponds to spontaneous direction under specified conditions.
  - For that direction, the corresponding cell potential is positive under the same sign convention.

## 2) Standard vs Non-Standard States
- `Delta G^0` and `E^0` refer to standard-state reference conditions.
- Non-standard composition enters through the reaction quotient:
  - `Delta G = Delta G^0 + RT ln(Q)`.
- This separation is required to move from reference thermodynamics to real conditions.

## 3) Role of Reaction Quotient and Activity
- `Q` is formally built from activities, not raw concentrations.
- Concentration-based `Q_c` is an approximation and should be labeled as such.
- If ionic strength is significant or non-ideal behavior is expected, activity corrections are necessary for rigor.

## 4) Thermodynamic Interpretation of Potential
- `E` is a thermodynamic driving-force representation when tied to `Delta G`.
- Nernst gives equilibrium potential shift with composition and temperature under the model assumptions.

## 5) Kinetic Interpretation of Current-Overpotential
- Butler-Volmer connects overpotential `eta` to current density `j`.
- Kinetics govern rate/current response, not equilibrium thermodynamic state definition.

## 6) Thermodynamics vs Kinetics
- Thermodynamics answers: "What is the equilibrium potential and direction?"
- Kinetics answers: "How fast/current at a given overpotential?"
- Conflating these leads to incorrect conclusions, especially in polarization analysis.

## 7) Importance of Transport Limitations
- Observed current can be limited by mass transport even if charge-transfer kinetics are fast.
- Any model claiming kinetic interpretation should check whether diffusion/migration/convection constraints are negligible.

## 8) Why Activities Matter Fundamentally
- Chemical potential is defined via activity terms.
- Using concentration in place of activity is a modeling approximation, not a fundamental identity.
- This distinction must be preserved in derivations and code APIs.
