import os, sys, filecmp
"""
    This module contains all functions and variables needed to handle extensions.
"""

image_exts = [
    ".jpg", 
    ".jpeg",
    ".png",
    ".heic", 
    ".webp",
    ".jpe", 
    ".jfif", 
    ".tif", 
    ".tiff", 
    ".gif",
    ".bmp",
    ".dib",
    ".ico"]


music_exts = [
    ".mp3", 
    ".mp2",
    ".wav",
    ".m4a",
    ".MP3"]

docs_exts  = [
    ".pptx", 
    ".pdf", 
    ".txt", 
    ".docx", 
    ".xlsx", 
    ".doc", 
    ".csv", 
    ".pub", 
    ".rtf"]

videos_exts = [
    ".mp4", 
    ".avi", 
    ".mpg", 
    ".mkv",
    ".3gp",
    ".MP4",
    ".wmv"
    ]

compacted_exts = [
    ".rar", 
    ".zip", 
    ".7z"]

exec_exts = [
    ".exe", 
    ".EXE", 
    ".bin"]

iso_exts = [
    ".iso",
    ]


def guess(file):
    """
        This function gets the extension of any file
    """
    return os.path.splitext(file)[-1]

def getAll():

    """
        This function returns a list of all extensions.
    """
    extensions = []
    
    extensions.extend(image_exts)
    extensions.extend(music_exts)
    extensions.extend(docs_exts)
    extensions.extend(videos_exts)

    return extensions

def isMusic(extension):

    res = False
    if extension in music_exts:
        res = True
    return res

def isImage(extension):
    res = False
    if extension in image_exts:
        res = True
    return res   

def isVideo(extension):
    res = False
    if extension in videos_exts:
        res = True
    return res

def isDoc(extension):
    res = False
    if extension in docs_exts:
        res = True
    return res

def isCompacted(extension):
    res = False
    if extension in compacted_exts:
        res = True
    return res

def isExecutable(extension):
    res = False
    if extension in exec_exts:
        res = True
    return res

def isIso(extension):
    res = False
    if extension in iso_exts:
        res = True
    return res