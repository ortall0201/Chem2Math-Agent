Evaluation rubric: Chem2Math Agent – Nernst derivation
=======================================================

Scoring
-------
- Each criterion can be scored on a 0–2 scale:
  - 0 = not demonstrated / incorrect.
  - 1 = partially correct or incomplete.
  - 2 = fully correct and clear.
- Total score is the sum over all criteria.

1. Algebraic correctness
------------------------
- **2**: All algebraic steps from the starting relations to the final Nernst equation are correct, with no unjustified jumps.
- **1**: Main structure is correct but contains one or two minor algebraic slips that do not fundamentally change the equation.
- **0**: Major algebraic mistakes that lead to an incorrect or unusable form of the Nernst equation.

2. Sign handling
----------------
- **2**: All signs are tracked carefully; the final dependence of \( E \) on \( Q \) has the correct sign and physical interpretation.
- **1**: Mostly correct sign handling, but with minor inconsistencies or unclear justifications.
- **0**: Incorrect sign conventions that reverse or corrupt the physical meaning of the relation.

3. Correct use of \( \ln \) vs. \( \log_{10} \)
----------------------------------------------
- **2**: Clear distinction between natural logarithm and base-10 logarithm; any conversion is done correctly and the factor \( 2.303 \) is properly explained.
- **1**: Uses the correct final form but does not clearly justify or explain the choice of logarithm base or the conversion factor.
- **0**: Confuses \(\ln\) and \(\log_{10}\), or introduces an incorrect numerical factor.

4. Preservation of scientific meaning
-------------------------------------
- **2**: The derivation preserves the scientific meaning of each quantity; assumptions and conditions of validity are stated clearly.
- **1**: The main physical meaning is present but some assumptions or interpretations are missing or vague.
- **0**: Key scientific meaning is lost, misrepresented, or contradicted during the derivation.

5. Clarity of explanation
-------------------------
- **2**: Steps are presented in a logical order; chemical assumptions are clearly separated from mathematical transformations; all symbols are defined.
- **1**: Explanation is understandable but omits some definitions, mixes chemical and mathematical reasoning, or skips nontrivial steps.
- **0**: Explanation is confusing, disorganized, or omits important reasoning steps.

6. Code correctness
-------------------
- **2**: The Python implementation matches the final derived equation exactly, with correct use of constants, arguments, and logarithms; docstring clearly states meaning and units.
- **1**: Code is mostly correct but contains minor issues (e.g., unclear documentation, mild inconsistency with the written equation).
- **0**: Code does not implement the stated equation, contains serious mistakes, or is unusable.

7. Ability to detect and correct mistakes
-----------------------------------------
- **2**: The agent explicitly checks for common pitfalls (sign errors, logarithm base, unit consistency) and corrects or flags them when they arise.
- **1**: The agent occasionally notices inconsistencies but does not systematically check for them.
- **0**: The agent accepts and propagates errors without detection or correction.

