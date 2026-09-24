---
id: q05-train-04
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [pre-training]
answer: D
---

**Question:** What is pre-training in the text-model example?

- A. Behavioral learning by comparing preferred assistant responses
- B. Response generation by running a model with fixed weights
- C. Instruction learning by imitating example assistant responses
- D. Foundational learning by predicting tokens in text

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: D**

- A. Not quite. Response comparisons are used in preference-based post-training. They build on a base model rather than describe the foundational prediction stage.
- B. Not quite. Running an already-trained model describes ordinary inference. Pre-training changes weights through a learning process.
- C. Not quite. Example responses are used in supervised fine-tuning. The foundational text-model example instead predicts the next token from existing text.
- D. Correct. The model learns broad language patterns and associations through prediction over large datasets. Later training can shape how it responds as an assistant.

</details>
