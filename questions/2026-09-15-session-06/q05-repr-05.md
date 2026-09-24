---
id: q05-repr-05
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [mlp]
answer: A
---

**Question:** What does the MLP (multi-layer perceptron) contribute within a transformer block?

- A. It transforms representations using learned parameters
- B. It executes file commands outside the model
- C. It assigns a fresh vocabulary ID to each interpretation
- D. It displays a finished word after each block

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The feed-forward network applies transformations learned during training. Its contribution helps the interpretation develop through the model.
- B. Not quite. External commands require a harness and tools. The MLP is part of the model's internal numerical processing.
- C. Not quite. The MLP changes the representation of a token. Successive interpretations do not require new vocabulary entries.
- D. Not quite. Intermediate blocks transform numerical representations. Choosing a token for output happens near the end.

</details>
