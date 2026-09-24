---
id: q05-repr-17
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [learned-knowledge, parameter]
answer: A
---

**Question:** Why might an unwanted model answer have no single hand-written rule you can edit?

- A. Learned values interact with the current context
- B. Training stores a separate source-code rule for each answer
- C. Understanding the program identifies each answer's cause directly
- D. The written explanation supplies the rule that generated the answer

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The program specifies computation, while learned parameter values help determine behavior. A particular answer need not correspond to a single written rule.
- B. Not quite. Training updates numerical parameters. It does not establish that each resulting answer has a separate hand-written rule.
- C. Not quite. You can inspect the software, but the algorithm alone does not explain every behavior arising from learned parameters and context.
- D. Not quite. An explanation is generated output. It does not establish that the model has a matching hand-written source-code rule for the answer.

</details>
