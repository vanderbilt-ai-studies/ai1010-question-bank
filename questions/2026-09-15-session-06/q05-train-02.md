---
id: q05-train-02
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [training-vs-inference, parameter]
answer: B
---

**Question:** Which change characterizes model training?

- A. Transforming representations for the current input
- B. Updating learned parameter values
- C. Extending the current conversation history
- D. Producing the next response for the user

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Intermediate representations change as a model processes input during inference too. Training is distinguished by updates to learned parameters.
- B. Correct. Training uses a learning objective and updates parameters. These weight changes distinguish it from an ordinary forward run.
- C. Not quite. A conversation can grow during inference. More history is not by itself evidence that the model weights changed.
- D. Not quite. Producing a response is an inference activity. Training additionally uses a learning process to change parameters.

</details>
