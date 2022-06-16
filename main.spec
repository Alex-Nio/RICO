# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.building.datastruct import TOC

block_cipher = None
added_files = [
    ('C:/Users/Nio/AppData/Local/Programs/Python/Python310/Lib/site-packages/vosk/,/vosk/'),
    ('C:/Users/Nio/Desktop/Работа/Code all/В работе/RICO/model_small',/model_small/),
    ('C:/Users/Nio/Desktop/Работа/Code all/В работе/RICO/omegaconf',/omegaconf/),
    ('C:/Users/Nio/Desktop/Работа/Code all/В работе/RICO/antlr4',/antlr4/),
    ('C:/Users/Nio/Desktop/Работа/Code all/В работе/RICO/yaml',/yaml/)
]
a = Analysis(['main.py'],
             pathex=['C:\\Users\\Nio\\Desktop\\Работа\\Code all\\В работе\\RICO'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
to_remove = ["_C", "_AES", "_ARC4", "_DES", "_DES3", "_SHA256", "_counter"]
for b in a.binaries:
    found = any(
        f'{crypto}.cp310-win_amd64.pyd' in b[1]
        for crypto in to_remove
    )
    if found:
        print(f"Removing {b[1]}")
        a.binaries.remove(b)
x = 'cp310-win_amd64.pyd'
datas_upd = TOC()

for d in a.datas:
    if x not in d[0] and x not in d[1]:
        datas_upd.append(d)

a.datas = datas_upd
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='RICO',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , uac_admin=True, icon='/icon.ico')