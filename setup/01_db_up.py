#!/usr/bin/env python3.13
"""Phase 1: restore a client .bak into SQL Server.

Modes:
  native (default) — production-like instance (DB_PORT, usually 1433). Uses
    setup/restore_native.py and DB_SA_* from .env.
  docker — drift-tool scratch container on port 14330 (legacy dev).
"""
import argparse
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "setup"))

DEFAULT_BAK = (
    REPO_ROOT
    / "data"
    / "db-snapshots"
    / "backup test"
    / "morec"
    / "Olives_BO.bak"
)


def log(msg):
    print(msg, flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("native", "docker"), default="native")
    parser.add_argument("--bak", default=str(DEFAULT_BAK))
    parser.add_argument("--db-name", default="Olives_BO")
    args = parser.parse_args()

    if args.mode == "docker":
        drift_root = Path(
            os.environ.get("DRIFT_TOOL_ROOT", "/media/alaa/data/olives/apps/drift-tool")
        )
        sys.path.insert(0, str(drift_root))
        from drift import docker_mgmt, restore, config  # noqa: E402

        docker_mgmt.ensure_running(log)
        info = restore.restore_backup(Path(args.bak), args.db_name, log)
        log(f"{args.db_name} ready: {info}")
        log(f"connect: 127.0.0.1:{config.HOST_PORT} as {config.SA_USER}")
        return

    import db_connect  # noqa: E402
    import restore_native  # noqa: E402

    log(
        f"native SQL Server @ {db_connect.sa_host()}:{db_connect.sa_port()} "
        f"as {db_connect.sa_user()}"
    )
    info = restore_native.restore_backup(Path(args.bak), args.db_name, log)
    log(f"{args.db_name} ready: {info}")
    log(
        f"next: python3.13 setup/native_bootstrap.py --client morec --db-name {args.db_name}"
    )


if __name__ == "__main__":
    main()
