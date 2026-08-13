#!/usr/bin/env python3.13
"""Bootstrap an existing native SQL Server database for the chatbot.

Use when Olives_BO (or a restored client DB) already exists on the instance —
typical for production-like dev (local SQL Server / Azure Data Studio, port 1433).

Steps:
  1. Apply chatbot_ro login + tenant views (03_apply_db_sql.py)
  2. Live schema introspection (02_introspect.py)
  3. Assemble + index docs corpus (04 + 05)

Does NOT restore a .bak — use setup/01_db_up.py --mode native for that."""
import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SETUP = REPO_ROOT / "setup"


def run(cmd: list[str]):
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", default="morec")
    parser.add_argument("--db-name", default=None, help="defaults to clients/<client>.yaml db_name")
    parser.add_argument("--skip-docs", action="store_true")
    args = parser.parse_args()

    sys.path.insert(0, str(REPO_ROOT))
    from core import config as client_config  # noqa: E402

    db_name = args.db_name or client_config.load_client(args.client)["db_name"]
    py = sys.executable

    run([py, str(SETUP / "03_apply_db_sql.py"), "--db-name", db_name])
    run([py, str(SETUP / "02_introspect.py"), "--client", args.client, "--db-name", db_name])
    if not args.skip_docs:
        run([py, str(SETUP / "04_assemble_docs_corpus.py")])
        run([py, str(SETUP / "05_index_docs.py"), "--client", args.client])

    print(f"\nNative bootstrap done for client={args.client} db={db_name}")
    print(f"Connect: {db_name} @ {__import__('os').environ.get('DB_HOST', '127.0.0.1')}:{__import__('os').environ.get('DB_PORT', '1433')} as chatbot_ro")


if __name__ == "__main__":
    main()
