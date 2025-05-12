# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.1 Listowanie zawartości katalogu

# This script counts the number of files in a directory and its subdirectories
# using three different methods: os.walk, recursive directory listing, and pathlib.
# It also skips hidden files and directories (those starting with a dot).

#!/usr/bin/env python3
import sys
import os
import pathlib


# This function uses os.walk to traverse the directory tree and count files.
def os_walk(path):
    global total
    
    for root, dirs, files in os.walk(path):
        splited_root = root.split(os.path.sep)
        if any([hiden for hiden in splited_root if hiden.startswith(".")]):
            continue
        for file in files:
            if file.startswith("."):
                continue
            total += 1
            # print(total, file)


# This function uses a recursive approach to traverse the directory tree and count files.
def recursive_walk(path):
    global total

    for element in os.listdir(path):
        if element.startswith("."):
            pass
        elif os.path.isfile(os.path.join(path, element)):
            total+=1
            # print(total, element)
        else: # os.path.isdir(os.path.join(path, element)):
            recursive_walk(os.path.join(path, element))


# This function uses pathlib to traverse the directory tree and count files.
# It uses the rglob method to find all files recursively.
def pathlib_walk(path):
    global total

    path_generator = pathlib.Path(path).rglob("*")
    for root in path_generator:
        splited_root = str(root).split(os.path.sep)
        if any([hiden for hiden in splited_root if hiden.startswith(".")]):
            continue
        if os.path.isfile(root):
            total += 1


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: walk.py <path>")

    path = sys.argv[1]
    # print(f"Path: {path}")

    # Ensure the path is absolute for passing hiden files and directories
    # to the walk functions
    path = os.path.abspath(path)

    global total

    total = 0
    os_walk(path)
    print(total)

    total = 0
    recursive_walk(path)
    print(total)

    total = 0
    pathlib_walk(path)
    print(total)


if __name__ == '__main__':
    main()