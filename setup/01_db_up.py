#!/usr/bin/env python3.13
"""Phase 1/9: bring up the scratch SQL Server container and restore a
client's .bak as the given db name. Reuses drift-tool's docker_mgmt +
restore modules (PLAN.md golden rule 2) -- do not reimplement
container/restore logic."""
import argparse
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DRIFT_TOOL_ROOT = Path(
    os.environ.get("DRIFT_TOOL_ROOT", "/media/alaa/data/olives/apps/drift-tool")
)
sys.path.insert(0, str(DRIFT_TOOL_ROOT))

from drift import docker_mgmt, restore, config  # noqa: E402

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
    parser.add_argument("--bak", default=str(DEFAULT_BAK))
    parser.add_argument("--db-name", default="chatbot_db")
    args = parser.parse_args()

    docker_mgmt.ensure_running(log)
    info = restore.restore_backup(Path(args.bak), args.db_name, log)
    log(f"{args.db_name} ready: {info}")
    log(f"connect: 127.0.0.1:{config.HOST_PORT} as {config.SA_USER}")


if __name__ == "__main__":
    main()
