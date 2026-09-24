---
id: q05-train-21
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [training-vs-inference, context]
answer: A
---

**Question:** You add a paragraph to a conversation, and the model uses it to improve an explanation. The system reports that no parameters changed. What best explains the improvement?

- A. Inference used the new context with existing learned weights
- B. Pre-training learned a new set of weights from the paragraph
- C. Supervised fine-tuning trained the model on a desired answer
- D. Reward-model training learned which explanation people prefer

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. Supplying relevant material can change performance during inference. The model can use the paragraph without changing its underlying weights.
- B. Not quite. The scenario states that parameters did not change. The improvement is explained by using relevant context, rather than a foundational learning update.
- C. Not quite. The paragraph was supplied in the conversation, and there was no weight update. That differs from training on demonstrations of desired responses.
- D. Not quite. The scenario provides contextual information, not human comparisons used to train a reward model. Better performance alone does not establish such training.

</details>
