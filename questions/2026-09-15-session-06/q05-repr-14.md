---
id: q05-repr-14
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [mlp, learned-knowledge]
answer: B
---

**Question:** Why is it misleading to describe the MLP (multi-layer perceptron) as the model's searchable fact database?

- A. It assigns vocabulary IDs instead of transforming representations
- B. Learned information is distributed across the network
- C. It operates on finished English sentences rather than numbers
- D. It stores the current prompt by retraining on every word

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Token lookup and representation transformation have different roles. The MLP participates in the latter.
- B. Correct. The MLP applies learned transformations, but knowledge is not confined to that component. A database lookup is too literal a picture of this processing.
- C. Not quite. The MLP transforms numerical representations. Treating it as an English-sentence processor adds another misleading picture.
- D. Not quite. Current context influences representations during inference. That does not mean the MLP updates its weights on each prompt word.

</details>
