#!/usr/bin/env python3.13
"""Lane A: generate headed markdown copies for FTS chunking.

Reads knowledge/back-office/, knowledge/front-office/, and the monolith
user guide; writes mirror trees under knowledge/guide-headed/ with ``#``
headings injected from existing numeric screen prefixes (``4.8 Customers…``,
``7.1.3 …``, ``1.5.1 …``) and ``CHAPTER N`` lines. Originals are untouched.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = REPO_ROOT / "knowledge"
OUT_ROOT = KNOWLEDGE / "guide-headed"

_NUM_PREFIX_RE = re.compile(r"^(\d+\.\d+(?:\.\d+)?)\s+(.+)$")
_CHAPTER_RE = re.compile(r"^(CHAPTER\s+\d+)\s*$", re.I)


def inject_headings(text: str) -> str:
    """Prefix ``# `` on numbered screen lines and CHAPTER lines not already headed."""
    out: list[str] = []
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            out.append(line)
            continue
        chapter = _CHAPTER_RE.match(line.strip())
        if chapter:
            out.append(f"# {chapter.group(1)}")
            continue
        numbered = _NUM_PREFIX_RE.match(line)
        if numbered:
            out.append(f"# {line}")
            continue
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def _copy_tree(src_dir: Path, dst_dir: Path) -> int:
    count = 0
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.glob("*.md")):
        headed = inject_headings(src.read_text(errors="replace"))
        (dst_dir / src.name).write_text(headed)
        count += 1
    return count


def main() -> int:
    sources = {
        OUT_ROOT / "back-office": KNOWLEDGE / "back-office",
        OUT_ROOT / "front-office": KNOWLEDGE / "front-office",
    }
    monolith_src = KNOWLEDGE / "reference" / "OLIVES USER GUIDE_2021Updated2025.md"
    monolith_dst = OUT_ROOT / "user_guide.md"

    total = 0
    for dst, src in sources.items():
        if not src.is_dir():
            print(f"[inject_doc_headings] missing {src}", file=sys.stderr)
            continue
        n = _copy_tree(src, dst)
        total += n
        print(f"[inject_doc_headings] {n} file(s) -> {dst.relative_to(REPO_ROOT)}")

    if monolith_src.exists():
        OUT_ROOT.mkdir(parents=True, exist_ok=True)
        monolith_dst.write_text(inject_headings(monolith_src.read_text(errors="replace")))
        total += 1
        print(f"[inject_doc_headings] monolith -> {monolith_dst.relative_to(REPO_ROOT)}")
    else:
        print(f"[inject_doc_headings] missing {monolith_src}", file=sys.stderr)

    print(f"[inject_doc_headings] wrote {total} headed file(s) under guide-headed/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
