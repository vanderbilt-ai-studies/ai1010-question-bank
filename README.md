# AI 1010 Question Bank

Every question from the AI 1010 pre-class quiz banks, in one place, tagged by
concept and dated. It is here so you can study by concept, see what you have
not mastered yet, and -- the real point -- **build your own self-testing
system** with an agent skill on your own computer.

AI 1010 is Vanderbilt's *Survey of Generative AI Tools and Applications*.

## What is in here

| Where | What it holds |
|---|---|
| [`questions/`](questions/) | One Markdown file per question, in one folder per class session. [Browse by date](questions/README.md). |
| [`CONCEPTS.md`](CONCEPTS.md) | Every concept tag, what it means, how many questions test it, and links to each question. |
| [`concepts.json`](concepts.json) | The same concept list as data. It is the only list of allowed tags. |
| [`data/questions.json`](data/questions.json) | Every question in one file, as structured data. **This is the file your skill should read.** |
| [`docs/build-your-own-self-test.md`](docs/build-your-own-self-test.md) | How to build a self-testing skill with Skill Creator. **Start here.** |
| [`docs/question-format.md`](docs/question-format.md) | The exact format of a question file and of `data/questions.json`. |
| [`tools/build.py`](tools/build.py) | Checks every question and regenerates the indexes. |

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

## Reading a question

Each question file shows the question and its lettered options. The answer and
an explanation for **every** option -- why it is right, or why it is tempting
but wrong -- sit in a collapsed **"Show the answer"** section underneath. Try
the question first, then open it. The explanations are where most of the
learning is.

The files are plain Markdown with no images, so they read cleanly on GitHub, in
any text editor, and with a screen reader. The collapsed section is a standard
HTML `<details>` element: press Enter or Space on "Show the answer" to open it.

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

## For the instructor: adding a question

Copy [`templates/new-question.md`](templates/new-question.md) into a folder
under `questions/` (any folder; `questions/added/` is fine), fill it in, and
commit. You can leave the `date` line out: when the commit reaches `main`, a
GitHub Action stamps it with the day it was added and rebuilds the indexes. To
check locally first, run:

```bash
python3 tools/build.py --fill-dates
```

Quiz banks from the course repository are exported with
`quizzes/export-question-bank.py` there, once the quiz's last section is past
its due time.
