---
id: q05-harness-17
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [permissions-and-safety, verification]
answer: A
---

**Question:** Why do access controls fail to guarantee that a model's written answer is accurate?

- A. They constrain actions without checking each claim
- B. They make permitted sources automatically trustworthy
- C. They turn successful tool use into proof of correctness
- D. They supply missing evidence through the permission decision

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The harness can limit what the system executes while the model can still generate a mistaken statement. Output verification addresses a separate concern.
- B. Not quite. Permission to access a source is not a judgment that its content or the resulting answer is accurate.
- C. Not quite. An operation can be allowed and successfully executed while the resulting answer is incomplete or incorrect.
- D. Not quite. A permission decision determines whether an action may run. It does not itself supply the task evidence the model needs.

</details>
