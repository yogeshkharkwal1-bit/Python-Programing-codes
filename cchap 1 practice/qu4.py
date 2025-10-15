# Qu 4 is a Python program to display the content of a directory using the os module.
import os

path = '/chap 1'  # Replace with your target directory
try:
    entries = os.listdir(path)
    print(f"Contents of '{path}':")
    for entry in entries:
        print(entry)
except OSError as e:
    print(f"Error accessing {path}: {e}")
