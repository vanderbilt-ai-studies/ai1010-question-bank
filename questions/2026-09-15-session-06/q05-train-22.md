---
id: q05-train-22
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [self-supervised-learning, pre-training]
answer: B
---

**Question:** A training program takes a sentence, hides its final token, and trains a model to predict that token from the earlier text. Which idea does this illustrate?

- A. Ordinary inference using weights without a learning update
- B. Self-supervised learning using a target supplied by the text
- C. Preference learning using human rankings of several responses
- D. Assistant fine-tuning using demonstrations of helpful replies

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. The scenario explicitly trains the model on a target. Ordinary inference generates outputs without that parameter-update process.
- B. Correct. The token already in the sentence supplies the answer for the learning objective. No person needs to label that continuation separately.
- C. Not quite. There are no ranked alternative responses in this scenario. The learning target is a token drawn from the existing text.
- D. Not quite. This example does not provide a desired assistant reply. It uses the next token from text as a prediction target.

</details>
