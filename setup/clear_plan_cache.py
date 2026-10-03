#!/usr/bin/env python3.13
"""One-shot purge of plan_cache for a client after semantic_version bump (I1)."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import memory


def main() -> None:
    parser = argparse.ArgumentParser(description="Delete all plan_cache rows for one client.")
    parser.add_argument("--client", required=True, help="Tenant name matching clients/<name>.yaml")
    args = parser.parse_args()
    removed = memory.clear_plan_cache(args.client)
    print(f"Removed {removed} plan_cache row(s) for client={args.client!r}")


if __name__ == "__main__":
    main()
