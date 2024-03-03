import os

file_path = 'example2.txt'

if os.path.exists(file_path):
    os.remove(file_path)
