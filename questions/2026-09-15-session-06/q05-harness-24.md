---
id: q05-harness-24
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tool, verification]
answer: D
---

**Question:** A file-reading tool returns "file not found." What information should guide the agent's next step?

- A. An assumed summary of what the file probably contains
- B. The model's confidence before the request was made
- C. An automatic increase in permissions for every folder
- D. The observed failure and the task's intended source

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. An expectation about contents is not evidence that the missing file was read.
- B. Not quite. The actual tool outcome is more relevant than the earlier expectation of success.
- C. Not quite. A missing file does not justify blanket access. The next action should fit the task and available controls.
- D. Correct. The returned observation should shape the next decision. The agent should not act as though the requested contents were received.

</details>
