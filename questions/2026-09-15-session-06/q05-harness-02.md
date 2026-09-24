---
id: q05-harness-02
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [harness, tool]
answer: B
---

**Question:** In the lecture's README example, what does the model produce before any file is read?

- A. An updated version of its learned weights
- B. A request describing a file-reading action
- C. The verified contents of the requested file
- D. A permission change for the working folder

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Producing a tool request is part of inference. Reading a file does not require retraining the model.
- B. Correct. The model proposes the action. A tool still needs to carry it out through the harness.
- C. Not quite. The contents become available after a successful file-reading operation. A request does not supply that evidence.
- D. Not quite. Writing a request does not grant access. The harness handles the request within the permissions available.

</details>
