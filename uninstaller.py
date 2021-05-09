import os, time, winreg, subprocess
print("=====================================================================")
print("======                POWFU - FILE ORGANIZER                   ======")   
print("======                       Uninstaller                       ======") 
print("=====================================================================")



def delete_key(key, value): 
    reg_connector = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    reg_key = winreg.OpenKeyEx(reg_connector, r'Directory\Background\shell', 0, winreg.KEY_READ)
    with reg_key:   
        try:
            if value == None:
                winreg.DeleteKey(reg_key, key)
                winreg.CloseKey(reg_key)
            os.unlink(os.path.join("C:", "Program Files", "PowFu - File Organizer"))
        except WindowsError as we:
            print("Something went wrong!\n%s"%we)