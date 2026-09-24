---
id: q05-train-24
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: D
---

**Question:** People compare two explanations of photosynthesis and prefer the one suited to a young learner. What information does this comparison provide for post-training?

- A. A guarantee that the model will explain every topic appropriately
- B. The next token that originally followed a passage in the training text
- C. Evidence that the current comparison has already updated the assistant weights
- D. A preference about which response better fits the intended audience

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. One preferred response provides useful training information, not a guarantee across topics and contexts. Behavioral reliability still needs attention.
- B. Not quite. That would be a self-supervised prediction target. This comparison instead expresses a judgment about alternative responses.
- C. Not quite. A human judgment can supply information for training. The judgment alone does not demonstrate that the subsequent training update has occurred.
- D. Correct. The comparison identifies a response that better serves the task. Preferences can guide behavioral training, including reward-model learning in the classic pipeline.

</details>
