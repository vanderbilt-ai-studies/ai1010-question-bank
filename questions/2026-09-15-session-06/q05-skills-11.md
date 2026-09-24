---
id: q05-skills-11
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [skill-structure, verification]
answer: C
---

**Question:** Why is seeing Markdown-style headings in an editor insufficient to confirm that a skill file was saved properly?

- A. Typing Markdown headings automatically changes the saved format
- B. Changing the filename also converts rich text into plain text
- C. The saved format or filename may still be wrong
- D. Opening a file in an editor establishes that the agent can use it

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Visible heading syntax does not establish the actual file format. A document can look like Markdown while still being saved as rich text.
- B. Not quite. The filename and saved format are separate checks. A .md name does not by itself convert rich-text contents.
- C. Correct. Appearance does not establish the saved file type. Check for plain-text Markdown and the intended filename before testing the skill.
- D. Not quite. An editor can display a document without proving it is saved as the intended skill file. Check the format and name, then test the result.

</details>
