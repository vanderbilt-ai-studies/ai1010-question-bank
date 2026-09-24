---
id: q05-repr-18
date: 2026-09-15
date_basis: discussed
session: 6
source: Quiz 5 - Sessions 1-6: Model Training, Alignment, and the Agent Harness
concepts: [learned-knowledge, parameter]
answer: B
---

**Question:** Why does understanding a model's algorithm leave questions about its learned behavior?

- A. The program becomes inaccessible once training has finished
- B. Learned values also affect the resulting behavior
- C. The algorithm is replaced by English instructions at inference
- D. The vocabulary indices specify each complete answer in advance

<details>
<summary>Show the answer and why each option is right or wrong</summary>

**Answer: B**

- A. Not quite. The notes say software remains inspectable. The difficulty is explaining learned behavior from the algorithm and parameters, not the disappearance of the program.
- B. Correct. The program describes how computation proceeds. The interaction of many learned parameters with context can still make a particular behavior hard to explain.
- C. Not quite. The numerical computation still runs during inference. Understanding it is useful even though it does not fully explain every learned behavior.
- D. Not quite. Vocabulary indices identify tokens. They do not provide a list of complete answers explaining the model's behavior.

</details>
