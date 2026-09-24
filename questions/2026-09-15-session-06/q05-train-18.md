---
id: q05-train-18
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: B
---

**Question:** How can two post-training procedures differ even when both use human preferences?

- A. A preferred output is a demonstration, so comparisons cannot guide learning
- B. Preferences can guide training through several different methods
- C. Preference information describes inference rather than further model training
- D. Every preference method requires humans to write a target for each next token

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Comparisons can identify a preferred output without supplying the same training information as a demonstration. The notes explicitly include preferences as a learning source.
- B. Correct. The notes identify alternatives to the classic reinforcement-learning pipeline. The common role of preference information does not make the procedures identical.
- C. Not quite. Preferences can supply learning information during post-training. Their use is not limited to the current inference response.
- D. Not quite. That requirement confuses different learning signals. The notes distinguish text-derived next-token targets, demonstrations, and comparisons of outputs.

</details>
