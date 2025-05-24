# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.6 Skrypt odpalany co jakiś czas

# This script is a simple cron job that appends the current date and time to a file.
# It is intended to be run periodically by a cron job.
# On MacOS and Linux, you can set up a cron job to run this script every 30 minutes.
# crontab -e
# */0.5 * * * * /usr/bin/python3 /path/to/crontab_worker.py /path/to/file.txt

#!/usr/bin/env python3
import sys
import os
from datetime import datetime


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: crontab_worker.py <path>")
    path = sys.argv[1]
    print(path)
    if os.path.isfile(path):
        with open(path, "a") as f:
            now = datetime.now()
            formatted = now.strftime("%A, %d %B %Y, %H:%M:%S")
            f.write(f"{formatted}\n")
            print(formatted)
    else:
        print(f"{path} is a directory")


if __name__ == '__main__':
    main()