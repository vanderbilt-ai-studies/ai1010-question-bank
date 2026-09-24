---
id: q05-repr-15
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [context, grounding, training-vs-inference]
answer: C
---

**Question:** Why can adding relevant material to context improve an answer without further training?

- A. The material becomes a new vocabulary entry before generation
- B. The material converts internal representations into written rules
- C. The model can use that evidence with its existing weights
- D. The material replaces the parameter arrays for that response

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: C**

- A. Not quite. Providing a document supplies tokens in context. It does not require adding a vocabulary entry for the document.
- B. Not quite. The internal computation still transforms numerical representations. Context provides evidence without changing that process into rule text.
- C. Correct. Context gives the model information to use in the current generation. Improved performance does not by itself imply changed parameters.
- D. Not quite. The arrays still supply learned parameters. New context influences the representations processed using those parameters.

</details>
