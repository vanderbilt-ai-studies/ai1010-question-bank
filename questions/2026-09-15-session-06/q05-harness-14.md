---
id: q05-harness-14
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [agent-skill, tool, permissions-and-safety]
answer: B
---

**Question:** Why does adding a procedure to a skill fail to guarantee that its steps can run?

- A. The model must discover the procedure in its pre-training data
- B. The system also needs the required tools and permissions
- C. A skill must replace the harness before it can be useful
- D. A skill must be converted into learned parameters first

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. The procedure can be loaded from the skill into context. It need not have appeared during pre-training.
- B. Correct. The procedure explains what to do. Actual execution depends on capabilities and access supplied by the surrounding system.
- C. Not quite. Skills guide the agent within its environment. They need not replace the software that runs tools.
- D. Not quite. The course uses skills as instructions and resources during a run, without retraining the model.

</details>
