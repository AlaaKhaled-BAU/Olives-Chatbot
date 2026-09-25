# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from pathlib import Path

block_cipher = None
ROOT_DIR = os.path.abspath(os.getcwd())

datas = [
    (os.path.join(ROOT_DIR, 'obsidian', 'olives'), os.path.join('obsidian', 'olives')),
    (os.path.join(ROOT_DIR, 'knowledge'), 'knowledge'),
    (os.path.join(ROOT_DIR, 'prompts'), 'prompts'),
    (os.path.join(ROOT_DIR, 'clients'), 'clients'),
    (os.path.join(ROOT_DIR, 'static'), 'static'),
    (os.path.join(ROOT_DIR, 'db'), 'db'),
    (os.path.join(ROOT_DIR, 'work', '105'), os.path.join('work', '105')),
    (os.path.join(ROOT_DIR, 'work', 'ro_password.txt'), 'work'),
]

hidden_imports = [
    'uvicorn',
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    'fastapi',
    'starlette',
    'pydantic',
    'pydantic_core',
    'pymssql',
    'sqlglot',
    'sqlglot.dialects',
    'sqlglot.dialects.tsql',
    'openai',
    'yaml',
    'slowapi',
    'prometheus_client',
    'sqlite3',
]

a = Analysis(
    ['desktop_app.py'],
    pathex=[ROOT_DIR],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'matplotlib', 'numpy', 'scipy', 'pandas', 'tests', 'evals', 'sqlmcp'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='OlivesChatbot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Shows friendly status console
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
