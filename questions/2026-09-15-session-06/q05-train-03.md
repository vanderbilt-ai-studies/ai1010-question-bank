---
id: q05-train-03
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [pre-training, self-supervised-learning]
answer: C
---

**Question:** In next-token pre-training, where does the prediction target come from?

- A. A person who ranks several assistant replies
- B. The reply preferred by a trained reward model
- C. The next token already found in the text
- D. A person who labels each possible continuation

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Ranking replies is a preference-feedback example from post-training. Next-token pre-training obtains its target from the training text.
- B. Not quite. A reward model can supply a signal in a classic human-feedback pipeline. The next-token target instead comes directly from the text.
- C. Correct. The text supplies both the preceding context and the token that follows it. This provides a learning target without hand-labeling every continuation.
- D. Not quite. People need not label each continuation in this example. The next token in the existing text supplies the target.

</details>
