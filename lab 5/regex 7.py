import re

def snakeToCamel(text):
    sozder = text.split('_')
    camel_str = sozder[0]
    for char in sozder[1:]:
        camel_str += char.capitalize()
    return camel_str

nura = "shake_case_str"
print(snakeToCamel(nura))


    