#!/usr/bin/env python3.13
"""Phase 2/9: apply 01_readonly_login.sql + 02_tenant_views.sql as SA, for
one target database. Builds the server-side wall -- read-only login with
no base-table grants, plus SESSION_CONTEXT-scoped `t.` views (PLAN.md
golden rule 3).

chatbot_ro is a SERVER-level login (CREATE LOGIN is instance-wide, not
per-database) shared across every client database on this one SQL Server
instance -- there's exactly one such login, not one per client. Its
password lives at the shared work/ro_password.txt (NOT per-client) and is
generated once, then reused on every subsequent run (for chatbot_db2,
chatbot_db3, ...) so applying the wall to a new client never rotates the
password out from under an already-configured one."""
import argparse
import os
import re
import secrets
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORK_DIR = REPO_ROOT / "work"
DB_DIR = REPO_ROOT / "db"
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "setup"))

import pymssql  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_connect  # noqa: E402

GO_SPLIT = re.compile(r"^\s*GO\s*$", re.IGNORECASE | re.MULTILINE)


def log(msg):
    print(msg, flush=True)


def connect(db_name):
    return db_connect.sa_connect(database=db_name, autocommit=True, timeout=60)


def run_script(cur, text, replacements):
    for key, value in replacements.items():
        text = text.replace(key, value)
    for batch in GO_SPLIT.split(text):
        batch = batch.strip()
        if batch:
            cur.execute(batch)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-name", default="chatbot_db")
    args = parser.parse_args()
    db_name = args.db_name

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    pw_path = WORK_DIR / "ro_password.txt"
    if pw_path.exists():
        password = pw_path.read_text().strip()
        log(f"reusing existing chatbot_ro password from {pw_path}")
    else:
        password = secrets.token_urlsafe(18) + "aA1!"
        pw_path.write_text(password)
        log(f"generated new chatbot_ro password, written to {pw_path}")

    conn = connect(db_name)
    cur = conn.cursor()

    log(f"[{db_name}] applying 01_readonly_login.sql (chatbot_ro login, no base-table grants)")
    run_script(cur, (DB_DIR / "01_readonly_login.sql").read_text(encoding="utf-8"), {
        "__CHATBOT_RO_PASSWORD__": password,
        "__DB_NAME__": db_name,
    })

    log(f"[{db_name}] applying 02_tenant_views.sql (schema t, SESSION_CONTEXT-scoped views)")
    run_script(cur, (DB_DIR / "02_tenant_views.sql").read_text(encoding="utf-8"), {
        "__DB_NAME__": db_name,
    })

    cur.execute("SELECT COUNT(*) FROM sys.views WHERE schema_id = SCHEMA_ID('t')")
    view_count = cur.fetchone()[0]
    log(f"[{db_name}] schema t has {view_count} views")
    conn.close()


if __name__ == "__main__":
    main()
