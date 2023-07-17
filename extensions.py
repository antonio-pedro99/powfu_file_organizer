"""
    This module contains all functions and variables needed to handle extensions.
"""

import os

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

docs_exts = [
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
        This function gess the extension of any file
    """
    return os.path.splitext(file)[-1]


def get_all():
    """
        This function returns a list of all extensions.
    """
    extensions = []

    extensions.extend(image_exts)
    extensions.extend(music_exts)
    extensions.extend(docs_exts)
    extensions.extend(videos_exts)

    return extensions


def is_music(extension):
    res = False
    if extension in music_exts:
        res = True
    return res


def is_image(extension):
    res = False
    if extension in image_exts:
        res = True
    return res


def is_video(extension):
    res = False
    if extension in videos_exts:
        res = True
    return res


def is_doc(extension):
    res = False
    if extension in docs_exts:
        res = True
    return res


def is_compacted(extension):
    res = False
    if extension in compacted_exts:
        res = True
    return res


def is_executable(extension):
    res = False
    if extension in exec_exts:
        res = True
    return res


def is_iso(extension):
    res = False
    if extension in iso_exts:
        res = True
    return res
