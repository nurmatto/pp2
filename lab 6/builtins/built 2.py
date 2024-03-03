nurma = input()

number_lower_case = 0
number_upper_case = 0

for i in nurma:
    if 97 <= ord(i) <= 122:
        number_lower_case += 1
    elif 65 <= ord(i) <= 90:
        number_upper_case += 1

print('Number of lowercase letters:', number_lower_case)
print('Number of uppercase letters:', number_upper_case)
