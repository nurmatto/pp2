import os

input_list = input().split()

with open('examplefile.txt', 'w') as file:
    for item in input_list:
        file.write(str(item) + ' ')
