import os

file_path = 'examplefile.txt'

if os.path.isfile(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    print(f"Number of lines in '{file_path}': {line_count}")
else:
    print(f"'{file_path}' does not exist.")
