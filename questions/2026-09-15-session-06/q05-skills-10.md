---
id: q05-skills-10
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [agent-skill, training-vs-inference]
answer: B
---

**Question:** Why can revising a skill change the agent's later work without training a new model?

- A. The revision replaces a set of learned model weights
- B. The revision changes guidance used during the work
- C. The revision turns previous reports into model parameters
- D. The revision makes the file location the task objective

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. This describes a change to the model rather than a change to its reusable guidance. Editing a skill ordinarily leaves the model weights unchanged.
- B. Correct. A skill supplies reusable instructions and resources. Changing that package can guide later runs without changing the underlying learned parameters.
- C. Not quite. Reports are artifacts you can inspect or package. Editing the skill does not convert those files into trained model weights.
- D. Not quite. The working location helps identify relevant materials. The procedure's instructions and the intended task still determine what the agent should do.

</details>
