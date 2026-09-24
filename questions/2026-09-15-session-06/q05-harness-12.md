---
id: q05-harness-12
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tool, verification]
answer: D
---

**Question:** Why does writing a command in chat fail to prove that the command ran?

- A. Displaying valid syntax is enough to establish execution
- B. A relevant skill automatically executes its written steps
- C. A detailed description counts as the operation's result
- D. Command text still needs an executor

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. A syntactically valid command still needs an executor. Its appearance in chat does not establish that it ran.
- B. Not quite. A skill can guide a procedure but does not itself provide a tool or permission to perform the action.
- C. Not quite. Describing the intended work is different from receiving an observation produced by performing it.
- D. Correct. The model can produce a textual command without running it. A tool or other executor must carry out the operation.

</details>
