---
id: q05-harness-11
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [tool, permissions-and-safety]
answer: C
---

**Question:** Why can a powerful model still fail to read a local file?

- A. Its training must have included that exact file
- B. Its skill must copy the file into permanent weights
- C. Its environment may lack the necessary access
- D. Its prompt must phrase the read as a confident command

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. A file-reading tool can supply current contents to context. The file need not have been present in the model's training data.
- B. Not quite. The file can be read into current context. A skill supplies guidance without permanently teaching the file through weight updates.
- C. Correct. The model's capability cannot replace an unavailable tool or missing permission for the file.
- D. Not quite. A clearer request can describe what you want, but wording cannot create a missing tool or grant file access.

</details>
