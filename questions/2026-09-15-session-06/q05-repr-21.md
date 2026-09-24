---
id: q05-repr-21
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [grounding, context]
answer: A
---

**Question:** You need an answer based on a policy document the model has not been given. Which step best follows the lecture's advice?

- A. Supply the relevant text or a way to retrieve it
- B. Ask the model to reconstruct it from similar policies
- C. Provide its filename and assume that supplies its contents
- D. Request a detailed answer before checking the source

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The task depends on evidence from this document. Put the relevant material in context or provide access so the model can use it with existing weights.
- B. Not quite. Learned associations can suggest plausible contents without establishing what this particular document says.
- C. Not quite. Naming a source identifies the material you want. Its relevant contents still need to enter context or be available through retrieval.
- D. Not quite. More detail does not supply the missing evidence. Source access should support the answer, followed by checking how the evidence was used.

</details>
