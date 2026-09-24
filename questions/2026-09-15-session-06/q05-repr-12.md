---
id: q05-repr-12
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [attention, activation-space]
answer: D
---

**Question:** Why can the phrase about a cruel trainer angering a cat change how you interpret cat?

- A. The vocabulary needs a new entry for an angry cat
- B. The prompt immediately retrains the model's parameters
- C. The model has already selected the final answer word
- D. The surrounding words shape the representation

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. A token's representation can shift with context while its vocabulary ID stays the same. A separate entry is not needed for each interpretation.
- B. Not quite. Using the sentence as context can change its interpretation during inference. That is different from updating weights through training.
- C. Not quite. The example concerns how representations develop inside the blocks. Token selection happens after those transformations.
- D. Correct. Attention brings relevant context into the token's representation. The trainer and anger context can make a large, angry animal more plausible.

</details>
