Evaluation rubric: Benchmark 1 (Nernst equation)
================================================

How to use this rubric
----------------------
Score each category on a 0–2 scale:
- **0**: incorrect / missing
- **1**: partially correct / incomplete
- **2**: correct and complete

Record notes for each category (especially failures). Total score is the sum.

Recommended gate (pass/fail)
----------------------------
Mark **FAIL** if any of the following are true:
- The final Nernst equation is algebraically incorrect.
- A sign error changes the physical dependence on \(Q\).
- \(\ln\) vs. \(\log_{10}\) is confused (or conversion factor is wrong).
- The code does not match the stated final equation.

Rubric (0–2 each)
-----------------

1) Constraint compliance (starting relations only)
--------------------------------------------------
- **2**: Uses only \( \Delta G = -nFE \) and \( \Delta G = \Delta G^\circ + RT\ln Q \) as starting relations; any additional statements are explicitly derived from them.
- **1**: Mostly respects constraints but briefly references an external identity without relying on it materially.
- **0**: Uses external formulas as starting points or substitutes them for derivation.

2) Symbol definitions and units
-------------------------------
- **2**: Defines every symbol (\(\Delta G, \Delta G^\circ, E, E^\circ, n, F, R, T, Q\)) with meaning and typical units; notes \(Q\) is dimensionless.
- **1**: Defines most symbols but misses some units/definitions or is inconsistent.
- **0**: Missing or incorrect symbol meanings; unclear what quantities represent.

3) Algebraic derivation (step-by-step)
--------------------------------------
- **2**: Shows every algebraic step from the two relations to the final \(E(\cdot)\); no unjustified jumps.
- **1**: Main path is correct but skips nontrivial steps or has minor, nonfatal slips.
- **0**: Major algebraic mistakes or derivation is not reproducible.

4) Sign conventions and physical directionality
-----------------------------------------------
- **2**: Sign handling is correct throughout; defines \(E^\circ\) from \(\Delta G^\circ = -nF E^\circ\); final equation has correct sign on the \(\ln Q\) term and the interpretation matches it.
- **1**: Mostly correct but with a small ambiguity or an unclear sign justification.
- **0**: Sign error or ambiguous convention that changes the predicted behavior of \(E\) vs. \(Q\).

5) Logarithm conventions (\(\ln\) vs. \(\log_{10}\))
----------------------------------------------------
- **2**: Uses \(\ln\) consistently; if \(\log_{10}\) is mentioned, converts correctly with \( \ln x = (\ln 10)\log_{10}x \approx 2.303\log_{10}x \) and explains \(2.303 = \ln 10\).
- **1**: Final form is correct but conversion explanation is incomplete or ambiguous.
- **0**: Mixes \(\ln\) and \(\log_{10}\) incorrectly or uses the wrong numerical factor.

6) Scientific meaning preserved
-------------------------------
- **2**: Clearly distinguishes chemical assumptions from math steps; states conditions/assumptions (e.g., activities vs concentrations approximation) without overclaiming.
- **1**: Meaning mostly preserved but assumptions are incomplete, mixed into algebra, or not clearly labeled.
- **0**: Misrepresents what \(Q\) is, what \(E\) represents, or otherwise breaks scientific meaning.

7) Interpretation: effect of concentration/composition
------------------------------------------------------
- **2**: Explains in words how changes in \(Q\) affect \(E\); includes checks \(Q=1\) and “increasing \(Q\)” consistent with the derived sign.
- **1**: Provides some interpretation but misses one check or is not clearly tied to the final equation.
- **0**: Interpretation contradicts the derived equation or is absent.

8) Code correctness and alignment
---------------------------------
- **2**: Python function implements exactly \( E = E^\circ - \frac{RT}{nF}\ln Q \) (or equivalent derived form), uses `math.log` for \(\ln\), includes correct constants, and matches the docstring.
- **1**: Code mostly correct but has minor issues (unclear docstring, slight mismatch in naming, weak validation).
- **0**: Code does not match the derived equation or uses the wrong log base/sign.

9) Input validation and domain handling
---------------------------------------
- **2**: Validates \(T>0\), \(n>0\), \(Q>0\) and raises clear errors; does not silently coerce invalid inputs.
- **1**: Some validation present but incomplete or error messages are unclear.
- **0**: No validation; accepts invalid domains leading to misleading outputs or runtime errors.

10) Mistake detection / self-checks
-----------------------------------
- **2**: Explicitly checks for common pitfalls (sign, \(\ln\) vs \(\log_{10}\), \(Q=1\) sanity check) and corrects any issues found.
- **1**: Mentions one check but not systematic.
- **0**: No self-checking; errors pass through unexamined.

