---
id: q05-harness-18
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [agent, tool, context]
answer: B
---

**Question:** Why can two agents using the same model perform differently on the same task?

- A. The same model requires the same tools in each environment
- B. Their tools, context, and procedures may differ
- C. The same model brings its folder permissions to each environment
- D. The same model guarantees the same evidence enters each context

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Tools belong to the surrounding system. Two agents can expose different actions while using the same underlying model.
- B. Correct. The model is one component of the agent. Its surroundings affect the information and actions available for the task.
- C. Not quite. File permissions are supplied by the environment. They are not a capability the model carries into every deployment.
- D. Not quite. An agent needs access to relevant evidence. Different tools and working contexts can provide different information to the same model.

</details>
