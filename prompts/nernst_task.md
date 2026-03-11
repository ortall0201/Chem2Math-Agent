Benchmark 1: Derive and implement the Nernst equation
=====================================================

Goal
----
Starting only from the two given thermodynamic relations, derive the Nernst equation step by step, explain every symbol, explain where the logarithmic term comes from, interpret how concentration changes affect potential, and implement the final result as a Python function.

Allowed starting relations (the only allowed starting point)
-----------------------------------------------------------
You MUST start from exactly these two relations and no others:

1. \( \Delta G = -n F E \)
2. \( \Delta G = \Delta G^\circ + R T \ln Q \)

Do not introduce additional “known formulas” (e.g., \(E = E^\circ - (RT/nF)\ln Q\), \( \Delta G^\circ = -RT\ln K\), \(E^\circ = (RT/nF)\ln K\), etc.) unless they are explicitly derived from the two relations above.

Derivation requirements
-----------------------
Your output MUST include the following sections, in order.

1. Chemical assumptions (explicit)
   - State what “\(Q\)” represents (reaction quotient) and that it is dimensionless.
   - State whether you are interpreting \(Q\) in terms of activities; if you mention concentrations/pressures, label that as an approximation.
   - State that the sign conventions depend on the reaction as written (i.e., on how \(Q\) is defined for that reaction).

2. Starting relations (verbatim)
   - Restate the two allowed starting relations exactly.
   - Define each symbol used in these relations:
     - \( \Delta G \), \( \Delta G^\circ \), \(n\), \(F\), \(E\), \(R\), \(T\), \(Q\)
   - For each symbol, provide meaning and typical units.

3. Derivation (math steps, no skipping)
   - Explicitly set the two expressions for \( \Delta G \) equal to each other and justify why (same process, same conditions).
   - Solve for \(E\) step by step, showing every algebraic manipulation.
   - Carefully track signs. If you multiply/divide both sides by \(-1\), say so.
   - Introduce \(E^\circ\) by defining it from \( \Delta G^\circ \) and the first relation:
     - Show the algebra that leads to \( \Delta G^\circ = -n F E^\circ \).
   - Substitute that definition into your expression for \(E\) and simplify, step by step.

4. Where the logarithm comes from (conceptual)
   - Explain in plain technical language why a \(\ln Q\) term appears:
     - It is already present in the second starting relation as the thermodynamic correction from standard conditions to the current composition.
   - Do NOT introduce additional thermodynamic identities. Stay anchored to the two relations.
   - If you mention a base-10 form, you MUST show the conversion \( \ln x = 2.303 \log_{10} x \) and identify \(2.303 = \ln 10\).

5. Final equation (boxed)
   - Present the final Nernst equation explicitly for \(E\) as a function of \(E^\circ\), \(T\), \(n\), and \(Q\).
   - State clearly whether your final equation uses \(\ln\) or \(\log_{10}\). Prefer \(\ln\).

6. Interpretation (words, not just symbols)
   - Explain how changing concentrations (i.e., changing \(Q\)) affects \(E\).
   - Include at least these two checks:
     - When \(Q = 1\), show what \(E\) reduces to and explain why.
     - When \(Q\) increases, state whether \(E\) increases or decreases (for the reaction as written), and connect that to the sign in your final equation.

Code implementation requirements
--------------------------------
After the derivation, write a minimal Python function implementing the final Nernst equation.

1. Function spec
   - Implement: `nernst_potential(E0, T, n, Q) -> float`
   - Use the natural logarithm: `math.log(Q)` (this is \(\ln Q\)).
   - Use only the Python standard library.

2. Validation requirements
   - Validate basic domain constraints:
     - \(T > 0\)
     - \(n > 0\)
     - \(Q > 0\)
   - Raise `ValueError` with a clear message when constraints are violated.

3. Constants
   - Use numeric constants inside the function (or module-level constants) for:
     - \(R\) (gas constant)
     - \(F\) (Faraday constant)
   - State their units in the docstring.

4. Minimal example
   - Provide one simple example demonstrating usage and expected approximate output.

