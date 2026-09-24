---
id: q05-harness-05
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [harness, permissions-and-safety]
answer: A
---

**Question:** What happens when the harness blocks a proposed tool operation?

- A. The external action remains unperformed
- B. The model becomes unable to explain the result
- C. The action runs when the model explains its value
- D. The skill supplies permission for the blocked step

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The harness can return a blocked status while the model continues generating text. The requested operation has not run.
- B. Not quite. Blocking an external action does not prevent the model from generating a textual explanation of the denial.
- C. Not quite. A persuasive explanation is still text. It does not supply the permission needed to execute the denied operation.
- D. Not quite. A skill describes what to do. It cannot grant access denied by the surrounding controls.

</details>
