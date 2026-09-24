---
id: q05-train-13
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [hallucination, pre-training]
answer: A
---

**Question:** Why can strong next-token prediction coexist with inaccurate claims?

- A. Learning likely text does not verify its associations
- B. Prediction quality measures how many claims humans have verified
- C. Inaccurate claims indicate that inference must have changed the weights
- D. Extensive training removes language patterns and keeps verified facts

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. Prediction can build useful language and world patterns. The objective does not turn every association learned from text into a true statement.
- B. Not quite. The described prediction objective concerns the next token, not a count of fact-checked claims. Good prediction is therefore not a truth guarantee.
- C. Not quite. An inaccurate output can arise while using existing weights. Weight updates are not needed for a model to generate a mistaken claim.
- D. Not quite. Pre-training learns patterns and associations from extensive text. The notes do not describe a filtering process that leaves a store of verified facts.

</details>
