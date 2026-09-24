---
id: q05-skills-17
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [skill-evaluation, task-specification]
answer: A
---

**Question:** You test a report-writing skill and find that it discusses two designs separately, although your task requires a comparison. What should you do next?

- A. Add the comparison requirement and inspect a new run
- B. Edit the current report and treat the skill as repaired
- C. Keep the skill unchanged and wait for a better result
- D. Remove the comparison criterion to match the output

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. Turn the missing task criterion into a specific instruction, then test whether the revised procedure produces the required comparison.
- B. Not quite. That can improve this report, but it does not revise the reusable procedure or show that a later run will make the comparison.
- C. Not quite. Another run might differ, but this leaves the identified instruction mismatch in place. Make the requirement explicit and test it.
- D. Not quite. The intended task supplies the evaluation standard. An incomplete result is a reason to repair the procedure, not redefine success around the omission.

</details>
