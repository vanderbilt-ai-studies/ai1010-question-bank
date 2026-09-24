---
id: q05-repr-11
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tokenization, token-embedding, semantic-space]
answer: C
---

**Question:** Why should you avoid treating a token ID as the token's meaning?

- A. It changes into a written definition when attention runs
- B. It is learned again whenever the token enters a prompt
- C. It indexes an entry with a numerical representation
- D. It contains the final representation after all blocks run

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Attention transforms numerical representations. It does not turn the index into dictionary text.
- B. Not quite. Processing a prompt uses the token ID to select a representation. Ordinary inference does not relearn the model's weights on every token.
- C. Correct. The index performs a lookup role. The selected numerical representation, and its later transformations, support interpretation.
- D. Not quite. The ID is used at the start to select an embedding. It is not the final result of the model's processing.

</details>
