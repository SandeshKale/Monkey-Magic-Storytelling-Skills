#!/usr/bin/env python3
"""Validate this skill repository and optionally build a distributable zip.

Checks (errors unless marked warn):
  * SKILL.md frontmatter: allowed keys, name format, description and compatibility limits,
    no angle brackets in the description
  * exactly one SKILL.md outside evals/, and it stays under 500 lines (warn above 400)
  * every relative markdown link resolves; every references/*.md is linked from SKILL.md
  * numeric drift guard: deadlines, caps, and limits agree across files, and known
    legacy contradictions have not crept back
  * source metadata: 11-character video ids, one playlist id everywhere
  * evals/evals.json is well formed (if present)

Standard library only. Python 3.8+.

Usage:
    python scripts/validate_skill.py                 # validate the repo it lives in
    python scripts/validate_skill.py --zip           # validate, then write dist/<name>.zip
    python scripts/validate_skill.py --check-dirname # also require the folder name to equal `name`
"""
import argparse
import json
import os
import re
import sys
import zipfile
from pathlib import Path

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SKIP_DIRS = {".git", ".github", "dist", "__pycache__", "node_modules"}
ZIP_EXCLUDE_DIRS = {".git", ".github", "dist", "evals", "__pycache__", "node_modules"}
ZIP_EXCLUDE_FILES = {"README.md", "CHANGELOG.md", ".gitignore", ".DS_Store"}

# label, regex (group 1 is the value), allowed values
DRIFT = [
    ("Why deadline", r"(?i)\bwhy\b(?:(?!cold open)[^.\n]){0,40}?\bby 0:(\d\d)\b", {"30", "45"}),
    ("cold-open deadline", r"(?i)cold open(?:(?!why)[^.\n]){0,30}?\bby 0:(\d\d)\b", {"20"}),
    ("first-conflict deadline", r"first conflict by (\d:\d\d)", {"2:00"}),
    ("video-model shot cap", r"under (\d+) words per shot", {"18"}),
    ("Shorts spoken-line cap", r"(\d+) words or fewer each", {"12"}),
    ("title length cap", r"(\d+) characters (?:or fewer|maximum)", {"100"}),
]
# Contradictions that existed in v1.1. They must not reappear outside the changelog.
LEGACY = [
    "30-45 seconds", "30–45 seconds", "0:30–1:15", "1:15–2:00",
    "75 percent-plus", "max ~12 words", "At least four rasas tagged on a long-form",
]


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, "no frontmatter block"
    data, cur = {}, None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")):
            if cur is None or not isinstance(data.get(cur), dict):
                return None, f"unexpected indentation: {raw!r}"
            k, _, v = raw.strip().partition(":")
            data[cur][k.strip()] = v.strip().strip('"').strip("'")
            continue
        k, sep, v = raw.partition(":")
        if not sep:
            return None, f"cannot parse line: {raw!r}"
        k, v = k.strip(), v.strip()
        if v == "":
            data[k] = {}
            cur = k
        else:
            data[k] = v.strip('"').strip("'")
            cur = k
    return data, None


def md_files(root):
    for p in sorted(root.rglob("*.md")):
        if not (set(p.relative_to(root).parts) & SKIP_DIRS):
            yield p


def validate(root, check_dirname):
    errs, warns = [], []
    E, W = errs.append, warns.append
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md not found"], []
    text = skill_md.read_text(encoding="utf-8")

    fm, err = parse_frontmatter(text)
    if err:
        return [f"frontmatter: {err}"], []
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        E(f"unexpected frontmatter key(s): {', '.join(sorted(extra))}")
    name = fm.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or ""):
        E(f"name {name!r} must be kebab-case (lowercase letters, digits, single hyphens)")
    if len(name) > 64:
        E(f"name is {len(name)} characters (max 64)")
    if check_dirname and root.name != name:
        E(f"folder name {root.name!r} does not match name {name!r}")
    desc = fm.get("description", "")
    if not desc:
        E("description is missing")
    if len(desc) > 1024:
        E(f"description is {len(desc)} characters (max 1024)")
    if "<" in desc or ">" in desc:
        E("description must not contain angle brackets")
    if len(fm.get("compatibility", "")) > 500:
        E("compatibility exceeds 500 characters")
    meta = fm.get("metadata", {})
    if meta and not isinstance(meta, dict):
        E("metadata must be a map")
    try:  # optional stricter parse when PyYAML happens to be installed
        import yaml  # type: ignore
        yaml.safe_load(re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1))
    except ImportError:
        pass
    except Exception as e:  # noqa: BLE001
        E(f"PyYAML could not parse frontmatter: {e}")

    lines = text.count("\n") + 1
    if lines > 500:
        E(f"SKILL.md is {lines} lines (max 500)")
    elif lines > 400:
        W(f"SKILL.md is {lines} lines; consider moving detail into references/")

    others = [p for p in root.rglob("SKILL.md")
              if p != skill_md and not (set(p.relative_to(root).parts) & (SKIP_DIRS | {"evals"}))]
    if others:
        E("extra SKILL.md file(s): " + ", ".join(str(p.relative_to(root)) for p in others))

    # links
    for f in md_files(root):
        for m in re.finditer(r"\]\(([^)\s]+)\)", f.read_text(encoding="utf-8")):
            href = m.group(1)
            if re.match(r"^(https?:|mailto:|#)", href):
                continue
            target = (f.parent / href.split("#")[0]).resolve()
            if not target.exists():
                E(f"{f.relative_to(root)}: broken link {href}")
    linked = set(re.findall(r"\]\((references/[^)#\s]+\.md)\)", text))
    for p in sorted((root / "references").glob("*.md")):
        if f"references/{p.name}" not in linked:
            E(f"references/{p.name} is not linked from SKILL.md, so it will never load")

    # drift guard
    for f in md_files(root):
        rel = f.relative_to(root)
        body = f.read_text(encoding="utf-8")
        if rel.name != "CHANGELOG.md":
            for old in LEGACY:
                if old.lower() in body.lower():
                    E(f"{rel}: legacy contradictory phrase reappeared: {old!r}")
        for label, pat, allowed in DRIFT:
            for m in re.finditer(pat, body):
                if m.group(1) not in allowed:
                    E(f"{rel}: {label} is {m.group(1)!r}, canonical is {sorted(allowed)}")
    for needle in ("0:45", "100 characters", "Short 1"):
        if needle not in text:
            E(f"SKILL.md canonical numbers table no longer mentions {needle!r}")

    # source metadata
    src = root / "references" / "source-and-attribution.md"
    if src.exists():
        for vid in re.findall(r"watch\?v=([^\s|)]+)", src.read_text(encoding="utf-8")):
            if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
                E(f"source-and-attribution.md: suspicious video id {vid!r}")
    pl = set()
    for f in md_files(root):
        pl |= set(re.findall(r"playlist\?list=([A-Za-z0-9_-]+)", f.read_text(encoding="utf-8")))
    pl |= set(re.findall(r"playlist\?list=([A-Za-z0-9_-]+)", meta.get("source_playlist", "") if isinstance(meta, dict) else ""))
    if len(pl) > 1:
        E(f"more than one playlist id in use: {sorted(pl)}")

    # evals
    ev = root / "evals" / "evals.json"
    if ev.exists():
        try:
            data = json.loads(ev.read_text(encoding="utf-8"))
            if data.get("skill_name") != name:
                E("evals/evals.json skill_name does not match the skill name")
            ids = [e.get("id") for e in data.get("evals", [])]
            if not ids or len(ids) != len(set(ids)):
                E("evals/evals.json needs unique ids")
            for e in data.get("evals", []):
                for k in ("id", "prompt", "expected_output", "expectations"):
                    if k not in e:
                        E(f"eval {e.get('id')} is missing '{k}'")
        except (ValueError, AttributeError) as e:
            E(f"evals/evals.json is not valid: {e}")
    else:
        W("no evals/evals.json")
    return errs, warns


def build_zip(root, out_dir):
    name = parse_frontmatter((root / "SKILL.md").read_text(encoding="utf-8"))[0]["name"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            rel = p.relative_to(root)
            if p.is_dir() or (set(rel.parts) & ZIP_EXCLUDE_DIRS):
                continue
            if rel.name in ZIP_EXCLUDE_FILES or rel.suffix in {".pyc", ".zip"}:
                continue
            zi = zipfile.ZipInfo(f"{name}/{rel.as_posix()}", date_time=(1980, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = (0o755 if rel.parts[0] == "scripts" else 0o644) << 16
            z.writestr(zi, p.read_bytes())
    with zipfile.ZipFile(out) as z:
        skill_files = [n for n in z.namelist() if n.endswith("/SKILL.md")]
        assert skill_files == [f"{name}/SKILL.md"], skill_files
        count = len(z.namelist())
    return out, count


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", default=None, help="skill root (default: parent of scripts/)")
    ap.add_argument("--check-dirname", action="store_true")
    ap.add_argument("--zip", nargs="?", const="dist", default=None, metavar="OUT_DIR")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve() if a.root else Path(__file__).resolve().parent.parent
    errs, warns = validate(root, a.check_dirname)
    for w in warns:
        print(f"WARN  {w}")
    for e in errs:
        print(f"ERROR {e}")
    print(f"\n{root.name}: {len(errs)} error(s), {len(warns)} warning(s) -> {'FAIL' if errs else 'OK'}")
    if errs:
        return 1
    if a.zip is not None:
        out, n = build_zip(root, root / a.zip if not os.path.isabs(a.zip) else Path(a.zip))
        print(f"wrote {out} ({n} files, single SKILL.md at the archive root folder)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
