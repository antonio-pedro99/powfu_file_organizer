import winreg, os, sys, shutil
"""
    This script is to install the program in Windows machine.

    Its function is to create a new Folder in C:\Program Files\ and copy the program.
    After this, create a new RegeditKey to help users to use the program by clicking on the right button.
"""

folder_name = "PowFu - File Organizer"
installation_destination = "C:\Program Files\\"
full = os.path.join(installation_destination, folder_name)


def moveFiles(file):
    """
        This is the function that move the files into their apropriete folder. 

        It also replaces duplicated files.

        Parametres : 
            File - The file to be copied as a string type.
            destination - The name of the folder where the file must be copied, as string.

        Return : This function does not return any value.
    """
    source = os.path.join(os.getcwd(), "windows-executable", file)
    try:
        if file not in os.listdir(full):
            shutil.copy(source, full)

    except BaseException as e:
        print("Something went wrong with %s"%e)


def createFolder():
    try:
        if folder_name not in os.listdir(installation_destination):
            os.makedirs(full)
        else:
            pass
    except BaseException as e:
        pass

def create_root_key():
    try:
        new_key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, r"Directory\\Background\\shell", 0, winreg.KEY_CREATE_SUB_KEY)
        key = winreg.CreateKey(new_key,  r"powfu")
        winreg.SetValue(key, "", winreg.REG_SZ, "Organize with PowFu - File Organizer")
        sub_key = winreg.CreateKey(key, r"command")
        winreg.SetValue(sub_key, "", winreg.REG_SZ, os.path.join(full, "powfu.exe"))
        winreg.CloseKey(new_key)
        winreg.CloseKey(key)
        winreg.CloseKey(sub_key)
        
    except WindowsError as we:
        raise "Ops! Somthing went wrong"

if __name__ == '__main__':
    createFolder()
    moveFiles(os.path.join("powfu.exe"))
    create_root_key()


