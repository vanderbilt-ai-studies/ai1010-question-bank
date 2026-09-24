---
id: q05-harness-08
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [connector]
answer: D
---

**Question:** What does a connector contribute to an agent system?

- A. A replacement for the model's learned parameters
- B. A preferred answer learned during post-training
- C. A self-contained set of grading criteria
- D. An integration with a service or resource

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. An integration gives access to a resource; it does not replace the numerical parameters of the model.
- B. Not quite. Post-training shapes behavior. A connector supplies a route to an external service or resource.
- C. Not quite. Criteria belong in the task or reusable instructions. A connector provides an integration rather than those criteria.
- D. Correct. A connector exposes an integration that an agent can use when the surrounding system permits it.

</details>
