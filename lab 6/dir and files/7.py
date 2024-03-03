import os

with open('examplefile.txt', 'r') as source_file:
    with open('examplefile_copy.txt', 'w') as target_file:
        for line in source_file:
            target_file.write(line)
