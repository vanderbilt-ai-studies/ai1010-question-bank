---
id: q05-train-08
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: D
---

**Question:** What follows reward-model training in the classic reinforcement learning from human feedback pipeline?

- A. Training the reward model again on example assistant responses
- B. Training the assistant to predict the next tokens in raw text
- C. Training the assistant to copy reward scores as desired replies
- D. Training the assistant using the learned reward signal

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. Example assistant responses provide demonstrations for supervised fine-tuning. After learning a reward signal from comparisons, the described pipeline uses that signal to optimize the assistant.
- B. Not quite. This is the foundational text-model training example. The stage after reward-model learning instead uses the learned preference signal for further assistant optimization.
- C. Not quite. This confuses an evaluation signal with a demonstration answer. A reward signal guides optimization; it is not the response the assistant is being taught to produce.
- D. Correct. The reward model learns from human comparisons, and reinforcement learning uses that signal to optimize the assistant. These are distinct stages.

</details>
