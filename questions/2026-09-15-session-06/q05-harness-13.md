---
id: q05-harness-13
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [permissions-and-safety, verification]
answer: A
---

**Question:** Why can a denied tool request be followed by a normal-looking written answer?

- A. Text generation can continue after a denial
- B. A fluent answer establishes that the action succeeded
- C. The model performs the action internally after denial
- D. The skill supplies temporary access after the denial

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The requested external operation can remain blocked while the model generates an explanation or other textual response.
- B. Not quite. Fluency is a property of generated text. It does not prove that an external operation occurred.
- C. Not quite. The model can reason about the denied action, but generating text does not carry out the blocked external operation.
- D. Not quite. A skill's instructions do not grant a missing permission or override the surrounding access controls.

</details>
