---
id: q05-repr-03
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [attention, mlp, decoder-stack]
answer: C
---

**Question:** What passes from attention to the feed-forward network inside a transformer block?

- A. New vocabulary entries for each token
- B. Written rules describing each token
- C. Updated numerical representations
- D. Completed sentences ready for display

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Changing a representation does not create a new vocabulary entry. The same token can have successive internal representations.
- B. Not quite. The block operates on numerical arrays using learned parameters. It does not pass a set of written meaning rules between its parts.
- C. Correct. The intermediate material is numerical. Attention and the feed-forward network transform representations before the model chooses an output token.
- D. Not quite. Sentences are the visible result of generation. Inside the block, the model is still transforming numerical representations.

</details>
