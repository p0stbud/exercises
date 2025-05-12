# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.2 Liczenie linii w pliku

#This script counts the number of lines in a file using two different methods:

#!/usr/bin/env python3
import sys
    

# The first method uses the readlines() function to read all lines into a list and then counts the number of non-empty lines that do not start with a comment (#).
def counter_readlines(path):
    with open(path, "r") as f:
        # list of lines
        lol = f.readlines()
        return len([l for l in lol if l.strip() and l.strip()[0] != '#'])


# The second method reads the file in binary mode and splits the content by line endings (EOL) to count the number of non-empty lines that do not start with a comment (#).
def counter_EOL(path):
    # open file in binary mode
    with open(path, "rb") as f:
        content = f.read()
        # list of lines
        # split by EOL
        lol = content.split(b'\x0a')
        return len([l for l in lol if l.strip() and l.strip()[0:1] != b'\x23'])


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: lines_counter.py <path/file.py>")
    path = sys.argv[1]
    len_readlines = counter_readlines(path)
    len_EOL = counter_EOL(path)
    print(len_readlines,
          len_EOL, sep='\n')


if __name__ == '__main__':
    main()