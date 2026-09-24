---
id: q05-skills-02
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [skill-structure]
answer: B
---

**Question:** Which file should you ask the agent to locate when you want to inspect a skill's main instructions?

- A. The newest output report
- B. The skill's SKILL.md file
- C. The current conversation export
- D. The model's parameter file

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. A report shows what a run produced. To inspect the procedure that guided the run, ask for the skill's instruction file.
- B. Correct. SKILL.md contains the skill's instructions. Open it and inspect the supporting files to understand the procedure you are using.
- C. Not quite. The conversation can describe a run, but the notes direct you to inspect the reusable instructions themselves in SKILL.md.
- D. Not quite. Parameters belong to the trained model. Editing a skill means inspecting its instructions, rather than inspecting learned model numbers.

</details>
