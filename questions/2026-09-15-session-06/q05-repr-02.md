---
id: q05-repr-02
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [token-embedding]
answer: B
---

**Question:** What is an embedding in the model described in the notes?

- A. A vocabulary number serving as an index
- B. A numerical vector representing a token
- C. A written definition retrieved for a token
- D. A numerical score for a possible next token

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. The vocabulary index is the token ID. It selects an initial embedding, which is a vector rather than just that index.
- B. Correct. An embedding supplies a numerical representation. That representation can then be transformed as the token passes through the model.
- C. Not quite. The model processes numerical representations rather than retrieving a dictionary definition as the embedding.
- D. Not quite. Scores are produced near the output to support next-token selection. The embedding is the numerical representation processed before that output stage.

</details>
