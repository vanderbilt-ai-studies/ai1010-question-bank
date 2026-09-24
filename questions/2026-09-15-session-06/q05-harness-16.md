---
id: q05-harness-16
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [alignment, permissions-and-safety]
answer: D
---

**Question:** Why is a well-aligned answer insufficient evidence for granting unrestricted tool access?

- A. One good answer establishes reliable choices on later tasks
- B. A helpful explanation establishes that broad access is needed
- C. Aligned responses make tool results reliable without inspection
- D. Good behavior does not establish the need for broad access

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. A useful response does not demonstrate how the model will behave in every later context. Access still needs to fit the task.
- B. Not quite. Helpfulness describes a response. It does not show that the requested work requires unrestricted tools or resources.
- C. Not quite. Behavioral training does not remove the need to inspect whether an operation and its result satisfy the task.
- D. Correct. Alignment addresses the model's choices, while permissions constrain executable actions. A good answer does not establish that unrestricted authority is appropriate.

</details>
