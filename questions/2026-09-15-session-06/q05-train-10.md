---
id: q05-train-10
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training, pre-training]
answer: B
---

**Question:** What does post-training build on?

- A. A reward model that has replaced foundational language training
- B. A base model that has already undergone foundational training
- C. A conversation history that has replaced the learned parameters
- D. A collection of preferred responses used without a trained model

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. A reward model can guide a later learning stage. It does not replace the base model and its foundational training.
- B. Correct. Post-training starts from a base model and further shapes its behavior and capabilities. Demonstrations and preferences can supply learning signals.
- C. Not quite. Conversation history is context, not a replacement for weights. Post-training updates a previously trained model.
- D. Not quite. Preferred responses can provide training information, but the process builds on a base model. The examples do not substitute for the model itself.

</details>
