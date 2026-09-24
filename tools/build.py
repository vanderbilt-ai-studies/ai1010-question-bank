#!/usr/bin/env python3
"""Validate the question bank and regenerate its indexes.

    python3 tools/build.py               validate, then write data/questions.json,
                                         CONCEPTS.md and questions/README.md
    python3 tools/build.py --fill-dates  also stamp a date on any question that
                                         lacks one (the day it was added)
    python3 tools/build.py --check       validate and confirm the generated files
                                         are current; writes nothing

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

LETTERS = "ABCDEFGH"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
OPTION_RE = re.compile(r"^- ([A-H])\. (.+)$")
DATE_BASES = ("discussed", "added")


class BankError(Exception):
    pass


# ---------------------------------------------------------------- parsing

def parse_frontmatter(text, where):
    if not text.startswith("---\n"):
        raise BankError(f"{where}: must start with a '---' frontmatter block")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise BankError(f"{where}: frontmatter block is not closed with '---'")
    meta = {}
    for n, line in enumerate(text[4:end].splitlines(), 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise BankError(f"{where}:{n}: expected 'key: value', got {line!r}")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
        elif len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        meta[key] = value
    return meta, text[end + 5:]


def parse_question(path):
    where = str(path.relative_to(ROOT))
    raw = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw, where)

    if "<details>" not in body or "</details>" not in body:
        raise BankError(f"{where}: needs a <details> block holding the answer and explanations")
    front, rest = body.split("<details>", 1)
    inside = rest.split("</details>", 1)[0]

    stem_lines, options = [], []
    for line in front.strip().splitlines():
        m = OPTION_RE.match(line)
        if m:
            options.append((m.group(1), m.group(2).strip()))
        elif options:
            if line.strip():
                raise BankError(f"{where}: unexpected text after the options: {line!r}")
        else:
            stem_lines.append(line)
    stem = "\n".join(stem_lines).strip()
    if stem.startswith("**Question:**"):
        stem = stem[len("**Question:**"):].strip()

    explanations = {}
    for line in inside.splitlines():
        m = OPTION_RE.match(line)
        if m:
            explanations[m.group(1)] = m.group(2).strip()

    return meta, stem, options, explanations, raw


def validate(path, meta, stem, options, explanations, concept_ids):
    where = str(path.relative_to(ROOT))
    problems = []
    qid = meta.get("id", "")
    if not ID_RE.match(qid):
        problems.append("id must be lowercase letters, digits and hyphens")
    elif qid != path.stem:
        problems.append(f"id '{qid}' must match the file name '{path.stem}.md'")
    date = meta.get("date")
    if date is not None and not DATE_RE.match(date):
        problems.append(f"date '{date}' must be YYYY-MM-DD")
    if meta.get("date_basis", "added") not in DATE_BASES:
        problems.append(f"date_basis must be one of {DATE_BASES}")
    concepts = meta.get("concepts")
    if not isinstance(concepts, list) or not concepts:
        problems.append("concepts must be a non-empty list like [token, attention]")
    else:
        unknown = [c for c in concepts if c not in concept_ids]
        if unknown:
            problems.append(f"unknown concept(s) {unknown}; add them to concepts.json first")
        if len(set(concepts)) != len(concepts):
            problems.append("concepts has a duplicate")
    if not stem:
        problems.append("the question text is empty")
    letters = [l for l, _ in options]
    if len(options) < 2:
        problems.append("needs at least two options written '- A. text'")
    elif letters != list(LETTERS[:len(letters)]):
        problems.append(f"options must be lettered A, B, C... in order; found {letters}")
    answer = meta.get("answer", "")
    if answer not in letters:
        problems.append(f"answer '{answer}' is not one of the option letters {letters}")
    missing = [l for l in letters if l not in explanations]
    if missing:
        problems.append(f"no explanation for option(s) {missing} inside <details>")
    if problems:
        raise BankError(where + ":\n  - " + "\n  - ".join(problems))


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


def stamp_date(path, raw, date):
    head, rest = raw[4:].split("\n---\n", 1)
    lines = [l for l in head.splitlines() if not l.startswith(("date:", "date_basis:"))]
    at = next((i + 1 for i, l in enumerate(lines) if l.startswith("id:")), 0)
    lines[at:at] = [f"date: {date}", "date_basis: added"]
    path.write_text("---\n" + "\n".join(lines) + "\n---\n" + rest, encoding="utf-8")


# ---------------------------------------------------------------- rendering

def render_concepts(vocab, questions):
    by_concept = {}
    for q in questions:
        for c in q["concepts"]:
            by_concept.setdefault(c, []).append(q)
    out = [
        "# Concepts",
        "",
        "<!-- Generated by tools/build.py from concepts.json. Edit concepts.json, not this file. -->",
        "",
        f"Every question is tagged with one or more of these {sum(len(g['concepts']) for g in vocab['groups'])} concepts. "
        "The first tag on a question is the concept it tests most directly. "
        "Counts include every question that carries the tag.",
        "",
        "Jump to a group: " + " | ".join(f"[{g['label']}](#{slug(g['label'])})" for g in vocab["groups"]),
        "",
    ]
    for g in vocab["groups"]:
        out += [f"## {g['label']}", "", "| Concept | Tag | Questions | What it means |", "|---|---|---|---|"]
        for c in g["concepts"]:
            n = len(by_concept.get(c["id"], []))
            out.append(f"| [{c['label']}](#{c['id']}) | `{c['id']}` | {n} | {c['definition']} |")
        out.append("")
    out += ["## Questions by concept", ""]
    for g in vocab["groups"]:
        for c in g["concepts"]:
            qs = sorted(by_concept.get(c["id"], []), key=lambda q: (q["date"], q["id"]))
            out += [f'<a id="{c["id"]}"></a>', "", f"### {c['label']}", "",
                    f"Tag `{c['id']}`. {c['definition']}", ""]
            if not qs:
                out += ["No questions yet.", ""]
                continue
            for q in qs:
                out.append(f"- {q['date']} -- [{q['id']}]({q['path']}): {shorten(q['question'])}")
            out.append("")
    return "\n".join(out)


def render_index(questions):
    groups = {}
    for q in questions:
        folder = str(Path(q["path"]).parent.relative_to("questions"))
        groups.setdefault(folder, []).append(q)
    out = [
        "# Questions by date",
        "",
        "<!-- Generated by tools/build.py. -->",
        "",
        "Each folder holds the questions from one class session (dated the day the material was "
        "discussed) or questions added straight to this repository (dated the day they were added).",
        "",
        "| Date | Folder | Source | Questions |",
        "|---|---|---|---|",
    ]
    for folder, qs in sorted(groups.items()):
        dates = sorted({q["date"] for q in qs})
        sources = sorted({q["source"] for q in qs if q["source"]})
        out.append(f"| {', '.join(dates)} | [{folder}]({folder}/) | {'; '.join(sources) or '-'} | {len(qs)} |")
    out += ["", f"Total: {len(questions)} questions.", ""]
    return "\n".join(out)


def slug(text):
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).replace(" ", "-")


def shorten(text, n=110):
    text = " ".join(text.split())
    return text if len(text) <= n else text[:n - 3].rstrip() + "..."


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate and compare; write nothing")
    ap.add_argument("--fill-dates", action="store_true", help="stamp missing dates into question files")
    args = ap.parse_args()

    vocab = json.loads(CONCEPTS_JSON.read_text(encoding="utf-8"))
    concept_ids = [c["id"] for g in vocab["groups"] for c in g["concepts"]]
    dupes = {c for c in concept_ids if concept_ids.count(c) > 1}
    if dupes:
        sys.exit(f"concepts.json: duplicate concept id(s) {sorted(dupes)}")
    bad = [c for c in concept_ids if not ID_RE.match(c)]
    if bad:
        sys.exit(f"concepts.json: ids must be lowercase-with-hyphens: {bad}")

    errors, questions, seen = [], [], {}
    for path in sorted(QUESTIONS.rglob("*.md")):
        if path.name.upper() == "README.MD" or path.name.startswith("_"):
            continue
        try:
            meta, stem, options, explanations, raw = parse_question(path)
            validate(path, meta, stem, options, explanations, set(concept_ids))
        except BankError as e:
            errors.append(str(e))
            continue
        qid = meta["id"]
        if qid in seen:
            errors.append(f"{path.relative_to(ROOT)}: id '{qid}' is also used by {seen[qid]}")
            continue
        seen[qid] = path.relative_to(ROOT)
        if not meta.get("date"):
            if args.check:
                errors.append(f"{path.relative_to(ROOT)}: no date (run tools/build.py --fill-dates)")
                continue
            if args.fill_dates:
                meta["date"], meta["date_basis"] = date_first_added(path), "added"
                stamp_date(path, raw, meta["date"])
                print(f"dated {path.relative_to(ROOT)} {meta['date']} (added)")
            else:
                errors.append(f"{path.relative_to(ROOT)}: no date (add 'date: YYYY-MM-DD' or run with --fill-dates)")
                continue
        questions.append({
            "id": qid,
            "date": meta["date"],
            "date_basis": meta.get("date_basis", "added"),
            "session": int(meta["session"]) if str(meta.get("session", "")).isdigit() else None,
            "source": meta.get("source", ""),
            "concepts": meta["concepts"],
            "level": meta.get("level") or None,
            "question": stem,
            "options": [{"letter": l, "text": t, "correct": l == meta["answer"],
                         "explanation": explanations[l]} for l, t in options],
            "answer": meta["answer"],
            "path": path.relative_to(ROOT).as_posix(),
        })

    if errors:
        print(f"{len(errors)} problem(s):\n", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)

    questions.sort(key=lambda q: (q["date"], q["id"]))
    outputs = {
        OUT_JSON: json.dumps({
            "about": "Generated by tools/build.py from questions/**/*.md. Do not edit by hand.",
            "count": len(questions),
            "concepts": [dict(c, group=g["id"]) for g in vocab["groups"] for c in g["concepts"]],
            "questions": questions,
        }, indent=1, ensure_ascii=False) + "\n",
        OUT_CONCEPTS: render_concepts(vocab, questions),
        OUT_INDEX: render_index(questions),
    }
    stale = [p for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    if args.check:
        if stale:
            sys.exit("out of date (run python3 tools/build.py): " + ", ".join(str(p.relative_to(ROOT)) for p in stale))
        print(f"ok: {len(questions)} questions, {len(concept_ids)} concepts, generated files current")
        return
    for p in stale:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(outputs[p], encoding="utf-8")
    print(f"ok: {len(questions)} questions, {len(concept_ids)} concepts; "
          f"rewrote {len(stale)} generated file(s)")


if __name__ == "__main__":
    main()
