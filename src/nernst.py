"""
Minimal Nernst equation utilities.

Derived from the core relations in `knowledge/core_principles.md`:
- Delta G = -n F E
- Delta G = Delta G^0 + R T ln Q
"""

from __future__ import annotations

import math

# SI units
R_GAS_CONSTANT = 8.314462618  # J/(mol*K)
F_FARADAY = 96485.33212  # C/mol = J/(V*mol)


def nernst_potential(E0: float, n: int, Q: float, T: float) -> float:
    """
    Compute the cell potential using the Nernst equation (natural log form).

    Implements:
        E = E0 - (R*T/(n*F)) * ln(Q)

    where `ln` is the natural logarithm.

    Parameters
    ----------
    E0 : float
        Standard cell potential (volts).
    n : int
        Number of electrons transferred (dimensionless). Must be a positive integer.
    Q : float
        Reaction quotient (dimensionless). Must be > 0.
    T : float
        Temperature (kelvin). Must be > 0.

    Returns
    -------
    float
        Cell potential E (volts).

    Example
    -------
    >>> round(nernst_potential(1.10, 2, 10.0, 298.15), 4)
    1.0704
    """
    if not isinstance(n, int):
        raise TypeError(f"n must be an int (electrons transferred), got {type(n).__name__}")

    try:
        E0_f = float(E0)
        Q_f = float(Q)
        T_f = float(T)
    except (TypeError, ValueError) as e:
        raise TypeError("E0, Q, and T must be real numbers") from e

    if T_f <= 0:
        raise ValueError("T must be > 0 (kelvin)")
    if n <= 0:
        raise ValueError("n must be > 0")
    if Q_f <= 0:
        raise ValueError("Q must be > 0 (reaction quotient is dimensionless)")

    return E0_f - (R_GAS_CONSTANT * T_f / (n * F_FARADAY)) * math.log(Q_f)


__all__ = ["nernst_potential", "R_GAS_CONSTANT", "F_FARADAY"]
