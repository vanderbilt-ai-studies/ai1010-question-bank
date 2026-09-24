#!/usr/bin/env python3
"""Self-test for tools/build.py: every example in docs/examples/ is valid,
and each broken variant is caught.   python3 tools/test_build.py"""
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

_, ids = build.load_concepts()
KNOWN = set(ids)
examples = {p.stem: json.loads(p.read_text()) for p in sorted((build.ROOT / "docs" / "examples").glob("*.json"))}
failures = []

for stem, q in examples.items():
    problems = build.validate_question(q, KNOWN, stem=stem)
    if problems:
        failures.append(f"{stem} should be valid: {problems}")
    build.normalize(q)
missing = set(build.TYPES) - {q["type"] for q in examples.values()}
if missing:
    failures.append(f"no example for type(s) {sorted(missing)}")


def broken(stem, change, why):
    q = copy.deepcopy(examples[stem])
    change(q)
    if not build.validate_question(q, KNOWN, stem=stem):
        failures.append(f"not caught: {stem} with {why}")


broken("example-mc", lambda q: q["options"][1].update(weight=100), "two correct options")
broken("example-mc", lambda q: q["options"][0].pop("feedback"), "an option without feedback")
broken("example-mc", lambda q: q.update(concepts=["not-a-concept"]), "an unknown concept")
broken("example-mc", lambda q: q.update(type="WR"), "a non-auto-graded type")
broken("example-mc", lambda q: q.update(answer="A"), "a field from another type")
broken("example-mc", lambda q: q.update(date="Sept 1"), "a malformed date")
broken("example-mc", lambda q: q.update(id="other-id"), "an id that does not match the file")
broken("example-tf", lambda q: q.update(answer="true"), "a string instead of true/false")
broken("example-tf", lambda q: q.pop("feedback_false"), "missing feedback for False")
broken("example-ms", lambda q: [o.update(correct=False) for o in q["options"]], "no correct option")
broken("example-ms", lambda q: q.update(grading="partial"), "an unknown grading rule")
broken("example-sa", lambda q: q["accepted"].append({"text": "([", "evaluation": "regex"}), "a bad regex")
broken("example-sa", lambda q: q.pop("feedback"), "no feedback")
broken("example-sa", lambda q: [a.update(weight=50) for a in q["accepted"]], "no full-credit answer")
broken("example-msa", lambda q: q.update(boxes=5), "more boxes than accepted answers")
broken("example-fib", lambda q: q.update(question="Only {{1}} here."), "blank markers that do not match")
broken("example-mat", lambda q: q["pairs"].append(dict(q["pairs"][0])), "a repeated choice")
broken("example-ord", lambda q: q.update(items=["only one"]), "a single item")
broken("example-arith", lambda q: q.update(formula="{n} / {speed}"), "an undefined variable")
broken("example-sigfig", lambda q: q.pop("significant_figures"), "no significant-figure count")

if failures:
    print("\n".join(failures))
    sys.exit(1)
print(f"ok: {len(examples)} examples valid, all broken variants caught")
