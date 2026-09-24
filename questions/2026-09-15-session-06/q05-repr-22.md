---
id: q05-repr-22
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [attention, activation-space, token-embedding]
answer: B
---

**Question:** You compare cat in a sentence about a sunny windowsill with cat in a sentence about an angry trainer. What should you expect inside the model?

- A. Each block must print a different replacement word for cat
- B. The same token can have different contextual representations
- C. The vocabulary must contain a separate ID for each sentence
- D. The two sentences must update different permanent weight values

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. Blocks transform numerical representations. They do not print intermediate replacement words as a required part of interpretation.
- B. Correct. The initial token identity does not force one interpretation. Attention can bring different surrounding information into its representation.
- C. Not quite. The cat-star diagram describes changing representations of the same token. Contextual interpretation does not require a new vocabulary entry for every sentence.
- D. Not quite. Processing different contexts changes current representations. Ordinary inference does not update permanent weights for each sentence.

</details>
