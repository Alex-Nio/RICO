# -*- mode: python ; coding: utf-8 -*-


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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
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