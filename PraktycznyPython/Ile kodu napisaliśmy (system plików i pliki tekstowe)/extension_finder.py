# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.3 Kolekcjonujemy rozszerzenia

#This script recursively walks through a directory and collects unique file extensions from the files it finds.

#!/usr/bin/env python3
import sys
import os


# This function recursively walks through a directory and collects file names in a global list.
def recursive_walk(path):
    global files
    for e in os.listdir(path):
        if os.path.isfile(os.path.join(path, e)):
            files.append(e)
        else: # os.path.isdir(os.path.join(path, e)):
            recursive_walk(os.path.join(path, e))


# This function takes a list of file names and collects unique file extensions, ignoring files that start with a dot.
def find_unique_extension(files):
    unique_ext = set()
    for file in files:
        if file.startswith('.'):
            continue
        name, ext = file.split('.')
        unique_ext.add('.' + ext)
    print(unique_ext)



def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: extension_finder.py <path>")
    path = sys.argv[1]
    path = os.path.abspath(path)

    global files
    files = list()
    recursive_walk(path)
    find_unique_extension(files)


if __name__ == '__main__':
    main()