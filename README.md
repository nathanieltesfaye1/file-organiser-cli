# File Organiser CLI Tool

A Python script that automatically organises messy folders by file type (e.g. '.jpg' files -> '/images/' folder). Very easy to add custom mappings for new file/folder combinations.

This project was built to solve a real-world problem, that being my chronically messy, horrifically unorganised Downloads folder. 

## Example Usage
[Here's an example of the tool in action.](https://drive.google.com/file/d/1ClfPLPgF3NxxVimzdNthW6qdreEXhwHL/view?usp=sharing)

## How it's Made

**Tech used**: Python3, pathlib, shutil

**Python** was chosen due to it's built-in tools for file operations (e.g. pathlib + shutil).

'**pathlib**' is used for cross-platform path handling, and '**shutil**' safely moves files between folders.

## Key Features
* Folders are only created for files that actually exist.
* Permissions are handled elegantly.
* Potential errors are handled gracefully.
* Files get auto-renamed if there already exists a file in the new folder with the same name.# file-organiser-cli
