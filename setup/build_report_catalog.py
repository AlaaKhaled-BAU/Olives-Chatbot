"""Build work/<client>/report_catalog.json from vault Rpt_* procedure metadata only."""
import argparse
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import config, vault  # noqa: E402

_RPT_RE = re.compile(r"^Rpt_|^RPT_", re.IGNORECASE)


def _wiki_list(items) -> list:
    if not items:
        return []
    if isinstance(items, str):
        items = [items]
    out = []
    for item in items:
        out.append(vault._wiki_name(str(item)))
    return out


def build_catalog(client: str) -> list:
    cards = []
    for n in vault.NOTES_INDEX:
        if n["db"] != "Olives_BO" or n["subdir"] != "Procedures":
            continue
        name = n["fname"].replace(".md", "")
        if not _RPT_RE.match(name):
            continue
        try:
            content = Path(n["path"]).read_text(encoding="utf-8")
        except OSError:
            continue
        fm = vault.parse_frontmatter(content)
        purpose, _ = vault.extract_section(content, "Purpose")
        params_body, _ = vault.extract_section(content, "Parameters")
        tables_read = _wiki_list(fm.get("reads_from"))
        when, _ = vault.extract_section(content, ["When to Run This", "When to Run"])
        cards.append({
            "name": fm.get("name", name),
            "purpose": (purpose or "").strip()[:500],
            "params": (params_body or "").strip()[:500],
            "tables": tables_read,
            "when_to_run": (when or "").strip()[:300],
            "vault_path": n["rel"],
        })
    return sorted(cards, key=lambda c: c["name"])


def main():
    parser = argparse.ArgumentParser(description="Build report_catalog.json from vault Rpt_* notes")
    parser.add_argument("--client", required=True)
    args = parser.parse_args()
    cards = build_catalog(args.client)
    out = config.work_dir(args.client) / "report_catalog.json"
    out.write_text(json.dumps(cards, indent=2, ensure_ascii=False))
    print(f"Wrote {len(cards)} report cards to {out}")


if __name__ == "__main__":
    main()
