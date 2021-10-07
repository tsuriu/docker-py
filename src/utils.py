import os
import csv

def calculate_files_size(path):
    size = 0

    for path, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    return "{:.2f}".format(size / (1024 ^2))

    