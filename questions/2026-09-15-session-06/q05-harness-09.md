---
id: q05-harness-09
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [agent, harness]
answer: A
---

**Question:** What is the model's role in the agent system described in the lecture?

- A. Interpreting context and proposing next steps
- B. Authorizing access to the project's resources
- C. Executing the requested external file operations
- D. Supplying the connection to an external service

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. The model contributes language understanding and decisions. The harness routes its proposed actions, and tools execute permitted operations.
- B. Not quite. Permission checks belong to the surrounding controls. The model's judgment that access would help does not grant it.
- C. Not quite. The model proposes operations. Tools carry out those external actions when the harness allows and routes them.
- D. Not quite. A connector exposes an integration with a service or resource. The model can use available capabilities as it decides what to do.

</details>
