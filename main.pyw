import shutil, os

main_folder = "PowFu - File Organizer"

folders_name = ["1. Musics", "2. Images", "3. Videos", "4. Documents", "5. Zippers","6. Programs", "7. Others"]
image_exts = [".jpg", ".jpeg", ".png",".ico", ".webp", ".jfif", ".gif"]
music_exts = [".mp3", ".mp2",".wav" ]
docs_exts  = [".pptx", ".pdf", ".txt", ".docx", ".xlsx", ".doc", ".csv", ".pub", ".rtf"]
videos_exts = [".mp4", ".avi", ".mpg", ".mkv",".3gp"]
compacted_exts = [".rar", ".zip", ".zp"]
exec_exts = [".exe"]

extensions = []
extensions.extend(image_exts)
extensions.extend(music_exts)
extensions.extend(docs_exts)
extensions.extend(videos_exts)

total_documents = 0
total_music = 0
total_videos = 0
total_images = 0
total_compacted = 0
total_exe= 0
total_others = 0
total_files = 0

def createFolders():
    flag = 0
    total = 0
    for i in os.listdir():
        if os.path.isfile(i):
            total = total + 1
    if total > 2:
        if os.path.exists(main_folder) == True:
            # os.makedirs(main_folder)
            # os.chdir(os.getcwd()+"\%s"%main_folder)
            # for folder in folders_name:
            #     os.makedirs(folder)
            os.chdir(os.getcwd()+"\%s"%main_folder)
        else:
            os.makedirs(main_folder)
            os.chdir(os.getcwd()+"\%s"%main_folder)
            for folder in folders_name:
                os.makedirs(folder)
            # flag = 1
            # print("It looks like this folder is already organized or there is a folder named as %s please try to rename that folder and try again|"%main_folder)
    else:
        flag = 1
        print("No files to organize!")
    return flag
def moveFiles(file, destination):
    shutil.move(os.getcwd()+"\%s"%file, os.getcwd()+"\%s\%s"%(main_folder, destination))
flag = createFolders()
os.chdir(os.getcwd()+"\..")
for file in os.listdir():
    if os.path.isdir(file):
        pass
    if os.path.isfile(file):
        extension = os.path.splitext(file)[-1]
        if file.endswith(extension):
            if extension in music_exts:
                moveFiles(file, folders_name[0])
                total_music = total_music + 1
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
            else:
                if file == "main.pyw" or file =="runner.bat":
                    pass
                else:
                    moveFiles(file,folders_name[6] )
                    total_others = total_others + 1
total_files = total_compacted + total_documents + total_exe + total_images + total_images + total_videos + total_others

if flag == 0:
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
    

