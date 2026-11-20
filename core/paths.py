"""Repo root when running from source. Folder of the exe when frozen.

Python startup is unchanged: this file lives in core/, so parent.parent is
the repository root. A PyInstaller exe uses the folder that contains the exe,
which is where .env, clients/, prompts/, and work/ sit.
"""
import sys
from pathlib import Path


def app_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS")).resolve()
    return Path(__file__).resolve().parent.parent
