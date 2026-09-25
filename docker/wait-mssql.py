#!/usr/bin/env python3
"""Wait until SQL Server accepts SA logins (used by build-mssql-demo.sh)."""
import os
import sys
import time

import pymssql

host = os.environ.get("DB_HOST", "127.0.0.1")
port = int(os.environ.get("DB_PORT", "1433"))
user = os.environ.get("DB_SA_USER", "sa")
password = os.environ["DB_SA_PASSWORD"]
deadline = time.time() + int(os.environ.get("MSSQL_WAIT_SECONDS", "300"))

while time.time() < deadline:
    try:
        conn = pymssql.connect(
            server=host,
            port=port,
            user=user,
            password=password,
            login_timeout=5,
        )
        conn.close()
        print(f"SQL Server ready at {host}:{port}", flush=True)
        sys.exit(0)
    except Exception as exc:  # noqa: BLE001
        print(f"  waiting… ({exc})", flush=True)
        time.sleep(5)

print("SQL Server did not become ready in time", file=sys.stderr, flush=True)
sys.exit(1)
