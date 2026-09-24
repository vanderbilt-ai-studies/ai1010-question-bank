# AI 1010 Question Bank

Every question from the AI 1010 pre-class quiz banks, in one place, tagged by
concept and dated. It is here so you can study by concept, see what you have
not mastered yet, and -- the real point -- **build your own self-testing
system** with an agent skill on your own computer.

AI 1010 is Vanderbilt's *Survey of Generative AI Tools and Applications*.

## What is in here

| Where | What it holds |
|---|---|
| [`data/questions.json`](data/questions.json) | Every question in one file. **This is the file your skill should read.** |
| [`CONCEPTS.md`](CONCEPTS.md) | Every concept tag, what it means, and how many questions test it. |
| [`concepts.json`](concepts.json) | The same concept list as data. It is the only list of allowed tags. |
| [`docs/build-your-own-self-test.md`](docs/build-your-own-self-test.md) | How to build a self-testing skill with Skill Creator. **Start here.** |
| [`docs/question-format.md`](docs/question-format.md) | The question types and exactly how each is stored. [Examples of every type](docs/examples/). |
| [`questions/`](questions/) | The source: one JSON file per question, one folder per class session. [Folders by date](questions/README.md). |
| [`tools/build.py`](tools/build.py) | Checks every question and regenerates `data/questions.json` and the indexes. |

## How each question is dated

Each question carries a `date` -- the day the material was **discussed in class**.
For a quiz question, that is the class session right before the quiz was due.
Quiz 3, for example, was due before Session 5, so its questions are dated
Session 4 (Tuesday, September 8). `date_basis: discussed` marks those.

Questions added straight to this repository instead carry the day they were
added, marked `date_basis: added`.

Many quizzes covered "Sessions 1 through N", so a question dated September 15
may test an idea first introduced in late August. Use the concept tags, not
the date, to find everything on one idea.

## Question types

Every question uses one of Brightspace's auto-graded question types, the same
kinds you meet on the course quizzes: true or false, multiple choice,
multi-select, short answer, multi-short answer, fill in the blanks, matching,
ordering, arithmetic and significant figures. Today the bank is all multiple
choice; other types will arrive as they are written. Build your skill to
handle every type in [question-format.md](docs/question-format.md) and it
will not break when they do.

Every question comes with an explanation -- for multiple choice, one for
**each** option, saying why it is right or why it is tempting but wrong. The
explanations are where most of the learning is, so make your skill show them.

## Getting a copy on your computer

You need a copy on your own machine for your skill to read it. Any of these
works:

- **GitHub Desktop:** File -> Clone repository -> `vanderbilt-ai-studies/ai1010-question-bank`.
- **Command line (CLI, command-line interface):**

  ```bash
  git clone https://github.com/vanderbilt-ai-studies/ai1010-question-bank.git
  ```

- **Ask your agent:** in Claude Code, "clone vanderbilt-ai-studies/ai1010-question-bank into my Documents folder."

New questions arrive after each quiz closes. To get them, pull (GitHub Desktop:
**Fetch origin**, then **Pull**; command line: `git pull`).

## A note on the quizzes themselves

This bank is for practice. The graded pre-class quizzes still have their own
rule: **no generative AI while taking them.** Practice here with any tools you
like, then take the real quiz on your own.

## For the instructor: adding questions

Quiz banks from the course repository are exported with
`quizzes/export-question-bank.py` there, once the quiz's last section is past
its due time. The exporter checks every question with this repository's
validator before writing anything.

A question added directly is one JSON file under `questions/` (for example
`questions/added/`), following [question-format.md](docs/question-format.md).
Leave out `date` and it is stamped with the day it was added. To check and
re-index locally:

```bash
python3 tools/build.py --fill-dates
```
