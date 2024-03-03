import os

path = os.getcwd()

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
all_elements = os.listdir(path)

print(f"Files: {files}, directories: {directories}, all elements: {all_elements}")
