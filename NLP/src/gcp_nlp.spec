# -*- mode: python -*-

block_cipher = None


a = Analysis(['gcp_nlp.py'],
             pathex=['C:\\Users\\iagboola\\Documents\\NLP'],
             binaries=[],
             datas=[],
             hiddenimports=['pandas._libs.tslibs.timezones'],
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
          name='gcp_nlp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
