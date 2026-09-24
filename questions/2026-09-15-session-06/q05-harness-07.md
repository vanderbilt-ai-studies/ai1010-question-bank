---
id: q05-harness-07
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [harness, tool]
answer: C
---

**Question:** Which sequence describes the agent loop after the model requests an action?

- A. Tool acts, harness checks, observation returns
- B. Harness checks, model guesses, tool result is omitted
- C. Harness checks, tool acts, observation returns
- D. Model reports success, tool acts, harness checks

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. This puts execution before the permission check. The harness must check and route a request before the allowed tool operation.
- B. Not quite. Checking a request does not supply its outcome. The tool must execute, and its observation returns to the model.
- C. Correct. The harness checks and routes the request. The resulting observation informs the model's next decision.
- D. Not quite. A success statement does not establish execution. The request must pass through the harness before the allowed operation runs.

</details>
