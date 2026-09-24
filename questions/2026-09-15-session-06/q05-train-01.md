---
id: q05-train-01
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [training-vs-inference]
answer: A
---

**Question:** What does ordinary inference do?

- A. Uses existing weights to generate an output
- B. Adjusts learned weights using prediction errors
- C. Fits a reward model to human comparisons
- D. Learns desired answers from demonstrations

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. Inference runs the trained model forward. Its current representations can change without updating its learned weights.
- B. Not quite. Adjusting parameters from a learning objective belongs to training. Generating the current answer ordinarily uses weights that have already been learned.
- C. Not quite. A reward model can be trained from preferences during post-training. That is a learning stage, rather than ordinary generation.
- D. Not quite. Learning from example responses describes supervised fine-tuning. Inference uses the resulting trained model.

</details>
