---
id: q05-train-23
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: C
---

**Question:** You want to shape a base model into a tutor. You train it on examples pairing student questions with clear, helpful answers. Which stage does this most directly illustrate?

- A. Foundational pre-training on unlabeled text continuations
- B. Ordinary inference on a growing conversation history
- C. Supervised fine-tuning on demonstrations
- D. Reward-model training on preference comparisons

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. The examples are selected as demonstrations of helpful tutoring responses. This is further behavioral training on top of the base model.
- B. Not quite. The scenario says the model is being trained on example pairs. That is a learning process, rather than merely generating the current response.
- C. Correct. The supplied answers demonstrate the behavior the model should learn. This is different from asking people to rank several competing answers.
- D. Not quite. The scenario supplies example answers rather than rankings of alternatives. Comparisons would provide the signal used to train a reward model in the classic pipeline.

</details>
