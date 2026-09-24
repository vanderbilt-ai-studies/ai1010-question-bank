---
id: q05-train-15
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [training-vs-inference, parameter]
answer: C
---

**Question:** Why does training measure performance against an objective before updating model parameters?

- A. The measurement determines which tool permissions the model needs
- B. The measurement certifies the truth of future generated claims
- C. The measured error helps guide parameter adjustments
- D. The measurement replaces the need to change any learned values

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Tool permissions constrain external operations. Training measurements instead support learning updates to the model's parameters.
- B. Not quite. A learning objective guides training, but success at prediction does not verify every learned association or guarantee future accuracy.
- C. Correct. Training measures performance and computes how parameters affect the error. Those results support updates to learned weights.
- D. Not quite. Evaluating performance supplies information for learning. Training also uses that information to update parameters; evaluation alone is not that update.

</details>
