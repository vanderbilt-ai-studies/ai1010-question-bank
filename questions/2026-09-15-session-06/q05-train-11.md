---
id: q05-train-11
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [training-vs-inference, activation-space]
answer: C
---

**Question:** Why can a model produce different responses to different inputs while its learned weights remain fixed?

- A. Its weights and intermediate representations refer to the same numbers
- B. The new input acts as a human preference comparison during training
- C. Its intermediate representations depend on the input being processed
- D. Each new input supplies an error signal that updates learned parameters

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. The notes distinguish learned weights from the representations produced during processing. Confusing them makes an ordinary inference change look like training.
- B. Not quite. Receiving input is not the same as training on human comparisons. An ordinary response can change through input-dependent processing without a learning update.
- C. Correct. Inference uses existing weights while processing the current input. Changing representations are different from changes to the weights themselves.
- D. Not quite. This confuses ordinary input-dependent processing with training. Training uses a learning process to update parameters; a new input alone does not establish such an update.

</details>
