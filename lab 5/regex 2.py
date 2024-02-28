import re

def searcher(string):
    nurma = r'ab{2,3}'
    if re.match(nurma, string):
        return True
    else:
        return False

s = str(input())
print(searcher(s))