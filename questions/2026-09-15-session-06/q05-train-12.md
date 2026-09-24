---
id: q05-train-12
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [self-supervised-learning]
answer: D
---

**Question:** Why is next-token prediction called self-supervised learning in the notes?

- A. The model can train without any target or performance objective
- B. The model certifies the factual accuracy of its own predictions
- C. A reward model supplies the target from human response rankings
- D. Existing text supplies the context and prediction target

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. Self-supervision still supplies a learning target. The distinction is that the target comes from the data rather than a separate human label for every continuation.
- B. Not quite. Self-supervision describes how targets are obtained. It does not establish the truth of the learned claims.
- C. Not quite. This describes a signal in the classic human-feedback pipeline. The next-token example is self-supervised because the existing text itself supplies the prediction target.
- D. Correct. A passage can supply a context and its next token. This creates a training example without requiring a person to label every continuation.

</details>
