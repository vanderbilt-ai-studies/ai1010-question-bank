---
id: q05-repr-19
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [attention, activation-space]
answer: C
---

**Question:** Why is literally averaging English words a misleading description of attention?

- A. Attention combines final answers after the model selects them
- B. Attention combines source-code rules written for each meaning
- C. Attention combines transformed numerical representations
- D. Attention combines written definitions retrieved from a database

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Attention operates inside the transformer blocks. It helps shape representations before next-token selection near the output.
- B. Not quite. The relevant inputs are numerical representations. There need not be a hand-written rule for each interpretation a model develops.
- C. Correct. The words help you picture the process, but the mechanism works on numerical representations. The notes describe weighted combinations of those transformed representations.
- D. Not quite. This replaces one literal word-based picture with another. The computation operates on representations, not retrieved dictionary prose.

</details>
