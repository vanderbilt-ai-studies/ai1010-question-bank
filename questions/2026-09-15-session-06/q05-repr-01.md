---
id: q05-repr-01
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tokenization, token]
answer: A
---

**Question:** What does a token ID identify?

- A. An entry in the model's vocabulary
- B. A coordinate describing the token's meaning
- C. A weight changed during the current response
- D. A score for the next possible token

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The ID selects a vocabulary entry and its starting embedding. Meaning is represented by numerical vectors, not by the ID itself.
- B. Not quite. This confuses an index with a representation. The token ID selects an embedding; it is not itself a semantic coordinate.
- C. Not quite. Weights are learned parameters. The ID identifies the token, and ordinary response generation does not update the model's weights.
- D. Not quite. Scores for possible next tokens are produced near the output. An ID identifies a vocabulary entry before that scoring step.

</details>
