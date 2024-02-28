import re

def ptrn(str):
    nurma = r'ab*'
    if re.match(nurma, str):
        return True
    else:
        return False

s = s(input())
print(ptrn(str))