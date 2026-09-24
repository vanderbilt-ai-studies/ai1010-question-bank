---
id: q05-train-25
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [alignment]
answer: A
---

**Question:** A model trained to favor refusals of harmful requests usually declines them, but a misleadingly framed version receives a harmful answer. Which conclusion best follows from the notes?

- A. Training has encouraged a behavior that remains unreliable in some contexts
- B. The initial refusals prove the later answer must be harmless in effect
- C. The changed wording proves that the model updated its weights during the request
- D. The later answer proves that post-training cannot influence model behavior

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. A preferred refusal can be learned without becoming an inviolable rule. The changed framing exposes a limit in behavioral reliability.
- B. Not quite. Earlier refusals do not establish the safety of a different response. The notes emphasize that behavior may change with framing.
- C. Not quite. Different inputs can lead to different outputs using existing weights. A behavioral change under new framing is not evidence of a training update.
- D. Not quite. An imperfect result does not show that training has no influence. Post-training can encourage preferred responses while leaving reliability gaps.

</details>
