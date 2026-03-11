# Derivations

## Fully Worked Derivation: Nernst Equation

### Goal
Derive:
`E = E^0 - (R T / (n F)) ln(Q)`

Starting only from:
1. `Delta G = -n F E`
2. `Delta G = Delta G^0 + R T ln(Q)`

### Step 1: Write the two expressions for `Delta G`
- Equation A: `Delta G = -n F E`
- Equation B: `Delta G = Delta G^0 + R T ln(Q)`

Because both right-hand sides equal `Delta G`, set them equal:
`-n F E = Delta G^0 + R T ln(Q)`

Common error:
- Dropping the negative sign in `-n F E`.

### Step 2: Express the standard-state free energy with standard potential
Apply Equation A at standard state:
`Delta G^0 = -n F E^0`

Substitute into the previous line:
`-n F E = -n F E^0 + R T ln(Q)`

Common error:
- Using `E` instead of `E^0` in the standard-state substitution.

### Step 3: Rearrange to isolate the potential term
Start from:
`-n F E = -n F E^0 + R T ln(Q)`

Add `n F E` to both sides:
`0 = -n F E^0 + n F E + R T ln(Q)`

Rearrange:
`n F (E - E^0) + R T ln(Q) = 0`

Move the logarithm term:
`n F (E - E^0) = -R T ln(Q)`

Divide by `n F`:
`E - E^0 = -(R T / (n F)) ln(Q)`

Add `E^0` to both sides:
`E = E^0 - (R T / (n F)) ln(Q)`

Common errors:
- Sign inversion mistakes during term movement.
- Forgetting to divide the entire right side by `nF`.

### Step 4: Explain where `ln(Q)` comes from
`ln(Q)` appears because the non-standard free-energy correction is logarithmic:
`Delta G - Delta G^0 = R T ln(Q)`.
This is the thermodynamic composition correction that shifts potential from `E^0` to `E`.

Common error:
- Treating composition correction as linear in `Q` instead of logarithmic.

### Step 5: Convert natural log to base-10 log (optional form)
Use identity:
`ln(Q) = 2.303 log10(Q)`

Substitute:
`E = E^0 - (2.303 R T / (n F)) log10(Q)`

At `T = 298.15 K`, coefficient simplifies numerically:
`2.303 R T / F ~ 0.05916 V`

So:
`E = E^0 - (0.05916 / n) log10(Q)` at `298.15 K`

Common errors:
- Using `log10` form without multiplying by `2.303`.
- Using `0.05916` at temperatures other than `298.15 K`.

### Final Checks
- `Q` must be dimensionless (activity-based definition).
- `n` must match balanced electron transfer in the overall reaction.
- Sign convention for cell direction must be consistent across all equations.

## Placeholder: Future Derivations (v2+)
- Butler-Volmer from interfacial rate expressions with explicit overpotential convention.
- Tafel approximation as asymptotic Butler-Volmer limit with validity window.
- Transport-limited current derivations coupling kinetics and Fick/Nernst-Planck terms.

## Fully Worked Derivation: Tafel Limit from Butler-Volmer

### Goal
Derive a kinetic limiting form from Butler-Volmer:
- anodic limit: `eta = (R T / (alpha_a n F)) * ln(j / j0)`
- cathodic limit: `eta = -(R T / (alpha_c n F)) * ln(|j| / j0)`

### Starting Equation (Butler-Volmer)
`j = j0 * [exp((alpha_a n F eta)/(R T)) - exp(-(alpha_c n F eta)/(R T))]`

### Variable Definitions
- `j`: net current density (`A/m^2`)
- `j0`: exchange current density (`A/m^2`)
- `eta`: overpotential (`V`)
- `alpha_a`, `alpha_c`: anodic/cathodic transfer coefficients (dimensionless)
- `n`: electron-transfer number (dimensionless)
- `F`: Faraday constant (`C/mol`)
- `R`: gas constant (`J/(mol*K)`)
- `T`: absolute temperature (`K`)

### Assumptions
1. Charge-transfer kinetics are represented by Butler-Volmer in this regime.
2. `j0`, `alpha_a`, `alpha_c` are treated as constants over the fitted range.
3. Overpotential magnitude is large enough that one exponential term dominates.
4. Transport and ohmic drop are not dominating the selected data segment.

### Sign Convention Used Here
- Positive `eta` and positive `j` denote anodic polarization/current.
- Negative `eta` and negative `j` denote cathodic polarization/current.
- Any other convention can be used, but must be applied consistently.

### A) Anodic Tafel Limit (`eta >> 0`)

#### Step A1: Write BV form
`j = j0 * [exp((alpha_a n F eta)/(R T)) - exp(-(alpha_c n F eta)/(R T))]`

#### Step A2: Apply large positive overpotential condition
For `eta >> 0`, the second exponential has a large negative argument, so:
`exp(-(alpha_c n F eta)/(R T)) ~ 0`

Therefore:
`j ~ j0 * exp((alpha_a n F eta)/(R T))`

#### Step A3: Divide by `j0`
`j / j0 ~ exp((alpha_a n F eta)/(R T))`

#### Step A4: Take natural logarithm
`ln(j / j0) ~ (alpha_a n F eta)/(R T)`

#### Step A5: Solve for `eta`
`eta ~ (R T / (alpha_a n F)) * ln(j / j0)`

This is the anodic Tafel form in natural-log notation.

### B) Cathodic Tafel Limit (`eta << 0`)

#### Step B1: Start from BV
`j = j0 * [exp((alpha_a n F eta)/(R T)) - exp(-(alpha_c n F eta)/(R T))]`

#### Step B2: Apply large negative overpotential condition
For `eta << 0`, first exponential has large negative argument, so:
`exp((alpha_a n F eta)/(R T)) ~ 0`

Therefore:
`j ~ -j0 * exp(-(alpha_c n F eta)/(R T))`

Net `j` is negative, so use magnitude:
`|j| ~ j0 * exp(-(alpha_c n F eta)/(R T))`

#### Step B3: Divide by `j0`
`|j| / j0 ~ exp(-(alpha_c n F eta)/(R T))`

#### Step B4: Take natural logarithm
`ln(|j| / j0) ~ -(alpha_c n F eta)/(R T)`

#### Step B5: Solve for `eta`
`eta ~ -(R T / (alpha_c n F)) * ln(|j| / j0)`

This is the cathodic Tafel form in natural-log notation.

### Base-10 Conversion (Optional)
Using `ln(x) = 2.303 log10(x)`:
- anodic: `eta ~ (2.303 R T / (alpha_a n F)) * log10(j / j0)`
- cathodic: `eta ~ -(2.303 R T / (alpha_c n F)) * log10(|j| / j0)`

### Limits of Interpretation
- This is an asymptotic approximation, not a universal replacement for full BV.
- Near equilibrium (`eta ~ 0`), both exponentials matter; use full BV.
- At high current, transport limitations can distort apparent Tafel slopes.
- Apparent linearity in a narrow window does not prove global Tafel validity.

### Common Derivation Mistakes
1. Dropping the minus sign in the cathodic branch.
2. Using `log10` without the `2.303` conversion factor.
3. Applying Tafel form at small `|eta|` where both BV terms are significant.
4. Ignoring transport limitation and misattributing curvature to kinetic parameters only.
5. Mixing `j` and `|j|` inconsistently in cathodic expressions.
