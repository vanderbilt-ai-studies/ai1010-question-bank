---
id: q05-repr-24
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [learned-knowledge, parameter]
answer: D
---

**Question:** A teammate wants to stop a model inventing a detail in future responses and says, "Find the line that tells it to invent that detail, then delete it." What is the best explanation of why this code search may fail?

- A. That detail must be stored in the vocabulary ID for its main word
- B. That detail shows the model rewrote its program during the reply
- C. Deleting the detail from this answer also changes the learned behavior
- D. The detail may emerge from learned values and context

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. Vocabulary IDs identify tokens. They do not each store an instruction to make a particular claim.
- B. Not quite. An unwanted output does not establish that the program changed. Ordinary inference runs computation using existing weights and current context.
- C. Not quite. Editing visible output repairs that artifact. It does not establish that the underlying parameters or behavior in future responses have changed.
- D. Correct. The notes explain why a specific answer need not have a corresponding hand-written rule. You can inspect the software without assuming that one line controls that behavior.

</details>
