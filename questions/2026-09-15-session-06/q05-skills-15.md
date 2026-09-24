---
id: q05-skills-15
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [verification]
answer: C
---

**Question:** Why does an agent's message saying it created a complete file provide weaker evidence than inspecting the file?

- A. The message changes the task requirements after execution
- B. The message determines the output format more reliably
- C. The message reports success without showing the full artifact
- D. The message confirms that every packaged component is the intended version

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. A completion message describes claimed success. The issue is whether the actual artifact satisfies the existing requirements, rather than whether the message creates new ones.
- B. Not quite. A message may describe a format, but opening the output lets you verify the artifact itself rather than relying on that description.
- C. Correct. A success claim does not establish that the complete artifact exists in the correct place. Inspect its contents and verify the intended version and location.
- D. Not quite. A claim of completion does not verify which versions are in the artifact. Open the file and inspect the included materials.

</details>
