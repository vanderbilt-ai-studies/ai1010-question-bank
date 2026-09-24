---
id: q05-train-19
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [alignment]
answer: C
---

**Question:** Why does training a model to refuse a harmful request leave behavioral reliability as an ongoing concern?

- A. A refusal during training guarantees matching responses during deployment
- B. A refusal shows that learned parameters no longer influence model behavior
- C. A favored response in training may not hold under unfamiliar framing
- D. A refusal changes external permissions each time the model generates it

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. This treats an encouraged behavior as an inviolable rule. The notes explicitly distinguish improved behavior from a guarantee across contexts.
- B. Not quite. Refusals can be shaped through post-training, which affects the model. They do not indicate that learned weights have stopped influencing responses.
- C. Correct. Post-training can encourage a refusal, but that response is not an unbreakable rule for every context. Reliability must extend beyond the situations represented in training.
- D. Not quite. This confuses the model choosing a response with external enforcement. Training encourages behavior; harness permissions separately constrain which actions can execute.

</details>
