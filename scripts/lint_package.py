#!/usr/bin/env python3
"""Lint a generated youtube-storytelling package (markdown).

Checks the mechanical items of references/audit-checklist.md. It cannot judge
truth or safety; it catches the failures that are cheap to detect: missing
sections, a broken spine, beats with no provenance, unknown ledger ids,
kill-list titles, over-long titles or spoken lines, teaching-example
contamination, and instruction-like text carried into the output.

Standard library only. Python 3.8+.

Usage:
    python scripts/lint_package.py package.md
    python scripts/lint_package.py short.md --format short
    python scripts/lint_package.py package.md --strict      # warnings and open GAPs fail
    python scripts/lint_package.py package.md --allow helmet --json

Exit code 0 = no errors, 1 = errors (or warnings/open GAPs under --strict),
2 = usage or file error.
"""
import argparse
import json
import re
import sys

TITLE_MAX = 100
THUMB_WORDS_MAX = 6
KILL_LIST = [r"\bvlog\b", r"must[- ]watch", r"you won'?t believe", r"\bpart 1\b", r"व्लॉग"]
VIEWS_MOTIVE = re.compile(
    r"\b(views?|algorithm|subscribers?|go viral|viral|monetiz\w*|grow (my )?channel|"
    r"CTR|watch ?time|clout)\b", re.I)
OUTCOME_WORDS = re.compile(r"\b(survived|made it|i did it|completed|won)\b", re.I)
CONTAMINATION = {
    "narmada": r"narmada", "parikrama": r"parikrama", "longest train": r"longest[- ]train",
    "delhi-to-london": r"delhi[- ]to[- ]london", "100 days of dreaming": r"100 days of dreaming",
    "helmet": r"helmet", "harsh gujral": r"harsh gujral",
    "ice-cream statue": r"ice[- ]cream statue", "sensory deprivation": r"sensory[- ]deprivation",
    "wi-fi extender": r"wi-?fi extender", "ration shop": r"ration[- ]shop",
    "solar roof": r"solar roof", "dustbin": r"dustbin", "sleeper coach": r"sleeper coach",
}
INJECTION = re.compile(
    r"(ignore|disregard) (all |any |the )?(previous|prior|above|earlier)? ?(instructions|rules)|"
    r"\bsystem prompt\b|\byou are now\b|^\s*system\s*:", re.I | re.M)
WALK_HOME = re.compile(
    r"\b(walk(ed|s)?|went|drove|headed|came|going|go) (back )?home\b|thanks for watching|"
    r"see you (in the )?next|\bthe end\b", re.I)
SRC_CELL = re.compile(r"^(F\d+(\s*[,;]\s*F\d+)*|STAGE|GAP)$", re.I)
SPINE_SHAPE = re.compile(
    r"\bwhen\b.*\bwants?\b.*\bbut\b.*(\bleaves?\b|\bleft\b|belief to watch for)", re.I | re.S)


class Finding:
    def __init__(self, level, code, msg, line=None):
        self.level, self.code, self.msg, self.line = level, code, msg, line

    def as_dict(self):
        return {"level": self.level, "code": self.code, "message": self.msg, "line": self.line}

    def __str__(self):
        where = f" (line {self.line})" if self.line else ""
        return f"{self.level:5s} [{self.code}] {self.msg}{where}"


class Doc:
    def __init__(self, text):
        self.lines = text.splitlines()
        self.heads = []
        for i, ln in enumerate(self.lines):
            m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", ln)
            if m:
                self.heads.append((i, len(m.group(1)), m.group(2)))

    def sections(self, pattern):
        out = []
        for k, (i, lvl, title) in enumerate(self.heads):
            if not re.search(pattern, title, re.I):
                continue
            end = len(self.lines)
            for (j, l2, _t) in self.heads[k + 1:]:
                if l2 <= lvl:
                    end = j
                    break
            out.append((title, i, "\n".join(self.lines[i + 1:end])))
        return out

    def first(self, pattern):
        s = self.sections(pattern)
        return s[0] if s else None


def body_text(text):
    return "\n".join(l for l in text.splitlines() if l.strip() and not l.strip().startswith("<!--"))


def list_items(text):
    items = []
    for l in text.splitlines():
        m = re.match(r"^\s*(?:\d+[.)]|[-*])\s+(.*\S)\s*$", l)
        if m:
            items.append(m.group(1))
    return items


def parse_table(doc, need_col):
    L = doc.lines
    for i, ln in enumerate(L):
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if not any(need_col.lower() == c.lower() or need_col.lower() in c.lower() for c in cells):
            continue
        rows, j = [], i + 2
        while j < len(L) and L[j].strip().startswith("|"):
            rows.append((j + 1, [c.strip() for c in L[j].strip().strip("|").split("|")]))
            j += 1
        return cells, rows
    return None, []


def sentences(text):
    text = re.sub(r"\[(GAP|STAGE)[^\]]*\]", " ", text)
    text = re.sub(r"[*_`>]", "", text)
    out = []
    for para in text.splitlines():
        p = para.strip()
        if not p or p.startswith(("#", "(", "|", "<!--")):
            continue
        for s in re.split(r"(?<=[.!?\u2026])\s+", p):
            if s.strip():
                out.append(s.strip())
    return out


def lint(text, fmt, max_words, allow):
    F = []
    doc = Doc(text)
    add = lambda lvl, code, msg, line=None: F.append(Finding(lvl, code, msg, line))

    if fmt == "auto":
        first_head = doc.heads[0][2] if doc.heads else ""
        fmt = "short" if re.search(r"shorts?\s+brief", first_head, re.I) else "long"
    if max_words is None:
        max_words = 12 if fmt == "short" else 18

    required = ([("first frame", "First frame"), ("question", "Question"),
                 ("last frame", "Last frame"), ("spoken", "Spoken lines")]
                if fmt == "short" else
                [("title", "Titles"), ("thumbnail", "Thumbnail"), ("spine", "Spine"),
                 ("^why", "Why"), ("spoken", "Spoken script"), ("open items", "Open items")])

    secs = {}
    for pat, label in required:
        s = doc.first(pat)
        if s is None:
            add("ERROR", "missing-section", f"no '{label}' section")
        elif not body_text(s[2]).strip():
            add("ERROR", "empty-section", f"'{label}' section is empty", s[1] + 1)
        secs[label] = s

    sp = secs.get("Spine")
    if sp and body_text(sp[2]) and not SPINE_SHAPE.search(sp[2]):
        add("ERROR", "spine-shape",
            "spine must read: When [x] wants [y] but [z] stands in the way, they [..], and leave [..] "
            "(prospective: 'the belief to watch for')", sp[1] + 1)

    mode_prospective = bool(re.search(r"mode\s*[—:\-]?\s*prospective|^prospective\b", text, re.I | re.M))

    ti = secs.get("Titles")
    if ti:
        items = list_items(ti[2])
        if not 3 <= len(items) <= 5:
            add("ERROR", "title-count", f"expected 3-5 titles, found {len(items)}", ti[1] + 1)
        for n, t in enumerate(items, 1):
            if len(t) > TITLE_MAX:
                add("ERROR", "title-length", f"title {n} is {len(t)} characters (max {TITLE_MAX})", ti[1] + 1)
            for k in KILL_LIST:
                if re.search(k, t, re.I):
                    add("ERROR", "title-kill-list", f"title {n} uses a kill-list phrase: {t[:60]}", ti[1] + 1)
                    break
            if mode_prospective and OUTCOME_WORDS.search(t):
                add("WARN", "title-outcome", f"title {n} may claim an outcome in a prospective package", ti[1] + 1)

    wh = secs.get("Why")
    if wh and body_text(wh[2]):
        why = body_text(wh[2])
        if re.search(r"\[GAP", why):
            add("WARN", "why-gap", "Why is a GAP, so the opening contract is unmet until the creator answers", wh[1] + 1)
        elif VIEWS_MOTIVE.search(why):
            add("ERROR", "why-views", "Why reads as a views/algorithm motive, not a human one", wh[1] + 1)

    if fmt == "long":
        header, rows = parse_table(doc, "Src")
        ledger = doc.first(r"ledger")
        ledger_ids = set(re.findall(r"^\s*(?:[-*]\s*)?(F\d+)\b", ledger[2], re.M)) if ledger else set()
        if header is None:
            add("ERROR", "no-beat-table", "no beat table with a 'Src' column")
        else:
            hl = [h.lower() for h in header]
            src_i = next(i for i, h in enumerate(hl) if "src" in h)
            safety_i = next((i for i, h in enumerate(hl) if "safety" in h), None)
            if not rows:
                add("ERROR", "empty-beat-table", "beat table has no rows")
            for ln, cells in rows:
                src = cells[src_i].strip() if src_i < len(cells) else ""
                if not src:
                    add("ERROR", "no-provenance", "beat has no Src (F#, STAGE, or GAP)", ln)
                    continue
                if not SRC_CELL.match(src):
                    add("ERROR", "bad-provenance", f"Src '{src}' is not F#, STAGE, or GAP", ln)
                    continue
                for fid in re.findall(r"F\d+", src, re.I):
                    if fid.upper() not in ledger_ids:
                        add("ERROR", "unknown-ledger-id", f"{fid} is cited but not in a 'Fact ledger' section", ln)
                if src.upper() == "STAGE" and safety_i is not None:
                    if safety_i >= len(cells) or not cells[safety_i].strip():
                        add("ERROR", "stage-no-safety", "STAGE beat has no safety line", ln)

    oi = doc.first(r"open items")
    oi_text = body_text(oi[2]) if oi else ""
    outside = "\n".join(
        l for i, l in enumerate(doc.lines)
        if not (oi and oi[1] < i <= oi[1] + len(oi[2].splitlines())))
    inline = re.findall(r"\[(GAP|STAGE)\b[^\]]*\]", outside)
    if inline and not re.search(r"\S", re.sub(r"(?im)^\s*[-*]?\s*[^:\n]*:\s*(none)?\s*$", "", oi_text)):
        add("ERROR", "open-items-missing", f"{len(inline)} inline GAP/STAGE marker(s) but Open items is empty")
    gap_count = len(re.findall(r"\[GAP\b", text))
    if gap_count:
        add("INFO", "open-gaps", f"{gap_count} GAP placeholder(s) remain; the creator must fill them")

    sp_sec = secs.get("Spoken script") or secs.get("Spoken lines")
    if sp_sec:
        for s in sentences(sp_sec[2]):
            n = len(s.split())
            if n > max_words:
                add("WARN", "spoken-line-length", f"{n} words (cap {max_words}): {s[:60]}...", sp_sec[1] + 1)

    if fmt == "long":
        cut = doc.first(r"change.*cut|^cut$")
        if cut and WALK_HOME.search(cut[2]):
            add("WARN", "ending-walks-home", "ending may not cut at the payoff (walks home / thanks for watching)", cut[1] + 1)

    m = re.search(r"text on thumb\w*[^:\n—-]*[:—-]\s*(.*)", text, re.I)
    if m:
        t = re.sub(r"\(.*?\)", "", m.group(1)).strip()
        if t and not t.startswith("[GAP") and len(t.split()) > THUMB_WORDS_MAX:
            add("WARN", "thumb-text", f"thumbnail text is {len(t.split())} words (max {THUMB_WORDS_MAX})")

    for name, pat in CONTAMINATION.items():
        if name in allow:
            continue
        if re.search(pat, text, re.I):
            add("WARN", "contamination", f"teaching-example term '{name}' appears; use --allow if the user supplied it")
    if INJECTION.search(text):
        add("WARN", "injection-text", "instruction-like text appears in the package; check it was not carried in from pasted notes")
    return F, fmt


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("file")
    ap.add_argument("--format", choices=["auto", "long", "short"], default="auto")
    ap.add_argument("--max-words", type=int, default=None, help="spoken-line cap (default 18 long, 12 short)")
    ap.add_argument("--allow", action="append", default=[], help="contamination term the user supplied (repeatable)")
    ap.add_argument("--strict", action="store_true", help="warnings and open GAPs count as failures")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        text = open(a.file, encoding="utf-8").read()
    except OSError as e:
        print(f"cannot read {a.file}: {e}", file=sys.stderr)
        return 2
    findings, fmt = lint(text, a.format, a.max_words, {x.lower() for x in a.allow})
    errors = [f for f in findings if f.level == "ERROR"]
    warns = [f for f in findings if f.level == "WARN"]
    gaps = [f for f in findings if f.code == "open-gaps"]
    failed = bool(errors) or (a.strict and (bool(warns) or bool(gaps)))
    if a.json:
        print(json.dumps({"format": fmt, "passed": not failed, "findings": [f.as_dict() for f in findings]}, indent=2))
    else:
        for f in findings:
            print(f)
        print(f"\n{a.file}: {len(errors)} error(s), {len(warns)} warning(s) [{fmt}]"
              f" -> {'FAIL' if failed else 'PASS'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
