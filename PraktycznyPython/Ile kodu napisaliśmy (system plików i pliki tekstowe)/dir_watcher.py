# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.5 Obserwowanie katalogu

# This script monitors a directory for changes to files and directories.
# It uses two methods:
# A) Active polling
# B) Watchdog library

# #!/usr/bin/env python3
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# cache is a dictionary that stores the last modification time of files used in active polling
cache = {}


# This class handles file system events.
class ObserverHandler(FileSystemEventHandler):
    def watch_modified(self, event):
        if not event.is_directory:
            print(f"File {event.src_path} has been modified")
        else:
            print(f"Directory {event.src_path} has beed modified")


# This function uses active polling to check if a file has been modified.
# It compares the last modification time of the file with the cached value.
def active_polling(path, file_name):
    global cache
    file_path = os.path.join(path, file_name)
    if file_name in cache:
        # Check if the file has been modified
        if os.stat(file_path).st_mtime != cache[file_name]:
            print(f"File {file_name} has been modified")
            # Update the cache
            cache[file_name] = os.stat(file_path).st_mtime
    else:
        # Add the file to the cache
        cache[file_name] = os.stat(file_path).st_mtime
        print(f"File {file_name} added to cache")


# This function recursively walks through the directory and its subdirectories.
def recursive_walk(path):
    global cache
    dirlist = os.listdir(path)
    for e in dirlist:
        if os.path.isfile(os.path.join(path, e)):
            active_polling(path, e)
        else:
            recursive_walk(os.path.join(path, e))


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: dir_watcher.py <path/file.py>")
    path = sys.argv[1]
    
    event_handler = ObserverHandler()
    observer = Observer()
    # schedule the event handler to watch the specified path
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            # recursive_walk(path)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    # observer.join() ensures that the observer thread is properly cleaned up
    observer.join()


if __name__ == '__main__':
    main()