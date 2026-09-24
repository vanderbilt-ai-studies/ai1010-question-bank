---
id: q05-repr-08
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [parameter, learned-knowledge]
answer: D
---

**Question:** What do the learned parameter arrays contain?

- A. Written definitions for each vocabulary entry
- B. Complete conversations from earlier model runs
- C. Hand-written instructions for particular answers
- D. Numerical values determined through training

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. A token ID selects a numerical representation. The model does not represent its learned parameters as dictionary definitions.
- B. Not quite. A conversation supplies context for a run. Learned parameter arrays instead contain numbers determined through training.
- C. Not quite. The program specifies operations, but a particular learned answer need not have a matching written rule.
- D. Correct. Training determines many values stored in parameter arrays. The model program specifies operations that use those learned numbers.

</details>
