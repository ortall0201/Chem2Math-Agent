# Skill Validation Specification (Hybrid: Human + Machine-Usable)

## Purpose
Define repeatable validation cases for electrochemistry-to-math reasoning and implementation handoff.

## Machine-Usable Cases (YAML)
```yaml
schema_version: "1.0"
cases:
  - id: ECHEM-T1
    skill_area: thermodynamic
    input_problem: "Derive the Nernst equation from Delta G = -nFE and Delta G = Delta G^0 + RT ln(Q), then express a base-10 form."
    source_asset: "skills/electrochemistry_skill/test_assets/thermodynamic_nernst_case.yaml"
    source_case_id: "ECHEM-THERMO-NERNST-001"
    expected_reasoning_outcome:
      - "Classify as thermodynamic-only using decision rule R1."
      - "Apply standard-state substitution Delta G^0 = -nFE^0."
      - "Show sign-consistent algebraic isolation of E."
    expected_mathematical_outcome:
      - "E = E^0 - (RT/(nF)) ln(Q)"
      - "E = E^0 - (2.303RT/(nF)) log10(Q)"
    relevant_failure_modes:
      - "1) Sign Errors in Electrochemical Relations"
      - "2) Confusing Delta G and Delta G^0"
      - "6) ln vs log10 Confusion"
    code_validation_possible: true
    code_validation_targets:
      - "nernst_potential(E0, n, Q, T)"

  - id: ECHEM-K1
    skill_area: kinetic
    input_problem: "From Butler-Volmer, derive the anodic and cathodic Tafel limits and state when they are valid."
    expected_reasoning_outcome:
      - "Classify as kinetic-only with limit analysis (R2)."
      - "Declare sign convention for eta and current."
      - "State asymptotic assumptions and limits of interpretation."
    expected_mathematical_outcome:
      - "eta = (RT/(alpha_a nF)) ln(j/j0) for anodic branch"
      - "eta = -(RT/(alpha_c nF)) ln(|j|/j0) for cathodic branch"
    relevant_failure_modes:
      - "6) ln vs log10 Confusion"
      - "9) Using Butler-Volmer Beyond Its Reasonable Interpretive Scope"
      - "10) Mixing Thermodynamic and Kinetic Logic"
    code_validation_possible: true
    code_validation_targets:
      - "butler_volmer_current(j0, eta, n, T, alpha_a, alpha_c)"

  - id: ECHEM-TR1
    skill_area: transport
    input_problem: "Estimate diffusion-limited current density from D, c_bulk, and diffusion-layer thickness delta under 1D steady assumptions."
    expected_reasoning_outcome:
      - "Classify as transport-only using R3."
      - "State planar 1D diffusion assumptions and exclusions (migration/convection not explicit)."
    expected_mathematical_outcome:
      - "j_lim = n F D c_bulk / delta"
    relevant_failure_modes:
      - "11) Ignoring Transport Limitations"
      - "7) Wrong Electron Count n"
    code_validation_possible: true
    code_validation_targets:
      - "diffusion_limited_current_density(n, D, c_bulk, delta)"

  - id: ECHEM-M1
    skill_area: mixed
    input_problem: "Given polarization data with near eta = 0 exponential growth and high-|eta| current plateau, choose a modeling strategy."
    source_asset: "skills/electrochemistry_skill/test_assets/mixed_plateau_case.yaml"
    source_case_id: "ECHEM-MIXED-PLATEAU-001"
    expected_reasoning_outcome:
      - "Classify as mixed using R4."
      - "Use kinetic model in activation region and transport limit at high current."
      - "Reject Nernst-only and BV-only global fit claims."
    expected_mathematical_outcome:
      - "BV relation used for activation-controlled segment."
      - "Transport-limited current bound used for plateau segment."
    relevant_failure_modes:
      - "9) Using Butler-Volmer Beyond Its Reasonable Interpretive Scope"
      - "10) Mixing Thermodynamic and Kinetic Logic"
      - "11) Ignoring Transport Limitations"
    code_validation_possible: true
    code_validation_targets:
      - "butler_volmer_current(j0, eta, n, T, alpha_a, alpha_c)"
      - "diffusion_limited_current_density(n, D, c_bulk, delta)"
      - "classify_regime(problem)"
      - "select_math_path(problem)"
```

## Human Review Checklist
- Confirm each case can be traced to at least one equation in `equations.md`.
- Confirm assumptions are explicit before equations are used.
- Confirm log-base handling and sign convention handling are explicit where relevant.
- Confirm every cited failure mode appears in `failure_modes.md`.
- Confirm `code_validation_possible` aligns with available function contracts in `code_mapping.md`.

## v1 Pass Criteria
- All four machine-usable cases pass human review checks.
- At least one thermodynamic, one kinetic, one transport, and one mixed case are represented.
- At least one case is directly executable once `src/` function contracts are implemented.
