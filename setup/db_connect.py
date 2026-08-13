"""SQL Server connection settings for setup scripts (SA) and shared env helpers.

Production-like dev: native SQL Server on DB_PORT (default 1433), e.g. the local
`mssql` container or a Windows instance. Docker drift-tool scratch DB remains
available via setup/01_db_up.py --mode docker (port 14330).
"""
import os
from pathlib import Path

import pymssql

REPO_ROOT = Path(__file__).resolve().parents[1]

# Host paths mounted into the local `mssql` container at SQL_SNAPSHOT_MOUNT (/snapshots).
_SNAPSHOT_HOST_ROOTS = (
    Path("/media/alaa/data/olives/data/db-snapshots"),
    Path("/media/alaa/data/client-chatbot/data/db-snapshots"),
)


def sa_host() -> str:
    return os.environ.get("DB_HOST", "127.0.0.1")


def sa_port() -> int:
    return int(os.environ.get("DB_PORT", "1433"))


def sa_user() -> str:
    return os.environ.get("DB_SA_USER", "sa")


def sa_password() -> str:
    pw = os.environ.get("DB_SA_PASSWORD", "").strip()
    if not pw:
        raise RuntimeError(
            "DB_SA_PASSWORD is not set. Add it to .env (see .env.example)."
        )
    return pw


def sa_connect(database: str | None = None, *, as_dict: bool = False, autocommit: bool = True, **kwargs):
    return pymssql.connect(
        server=sa_host(),
        port=sa_port(),
        user=sa_user(),
        password=sa_password(),
        database=database or "master",
        autocommit=autocommit,
        login_timeout=10,
        as_dict=as_dict,
        **kwargs,
    )


def bak_to_sql_disk_path(host_bak: Path) -> str:
    """Map a host .bak path to the path SQL Server sees (RESTORE FROM DISK)."""
    host_bak = host_bak.resolve()
    mount = os.environ.get("SQL_SNAPSHOT_MOUNT", "/snapshots")
    for root in _SNAPSHOT_HOST_ROOTS:
        try:
            rel = host_bak.relative_to(root.resolve())
            return f"{mount}/{rel.as_posix()}"
        except ValueError:
            continue
  # Already a SQL Server–visible path (e.g. Windows C:\backups\...)
    return str(host_bak)
