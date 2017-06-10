# -*- mode: python -*-

block_cipher = None


a = Analysis(['현금인출기.py'],
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
          name='현금인출기',
          debug=False,
          strip=False,
          upx=True,
          console=True )
