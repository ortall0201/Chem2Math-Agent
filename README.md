Chem2Math Agent is a small research project exploring whether an AI system can act as a precise interface between chemistry and mathematics.

The goal is to take well-defined chemical principles, translate them into formal mathematical structures, and then turn those structures into simple, correct code. The emphasis is on scientific and algebraic correctness rather than style.

Main project flow:

Chemistry -> Math -> Code

The first benchmark for this repository is the Nernst equation: starting from basic thermodynamic relations, the agent should derive the Nernst equation step by step, explain each symbol, justify the appearance of the logarithmic term, and produce a minimal Python implementation.

Current v1 implementation status:
- Domain skill package: `skills/electrochemistry_skill/`
- Thermodynamic equation function: `src/nernst.py` (`nernst_potential`)
- Minimal regime orchestrator: `src/electrochemistry_orchestrator.py`
  - `butler_volmer_current`
  - `diffusion_limited_current_density`
  - `classify_regime`, `select_math_path`, `orchestrate_problem`
