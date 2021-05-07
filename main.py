import shutil, os, time
import extensions as exts

'''
    This a utility script to help users organize their files without stress.
    It goes through a folder and check all files and organize them per type.
    Modules Used:
    shutil - provides utilities functions for copying, archiving files and directiry trees.
    os - it allows us to work with directories, files and so on.
    sys - This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.
'''

main_folder = "PowFu - File Organizer" 
extensions = exts.getAll

folders_name = [
    "1. Musics", 
    "2. Images", 
    "3. Videos", 
    "4. Documents", 
    "5. Zippers",
    "6. Programs", 
    "7. Others"]


def createFolders():
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
  
    for i in os.listdir(os.getcwd()):
        if os.path.isfile(i): 
            total = total + 1
    if total > 0: 
        if os.path.exists(main_folder) == True: 
            os.chdir(os.path.join(os.getcwd(), main_folder)) 
        else: 
            os.makedirs(main_folder) 
            os.chdir(os.path.join(os.getcwd(), main_folder)) 
            for folder in folders_name: 
                os.makedirs(folder)
    else: 
        flag = 1 
        print("No files to organize!")
    return flag

def moveFiles(file, destination):
    """
        This is the function that move the files into their apropriete folder. 

        It also replaces duplicated files.

        Parametres : 
            File - The file to be copied as a string type.
            destination - The name of the folder where the file must be copied, as string.

        Return : This function does not return any value.
    """

    destin =  os.path.join(os.getcwd(), main_folder, destination )
    source =  os.path.join(os.getcwd(), file) 
    try:
        if file in os.listdir(destin):
            os.unlink(os.path.join(destin, file))
            shutil.move(source, destin)
        else: 
            shutil.move(source, destin)
    except BaseException as e:
        pass


def main():

    total_documents = 0
    total_music = 0
    total_videos = 0
    total_images = 0
    total_compacted = 0
    total_exe= 0
    total_others = 0
    total_files = 0

    for file in os.listdir(os.getcwd()): 
        if os.path.isdir(file): 
            pass
        if os.path.isfile(file): 
            extension = exts.guess(file)
            if file.endswith(extension): 
                if exts.isMusic(extension):
                    moveFiles(file, folders_name[0]) 
                    total_music = total_music + 1
                elif exts.isImage(extension):
                    moveFiles(file, folders_name[1])
                    total_images = total_images + 1
                elif exts.isVideo(extension):
                    moveFiles(file, folders_name[2])
                    total_videos = total_videos + 1
                elif exts.isDoc(extension):
                    moveFiles(file, folders_name[3])
                    total_documents = total_documents + 1
                elif exts.isCompacted(extension):
                    moveFiles(file, folders_name[4])
                    total_compacted = total_compacted + 1
                elif exts.isExecutable(extension):
                    if file == "PowFu-File Organizer.exe" or file ==  "PowFu-File Organizer.bin" or file == "PowFu-File Organizer.run" : 
                        pass
                    else:
                        moveFiles(file, folders_name[5])
                        total_exe = total_exe + 1
                else: 
                    moveFiles(file,folders_name[6])
                    total_others = total_others + 1
    total_files = total_compacted + total_documents + total_exe + total_images + total_videos + total_others

    if flag == 0: 
        
        print("============== RESULTS ========================")
        print("Total Number of file copied: %s"%total_files)
        print("Total Number of Documents copied: %s"%total_documents)
        print("Total Number of Musics copied: %s"%total_music)
        print("Total Number of Images copied: %s"%total_images)
        print("Total Number of Videos copied: %s"%total_videos)
        print("Total Number of Compacteds copied: %s"%total_compacted)
        print("Total Number of Programs copied: %s"%total_exe)
        print("Total Number of others file copied: %s"%total_others)
        print("Your Computer is organized now! Go to %s"%os.path.join(os.getcwd()), main_folder)
        
        time.sleep(3)


if __name__ == '__main__':
    flag = createFolders() 
    os.chdir(os.path.join(os.getcwd(), "..")) 
    main()
    