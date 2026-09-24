---
id: q05-harness-22
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [permissions-and-safety, verification]
answer: B
---

**Question:** An agent can read your project but lacks permission to modify it. It proposes a useful edit. What follows?

- A. The read permission also permits the proposed modification
- B. The suggestion does not change the project file
- C. The value of the edit supplies the missing permission
- D. The skill can write the edit using its instructions

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Reading and changing files require the relevant access. The scenario explicitly says the agent lacks permission to modify the project.
- B. Correct. A model can describe a useful edit without executing it. Reading access and a proposal do not establish a completed modification.
- C. Not quite. A model's judgment that an action is useful does not grant write access. The surrounding controls determine permitted execution.
- D. Not quite. The skill can guide an editing procedure. Its instructions do not perform the file operation or supply the missing write permission.

</details>
