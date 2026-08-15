#!/usr/bin/env python3.13
"""Phase 10 (optional): symlink the already-converted docs into
docs_corpus/ (gitignored -- a derived/assembled view, not new content).
No MinerU needed for these: per PLAN.md's own repo inventory (client-chatbot/PLAN.md
Sec 1.5.A), the user-guide and SQL-doc PDFs/DOCXs were already converted
to markdown by hand before this project started."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "docs_corpus"

FILES = {
    # Lane A: headed copy (setup/inject_doc_headings.py) — chunker needs # headings.
    "user_guide.md": REPO_ROOT / "knowledge" / "guide-headed" / "user_guide.md",
    "sql_documentation.md": REPO_ROOT / "knowledge" / "reference" / "Olives SQL_Documentation.md",
    "tables_summary.md": REPO_ROOT / "knowledge" / "reference" / "tables summary.md",
    # C5: support-agent/system_options_guide.md over the repo-root "system
    # option explained.md" -- same 754 options, but this one is already
    # organized under real markdown headings (category per section), which
    # is what docs.py's chunk-by-heading indexer needs; the root file is one
    # flat pipe-table with no heading structure to chunk on.
    "system_options_guide.md": REPO_ROOT / "knowledge" / "support-agent" / "system_options_guide.md",
    # database_mapping.md deliberately excluded -- it's a support-STAFF
    # runbook ("diagnose data errors... configure manual database fixes"),
    # not end-user documentation. Same exclusion spirit as procedures.md.
}
DIRS = {
    "back-office": REPO_ROOT / "knowledge" / "guide-headed" / "back-office",
    "front-office": REPO_ROOT / "knowledge" / "guide-headed" / "front-office",
}


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    missing = []
    for link_name, target in {**FILES, **DIRS}.items():
        if not target.exists():
            missing.append(str(target))
            continue
        link = OUT_DIR / link_name
        if link.is_symlink() or link.exists():
            link.unlink()
        link.symlink_to(target)
        print(f"linked {link_name} -> {target}")
    if missing:
        print(f"WARNING: {len(missing)} source(s) not found: {missing}")


if __name__ == "__main__":
    main()
