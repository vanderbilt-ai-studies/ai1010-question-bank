---
id: q05-train-05
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [pre-training, post-training]
answer: A
---

**Question:** Which description best fits a base model after next-token pre-training?

- A. A model with text patterns but uncertain assistant behavior
- B. A model whose helpful conversational responses are already assured
- C. A model whose learned statements have already been checked for truth
- D. A model whose replies are selected directly by human evaluators

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. Prediction can build language patterns and world associations. It does not by itself guarantee reliable conversational helpfulness.
- B. Not quite. Prediction training provides a foundation, but it does not guarantee helpful assistant behavior. Further training can shape that behavior, while suitable patterns can also elicit answers from a base model.
- C. Not quite. Learning to predict likely text does not verify each learned claim. A base model can acquire associations without guaranteeing their accuracy.
- D. Not quite. People may provide examples or preferences during post-training. A base model produces text using its learned parameters, rather than having humans choose each reply.

</details>
