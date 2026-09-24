---
id: q05-train-17
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: A
---

**Question:** Why are reward-model training and assistant optimization separate stages in the classic human-feedback pipeline?

- A. One learns a preference signal; the other trains the assistant with it
- B. One learns a preference signal; the other copies it as an example reply
- C. One learns a preference signal; the other runs the assistant without updates
- D. One learns demonstration answers; the other ranks responses with people

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The reward model first learns a signal from human comparisons. Reinforcement learning then uses that signal to optimize the assistant.
- B. Not quite. A learned reward is a signal for optimization, rather than a demonstration response to imitate. Example replies serve a different role in supervised fine-tuning.
- C. Not quite. Running the assistant with unchanged weights describes inference. In the training pipeline, the learned reward signal guides further optimization of the assistant.
- D. Not quite. Demonstrations and human comparisons are inputs to different training stages. The question concerns learning a reward signal from comparisons and then using it to train the assistant.

</details>
