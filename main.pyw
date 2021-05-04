import shutil, os, sys

'''
    This an utility script to help users organize their files without stress.
    It goes through a folder and check all files and organize them per type.
    Modules Used:
    shutil - provides utilities functions for copying, archiving files and directiry trees.
    os - it allows us to work with directories, files and so on.
    sys - This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.
'''
#Name of the folder where the files will be organized
main_folder = "PowFu - File Organizer" 
#names of the folders where each document will be moved to.
folders_name = ["1. Musics", "2. Images", "3. Videos", "4. Documents", "5. Zippers","6. Programs", "7. Others"]
#extensions for files of type image.
image_exts = [".jpg", ".jpeg", ".png",".ico", ".webp", ".jfif", ".gif"]
##extensions for files of type music.
music_exts = [".mp3", ".mp2",".wav" ]
#extensions for files of type document.
docs_exts  = [".pptx", ".pdf", ".txt", ".docx", ".xlsx", ".doc", ".csv", ".pub", ".rtf"]
#extensions for files of type videos.
videos_exts = [".mp4", ".avi", ".mpg", ".mkv",".3gp"]
#extensions for files of type compressed arquives.
compacted_exts = [".rar", ".zip", ".zp"]
#extensions for executables files.
exec_exts = [".exe"]
#this list will contain all extensions type by calling extend method
extensions = []
extensions.extend(image_exts)
extensions.extend(music_exts)
extensions.extend(docs_exts)
extensions.extend(videos_exts)

#below are totalizers variables, they will count the numbers of each type organized.
total_documents = 0
total_music = 0
total_videos = 0
total_images = 0
total_compacted = 0
total_exe= 0
total_others = 0
total_files = 0

def createFolders():
    """
        This is the function that creates a new folder named as 
        PowFu- files organizer if the script was never runned in the context folder.

        If the script has already ran into this folder or there are no files except "main.pyw" and "runner.bat",
        it will inform the user that there are no files to organize.

        Parametres : This function does not receive any parametre
        Return : This function return an integer value "flag", which I used to show the final result.
        To be more specific, if flag is 0 that means that a folder where created and some files were organized otherwise do nothing.

    """
    flag = 0 
    total = 0 #total of files on the current folder except the folders.
    
    for i in os.listdir(os.getcwd()):#Iterate through the folder
        if os.path.isfile(i): #If the i is file, add +1 to total
            total = total + 1
    if total > 2: #if total is greater than 2, it means that except the main.pyw, and runner.bat there are files to organize
        
        if os.path.exists(main_folder) == True: #if the the folder where we will organize already existis
            os.chdir(os.getcwd()+"\%s"%main_folder) #we will go into that folder
        else: #otherwise

            os.makedirs(main_folder) #create the folder
            os.chdir(os.getcwd()+"\%s"%main_folder) #go into the folder
            for folder in folders_name: #iterate through folders_name list and create all requerided folders.
                os.makedirs(folder)
    else: #otherwise
        flag = 1 
        print("No files to organize!")
    return flag

def moveFiles(file, destination):
    """
        This is the function that move the files into their apropriete folder. 

        It also replace duplicated files.

        Parametres : 
            File - The file to be copied as a string type.
            destination - The name of the folder where the file must be copied, as string.

        Return : This function does not return any value.
    """

    destin =  os.getcwd()+"\%s\%s"%(main_folder, destination)

    source = os.getcwd()+"\%s"%file #source path, in this case where the scrip will be executed
    try:
        #if the file is already in the folder, unlike it and move a new one.
        if file in os.listdir(destin):
            os.unlink(destin+"\%s"%file)
            shutil.move(source, destin)
        else: #otherwise just move it
            shutil.move(source, destin)
    except BaseException:
        pass

flag = createFolders() #here we instance a variable name as flag and consequentily call the createFolder function
os.chdir(os.getcwd()+"\..") #After create the folder, the current path will be PowFu..., then this line get out of this folder and go to the previous folder

for file in os.listdir(os.getcwd()): #iterate again all the files
    if os.path.isdir(file): #if it is folder, skip it. 
        pass
    if os.path.isfile(file): #if it is a file
        extension = os.path.splitext(file)[-1] #get the extension of the folder.
        #the os.path.splittext() method return a tuple of a path like ("C", "Users", "AntonioDev", "somefile", ".extension of the file")
        #the we only use the last element of this tuple because it will always be the extension
        if file.endswith(extension): #if the current file ends with some extension
            if extension in music_exts: #if the extension is in musics extension list
                moveFiles(file, folders_name[0]) #move the file into the first folders created to save musics
                total_music = total_music + 1 #add 1 to total music.
            #the same happens for others files found.
            elif extension in image_exts:
                moveFiles(file, folders_name[1])
                total_images = total_images + 1
            elif extension in videos_exts:
                moveFiles(file, folders_name[2])
                total_videos = total_videos + 1
            elif extension in docs_exts:
                moveFiles(file, folders_name[3])
                total_documents = total_documents + 1
            elif extension in compacted_exts:
                moveFiles(file, folders_name[4])
                total_compacted = total_compacted + 1
            elif extension in exec_exts:
                moveFiles(file, folders_name[5])
                total_exe = total_exe + 1
            else: #it is a special case, that indicates that the 
                  #current file's extension, is not in any extension list we have created
                  #then move it to Others folder if the file is not main.pyw or runner.bat
                if file == "main.pyw" or file =="runner.bat":
                    pass
                else:
                    moveFiles(file,folders_name[6])
                    total_others = total_others + 1

#calculate the total of files organized!
total_files = total_compacted + total_documents + total_exe + total_files + total_images + total_images + total_videos

if flag == 0: #if flag is equal to zero, then we have complete all the task sucessfully, show the results to the user.
    print("==============RESULTS========================")
    print("Total Number of file copied: %s"%total_files)
    print("Total Number of Documents copied: %s"%total_documents)
    print("Total Number of Musics copied: %s"%total_music)
    print("Total Number of Images copied: %s"%total_images)
    print("Total Number of Videos copied: %s"%total_videos)
    print("Total Number of Compacteds copied: %s"%total_compacted)
    print("Total Number of Programs copied: %s"%total_exe)
    print("Total Number of others file copied: %s"%total_others)
    print("Your Computer is organized now! Go to %s"%os.getcwd()+"\%s"%main_folder)
    

