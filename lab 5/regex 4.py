import re

nurma = re.compile(r"[A-Z]{1}[a-z]+")
print(nurma.findall("Nurmukhamed is best programer"))