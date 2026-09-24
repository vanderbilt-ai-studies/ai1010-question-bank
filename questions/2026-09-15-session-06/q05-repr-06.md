---
id: q05-repr-06
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [activation-space, attention]
answer: B
---

**Question:** In the teaching diagram, what do cat-star and cat-star-star represent?

- A. Replacements for the model's training parameters
- B. Later representations of the same token
- C. Additional entries added to the vocabulary
- D. Separate words printed in the final answer

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Representations change as input is processed. The diagram does not show weight updates during training.
- B. Correct. The labels mark stages in processing the token. They help you picture a changing representation without implying a different vocabulary entry.
- C. Not quite. The star labels are explanatory labels for internal stages. The model does not add those labels to its vocabulary during the example.
- D. Not quite. The diagram describes internal processing. Its star labels are not successive words the model must output.

</details>
