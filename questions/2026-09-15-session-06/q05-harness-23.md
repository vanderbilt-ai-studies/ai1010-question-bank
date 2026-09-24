---
id: q05-harness-23
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tool, agent-skill]
answer: C
---

**Question:** Your skill says "upload the final report," but the agent has no upload tool. What is the immediate limitation?

- A. The skill's wording determines whether an upload tool exists
- B. The model's confidence determines whether an upload can run
- C. The environment lacks a required action capability
- D. The report's completeness determines whether it was uploaded

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. An instruction can name an action without providing the capability to execute it. Tools must be available in the environment.
- B. Not quite. Confidence is a feature of the response. It does not replace an unavailable upload tool.
- C. Correct. The skill gives guidance, while tools provide actions. An upload step requires a tool or integration that can carry it out.
- D. Not quite. A complete local artifact and a successful external upload are separate outcomes. The task still needs an available upload capability.

</details>
