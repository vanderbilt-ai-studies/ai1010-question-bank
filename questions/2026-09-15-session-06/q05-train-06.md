---
id: q05-train-06
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: B
---

**Question:** What is the role of example responses in supervised fine-tuning?

- A. They measure how often a response appears in the original text
- B. They demonstrate the responses the model should learn to produce
- C. They provide pairs of replies for people to rank by preference
- D. They supply a fixed conversation for an inference run to complete

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. The notes describe desired-answer demonstrations, not counting occurrences in pre-training text. Fine-tuning learns from those examples of behavior.
- B. Correct. Supervised fine-tuning trains on demonstrations of desired responses. This shapes behavior beyond foundational next-token pre-training.
- C. Not quite. Ranking alternatives supplies preference information. Demonstrations instead show the desired response itself.
- D. Not quite. Examples can be placed in context, but supervised fine-tuning uses them for training. That process changes learned parameters.

</details>
