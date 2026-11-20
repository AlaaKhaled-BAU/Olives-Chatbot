# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['windows_packaging/exe_entry.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('clients/105.yaml', 'clients'),
        ('prompts', 'prompts'),
        ('static', 'static'),
        ('knowledge/report_templates', 'knowledge/report_templates'),
        ('knowledge/reference/tables summary.md', 'knowledge/reference'),
        ('work/ro_password.txt', 'work'),
        ('work/105/schema_cache.json', 'work/105'),
        ('work/105/docs.sqlite', 'work/105'),
        ('work/105/vault_cards.sqlite', 'work/105'),
        ('work/105/module_map.json', 'work/105'),
        ('work/105/report_catalog.json', 'work/105'),
    ],
    hiddenimports=['uvicorn.logging', 'uvicorn.loops.auto', 'uvicorn.protocols.http.auto', 'uvicorn.lifespan.on', 'pymssql', 'api.server', 'core.paths'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy', 'pandas', 'IPython', 'pytest', 'matplotlib', 'scipy', 'tkinter'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='OlivesChatbot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
