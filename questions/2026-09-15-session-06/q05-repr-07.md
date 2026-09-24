---
id: q05-repr-07
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [probability-distribution-over-tokens, transformer-pipeline]
answer: C
---

**Question:** What is the role of the output projection described in the notes?

- A. It executes a tool request through its permissions
- B. It changes learned weights using the current prompt
- C. It maps the final representation to token scores
- D. It retrieves an initial embedding from a token ID

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Tool execution belongs to the surrounding harness and tools. Output projection produces token scores inside the model.
- B. Not quite. Producing token scores is part of inference. It does not itself train new weights on the prompt.
- C. Correct. After the blocks transform representations, the output stage produces scores for possible next tokens. A token can then be selected.
- D. Not quite. Initial lookup happens before the transformer blocks. Output projection acts on the representation after processing.

</details>
