---
id: q05-repr-10
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [parameter, training-vs-inference]
answer: B
---

**Question:** What determines many of the values stored in a model's parameter arrays?

- A. The written explanation produced after an answer
- B. The learning process during training
- C. The conversation added during ordinary inference
- D. The file permissions of the agent harness

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. An explanation is generated output. Parameter values are learned during training, not established by that explanation.
- B. Correct. Training determines learned parameter values. The program specifies how operations use those arrays.
- C. Not quite. Conversation context can change current representations. Ordinary inference does not use that growing context to update the learned weights.
- D. Not quite. Permissions constrain external actions. They do not determine the model's learned numerical parameters.

</details>
