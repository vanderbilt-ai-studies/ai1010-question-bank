---
id: q05-harness-04
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tool, context]
answer: D
---

**Question:** Where does a successful tool result go so the model can use it?

- A. Into the vocabulary as a newly defined token
- B. Into the weights as an immediate training update
- C. Into the skill as an automatic procedure revision
- D. Into the context used for the next decision

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. A tool result supplies task information. It does not require a vocabulary entry for the entire observation.
- B. Not quite. A model can use the returned evidence during inference without updating its learned parameters.
- C. Not quite. A tool observation is information for the task. Revising reusable instructions is a separate action, not an automatic consequence of receiving a result.
- D. Correct. The result becomes an observation the model can use when deciding its next step.

</details>
