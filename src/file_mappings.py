# Here are the custom mappings:
# They are very easily extendable
# Now, let's run the file organiser...

FOLDER_TO_EXTENSIONS = {
    "images": [".jpg", ".jpeg", ".png", ".svg", ".webp", ".raw", ".tiff", ".heic", ".gif"],
    "documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".md", ".txt"],
    "audio": [".mp3", ".wav"],
    "videos": [".mp4", "mov", "mkv"],
    "archives": [".zip", ".rar", ".tar"]
}



FILE_EXTENSION_TO_FOLDER = {
    ext: folder

    for (folder, extension) in FOLDER_TO_EXTENSIONS.items()
        for ext in extension
}