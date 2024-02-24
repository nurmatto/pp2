def nurma_generator(x):
    for i in range(1,x+1):
        yield (i*i)
n = int(input())
list_of_numbers = list(nurma_generator(n))

for i in list_of_numbers:
    print(i, end=' ')