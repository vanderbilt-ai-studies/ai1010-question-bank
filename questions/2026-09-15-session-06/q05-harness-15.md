---
id: q05-harness-15
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tool, context]
answer: C
---

**Question:** Why should a file operation return its result to the model?

- A. The returned text serves as proof that the full task is finished
- B. The result grants permission for the next requested operation
- C. The next decision should reflect the actual outcome
- D. The returned text permanently revises the model's knowledge

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. A tool result reports one operation. The model may need further steps, and the final work still needs checking against the task.
- B. Not quite. An observation supplies information. Permission for another action remains a matter for the surrounding controls.
- C. Correct. The observation lets the model adapt its next step to what happened rather than continue from an unverified expectation.
- D. Not quite. The model can use a tool result in its current context. This is different from changing learned weights through training.

</details>
