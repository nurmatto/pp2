import re

soz = "WhatIfIWillTheBestInThingsWhichILove?"
sozder = re.findall(r'[A-Z][^A-Z]*', soz)
soz_2 = ' '.join(sozder)
print(soz_2)