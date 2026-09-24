---
id: q05-skills-12
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [skill-evaluation, verification]
answer: D
---

**Question:** Why should you compare a skill's test output with your original task criteria?

- A. The test output establishes what the task should have been
- B. The criteria determine which model parameters were changed
- C. The criteria replace the need to open the output artifact
- D. A finished run may still omit required work

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. This reverses the comparison. Your intended task and criteria provide the standard for deciding whether the produced output is useful.
- B. Not quite. Skill testing checks the result of reusable instructions. It does not require treating an instruction edit as a model-weight update.
- C. Not quite. Criteria tell you what to look for, but you still need to inspect the actual output to see whether it meets them.
- D. Correct. Completing a run and satisfying the task are different checks. Evaluate the actual output against what you asked the skill to accomplish.

</details>
