# -*- mode: python ; coding: utf-8 -*

a = Analysis(
    ['server.py'],
    pathex=[],
    binaries=[],
    datas=[
    # ("nltk_data/stopwords","./llama_index/core/_static/nltk_cache/stopwords"),
    # ("nltk_data/punkt","./llama_index/core/_static/nltk_cache/punkt")
    ],
    hiddenimports=[
    'asyncpg.pgproto.pgproto',
    'scipy.special._cdflib',
    'socksio',
    'tkinter',
    'tiktoken_ext.openai_public',
    'tiktoken_ext'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='server',
)
