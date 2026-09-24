---
id: q05-repr-23
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [parameter, model-size]
answer: C
---

**Question:** You see two model implementations with similar processing steps, but one uses much larger parameter arrays. What conclusion is supported?

- A. Larger parameter arrays must contain more hand-written answer rules
- B. Larger parameter arrays make context unnecessary for interpretation
- C. Similar operations can work with very different learned models
- D. Similar processing steps require the same parameter values

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Parameters are learned numerical values. Their larger size does not mean programmers wrote a separate rule for every possible answer.
- B. Not quite. Context still influences representations through attention. Parameter size does not remove the value of relevant task information.
- C. Correct. The notes separate the broad algorithm from parameter size and values. Similar processing steps do not make the models identical.
- D. Not quite. The algorithm specifies operations, while training determines many values. Matching broad steps does not establish identical learned numbers.

</details>
