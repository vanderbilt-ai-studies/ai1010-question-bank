---
id: q05-harness-03
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [harness, tool]
answer: C
---

**Question:** Which part of an agent system carries out an allowed file-reading operation?

- A. A reusable skill describing the procedure
- B. The trained model producing a request
- C. A file-reading tool routed by the harness
- D. The generated command displayed in chat

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. A skill supplies instructions about reading the file. It does not itself carry out the external operation.
- B. Not quite. The model can propose the action. A separate tool must actually access the file.
- C. Correct. The harness checks and routes the request; the file-reading tool performs the allowed operation.
- D. Not quite. A command can describe the intended operation while remaining text. It needs an executor before the file is read.

</details>
