---
id: q05-train-14
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [pre-training, post-training]
answer: B
---

**Question:** Why might a base model continue a request as part of a document instead of answering helpfully?

- A. A base model has already optimized each reply for a user preference score
- B. Its objective teaches continuation, not reliable assistance
- C. Its foundational objective teaches refusal instead of language prediction
- D. A base model lacks learned patterns needed to produce connected text

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Optimizing with a reward signal is part of a classic post-training pipeline. It does not describe a base model after foundational prediction training.
- B. Correct. Predicting what text comes next can support document continuation. Further training helps shape reliable assistant-style responses.
- C. Not quite. Refusal of harmful requests is an example of preferred behavior encouraged later. The foundational text-model objective is prediction.
- D. Not quite. Pre-training can build extensive language patterns. The issue is the style and purpose of the continuation, not an absence of language learning.

</details>
