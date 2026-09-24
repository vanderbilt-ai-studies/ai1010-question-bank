---
id: q05-harness-19
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [permissions-and-safety]
answer: C
---

**Question:** Why is the label "sandbox" insufficient evidence that a deployment is safe?

- A. The label establishes that every file operation is blocked
- B. The label establishes that generated statements are accurate
- C. Its controls still need implementation and testing
- D. The label establishes that broader access is appropriate

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. The name alone does not establish which actions the actual controls restrict. Their implementation and behavior must be checked.
- B. Not quite. Access controls address executable actions. They do not guarantee that every written claim is true.
- C. Correct. Calling an environment a sandbox does not establish that its intended restrictions exist or work. Inspect and test the actual controls.
- D. Not quite. A label does not determine the authority needed for a task. The tools and working area should be chosen deliberately.

</details>
