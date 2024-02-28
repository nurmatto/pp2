import re

nurma = re.compile(r'a.*b$')
print(nurma.findall("am I the best ever?b"))