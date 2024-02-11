from itertools import permutations

your_string=input()
def printer_permutator():
    perms = permutations(your_string)
    for permuts in perms:
        print(permuts)
printer_permutator()