# -*- mode: python -*-

block_cipher = None


a = Analysis(['wx_테트리스.py'],
             pathex=['C:\\stock\\0x29 python강의\\pybasic5\\quiz'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='wx_테트리스',
          debug=False,
          strip=False,
          upx=True,
          console=True )
