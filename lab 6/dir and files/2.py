import os

path = os.getcwd()

existance_access = os.access(path, mode=os.F_OK)
reading_access = os.access(path, mode=os.R_OK)
writing_access = os.access(path, mode=os.W_OK)
executability_access = os.access(path, mode=os.X_OK)

print(f"Path accessibility: Existance: {existance_access}, Reading: {reading_access}, Writing: {writing_access}, Executability: {executability_access}")
