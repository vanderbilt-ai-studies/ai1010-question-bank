# Build your own self-testing skill

This bank is raw material. What you build on top of it is up to you. The goal:
an agent skill on your own computer that quizzes you from this bank the way
*you* want to be quizzed, remembers how you did, and steers you toward what
you have not mastered.

You will build it with **Skill Creator**, the skill for building skills that
you met in Session 5. You describe what you want; it drafts the skill, tests
it, and helps you improve it. Everything you have learned about skills applies:
a clear description so it triggers, a SKILL.md with the procedure, scripts for
the parts that should be exact, and an evaluation to check it actually helps.

## Before you start

You need:

1. **A copy of this repository** on your computer (see "Getting a copy" in the
   [README](../README.md)). Note the folder path -- your skill needs it.
2. **An agent that can read files on your computer:** Claude Code (desktop app
   or command line) or Cowork. Plain chat cannot read the bank from disk.
3. **Skill Creator** enabled. It is one of the skills in your Claude settings;
   if you are not sure, ask your agent "is skill-creator available?"

## The one file your skill should read

[`data/questions.json`](../data/questions.json) holds every question as
structured data. One entry looks like this (shortened):

```json
{
  "id": "q02-a-01",
  "date": "2026-09-03",
  "date_basis": "discussed",
  "session": 3,
  "source": "Quiz 2 - Sessions 1-3: Choosing a Model and Thinking Budgets",
  "concepts": ["model-selection"],
  "question": "Claude's four model tiers, listed from the smallest to the largest, are:",
  "options": [
    {"letter": "A", "text": "Sonnet 5, Haiku 4.5, Opus 5, Fable 5.1", "correct": false, "explanation": "Not quite. ..."},
    {"letter": "B", "text": "Haiku 4.5, Sonnet 5, Opus 5, Fable 5.1", "correct": true,  "explanation": "Correct. ..."}
  ],
  "answer": "B",
  "path": "questions/2026-09-03-session-03/q02-a-01.md"
}
```

The same file also lists every concept, with its definition, under
`"concepts"`. The full format is in [question-format.md](question-format.md).

## Decide what you want before you open Skill Creator

Skill Creator works best when you know what "good" looks like. Spend five
minutes on these. There is no right answer; your choices are what make the
skill yours.

- **What do you want to practice?** One concept (`attention`)? Everything from
  one week? Your weakest concepts? A mixed review before the midterm?
- **How should a session feel?** Ten questions and a score? Keep going until
  you get three in a row? One question a day?
- **What happens after you answer?** Show every option's explanation, or only
  the one you picked? Ask you to explain *why* before revealing the answer?
- **What should it remember?** Which questions you missed, when you last saw
  each concept, how long it has been since you got one right?
- **How should it choose the next question?** At random, weakest concept
  first, or spaced repetition (a missed question comes back soon; one you keep
  getting right comes back rarely)?

## Where to keep your progress

**Keep your own records outside this repository folder** -- for example
`~/ai1010-self-test/progress.json`. When you pull new questions, git updates
this folder, and a file you added inside it can get in the way. Your score
history is yours; it never needs to go back to GitHub.

Store progress by question `id`. Ids never change, so your history stays
correct as new questions arrive.

## A starting prompt for Skill Creator

Open Claude Code (or Cowork) and paste something like this, changing the parts
in brackets to match your decisions:

> Use skill-creator to build me a personal skill called `ai1010-self-test`.
>
> It quizzes me from the AI 1010 question bank at
> `[/Users/you/Documents/ai1010-question-bank]`. It reads
> `data/questions.json` there; each question has an id, a date, concept tags,
> lettered options, the correct answer and an explanation for every option.
>
> When I say things like "quiz me on attention" or "review this week", it
> should: [pick 10 questions on the concepts or dates I name, favoring ones I
> have missed before]; show one question at a time **without revealing the
> answer**; wait for my letter; then tell me if I was right and show
> [the explanation for my choice and for the correct answer].
>
> Keep my history in `[~/ai1010-self-test/progress.json]` (outside the bank
> folder): for each question id, when I saw it and whether I got it right.
> At the end of a session, show my score and my three weakest concepts.
>
> Use a small Python script for choosing questions and updating my history,
> so that part is exact; use the model for conversation and explanations.

Skill Creator will ask follow-up questions, draft the skill, and offer to test
it. Let it.

## Things that go wrong (and what to ask for instead)

- **It shows the answer with the question.** The model can see the whole
  question, answer and all. Ask for the question-picking script to print only
  the stem and options, and to look up the answer only after you reply.
- **It makes up questions.** If the skill writes its own questions and passes
  them off as bank questions, you are studying something your instructor never
  wrote. Tell it to draw only from `data/questions.json` and to cite the
  question `id`. If you *want* generated practice questions, ask for them to be
  labeled clearly as generated.
- **It forgets your history.** If progress lives only in the conversation, it
  is gone next time. Check the progress file is actually being written (open it
  yourself -- do not take the agent's word for it).
- **It cannot find the bank.** Put the full folder path in the SKILL.md, or
  have the skill ask you for it once and save it to your progress folder.
- **It triggers when you did not want it, or not at all.** That is the
  description. Revise it with Skill Creator's description-tuning step.
- **Old questions after a pull.** Your skill should re-read the file each
  session rather than caching a copy.

## Test it like you learned to

Session 5 was about evaluating skills. Apply it here:

1. **Decide what "working" means first.** For example: never shows the
   answer early; only uses bank questions; the progress file is correct after
   a session; the weakest-concept report matches the history.
2. **Try a few different requests:** a single concept, a date range, "my
   weakest stuff", a concept with only a handful of questions (the counts are in
   [CONCEPTS.md](../CONCEPTS.md)).
3. **Check the evidence yourself.** Open the progress file. Look up a
   question id and confirm the answer the skill marked correct.
4. **Try it on a smaller model.** A skill that works on Opus may stumble on
   Haiku. If you want it cheap and fast, test it there.

## Ideas for going further

- **Spaced repetition:** schedule each question's next appearance based on
  your history, so review time goes where it is needed.
- **Concept map:** use the concept groups in `concepts.json` to show your
  mastery group by group (inside the model, training, agents, skills...).
- **Explain it back:** before revealing the answer, ask you to explain your
  choice in a sentence, then compare your reasoning to the explanation.
- **Exam mode:** a timed, mixed set drawn in proportion to how often each
  concept appears in the bank.
- **Weekly digest:** at the end of each week, list the concepts that came up
  in class that you have not practiced yet (compare question dates to your
  history).

## Sharing what you build

Session 8 covered sharing skills through repositories. If your skill turns out
well, put it in your own GitHub repository with a README explaining how to
set it up -- but leave your `progress.json` out of it. Your history is your
own.
