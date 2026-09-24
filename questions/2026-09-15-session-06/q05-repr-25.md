---
id: q05-repr-25
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [activation-space, training-vs-inference, decoder-stack]
answer: A
---

**Question:** While tracing one response, you observe a token's numerical representation changing across several blocks while learned weights stay fixed. How should you interpret this?

- A. The blocks are processing context with the trained model
- B. Each changed representation is a newly created vocabulary entry
- C. Each block has completed a fresh round of model training
- D. The trace is showing finished answer words between the blocks

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: A**

- A. Correct. Changing intermediate representations is expected during inference. The weights can remain fixed while attention and feed-forward transformations alter those representations.
- B. Not quite. The cat-star example uses multiple stages for the same token. A changed vector is not evidence of an expanded vocabulary.
- C. Not quite. Training updates parameters. Your observation describes changing representations with fixed weights, which fits ordinary inference.
- D. Not quite. The values moving through blocks are numerical representations. Finished output tokens are selected near the end of the processing.

</details>
