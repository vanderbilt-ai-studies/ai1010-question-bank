---
id: q05-train-07
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: C
---

**Question:** In the classic reinforcement learning from human feedback pipeline, what does a reward model learn from?

- A. The current conversation without any parameter updates
- B. Example answers demonstrating desired assistant responses
- C. Human comparisons of alternative outputs
- D. Human selection of the next token in every training sentence

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Using a conversation to generate a response is ordinary inference. The reward model is trained using human comparisons.
- B. Not quite. Demonstrations show desired responses for supervised fine-tuning. The reward model in the classic pipeline instead learns from comparisons of alternative outputs.
- C. Correct. People compare outputs, and the reward model learns from those comparisons. Its learned signal is then used to optimize the assistant.
- D. Not quite. Hand-labeling every next token is not the described source of preference feedback. People compare outputs in the classic pipeline.

</details>
