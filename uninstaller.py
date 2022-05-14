import os

# todo: python 3.7 and 3.8 doesn't have this module, please update!
import winreg

print("""
    =====================================================================
    ======                POWFU - FILE ORGANIZER                   ======
    ======                       Uninstaller                       ======
    =====================================================================
    """)


def delete_key(key, value):
    reg_connector = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    reg_key = winreg.OpenKeyEx(reg_connector, 'Directory/Background/shell', 0, winreg.KEY_READ)
    with reg_key:
        try:
            if value is None:
                winreg.DeleteKey(reg_key, key)
                winreg.CloseKey(reg_key)
            os.unlink(os.path.join("C:", "Program Files", "PowFu - File Organizer"))
        except WindowsError as we:
            print(f"Something went wrong!\n{we}")
