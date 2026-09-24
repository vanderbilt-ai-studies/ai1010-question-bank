#!/usr/bin/env python3
"""Validate the question bank and regenerate its indexes.

    python3 tools/build.py               validate, then write data/questions.json,
                                         CONCEPTS.md and questions/README.md
    python3 tools/build.py --fill-dates  also stamp a date on any question that
                                         lacks one (the day it was added)
    python3 tools/build.py --check       validate and confirm the generated files
                                         are current; writes nothing

Each question is one JSON file under questions/. Its `type` is one of the
auto-graded Brightspace question types; see docs/question-format.md.
Other tools (the course exporter) import validate_question() from here, so
this file is the single definition of a valid question.

Standard library only, so it runs anywhere Python 3.9+ does.
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = ROOT / "questions"
CONCEPTS_JSON = ROOT / "concepts.json"
OUT_JSON = ROOT / "data" / "questions.json"
OUT_CONCEPTS = ROOT / "CONCEPTS.md"
OUT_INDEX = QUESTIONS / "README.md"

# Brightspace's auto-graded question types. Written Response and Likert are
# not auto-graded, so they do not belong in a self-testing bank.
TYPES = {
    "TF": "True or False",
    "MC": "Multiple Choice",
    "MS": "Multi-Select",
    "SA": "Short Answer",
    "MSA": "Multi-Short Answer",
    "FIB": "Fill in the Blanks",
    "MAT": "Matching",
    "ORD": "Ordering",
    "ARITH": "Arithmetic",
    "SIGFIG": "Significant Figures",
}
MS_GRADING = ("all_or_nothing", "right_answers", "right_minus_wrong", "correct_answers_limited_selections")
PAIR_GRADING = ("equally_weighted", "all_or_nothing", "right_minus_wrong")
EVALUATION = ("case_insensitive", "case_sensitive", "regex")
LEVELS = ("recall", "understanding", "application")
DATE_BASES = ("discussed", "added")

COMMON = {"id", "type", "date", "date_basis", "session", "source", "concepts",
          "level", "points", "question", "feedback", "hint"}
TYPE_FIELDS = {
    "TF": {"answer", "feedback_true", "feedback_false"},
    "MC": {"options"},
    "MS": {"options", "grading"},
    "SA": {"accepted"},
    "MSA": {"boxes", "accepted"},
    "FIB": {"blanks"},
    "MAT": {"pairs", "distractors", "grading"},
    "ORD": {"items", "grading"},
    "ARITH": {"formula", "variables", "decimals", "tolerance", "units"},
    "SIGFIG": {"formula", "variables", "significant_figures", "tolerance"},
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
BLANK_RE = re.compile(r"\{\{(\d+)\}\}")
VAR_RE = re.compile(r"\{([A-Za-z_]\w*)\}")


# ---------------------------------------------------------------- validation

def _text(v):
    return isinstance(v, str) and v.strip() != ""


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _check_accepted(answers, where, p):
    """Typed-answer list for SA, MSA and each FIB blank."""
    if not isinstance(answers, list) or not answers:
        p.append(f"{where} must be a non-empty list of accepted answers")
        return
    for i, a in enumerate(answers):
        w = f"{where}[{i}]"
        if not isinstance(a, dict) or not _text(a.get("text")):
            p.append(f"{w} needs non-empty 'text'")
            continue
        extra = set(a) - {"text", "weight", "evaluation"}
        if extra:
            p.append(f"{w} has unknown field(s) {sorted(extra)}")
        if "weight" in a and not (_num(a["weight"]) and 0 <= a["weight"] <= 100):
            p.append(f"{w}.weight must be 0-100")
        ev = a.get("evaluation", "case_insensitive")
        if ev not in EVALUATION:
            p.append(f"{w}.evaluation must be one of {EVALUATION}")
        elif ev == "regex":
            try:
                re.compile(a["text"])
            except re.error as e:
                p.append(f"{w} is not a valid regular expression: {e}")
    if not any(a.get("weight", 100) == 100 for a in answers if isinstance(a, dict)):
        p.append(f"{where}: at least one accepted answer must be worth 100")


def _check_variables(q, p):
    vs = q.get("variables")
    if not isinstance(vs, list) or not vs:
        p.append("variables must be a non-empty list")
        return
    names = set()
    for i, v in enumerate(vs):
        if not isinstance(v, dict) or not re.match(r"^[A-Za-z_]\w*$", str(v.get("name", ""))):
            p.append(f"variables[{i}] needs a 'name' (letters, digits, underscore)")
            continue
        names.add(v["name"])
        if not (_num(v.get("min")) and _num(v.get("max")) and v["min"] <= v["max"]):
            p.append(f"variables[{i}] needs numeric min <= max")
        extra = set(v) - {"name", "min", "max", "decimals", "step"}
        if extra:
            p.append(f"variables[{i}] has unknown field(s) {sorted(extra)}")
    used = set(VAR_RE.findall(q.get("formula", "")))
    if not _text(q.get("formula")):
        p.append("formula is required, with variables written {x}")
    elif used - names:
        p.append(f"formula uses undefined variable(s) {sorted(used - names)}")
    tol = q.get("tolerance")
    if tol is not None and not (isinstance(tol, dict) and _num(tol.get("value"))
                                and tol.get("mode") in ("units", "percent")):
        p.append("tolerance must be {\"value\": number, \"mode\": \"units\" | \"percent\"}")


def validate_question(q, concept_ids, stem=None):
    """Return a list of problems with question dict q; empty means valid."""
    p = []
    if not isinstance(q, dict):
        return ["a question must be a JSON object"]
    qid, qtype = q.get("id", ""), q.get("type")
    if not ID_RE.match(str(qid)):
        p.append("id must be lowercase letters, digits and hyphens")
    elif stem is not None and qid != stem:
        p.append(f"id '{qid}' must match the file name '{stem}.json'")
    if qtype not in TYPES:
        return p + [f"type must be one of {list(TYPES)} (auto-graded Brightspace types)"]
    extra = set(q) - COMMON - TYPE_FIELDS[qtype]
    if extra:
        p.append(f"unknown field(s) for type {qtype}: {sorted(extra)}")

    if q.get("date") is not None and not DATE_RE.match(str(q["date"])):
        p.append("date must be YYYY-MM-DD")
    if q.get("date_basis", "added") not in DATE_BASES:
        p.append(f"date_basis must be one of {DATE_BASES}")
    if q.get("session") is not None and not isinstance(q["session"], int):
        p.append("session must be a whole number")
    if q.get("level") is not None and q["level"] not in LEVELS:
        p.append(f"level must be one of {LEVELS}")
    if "points" in q and not (_num(q["points"]) and q["points"] > 0):
        p.append("points must be a positive number")
    for f in ("source", "feedback", "hint"):
        if f in q and not isinstance(q[f], str):
            p.append(f"{f} must be text")
    concepts = q.get("concepts")
    if not isinstance(concepts, list) or not concepts:
        p.append("concepts must be a non-empty list of concept ids")
    else:
        unknown = [c for c in concepts if c not in concept_ids]
        if unknown:
            p.append(f"unknown concept(s) {unknown}; add them to concepts.json first")
        if len(set(concepts)) != len(concepts):
            p.append("concepts has a duplicate")
    if not _text(q.get("question")):
        p.append("question text is empty")

    if qtype == "TF":
        if not isinstance(q.get("answer"), bool):
            p.append("answer must be true or false")
        for f in ("feedback_true", "feedback_false"):
            if not _text(q.get(f)):
                p.append(f"{f} is required (feedback for choosing that answer)")

    elif qtype in ("MC", "MS"):
        opts = q.get("options")
        if not isinstance(opts, list) or len(opts) < 2:
            p.append("options must list at least two choices")
            opts = []
        for i, o in enumerate(opts):
            w = f"options[{i}]"
            if not isinstance(o, dict) or not _text(o.get("text")) or not _text(o.get("feedback")):
                p.append(f"{w} needs non-empty 'text' and 'feedback'")
                continue
            allowed = {"text", "feedback", "weight"} if qtype == "MC" else {"text", "feedback", "correct"}
            if set(o) - allowed:
                p.append(f"{w} has unknown field(s) {sorted(set(o) - allowed)}")
            if qtype == "MC" and not (_num(o.get("weight")) and 0 <= o["weight"] <= 100):
                p.append(f"{w}.weight must be 0-100 (100 = the correct answer)")
            if qtype == "MS" and not isinstance(o.get("correct"), bool):
                p.append(f"{w}.correct must be true or false")
        if qtype == "MC" and opts and sum(1 for o in opts if isinstance(o, dict) and o.get("weight") == 100) != 1:
            p.append("exactly one option must have weight 100")
        if qtype == "MS":
            if opts and not any(isinstance(o, dict) and o.get("correct") is True for o in opts):
                p.append("at least one option must be correct")
            if q.get("grading", "all_or_nothing") not in MS_GRADING:
                p.append(f"grading must be one of {MS_GRADING}")

    elif qtype == "SA":
        _check_accepted(q.get("accepted"), "accepted", p)

    elif qtype == "MSA":
        if not (isinstance(q.get("boxes"), int) and q["boxes"] >= 1):
            p.append("boxes (number of answer boxes) must be a whole number >= 1")
        _check_accepted(q.get("accepted"), "accepted", p)
        if isinstance(q.get("boxes"), int) and isinstance(q.get("accepted"), list) \
                and len(q["accepted"]) < q["boxes"]:
            p.append("need at least as many accepted answers as boxes")

    elif qtype == "FIB":
        blanks = q.get("blanks")
        marks = [int(n) for n in BLANK_RE.findall(q.get("question", ""))]
        if not isinstance(blanks, list) or not blanks:
            p.append("blanks must be a non-empty list")
        else:
            if marks != list(range(1, len(blanks) + 1)):
                p.append(f"question must mark blanks {{{{1}}}}..{{{{{len(blanks)}}}}} once each, in order; found {marks}")
            for i, b in enumerate(blanks):
                if not isinstance(b, dict) or set(b) - {"accepted", "size"}:
                    p.append(f"blanks[{i}] must be {{\"accepted\": [...]}} (optional \"size\")")
                    continue
                _check_accepted(b.get("accepted"), f"blanks[{i}].accepted", p)

    elif qtype == "MAT":
        pairs = q.get("pairs")
        if not isinstance(pairs, list) or len(pairs) < 2:
            p.append("pairs must list at least two {\"choice\", \"match\"} pairs")
        else:
            for i, pr in enumerate(pairs):
                if not isinstance(pr, dict) or set(pr) != {"choice", "match"} \
                        or not _text(pr["choice"]) or not _text(pr["match"]):
                    p.append(f"pairs[{i}] must be {{\"choice\": text, \"match\": text}}")
            choices = [pr.get("choice") for pr in pairs if isinstance(pr, dict)]
            if len(set(choices)) != len(choices):
                p.append("each choice may appear only once")
        d = q.get("distractors", [])
        if not (isinstance(d, list) and all(_text(x) for x in d)):
            p.append("distractors must be a list of extra match texts")
        if q.get("grading", "equally_weighted") not in PAIR_GRADING:
            p.append(f"grading must be one of {PAIR_GRADING}")

    elif qtype == "ORD":
        items = q.get("items")
        if not (isinstance(items, list) and len(items) >= 2 and all(_text(x) for x in items)):
            p.append("items must list at least two texts, in the correct order")
        elif len(set(items)) != len(items):
            p.append("items must be distinct")
        if q.get("grading", "equally_weighted") not in PAIR_GRADING:
            p.append(f"grading must be one of {PAIR_GRADING}")

    elif qtype == "ARITH":
        _check_variables(q, p)
        if "decimals" in q and not (isinstance(q["decimals"], int) and q["decimals"] >= 0):
            p.append("decimals must be a whole number >= 0")

    elif qtype == "SIGFIG":
        _check_variables(q, p)
        if not (isinstance(q.get("significant_figures"), int) and q["significant_figures"] >= 1):
            p.append("significant_figures must be a whole number >= 1")

    if qtype not in ("TF", "MC", "MS") and not _text(q.get("feedback")):
        p.append("feedback is required: explain the answer, since there are no per-option explanations")
    return p


def normalize(q):
    """Fill defaults so every consumer sees the same shape."""
    q = dict(q)
    q.setdefault("date_basis", "added")
    q.setdefault("points", 1)
    for f in ("session", "level", "source", "feedback", "hint"):
        q.setdefault(f, None)
    t = q["type"]
    if t == "MC":
        q["options"] = [dict(o, correct=o["weight"] == 100) for o in q["options"]]
    if t == "MS":
        q.setdefault("grading", "all_or_nothing")
    if t in ("MAT", "ORD"):
        q.setdefault("grading", "equally_weighted")
    if t == "MAT":
        q.setdefault("distractors", [])

    def acc(lst):
        return [{"text": a["text"], "weight": a.get("weight", 100),
                 "evaluation": a.get("evaluation", "case_insensitive")} for a in lst]
    if t in ("SA", "MSA"):
        q["accepted"] = acc(q["accepted"])
    if t == "FIB":
        q["blanks"] = [dict(b, accepted=acc(b["accepted"])) for b in q["blanks"]]
    return q


# ---------------------------------------------------------------- dates

def today_central():
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo("America/Chicago")).date().isoformat()
    except Exception:
        return datetime.date.today().isoformat()


def date_first_added(path):
    """The day git first saw this file; today if it has not been committed."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%cs", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
        if out:
            return out[-1]
    except (OSError, subprocess.CalledProcessError):
        pass
    return today_central()


def write_question(path, q):
    path.write_text(json.dumps(q, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def with_date(q, date):
    """Insert date and date_basis right after id and type."""
    out = {}
    for k, v in q.items():
        if k in ("date", "date_basis"):
            continue
        out[k] = v
        if k == "type":
            out["date"], out["date_basis"] = date, "added"
    return out


# ---------------------------------------------------------------- rendering

def render_concepts(vocab, questions):
    counts = {}
    for q in questions:
        for c in q["concepts"]:
            counts[c] = counts.get(c, 0) + 1
    total = sum(len(g["concepts"]) for g in vocab["groups"])
    out = [
        "# Concepts",
        "",
        "<!-- Generated by tools/build.py from concepts.json. Edit concepts.json, not this file. -->",
        "",
        f"Every question is tagged with one or more of these {total} concepts. The first tag on a "
        "question is the concept it tests most directly. Counts include every question carrying the tag.",
        "",
    ]
    for g in vocab["groups"]:
        out += [f"## {g['label']}", "", "| Concept | Tag | Questions | What it means |", "|---|---|---|---|"]
        for c in g["concepts"]:
            out.append(f"| {c['label']} | `{c['id']}` | {counts.get(c['id'], 0)} | {c['definition']} |")
        out.append("")
    return "\n".join(out)


def render_index(questions):
    groups = {}
    for q in questions:
        groups.setdefault(str(Path(q["path"]).parent.relative_to("questions")), []).append(q)
    out = [
        "# Questions by date",
        "",
        "<!-- Generated by tools/build.py. -->",
        "",
        "Each folder holds the questions from one class session (dated the day the material was "
        "discussed) or questions added straight to this repository (dated the day they were added).",
        "",
        "| Date | Folder | Source | Questions | Types |",
        "|---|---|---|---|---|",
    ]
    for folder, qs in sorted(groups.items()):
        dates = sorted({q["date"] for q in qs})
        sources = sorted({q["source"] for q in qs if q["source"]})
        kinds = {}
        for q in qs:
            kinds[q["type"]] = kinds.get(q["type"], 0) + 1
        out.append(f"| {', '.join(dates)} | [{folder}]({folder}/) | {'; '.join(sources) or '-'} | "
                   f"{len(qs)} | {', '.join(f'{k} {n}' for k, n in sorted(kinds.items()))} |")
    out += ["", f"Total: {len(questions)} questions.", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- main

def load_concepts():
    vocab = json.loads(CONCEPTS_JSON.read_text(encoding="utf-8"))
    ids = [c["id"] for g in vocab["groups"] for c in g["concepts"]]
    dupes = sorted({c for c in ids if ids.count(c) > 1})
    bad = [c for c in ids if not ID_RE.match(c)]
    if dupes or bad:
        sys.exit(f"concepts.json: duplicate ids {dupes}; badly formed ids {bad}")
    return vocab, ids


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate and compare; write nothing")
    ap.add_argument("--fill-dates", action="store_true", help="stamp missing dates into question files")
    args = ap.parse_args()

    vocab, concept_ids = load_concepts()
    known = set(concept_ids)
    errors, questions, seen = [], [], {}
    stray = [p for p in QUESTIONS.rglob("*") if p.is_file() and p.suffix != ".json" and p != OUT_INDEX]
    for p in stray:
        errors.append(f"{p.relative_to(ROOT)}: only .json question files belong under questions/")

    for path in sorted(QUESTIONS.rglob("*.json")):
        rel = path.relative_to(ROOT)
        try:
            q = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{rel}: not valid JSON ({e})")
            continue
        problems = validate_question(q, known, stem=path.stem)
        if problems:
            errors.append(f"{rel}:\n  - " + "\n  - ".join(problems))
            continue
        if q["id"] in seen:
            errors.append(f"{rel}: id '{q['id']}' is also used by {seen[q['id']]}")
            continue
        seen[q["id"]] = rel
        if not q.get("date"):
            if args.fill_dates and not args.check:
                q = with_date(q, date_first_added(path))
                write_question(path, q)
                print(f"dated {rel} {q['date']} (added)")
            else:
                errors.append(f"{rel}: no date (run python3 tools/build.py --fill-dates)")
                continue
        questions.append(dict(normalize(q), path=rel.as_posix()))

    if errors:
        print(f"{len(errors)} problem(s):\n", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)

    questions.sort(key=lambda q: (q["date"], q["id"]))
    outputs = {
        OUT_JSON: json.dumps({
            "about": "Generated by tools/build.py from questions/**/*.json. Do not edit by hand. "
                     "Format: docs/question-format.md.",
            "count": len(questions),
            "types": TYPES,
            "concepts": [dict(c, group=g["id"]) for g in vocab["groups"] for c in g["concepts"]],
            "questions": questions,
        }, indent=1, ensure_ascii=False) + "\n",
        OUT_CONCEPTS: render_concepts(vocab, questions),
        OUT_INDEX: render_index(questions),
    }
    stale = [p for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    if args.check:
        if stale:
            sys.exit("out of date (run python3 tools/build.py): "
                     + ", ".join(str(p.relative_to(ROOT)) for p in stale))
        print(f"ok: {len(questions)} questions, {len(concept_ids)} concepts, generated files current")
        return
    for p in stale:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(outputs[p], encoding="utf-8")
    print(f"ok: {len(questions)} questions, {len(concept_ids)} concepts; rewrote {len(stale)} generated file(s)")


if __name__ == "__main__":
    main()
