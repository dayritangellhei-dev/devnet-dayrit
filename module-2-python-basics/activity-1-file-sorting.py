"""
Module 2 — Activity: File Sorting with os and shutil
Student: Angel Lhei D. Dayrit
Date: 10/3/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module: A built-in Python module that lets your program interact 
  with the operating system.
- shutil module: A module used for high-level file operations like 
  moving, copying, or deleting files and directories.
- file path: The exact address or location of a file or folder in 
  your computer's storage system.
- directory: The technical name for a folder on a computer.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

list_of_files = os.listdir()
print(list_of_files)

folder_path = input("Enter the folder path: ")

if os.path.exists('file.txt'):
    print("The file exists!")
else:
    print("The file does not exist.")

os.mkdir("image") 
os.mkdir("documents")
os.mkdir("videos")
os.mkdir("others") 



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
