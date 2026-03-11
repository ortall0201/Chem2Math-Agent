"""
Minimal electrochemistry execution layer for regime selection and core equations.

This module intentionally stays small:
- Butler-Volmer current (kinetic)
- Diffusion-limited current-density helper (transport)
- Rule-based regime selector/orchestrator (thermo/kinetic/transport/mixed)
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Literal

try:
    from .nernst import F_FARADAY, R_GAS_CONSTANT, nernst_potential
except ImportError:
    from nernst import F_FARADAY, R_GAS_CONSTANT, nernst_potential

Regime = Literal["thermodynamic-only", "kinetic-only", "transport-only", "mixed"]


def butler_volmer_current(
    j0: float,
    eta: float,
    n: int,
    T: float,
    alpha_a: float,
    alpha_c: float,
    F: float = F_FARADAY,
    R: float = R_GAS_CONSTANT,
) -> float:
    """
    Compute Butler-Volmer net current density.

    j = j0 * [exp((alpha_a*n*F*eta)/(R*T)) - exp(-(alpha_c*n*F*eta)/(R*T))]
    """
    if not isinstance(n, int):
        raise TypeError(f"n must be an int, got {type(n).__name__}")

    try:
        j0_f = float(j0)
        eta_f = float(eta)
        T_f = float(T)
        aa_f = float(alpha_a)
        ac_f = float(alpha_c)
        F_f = float(F)
        R_f = float(R)
    except (TypeError, ValueError) as e:
        raise TypeError("j0, eta, T, alpha_a, alpha_c, F, and R must be real numbers") from e

    if j0_f <= 0:
        raise ValueError("j0 must be > 0")
    if n <= 0:
        raise ValueError("n must be > 0")
    if T_f <= 0:
        raise ValueError("T must be > 0 (kelvin)")
    if not (0 < aa_f <= 1):
        raise ValueError("alpha_a must be in (0, 1]")
    if not (0 < ac_f <= 1):
        raise ValueError("alpha_c must be in (0, 1]")
    if F_f <= 0 or R_f <= 0:
        raise ValueError("F and R must be > 0")

    anodic = math.exp((aa_f * n * F_f * eta_f) / (R_f * T_f))
    cathodic = math.exp(-(ac_f * n * F_f * eta_f) / (R_f * T_f))
    return j0_f * (anodic - cathodic)


def diffusion_limited_current_density(
    n: int,
    D: float,
    c_bulk: float,
    delta: float,
    F: float = F_FARADAY,
) -> float:
    """
    Estimate 1D diffusion-limited current-density magnitude.

    j_lim = n * F * D * c_bulk / delta
    """
    if not isinstance(n, int):
        raise TypeError(f"n must be an int, got {type(n).__name__}")

    try:
        D_f = float(D)
        c_f = float(c_bulk)
        delta_f = float(delta)
        F_f = float(F)
    except (TypeError, ValueError) as e:
        raise TypeError("D, c_bulk, delta, and F must be real numbers") from e

    if n <= 0:
        raise ValueError("n must be > 0")
    if D_f <= 0:
        raise ValueError("D must be > 0")
    if c_f < 0:
        raise ValueError("c_bulk must be >= 0")
    if delta_f <= 0:
        raise ValueError("delta must be > 0")
    if F_f <= 0:
        raise ValueError("F must be > 0")

    return n * F_f * D_f * c_f / delta_f


def classify_regime(problem: Dict[str, Any]) -> Regime:
    """
    Classify electrochemistry problem into thermo/kinetic/transport/mixed.

    Required keys are boolean feature flags. Missing flags default to False.
    """
    has_current_overpotential = bool(problem.get("has_current_overpotential_data", False))
    asks_equilibrium = bool(problem.get("asks_equilibrium_potential", False))
    asks_spontaneity = bool(problem.get("asks_reaction_spontaneity", False))
    has_plateau = bool(problem.get("has_limiting_current_plateau", False))
    has_transport_clues = bool(problem.get("mentions_transport_limitations", False))
    has_exponential_near_zero = bool(problem.get("has_exponential_region_near_zero_eta", False))
    charge_transfer_control = bool(problem.get("assumes_charge_transfer_control", False))
    asks_flux = bool(problem.get("asks_flux_or_limiting_current", False))

    # R4 mixed: simultaneous activation signature + transport signature.
    if has_exponential_near_zero and (has_plateau or has_transport_clues):
        return "mixed"

    # R1 thermodynamic-only: equilibrium/spontaneity question without current behavior target.
    if (asks_equilibrium or asks_spontaneity) and not has_current_overpotential:
        return "thermodynamic-only"

    # R3 transport-only: transport/limiting-current target with no kinetic fit target.
    if asks_flux and not has_current_overpotential:
        return "transport-only"

    # R2 kinetic-only: current-overpotential relation under charge-transfer control and no plateau clues.
    if has_current_overpotential and charge_transfer_control and not (has_plateau or has_transport_clues):
        return "kinetic-only"

    # Conservative default for ambiguous data: mixed.
    return "mixed"


def select_math_path(problem: Dict[str, Any]) -> Dict[str, Any]:
    """
    Select equation family and implementation path from problem descriptors.
    """
    regime = classify_regime(problem)

    if regime == "thermodynamic-only":
        return {
            "classification": regime,
            "equation_family": ["Nernst / Gibbs-potential relations"],
            "functions": ["nernst_potential(E0, n, Q, T)"],
            "failure_modes_to_check": [
                "Sign Errors in Electrochemical Relations",
                "Confusing Delta G and Delta G^0",
                "ln vs log10 Confusion",
            ],
        }

    if regime == "kinetic-only":
        return {
            "classification": regime,
            "equation_family": ["Butler-Volmer", "Tafel (limit only)"],
            "functions": ["butler_volmer_current(j0, eta, n, T, alpha_a, alpha_c)"],
            "failure_modes_to_check": [
                "Using Butler-Volmer Beyond Its Reasonable Interpretive Scope",
                "Mixing Thermodynamic and Kinetic Logic",
            ],
        }

    if regime == "transport-only":
        return {
            "classification": regime,
            "equation_family": ["Fick transport anchor", "diffusion-limited current helper"],
            "functions": ["diffusion_limited_current_density(n, D, c_bulk, delta)"],
            "failure_modes_to_check": [
                "Ignoring Transport Limitations",
                "Wrong Electron Count n",
            ],
        }

    return {
        "classification": "mixed",
        "equation_family": ["Butler-Volmer (activation region)", "Transport-limited bound"],
        "functions": [
            "butler_volmer_current(j0, eta, n, T, alpha_a, alpha_c)",
            "diffusion_limited_current_density(n, D, c_bulk, delta)",
        ],
        "failure_modes_to_check": [
            "Using Butler-Volmer Beyond Its Reasonable Interpretive Scope",
            "Mixing Thermodynamic and Kinetic Logic",
            "Ignoring Transport Limitations",
        ],
    }


def orchestrate_problem(problem: Dict[str, Any]) -> Dict[str, Any]:
    """
    Minimal orchestration entrypoint.

    If enough parameters are present, compute one representative value.
    Otherwise return only the selected path.
    """
    plan = select_math_path(problem)
    out: Dict[str, Any] = {"plan": plan, "computed": {}}

    classification = plan["classification"]

    if classification == "thermodynamic-only":
        required = ["E0", "T", "n", "Q"]
        if all(k in problem for k in required):
            out["computed"]["E"] = nernst_potential(
                E0=problem["E0"], n=problem["n"], Q=problem["Q"], T=problem["T"]
            )
        return out

    if classification == "kinetic-only":
        required = ["j0", "eta", "n", "T", "alpha_a", "alpha_c"]
        if all(k in problem for k in required):
            out["computed"]["j"] = butler_volmer_current(
                j0=problem["j0"],
                eta=problem["eta"],
                n=problem["n"],
                T=problem["T"],
                alpha_a=problem["alpha_a"],
                alpha_c=problem["alpha_c"],
            )
        return out

    if classification == "transport-only":
        required = ["n", "D", "c_bulk", "delta"]
        if all(k in problem for k in required):
            out["computed"]["j_lim"] = diffusion_limited_current_density(
                n=problem["n"],
                D=problem["D"],
                c_bulk=problem["c_bulk"],
                delta=problem["delta"],
            )
        return out

    # mixed
    required_kin = ["j0", "eta", "n", "T", "alpha_a", "alpha_c"]
    required_tr = ["n", "D", "c_bulk", "delta"]

    if all(k in problem for k in required_kin):
        out["computed"]["j_kinetic"] = butler_volmer_current(
            j0=problem["j0"],
            eta=problem["eta"],
            n=problem["n"],
            T=problem["T"],
            alpha_a=problem["alpha_a"],
            alpha_c=problem["alpha_c"],
        )
    if all(k in problem for k in required_tr):
        out["computed"]["j_lim"] = diffusion_limited_current_density(
            n=problem["n"],
            D=problem["D"],
            c_bulk=problem["c_bulk"],
            delta=problem["delta"],
        )
    if "j_kinetic" in out["computed"] and "j_lim" in out["computed"]:
        # Conservative mixed prediction as transport-capped magnitude with kinetic sign.
        sign = 1.0 if out["computed"]["j_kinetic"] >= 0 else -1.0
        out["computed"]["j_mixed_capped"] = sign * min(
            abs(out["computed"]["j_kinetic"]),
            abs(out["computed"]["j_lim"]),
        )
    return out


__all__: List[str] = [
    "butler_volmer_current",
    "diffusion_limited_current_density",
    "classify_regime",
    "select_math_path",
    "orchestrate_problem",
]
