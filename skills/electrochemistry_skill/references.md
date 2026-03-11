# References

This reference set is curated for v1 skill grounding.
Quality-control pass date: 2026-03-11.

Formatting policy used here:
- prefer `Authors. Title. Journal/Book (Year). DOI.` format
- prefer DOI resolver links (`https://doi.org/...`) when DOI exists
- keep one direct publisher URL when useful

## Foundational Textbooks

1. Bard, A. J.; Faulkner, L. R.; White, H. S. *Electrochemical Methods: Fundamentals and Applications*, 3rd Edition. Wiley (2022).  
   ISBN: 9781119334064  
   Publisher link: https://books.wiley.com/titles/9781119334064/  
   Relevance: Primary foundational source for thermodynamics, kinetics, transport, and experimental electrochemistry conventions.

2. Bockris, J. O'M.; Reddy, A. K. N.; Gamboa-Aldeco, M. *Modern Electrochemistry* (2-volume set), 2nd ed., Kluwer/Plenum.  
   QC note: DOI not used for this textbook entry in this file; stable publisher metadata can be added in v2.
   Relevance: Classical deep treatment of electrode processes, interfacial thermodynamics, and kinetics; useful for v2 model extensions.

## Review Papers

1. Chen, H.; Compton, R. G. Machine learning in fundamental electrochemistry: Recent advances and future opportunities. *Current Opinion in Electrochemistry* (2023).  
   DOI: 10.1016/j.coelec.2023.101214  
   DOI link: https://doi.org/10.1016/j.coelec.2023.101214  
   Publisher link: https://www.sciencedirect.com/science/article/pii/S2451910323000078  
   Relevance: Connects electrochemical fundamentals with ML opportunities; informs how this skill can evolve into data-driven workflows.

2. Lukacs, Z.; Kristof, T. Linear transformations of the Butler-Volmer equation. *Electrochemistry Communications* (2023).  
   DOI: 10.1016/j.elecom.2023.107556  
   DOI link: https://doi.org/10.1016/j.elecom.2023.107556  
   Publisher link: https://www.sciencedirect.com/science/article/pii/S1388248123001303  
   Relevance: Useful for robust interpretation and parameterization of BV-type relations in future kinetic modules.

## Open Educational Resources

1. LibreTexts Chemistry: Electrochemistry modules (electrochemical cells, Nernst equation).  
   Link: https://chem.libretexts.org/  
   Relevance: Open-access baseline explanations suitable for quick cross-checks and pedagogical examples.

2. IUPAC Gold Book (electrochemistry terminology entries).  
   Link: https://goldbook.iupac.org/  
   Relevance: Terminology normalization source for glossary definitions and symbol consistency.

## Recent AI / Computational Chemistry / Electrochemistry Workflow Papers

1. Pham, T. D.; Tanikanti, A.; Keceli, M. ChemGraph as an agentic framework for computational chemistry workflows. *Communications Chemistry* (2026).  
   DOI: 10.1038/s42004-025-01776-9  
   DOI link: https://doi.org/10.1038/s42004-025-01776-9  
   Publisher link: https://www.nature.com/articles/s42004-025-01776-9  
   Relevance: Architecture-level reference for agent-based chemistry workflow orchestration.

2. Jacobs, P. F.; Pollice, R. Developing large language models for quantum chemistry simulation input generation. *Digital Discovery* (2025).  
   DOI: 10.1039/D4DD00366G  
   DOI link: https://doi.org/10.1039/D4DD00366G  
   Publisher link: https://pubs.rsc.org/en/content/articlelanding/2025/dd/d4dd00366g  
   Relevance: Demonstrates LLM-to-formal-input translation patterns aligned with Chem2Math goals.

3. Li, T.; Zhang, C.; Li, X. Machine learning for flow batteries: opportunities and challenges. *Chemical Science* (2022).  
   DOI: 10.1039/D2SC00291D  
   DOI link: https://doi.org/10.1039/D2SC00291D  
   Publisher link: https://pubs.rsc.org/en/content/articlehtml/2022/sc/d2sc00291d  
   Relevance: Domain application showing where electrochemical modeling and ML integration intersect in energy systems.

## QC Notes
- Corrected malformed flow-battery URL in prior version (`sciencedirect.com/org/...`) to official RSC article link.
- Normalized ChemGraph year to 2026 based on article publication metadata.
- Added DOI links for machine-resolvable citation stability.

## How These References Map to This Skill
- `principles.md`, `equations.md`, `derivations.md`: primarily grounded in Bard-Faulkner-White and standard electrochemical thermodynamics/kinetics texts.
- `failure_modes.md`: built from recurring modeling errors discussed across textbook and applied electrochemistry literature.
- `reasoning_protocol.md` and `code_mapping.md`: informed by workflow papers and reproducible computational practice patterns.
