import sys
from pathlib import Path

icon = None
if sys.platform == "win32":
    icon = 'src/resources/icon.ico'
elif sys.platform == "darwin":
    icon = 'src/resources/icon.icns'

a = Analysis(
    ['src/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[('src/resources/*', 'resources/')],
    hiddenimports=[
        'pandas', 'numpy', 'customtkinter', 'openpyxl', 'xlrd',
        'concurrent.futures', 'urllib.request', 'urllib.error'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='ProfileDorm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=icon,
    onefile=True,  # Ensure this is set to True
)

if sys.platform == "darwin":
    app = BUNDLE(
        exe,
        name='ProfileDorm.app',
        icon=icon,
        bundle_identifier='com.osasima.profiledorm',
        info_plist={
            'NSHighResolutionCapable': 'True',
            'CFBundleShortVersionString': '1.0.0',
        },
    )