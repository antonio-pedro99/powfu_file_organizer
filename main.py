"""
    This a utility script to help users organize their files without stress.
    It goes through a folder and check all files and organize them per type.
    Modules Used:

    - shutil: provides utilities and functions for copying, archiving files and directory's tree.
    - os: allows us to work with directories, files and so on.
    - sys: This module provides access to some objects and functions used by the interpreter and to  interact with the system.
"""

import getpass
import os
import shutil
import time

import extensions as exts

main_folder = "PowFu - File Organizer"
extensions = exts.get_all()

folders_name = [
    "Musics",
    "Images",
    "Videos",
    "Documents",
    "Zippers",
    "Programs",
    "Others"]

# don't worry, python don't need to use this slash '\'
# because the compiler (on windows) convert this '/' to this '\'
folder_exceptions = [
    "C:/",
    "C:/Windows",
    "C:/Windows/System32",
    "C:/Program Files",
    "C:/Program Files (x86)",
    "C:/Users",
    f"C:/Users/{getpass.getuser()}",
    f"C:/Users/{getpass.getuser()}/Desktop"
]

def create_one(_extensions_found):
    i = 0
    for extension in _extensions_found:
        if exts.is_music(extension):
            i = 0
        elif exts.is_image(extension):
            i = 1
        elif exts.is_video(extension):
            i = 2
        elif exts.is_doc(extension):
            i = 3
        elif exts.is_compacted(extension):
            i = 4
        elif exts.is_executable(extension):
            i = 5
        else:
            i = 6
        if folders_name[i] not in os.listdir(os.getcwd()):
            os.makedirs(folders_name[i])

def create_folders():
    """
        This is the function that creates a new folder named as 
        PowFu- files organizer if the script was never ran in the context folder.

        If the script has already ran into this folder or there are no files except "the program",
        it will inform the user that there are no files to organize.

        Parametres : This function does not receive any parametre
        Return : This function returns a integer value "flag", which I used to show the final result.
        To be more specific, if flag is 0 that means that a folder where created and some files were organized otherwise do nothing.

    """
    flag = 0
    total = 0
    current_path = os.getcwd()
    extensions_found = []
    if current_path not in folder_exceptions:
        for i in os.listdir(current_path):
            if os.path.isfile(i):
                if exts.guess(i) not in extensions_found:
                    extensions_found.append(exts.guess(i))
                total += 1
        if total > 0:
            if not os.path.exists(main_folder):
                os.makedirs(main_folder)
            os.chdir(os.path.join(current_path, main_folder))
            create_one(extensions_found)
        else:
            flag = 1
            print("No files to organize!")
    else:
        flag = 1
        print("Access denied - You can not organize this folder!")
    return flag

def move_files(file, destination):
    """
    This is the function that move the files into their apropriate folder.
    It also replaces duplicated files.

    :param file: The file to be copied as a string type.
    :param destination: The name of the folder where the file must be copied, as string.

    - Return: This function does not return any value.
    """

    destin = os.path.join(os.getcwd(), main_folder, destination)
    source = os.path.join(os.getcwd(), file)
    try:
        if file in os.listdir(destin):
            os.unlink(os.path.join(destin, file))
            shutil.move(source, destin)
        else:
            shutil.move(source, destin)
    except BaseException as e:
        pass


def banner():
    print("""
    =====================================================================
    ======                POWFU - FILE ORGANIZER                   ======
    ======                  By. Antonio Pedro                      ======
    =====================================================================
    """)

def main():
    total_documents = 0
    total_music = 0
    total_videos = 0
    total_images = 0
    total_compacted = 0
    total_exe = 0
    total_others = 0
    total_files = 0

    flag = create_folders()
    banner()
    for file in os.listdir(os.getcwd()):
        if os.path.isdir(file):
            pass
        if os.path.isfile(file):
            extension = exts.guess(file)
            if file.endswith(extension):
                if exts.is_music(extension):
                    move_files(file, folders_name[0])
                    total_music += 1
                elif exts.is_image(extension):
                    move_files(file, folders_name[1])
                    total_images += 1
                elif exts.is_video(extension):
                    move_files(file, folders_name[2])
                    total_videos += 1
                elif exts.is_doc(extension):
                    move_files(file, folders_name[3])
                    total_documents += 1
                elif exts.is_compacted(extension):
                    move_files(file, folders_name[4])
                    total_compacted += 1
                elif exts.is_executable(extension):
                    if file == "PowFu-File Organizer.run":
                        pass
                    else:
                        move_files(file, folders_name[5])
                        total_exe += 1
                else:
                    move_files(file, folders_name[6])
                    total_others += 1
    total_files = total_compacted + total_documents + total_exe + total_images + total_videos + total_others

    if flag == 0:
        print("Total Number of file copied: %s" % total_files)
        print("Total Number of Documents copied: %s" % total_documents)
        print("Total Number of Musics copied: %s" % total_music)
        print("Total Number of Images copied: %s" % total_images)
        print("Total Number of Videos copied: %s" % total_videos)
        print("Total Number of Compacteds copied: %s" % total_compacted)
        print("Total Number of Programs copied: %s" % total_exe)
        print("Total Number of others file copied: %s" % total_others)
        print("Your Computer is organized now! Go to %s" % os.path.join(os.getcwd()), main_folder)

        time.sleep(3)

if __name__ == '__main__':
    os.chdir(os.path.join(os.getcwd(), ".."))
    main()
