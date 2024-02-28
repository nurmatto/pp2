import re

text = "Hey everyone i am nurma"
text_2 = re.sub(r'[ ,.]', ':', text)
print(text_2)