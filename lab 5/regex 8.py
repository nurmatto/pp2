import re

nuraa = "NurmaIsNumberOne"

sozder = re.findall(r'[A-Z][^A-Z]*', nuraa)
print(sozder)