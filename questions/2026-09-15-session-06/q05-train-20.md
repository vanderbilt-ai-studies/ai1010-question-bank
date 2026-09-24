---
id: q05-train-20
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [training-vs-inference, data-privacy]
answer: D
---

**Question:** Why is possible future use of a conversation for training different from learning during the current response?

- A. Saving a conversation for future use performs a current parameter update
- B. Processing a conversation with fixed weights rules out later training use
- C. Adding a conversation to context is the same learning process as later training
- D. Updating parameters later is separate from generating the current response

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. Data retention and parameter updates are different events. Saving information does not establish that the current response is updating weights.
- B. Not quite. Current inference does not establish a provider's future data-use policy. The notes say later collection and training depend on the service and settings.
- C. Not quite. Context and intermediate representations can change during inference. Training adds a separate learning process that updates learned parameters.
- D. Correct. A provider may separately collect data for future training. Ordinary inference can use existing weights even if a later training process occurs.

</details>
