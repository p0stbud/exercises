# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.4 Detekcja typu pliku po zawartości


#!/usr/bin/env python3
import sys
import os
import re
from pygments.lexers import guess_lexer


patterns_A = {
    "C/C++": [
        "#include", 
        "#define"
    ],
    "PHP": [
        "<?php"
    ],
    "Python": [
        "def ", 
        "import "
    ],
    "HTML": [
        "<html", 
        "<body", 
        "<div"
    ]
}


patterns_B = {
    "C/C++": [
        r'^\s*#include\s*<.*>',
        r'^\s*#include\s*".*"',
        r'^\s*#define\s.*'
    ],
    "PHP": [
        r'^\s*<\?php',
        r'^\s*echo\s+["\'].*["\']\s*;',
        r'^\s*\$[a-zA-Z_]\w*\s*=',
        r'^\s*function\s+[a-zA-Z_]\w*\s*\('
    ],
    "Python": [
        r'^\s*def\s+[a-zA-Z_]\w*\s*\(',
        r'^\s*import\s+[a-zA-Z_][\w\.]*',
        r'^\s*from\s+[a-zA-Z_][\w\.]*\s+import\s+',
        r'^\s*class\s+[A-Za-z_]\w*\s*:',
        r'^\s*for\s+[a-zA-Z_]\w*\s+in\s+.*:'
    ],
    "HTML": [
        r'^\s*<!DOCTYPE\s+html',
        r'^\s*<html.*?>',
        r'^\s*<head.*?>',
        r'^\s*<body.*?>',
        r'^\s*<div.*?>',
        r'^\s*<span.*?>',
        r'^\s*<a\s+.*?>'
    ]
}

# Function checking if the file contains a specific pattern. This is "A" problem from the exercise.
def is_code(path):
    with open(path, 'rb') as f:
        # list of lines
        lol = f.readlines()
        for line in lol:
            if not line.strip():
                continue
            for lang, pattern in patterns_A.items():
                for p in pattern:
                    if p.encode() in line:
                        print(lang, os.path.basename(path), line.strip())
                        return lang


# Functions checking if the file contains a specific pattern using regex. This is "B" problem from the exercise.
def is_code_re(path):
    with open(path, 'rb') as f:
        # list of lines
        lol = f.readlines()
        for line in lol:
            if not line.strip():
                continue
            for lang, pattern in patterns_B.items():
                for p in pattern:
                    if re.match(p.encode(), line):
                        print(lang, os.path.basename(path), line.strip())
                        return lang
                    

def is_code_lexer(path):
    with open(path, 'rb') as f:
        content = f.read()
        lang = guess_lexer(content).name
        if any(lang in s for s in patterns_A.keys()):
            print(lang, os.path.basename(path))
            return lang


def recursive_detector(path):
    global program_lang
    dirlist = os.listdir(path)
    for e in dirlist:
        if os.path.isfile(os.path.join(path, e)):
            # Check using the "A" problem
            # if res := is_code(os.path.join(path, e)):
                # program_lang.add(res)
            # Check using the "B" problem
            # if res := is_code_re(os.path.join(path, e)):
                # program_lang.add(res)
            # Check using the "C" problem
            if res := is_code_lexer(os.path.join(path, e)):
                program_lang.add(res)
        else:
            recursive_detector(os.path.join(path, e))


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: lines_counter.py <path/file.py>")
    path = sys.argv[1]
    path = os.path.abspath(path)

    global program_lang
    program_lang = set()
    recursive_detector(path)
    print(program_lang)


if __name__ == '__main__':
    main()