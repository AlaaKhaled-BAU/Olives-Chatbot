#!/usr/bin/env python3.13
"""C5: build work/<client>/docs.sqlite from docs_corpus/ (run
04_assemble_docs_corpus.py first so the symlinks exist). Pure filesystem +
sqlite -- no DB connection needed, unlike 02/03. Re-run whenever the corpus
content or the client roster (clients/*.yaml) changes; it fully replaces
the previous index each time (core.docs.build_index drops and recreates
the table), so it's always safe to re-run."""
import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from core import docs  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", required=True)
    args = parser.parse_args()

    if not docs.CORPUS_DIR.exists():
        print(f"[index_docs] {docs.CORPUS_DIR} does not exist -- run "
              f"04_assemble_docs_corpus.py first", file=sys.stderr)
        sys.exit(1)

    result = docs.build_index(args.client)
    print(f"[index_docs] {args.client}: indexed {result['indexed']} chunk(s), "
          f"excluded {result['excluded']} (named another client) -> {docs.db_path(args.client)}")


if __name__ == "__main__":
    main()
