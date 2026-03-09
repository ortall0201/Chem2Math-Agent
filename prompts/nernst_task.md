Task: Derive and implement the Nernst equation
=============================================

Goal
----
Starting only from the two thermodynamic relations in `knowledge/core_principles.md`, derive the Nernst equation step by step, explain the meaning of each symbol, explain where the logarithmic term comes from, and then implement the final equation as a Python function.

Given core principles
---------------------
You must use only the following relations as your starting point:
- \( \Delta G = -n F E \)
- \( \Delta G = \Delta G^\circ + R T \ln Q \)

Here:
- \( \Delta G \) is the Gibbs free energy change under the given conditions.
- \( \Delta G^\circ \) is the standard Gibbs free energy change.
- \( n \) is the number of moles of electrons transferred in the redox reaction.
- \( F \) is the Faraday constant.
- \( E \) is the cell potential under the given conditions.
- \( R \) is the gas constant.
- \( T \) is the absolute temperature (in kelvin).
- \( Q \) is the reaction quotient.

Derivation requirements
-----------------------
1. **State assumptions explicitly**
   - State any assumptions you make about the reaction, temperature, or activities vs. concentrations.
   - Make clear that you are working within classical electrochemical thermodynamics.

2. **Align the two expressions for \( \Delta G \)**
   - Show clearly how \( \Delta G = -n F E \) and \( \Delta G = \Delta G^\circ + R T \ln Q \) can be equated.
   - Justify why it is valid to equate them for the same process under the same conditions.

3. **Solve for \( E \)**
   - Perform the algebra step by step to obtain an expression for \( E \) as a function of \( E^\circ \), \( T \), \( n \), and \( Q \).
   - Carefully track minus signs at each algebraic step.
   - Define \( E^\circ \) in terms of \( \Delta G^\circ \).

4. **Explain the logarithmic term**
   - Explain clearly why a logarithmic term \( \ln Q \) appears in the final expression.
   - Connect the logarithm to:
     - The dependence of Gibbs free energy on the reaction quotient.
     - The statistical/thermodynamic interpretation (at a high level, not in full detail).
   - If you convert the expression from \( \ln \) to \( \log_{10} \), show the conversion factor \( 2.303 \) explicitly and explain its origin.

5. **Define all symbols and units**
   - For the final Nernst equation, list each symbol, its meaning, and its typical units.
   - Note any common conventions (e.g., temperature in kelvin, potentials in volts).

6. **Discuss sign conventions**
   - Explain the sign of the \( \ln Q \) term and how it depends on the direction of the reaction as written.
   - Clarify how increasing \( Q \) affects \( E \), and why this makes physical sense.

Code implementation requirements
--------------------------------
After the derivation, write a minimal Python function implementing the final Nernst equation.

1. **Function specification**
   - Implement a function `nernst_potential(E0, T, n, Q)` in Python.
   - Use the natural logarithm form as the primary implementation.
   - You may optionally mention a base-10 logarithm variant, but the core implementation should use `math.log` (natural log).

2. **Docstring and arguments**
   - Include a short docstring that:
     - States the mathematical form being implemented.
     - Defines each argument (`E0`, `T`, `n`, `Q`) and the expected units.
   - Assume `F` and `R` are given as constants inside the function, with clear values and units.

3. **Correctness constraints**
   - The code must correspond exactly to your final derived equation.
   - Handle sign conventions carefully so that the behavior of \( E \) as a function of \( Q \) matches the derived and physical expectations.
   - Use only the Python standard library (`math`).

4. **Sanity check**
   - Briefly describe how you would sanity-check the function (e.g., behavior as \( Q \to 1 \), or comparison to the standard 25 °C form).

