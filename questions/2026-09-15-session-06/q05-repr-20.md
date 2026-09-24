---
id: q05-repr-20
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [context, context-length, grounding]
answer: D
---

**Question:** Why does a large context capacity still require you to choose useful material?

- A. Capacity determines which prompt facts become permanent weights
- B. Capacity makes each document a verified source of factual truth
- C. Capacity selects the next token before representations change
- D. Capacity holds material; useful evidence helps the task

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. Context capacity concerns what can be supplied for a run. It does not determine permanent learning of prompt facts during ordinary inference.
- B. Not quite. The ability to include a document does not verify its content or the answer. You still need relevant evidence and inspection of its use.
- C. Not quite. Context capacity is not the token-selection step. Representations are still processed through the model before output scoring.
- D. Correct. A large context can hold more material, but you still need information that bears on the task and must verify how the model uses it.

</details>
