---
id: q05-harness-21
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [verification, tool]
answer: A
---

**Question:** You ask an agent to summarize a README. It displays a file-reading command, but no tool result appears. What should you check next?

- A. Whether the harness actually ran the file-reading tool
- B. Whether the command was phrased with enough confidence
- C. Whether the answer contains a sufficiently large word count
- D. Whether the model knows the general purpose of README files

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. You need evidence that the requested file was read before treating the summary as grounded in its contents.
- B. Not quite. More confident language does not establish that the operation was executed.
- C. Not quite. Length does not show that the agent obtained the source material.
- D. Not quite. General knowledge may help interpret a file, but it does not establish access to this particular file.

</details>
