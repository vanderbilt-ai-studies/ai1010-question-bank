---
id: q05-repr-04
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [attention]
answer: D
---

**Question:** What role does attention play in interpreting a token?

- A. It chooses the displayed token before any blocks run
- B. It replaces the vocabulary index with a new index
- C. It saves the conversation by updating model weights
- D. It incorporates relevant information from context

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. Next-token selection occurs near the end of the model's processing. Attention works on representations inside the blocks.
- B. Not quite. The representation changes during attention. That change is not a reassignment of the token's vocabulary ID.
- C. Not quite. Using context during ordinary inference changes current representations, not the learned weights.
- D. Correct. Attention lets the token's representation draw on surrounding information. This can shift its interpretation as more relevant context is considered.

</details>
