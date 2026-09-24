---
id: q05-train-16
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [post-training]
answer: D
---

**Question:** How do demonstrations and preference comparisons supply different training information?

- A. Demonstrations rank alternatives; comparisons provide the full desired answer
- B. Demonstrations measure truth; comparisons guarantee future helpful behavior
- C. Demonstrations change conversation history; comparisons leave parameters fixed
- D. Demonstrations give examples; comparisons express relative preference

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. This reverses the roles described in the notes. Demonstrations supply example responses, while comparisons identify a preferred alternative.
- B. Not quite. Neither training input guarantees those outcomes. The notes distinguish example responses from relative preferences and emphasize the limits of behavioral training.
- C. Not quite. These are sources of training information in this question. Using them in training differs from adding material to a current inference context.
- D. Correct. An example answer illustrates what to produce. Comparing alternatives expresses relative preference, which can train a reward model in the classic pipeline.

</details>
